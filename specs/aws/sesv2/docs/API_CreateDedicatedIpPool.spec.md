---
id: "@specs/aws/sesv2/docs/API_CreateDedicatedIpPool"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateDedicatedIpPool"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# CreateDedicatedIpPool

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_CreateDedicatedIpPool
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateDedicatedIpPool
<a name="API_CreateDedicatedIpPool"></a>

Create a new pool of dedicated IP addresses. A pool can include one or more dedicated IP addresses that are associated with your AWS account. You can associate a pool with a configuration set. When you send an email that uses that configuration set, the message is sent from one of the addresses in the associated pool.

## Request Syntax
<a name="API_CreateDedicatedIpPool_RequestSyntax"></a>

```
POST /v2/email/dedicated-ip-pools HTTP/1.1
Content-type: application/json

{
   "PoolName": "{{string}}",
   "ScalingMode": "{{string}}",
   "Tags": [ 
      { 
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_CreateDedicatedIpPool_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateDedicatedIpPool_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [PoolName](#API_CreateDedicatedIpPool_RequestSyntax) **   <a name="SES-CreateDedicatedIpPool-request-PoolName"></a>
The name of the dedicated IP pool.  
Type: String  
Required: Yes

 ** [ScalingMode](#API_CreateDedicatedIpPool_RequestSyntax) **   <a name="SES-CreateDedicatedIpPool-request-ScalingMode"></a>
The type of scaling mode.  
Type: String  
Valid Values: `STANDARD | MANAGED`   
Required: No

 ** [Tags](#API_CreateDedicatedIpPool_RequestSyntax) **   <a name="SES-CreateDedicatedIpPool-request-Tags"></a>
An object that defines the tags (keys and values) that you want to associate with the pool.  
Type: Array of [Tag](API_Tag.md) objects  
Required: No

## Response Syntax
<a name="API_CreateDedicatedIpPool_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_CreateDedicatedIpPool_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_CreateDedicatedIpPool_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AlreadyExistsException **   
The resource specified in your request already exists.  
HTTP Status Code: 400

 ** BadRequestException **   
The input you provided is invalid.  
HTTP Status Code: 400

 ** ConcurrentModificationException **   
The resource is being modified by another operation or thread.  
HTTP Status Code: 500

 ** LimitExceededException **   
There are too many instances of the specified resource type.  
HTTP Status Code: 400

 ** TooManyRequestsException **   
Too many requests have been made to the operation.  
HTTP Status Code: 429

## See Also
<a name="API_CreateDedicatedIpPool_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sesv2-2019-09-27/CreateDedicatedIpPool) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sesv2-2019-09-27/CreateDedicatedIpPool) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/CreateDedicatedIpPool) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sesv2-2019-09-27/CreateDedicatedIpPool) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/CreateDedicatedIpPool) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sesv2-2019-09-27/CreateDedicatedIpPool) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sesv2-2019-09-27/CreateDedicatedIpPool) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sesv2-2019-09-27/CreateDedicatedIpPool) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sesv2-2019-09-27/CreateDedicatedIpPool) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/CreateDedicatedIpPool) 