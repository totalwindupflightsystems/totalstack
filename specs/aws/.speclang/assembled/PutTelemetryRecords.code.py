
def put_telemetry_records(store, request):
    records = request.get('TelemetryRecords', [])
    if not records:
        raise InvalidRequestException('TelemetryRecords is required')
    ec2_instance_id = request.get('EC2InstanceId', '')
    hostname = request.get('Hostname', '')
    resource_arn = request.get('ResourceARN', '')
    for rec in records:
        rec['EC2InstanceId'] = ec2_instance_id
        rec['Hostname'] = hostname
        rec['ResourceARN'] = resource_arn
    return {}
