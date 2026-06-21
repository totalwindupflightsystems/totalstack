---
id: "@specs/aws/rekognition/plan"
target_lang: plan
version: 1.0.0
owned-by: specwriter
status: active
depends_on:
  - "@specs/aws/rekognition"
---

# Amazon Rekognition — Implementation Plan

## Operations Covered (30 core operations)

### Collection Management (4)
- `CreateCollection`, `DeleteCollection`, `DescribeCollection`, `ListCollections`

### Face Operations (5)
- `IndexFaces`, `ListFaces`, `DeleteFaces`, `SearchFaces`, `SearchFacesByImage`

### Image Detection — Synchronous (7)
- `DetectFaces`, `DetectLabels`, `DetectModerationLabels`, `DetectText`
- `RecognizeCelebrities`, `CompareFaces`, `DetectProtectiveEquipment`

### Video Analysis — Asynchronous (10)
- `StartFaceDetection`, `GetFaceDetection`
- `StartLabelDetection`, `GetLabelDetection`
- `StartContentModeration`, `GetContentModeration`
- `StartTextDetection`, `GetTextDetection`
- `StartCelebrityRecognition`, `GetCelebrityRecognition`

### Celebrity (1)
- `GetCelebrityInfo`

### Tags (3)
- `TagResource`, `UntagResource`, `ListTagsForResource`

## Error Model

| Exception | HTTP | AWS Error Code |
|-----------|------|----------------|
| `InvalidParameterException` | 400 | InvalidParameterException |
| `ResourceNotFoundException` | 404 | ResourceNotFoundException |
| `AccessDeniedException` | 403 | AccessDeniedException |
| `ProvisionedThroughputExceededException` | 400 | ProvisionedThroughputExceededException |
| `ResourceInUseException` | 409 | ResourceInUseException |
| `ThrottlingException` | 429 | ThrottlingException |
| `InternalServerException` | 500 | InternalServerError |
| `ServiceQuotaExceededException` | 400 | ServiceQuotaExceededException |
| `InvalidImageFormatException` | 400 | InvalidImageFormatException |
| `ImageTooLargeException` | 400 | ImageTooLargeException |
| `VideoTooLargeException` | 400 | VideoTooLargeException |
| `HumanLoopQuotaExceededException` | 400 | HumanLoopQuotaExceededException |

## Store Architecture

```python
class RekognitionStore:
    collections: dict[str, CollectionRecord]      # CollectionId → record
    faces: dict[str, FaceRecord]                   # FaceId → record (faces belong to a collection)
    collection_faces: dict[str, set[str]]          # CollectionId → set of FaceIds
    video_jobs: dict[str, VideoJobRecord]          # JobId → record
    stream_processors: dict[str, StreamProcessorRecord]  # Name → record
    users: dict[str, UserRecord]                   # UserId → record (users belong to a collection)
    collection_users: dict[str, set[str]]          # CollectionId → set of UserIds
    celebrity_db: dict[str, CelebrityRecord]       # CelebrityId → record (pre-populated)
    tags: dict[str, dict[str, str]]               # ResourceArn → {Key: Value}
```

## Mock Data Strategy
- Face bounding boxes: deterministic based on face count
- Labels: return standard set of labels with confidence scores
- Moderation labels: return safe content by default
- Celebrity matches: return a small set of fake celebrities
- Video jobs: complete immediately with deterministic results
