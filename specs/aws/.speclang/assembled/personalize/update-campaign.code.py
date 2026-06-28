def handler(store, r): store.update_campaign(r["campaignArn"], **{k:v for k,v in r.items() if k not in ("campaignArn",)}); return {}
