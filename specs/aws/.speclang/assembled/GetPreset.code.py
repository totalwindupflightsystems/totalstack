
def execute_get_preset(store, request):
    """Get a preset by name."""
    name = request.get('Name')
    if not name:
        raise InvalidParameterException("Name is required")

    preset = store.presets.get(name)
    if not preset:
        raise ResourceNotFoundException(f"Preset '{name}' not found")

    return {"Preset": preset.to_dict()}
