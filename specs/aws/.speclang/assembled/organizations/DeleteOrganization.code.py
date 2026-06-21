"""DeleteOrganization handler."""


def handle_delete_organization(store, request: dict) -> dict:
    store.delete_organization()
    return {}
