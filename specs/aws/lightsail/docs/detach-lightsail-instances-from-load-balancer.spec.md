---
id: "@specs/aws/lightsail/docs/detach-lightsail-instances-from-load-balancer"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Detach instances"
status: active
depends_on:
  - "@specs/aws/lightsail/meta"
---

# Detach instances

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lightsail/docs/detach-lightsail-instances-from-load-balancer
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Detach instances from a Lightsail load balancer
<a name="detach-lightsail-instances-from-load-balancer"></a>

If you no longer want to have an instance attached to your Amazon Lightsail load balancer, you can detach it. When you detach a Lightsail instance from a load balancer, we wait until the specified instances are no longer needed before detaching.

1. In the left navigation pane, choose **Networking**.

1. Choose the load balancer you want to manage.

1. On the **Target instances** tab, choose **Detach** next to the load balancer you want to detach.