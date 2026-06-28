---
id: "@specs/aws/datasync/docs/discovery-job-create"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Working with discovery jobs"
status: active
depends_on:
  - "@specs/aws/datasync/meta"
---

# Working with discovery jobs

> **source:** AWS Documentation
> **spec:id:** @specs/aws/datasync/docs/discovery-job-create
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Working with DataSync discovery jobs
<a name="discovery-job-create"></a>

After you deploy your AWS DataSync agent and add your on-premises storage system to DataSync Discovery, you can run discovery jobs to collect information about the system and get AWS migration recommendations. 

## Starting a discovery job
<a name="discovery-job-start"></a>

You can run a discovery job for up to 31 days. A storage system can have only one active discovery job at a time. The information that a discovery job collects is available for up to 60 days following the end of the job (unless you remove the related storage system from DataSync Discovery before that).

**Tip**  
DataSync Discovery can provide more accurate recommendations the longer your discovery job runs. We recommend running a discovery job for at least 14 days.

### Using the AWS CLI
<a name="discovery-job-start-cli"></a>

With the AWS Command Line Interface (AWS CLI), you can run a discovery job for as short as 1 hour.

1. Copy the following `start-discovery-job` command:

   ```
   aws datasync start-discovery-job \
     --storage-system-arn "{{your-storage-system-arn}}" \
     --collection-duration-minutes {{discovery-job-duration}}
   ```

1. Specify the following parameters in the command:
   + `--storage-system-arn` – Specify the Amazon Resource Name (ARN) of the [on-premises storage system that you added](discovery-configure-storage.md#discovery-add-storage) to DataSync Discovery.
   + `--collection-duration-minutes` – Specify how long that you want the discovery job to run in minutes. Enter a value between `60` (1 hour) and `44640` (31 days).

1. Run the `start-discovery-job` command.

   You get a response that shows the discovery job that you just started.

   ```
   {
       "DiscoveryJobArn": "arn:aws:datasync:us-east-1:123456789012:system/storage-system-abcdef01234567890/job/discovery-job-12345678-90ab-cdef-0abc-021345abcdef6"
   }
   ```

Shortly after starting the discovery job, you can begin [looking at the information that the job collects](discovery-understand-findings.md#discovery-view-metrics) (including storage system capacity and usage).

## Stopping a discovery job
<a name="discovery-job-stop"></a>

Stop a discovery job at any time. You can still [get recommendations](discovery-understand-recommendations.md#discovery-understand-recommendations-view) for a stopped job.

### Using the AWS CLI
<a name="discovery-job-stop-cli"></a>

1. Copy the following `stop-discovery-job` command:

   ```
   aws datasync stop-discovery-job --discovery-job-arn "{{your-discovery-job-arn}}"
   ```

1. For `--discovery-job-arn`, specify the ARN of the discovery job that's currently running.

1. Run the `stop-discovery-job` command.

   If successful, you get an HTTP 200 response with an empty HTTP body.