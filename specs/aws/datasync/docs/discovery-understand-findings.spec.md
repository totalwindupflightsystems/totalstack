---
id: "@specs/aws/datasync/docs/discovery-understand-findings"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Viewing storage resource information"
status: active
depends_on:
  - "@specs/aws/datasync/meta"
---

# Viewing storage resource information

> **source:** AWS Documentation
> **spec:id:** @specs/aws/datasync/docs/discovery-understand-findings
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Viewing storage resource information collected by AWS DataSync Discovery
<a name="discovery-understand-findings"></a>

AWS DataSync Discovery collects information about your on-premises storage system that can help you understand how its storage resources are configured, performing, and utilized. DataSync Discovery uses this information to generate recommendations for migrating your data to AWS.

A discovery job can give you the following information about your storage system's resources (such as its volumes):
+ Total, available, and in use storage capacity
+ Number of Common Internet File System (CIFS) shares in a resource and whether a resource is available via Network File System (NFS)
+ Data transfer protocols
+ Performance (such as IOPS, throughput, and latency)

## Viewing information collected about your storage system
<a name="discovery-view-metrics"></a>

You can begin to see what kind of information DataSync Discovery is collecting about your on-premises storage system shortly after you start a discovery job.

You can view this information by using the following options:
+ **The [DescribeStorageSystemResources](https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeStorageSystemResources.html) operation** – Get data about all of the storage system resources that DataSync Discovery can collect information about, including utilization, capacity, and configuration data. 
+ ** The [DescribeStorageSystemResourceMetrics](https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeStorageSystemResourceMetrics.html) operation** – Get performance and capacity information that DataSync Discovery can collect about a specific resource in your storage system.

### Using the AWS CLI
<a name="discovery-view-metrics-cli"></a>

The following steps show how to use the [DescribeStorageSystemResources](https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeStorageSystemResources.html) operation with the AWS CLI.

1. Copy the following `describe-storage-system-resources` command:

   ```
   aws datasync describe-storage-system-resources \
     --discovery-job-arn "{{your-discovery-job-arn}}" \
     --resource-type "{{storage-system-resource-type}}"
   ```

1. Specify the following parameters in the command:
   + `--discovery-job-arn` – Specify the Amazon Resource Name (ARN) of the [discovery job](discovery-job-create.md#discovery-job-start) that you ran.
   + `--resource-type` – Specify one of the following values, depending on what kind of storage system resources you want information about:
     + `CLUSTER`
     + `SVM`
     + `VOLUME`

1. (Optional) Specify the `--resource-ids` parameter with the IDs of the storage system resources that you want information about.

1. Run the `describe-storage-system-resources` command.

   The following example response returns information that a discovery job collected about two volumes in a storage system.

   Note that the `RecommendationStatus` is `NONE` for each volume. To get AWS storage recommendations, you must run the `generate-recommendations` command before the `describe-storage-system-resources` command. For more information, see [Getting recommendations](discovery-understand-recommendations.md#discovery-understand-recommendations-view).

   ```
   {
       "ResourceDetails": {
           "NetAppONTAPVolumes": [
               {
                   "VolumeName": "vol1",
                   "ResourceId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
                   "CifsShareCount": 0,
                   "SecurityStyle": "unix",
                   "SvmUuid": "a1b2c3d4-5678-90ab-cdef-EXAMPLEaaaaa",
                   "SvmName": "my-svm",
                   "CapacityUsed": 409600,
                   "CapacityProvisioned": 1099511627776,
                   "LogicalCapacityUsed": 409600,
                   "NfsExported": true,
                   "SnapshotCapacityUsed": 573440,
                   "MaxP95Performance": {
                       "IopsRead": 251.0,
                       "IopsWrite": 44.0,
                       "IopsOther": 17.0,
                       "IopsTotal": 345.0,
                       "ThroughputRead": 2.06,
                       "ThroughputWrite": 0.88,
                       "ThroughputOther": 0.11,
                       "ThroughputTotal": 2.17,
                       "LatencyRead": 0.06,
                       "LatencyWrite": 0.07,
                       "LatencyOther": 0.13
                   },
                   "Recommendations": [],
                   "RecommendationStatus": "NONE"
               },
               {
                   "VolumeName": "root_vol",
                   "ResourceId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
                   "CifsShareCount": 0,
                   "SecurityStyle": "unix",
                   "SvmUuid": "a1b2c3d4-5678-90ab-cdef-EXAMPLEaaaaa",
                   "SvmName": "my-svm",
                   "CapacityUsed": 462848,
                   "CapacityProvisioned": 1073741824,
                   "LogicalCapacityUsed": 462848,
                   "NfsExported": true,
                   "SnapshotCapacityUsed": 421888,
                   "MaxP95Performance": {
                       "IopsRead": 261.0,
                       "IopsWrite": 53.0,
                       "IopsOther": 23.0,
                       "IopsTotal": 360.0,
                       "ThroughputRead": 10.0,
                       "ThroughputWrite": 2.0,
                       "ThroughputOther": 4.0,
                       "ThroughputTotal": 12.0,
                       "LatencyRead": 0.25,
                       "LatencyWrite": 0.3,
                       "LatencyOther": 0.55
                   },
                   "Recommendations": [],
                   "RecommendationStatus": "NONE"
               }
           ]
       }
   }
   ```