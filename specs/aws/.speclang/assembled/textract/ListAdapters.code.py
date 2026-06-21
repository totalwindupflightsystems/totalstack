# spec:trace: aws/textract/ListAdapters.spec.py.md#implementation
# spec:id: @specs/aws/textract/listadapters
# spec:generated: DO NOT EDIT — edit the spec instead

def execute_list_adapters(store, request: dict) -> dict:
    max_results = min(request.get("MaxResults", 1000), 1000)
    next_token = request.get("NextToken")
    return store.list_adapters(max_results=max_results, next_token=next_token)

