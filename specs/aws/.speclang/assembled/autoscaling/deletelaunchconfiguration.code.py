def handler(store, r: dict) -> dict:
    return store.delete_launch_config(r["LaunchConfigurationName"])