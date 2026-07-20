"""Bedrock Runtime Store — model invocation + async invoke tracking.

Bedrock Runtime is the data plane for Amazon Bedrock. Operations fall
into two categories:

1. **Stateless model calls** (Converse, ConverseStream, InvokeModel,
   InvokeModelWithResponseStream, InvokeModelWithBidirectionalStream,
   CountTokens, ApplyGuardrail) — these pass through to model backends
   and return responses without store persistence.

2. **Async invoke tracking** (StartAsyncInvoke, GetAsyncInvoke,
   ListAsyncInvokes) — these create persistent, trackable invocation jobs.
"""

import time
import uuid


# ── Exception classes ──────────────────────────────────────────────

class BedrockRuntimeException(Exception):
    """Base exception for Bedrock Runtime."""


class AccessDeniedException(BedrockRuntimeException):
    """Access denied to the specified resource."""


class InternalServerException(BedrockRuntimeException):
    """An internal server error occurred."""


class ModelErrorException(BedrockRuntimeException):
    """The model returned an error."""


class ModelNotReadyException(BedrockRuntimeException):
    """The model is not ready for inference."""


class ModelStreamErrorException(BedrockRuntimeException):
    """An error occurred during streaming."""


class ModelTimeoutException(BedrockRuntimeException):
    """The model did not respond within the timeout period."""


class ResourceNotFoundException(BedrockRuntimeException):
    """The specified resource was not found."""


class ServiceQuotaExceededException(BedrockRuntimeException):
    """You have exceeded your service quota."""


class ThrottlingException(BedrockRuntimeException):
    """The request was throttled."""


class ValidationException(BedrockRuntimeException):
    """The input fails to satisfy the constraints."""


# ── Data / Record classes ──────────────────────────────────────────

class AsyncInvokeOutputDataConfig:
    """Output configuration for async invoke jobs."""

    def __init__(self, s3OutputDataConfig=None, **kwargs):
        self.s3OutputDataConfig = s3OutputDataConfig or {}

    def to_dict(self):
        return {
            "s3OutputDataConfig": self.s3OutputDataConfig,
        }


class AsyncInvokeJobRecord:
    """Record for a tracked async invocation job."""

    def __init__(self, modelId, modelInput, outputDataConfig,
                 clientRequestToken=None, tags=None, **kwargs):
        self.invocationArn = f"arn:aws:bedrock:us-east-1:000000000000:async-invoke/{uuid.uuid4().hex[:12]}"
        self.modelId = modelId
        self.modelInput = modelInput
        self.outputDataConfig = outputDataConfig or {}
        self.clientRequestToken = clientRequestToken or uuid.uuid4().hex
        self.status = "InProgress"
        self.failureMessage = None
        self.submitTime = time.time()
        self.lastModifiedTime = self.submitTime
        self.endTime = None
        self.tags = tags or []

    def to_dict(self):
        return {
            "invocationArn": self.invocationArn,
            "modelArn": self.modelId,
            "modelInput": self.modelInput,
            "outputDataConfig": self.outputDataConfig.to_dict() if hasattr(self.outputDataConfig, 'to_dict') else self.outputDataConfig,
            "clientRequestToken": self.clientRequestToken,
            "status": self.status,
            "failureMessage": self.failureMessage,
            "submitTime": self.submitTime,
            "lastModifiedTime": self.lastModifiedTime,
            "endTime": self.endTime,
        }

    def to_summary(self):
        return {
            "invocationArn": self.invocationArn,
            "modelArn": self.modelId,
            "status": self.status,
            "submitTime": self.submitTime,
            "lastModifiedTime": self.lastModifiedTime,
            "endTime": self.endTime,
        }


# ── Store ───────────────────────────────────────────────────────────

class BedrockRuntimeStore:
    """Store for Bedrock Runtime — tracks async invoke jobs.

    Stateless operations (Converse, InvokeModel, etc.) return responses
    without store persistence. Only async invoke jobs are tracked.
    """

    def __init__(self):
        self._async_invokes: dict[str, AsyncInvokeJobRecord] = {}

    # ── Async Invoke methods ───────────────────────────────────────

    def start_async_invoke(self, modelId, modelInput, outputDataConfig,
                           clientRequestToken=None, tags=None):
        """Create and track a new async invocation job."""
        if isinstance(outputDataConfig, dict):
            outputDataConfig = AsyncInvokeOutputDataConfig(**outputDataConfig)
        job = AsyncInvokeJobRecord(
            modelId=modelId,
            modelInput=modelInput,
            outputDataConfig=outputDataConfig,
            clientRequestToken=clientRequestToken,
            tags=tags,
        )
        self._async_invokes[job.invocationArn] = job
        return job.to_dict()

    def get_async_invoke(self, invocationArn):
        """Get a single async invoke job by ARN."""
        if invocationArn not in self._async_invokes:
            raise ResourceNotFoundException(
                f"Async invoke job '{invocationArn}' not found"
            )
        return self._async_invokes[invocationArn].to_dict()

    def list_async_invokes(self, maxResults=None, statusEquals=None,
                           submitTimeAfter=None, submitTimeBefore=None,
                           sortBy=None, sortOrder=None, nextToken=None):
        """List async invoke jobs with optional filtering."""
        jobs = list(self._async_invokes.values())

        if statusEquals:
            jobs = [j for j in jobs if j.status == statusEquals]
        if submitTimeAfter:
            jobs = [j for j in jobs if j.submitTime >= submitTimeAfter]
        if submitTimeBefore:
            jobs = [j for j in jobs if j.submitTime <= submitTimeBefore]

        if sortOrder == "Descending":
            jobs.sort(key=lambda j: j.submitTime, reverse=True)
        else:
            jobs.sort(key=lambda j: j.submitTime, reverse=True)  # newest first

        limit = maxResults or 50
        summaries = [j.to_summary() for j in jobs[:limit]]
        return {
            "asyncInvokeSummaries": summaries,
            "nextToken": None,
        }

    # ── Async Invoke accessor (method-style for generated handlers) ─

    def async_invokes(self, arn=None):
        """Method-style accessor. Returns single job or list of all."""
        if arn is not None:
            return self._async_invokes.get(arn)
        return list(self._async_invokes.values())
