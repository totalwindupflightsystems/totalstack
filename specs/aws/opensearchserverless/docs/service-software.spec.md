---
id: "@specs/aws/opensearchserverless/docs/service-software"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Service software updates"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Service software updates

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/service-software
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Service software updates in Amazon OpenSearch Service
<a name="service-software"></a>

**Note**  
For explanations of the changes and additions made in each *major* (non-patch) service software update, see the [release notes](release-notes.md).

Amazon OpenSearch Service regularly releases service software updates that add features or otherwise improve your domains. The **Notifications** panel in the console is the easiest way to see if an update is available or to check the status of an update. Each notification includes details about the service software update. All service software updates use blue/green deployments to minimize downtime.

Service software updates differ from OpenSearch Service *version* upgrades. For information about upgrading to a later version of OpenSearch Service, see [Upgrading Amazon OpenSearch Service domains](version-migration.md).

 OpenSearch Service requires you to apply required service software updates within 30 days of their availability. These updates are critical for maintaining security compliance. 

 If you don't apply required updates within the 30-day period, you'll receive reminder notifications every 15 days for 30 days. After this period without compliance, your domain will be isolated with the following effects: 
+ All network access to your domain is removed
+ Domain status changes to **isolated**
+ The domain remains unusable until you apply the required updates

 During isolation, you'll continue receiving reminder notifications every 15 days for 60 days. If you don't apply the required updates within this period, your OpenSearch Service domain and all associated data will be permanently deleted. For more information, see [Troubleshooting validation errors](managedomains-configuration-changes.md#validation).

## Optional versus required updates
<a name="service-software-optional-required"></a>

OpenSearch Service has two broad categories of service software updates:

### Optional updates
<a name="service-software-optional"></a>

Optional service software updates generally include enhancements and support for new features or functionality. Optional updates aren't enforced on your domains, and there's no hard deadline to install them. The availability of the update is communicated through email and a console notification. You can choose to apply the update immediately or reschedule it for a more appropriate date and time. You can also schedule it during the domain's [off-peak window](off-peak.md). The majority of software updates are optional.

Regardless of whether or not you schedule an update, if the `UseLatestServiceSoftwareForBlueGreen` setting is enabled and you make a change on the domain that causes a [blue/green deployment](managedomains-configuration-changes.md), OpenSearch Service automatically updates your service software for you. If this setting is disabled, the service software is not automatically updated during a blue/green deployment.

You can configure your domain to automatically apply optional updates during [off-peak hours](off-peak.md). When this option is turned on, OpenSearch Service waits at least 13 days from when an optional update is available and then schedules the update after seven days. You receive a console notification when the update is scheduled and you can choose to reschedule it for a later date.

To turn on automatic software updates, select **Enable automatic software update** when you create or update your domain. To configure the same setting using the AWS CLI, set `--software-update-options` to `true` when you create or update your domain.

### Required updates
<a name="service-software-required"></a>

Required service software updates generally include critical security fixes or other mandatory updates to ensure the continued integrity and functionality of your domain. Examples of required updates are Log4j Common Vulnerabilities and Exposures (CVEs) and enforcement of Instance Metadata Service Version 2 (IMDSv2). The number of mandatory updates in a year is usually less than three.

OpenSearch Service automatically schedules these updates and notifies you seven days before the scheduled update through email and a console notification. You can choose to apply the update immediately or reschedule it for a more appropriate date and time *within the allowed timeframe.* You can also schedule it during the domain's next [off-peak window](off-peak.md). If you take no action on a required update and you don't make any domain changes that cause a blue/green deployment, OpenSearch Service can initiate the update at any time beyond the specified deadline (typically 14 days from availability), within the domain's off-peak window.

Regardless of when the update is scheduled for, if the `UseLatestServiceSoftwareForBlueGreen` setting is enabled and you make a change on the domain that causes a [blue/green deployment](managedomains-configuration-changes.md), OpenSearch Service automatically updates your domain for you. If this setting is disabled, the service software is not automatically updated during a blue/green deployment.

## Patch updates
<a name="service-software-patches"></a>

Service software versions that end in "-P" and a number, such as R20211203-{{P4}}, are patch releases. Patches are likely to include performance improvements, minor bug fixes, and security fixes or posture improvements. Patch releases do not include new features or breaking changes, and they generally don't have a direct or noticeable impact on users. The service software notification tells you if a patch release is optional or mandatory.

## Considerations
<a name="service-software-considerations"></a>

Consider the following when deciding whether to update your domain:
+ Manually updating your domain lets you take advantage of new features more quickly. When you choose **Update**, OpenSearch Service places the request in a queue and begins the update when it has time. 
+ When you initiate a service software update, OpenSearch Service sends a notification when the update starts and when it completes.
+ Software updates use blue/green deployments to minimize downtime. Updates can temporarily strain a cluster's dedicated master nodes, so make sure to maintain sufficient capacity to handle the associated overhead.
+ Updates typically complete within minutes, but can also take several hours or even days if your system is experiencing heavy load. Consider updating your domain during the configured [off-peak window](off-peak.md) to avoid long update periods. 

**Note**  
The `UseLatestServiceSoftwareForBlueGreen` setting is disabled by default. When enabled, any blue/green deployment on your domain automatically applies the latest available service software update along with the configuration change. To enable this setting, use the `UpdateDomainConfig` API or the AWS CLI.

## Starting a service software update
<a name="service-software-requesting"></a>

You can request a service software update through the OpenSearch Service console, the AWS CLI, or one of the SDKs. 

### Console
<a name="service-software-request-console"></a>

**To request a service software update**

1. Open the Amazon OpenSearch Service console at [https://console.aws.amazon.com/aos/home](https://console.aws.amazon.com/aos/home).

1. Select the domain name to open its configuration.

1. Choose **Actions**, **Update** and select one of the following options:
   + **Apply update now** - Immediately schedules the action to happen in the current hour *if there's capacity available*. If capacity isn't available, we provide other available time slots to choose from.
   + **Schedule it in off-peak window** – Only available if the off-peak window is enabled for the domain. Schedules the update to take place during the domain's configured off-peak window. There's no guarantee that the update will happen during the next immediate window. Depending on capacity, it might happen in subsequent days. For more information, see [Scheduling software updates during off-peak windows](#service-software-offpeak).
   + **Schedule for specific date and time** – Schedules the update to take place at a specific date and time. If the time that you specify is unavailable for capacity reasons, you can select a different time slot.

   If you schedule the update for a later date (within or outside the domain's off-peak window), you can reschedule it at any time. For instructions, see [Rescheduling actions](off-peak.md#off-peak-reschedule).

1. Choose **Confirm**.

### AWS CLI
<a name="service-software-request-cli"></a>

Send a [start-service-software-update](https://docs.aws.amazon.com/cli/latest/reference/opensearch/start-service-software-update.html) AWS CLI request to initiate a service software update. This example adds the update to the queue immediately:

```
aws opensearch start-service-software-update \
  --domain-name {{my-domain}} \
  --schedule-at "NOW"
```

**Response**:

```
{
    "ServiceSoftwareOptions": {
        "CurrentVersion": "R20220928-P1",
        "NewVersion": "R20220928-P2",
        "UpdateAvailable": true,
        "Cancellable": true,
        "UpdateStatus": "PENDING_UPDATE",
        "Description": "",
        "AutomatedUpdateDate": "1969-12-31T16:00:00-08:00",
        "OptionalDeployment": true
    }
}
```

**Tip**  
After you request an update, you have a narrow window of time in which you can cancel it. The duration of this `PENDING_UPDATE` state can vary greatly and depends on your AWS Region and the number of concurrent updates that OpenSearch Service is performing. To cancel an update, use the console or `cancel-service-software-update` AWS CLI command.

If the request fails with a `BaseException`, it means that the time you specified isn't available for capacity reasons, and you must specify a different time. OpenSearch Service provides alternate available slot suggestions in the response.

### AWS SDKs
<a name="service-software-request-sdk"></a>

This sample Python script uses the [describe\_domain](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch.html#OpenSearchService.Client.describe_domain) and [start\_service\_software\_update](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch.html#OpenSearchService.Client.start_service_software_update) methods from the AWS SDK for Python (Boto3) to check whether a domain is eligible for a service software update and if so, starts the update. You must provide a value for `domain_name`.

```
import boto3
from botocore.config import Config
import time

# Build the client using the default credential configuration.
# You can use the CLI and run 'aws configure' to set access key, secret
# key, and default region.

my_config = Config(
    # Optionally lets you specify a Region other than your default.
    region_name='us-east-1'
)

domain_name = ''  # The name of the domain to check and update

client = boto3.client('opensearch', config=my_config)


def getUpdateStatus(client):
    """Determines whether the domain is eligible for an update"""
    response = client.describe_domain(
        DomainName=domain_name
    )
    sso = response['DomainStatus']['ServiceSoftwareOptions']
    if sso['UpdateStatus'] == 'ELIGIBLE':
        print('Domain [' + domain_name + '] is eligible for a service software update from version ' +
              sso['CurrentVersion'] + ' to version ' + sso['NewVersion'])
        updateDomain(client)
    else:
        print('Domain is not eligible for an update at this time.')


def updateDomain(client):
    """Starts a service software update for the eligible domain"""
    response = client.start_service_software_update(
        DomainName=domain_name
    )
    print('Updating domain [' + domain_name + '] to version ' +
          response['ServiceSoftwareOptions']['NewVersion'] + '...')
    waitForUpdate(client)


def waitForUpdate(client):
    """Waits for the domain to finish updating"""
    response = client.describe_domain(
        DomainName=domain_name
    )
    status = response['DomainStatus']['ServiceSoftwareOptions']['UpdateStatus']
    if status == 'PENDING_UPDATE' or status == 'IN_PROGRESS':
        time.sleep(30)
        waitForUpdate(client)
    elif status == 'COMPLETED':
        print('Domain [' + domain_name +
              '] successfully updated to the latest software version')
    else:
        print('Domain is not currently being updated.')

def main():
    getUpdateStatus(client)
```

## Scheduling software updates during off-peak windows
<a name="service-software-offpeak"></a>

Each OpenSearch Service domain created after February 16, 2023 has a daily 10-hour window between 10:00 P.M. and 8:00 A.M. local time that we consider the [off-peak window](off-peak.md). OpenSearch Service uses this window to schedule service software updates for the domain. Off-peak updates help to minimize strain on a cluster's dedicated master nodes during higher traffic periods. OpenSearch Service can't initiate updates outside of this 10-hour window without your consent.
+ For *optional* updates, OpenSearch Service notifies you of the update's availability and prompts you to schedule the update during an upcoming off-peak window.
+ For *required* updates, OpenSearch Service automatically schedules the update during an upcoming off-peak window and notifies you three days ahead of time. You can reschedule the update (for within or outside the off-peak window), but only within the required timeframe for the update to be completed.

For each domain, you can choose to override the default 10:00 P.M. start time with a custom time. For instructions, see [Configuring a custom off-peak window](off-peak.md#off-peak-custom).

### Console
<a name="service-software-offpeak-console"></a>

**To schedule an update during an upcoming off-peak window**

1. Open the Amazon OpenSearch Service console at [https://console.aws.amazon.com/aos/home](https://console.aws.amazon.com/aos/home ).

1. Select the domain name to open its configuration.

1. Choose **Actions**, **Update**.

1. Select **Schedule it in off-peak window**.

1. Choose **Confirm**.

You can view the scheduled action on the **Off-peak window** tab and reschedule it at any time. See [Viewing scheduled actions](off-peak.md#off-peak-view).

### CLI
<a name="service-software-offpeak-cli"></a>

To schedule an update during an upcoming off-peak window using the AWS CLI, send a [StartServiceSoftwareUpdate](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_StartServiceSoftwareUpdate.html) request and specify `OFF_PEAK_WINDOW` for the `--schedule-at` parameter:

```
aws opensearch start-service-software-update \
  --domain-name {{my-domain}} \
  --schedule-at "OFF_PEAK_WINDOW"
```

## Monitoring service software updates
<a name="service-software-monitor"></a>

OpenSearch Service sends a [notification](managedomains-notifications.md) when a service software update is available, required, started, completed, or failed. You can view these notifications on the **Notifications** panel of the OpenSearch Service console. The notification severity is `Informational` if the update is optional and `High` if it's required. 

OpenSearch Service also sends service software events to Amazon EventBridge. You can use EventBridge to configure rules that send an email or perform a specific action when an event is received. For an example walk through, see [Tutorial: Sending Amazon SNS alerts for available software updates](sns-events.md).

To see the format of each service software event sent to Amazon EventBridge, see [Service software update events](monitoring-events.md#monitoring-events-sso).

## When domains are ineligible for an update
<a name="service-software-ineligible"></a>

Your domain is ineligible for a service software update if it's in any of the following states:


| State | Description | 
| --- | --- | 
| Domain in processing | The domain is in the middle of a configuration change. Check update eligibility after the operation completes. | 
| Red cluster status | One or more indexes in the cluster is red. For troubleshooting steps, see [Red cluster status](handling-errors.md#handling-errors-red-cluster-status). | 
| High error rate | The OpenSearch cluster is returning a large number of 5*xx* errors when attempting to process requests. This problem is usually the result of too many simultaneous read or write requests. Consider reducing traffic to the cluster or scaling your domain. | 
| Split brain | *Split brain* means your OpenSearch cluster has more than one master node and has split into two clusters that never will rejoin on their own. You can avoid split brain by using the recommended number of [dedicated master nodes](managedomains-dedicatedmasternodes.md). For help recovering from split brain, contact [Support](https://console.aws.amazon.com/support/home). | 
| Amazon Cognito integration issue | Your domain uses [authentication for OpenSearch Dashboards](cognito-auth.md), and OpenSearch Service can't find one or more Amazon Cognito resources. This problem usually occurs if the Amazon Cognito user pool is missing. To correct the issue, recreate the missing resource and configure the OpenSearch Service domain to use it. | 
| Other service issue | Issues with OpenSearch Service itself might cause your domain to display as ineligible for an update. If none of the previous conditions apply to your domain and the problem persists for more than a day, contact [Support](https://console.aws.amazon.com/support/home). | 

## Rolling back a service software update
<a name="service-software-rollback"></a>

Amazon OpenSearch Service supports rolling back service software updates. You can initiate a rollback using the OpenSearch Service console, the AWS CLI, or one of the AWS SDKs. Software updates are rolled back using a blue/green deployment.

**Note**  
Rollback is supported only for service software updates applied on or after April 24, 2026. Engine version upgrades cannot be rolled back.

### Rollback eligibility and considerations
<a name="service-software-rollback-eligibility"></a>

Your domain must meet all of the following conditions for a rollback to be available:
+ **Domain is active** – The domain must be in an `Active` state. Rollback is not available while a configuration change, software update, or other blue/green deployment is in progress.
+ **Within the rollback time window** – The software update must have been applied within the allowed rollback period. See [Rollback time windows](#service-software-rollback-windows).
+ **No configuration changes after the update** – If you made a configuration change to the domain after the software update was applied, rollback is blocked. Configuration changes can affect domain settings in ways that are incompatible with the previous software version. For example, changing instance types, enabling replicas, or adjusting storage settings after an update will block rollback.
+ **Update was not auto-applied by the service** – If you did not act on a mandatory update within the 30-day availability window and OpenSearch Service applied the update automatically, rollback is not available for that update.
+ **Update was not an engine version upgrade** – Engine version changes (for example, upgrading from OpenSearch 1.3 to OpenSearch 2.11) are irreversible. Only service software version rollbacks are supported.
+ **A previous software version exists** – Rollback is available only for software updates applied after this feature became generally available (GA). Domains that have not yet undergone a software update since GA do not have a previous version to roll back to.
+ **Only one rollback is permitted per update** – Once a rollback is complete, the domain is considered to be in a rolled-back state. You cannot roll back again until a new software update has been successfully applied.
+ **Software update was explicitly initiated** – Rollback is only available when the software update was explicitly initiated by you or automatically scheduled by OpenSearch Service as part of a mandatory or optional update. Rollback is not available when:
  + The software update was applied during a blue/green deployment triggered by a configuration change. This includes cases where the `UseLatestServiceSoftwareForBlueGreen` setting is enabled, which bundles the latest software update with configuration changes. This setting is disabled by default.
  + The update was applied during a service-initiated maintenance operation on your domain, such as infrastructure recovery, automated remediation, or other internal operations performed by OpenSearch Service to maintain the health and availability of your domain.

### Rollback time windows
<a name="service-software-rollback-windows"></a>

The rollback window depends on the type of software update that was applied.


| Update type | Rollback window | Notes | 
| --- | --- | --- | 
| Optional | 15 days from the date the update was applied | Applies whether you applied the update manually, scheduled it, or it was applied automatically during off-peak hours. | 
| Mandatory | 15 days from the date the update was applied | Available only if you applied the update yourself within the 30-day availability window. If the service auto-applied the update after the deadline, rollback is not available. | 

After the rollback window expires, self-service rollback is no longer available. Contact [Support](https://console.aws.amazon.com/support/home) if you are experiencing a critical issue after the window has closed.

### How to request a rollback
<a name="service-software-rollback-requesting"></a>

You can request a rollback using the `RollbackServiceSoftwareUpdate` API.

#### Request
<a name="service-software-rollback-request"></a>

```
POST /2021-01-01/opensearch/serviceSoftwareUpdate/rollback
```

Request body:

```
{
    "DomainName": "{{your-domain-name}}"
}
```

#### Response
<a name="service-software-rollback-response"></a>

The API returns an HTTP 200 response in all non-error cases. The `RollbackAvailable` field in the response body indicates whether the rollback was initiated.

```
{
    "RollbackServiceSoftwareOptions": {
        "CurrentVersion": "string",
        "NewVersion": "string",
        "RollbackAvailable": boolean,
        "Description": "string"
    }
}
```

Response fields:


| Field | Type | Description | 
| --- | --- | --- | 
| CurrentVersion | String | The software version currently running on the domain. | 
| NewVersion | String | The software version the domain will be rolled back to. Returns null if rollback is not available. | 
| RollbackAvailable | Boolean | `true` if the rollback has been successfully initiated. `false` if the domain is not eligible for rollback. | 
| Description | String | A human-readable message describing the result or the reason rollback is unavailable. | 

#### Error responses
<a name="service-software-rollback-errors"></a>


| Error | Description | 
| --- | --- | 
| ResourceNotFoundException | The specified domain does not exist. | 
| ValidationException | The domain is not in an active state. Wait for any in-progress changes to complete before retrying. | 
| InternalException | The service encountered an internal error. Retry the request. | 
| DisabledOperationException | The rollback operation is not supported for this domain. | 

#### Response messages
<a name="service-software-rollback-messages"></a>

The following table describes the possible response messages returned by the `RollbackServiceSoftwareUpdate` API.


| Case | Description | 
| --- | --- | 
| Success | Rollback initiated successfully. The domain will be rolled back from {{current-version}} to {{previous-version}}. | 
| Feature not enabled | Rollback is not available. Contact [Support](https://console.aws.amazon.com/support/home) for assistance. | 
| Previous software not available | No previous software version available for rollback. Contact [Support](https://console.aws.amazon.com/support/home) for assistance. | 
| Previous software is same as current | Rollback is not available. No previous software version available for rollback. Contact [Support](https://console.aws.amazon.com/support/home) for assistance. | 
| Domain is already rolled back | Domain is already in a rolled-back state. | 
| Rollback not available | Rollback is not available. A service-side configuration is preventing rollback for this domain. Contact [Support](https://console.aws.amazon.com/support/home) for assistance. | 
| Outside the time window | Rollback is not available. The 15-day rollback window has expired. Contact [Support](https://console.aws.amazon.com/support/home) for assistance. | 
| Mandatory service update auto-applied | Rollback is not available. The current version was applied through a mandatory service update. Contact [Support](https://console.aws.amazon.com/support/home) for assistance. | 
| Engine version upgrade | Rollback is not available. Engine version upgrades are irreversible. Contact [Support](https://console.aws.amazon.com/support/home) for assistance. | 
| Configuration changed after update | Rollback is not available. Cluster configuration has changed since last software update. Contact [Support](https://console.aws.amazon.com/support/home) for assistance. | 

**Example response:**

```
{
    "RollbackServiceSoftwareOptions": {
        "CurrentVersion": "OpenSearch_2_11_R20240115",
        "NewVersion": "OpenSearch_2_11_R20231023",
        "RollbackAvailable": true,
        "Description": "Rollback initiated successfully. The domain will be rolled back from OpenSearch_2_11_R20240115 to OpenSearch_2_11_R20231023."
    }
}
```

When rollback is not available, `RollbackAvailable` returns `false` and the `Description` field contains the reason from the table above.