---
id: "@specs/aws/datasync/docs/create-lustre-location"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Configuring transfers with FSx for Lustre"
status: active
depends_on:
  - "@specs/aws/datasync/meta"
---

# Configuring transfers with FSx for Lustre

> **source:** AWS Documentation
> **spec:id:** @specs/aws/datasync/docs/create-lustre-location
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Configuring DataSync transfers with FSx for Lustre
<a name="create-lustre-location"></a>

To transfer data to or from your Amazon FSx for Lustre file system, you must create an AWS DataSync transfer *location*. DataSync can use this location as a source or destination for transferring data.

## Providing DataSync access to FSx for Lustre file systems
<a name="create-lustre-location-access"></a>

DataSync accesses your FSx for Lustre file system using the Lustre client. DataSync requires access to all data on your FSx for Lustre file system. To have this level of access, DataSync mounts your file system as the root user using a user ID (UID) and group ID (GID) of `0`.

DataSync mounts your file system from your virtual private cloud (VPC) using [network interfaces](required-network-interfaces.md). DataSync fully manages the creation, the use, and the deletion of these network interfaces on your behalf.

**Note**  
VPCs that you use with DataSync must have default tenancy. VPCs with dedicated tenancy aren't supported.

## Creating your FSx for Lustre transfer location
<a name="create-lustre-location-how-to"></a>

To create the transfer location, you need an existing FSx for Lustre file system. For more information, see [Getting started with Amazon FSx for Lustre](https://docs.aws.amazon.com/fsx/latest/LustreGuide/getting-started.html) in the *Amazon FSx for Lustre User Guide*.

### Using the DataSync console
<a name="create-lustre-location-how-to-console"></a>

1. Open the AWS DataSync console at [https://console.aws.amazon.com/datasync/](https://console.aws.amazon.com/datasync/).

1. In the left navigation pane, expand **Data transfer**, then choose **Locations** and **Create location**.

1. For **Location type**, choose **Amazon FSx**.

   You configure this location as a source or destination later. 

1. For **FSx file system**, choose the FSx for Lustre file system that you want to use as a location. 

1. For **Mount path**, enter the mount path for your FSx for Lustre file system.

   The path can include a subdirectory. When the location is used as a source, DataSync reads data from the mount path. When the location is used as a destination, DataSync writes all data to the mount path. If a subdirectory isn't provided, DataSync uses the root directory (`/`).

1. For **Security groups**, choose up to five security groups that provide access to your FSx for Lustre file system.

   The security groups must be able to access the file system's ports. The file system must also allow access from the security groups.

   For more information about security groups, see [File System Access Control with Amazon VPC](https://docs.aws.amazon.com/fsx/latest/LustreGuide/limit-access-security-groups.html) in the *Amazon FSx for Lustre User Guide*.

1. (Optional) Enter values for the **Key** and **Value** fields to tag the FSx for Lustre file system.

   Tags help you manage, filter, and search for your AWS resources. We recommend creating at least a name tag for your location. 

1. Choose **Create location**.

### Using the AWS CLI
<a name="create-location-lustre-cli"></a>

**To create an FSx for Lustre location by using the AWS CLI**
+ Use the following command to create an FSx for Lustre location.

  ```
  aws datasync create-location-fsx-lustre \
      --fsx-filesystem-arn arn:aws:fsx:{{region}}:{{account-id}}:file-system:{{filesystem-id}} \
      --security-group-arns arn:aws:ec2:{{region}}:{{account-id}}:security-group/{{group-id}}
  ```

  The following parameters are required in the `create-location-fsx-lustre` command.
  + `fsx-filesystem-arn` – The fully qualified Amazon Resource Name (ARN) of the file system that you want to read from or write to.
  + `security-group-arns` – The ARN of an Amazon EC2 security group to apply to the [network interfaces](required-network-interfaces.md) of the file system's preferred subnet.

The preceding command returns a location ARN similar to the following.

```
{
    "LocationArn": "arn:aws:datasync:us-west-2:111222333444:location/loc-07sb7abfc326c50fb"
}
```