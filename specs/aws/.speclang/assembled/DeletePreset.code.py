// spec:trace spec=/home/kara/totalstack/specs/aws/mediaconvert/DeletePreset.spec.py.md#implementation
// spec:generated DO NOT EDIT — edit the spec instead

def execute_delete_preset(store, request):
    """Delete a preset."""
    name = request.get('Name')
    if not name:
        raise InvalidParameterException("Name is required")
    
    if name not in store.presets:
        raise ResourceNotFoundException(f"Preset '{name}' not found")
    
    del store.presets[name]
    
    return {}