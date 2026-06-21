---
id: "@specs/aws/mediaconvert/ListJobTemplates"
version: 1.0.0
target_lang: py
owned-by: codegen
status: active
depends_on:
  - "@specs/aws/mediaconvert/plan"
---

# ListJobTemplates

List job templates with optional filters and pagination.

## Implementation

```speclang
def execute_list_job_templates(store, request):
    """List job templates."""
    max_results = min(request.get('MaxResults', 20), 100)
    next_token = request.get('NextToken', '')
    category = request.get('Category', '')
    list_order = request.get('ListOrder', 'ASCENDING')
    
    all_templates = list(store.job_templates.values())
    
    if category:
        all_templates = [t for t in all_templates if t.category == category]
    
    all_templates.sort(key=lambda t: t.name, reverse=(list_order == 'DESCENDING'))
    
    start_idx = 0
    if next_token:
        try:
            start_idx = int(next_token)
        except ValueError:
            start_idx = 0
    
    page = all_templates[start_idx:start_idx + max_results]
    
    result = {"JobTemplates": [t.to_dict() for t in page]}
    if start_idx + max_results < len(all_templates):
        result["NextToken"] = str(start_idx + max_results)
    
    return result
```
