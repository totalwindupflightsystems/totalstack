---
id: "@specs/aws/lightsail/docs/amazon-lightsail-viewing-container-service-container-logs"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS View container logs"
status: active
depends_on:
  - "@specs/aws/lightsail/meta"
---

# View container logs

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lightsail/docs/amazon-lightsail-viewing-container-service-container-logs
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Analyze Lightsail container service logs
<a name="amazon-lightsail-viewing-container-service-container-logs"></a>

Every container in your Amazon Lightsail container service deployment generates a log. The container logs provide the stdout and stderr streams of processes that run inside your containers. Access your containers' logs periodically to diagnose their operations. The latest three days of log entries are stored before the oldest ones are replaced by the newest entries.

## Filter container logs
<a name="filtering-log"></a>

Container logs can have hundreds of entries per day. Use the filtering options to reduce the number of entries displayed in your log window, and make it easier to find what you're looking for. You can filter container logs by a start and end date (in local time), and by a specific term. When filtering by a term, you can choose to include or exclude log entries for the term you specify.

![Container service log filters in the Lightsail console](http://docs.aws.amazon.com/lightsail/latest/userguide/images/container-service-container-log-filter.png)


The *include* or *exclude* filter term looks for an exact match that is case-sensitive. For example, if you specify to include only log events that have `HTTP` in the message, then you will see all log events that include `HTTP` in the message, but none that include `http` in the message. If you specify to exclude `Error`, then you will see all log events that don't include `Error` in the message, and you will also see log events that include `ERROR` in the message.

## Prerequisites
<a name="view-contgainer-logs-prerequisites"></a>

Before you get started, you need to create a Lightsail container service. For more information, see [Creating Amazon Lightsail container services](amazon-lightsail-creating-container-services.md).

You also should create a deployment in your container service that configures and launches your containers. For more information, see [Creating and managing deployments for your Amazon Lightsail container services](amazon-lightsail-container-services-deployments.md).

## View the container logs
<a name="view-contgainer-logs"></a>

Complete the following procedure to view the container logs of your Lightsail container service.

1. Sign in to the [Lightsail console](https://lightsail.aws.amazon.com/).

1. In the left navigation pane, choose **Containers**.

1. Choose the name of the container service for which you want to view the container logs.

1. On the container service management page, choose the **Deployments** tab.

   The **Deployments** page lists your current deployment and deployment versions, if any.

1. Choose one of the following options to view container logs:
   + To access the container logs of the current deployment, choose **Open log** for the container entries under the **Current deployment** section of the page.
   + To access the container logs of a previous deployment, choose the actions menu icon (⋮) for a previous deployment under the **Deployment versions** section of the page, and then choose **Show details**. In the **Version details** page that appears, choose Open log for the container entries that are listed.

   The container log opens in a new browser window. You can scroll down to view more log entries, and refresh the page to load the newest set of entries. The filtering options are displayed at the bottom of the page.
**Note**  
Log entries are displayed in ascending order, and in Coordinated Universal Time (UTC). That is, the oldest log entries are at the top, and you must scroll down to see newer log entries.  
![Container log in the Lightsail console](http://docs.aws.amazon.com/lightsail/latest/userguide/images/container-service-container-log.png)