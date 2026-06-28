---
id: "@specs/aws/datasync/docs/working-with-locations"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Where can I transfer my data?"
status: active
depends_on:
  - "@specs/aws/datasync/meta"
---

# Where can I transfer my data?

> **source:** AWS Documentation
> **spec:id:** @specs/aws/datasync/docs/working-with-locations
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Where can I transfer my data with AWS DataSync?
<a name="working-with-locations"></a>

Where you can transfer your data with AWS DataSync depends on the following factors:
+ Your transfer's source and destination [locations](how-datasync-transfer-works.md#sync-locations)
+ If your locations are in different AWS accounts
+ If your locations are in different AWS Regions
+ If your are using Basic mode or Enhanced mode

## Supported transfers in the same AWS account
<a name="working-with-locations-same-account"></a>

DataSync supports transfers between the following storage resources that are associated with the same AWS account.


| Source | Destination | Requires an agent? | Supported task mode | 
| --- | --- | --- | --- | 
|  [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/working-with-locations.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/working-with-locations.html)  | Yes | Basic, Enhanced | 
|  [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/working-with-locations.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/working-with-locations.html)  | Yes | Basic only | 
|  [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/working-with-locations.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/working-with-locations.html)  | Yes | Basic only | 
|  [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/working-with-locations.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/working-with-locations.html)  | Only for Basic mode | Basic, Enhanced | 
|  [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/working-with-locations.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/working-with-locations.html)  | Yes | Basic only | 
|  [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/working-with-locations.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/working-with-locations.html)  | No | Basic, Enhanced | 
|  [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/working-with-locations.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/working-with-locations.html)  | No | Basic only | 
|  [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/working-with-locations.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/working-with-locations.html)  | Yes | Basic, Enhanced | 
|  [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/working-with-locations.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/working-with-locations.html)  | Yes | Basic only | 
|  [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/working-with-locations.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/working-with-locations.html)  | Only for Basic mode | Basic, Enhanced | 
|  [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/working-with-locations.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/working-with-locations.html)  | Yes | Basic only | 
|  [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/working-with-locations.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/working-with-locations.html)  | Yes | Basic only | 
|  [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/working-with-locations.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/working-with-locations.html)  | Yes | Basic only | 
|  [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/working-with-locations.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/working-with-locations.html)  | No | Basic only | 
|  [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/working-with-locations.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/working-with-locations.html)  | No | Basic only | 
|  [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/working-with-locations.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/working-with-locations.html)  | Yes | Basic only | 
|  [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/working-with-locations.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/working-with-locations.html)  | Yes | Basic only | 

## Supported transfers across AWS accounts
<a name="working-with-locations-across-accounts"></a>

DataSync supports some transfers between storage resources that are associated with different AWS accounts.


| Source | Destination | Requires an agent? | Supported task mode | 
| --- | --- | --- | --- | 
|  [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/working-with-locations.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/working-with-locations.html)  | Yes | Basic, Enhanced | 
|  [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/working-with-locations.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/working-with-locations.html)  | Yes | Basic only | 
|  [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/working-with-locations.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/working-with-locations.html)  | No | Basic, Enhanced | 
|  [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/working-with-locations.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/working-with-locations.html)  | No | Basic only | 
|  [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/working-with-locations.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/working-with-locations.html)  | Yes | Basic, Enhanced | 
|  [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/working-with-locations.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/working-with-locations.html)  | Yes | Basic only | 
|  [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/working-with-locations.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/working-with-locations.html)  | No | Basic only | 
|  [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/working-with-locations.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/working-with-locations.html)  | Yes (when used as an NFS/SMB location) | Basic only | 

1 Configured as an [NFS location](create-nfs-location.md).

2 Configured as an [SMB location](create-smb-location.md).

3 Configured as an NFS or SMB location.

## Supported transfers in the same AWS Region
<a name="working-with-locations-same-region"></a>

There are no restrictions when transferring data within the same AWS Region (including [opt-in Regions](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-regions.html)). For more information, see [AWS Regions supported by DataSync](https://docs.aws.amazon.com/general/latest/gr/datasync.html).

## Supported transfers between AWS Regions
<a name="working-with-locations-cross-regions"></a>

Note the following when transferring data between [AWS Regions supported by DataSync](https://docs.aws.amazon.com/general/latest/gr/datasync.html):
+ When transferring between AWS storage services in different AWS Regions, one of the two locations must be in the Region where you're using DataSync.
+ You can't transfer across Regions with an NFS, SMB, HDFS, or object storage location. In these situations, both of your transfer locations must be in the same Region where you [activate your DataSync agent](activate-agent.md).
+ With AWS GovCloud (US) Regions, you can:
  + Transfer between the AWS GovCloud (US-East) and AWS GovCloud (US-West) Regions.
  + Transfer between an AWS GovCloud (US) Region and commercial AWS Region, such as US East (N. Virginia). This type of transfer requires an [agent](agent-requirements.md) when transferring between Amazon EFS or Amazon FSx file systems.

**Important**  
You pay for data transferred between AWS Regions. This transfer is billed as data transfer out from the source to destination Region. For more information, see [AWS DataSync Pricing](https://aws.amazon.com/datasync/pricing/).

## Determining if your transfer requires a DataSync agent
<a name="datasync-transfer-requirements"></a>

Depending on your transfer scenario, you might need a DataSync agent. For more information, see [Do I need an AWS DataSync agent?](do-i-need-datasync-agent.md)