# spec:trace: aws/textract/AnalyzeExpense.spec.py.md#implementation
# spec:id: @specs/aws/textract/analyzeexpense
# spec:generated: DO NOT EDIT — edit the spec instead

def execute_analyze_expense(store, request: dict) -> dict:
    doc = request.get("Document", {})
    if not doc.get("Bytes") and not doc.get("S3Object"):
        raise InvalidParameterException(
            "Document must provide either Bytes or S3Object"
        )
    if doc.get("Bytes") and doc.get("S3Object"):
        raise InvalidParameterException(
            "Document cannot provide both Bytes and S3Object"
        )

    expense_docs = _generate_mock_expense_documents()
    return {
        "DocumentMetadata": _build_document_metadata(),
        "ExpenseDocuments": expense_docs,
    }

