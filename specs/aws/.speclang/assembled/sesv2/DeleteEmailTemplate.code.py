def handler(store, request: dict):
    return store.delete_email_template(request["TemplateName"])
