---
id: "@specs/aws/appconfig/docs/appconfig-integration-containers-agent-starting-eks"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Starting the AWS AppConfig agent for Amazon EKS integration"
status: active
depends_on:
  - "@specs/aws/appconfig/meta"
---

# Starting the AWS AppConfig agent for Amazon EKS integration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appconfig/docs/appconfig-integration-containers-agent-starting-eks
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Starting the AWS AppConfig agent for Amazon EKS integration
<a name="appconfig-integration-containers-agent-starting-eks"></a>

The AWS AppConfig Agent sidecar container is automatically available in your Amazon EKS environment. To use it, you must start it. The following procedure describes how to use the Amazon EKS `kubectl` command line tool to start the agent.

**Note**  
Before you continue, ensure that your `kubeconfig` file is up to date. For more information about creating or editing a `kubeconfig` file, see [Creating or updating a kubeconfig file for an Amazon EKS cluster](https://docs.aws.amazon.com/eks/latest/userguide/create-kubeconfig.html) in the **Amazon EKS User Guide**.

**To start AWS AppConfig Agent (kubectl command line tool)**

1. Open the manifest for your application and verify that your Amazon EKS application is running as a single-container deployment. Contents of the file should look similar to the following.

   ```
   apiVersion: apps/v1
   kind: Deployment
   metadata:
     name: {{my-app}}
     namespace: {{my-namespace}}
     labels:
       app: {{my-application-label}}
   spec:
     replicas: 1
     selector:
       matchLabels:
         app: {{my-application-label}}
     template:
       metadata:
         labels:
           app: {{my-application-label}}
       spec:
         containers:
         - name: {{my-app}}
           image: {{my-repo}}/{{my-image}}
           imagePullPolicy: IfNotPresent
   ```

1. Add the AWS AppConfig Agent container definition details to your deployment manifest.

   ```
   - name: appconfig-agent
           image: public.ecr.aws/aws-appconfig/aws-appconfig-agent:2.x
           ports:
           - name: http
             containerPort: 2772
             protocol: TCP
           env:
           - name: SERVICE_REGION
             value: {{AWS Region}}
           imagePullPolicy: IfNotPresent
   ```
**Note**  
Note the following information.  
AWS AppConfig Agent runs on port 2772, by default. You can specify a different port.
You can adjust the default behavior of AWS AppConfig Agent by entering environment variables. For more information, see [(Optional) Using environment variables to configure AWS AppConfig Agent for Amazon ECS and Amazon EKS](appconfig-integration-containers-agent-configuring.md).
For {{AWS Region}}, specify the AWS Region code (for example, `us-west-1`) where AWS AppConfig Agent retrieves configuration data.

1. Run the following `kubectl` command to apply the changes to your cluster. Replace {{my-deployment}} with the name of your deployment manifest.

   ```
   kubectl apply -f {{my-deployment}}.yml
   ```

1. After the deployment finishes, verify that AWS AppConfig Agent is running. Use the following command to view the application pod log file.

   ```
   kubectl logs -n {{my-namespace}} -c appconfig-agent {{my-pod}}
   ```

   Locate a statement like the following for the AWS AppConfig Agent container: `[appconfig agent] 1970/01/01 00:00:00 INFO serving on localhost:2772`

**Note**  
You can adjust the default behavior of AWS AppConfig Agent by entering or changing environment variables. For information about the available environment variables, see [(Optional) Using environment variables to configure AWS AppConfig Agent for Amazon ECS and Amazon EKS](appconfig-integration-containers-agent-configuring.md).