---
id: "@specs/aws/appconfig/docs/appconfig-integration-containers-agent-daemon"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS (Optional) Running AWS AppConfig as a DaemonSet in Amazon EKS"
status: active
depends_on:
  - "@specs/aws/appconfig/meta"
---

# (Optional) Running AWS AppConfig as a DaemonSet in Amazon EKS

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appconfig/docs/appconfig-integration-containers-agent-daemon
> **target_lang:** meta — documentation tier. ALL sections preserved.



# (Optional) Running AWS AppConfig as a DaemonSet in Amazon EKS
<a name="appconfig-integration-containers-agent-daemon"></a>

With Amazon EKS, you can run AWS AppConfig Agent as a sidecar, which results in one agent container *per application pod*. Or, if you prefer, you can run AWS AppConfig Agent as a [DaemonSet](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/), which results in one agent container *per node in your cluster*. 

**Note**  
If you run AWS AppConfig Agent as a DaemonSet, the agent runs in a separate pod, which means you can't access it with calls to `localhost`. You must inject or otherwise discover the agent pod's IP address in order to call it.

To run AWS AppConfig Agent as a DaemonSet, create a manifest file with the following contents. Replace {{highlighted}} text with details for your application and environment. For {{AWS Region}}, specify an AWS Region code (for example, `us-west-1`). 

```
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: aws-appconfig-agent
  namespace: {{my_namespace}}
  labels:
    app: {{my_application_label}}
spec:
   selector:
    matchLabels:
      app: {{my_application_label}}
  template:
    metadata:
      labels:
        app: {{my_application_label}}
    spec:
      containers:
      - name: aws-appconfig-agent
        image: public.ecr.aws/aws-appconfig/aws-appconfig-agent:2.x
        ports:
        - name: http
          containerPort: 2772
          protocol: TCP
        env:
        - name: SERVICE_REGION
          value: {{AWS Region}}
        imagePullPolicy: IfNotPresent
      # set a high priority class to ensure the agent is running on every node
      priorityClassName: system-node-critical
```

Run the following command to apply the AWS AppConfig Agent DaemonSet to your cluster. Replace {{aws\_appconfig\_agent\_daemonset}} with the name of your DaemonSet manifest.

```
kubectl apply -f {{aws_appconfig_agent_daemonset}}.yml
```