---
id: "@specs/aws/lightsail/docs/amazon-lightsail-container-services-deployment-versions"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Manage deployment versions"
status: active
depends_on:
  - "@specs/aws/lightsail/meta"
---

# Manage deployment versions

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lightsail/docs/amazon-lightsail-container-services-deployment-versions
> **target_lang:** meta — documentation tier. ALL sections preserved.



# View and manage Lightsail container service deployment versions
<a name="amazon-lightsail-container-services-deployment-versions"></a>

Every deployment that you create in your Amazon Lightsail container service is saved as a deployment version. If you modify the parameters of an existing deployment, the containers are re-deployed to your service and the modified deployment results in a new deployment version. The latest 50 deployment versions for each container service are saved. You can use any of the 50 deployment versions to create a new deployment in the same container service. In this guide, we show you how to view and manage the deployment versions of your container service.

For more information about container services, see [Container services](amazon-lightsail-container-services.md).

## Deployment version status
<a name="deployment-versions-status"></a>

Each of your deployment versions can be in one of the following states after it's created:
+ **Deploying (Activating)** – The deployment is being launched.
+ **Active** – Your deployment was successfully created, and it's currently running on your container service. Your container service can have only one deployment in an active state at a time.
+ **Inactive** – Your previously successfully created deployment is no longer running on your container.
+ **Failed** – Your deployment failed because one or more of the containers specified in the deployment failed to launch.

## Prerequisites
<a name="deployment-versions-prerequisites"></a>

Before you get started, you need to create a Lightsail container service. For more information, see [Create a container service](amazon-lightsail-creating-container-services.md).

You also should create a deployment in your container service that configures and launches your containers. For more information, see [Creating and managing deployments for your Amazon Lightsail container services](amazon-lightsail-container-services-deployments.md).

## View the deployment versions of a container service
<a name="view-deployment-versions"></a>

Complete the following procedure to view the deployment versions of your Lightsail container service.

1. Sign in to the [Lightsail console](https://lightsail.aws.amazon.com/).

1. In the left navigation pane, choose **Containers**.

1. Choose the name of the container service for which you want to view the deployment versions.

1. On the container service management page, choose the **Deployments** tab.

   The **Deployments** page lists your current deployment and deployment versions, if any.

1. The deployment versions of your container service are listed under the **Deployment versions** section of the page.

   Each deployment has a date, in which it was created, a status, and an actions menu.

1. Choose one of the following options through the actions menu of a deployment version:
   + **Create new deployment** – Choose this option to create a new deployment from the selected deployment version. For more information about creating a deployment, see [Create or modify your container service deployment](https://lightsail.aws.amazon.com/ls/docs/en_us/articles/amazon-lightsail-container-services-deployments#creating-container-service-deployment).
**Note**  
If you choose to create a new deployment from a version that has a **Failed** status, then you must correct the cause of the failure before creating the deployment. Otherwise, the deployment will likely fail again.
   + **View details** – Choose this option to view the container entry and public endpoint parameters of the selected deployment version. You can also view the container logs for the deployment in case you need to diagnose a failed deployment. For more information, see [View container service logs](amazon-lightsail-viewing-container-service-container-logs.md).