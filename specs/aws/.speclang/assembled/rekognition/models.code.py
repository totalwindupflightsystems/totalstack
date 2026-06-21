# spec:trace: aws/rekognition/rekognition.spec.plan.md#implementation
# spec:id: @specs/aws/rekognition/plan
# spec:generated: DO NOT EDIT — edit the spec instead
"""Rekognition store and exception classes for greenfield TotalStack service."""

import time
import uuid
from typing import Any


# ── Exception Classes ──

class InvalidParameterException(Exception):
    """HTTP 400 - Invalid parameter."""
    pass


class ResourceNotFoundException(Exception):
    """HTTP 404 - Resource not found."""
    pass


class AccessDeniedException(Exception):
    """HTTP 403 - Access denied."""
    pass


class ProvisionedThroughputExceededException(Exception):
    """HTTP 400 - Throughput exceeded."""
    pass


class ResourceInUseException(Exception):
    """HTTP 409 - Resource in use (e.g., duplicate collection)."""
    pass


class ThrottlingException(Exception):
    """HTTP 429 - Rate limit exceeded."""
    pass


class InternalServerException(Exception):
    """HTTP 500 - Internal server error."""
    pass


class ServiceQuotaExceededException(Exception):
    """HTTP 400 - Service quota exceeded."""
    pass


class InvalidImageFormatException(Exception):
    """HTTP 400 - Invalid image format."""
    pass


class ImageTooLargeException(Exception):
    """HTTP 400 - Image too large."""
    pass


class VideoTooLargeException(Exception):
    """HTTP 400 - Video too large."""
    pass


class HumanLoopQuotaExceededException(Exception):
    """HTTP 400 - Human loop quota exceeded."""
    pass


class InvalidS3ObjectException(Exception):
    """HTTP 400 - Unable to access S3 object."""
    pass


class IdempotentParameterMismatchException(Exception):
    """HTTP 400 - Idempotent parameter mismatch."""
    pass


class LimitExceededException(Exception):
    """HTTP 400 - Limit exceeded."""
    pass


class InvalidPaginationTokenException(Exception):
    """HTTP 400 - Invalid pagination token."""
    pass


# ── Data Records ──

class CollectionRecord:
    """Represents a Rekognition collection."""
    def __init__(self, collection_id: str):
        self.CollectionId = collection_id
        self.FaceCount = 0
        self.CreatedTimestamp = time.time()
    
    def to_dict(self):
        return {
            "CollectionId": self.CollectionId,
            "FaceCount": self.FaceCount,
            "CreatedTimestamp": self.CreatedTimestamp,
        }


class FaceRecord:
    """Represents an indexed face."""
    def __init__(self, face_id: str, image_id: str = "", bounding_box: dict = None, 
                 external_image_id: str = "", confidence: float = 99.0):
        self.FaceId = face_id
        self.ImageId = image_id
        self.BoundingBox = bounding_box or {"Width": 0.3, "Height": 0.4, "Left": 0.2, "Top": 0.1}
        self.ExternalImageId = external_image_id
        self.Confidence = confidence


class VideoJobRecord:
    """Represents an async video analysis job."""
    def __init__(self, job_id: str, api: str, video: dict = None):
        self.JobId = job_id
        self.Status = "SUCCEEDED"
        self.API = api
        self.Video = video or {}
        self.CreatedTimestamp = time.time()
        self.Results = []


class UserRecord:
    """Represents a user in a collection."""
    def __init__(self, user_id: str):
        self.UserId = user_id
        self.CreatedTimestamp = time.time()
        self.FaceId = ""


# ── Mock Data Generators ──

def _generate_mock_face(face_id: str = None, index: int = 0):
    """Generate a deterministic mock face record."""
    fid = face_id or str(uuid.uuid4())[:8]
    return {
        "FaceId": fid,
        "BoundingBox": {
            "Width": 0.3,
            "Height": 0.4,
            "Left": 0.2 + (index * 0.1),
            "Top": 0.1
        },
        "Confidence": 99.0 - (index * 0.5),
        "Landmarks": [
            {"Type": "eyeLeft", "X": 0.3 + (index * 0.05), "Y": 0.2},
            {"Type": "eyeRight", "X": 0.5 + (index * 0.05), "Y": 0.2},
            {"Type": "nose", "X": 0.4 + (index * 0.05), "Y": 0.3},
            {"Type": "mouthLeft", "X": 0.35 + (index * 0.05), "Y": 0.45},
            {"Type": "mouthRight", "X": 0.45 + (index * 0.05), "Y": 0.45},
        ],
        "Emotions": [
            {"Type": "HAPPY", "Confidence": 85.0},
            {"Type": "CALM", "Confidence": 75.0},
        ],
        "AgeRange": {"Low": 25, "High": 35},
        "Gender": {"Value": "Male", "Confidence": 90.0},
        "Smile": {"Value": True, "Confidence": 95.0},
    }


def _generate_mock_label(index: int = 0):
    """Generate a deterministic mock label."""
    label_names = ["Person", "Human", "Face", "Clothing", "Apparel",
                   "Car", "Vehicle", "Building", "Tree", "Plant",
                   "Animal", "Dog", "Cat", "Food", "Furniture"]
    return {
        "Name": label_names[index % len(label_names)],
        "Confidence": 99.0 - (index * 0.3),
        "Instances": [],
        "Parents": [],
    }


def _generate_mock_celebrity(index: int = 0):
    """Generate a mock celebrity record."""
    celeb_names = ["Celebrity Alpha", "Celebrity Beta", "Celebrity Gamma",
                   "Celebrity Delta", "Celebrity Epsilon"]
    return {
        "Name": celeb_names[index % len(celeb_names)],
        "Id": f"celebrity-{index + 1}",
        "Urls": [f"https://www.imdb.com/name/nm{1000000 + index:07d}"],
        "MatchConfidence": 99.0 - (index * 0.5),
        "Face": _generate_mock_face(f"celeb-face-{index}", index),
        "KnownGender": {"Type": "Male" if index % 2 == 0 else "Female"},
    }


# ── Main Store ──

class RekognitionStore:
    """Complete Rekognition emulator store — dict-backed, no external dependencies."""
    
    def __init__(self):
        self.collections: dict = {}           # CollectionId → CollectionRecord/ dict
        self.faces: dict = {}                 # FaceId → FaceRecord / dict
        self.collection_faces: dict = {}      # CollectionId → set of FaceIds
        self.collection_users: dict = {}      # CollectionId → set of UserIds
        self.video_jobs: dict = {}            # JobId → VideoJobRecord / dict
        self.users: dict = {}                 # UserId → UserRecord / dict
        self.celebrity_db: dict = self._init_celebrities()
        self.tags: dict = {}                  # ResourceArn → {Key: Value}
    
    @staticmethod
    def _init_celebrities():
        """Pre-populate celebrity database with mock data."""
        celebs = {}
        for i in range(5):
            c = _generate_mock_celebrity(i)
            celebs[c["Id"]] = c
        return celebs
