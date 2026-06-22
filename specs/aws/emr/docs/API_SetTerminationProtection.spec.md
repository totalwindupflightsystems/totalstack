---
id: "@specs/aws/emr/docs/API_SetTerminationProtection"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS SetTerminationProtection"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# SetTerminationProtection

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_SetTerminationProtection
> **target_lang:** meta — documentation tier. ALL sections preserved.



# SetTerminationProtection
<a name="API_SetTerminationProtection"></a>

SetTerminationProtection locks a cluster (job flow) so the Amazon EC2 instances in the cluster cannot be terminated by user intervention, an API call, or in the event of a job-flow error. The cluster still terminates upon successful completion of the job flow. Calling `SetTerminationProtection` on a cluster is similar to calling the Amazon EC2 `DisableAPITermination` API on all Amazon EC2 instances in a cluster.

 `SetTerminationProtection` is used to prevent accidental termination of a cluster and to ensure that in the event of an error, the instances persist so that you can recover any data stored in their ephemeral instance storage.

 To terminate a cluster that has been locked by setting `SetTerminationProtection` to `true`, you must first unlock the job flow by a subsequent call to `SetTerminationProtection` in which you set the value to `false`. 

 For more information, see [Managing Cluster Termination](https://docs.aws.amazon.com/emr/latest/ManagementGuide/UsingEMR_TerminationProtection.html) in the *Amazon EMR Management Guide*. 

## Request Syntax
<a name="API_SetTerminationProtection_RequestSyntax"></a>

```
{
   "JobFlowIds": [ "{{string}}" ],
   "TerminationProtected": {{boolean}}
}
```

## Request Parameters
<a name="API_SetTerminationProtection_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [JobFlowIds](#API_SetTerminationProtection_RequestSyntax) **   <a name="EMR-SetTerminationProtection-request-JobFlowIds"></a>
 A list of strings that uniquely identify the clusters to protect. This identifier is returned by [RunJobFlow](API_RunJobFlow.md) and can also be obtained from [DescribeJobFlows](API_DescribeJobFlows.md) .   
Type: Array of strings  
Length Constraints: Minimum length of 0. Maximum length of 10280.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: Yes

 ** [TerminationProtected](#API_SetTerminationProtection_RequestSyntax) **   <a name="EMR-SetTerminationProtection-request-TerminationProtected"></a>
A Boolean that indicates whether to protect the cluster and prevent the Amazon EC2 instances in the cluster from shutting down due to API calls, user intervention, or job-flow error.  
Type: Boolean  
Required: Yes

## Response Elements
<a name="API_SetTerminationProtection_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_SetTerminationProtection_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **   
Indicates that an error occurred while processing the request and that the request was not completed.  
HTTP Status Code: 400

## Examples
<a name="API_SetTerminationProtection_Examples"></a>

### Example
<a name="API_SetTerminationProtection_Example_1"></a>

This example illustrates one usage of SetTerminationProtection.

#### Sample Request
<a name="API_SetTerminationProtection_Example_1_Request"></a>

```
POST / HTTP/1.1
Content-Type: application/x-amz-json-1.1
X-Amz-Target: ElasticMapReduce.SetTerminationProtection
Content-Length: 61
User-Agent: aws-sdk-ruby/1.9.2 ruby/1.9.3 i386-mingw32
Host: us-east-1.elasticmapreduce.amazonaws.com
X-Amz-Date: 20130716T211420Z
X-Amz-Content-Sha256: c362fadae0fce377aa63f04388aeb90c53cedb17a8bfbb8cffcb10c2378137f9
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20130716/us-east-1/elasticmapreduce/aws4_request, SignedHeaders=content-length;content-type;host;user-agent;x-amz-content-sha256;x-amz-date;x-amz-target, Signature=764b6aa1a38733cadff35a2e884887e9f1208a422266bc83ac77e8d0b80bd4cf
Accept: */*

{
    "JobFlowIds": ["j-3TS0OIYO4NFN"],
    "TerminationProtected": true
}
```

#### Sample Response
<a name="API_SetTerminationProtection_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: af23b1db-ee5c-11e2-9787-192218ecb460
Content-Type: application/x-amz-json-1.1
Content-Length: 0
Date: Tue, 16 Jul 2013 21:14:21 GMT
```

## See Also
<a name="API_SetTerminationProtection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticmapreduce-2009-03-31/SetTerminationProtection) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticmapreduce-2009-03-31/SetTerminationProtection) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/SetTerminationProtection) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticmapreduce-2009-03-31/SetTerminationProtection) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/SetTerminationProtection) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticmapreduce-2009-03-31/SetTerminationProtection) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticmapreduce-2009-03-31/SetTerminationProtection) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticmapreduce-2009-03-31/SetTerminationProtection) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticmapreduce-2009-03-31/SetTerminationProtection) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/SetTerminationProtection) 