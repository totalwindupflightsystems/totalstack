---
id: "@specs/aws/rds/docs/API_SwitchoverBlueGreenDeployment"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS SwitchoverBlueGreenDeployment"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# SwitchoverBlueGreenDeployment

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_SwitchoverBlueGreenDeployment
> **target_lang:** meta — documentation tier. ALL sections preserved.



# SwitchoverBlueGreenDeployment
<a name="API_SwitchoverBlueGreenDeployment"></a>

Switches over a blue/green deployment.

Before you switch over, production traffic is routed to the databases in the blue environment. After you switch over, production traffic is routed to the databases in the green environment.

For more information, see [Using Amazon RDS Blue/Green Deployments for database updates](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/blue-green-deployments.html) in the *Amazon RDS User Guide* and [Using Amazon RDS Blue/Green Deployments for database updates](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/blue-green-deployments.html) in the *Amazon Aurora User Guide*.

## Request Parameters
<a name="API_SwitchoverBlueGreenDeployment_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** BlueGreenDeploymentIdentifier **   
The resource ID of the blue/green deployment.  
Constraints:  
+ Must match an existing blue/green deployment resource ID.
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[A-Za-z][0-9A-Za-z-:._]*`   
Required: Yes

 ** SwitchoverTimeout **   
The amount of time, in seconds, for the switchover to complete.  
Default: 300  
If the switchover takes longer than the specified duration, then any changes are rolled back, and no changes are made to the environments.  
Type: Integer  
Valid Range: Minimum value of 30.  
Required: No

## Response Elements
<a name="API_SwitchoverBlueGreenDeployment_ResponseElements"></a>

The following element is returned by the service.

 ** BlueGreenDeployment **   
Details about a blue/green deployment.  
For more information, see [Using Amazon RDS Blue/Green Deployments for database updates](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/blue-green-deployments.html) in the *Amazon RDS User Guide* and [Using Amazon RDS Blue/Green Deployments for database updates](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/blue-green-deployments.html) in the *Amazon Aurora User Guide*.  
Type: [BlueGreenDeployment](API_BlueGreenDeployment.md) object

## Errors
<a name="API_SwitchoverBlueGreenDeployment_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BlueGreenDeploymentNotFoundFault **   
 `BlueGreenDeploymentIdentifier` doesn't refer to an existing blue/green deployment.  
HTTP Status Code: 404

 ** InvalidBlueGreenDeploymentStateFault **   
The blue/green deployment can't be switched over or deleted because there is an invalid configuration in the green environment.  
HTTP Status Code: 400

## Examples
<a name="API_SwitchoverBlueGreenDeployment_Examples"></a>

### Example
<a name="API_SwitchoverBlueGreenDeployment_Example_1"></a>

This example illustrates one usage of SwitchoverBlueGreenDeployment.

#### Sample Request
<a name="API_SwitchoverBlueGreenDeployment_Example_1_Request"></a>

```
https://rds.us-west-2.amazonaws.com/
   ?Action=SwitchoverBlueGreenDeployment
   &BlueGreenDeploymentIdentifier=bgd-mdoyy2mn7vbkhhgg
   &SwitchoverTimeout=400
   &SignatureMethod=HmacSHA256
   &SignatureVersion=4
   &Version=2014-10-31
   &X-Amz-Algorithm=AWS4-HMAC-SHA256
   &X-Amz-Credential=AKIADQKE4SARGYLE/20141031/us-west-2/rds/aws4_request
   &X-Amz-Date=20230110T190520Z
   &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
   &X-Amz-Signature=8a684aebe6d5219bb3572316a341963324d6ef339bd0dcfa5854f1a01d401214
```

#### Sample Response
<a name="API_SwitchoverBlueGreenDeployment_Example_1_Response"></a>

```
<SwitchoverBlueGreenDeploymentResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/">
  <SwitchoverBlueGreenDeploymentResult>
    <BlueGreenDeployment>
      <TagList/>
      <BlueGreenDeploymentName>my-blue-green-deployment</BlueGreenDeploymentName>
      <CreateTime>2023-01-10T18:42:09.330Z</CreateTime>
      <SwitchoverDetails>
        <member>
          <SourceMember>arn:aws:rds:us-west-2:123456789012:db:database-1</SourceMember>
          <TargetMember>arn:aws:rds:us-west-2:123456789012:db:database-1-green-7jtrw5</TargetMember>
          <Status>AVAILABLE</Status>
        </member>
      </SwitchoverDetails>
      <Source>arn:aws:rds:us-west-2:123456789012:db:database-1</Source>
      <BlueGreenDeploymentIdentifier>bgd-mdoyy2mn7vbkhhgg</BlueGreenDeploymentIdentifier>
      <Tasks>
        <member>
          <Name>CREATING_READ_REPLICA_OF_SOURCE</Name>
          <Status>COMPLETED</Status>
        </member>
        <member>
          <Name>CONFIGURE_BACKUPS</Name>
          <Status>COMPLETED</Status>
        </member>
      </Tasks>
      <Target>arn:aws:rds:us-west-2:123456789012:db:database-1-green-7jtrw5</Target>
      <Status>SWITCHOVER_IN_PROGRESS</Status>
    </BlueGreenDeployment>
  </SwitchoverBlueGreenDeploymentResult>
  <ResponseMetadata>
    <RequestId>c4f69d85-87e5-4fbb-b6b8-ccdb17404af6</RequestId>
  </ResponseMetadata>
</SwitchoverBlueGreenDeploymentResponse>
```

## See Also
<a name="API_SwitchoverBlueGreenDeployment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/SwitchoverBlueGreenDeployment) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/SwitchoverBlueGreenDeployment) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/SwitchoverBlueGreenDeployment) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/SwitchoverBlueGreenDeployment) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/SwitchoverBlueGreenDeployment) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/SwitchoverBlueGreenDeployment) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/SwitchoverBlueGreenDeployment) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/SwitchoverBlueGreenDeployment) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/SwitchoverBlueGreenDeployment) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/SwitchoverBlueGreenDeployment) 