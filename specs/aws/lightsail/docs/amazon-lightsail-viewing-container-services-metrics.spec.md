---
id: "@specs/aws/lightsail/docs/amazon-lightsail-viewing-container-services-metrics"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Container metrics"
status: active
depends_on:
  - "@specs/aws/lightsail/meta"
---

# Container metrics

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lightsail/docs/amazon-lightsail-viewing-container-services-metrics
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Monitor Lightsail container service resource utilization
<a name="amazon-lightsail-viewing-container-services-metrics"></a>

After you create an Amazon Lightsail container service, you can view its metric graphs on the **Metrics** tab of the service’s management page. Monitoring metrics is an important part of maintaining the reliability, availability, and performance of your resources. Monitor and collect metric data from your resources regularly so that you can more readily debug a multi-point failure, if one occurs. For more information about metrics, see [Metrics in Amazon Lightsail](understanding-instance-health-metrics-in-amazon-lightsail.md).

When monitoring your resources, you should establish a baseline for normal resource performance in your environment.

**Note**  
Alarms and notifications are currently not supported for container service metrics.

## Container service metrics
<a name="container-service-metrics-available"></a>

The following container service metrics are available:
+ **CPU utilization** — The average percentage of compute units that are currently in use across all nodes of your container service. This metric identifies the processing power required to run containers on your container service.
+ **Memory utilization** — The average percentage of memory that is currently in use across all nodes of your container service. This metric identifies the memory required to run containers on your container service.

**Note**  
If you create a new deployment, then the existing utilization metrics of your container service will disappear, and only metrics for the new current deployment will be shown.

## View container service metrics in the Lightsail console
<a name="view-container-service-metrics"></a>

Complete the following procedure to view container service metrics in the Lightsail console.

1. Sign in to the [Lightsail console](https://lightsail.aws.amazon.com/).

1. In the left navigation pane, choose **Containers**.

1. Choose the name of the container for which you want to view metrics.

1. Choose the **Metrics** tab on the container service management page.

1. Choose the metric that you want to view in the dropdown menu under the **Metrics** graphs heading.

   The graph displays a visual representation of the data points for the chosen metric.

1. You can perform the following actions on the metrics graph:
   + Change the view of the graph to show data for 1 hour, 6 hours, 1 day, 1 week, 2 weeks, and Current month.
   + Pause your cursor on a data point to view detailed information about that data point.
**Note**  
Alarms and notifications are currently not supported for container service metrics.