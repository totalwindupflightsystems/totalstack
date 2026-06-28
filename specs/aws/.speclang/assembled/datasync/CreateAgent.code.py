def create_agent(store, request: dict) -> dict:
    return store.create_agent(
        ActivationKey=request["ActivationKey"],
        AgentName=request.get("AgentName"),
        Tags=request.get("Tags"),
        VpcEndpointId=request.get("VpcEndpointId"),
        SubnetArns=request.get("SubnetArns"),
        SecurityGroupArns=request.get("SecurityGroupArns"),
    )
