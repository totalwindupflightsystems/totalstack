# spec:trace: aws/codeartifact/AuthorizationAndTags.spec.py.md#implementation
# spec:id: @specs/aws/codeartifact/authorizationandtags
# spec:generated: DO NOT EDIT — edit the spec instead

@dataclass
def execute_get_authorization_token(store, request):
    """Generates a temporary authorization token for accessing repositories in the domain."""
    domain_name = request.get("domain", "")
    if not domain_name:
        raise ValidationException("domain is required")
    domain = store._get_domain(domain_name)
    duration = request.get("durationSeconds", 43200)
    token = f"codeartifact-token-{uuid.uuid4().hex}-{domain_name}"
    import time
    return {
        "authorizationToken": token,
        "expiration": time.time() + duration,
    }

@dataclass
def execute_tag_resource(store, request):
    """Adds tags to a resource."""
    arn = request.get("resourceArn", "")
    tags = request.get("tags", [])
    if not arn:
        raise ValidationException("resourceArn is required")
    if not tags:
        raise ValidationException("tags is required")
    for tag in tags:
        store.tags[arn][tag["key"]] = tag["value"]
    return {}

@dataclass
def execute_untag_resource(store, request):
    """Removes tags from a resource."""
    arn = request.get("resourceArn", "")
    tag_keys = request.get("tagKeys", [])
    if not arn:
        raise ValidationException("resourceArn is required")
    if not tag_keys:
        raise ValidationException("tagKeys is required")
    for key in tag_keys:
        store.tags[arn].pop(key, None)
    return {}

@dataclass
def execute_list_tags_for_resource(store, request):
    """Lists tags for a resource."""
    arn = request.get("resourceArn", "")
    if not arn:
        raise ValidationException("resourceArn is required")
    tags = store.tags.get(arn, {})
    return {"tags": [{"key": k, "value": v} for k, v in tags.items()]}

