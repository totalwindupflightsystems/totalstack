// spec:trace spec=/home/kara/totalstack/specs/aws/textract/AnalyzeDocument.spec.py.md#implementation
// spec:generated DO NOT EDIT — edit the spec instead

def execute_analyze_document(store, request: dict) -> dict:
    doc = request.get("Document", {})
    feature_types = request.get("FeatureTypes", [])

    # Validate — exactly one of Bytes or S3Object
    has_bytes = "Bytes" in doc
    has_s3 = "S3Object" in doc
    if not has_bytes and not has_s3:
        raise InvalidParameterException(
            "Document must provide either Bytes or S3Object"
        )
    if has_bytes and has_s3:
        raise InvalidParameterException(
            "Document cannot provide both Bytes and S3Object"
        )

    # Check feature types
    valid_features = {"TABLES", "FORMS", "QUERIES", "SIGNATURES", "LAYOUT"}
    for ft in feature_types:
        if ft not in valid_features:
            raise InvalidParameterException(
                f"Invalid FeatureType: {ft}. Valid values: {sorted(valid_features)}"
            )

    blocks = []
    # Always return text blocks
    blocks.extend(_generate_mock_document_blocks(page_count=1))

    if "TABLES" in feature_types:
        blocks.extend(_generate_mock_table_blocks())
    if "FORMS" in feature_types:
        blocks.extend(_generate_mock_form_blocks())
    if "SIGNATURES" in feature_types:
        blocks.append(_make_block("SIGNATURE", "sig-0", 1, confidence=95.0))
    if "QUERIES" in feature_types:
        queries_config = request.get("QueriesConfig", {}).get("Queries", [])
        for i, q in enumerate(queries_config):
            blocks.append(_make_block("QUERY", f"query-{i}", 1,
                          text=q.get("Text", ""),
                          query={"Text": q.get("Text", ""), "Alias": q.get("Alias", "")}))
            blocks.append(_make_block("QUERY_RESULT", f"qr-{i}", 1,
                          text="Mock result", confidence=90.0))

    response = {
        "DocumentMetadata": _build_document_metadata(),
        "Blocks": blocks,
        "AnalyzeDocumentModelVersion": "1.0",
    }
    if "HUMAN_LOOP" in [ft.upper() for ft in feature_types] or request.get("HumanLoopConfig"):
        response["HumanLoopActivationOutput"] = {
            "HumanLoopArn": "arn:aws:sagemaker:us-east-1:123456789012:flow-definition/mock",
            "HumanLoopActivationReason": {"Text": "Mock"},
            "HumanLoopActivationConditionsEvaluationResults": "{}",
        }
    return response