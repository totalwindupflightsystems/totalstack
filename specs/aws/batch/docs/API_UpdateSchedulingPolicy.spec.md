---
id: "@specs/aws/batch/docs/API_UpdateSchedulingPolicy"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateSchedulingPolicy"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# UpdateSchedulingPolicy

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_UpdateSchedulingPolicy
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateSchedulingPolicy
<a name="API_UpdateSchedulingPolicy"></a>

Updates a scheduling policy.

## Request Syntax
<a name="API_UpdateSchedulingPolicy_RequestSyntax"></a>

```
POST /v1/updateschedulingpolicy HTTP/1.1
Content-type: application/json

{
   "arn": "{{string}}",
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
   "quotaSharePolicy": { 
      "idleResourceAssignmentStrategy": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_UpdateSchedulingPolicy_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateSchedulingPolicy_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [arn](#API_UpdateSchedulingPolicy_RequestSyntax) **   <a name="Batch-UpdateSchedulingPolicy-request-arn"></a>
The Amazon Resource Name (ARN) of the scheduling policy to update.  
Type: String  
Required: Yes

 ** [fairsharePolicy](#API_UpdateSchedulingPolicy_RequestSyntax) **   <a name="Batch-UpdateSchedulingPolicy-request-fairsharePolicy"></a>
The fair-share policy scheduling details. Once set during creation, a fairsharePolicy cannot be removed or changed to a quotaSharePolicy.  
Type: [FairsharePolicy](API_FairsharePolicy.md) object  
Required: No

 ** [quotaSharePolicy](#API_UpdateSchedulingPolicy_RequestSyntax) **   <a name="Batch-UpdateSchedulingPolicy-request-quotaSharePolicy"></a>
The quota share scheduling policy details. Once set during creation, a quotaSharePolicy cannot be removed or changed to a fairsharePolicy.  
Type: [QuotaSharePolicy](API_QuotaSharePolicy.md) object  
Required: No

## Response Syntax
<a name="API_UpdateSchedulingPolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateSchedulingPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateSchedulingPolicy_Errors"></a>

 ** ClientException **   
These errors are usually caused by a client action. One example cause is using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Another cause is specifying an identifier that's not valid.  
HTTP Status Code: 400

 ** ServerException **   
These errors are usually caused by a server issue.  
HTTP Status Code: 500

## Examples
<a name="API_UpdateSchedulingPolicy_Examples"></a>

In the following example or examples, the Authorization header contents (` [authorization-params] `) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_UpdateSchedulingPolicy_Example_1"></a>

This example removes the "*Stage*" tag from the job definition with an ARN of "*arn:aws:batch:us-east-1:123456789012:job-definition/sleep30:1*".

#### Sample Request
<a name="API_UpdateSchedulingPolicy_Example_1_Request"></a>

```
POST /v1/updateschedulingpolicy HTTP/1.1
Host: batch.us-east-1.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/1.20.21 Python/3.6.9 Linux/4.4.0-19041-Microsoft botocore/1.21.21
X-Amz-Date: 20210929T022142Z
X-Amz-Security-Token: [security-token]
Authorization: [authorization-params]


{
  "arn": "arn:aws:batch:us-east-1:123456789012:scheduling-policy/ExampleFairSharePolicy3",
  "fairsharePolicy": {
    "shareDecaySeconds": 3600,
    "computeReservation": 1,
    "shareDistribution": [
      {
        "shareIdentifier": "MostImportant",
        "weightFactor": 0.0001
      },{
        "shareIdentifier": "Normal",
        "weightFactor": 1.0
      },{
        "shareIdentifier": "LeastImportant",
        "weightFactor": 999.9999
      }
    ]
  }
}
```

#### Sample Response
<a name="API_UpdateSchedulingPolicy_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Wed, 29 Sep 2021 02:21:43 GMT
Content-Type: application/json
Content-Length: 2
x-amzn-RequestId: [request-id]
Access-Control-Allow-Origin: *
x-amz-apigw-id: [apigw-id]
Access-Control-Expose-Headers: X-amzn-errortype,X-amzn-requestid,X-amzn-errormessage,X-amzn-trace-id,X-amz-apigw-id,date
X-Amzn-Trace-Id: [trace-id]
Connection: keep-alive

{}
```

## See Also
<a name="API_UpdateSchedulingPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/batch-2016-08-10/UpdateSchedulingPolicy) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/batch-2016-08-10/UpdateSchedulingPolicy) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/UpdateSchedulingPolicy) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/batch-2016-08-10/UpdateSchedulingPolicy) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/UpdateSchedulingPolicy) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/batch-2016-08-10/UpdateSchedulingPolicy) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/batch-2016-08-10/UpdateSchedulingPolicy) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/batch-2016-08-10/UpdateSchedulingPolicy) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/batch-2016-08-10/UpdateSchedulingPolicy) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/UpdateSchedulingPolicy) 