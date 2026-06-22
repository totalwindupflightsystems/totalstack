---
id: "@specs/aws/batch/docs/API_CreateSchedulingPolicy"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateSchedulingPolicy"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# CreateSchedulingPolicy

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_CreateSchedulingPolicy
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateSchedulingPolicy
<a name="API_CreateSchedulingPolicy"></a>

Creates an AWS Batch scheduling policy.

## Request Syntax
<a name="API_CreateSchedulingPolicy_RequestSyntax"></a>

```
POST /v1/createschedulingpolicy HTTP/1.1
Content-type: application/json

{
   "fairsharePolicy": { 
      "computeReservation": {{number}},
      "shareDecaySeconds": {{number}},
      "shareDistribution": [ 
         { 
            "shareIdentifier": "{{string}}",
            "weightFactor": {{number}}
         }
      ]
   },
   "name": "{{string}}",
   "quotaSharePolicy": { 
      "idleResourceAssignmentStrategy": "{{string}}"
   },
   "tags": { 
      "{{string}}" : "{{string}}" 
   }
}
```

## URI Request Parameters
<a name="API_CreateSchedulingPolicy_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateSchedulingPolicy_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [fairsharePolicy](#API_CreateSchedulingPolicy_RequestSyntax) **   <a name="Batch-CreateSchedulingPolicy-request-fairsharePolicy"></a>
The fair-share scheduling policy details. Only one of fairsharePolicy or quotaSharePolicy can be set. Once set, this policy type cannot be removed or changed to a quotaSharePolicy.  
Type: [FairsharePolicy](API_FairsharePolicy.md) object  
Required: No

 ** [name](#API_CreateSchedulingPolicy_RequestSyntax) **   <a name="Batch-CreateSchedulingPolicy-request-name"></a>
The name of the fair-share scheduling policy. It can be up to 128 letters long. It can contain uppercase and lowercase letters, numbers, hyphens (-), and underscores (\_).  
Type: String  
Required: Yes

 ** [quotaSharePolicy](#API_CreateSchedulingPolicy_RequestSyntax) **   <a name="Batch-CreateSchedulingPolicy-request-quotaSharePolicy"></a>
The quota share scheduling policy details. Only one of fairsharePolicy or quotaSharePolicy can be set. Once set, this policy type cannot be removed or changed to a fairSharePolicy.  
Type: [QuotaSharePolicy](API_QuotaSharePolicy.md) object  
Required: No

 ** [tags](#API_CreateSchedulingPolicy_RequestSyntax) **   <a name="Batch-CreateSchedulingPolicy-request-tags"></a>
The tags that you apply to the scheduling policy to help you categorize and organize your resources. Each tag consists of a key and an optional value. For more information, see [Tagging AWS Resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) in * AWS General Reference*.  
These tags can be updated or removed using the [TagResource](https://docs.aws.amazon.com/batch/latest/APIReference/API_TagResource.html) and [UntagResource](https://docs.aws.amazon.com/batch/latest/APIReference/API_UntagResource.html) API operations.  
Type: String to string map  
Map Entries: Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Value Length Constraints: Maximum length of 256.  
Required: No

## Response Syntax
<a name="API_CreateSchedulingPolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "name": "string"
}
```

## Response Elements
<a name="API_CreateSchedulingPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_CreateSchedulingPolicy_ResponseSyntax) **   <a name="Batch-CreateSchedulingPolicy-response-arn"></a>
The Amazon Resource Name (ARN) of the scheduling policy. The format is `aws:Partition:batch:Region:Account:scheduling-policy/Name `. For example, `aws:aws:batch:us-west-2:123456789012:scheduling-policy/MySchedulingPolicy`.  
Type: String

 ** [name](#API_CreateSchedulingPolicy_ResponseSyntax) **   <a name="Batch-CreateSchedulingPolicy-response-name"></a>
The name of the scheduling policy.  
Type: String

## Errors
<a name="API_CreateSchedulingPolicy_Errors"></a>

 ** ClientException **   
These errors are usually caused by a client action. One example cause is using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Another cause is specifying an identifier that's not valid.  
HTTP Status Code: 400

 ** ServerException **   
These errors are usually caused by a server issue.  
HTTP Status Code: 500

## Examples
<a name="API_CreateSchedulingPolicy_Examples"></a>

In the following example or examples, the Authorization header contents (` [authorization-params] `) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_CreateSchedulingPolicy_Example_1"></a>

This example creates a scheduling policy with the specified share identifiers and share identifier prefixes.

#### Sample Request
<a name="API_CreateSchedulingPolicy_Example_1_Request"></a>

```
POST /v1/createschedulingpolicy HTTP/1.1
Host: batch.us-east-1.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/1.20.21 Python/3.6.9 Linux/4.4.0-19041-Microsoft botocore/1.21.21
X-Amz-Date: 20210928T231724Z
X-Amz-Security-Token: [security-token]
Authorization: [authorization-params]
Content-Length: [content-length]

{
  "name": "ExampleFairSharePolicy",
  "fairsharePolicy": {
    "shareDecaySeconds": 3600,
    "computeReservation": 1,
    "shareDistribution": [
      {
        "shareIdentifier": "A1*",
        "weightFactor": 0.1
      },
      {
        "shareIdentifier": "A2",
        "weightFactor": 0.2
      },
      {
        "shareIdentifier": "B*",
        "weightFactor": 0.8
      },
      {
        "shareIdentifier": "C",
        "weightFactor": 1.2
      },
      {
        "shareIdentifier": "D*",
        "weightFactor": 1.5
      },
      {
        "shareIdentifier": "E",
        "weightFactor": 1.8
      }
    ]
  },
  "tags": {
    "Hot": "Dog",
    "Beef": "Brisket",
    "Pork": "Ribs",
    "Department": "Engineering"
  }
}
```

#### Sample Response
<a name="API_CreateSchedulingPolicy_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 28 Sep 2021 23:17:50 GMT
Content-Type: application/json
Content-Length: [content-length]
x-amzn-RequestId: [request-id]
Access-Control-Allow-Origin: *
x-amz-apigw-id: [apigw-id]
Access-Control-Expose-Headers: X-amzn-errortype,X-amzn-requestid,X-amzn-errormessage,X-amzn-trace-id,X-amz-apigw-id,date
X-Amzn-Trace-Id: [trace-id]
Connection: keep-alive

{
   "schedulingPolicies": [{
      "arn": "arn:aws:batch:us-east-1:123456789012:scheduling-policy/ExampleFairSharePolicy"
   }]
}
```

## See Also
<a name="API_CreateSchedulingPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/batch-2016-08-10/CreateSchedulingPolicy) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/batch-2016-08-10/CreateSchedulingPolicy) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/CreateSchedulingPolicy) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/batch-2016-08-10/CreateSchedulingPolicy) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/CreateSchedulingPolicy) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/batch-2016-08-10/CreateSchedulingPolicy) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/batch-2016-08-10/CreateSchedulingPolicy) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/batch-2016-08-10/CreateSchedulingPolicy) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/batch-2016-08-10/CreateSchedulingPolicy) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/CreateSchedulingPolicy) 