---
id: "@specs/aws/rds/docs/API_DescribeDBSecurityGroups"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeDBSecurityGroups"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# DescribeDBSecurityGroups

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_DescribeDBSecurityGroups
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeDBSecurityGroups
<a name="API_DescribeDBSecurityGroups"></a>

Returns a list of `DBSecurityGroup` descriptions. If a `DBSecurityGroupName` is specified, the list will contain only the descriptions of the specified DB security group.

**Note**  
EC2-Classic was retired on August 15, 2022. If you haven't migrated from EC2-Classic to a VPC, we recommend that you migrate as soon as possible. For more information, see [Migrate from EC2-Classic to a VPC](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/vpc-migrate.html) in the *Amazon EC2 User Guide*, the blog [EC2-Classic Networking is Retiring – Here’s How to Prepare](http://aws.amazon.com/blogs/aws/ec2-classic-is-retiring-heres-how-to-prepare/), and [Moving a DB instance not in a VPC into a VPC](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.Non-VPC2VPC.html) in the *Amazon RDS User Guide*.

## Request Parameters
<a name="API_DescribeDBSecurityGroups_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBSecurityGroupName **   
The name of the DB security group to return details for.  
Type: String  
Required: No

 **Filters.Filter.N**   
This parameter isn't currently supported.  
Type: Array of [Filter](API_Filter.md) objects  
Required: No

 ** Marker **   
An optional pagination token provided by a previous `DescribeDBSecurityGroups` request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.  
Type: String  
Required: No

 ** MaxRecords **   
The maximum number of records to include in the response. If more records exist than the specified `MaxRecords` value, a pagination token called a marker is included in the response so that you can retrieve the remaining results.  
Default: 100  
Constraints: Minimum 20, maximum 100.  
Type: Integer  
Required: No

## Response Elements
<a name="API_DescribeDBSecurityGroups_ResponseElements"></a>

The following elements are returned by the service.

 **DBSecurityGroups.DBSecurityGroup.N**   
A list of `DBSecurityGroup` instances.  
Type: Array of [DBSecurityGroup](API_DBSecurityGroup.md) objects

 ** Marker **   
An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.  
Type: String

## Errors
<a name="API_DescribeDBSecurityGroups_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBSecurityGroupNotFound **   
 `DBSecurityGroupName` doesn't refer to an existing DB security group.  
HTTP Status Code: 404

## Examples
<a name="API_DescribeDBSecurityGroups_Examples"></a>

### Example
<a name="API_DescribeDBSecurityGroups_Example_1"></a>

This example illustrates one usage of DescribeDBSecurityGroups.

#### Sample Request
<a name="API_DescribeDBSecurityGroups_Example_1_Request"></a>

```
https://rds.us-west-2.amazonaws.com/
   ?Action=DescribeDBSecurityGroups
   &MaxRecords=100
   &SignatureMethod=HmacSHA256
   &SignatureVersion=4
   &Version=2014-10-31
   &X-Amz-Algorithm=AWS4-HMAC-SHA256
   &X-Amz-Credential=AKIADQKE4SARGYLE/20140421/us-west-2/rds/aws4_request
   &X-Amz-Date=20140421T194732Z
   &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
   &X-Amz-Signature=b14bcddedcf2fd7ffbbcc45ed2caa99cd848ee309a19070f946ad2a54f5331fe
```

#### Sample Response
<a name="API_DescribeDBSecurityGroups_Example_1_Response"></a>

```
<DescribeDBSecurityGroupsResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/">
  <DescribeDBSecurityGroupsResult>
    <DBSecurityGroups>
      <DBSecurityGroup>
        <EC2SecurityGroups/>
        <DBSecurityGroupDescription>My security group</DBSecurityGroupDescription>
        <IPRanges>
          <IPRange>
            <CIDRIP>192.0.0.0/24</CIDRIP>
            <Status>authorized</Status>
          </IPRange>
          <IPRange>
            <CIDRIP>190.0.1.0/29</CIDRIP>
            <Status>authorized</Status>
          </IPRange>
          <IPRange>
            <CIDRIP>190.0.2.0/29</CIDRIP>
            <Status>authorized</Status>
          </IPRange>
          <IPRange>
            <CIDRIP>10.0.0.0/8</CIDRIP>
            <Status>authorized</Status>
          </IPRange>
        </IPRanges>
        <OwnerId>803#########</OwnerId>
        <DBSecurityGroupName>my-secgrp</DBSecurityGroupName>
      </DBSecurityGroup>
      <DBSecurityGroup>
        <EC2SecurityGroups/>
        <DBSecurityGroupDescription>default</DBSecurityGroupDescription>
        <IPRanges/>
        <OwnerId>803#########</OwnerId>
        <DBSecurityGroupName>default</DBSecurityGroupName>
      </DBSecurityGroup>
   </DBSecurityGroups>
  </DescribeDBSecurityGroupsResult>
  <ResponseMetadata>
    <RequestId>b76e692c-b98c-11d3-a907-5a2c468b9cb0</RequestId>
  </ResponseMetadata>
</DescribeDBSecurityGroupsResponse>
```

## See Also
<a name="API_DescribeDBSecurityGroups_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/DescribeDBSecurityGroups) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/DescribeDBSecurityGroups) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DescribeDBSecurityGroups) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/DescribeDBSecurityGroups) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DescribeDBSecurityGroups) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/DescribeDBSecurityGroups) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/DescribeDBSecurityGroups) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/DescribeDBSecurityGroups) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/DescribeDBSecurityGroups) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DescribeDBSecurityGroups) 