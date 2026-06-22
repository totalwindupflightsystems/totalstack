---
id: "@specs/aws/emr/docs/API_TerminateJobFlows"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS TerminateJobFlows"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# TerminateJobFlows

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_TerminateJobFlows
> **target_lang:** meta — documentation tier. ALL sections preserved.



# TerminateJobFlows
<a name="API_TerminateJobFlows"></a>

TerminateJobFlows shuts a list of clusters (job flows) down. When a job flow is shut down, any step not yet completed is canceled and the Amazon EC2 instances on which the cluster is running are stopped. Any log files not already saved are uploaded to Amazon S3 if a LogUri was specified when the cluster was created.

The maximum number of clusters allowed is 10. The call to `TerminateJobFlows` is asynchronous. Depending on the configuration of the cluster, it may take up to 1-5 minutes for the cluster to completely terminate and release allocated resources, such as Amazon EC2 instances.

## Request Syntax
<a name="API_TerminateJobFlows_RequestSyntax"></a>

```
{
   "JobFlowIds": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_TerminateJobFlows_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [JobFlowIds](#API_TerminateJobFlows_RequestSyntax) **   <a name="EMR-TerminateJobFlows-request-JobFlowIds"></a>
A list of job flows to be shut down.  
Type: Array of strings  
Length Constraints: Minimum length of 0. Maximum length of 10280.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: Yes

## Response Elements
<a name="API_TerminateJobFlows_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_TerminateJobFlows_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **   
Indicates that an error occurred while processing the request and that the request was not completed.  
HTTP Status Code: 400

## Examples
<a name="API_TerminateJobFlows_Examples"></a>

### Example
<a name="API_TerminateJobFlows_Example_1"></a>

This example illustrates one usage of TerminateJobFlows.

#### Sample Request
<a name="API_TerminateJobFlows_Example_1_Request"></a>

```
POST / HTTP/1.1
Content-Type: application/x-amz-json-1.1
X-Amz-Target: ElasticMapReduce.TerminateJobFlows
Content-Length: 33
User-Agent: aws-sdk-ruby/1.9.2 ruby/1.9.3 i386-mingw32
Host: us-east-1.elasticmapreduce.amazonaws.com
X-Amz-Date: 20130716T211858Z
X-Amz-Content-Sha256: ab64713f61e066e80a6083844b9249b6c6362d34a7ae7393047aa46d38b9e315
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20130716/us-east-1/elasticmapreduce/aws4_request, SignedHeaders=content-length;content-type;host;user-agent;x-amz-content-sha256;x-amz-date;x-amz-target, Signature=9791416eaf09f36aa753a324b0de27ff5cc7084b8548cc748487a2bcb3439d58
Accept: */*

{"JobFlowIds": ["j-3TS0OIYO4NFN"]}
```

#### Sample Response
<a name="API_TerminateJobFlows_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 5551a7c9-ee5d-11e2-9542-25296c300ff0
Content-Type: application/x-amz-json-1.1
Content-Length: 0
Date: Tue, 16 Jul 2013 21:18:59 GMT
```

## See Also
<a name="API_TerminateJobFlows_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticmapreduce-2009-03-31/TerminateJobFlows) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticmapreduce-2009-03-31/TerminateJobFlows) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/TerminateJobFlows) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticmapreduce-2009-03-31/TerminateJobFlows) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/TerminateJobFlows) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticmapreduce-2009-03-31/TerminateJobFlows) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticmapreduce-2009-03-31/TerminateJobFlows) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticmapreduce-2009-03-31/TerminateJobFlows) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticmapreduce-2009-03-31/TerminateJobFlows) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/TerminateJobFlows) 