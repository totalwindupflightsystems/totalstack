def handler(store, request: dict) -> dict:
    return store.create_custom_action_type(
        category=request["category"],
        provider=request["provider"],
        version=request["version"],
        input_artifact_details=request.get("inputArtifactDetails", {}),
        output_artifact_details=request.get("outputArtifactDetails", {}),
        settings=request.get("settings"),
        configuration_properties=request.get("configurationProperties"),
        tags=request.get("tags"),
    )
