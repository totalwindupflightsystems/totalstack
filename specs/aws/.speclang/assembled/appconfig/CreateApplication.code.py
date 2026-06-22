def create_application(store, request):
    return store.create_application(name=request.get('name',''), description=request.get('description'), **{k:v for k,v in request.items() if k not in ('name','description')})
