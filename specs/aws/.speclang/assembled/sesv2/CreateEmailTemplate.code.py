def handler(store, request: dict):
    return store.create_email_template(request["TemplateName"], request["TemplateContent"], **{k: v for k, v in request.items() if k not in ("TemplateName", "TemplateContent")})
