---
id: "@specs/aws/mediaconvert/CreatePreset"
version: 1.0.0
target_lang: py
owned-by: codegen
status: active
depends_on:
  - "@specs/aws/mediaconvert/plan"
---

# CreatePreset

Create a new output preset.

## Implementation

```speclang
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
```
