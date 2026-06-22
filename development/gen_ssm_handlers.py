#!/usr/bin/env python3
"""Write SSM handlers."""
import os
d = '/home/kara/totalstack/specs/aws/.speclang/assembled/ssm'
os.makedirs(d, exist_ok=True)

handlers = {
    'putparameter': 'def handler(store, r: dict) -> dict:\n    return store.put_parameter(r["Name"], r["Value"], r.get("Type", "String"), r.get("Description", ""), r.get("Overwrite", False))',
    'getparameter': 'def handler(store, r: dict) -> dict:\n    return store.get_parameter(r["Name"], r.get("WithDecryption", False))',
    'getparameters': 'def handler(store, r: dict) -> dict:\n    return store.get_parameters(r["Names"], r.get("WithDecryption", False))',
    'describeparameters': 'def handler(store, r: dict) -> dict:\n    return store.describe_parameters(r.get("Filters"), r.get("MaxResults", 50))',
    'deleteparameter': 'def handler(store, r: dict) -> dict:\n    return store.delete_parameter(r["Name"])',
    'getparameterhistory': 'def handler(store, r: dict) -> dict:\n    return store.get_parameter_history(r["Name"], r.get("MaxResults", 50))',
    'addtagstoresource': 'def handler(store, r: dict) -> dict:\n    return store.add_tags(r["ResourceId"], r["Tags"])',
    'listtagsforresource': 'def handler(store, r: dict) -> dict:\n    return store.list_tags(r["ResourceId"])',
    'removetagsfromresource': 'def handler(store, r: dict) -> dict:\n    return store.remove_tags(r["ResourceId"], r["TagKeys"])',
}
for name, code in handlers.items():
    with open(f'{d}/{name}.code.py', 'w') as f:
        f.write(code)
print(f'{len(handlers)} handlers')
