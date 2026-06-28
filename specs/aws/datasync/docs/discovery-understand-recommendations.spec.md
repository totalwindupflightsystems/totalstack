---
id: "@specs/aws/datasync/docs/discovery-understand-recommendations"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Getting recommendations"
status: active
depends_on:
  - "@specs/aws/datasync/meta"
---

# Getting recommendations

> **source:** AWS Documentation
> **spec:id:** @specs/aws/datasync/docs/discovery-understand-recommendations
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Getting recommendations from AWS DataSync Discovery
<a name="discovery-understand-recommendations"></a>

After AWS DataSync Discovery collects information about your on-premises storage system, it can recommend moving your data on a per-resource basis to one or more of the following AWS storage services:
+ [Amazon FSx for NetApp ONTAP](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/what-is-fsx-ontap.html)
+ [Amazon Elastic File System (Amazon EFS)](https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html)
+ [Amazon FSx for Windows File Server](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/what-is.html)

## What's included in the recommendations?
<a name="discovery-understand-recommendations-how"></a>

DataSync Discovery recommendations include storage configurations and cost estimates to help you choose the AWS storage service that works for your data.

### AWS storage configuration
<a name="discovery-understand-recommendations-storage-configs"></a>

DataSync Discovery provides information about how you might want to configure a recommended AWS storage service. The storage configuration is designed to optimize costs while helping meet storage performance and capacity needs based on information that's collected during a discovery job.

The storage configuration is only an approximation and might not account for all capabilities provided by an AWS storage service. For more information, see [What's not included in the recommendations?](#discovery-understand-recommendations-how-not)

### Estimated cost
<a name="discovery-understand-recommendations-estimated-cost"></a>

DataSync Discovery provides an estimated monthly cost for each AWS storage service that it recommends. The cost is based on standard AWS pricing and provides only an estimate of your AWS fees. It does not include any taxes that might apply. Your actual fees depend on a variety of factors, including your usage of AWS services.

The estimated cost also doesn't include the one-time or periodic fees for migrating your data to AWS.

## What's not included in the recommendations?
<a name="discovery-understand-recommendations-how-not"></a>

DataSync Discovery won't recommend an AWS storage service that doesn't meet your storage configuration needs.

Additionally, the following AWS storage capabilities currently aren't accounted for when recommendations are determined:
+ **Amazon FSx for NetApp ONTAP** – Single-AZ deployments and backup storage
+ **Amazon EFS** – EFS One Zone storage classes and backup storage
+ **Amazon FSx for Windows File Server** – Single-AZ deployments and backup storage

## Getting recommendations
<a name="discovery-understand-recommendations-view"></a>

You can generate AWS storage recommendations after your discovery job completes, when you stop the job, and even sometimes if the job completes but had some issues collecting information from your storage system.

There might be situations when you can't get recommendations (for example, if your discovery job fails). For more information, see [Recommendation statuses](discovery-job-statuses.md#recommendation-statuses-table).

**Tip**  
Before starting your migration to AWS, review the DataSync Discovery recommendations with your AWS account team.

### Using the AWS CLI
<a name="view-recommendations-cli"></a>

1. Copy the following `describe-discovery-job` command:

   ```
   aws datasync describe-discovery-job --discovery-job-arn "{{your-discovery-job-arn}}"
   ```

1. For the `--discovery-job-arn` parameter, specify the Amazon Resource Name (ARN) of the [discovery job](discovery-job-create.md#discovery-job-start) that you ran on the storage system.

1. Run the `describe-discovery-job` command.

   If your response includes a `Status` that isn't `FAILED`, you can continue. If you see `FAILED`, you must run another discovery job on your storage system to try to generate recommendations.

1. If your discovery job completed successfully, skip this step. Otherwise, do the following to manually generate recommendations:

   1. Copy the following `generate-recommendations` command:

      ```
      aws datasync generate-recommendations \
        --discovery-job-arn "{{your-discovery-job-arn}}" \
        --resource-type {{cluster-svm-volume}} \
        --resource-ids {{storage-resource-UUIDs}}
      ```

   1. For the `--discovery-job-arn` parameter, specify the ARN of the same discovery job that you specified in Step 2.

   1. For the `--resource-type` parameter, specify `CLUSTER`, `SVM`, or `RESOURCE` depending on the kind of resource you want recommendations on.

   1. For the `--resource-ids` parameter, specify universally unique identifiers (UUIDs) of the resources that you want recommendations on.

   1. Run the `generate-recommendations` command.

   1. Wait until the `RecommendationStatus` element in the response has a `COMPLETED` status, then move to the next step.

1. Copy the following `describe-storage-system-resources` command:

   ```
   aws datasync describe-storage-system-resources \
     --discovery-job-arn "{{your-discovery-job-arn}}" \
     --resource-type {{cluster-svm-volume}}
   ```

1. Specify the following parameters in the command:
   + `--discovery-job-arn` – Specify the ARN of the same discovery job that you specified in Step 2.
   + `--resource-type` – Specify the resource type you generated recommendations on (for example, `VOLUME`).

1. Run the `describe-storage-system-resources` command.
**Note**  
In the response, if you don't see `COMPLETED` for `RecommendationStatus`, check the [recommendation statuses](https://docs.aws.amazon.com/datasync/latest/userguide/discovery-job-statuses.html#recommendation-statuses-table) for more information. You may need to retry generating recommendations.

   In this example response, the `Recommendations` element suggests a couple AWS storage services where you can migrate a specific volume, how you might configure the service, and estimated monthly AWS storage costs.

   ```
   {
       "Recommendations": [{
               "StorageType": "fsxOntap",
               "StorageConfiguration": {
                   "StorageCapacityGB": "1024",
                   "ProvisionedIOpsMode": "AUTOMATIC",
                   "CapacityPoolGB": "0",
                   "TotalIOps": "0",
                   "DeploymentType": "Multi-AZ",
                   "ThroughputCapacity": "128"
               },
               "EstimatedMonthlyStorageCost": "410.0"
           },
           {
               "StorageType": "efs",
               "StorageConfiguration": {
                   "InfrequentAccessStorageGB": "1",
                   "StandardStorageGB": "1",
                   "InfrequentAccessRequests": "0",
                   "ProvisionedThroughputMBps": "0",
                   "PerformanceMode": "General Purpose",
                   "ThroughputMode": "Bursting"
               },
               "EstimatedMonthlyStorageCost": "1.0"
           }
       ],
       "RecommendationStatus": "COMPLETED"
   }
   ```