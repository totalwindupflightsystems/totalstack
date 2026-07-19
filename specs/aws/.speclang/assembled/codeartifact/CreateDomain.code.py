# spec:trace: aws/codeartifact/CreateDomain.spec.py.md#implementation
# spec:id: @specs/aws/codeartifact/createdomain
# spec:generated: DO NOT EDIT — edit the spec instead


def execute_create_domain(store, request):
    """Creates a domain. CodeArtifact domains make it easier to manage multiple repositories across an organization."""
    domain_name = request.get("domain", "")
    if not domain_name:
        raise ValidationException("domain is required")

    _validate_domain_name(domain_name)

    if domain_name in store.domains:
        raise ConflictException(f"Domain {domain_name} already exists")

    owner = "123456789012"
    domain = DomainRecord(
        name=domain_name,
        owner=owner,
        encryption_key=request.get("encryptionKey"),
    )

    store.domains[domain_name] = domain
    store.domain_policies[domain_name] = ""

    result = {
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

    if request.get("tags"):
        arn = domain.arn
        for tag in request["tags"]:
            store.tags[arn][tag["key"]] = tag["value"]

    return result

