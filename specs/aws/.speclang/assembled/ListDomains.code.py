
def execute_list_domains(store, request):
    """Returns a list of DomainSummary objects for all domains owned by the AWS account."""
    max_results = request.get("maxResults", 100)
    next_token = request.get("nextToken", None)

    domains = sorted(store.domains.values(), key=lambda d: d.name)

    if next_token:
        try:
            start_idx = int(next_token)
            domains = domains[start_idx:]
        except (ValueError, IndexError):
            pass

    items = domains[:max_results]
    result = {
        "domains": [
            {
                "name": d.name,
                "owner": d.owner,
                "arn": d.arn,
                "status": d.status,
                "createdTime": d.created_time,
                "encryptionKey": d.encryption_key,
            }
            for d in items
        ]
    }

    if len(domains) > max_results:
        result["nextToken"] = str(max_results)

    return result
