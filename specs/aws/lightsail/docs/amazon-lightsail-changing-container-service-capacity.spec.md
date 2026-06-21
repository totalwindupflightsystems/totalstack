---
id: "@specs/aws/lightsail/docs/amazon-lightsail-changing-container-service-capacity"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Change container capacity"
status: active
depends_on:
  - "@specs/aws/lightsail/meta"
---

# Change container capacity

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lightsail/docs/amazon-lightsail-changing-container-service-capacity
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Scale capacity for your Lightsail container service
<a name="amazon-lightsail-changing-container-service-capacity"></a>

The capacity of your Amazon Lightsail container service is made up of its scale and power. The scale specifies the number of compute nodes in your container service, and the power specifies the memory and vCPUs of each node in your service. You pick the scale based on the number of nodes you want powering your service for better availability and higher capacity

By following the procedure in this guide, you can dynamically increase the power and scale of your container service at any time without any down-time if you find that it's under-provisioned, or decrease it if you find that it's over-provisioned. Lightsail automatically manages the capacity change along with your current deployment.

**Note**  
If you create a new deployment, then the existing utilization metrics of your container service will disappear, and only metrics for the new current deployment will be shown.

For more information about container services, see [Container services](amazon-lightsail-container-services.md).

## Change the capacity of your container service
<a name="change-container-service-capacity"></a>

Complete the following procedure to change the capacity of your Lightsail container service.

1. Sign in to the [Lightsail console](https://lightsail.aws.amazon.com/).

1. In the left navigation pane, choose **Containers**.

1. Choose the name of the container service for which you want to change the capacity.

1. On the container service management page, choose the **Capacity** tab.

   The current power, scale, and monthly price of your container service is displayed in the **Capacity** page.

1. Choose **Change capacity** to change the power and scale to something else.

1. On the confirmation prompt that appears, choose **Yes, continue** to acknowledge that changing the capacity of your container service will re-deploy the current deployment.

1. Choose the new power and scale of your container service.

1. Choose **Yes, apply** to apply the new capacity to your container service.

   The status of your container service changes to **Updating**. After a few moments, the status of your service changes to **Enabled**, and it begins operating under its new capacity.