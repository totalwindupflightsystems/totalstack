
def execute_update_job_template(store, request):
    """Update an existing job template."""
    name = request.get('Name')
    if not name:
        raise InvalidParameterException("Name is required")

    tmpl = store.job_templates.get(name)
    if not tmpl:
        raise ResourceNotFoundException(f"Job template '{name}' not found")

    if 'Settings' in request:
        tmpl.settings = request['Settings']
    if 'Description' in request:
        tmpl.description = request['Description']
    if 'Category' in request:
        tmpl.category = request['Category']
    if 'Queue' in request:
        tmpl.queue = request['Queue']
    if 'Priority' in request:
        tmpl.priority = request['Priority']

    tmpl.last_updated = time.time()

    return {"JobTemplate": tmpl.to_dict()}
