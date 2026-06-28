def handler(store, request: dict) -> dict:
    return store.update_index(request['Id'], Name=request.get('Name'), Description=request.get('Description'), RoleArn=request.get('RoleArn'))

