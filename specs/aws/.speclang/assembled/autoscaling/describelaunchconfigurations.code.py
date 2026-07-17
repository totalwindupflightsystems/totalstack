def handler(store, r: dict) -> dict:
    return store.describe_launch_configs(r.get("LaunchConfigurationNames"))