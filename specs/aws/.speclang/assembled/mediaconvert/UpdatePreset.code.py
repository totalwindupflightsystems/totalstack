# spec:trace: aws/mediaconvert/UpdatePreset.spec.py.md#implementation
# spec:id: @specs/aws/mediaconvert/updatepreset
# spec:generated: DO NOT EDIT — edit the spec instead

def execute_update_preset(store, request):
    """Update an existing preset."""
    name = request.get('Name')
    if not name:
        raise InvalidParameterException("Name is required")
    
    preset = store.presets.get(name)
    if not preset:
        raise ResourceNotFoundException(f"Preset '{name}' not found")
    
    if 'Settings' in request:
        preset.settings = request['Settings']
    if 'Description' in request:
        preset.description = request['Description']
    if 'Category' in request:
        preset.category = request['Category']
    
    preset.last_updated = time.time()
    
    return {"Preset": preset.to_dict()}

