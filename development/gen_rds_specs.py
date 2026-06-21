#!/usr/bin/env python3
"""Batch generate RDS handler specs — flat directory, no subdirs."""
import os

SERVICE = 'rds'
PROJECT_ROOT = '/home/kara/totalstack'
SPECS_DIR = f'{PROJECT_ROOT}/specs/aws/{SERVICE}'
ASSEMBLED_DIR = f'{PROJECT_ROOT}/specs/aws/.speclang/assembled/{SERVICE}'
os.makedirs(SPECS_DIR, exist_ok=True)
os.makedirs(ASSEMBLED_DIR, exist_ok=True)

CORE_OPS = [
    'CreateDBInstance', 'DescribeDBInstances', 'ModifyDBInstance', 'DeleteDBInstance', 'RebootDBInstance',
    'CreateDBCluster', 'DescribeDBClusters', 'ModifyDBCluster', 'DeleteDBCluster',
    'CreateDBSnapshot', 'DescribeDBSnapshots', 'DeleteDBSnapshot',
    'CreateDBParameterGroup', 'DescribeDBParameterGroups', 'ModifyDBParameterGroup', 'DeleteDBParameterGroup',
    'CreateDBSubnetGroup', 'DescribeDBSubnetGroups', 'DeleteDBSubnetGroup',
    'CreateDBClusterParameterGroup', 'DescribeDBClusterParameterGroups', 'DeleteDBClusterParameterGroup',
    'AddTagsToResource', 'RemoveTagsFromResource', 'ListTagsForResource',
]

docs_dir = f'{SPECS_DIR}/docs'
doc_list = os.listdir(docs_dir) if os.path.exists(docs_dir) else []

def find_doc(op_name):
    for d in doc_list:
        if op_name.lower() in d.lower():
            return d
    return None

generated = 0
for op_name in CORE_OPS:
    doc_file = find_doc(op_name)
    filename = f'handler-{op_name.lower()}'
    
    ref_lines = ''
    if doc_file:
        ref_lines = f'> **@ref:** specs/aws/{SERVICE}/docs/{doc_file}\n'
    
    content = f"""---
id: "@specs/aws/{SERVICE}/{filename}"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/{SERVICE}/plan"
---

# {op_name}

> **spec:trace:** specs/aws/{SERVICE}/{SERVICE}.spec.plan.md
> **spec:id:** @specs/aws/{SERVICE}/{filename}
> **spec:implements:** @kind:operation {op_name}
{ref_lines}
AWS RDS {op_name} operation handler.

```speclang
def handler(store, request: dict) -> dict:
    \"\"\"{op_name} handler for RDS.\"\"\"
    return {{}}
```
"""
    path = f'{SPECS_DIR}/{filename}.spec.py.md'
    with open(path, 'w') as f:
        f.write(content)
    generated += 1
    status = '✓' if doc_file else '✗ MISSING'
    print(f'  {status} {op_name}')

print(f'\nGenerated {generated} specs in {SPECS_DIR}/')
print(f'Docs available: {len(doc_list)}')
