---
id: "@specs/aws/rekognition"
target_lang: meta
version: 1.0.0
owned-by: specwriter
status: active
---

# Amazon Rekognition Service — Meta Specification

## Why
Amazon Rekognition provides deep learning-based image and video analysis. It detects objects, scenes, faces, text, and unsafe content in images and videos. This TotalStack emulator provides an offline-compatible store-backed implementation for local development and testing.

## Service Architecture
Rekognition spans several domains:
- **Collections**: Persistent face storage (CreateCollection, DeleteCollection, ListCollections, DescribeCollection)
- **Faces**: Face indexing and search within collections (IndexFaces, ListFaces, DeleteFaces, SearchFaces, SearchFacesByImage)
- **Image Detection**: Synchronous analysis of single images (DetectFaces, DetectLabels, DetectModerationLabels, DetectText, RecognizeCelebrities, CompareFaces, DetectProtectiveEquipment)
- **Video Detection**: Asynchronous analysis of stored videos in S3 (Start/Get for FaceDetection, LabelDetection, ContentModeration, TextDetection, CelebrityRecognition, FaceSearch, PersonTracking, SegmentDetection)
- **Stream Processors**: Real-time video stream analysis (Create, Start, Stop, Delete, List, Describe, Update)
- **Users**: User management within collections (CreateUser, DeleteUser, ListUsers)
- **Celebrity**: Celebrity info lookup (GetCelebrityInfo)
- **Tags**: Resource tagging (TagResource, UntagResource, ListTagsForResource)

## Design Philosophy
1. **Store-backed**: All state lives in Python dicts — no external dependencies
2. **Mock face data**: Return realistic but deterministic fake face data (bounding boxes, landmarks, attributes)
3. **Async video jobs**: Fake video analysis jobs that complete instantly with deterministic results
4. **Protocol**: JSON-based AWS protocol (not query)
5. **Error fidelity**: Match AWS error codes and HTTP status codes
