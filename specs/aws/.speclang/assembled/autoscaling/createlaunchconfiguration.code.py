def handler(store, r: dict) -> dict:
    return store.create_launch_config(r["LaunchConfigurationName"], r.get("ImageId", "ami-test"), r.get("InstanceType", "t3.micro"))