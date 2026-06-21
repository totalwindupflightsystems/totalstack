def handler(store, request):
    auto_renew = request.get("AutoRenew")
    return store.update_subscription(auto_renew=auto_renew)
