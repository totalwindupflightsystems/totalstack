# spec:trace: aws/codeartifact/DescribeDomain.spec.py.md#implementation
# spec:id: @specs/aws/codeartifact/describedomain
# spec:generated: DO NOT EDIT — edit the spec instead


def execute_describe_domain(store, request):
    """Returns a DomainDescription object that contains information about the requested domain."""
    domain_name = request.get("domain", "")
    if not domain_name:
        raise ValidationException("domain is required")

    domain = store._get_domain(domain_name)

    return {
        "domain": {
            "name": domain.name,
            "owner": domain.owner,
            "arn": domain.arn,
            "status": domain.status,
            "createdTime": domain.created_time,
            "encryptionKey": domain.encryption_key,
            "repositoryCount": domain.repository_count,
            "assetSizeBytes": domain.asset_size_bytes,
            "s3BucketArn": domain.s3_bucket_arn,
        }
    }

