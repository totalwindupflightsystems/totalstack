"""StopDeployment handler for CodeDeploy."""


def stop_deployment(store, request):
    deployment_id = request.get('deploymentId', '').strip()
    auto_rollback_enabled = request.get('autoRollbackEnabled', False)

    deployment = store.deployments.stop_deployment(deployment_id)
    result = {
        'status': 'Succeeded',
        'statusMessage': f"Deployment {deployment_id} stopped successfully"
    }
    return result
