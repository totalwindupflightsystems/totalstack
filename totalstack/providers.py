"""
TotalStack service providers — register our stores alongside LocalStack's.
Loaded by LocalStack's plugin system via entry point.
"""
from localstack.services.plugins import Service, aws_provider


@aws_provider(api="acm", name="totalstack")
def acm_totalstack():
    """ACM provider backed by TotalStack's real ACMStore — no moto."""
    from localstack.services.moto import MotoFallbackDispatcher
    from totalstack.services.acm.provider import TotalStackAcmProvider

    provider = TotalStackAcmProvider()
    return Service.for_provider(provider, dispatch_table_factory=MotoFallbackDispatcher)
