---
id: "@specs/aws/rds/docs/API_DescribeBlueGreenDeployments"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeBlueGreenDeployments"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# DescribeBlueGreenDeployments

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_DescribeBlueGreenDeployments
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeBlueGreenDeployments
<a name="API_DescribeBlueGreenDeployments"></a>

Describes one or more blue/green deployments.

For more information, see [Using Amazon RDS Blue/Green Deployments for database updates](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/blue-green-deployments.html) in the *Amazon RDS User Guide* and [ Using Amazon RDS Blue/Green Deployments for database updates](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/blue-green-deployments.html) in the *Amazon Aurora User Guide*.

## Request Parameters
<a name="API_DescribeBlueGreenDeployments_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** BlueGreenDeploymentIdentifier **   
The blue/green deployment identifier. If you specify this parameter, the response only includes information about the specific blue/green deployment. This parameter isn't case-sensitive.  
Constraints:  
+ Must match an existing blue/green deployment identifier.
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[A-Za-z][0-9A-Za-z-:._]*`   
Required: No

 **Filters.Filter.N**   
A filter that specifies one or more blue/green deployments to describe.  
Valid Values:  
+  `blue-green-deployment-identifier` - Accepts system-generated identifiers for blue/green deployments. The results list only includes information about the blue/green deployments with the specified identifiers.
+  `blue-green-deployment-name` - Accepts user-supplied names for blue/green deployments. The results list only includes information about the blue/green deployments with the specified names.
+  `source` - Accepts source databases for a blue/green deployment. The results list only includes information about the blue/green deployments with the specified source databases.
+  `target` - Accepts target databases for a blue/green deployment. The results list only includes information about the blue/green deployments with the specified target databases.
Type: Array of [Filter](API_Filter.md) objects  
Required: No

 ** Marker **   
An optional pagination token provided by a previous `DescribeBlueGreenDeployments` request. If you specify this parameter, the response only includes records beyond the marker, up to the value specified by `MaxRecords`.  
Type: String  
Required: No

 ** MaxRecords **   
The maximum number of records to include in the response. If more records exist than the specified `MaxRecords` value, a pagination token called a marker is included in the response so you can retrieve the remaining results.  
Default: 100  
Constraints:  
+ Must be a minimum of 20.
+ Can't exceed 100.
Type: Integer  
Valid Range: Minimum value of 20. Maximum value of 100.  
Required: No

## Response Elements
<a name="API_DescribeBlueGreenDeployments_ResponseElements"></a>

The following elements are returned by the service.

 **BlueGreenDeployments.member.N**   
A list of blue/green deployments in the current account and AWS Region.  
Type: Array of [BlueGreenDeployment](API_BlueGreenDeployment.md) objects

 ** Marker **   
A pagination token that can be used in a later `DescribeBlueGreenDeployments` request.  
Type: String

## Errors
<a name="API_DescribeBlueGreenDeployments_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BlueGreenDeploymentNotFoundFault **   
 `BlueGreenDeploymentIdentifier` doesn't refer to an existing blue/green deployment.  
HTTP Status Code: 404

## Examples
<a name="API_DescribeBlueGreenDeployments_Examples"></a>

### Example
<a name="API_DescribeBlueGreenDeployments_Example_1"></a>

This example illustrates one usage of DescribeBlueGreenDeployments.

#### Sample Request
<a name="API_DescribeBlueGreenDeployments_Example_1_Request"></a>

```
https://rds.us-west-2.amazonaws.com/
   ?Action=DescribeBlueGreenDeployments
   &BlueGreenDeploymentIdentifier=bgd-clyvb1zv1geqensv
   &SignatureMethod=HmacSHA256
   &SignatureVersion=4
   &Version=2014-10-31
   &X-Amz-Algorithm=AWS4-HMAC-SHA256
   &X-Amz-Credential=AKIADQKE4SARGYLE/20141031/us-west-2/rds/aws4_request
   &X-Amz-Date=20230110T005253Z
   &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
   &X-Amz-Signature=8a684aebe6d5219bb3572316a341963324d6ef339bd0dcfa5854f1a01d401214
```

#### Sample Response
<a name="API_DescribeBlueGreenDeployments_Example_1_Response"></a>

```
<DescribeBlueGreenDeploymentsResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/">
  <DescribeBlueGreenDeploymentsResult>
    <BlueGreenDeployments>
      <member>
        <TagList/>
        <BlueGreenDeploymentName>my-blue-green-deployment</BlueGreenDeploymentName>
        <CreateTime>2023-01-10T20:08:48.940Z</CreateTime>
        <SwitchoverDetails>
          <member>
            <SourceMember>arn:aws:rds:us-west-2:123456789012:db:database-1</SourceMember>
            <TargetMember>arn:aws:rds:us-west-2:123456789012:db:database-1-green-mhv83d</TargetMember>
            <Status>PROVISIONING</Status>
          </member>
        </SwitchoverDetails>
        <Source>arn:aws:rds:us-west-2:123456789012:db:database-1</Source>
        <BlueGreenDeploymentIdentifier>bgd-clyvb1zv1geqensv</BlueGreenDeploymentIdentifier>
        <Tasks>
          <member>
            <Name>CREATING_READ_REPLICA_OF_SOURCE</Name>
            <Status>IN_PROGRESS</Status>
          </member>
          <member>
            <Name>DB_ENGINE_VERSION_UPGRADE</Name>
            <Status>PENDING</Status>
          </member>
          <member>
            <Name>CONFIGURE_BACKUPS</Name>
            <Status>PENDING</Status>
          </member>
        </Tasks>
        <Target>arn:aws:rds:us-west-2:123456789012:db:database-1-green-mhv83d</Target>
        <Status>PROVISIONING</Status>
      </member>
    </BlueGreenDeployments>
  </DescribeBlueGreenDeploymentsResult>
  <ResponseMetadata>
    <RequestId>a534de7b-dc20-4b16-863a-24f456385d3a</RequestId>
  </ResponseMetadata>
</DescribeBlueGreenDeploymentsResponse>
```

## See Also
<a name="API_DescribeBlueGreenDeployments_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/DescribeBlueGreenDeployments) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/DescribeBlueGreenDeployments) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DescribeBlueGreenDeployments) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/DescribeBlueGreenDeployments) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DescribeBlueGreenDeployments) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/DescribeBlueGreenDeployments) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/DescribeBlueGreenDeployments) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/DescribeBlueGreenDeployments) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/DescribeBlueGreenDeployments) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DescribeBlueGreenDeployments) 