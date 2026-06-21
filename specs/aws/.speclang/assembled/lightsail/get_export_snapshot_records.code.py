# spec:trace: aws/lightsail/get_export_snapshot_records.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/get-export-snapshot-records
# spec:generated: DO NOT EDIT — edit the spec instead

def get_export_snapshot_records(store, request: dict) -> dict:
    """Returns all export snapshot records created as a result of the export snapshot operation. An export snapshot record can be used to create a new Amazon EC2 instance and its related resources with the C"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)

