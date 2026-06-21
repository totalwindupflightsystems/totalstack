---
id: "@specs/aws/mediaconvert/DeletePreset"
version: 1.0.0
target_lang: py
owned-by: codegen
status: active
depends_on:
  - "@specs/aws/mediaconvert/plan"
---

# DeletePreset

Delete a preset.

## Implementation

```speclang
def execute_delete_preset(store, request):
    """Delete a preset."""
    name = request.get('Name')
    if not name:
        raise InvalidParameterException("Name is required")
    
    if name not in store.presets:
        raise ResourceNotFoundException(f"Preset '{name}' not found")
    
    del store.presets[name]
    
    return {}
```
