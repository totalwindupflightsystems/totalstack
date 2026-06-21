---
id: "@specs/aws/lightsail/docs/enable-set-up-health-checking-for-lightsail-load-balancer-metrics"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Health checks"
status: active
depends_on:
  - "@specs/aws/lightsail/meta"
---

# Health checks

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lightsail/docs/enable-set-up-health-checking-for-lightsail-load-balancer-metrics
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Configure Lightsail load balancer health checks
<a name="enable-set-up-health-checking-for-lightsail-load-balancer-metrics"></a>

By default, Lightsail performs health checks on your instances at the root (`"/"`) of your web application. The health checks are used to monitor the health of the registered instances so that the load balancer can send requests only to the healthy instances. The health checks start as soon as you attach the instances to your load balancer.

One of the following statuses is returned.
+ Passed
+ Failed

If your health check fails, you can try to figure out what is wrong by using the AWS Command Line Interface or the Lightsail API. See our troubleshooting guide for more information.

## Customize your health check path
<a name="customize-health-check-path"></a>

You might want to customize your health check path. For example, if your home page loads slowly or has a lot of images on it, you can configure Lightsail to check a different page that loads faster.

1. In the left navigation pane, choose **Networking**.

1. Choose your load balancer to manage it.

1. On the **Target instances** tab, choose **Customize health checking**.

1. Type a valid path for your health check, and then choose **Save**.  
![Customize the health check path](http://docs.aws.amazon.com/lightsail/latest/userguide/images/customize-health-checking-path.png)