#!/usr/bin/env python3
"""Extract ```speclang code blocks from .spec.py.md files and write to .code.py files.

Run this when the SpecLang cascade runner is unreliable or when you need fast,
deterministic code extraction without waiting for Pi Agent sessions.

Strips DSL annotations (@kind:operation, @aws-operation:, @required:, @errors:)
including multi-line continuations, so the output is valid Python.

Usage:
    # Extract all specs for a service
    python3 scripts/extract_speclang_code.py <specs_dir> <output_dir>

    # Example:
    python3 scripts/extract_speclang_code.py \
        /home/kara/totalstack/specs/aws/xray \
        /home/kara/totalstack/specs/aws/.speclang/assembled/xray

Output:
    Each .spec.py.md file with a ```speclang block produces a .code.py file
    with spec:trace headers. DSL annotations are stripped; only valid Python remains.
"""
import os
import re
import sys

def strip_dsl_annotations(code):
    """Strip @kind:, @aws-operation:, @required:, @errors: annotations including
    multi-line continuations (indented lines following the annotation start)."""
    lines = code.split('\n')
    clean = []
    skip_next_indented = False

    for line in lines:
        # Detect new DSL annotation start
        is_annotation_start = bool(re.match(r'^\s*@(kind|aws-operation|required|errors):', line))

        if is_annotation_start:
            skip_next_indented = True
            continue

        # Skip indented continuation lines of a previous annotation
        if skip_next_indented:
            if line and (line[0] in (' ', '\t')):
                continue
            else:
                skip_next_indented = False
                if not line.strip():
                    # Blank line after annotation — skip it too
                    continue

        clean.append(line)

    # Remove leading blank lines
    while clean and not clean[0].strip():
        clean.pop(0)

    return '\n'.join(clean)


specs_dir = sys.argv[1]
assembled_dir = sys.argv[2]
os.makedirs(assembled_dir, exist_ok=True)

count = 0
total_lines = 0

for fname in sorted(os.listdir(specs_dir)):
    if not fname.endswith('.spec.py.md'):
        continue

    fpath = os.path.join(specs_dir, fname)
    with open(fpath) as f:
        content = f.read()

    # Extract ```speclang blocks
    blocks = re.findall(r'```speclang\n(.*?)```', content, re.DOTALL)

    if not blocks:
        print(f"WARNING: No speclang block in {fname}")
        continue

    # Derive output name: CreateGroup.spec.py.md -> CreateGroup.code.py
    out_name = fname.replace('.spec.py.md', '.code.py')
    out_path = os.path.join(assembled_dir, out_name)

    raw_code = '\n'.join(blocks)
    clean_code = strip_dsl_annotations(raw_code)
    lines = clean_code.count('\n') + 1

    # Derive service name from the specs_dir path (e.g. .../aws/xray -> xray)
    path_parts = os.path.normpath(specs_dir).split(os.sep)
    service_name = path_parts[-1] if len(path_parts) > 1 else 'unknown'
    spec_path = os.path.join(*path_parts[-2:], fname) if len(path_parts) >= 2 else fname

    # Add trace header
    spec_id = fname.replace('.spec.py.md', '').lower().replace('_', '-')
    trace_header = f'''# spec:trace: {spec_path}#implementation
# spec:id: @specs/aws/{service_name}/{spec_id}
# spec:generated: DO NOT EDIT — edit the spec instead

'''

    with open(out_path, 'w') as f:
        f.write(trace_header + clean_code + '\n')

    print(f"  {out_name}: {lines} lines")
    count += 1
    total_lines += lines

print(f"\nExtracted {count} files, {total_lines} total lines to {assembled_dir}")
