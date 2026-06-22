---
id: "@specs/aws/appconfig/docs/appconfig-integration-containers-agent-starting-ecs"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Starting the AWS AppConfig agent for Amazon ECS integration"
status: active
depends_on:
  - "@specs/aws/appconfig/meta"
---

# Starting the AWS AppConfig agent for Amazon ECS integration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appconfig/docs/appconfig-integration-containers-agent-starting-ecs
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Starting the AWS AppConfig agent for Amazon ECS integration
<a name="appconfig-integration-containers-agent-starting-ecs"></a>

The AWS AppConfig Agent sidecar container is automatically available in your Amazon ECS environment. To use it, you must start it, as described in the following procedure.

**To start Amazon ECS (console)**

1. Open the console at [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2).

1. In the navigation pane, choose **Task definitions**.

1. Choose the task definition for your application, and then select the latest revision.

1. Choose **Create new revision**, **Create new revision**.

1. Choose **Add more containers**.

1. For** Name**, enter a unique name for the AWS AppConfig Agent container.

1. For **Image URI**, enter: **public.ecr.aws/aws-appconfig/aws-appconfig-agent:2.x**

1. For **Essential container**, choose **Yes**.

1. In the **Port mappings** section, choose **Add port mapping**.

1. For **Container port**, enter **2772**.
**Note**  
AWS AppConfig Agent runs on port 2772, by default. You can specify a different port.

1. Choose **Create**. Amazon ECS creates a new container revision and displays the details.

1. In the navigation pane, choose **Clusters**, and then choose your application cluster in the list.

1. On the **Services** tab, select the service for your application.

1. Choose **Update**.

1. Under **Deployment configuration**, for **Revision**, choose the latest revision.

1. Choose **Update**. Amazon ECS deploys the latest task definition.

1. After the deployment finishes, you can verify that AWS AppConfig Agent is running on the **Configuration and tasks** tab. On the **Tasks** tab, choose the running task.

1. In the **Containers** section, verify that the AWS AppConfig Agent container is listed.

1. To verify that AWS AppConfig Agent started, choose the **Logs** tab. Locate a statement like the following for the AWS AppConfig Agent container: `[appconfig agent] 1970/01/01 00:00:00 INFO serving on localhost:2772`

**Note**  
Note the following information.  
AWS AppConfig Agent is a long-running process. As a best practice for Amazon ECS containers, configure health checks for your containers, specifically setting the container dependency to the HEALTHY condition. For more information, see [ContainerDependency](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ContainerDependency.html) in the *Amazon Elastic Container Service API Reference*.
You can adjust the default behavior of AWS AppConfig Agent by entering or changing environment variables. For information about the available environment variables, see [(Optional) Using environment variables to configure AWS AppConfig Agent for Amazon ECS and Amazon EKS](appconfig-integration-containers-agent-configuring.md). For information about how to change environment variables in Amazon ECS, see [Passing environment variables to a container](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/taskdef-envfiles.html) in the *Amazon Elastic Container Service Developer Guide*.