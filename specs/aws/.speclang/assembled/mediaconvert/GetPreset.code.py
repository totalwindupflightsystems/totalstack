# spec:trace: aws/mediaconvert/GetPreset.spec.py.md#implementation
# spec:id: @specs/aws/mediaconvert/getpreset
# spec:generated: DO NOT EDIT — edit the spec instead

def execute_get_preset(store, request):
    """Get a preset by name."""
    name = request.get('Name')
    if not name:
        raise InvalidParameterException("Name is required")
    
    preset = store.presets.get(name)
    if not preset:
        raise ResourceNotFoundException(f"Preset '{name}' not found")
    
    return {"Preset": preset.to_dict()}

