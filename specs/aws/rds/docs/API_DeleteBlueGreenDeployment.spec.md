---
id: "@specs/aws/rds/docs/API_DeleteBlueGreenDeployment"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteBlueGreenDeployment"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# DeleteBlueGreenDeployment

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_DeleteBlueGreenDeployment
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteBlueGreenDeployment
<a name="API_DeleteBlueGreenDeployment"></a>

Deletes a blue/green deployment.

For more information, see [Using Amazon RDS Blue/Green Deployments for database updates](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/blue-green-deployments.html) in the *Amazon RDS User Guide* and [Using Amazon RDS Blue/Green Deployments for database updates](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/blue-green-deployments.html) in the *Amazon Aurora User Guide*.

## Request Parameters
<a name="API_DeleteBlueGreenDeployment_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** BlueGreenDeploymentIdentifier **   
The unique identifier of the blue/green deployment to delete. This parameter isn't case-sensitive.  
Constraints:   
+ Must match an existing blue/green deployment identifier.
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[A-Za-z][0-9A-Za-z-:._]*`   
Required: Yes

 ** DeleteTarget **   
Specifies whether to delete the resources in the green environment. You can't specify this option if the blue/green deployment [status](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_BlueGreenDeployment.html) is `SWITCHOVER_COMPLETED`.  
Type: Boolean  
Required: No

## Response Elements
<a name="API_DeleteBlueGreenDeployment_ResponseElements"></a>

The following element is returned by the service.

 ** BlueGreenDeployment **   
Details about a blue/green deployment.  
For more information, see [Using Amazon RDS Blue/Green Deployments for database updates](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/blue-green-deployments.html) in the *Amazon RDS User Guide* and [Using Amazon RDS Blue/Green Deployments for database updates](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/blue-green-deployments.html) in the *Amazon Aurora User Guide*.  
Type: [BlueGreenDeployment](API_BlueGreenDeployment.md) object

## Errors
<a name="API_DeleteBlueGreenDeployment_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BlueGreenDeploymentNotFoundFault **   
 `BlueGreenDeploymentIdentifier` doesn't refer to an existing blue/green deployment.  
HTTP Status Code: 404

 ** InvalidBlueGreenDeploymentStateFault **   
The blue/green deployment can't be switched over or deleted because there is an invalid configuration in the green environment.  
HTTP Status Code: 400

## Examples
<a name="API_DeleteBlueGreenDeployment_Examples"></a>

### Example
<a name="API_DeleteBlueGreenDeployment_Example_1"></a>

This example illustrates one usage of DeleteBlueGreenDeployment.

#### Sample Request
<a name="API_DeleteBlueGreenDeployment_Example_1_Request"></a>

```
https://rds.us-west-2.amazonaws.com/
   ?Action=DeleteBlueGreenDeployment
   &BlueGreenDeploymentIdentifier=bgd-mdoyy2mn7vbkhhgg
   &SignatureMethod=HmacSHA256
   &SignatureVersion=4
   &Version=2014-10-31
   &X-Amz-Credential=AKIADQKE4SARGYLE/20141031/us-west-2/rds/aws4_request
   &X-Amz-Date=20230110T191150Z
   &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-date
   &X-Amz-Signature=8a684aebe6d5219bb3572316a341963324d6ef339bd0dcfa5854f1a01d401214
```

#### Sample Response
<a name="API_DeleteBlueGreenDeployment_Example_1_Response"></a>

```
<DeleteBlueGreenDeploymentResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/">
  <DeleteBlueGreenDeploymentResult>
    <BlueGreenDeployment>
      <TagList/>
      <BlueGreenDeploymentName>my-blue-green-deployment</BlueGreenDeploymentName>
      <DeleteTime>2023-01-10T19:11:51.293Z</DeleteTime>
      <CreateTime>2023-01-10T18:42:09.330Z</CreateTime>
      <SwitchoverDetails>
        <member>
          <SourceMember>arn:aws:rds:us-west-2:123456789012:db:database-1-old1</SourceMember>
          <TargetMember>arn:aws:rds:us-west-2:123456789012:db:database-1</TargetMember>
          <Status>SWITCHOVER_COMPLETED</Status>
        </member>
      </SwitchoverDetails>
      <Source>arn:aws:rds:us-west-2:123456789012:db:database-1-old1</Source>
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
      <Target>arn:aws:rds:us-west-2:123456789012:db:database-1</Target>
      <Status>DELETING</Status>
    </BlueGreenDeployment>
  </DeleteBlueGreenDeploymentResult>
  <ResponseMetadata>
    <RequestId>34deffd3-543a-4c26-9ff1-f859894f43bc</RequestId>
  </ResponseMetadata>
</DeleteBlueGreenDeploymentResponse>
```

## See Also
<a name="API_DeleteBlueGreenDeployment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/DeleteBlueGreenDeployment) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/DeleteBlueGreenDeployment) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DeleteBlueGreenDeployment) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/DeleteBlueGreenDeployment) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DeleteBlueGreenDeployment) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/DeleteBlueGreenDeployment) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/DeleteBlueGreenDeployment) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/DeleteBlueGreenDeployment) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/DeleteBlueGreenDeployment) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DeleteBlueGreenDeployment) 