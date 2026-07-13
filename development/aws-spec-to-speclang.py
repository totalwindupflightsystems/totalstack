#!/usr/bin/env python3
"""
botocore → SpecLang converter: service-2.json → .spec.py.md files

Every AWS service has a botocore service-2.json with:
- Full operation documentation (behavioral notes, limits, edge cases)
- Per-field input/output member docs
- Error shape descriptions
- Complete type system (required/optional, enums, nested shapes)

This script converts that machine-readable AWS spec into SpecLang .spec.py.md
files that the cascade's CodeGen stage can consume to generate implementations.

Usage:
    .venv/bin/python3 development/aws-spec-to-speclang.py dynamodb
    .venv/bin/python3 development/aws-spec-to-speclang.py athena
    .venv/bin/python3 development/aws-spec-to-speclang.py neptune

Output: specs/aws/{service}/*.spec.py.md (overwrites existing)
"""

import sys
import os
import html
import re

import botocore.loaders

# ── helpers ──────────────────────────────────────────────────────────


def strip_html(html_text: str) -> str:
    """Strip HTML tags, decode entities, collapse whitespace."""
    if not html_text:
        return ""
    text = re.sub(r"<[^>]+>", " ", html_text)
    text = html.unescape(text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def indent(text: str, prefix: str = "    ") -> str:
    return prefix + text.replace("\n", "\n" + prefix)


def aws_type_to_python(shape_name: str, shapes: dict) -> str:
    """Map AWS shape name to a Python type hint."""
    if shape_name in (
        "String",
        "ResourceArn",
        "TableArn",
        "ConditionExpression",
        "KeyExpression",
        "FilterExpression",
        "ProjectionExpression",
        "UpdateExpression",
        "AttributeName",
        "PartiQLStatement",
        "TagKeyString",
        "TagValueString",
        "AuthToken",
        "KmsKeyId",
        "SnapshotName",
        "CacheNodeType",
        "PreferredAvailabilityZone",
        "ClusterId",
        "DBClusterIdentifier",
        "DBInstanceIdentifier",
        "ParameterGroupName",
        "SubnetGroupName",
        "DomainName",
        "RepositoryName",
        "PackageName",
        "AssetId",
        "JobId",
        "PresetId",
        "QueueId",
        "TemplateId",
        "ProjectName",
        "BuildId",
        "ApplicationName",
        "DeploymentGroupName",
        "ReplicationGroupId",
        "CacheClusterId",
        "SnapshotName",
        "UserName",
        "UserGroupId",
        "DatabaseName",
        "QueryString",
        "NamedQueryId",
        "WorkGroupName",
        "CatalogName",
        "StatementName",
        "QueryExecutionId",
    ):
        return "str"
    if shape_name in ("Boolean", "BooleanOptional", "BoxedBoolean"):
        return "bool"
    if shape_name in (
        "Integer",
        "IntegerOptional",
        "PositiveIntegerObject",
        "Port",
        "BackupRetentionPeriod",
        "SnapshotRetentionLimit",
        "NumCacheNodes",
    ):
        return "int"
    if shape_name in ("Long", "LongOptional"):
        return "int"
    if shape_name in ("Float", "Double", "DoubleOptional"):
        return "float"
    if shape_name in ("Timestamp", "TStamp", "Date"):
        return "str  # ISO8601"
    if shape_name in ("Blob", "Binary"):
        return "bytes"
    if shape_name and shape_name.endswith("List"):
        member_shape = shapes.get(shape_name, {}).get("member", {}).get("shape", "Any")
        inner = aws_type_to_python(member_shape, shapes)
        return f"list[{inner}]"
    if shape_name and shape_name.endswith("Map"):
        return "dict[str, Any]"
    return "Any  # complex shape"


def derive_handler_impl(op_name: str, op_data: dict, shapes: dict) -> str:
    """Derive a baseline handler implementation from the AWS operation spec."""
    input_shape_name = op_data["input"]["shape"]
    output_shape_name = op_data.get("output", {}).get("shape", "")
    input_shape = shapes.get(input_shape_name, {})
    output_shape = shapes.get(output_shape_name, {}) if output_shape_name else {}
    required = set(input_shape.get("required", []))
    members = input_shape.get("members", {})
    output_members = output_shape.get("members", {})
    errors = [e["shape"] for e in op_data.get("errors", [])]

    doc = strip_html(
        op_data.get("documentation", f"Creates or modifies {op_data['name']} resources.")
    )

    # Determine operation kind
    op_lower = op_name.lower()
    is_create = any(kw in op_lower for kw in ["create", "put", "add", "start", "begin", "register"])
    is_delete = any(
        kw in op_lower for kw in ["delete", "remove", "stop", "cancel", "terminate", "deregister"]
    )
    is_update = any(
        kw in op_lower for kw in ["update", "modify", "change", "set", "enable", "disable"]
    )
    is_get = any(kw in op_lower for kw in ["get", "describe", "fetch", "retrieve"])
    is_list = any(kw in op_lower for kw in ["list", "scan", "query", "search", "batch"])
    is_tag = any(kw in op_lower for kw in ["tag", "untag"])

    # Find the primary identifier field (usually first required member)
    id_field = None
    for m in required:
        if any(p in m.lower() for p in ["name", "id", "arn", "identifier"]):
            id_field = m
            break
    if id_field is None and required:
        id_field = sorted(required)[0]

    # Build handler code
    lines = []
    lines.append(f"def {to_snake(op_name)}(store, request: dict) -> dict:")
    lines.append(f'    """{doc[:200]}"""')

    # Required field validation
    for field in sorted(required):
        field_snake = to_snake(field)
        lines.append(
            f'    {field_snake} = request.get("{field}", "").strip() if isinstance(request.get("{field}"), str) else request.get("{field}")'
        )
        if not is_delete:
            lines.append(f"    if not {field_snake}:")
            lines.append(f'        raise ValidationException("{field} is required")')

    if is_create:
        lines.append("")
        if id_field:
            id_snake = to_snake(id_field)
            lines.append(f"    if store.{get_store_key(op_name, shapes)}({id_snake}):")
            lines.append(
                f'        raise ResourceInUseException(f"Resource {id_snake} already exists")'
            )

        # Build record dict from all members
        lines.append("")
        lines.append("    record = {")
        for field in members:
            field_snake = to_snake(field)
            lines.append(f'        "{field}": {field_snake},')
        lines.append("    }")
        lines.append("")
        # Create in store
        store_key = get_store_key(op_name, shapes)
        if id_field:
            lines.append(f"    store.{store_key}({to_snake(id_field)}, record)")
        else:
            lines.append(f"    store.{store_key}(record)")

        # Build response from output shape
        lines.append("")
        lines.append("    return {")
        for field in output_members:
            field_snake = to_snake(field)
            if id_field and field == id_field:
                lines.append(f'        "{field}": {to_snake(id_field)},')
            else:
                lines.append(f'        "{field}": record.get("{field}", {{}}),')
        lines.append("    }")

    elif is_get:
        lines.append("")
        if id_field:
            id_snake = to_snake(id_field)
            # Some Get ops use store.collection[id], others use store.get_x(id)
            store_key = get_store_key(op_name, shapes)
            lines.append(f"    resource = store.{store_key}({id_snake})")
            lines.append("    if not resource:")
            lines.append(
                f'        raise ResourceNotFoundException(f"Resource {id_snake} not found")'
            )
            lines.append(f'    return {{"{id_field}": {id_snake}, **resource}}')
        else:
            lines.append("    # Auto-generated get handler — verify resource key")
            lines.append("    return store.get_resource(request)")

    elif is_delete:
        lines.append("")
        if id_field:
            id_snake = to_snake(id_field)
            store_key = get_store_key(op_name, shapes)
            lines.append(f"    if not store.{store_key}({id_snake}):")
            lines.append(
                f'        raise ResourceNotFoundException(f"Resource {id_snake} not found")'
            )
            lines.append(f"    store.delete_{store_key}({id_snake})")
        lines.append("    return {}")

    elif is_list:
        lines.append("")
        # Extract pagination params
        token_field = None
        limit_field = None
        for m in members:
            ml = m.lower()
            if "token" in ml or "marker" in ml:
                token_field = m
            if "limit" in ml or "max" in ml:
                limit_field = m

        list_key = get_list_key(op_name, output_members)
        lines.append(f"    items = store.list_{get_store_key(op_name, shapes)}()")
        lines.append(f'    return {{"{list_key}": list(items.values())}}')

    elif is_update:
        lines.append("")
        if id_field:
            id_snake = to_snake(id_field)
            store_key = get_store_key(op_name, shapes)
            lines.append(f"    resource = store.{store_key}({id_snake})")
            lines.append("    if not resource:")
            lines.append(
                f'        raise ResourceNotFoundException(f"Resource {id_snake} not found")'
            )
            lines.append("")
            lines.append("    # Update mutable fields")
            for field in members:
                if field not in required:
                    field_snake = to_snake(field)
                    lines.append(f'    if "{field}" in request:')
                    lines.append(f'        resource["{field}"] = {field_snake}')
            lines.append("")
            lines.append(f"    store.{store_key}({id_snake}, resource)")
            lines.append("    return resource")

    elif is_tag:
        lines.append("")
        lines.append("    # Tag/untag resource")
        lines.append(
            '    resource_arn = request.get("ResourceARN", request.get("ResourceName", ""))'
        )
        lines.append('    store.tag_resource(resource_arn, request.get("Tags", []))')
        lines.append("    return {}")

    else:
        lines.append("")
        lines.append("    # Auto-generated handler — operation not classified as CRUD")
        lines.append(f'    return store.execute("{op_name}", request)')

    return "\n".join(lines)


def to_snake(name: str) -> str:
    """CamelCase → snake_case."""
    s1 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", s1).lower()


def get_store_key(op_name: str, shapes: dict) -> str:
    """Derive the store collection name (e.g., 'cache_clusters', 'work_groups')."""
    # Strip known prefixes
    key = op_name
    for prefix in [
        "Create",
        "Delete",
        "Get",
        "Describe",
        "Update",
        "Modify",
        "List",
        "BatchGet",
        "BatchWrite",
        "Put",
        "Add",
        "Remove",
        "Start",
        "Stop",
        "Cancel",
        "Copy",
        "Reboot",
    ]:
        if key.startswith(prefix):
            key = key[len(prefix) :]
            break
    return to_snake(key) + "s"


def get_list_key(op_name: str, output_members: dict) -> str:
    """Find the list-result key in output members (e.g., 'TableNames', 'CacheClusters')."""
    for name in output_members:
        if name.endswith("s") or "List" in name:
            return name
    if output_members:
        return sorted(output_members.keys())[0]
    return "Items"


# ── main converter ───────────────────────────────────────────────────


def convert_service(service_name: str, output_dir: str):
    """Convert one AWS service from botocore → SpecLang .spec.py.md files."""
    loader = botocore.loaders.Loader()
    svc = loader.load_service_model(service_name, "service-2")
    shapes = svc.get("shapes", {})
    operations = svc.get("operations", {})
    metadata = svc.get("metadata", {})
    proto = metadata.get("protocol", "json")
    api_version = metadata.get("apiVersion", "unknown")

    os.makedirs(output_dir, exist_ok=True)

    ops_written = 0
    for op_name, op_data in sorted(operations.items()):
        if "input" not in op_data:
            continue  # skip operations without input shapes (e.g., some list operations)
        input_shape_name = op_data["input"]["shape"]
        input_shape = shapes.get(input_shape_name, {})
        output_shape_name = op_data.get("output", {}).get("shape", "")
        output_shape = shapes.get(output_shape_name, {}) if output_shape_name else {}
        members = input_shape.get("members", {})
        required = set(input_shape.get("required", []))
        output_members = output_shape.get("members", {})
        errors = op_data.get("errors", [])
        op_doc = strip_html(op_data.get("documentation", ""))

        # Build spec file
        spec_id = f"@specs/aws/{service_name}/{to_snake(op_name)}"
        snake_name = to_snake(op_name)

        lines = []
        lines.append("---")
        lines.append(f'id: "{spec_id}"')
        lines.append("version: 1.0.0")
        lines.append("target_lang: py")
        lines.append("owned-by: codegen")
        lines.append("model_pool: code-gen")
        lines.append("status: active")
        lines.append("depends_on:")
        lines.append(f'  - "@specs/aws/{service_name}/plan"')
        lines.append(f'  - "@specs/aws/{service_name}/docs/API_{op_name}"')
        lines.append("---")
        lines.append("")
        lines.append(f"# {op_name}")
        lines.append("")
        lines.append(
            f"> **spec:trace:** specs/aws/{service_name}/{service_name}.spec.plan.md#operation-inventory"
        )
        lines.append(f"> **spec:id:** {spec_id}")
        lines.append(f"> **spec:implements:** @kind:operation {op_name}")
        lines.append(f"> **AWS Protocol:** {proto}")
        lines.append(f"> **HTTP:** {op_data['http']['method']} {op_data['http']['requestUri']}")
        lines.append(f"> **@ref:** specs/aws/{service_name}/docs/API_{op_name}.spec.md")
        lines.append("")
        lines.append(op_doc)
        lines.append("")
        lines.append("## Input Shape: " + input_shape_name)
        lines.append("")
        lines.append("| Parameter | Type | Required | Description |")
        lines.append("|-----------|------|----------|-------------|")
        for field in sorted(members.keys()):
            m = members[field]
            shape = m.get("shape", "Unknown")
            py_type = aws_type_to_python(shape, shapes)
            is_req = "✓" if field in required else ""
            doc = strip_html(m.get("documentation", ""))[:120]
            lines.append(f"| {field} | {py_type} | {is_req} | {doc} |")

        if output_shape_name:
            lines.append("")
            lines.append("## Output Shape: " + output_shape_name)
            lines.append("")
            for field in sorted(output_members.keys()):
                m = output_members[field]
                shape = m.get("shape", "Unknown")
                py_type = aws_type_to_python(shape, shapes)
                doc = strip_html(m.get("documentation", ""))[:120]
                lines.append(f"- **{field}** ({py_type}): {doc}")

        if errors:
            lines.append("")
            lines.append("## Errors")
            for err in errors[:10]:
                err_shape = shapes.get(err["shape"], {})
                err_doc = strip_html(err_shape.get("documentation", ""))[:200]
                lines.append(f"- **{err['shape']}**: {err_doc}")

        # Generate handler implementation derived from AWS spec
        impl = derive_handler_impl(op_name, op_data, shapes)

        lines.append("")
        lines.append("## Implementation")
        lines.append("")
        lines.append("```speclang")
        lines.append(impl)
        lines.append("```")

        filepath = os.path.join(output_dir, f"{snake_name}.spec.py.md")
        with open(filepath, "w") as f:
            f.write("\n".join(lines) + "\n")

        ops_written += 1

    return ops_written


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: aws-spec-to-speclang.py <service-name> [output-dir]")
        print("Example: .venv/bin/python3 development/aws-spec-to-speclang.py athena")
        sys.exit(1)

    svc = sys.argv[1]
    out = sys.argv[2] if len(sys.argv) > 2 else f"specs/aws/{svc}"

    count = convert_service(svc, out)
    print(f"✅ {count} .spec.py.md files written to {out}/")
    print("   Next: cd ~/SpecLang && npx tsx .speclang/assembler.spec.ts")
