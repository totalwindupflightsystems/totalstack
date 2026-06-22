---
id: "@specs/aws/emr/docs/API_SetUnhealthyNodeReplacement"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS SetUnhealthyNodeReplacement"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# SetUnhealthyNodeReplacement

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_SetUnhealthyNodeReplacement
> **target_lang:** meta — documentation tier. ALL sections preserved.



# SetUnhealthyNodeReplacement
<a name="API_SetUnhealthyNodeReplacement"></a>

Specify whether to enable unhealthy node replacement, which lets Amazon EMR gracefully replace core nodes on a cluster if any nodes become unhealthy. For example, a node becomes unhealthy if disk usage is above 90%. If unhealthy node replacement is on and `TerminationProtected` are off, Amazon EMR immediately terminates the unhealthy core nodes. To use unhealthy node replacement and retain unhealthy core nodes, use [SetTerminationProtection](API_SetTerminationProtection.md) to turn on termination protection. In such cases, Amazon EMR adds the unhealthy nodes to a denylist, reducing job interruptions and failures.

If unhealthy node replacement is on, Amazon EMR notifies YARN and other applications on the cluster to stop scheduling tasks with these nodes, moves the data, and then terminates the nodes.

For more information, see [graceful node replacement](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-node-replacement.html) in the *Amazon EMR Management Guide*.

## Request Syntax
<a name="API_SetUnhealthyNodeReplacement_RequestSyntax"></a>

```
{
   "JobFlowIds": [ "{{string}}" ],
   "UnhealthyNodeReplacement": {{boolean}}
}
```

## Request Parameters
<a name="API_SetUnhealthyNodeReplacement_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [JobFlowIds](#API_SetUnhealthyNodeReplacement_RequestSyntax) **   <a name="EMR-SetUnhealthyNodeReplacement-request-JobFlowIds"></a>
The list of strings that uniquely identify the clusters for which to turn on unhealthy node replacement. You can get these identifiers by running the [RunJobFlow](API_RunJobFlow.md) or the [DescribeJobFlows](API_DescribeJobFlows.md) operations.  
Type: Array of strings  
Length Constraints: Minimum length of 0. Maximum length of 10280.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: Yes

 ** [UnhealthyNodeReplacement](#API_SetUnhealthyNodeReplacement_RequestSyntax) **   <a name="EMR-SetUnhealthyNodeReplacement-request-UnhealthyNodeReplacement"></a>
Indicates whether to turn on or turn off graceful unhealthy node replacement.  
Type: Boolean  
Required: Yes

## Response Elements
<a name="API_SetUnhealthyNodeReplacement_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_SetUnhealthyNodeReplacement_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **   
Indicates that an error occurred while processing the request and that the request was not completed.  
HTTP Status Code: 400

## Examples
<a name="API_SetUnhealthyNodeReplacement_Examples"></a>

### Example
<a name="API_SetUnhealthyNodeReplacement_Example_1"></a>

This example illustrates one usage of SetUnhealthyNodeReplacement.

#### Sample Request
<a name="API_SetUnhealthyNodeReplacement_Example_1_Request"></a>

```
POST / HTTP/1.1
Content-Type: application/x-amz-json-1.1
X-Amz-Target: ElasticMapReduce.SetUnhealthyNodeReplacement
Content-Length: 61
User-Agent: aws-sdk-ruby/1.9.2 ruby/1.9.3 i386-mingw32
Host: us-east-1.elasticmapreduce.amazonaws.com
X-Amz-Date: 20130716T211420Z
X-Amz-Content-Sha256: c362fadae0fce377aa63f04388aeb90c53cedb17a8bfbb8cffcb10c2378137f9
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20130716/us-east-1/elasticmapreduce/aws4_request, SignedHeaders=content-length;content-type;host;user-agent;x-amz-content-sha256;x-amz-date;x-amz-target, Signature=764b6aa1a38733cadff35a2e884887e9f1208a422266bc83ac77e8d0b80bd4cf
Accept: */*
 
{
    "JobFlowIds": ["j-3TS0OIYO4NFN"],
    "SetUnhealthyNodeReplacement": true
}
```

#### Sample Response
<a name="API_SetUnhealthyNodeReplacement_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: af23b1db-ee5c-11e2-9787-192218ecb460
Content-Type: application/x-amz-json-1.1
Content-Length: 0
Date: Tue, 16 Jul 2013 21:14:21 GMT
```

## See Also
<a name="API_SetUnhealthyNodeReplacement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticmapreduce-2009-03-31/SetUnhealthyNodeReplacement) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticmapreduce-2009-03-31/SetUnhealthyNodeReplacement) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/SetUnhealthyNodeReplacement) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticmapreduce-2009-03-31/SetUnhealthyNodeReplacement) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/SetUnhealthyNodeReplacement) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticmapreduce-2009-03-31/SetUnhealthyNodeReplacement) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticmapreduce-2009-03-31/SetUnhealthyNodeReplacement) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticmapreduce-2009-03-31/SetUnhealthyNodeReplacement) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticmapreduce-2009-03-31/SetUnhealthyNodeReplacement) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/SetUnhealthyNodeReplacement) 