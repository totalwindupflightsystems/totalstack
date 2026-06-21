"""Handler for CreateWebACL — AWS WAFv2."""
def handler(store, request):
    name = request.get("Name")
    scope = request.get("Scope")
    if not name:
        raise WAFInvalidParameterException("Name is required")
    if not scope:
        raise WAFInvalidParameterException("Scope is required")
    if not request.get("DefaultAction"):
        raise WAFInvalidParameterException("DefaultAction is required")
    if not request.get("VisibilityConfig"):
        raise WAFInvalidParameterException("VisibilityConfig is required")
    return store.create_web_acl(
        name=name,
        scope=scope,
        default_action=request["DefaultAction"],
        visibility_config=request["VisibilityConfig"],
        description=request.get("Description", ""),
        rules=request.get("Rules"),
        capacity=request.get("Capacity"),
        custom_response_bodies=request.get("CustomResponseBodies"),
        captcha_config=request.get("CaptchaConfig"),
        challenge_config=request.get("ChallengeConfig"),
        token_domains=request.get("TokenDomains"),
        tags=request.get("Tags"))
