# spec:trace: aws/mediaconvert/CreatePreset.spec.py.md#implementation
# spec:id: @specs/aws/mediaconvert/createpreset
# spec:generated: DO NOT EDIT — edit the spec instead

def execute_create_preset(store, request):
    """Create a new preset."""
    name = request.get('Name')
    settings = request.get('Settings')
    
    if not name:
        raise InvalidParameterException("Name is required")
    if not settings:
        raise InvalidParameterException("Settings is required")
    
    if name in store.presets:
        raise ConflictException(f"Preset '{name}' already exists")
    
    preset = PresetRecord(
        name=name,
        settings=settings,
        Description=request.get('Description', ''),
        Category=request.get('Category', ''),
        Tags=request.get('Tags', {}),
    )
    
    store.presets[name] = preset
    
    return {"Preset": preset.to_dict()}

