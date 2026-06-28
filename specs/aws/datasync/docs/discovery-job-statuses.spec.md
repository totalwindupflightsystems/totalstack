---
id: "@specs/aws/datasync/docs/discovery-job-statuses"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DataSync Discovery statuses"
status: active
depends_on:
  - "@specs/aws/datasync/meta"
---

# DataSync Discovery statuses

> **source:** AWS Documentation
> **spec:id:** @specs/aws/datasync/docs/discovery-job-statuses
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AWS DataSync Discovery statuses
<a name="discovery-job-statuses"></a>

You can check the status of your discovery jobs and whether AWS DataSync Discovery can provide storage recommendations for your AWS migrations.

## Discovery job statuses
<a name="discovery-job-statuses-table"></a>

Use the following table to understand what's going on with your discovery job.


| API status | Description | 
| --- | --- | 
| `RUNNING` | Your discovery job is running. The job collects data about your on-premises storage system for the duration that you specified. | 
| `WARNING` | Your discovery job has encountered errors and currently can't collect data. Review the Amazon CloudWatch logs and address these issues within 12 hours, or the job will be terminated. | 
| `STOPPED` | You stopped your discovery job before the job was expected to finish. | 
| `COMPLETED` | Your discovery job successfully collected all data from your on-premises storage system. | 
| `COMPLETED_WITH_ISSUES` | There were times during the discovery job when DataSync Discovery couldn't collect data. For details, see your CloudWatch logs. | 
| `TERMINATED` | Your discovery job was canceled because of unresolved issues and some data wasn’t collected. For details, see your CloudWatch logs. | 
| `FAILED` | Your discovery job encountered issues and couldn’t collect data from your on-premises storage system. For details, see your CloudWatch logs. | 

## Recommendation statuses
<a name="recommendation-statuses-table"></a>

Use the following table to understand whether DataSync Discovery recommendations for a specific on-premises storage resource are ready to view. 


| API status | Description | 
| --- | --- | 
| `NONE` | You can't generate recommendations yet. Try generating recommendations when your discovery job completes. | 
| `NONE` | Your discovery job collected enough data for DataSync Discovery to provide recommendations. You may be able to generate recommendations if you stopped the discovery job early or the job completed but had issues with data collection. | 
| `IN_PROGRESS` | DataSync Discovery is working on your recommendations. How long this takes depends on how many resources you're generating recommendations for. If you're using the console, it may take a few minutes to generate recommendations for a storage resource. | 
| `COMPLETED` | You can view your recommendations. | 
| `FAILED` | DataSync Discovery couldn't generate recommendations. You can review your CloudWatch logs to identify the issue and try generating the recommendations again. | 
| `NONE` | Recommendations aren't available. You may see this status for a failed discovery job or issue with the storage resource. | 
|  `COMPLETED`  | DataSync Discovery currently doesn't support an AWS storage service that meets the needs of the storage resource. | 