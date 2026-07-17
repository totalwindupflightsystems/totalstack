def handler(store, r: dict) -> dict:
    rec = store.create_rule(r["ruleId"], r["detectorId"],
        expression=r.get("expression", ""), language=r.get("language", "DETECTORPL"),
        outcomes=r.get("outcomes", []),
        **{k: v for k, v in r.items() if k not in ("ruleId", "detectorId", "expression", "language", "outcomes")})
    return rec.to_dict()
