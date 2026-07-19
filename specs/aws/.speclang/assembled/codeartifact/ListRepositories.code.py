# spec:trace: aws/codeartifact/ListRepositories.spec.py.md#implementation
# spec:id: @specs/aws/codeartifact/listrepositories
# spec:generated: DO NOT EDIT — edit the spec instead


def execute_list_repositories(store, request):
    """Returns a list of RepositorySummary objects."""
    max_results = request.get("maxResults", 100)
    next_token = request.get("nextToken")
    repos = sorted(store.repositories.values(), key=lambda r: (r.domain_name, r.name))
    if next_token:
        try: repos = repos[int(next_token):]
        except: pass
    items = repos[:max_results]
    result = {"repositories": [{"name": r.name, "administratorAccount": r.administrator_account, "domainName": r.domain_name, "domainOwner": r.domain_owner, "arn": r.arn, "description": r.description} for r in items]}
    if len(repos) > max_results:
        result["nextToken"] = str(max_results)
    return result

