"""DescribeOrganization handler."""


def handle_describe_organization(store, request: dict) -> dict:
    org = store.describe_organization()
    return {"Organization": org.to_dict()}
