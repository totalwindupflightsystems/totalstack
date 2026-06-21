"""CreateOrganization handler."""


def handle_create_organization(store, request: dict) -> dict:
    feature_set = request.get("FeatureSet", "ALL")
    if feature_set not in ("ALL", "CONSOLIDATED_BILLING"):
        raise InvalidInputException(f"Invalid FeatureSet: {feature_set}")

    org = store.create_organization(feature_set=feature_set)
    return {"Organization": org.to_dict()}
