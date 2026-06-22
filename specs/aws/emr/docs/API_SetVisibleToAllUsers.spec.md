---
id: "@specs/aws/emr/docs/API_SetVisibleToAllUsers"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS SetVisibleToAllUsers"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# SetVisibleToAllUsers

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_SetVisibleToAllUsers
> **target_lang:** meta — documentation tier. ALL sections preserved.



# SetVisibleToAllUsers
<a name="API_SetVisibleToAllUsers"></a>

**Important**  
The SetVisibleToAllUsers parameter is no longer supported. Your cluster may be visible to all users in your account. To restrict cluster access using an IAM policy, see [Identity and Access Management for Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-access-IAM.html). 

Sets the [Cluster:VisibleToAllUsers](API_Cluster.md#EMR-Type-Cluster-VisibleToAllUsers) value for an Amazon EMR cluster. When `true`, IAM principals in the AWS account can perform Amazon EMR cluster actions that their IAM policies allow. When `false`, only the IAM principal that created the cluster and the AWS account root user can perform Amazon EMR actions on the cluster, regardless of IAM permissions policies attached to other IAM principals.

This action works on running clusters. When you create a cluster, use the [RunJobFlow:VisibleToAllUsers](API_RunJobFlow.md#EMR-RunJobFlow-request-VisibleToAllUsers) parameter.

For more information, see [Understanding the Amazon EMR Cluster VisibleToAllUsers Setting](https://docs.aws.amazon.com/emr/latest/ManagementGuide/security_IAM_emr-with-IAM.html#security_set_visible_to_all_users) in the *Amazon EMR Management Guide*.

## Request Syntax
<a name="API_SetVisibleToAllUsers_RequestSyntax"></a>

```
{
   "JobFlowIds": [ "{{string}}" ],
   "VisibleToAllUsers": {{boolean}}
}
```

## Request Parameters
<a name="API_SetVisibleToAllUsers_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [JobFlowIds](#API_SetVisibleToAllUsers_RequestSyntax) **   <a name="EMR-SetVisibleToAllUsers-request-JobFlowIds"></a>
The unique identifier of the job flow (cluster).  
Type: Array of strings  
Length Constraints: Minimum length of 0. Maximum length of 10280.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: Yes

 ** [VisibleToAllUsers](#API_SetVisibleToAllUsers_RequestSyntax) **   <a name="EMR-SetVisibleToAllUsers-request-VisibleToAllUsers"></a>
A value of `true` indicates that an IAM principal in the AWS account can perform Amazon EMR actions on the cluster that the IAM policies attached to the principal allow. A value of `false` indicates that only the IAM principal that created the cluster and the AWS root user can perform Amazon EMR actions on the cluster.  
Type: Boolean  
Required: Yes

## Response Elements
<a name="API_SetVisibleToAllUsers_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_SetVisibleToAllUsers_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **   
Indicates that an error occurred while processing the request and that the request was not completed.  
HTTP Status Code: 400

## Examples
<a name="API_SetVisibleToAllUsers_Examples"></a>

### Example
<a name="API_SetVisibleToAllUsers_Example_1"></a>

This example illustrates one usage of SetVisibleToAllUsers.

#### Sample Request
<a name="API_SetVisibleToAllUsers_Example_1_Request"></a>

```
POST / HTTP/1.1
Content-Type: application/x-amz-json-1.1
X-Amz-Target: ElasticMapReduce.SetVisibleToAllUsers
Content-Length: 58
User-Agent: aws-sdk-ruby/1.9.2 ruby/1.9.3 i386-mingw32
Host: us-east-1.elasticmapreduce.amazonaws.com
X-Amz-Date: 20130715T221616Z
X-Amz-Content-Sha256: 2ff32d11eab2383d764ffcb97571454e798689ecd09a7b1bb2327e22b0b930d4
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20130715/us-east-1/elasticmapreduce/aws4_request, SignedHeaders=content-length;content-type;host;user-agent;x-amz-content-sha256;x-amz-date;x-amz-target, Signature=e1a00b37787d9ccc43c9de32f1f0a73813b0bd6643d4db7762b62a7092d51997
Accept: */*

{
    "JobFlowIds": ["j-ZKIY4CKQRX72"],
    "VisibleToAllUsers": true
}
```

#### Sample Response
<a name="API_SetVisibleToAllUsers_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 2be9cde9-ed9c-11e2-82b6-2351cde3f33f
Content-Type: application/x-amz-json-1.1
Content-Length: 0
Date: Mon, 15 Jul 2013 22:16:18 GMT
```

## See Also
<a name="API_SetVisibleToAllUsers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticmapreduce-2009-03-31/SetVisibleToAllUsers) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticmapreduce-2009-03-31/SetVisibleToAllUsers) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/SetVisibleToAllUsers) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticmapreduce-2009-03-31/SetVisibleToAllUsers) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/SetVisibleToAllUsers) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticmapreduce-2009-03-31/SetVisibleToAllUsers) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticmapreduce-2009-03-31/SetVisibleToAllUsers) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticmapreduce-2009-03-31/SetVisibleToAllUsers) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticmapreduce-2009-03-31/SetVisibleToAllUsers) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/SetVisibleToAllUsers) 