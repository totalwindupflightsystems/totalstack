---
id: "@specs/aws/sesv2/docs/API_UpdateReputationEntityCustomerManagedStatus"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateReputationEntityCustomerManagedStatus"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# UpdateReputationEntityCustomerManagedStatus

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_UpdateReputationEntityCustomerManagedStatus
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateReputationEntityCustomerManagedStatus
<a name="API_UpdateReputationEntityCustomerManagedStatus"></a>

Update the customer-managed sending status for a reputation entity. This allows you to enable, disable, or reinstate sending for the entity.

The customer-managed status works in conjunction with the AWS Amazon SES-managed status to determine the overall sending capability. When you update the customer-managed status, the AWS Amazon SES-managed status remains unchanged. If AWS Amazon SES has disabled the entity, it will not be allowed to send regardless of the customer-managed status setting. When you reinstate an entity through the customer-managed status, it can continue sending only if the AWS Amazon SES-managed status also permits sending, even if there are active reputation findings, until the findings are resolved or new violations occur.

## Request Syntax
<a name="API_UpdateReputationEntityCustomerManagedStatus_RequestSyntax"></a>

```
PUT /v2/email/reputation/entities/{{ReputationEntityType}}/{{ReputationEntityReference}}/customer-managed-status HTTP/1.1
Content-type: application/json

{
   "SendingStatus": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateReputationEntityCustomerManagedStatus_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ReputationEntityReference](#API_UpdateReputationEntityCustomerManagedStatus_RequestSyntax) **   <a name="SES-UpdateReputationEntityCustomerManagedStatus-request-uri-ReputationEntityReference"></a>
The unique identifier for the reputation entity. For resource-type entities, this is the Amazon Resource Name (ARN) of the resource.  
Length Constraints: Minimum length of 1.  
Required: Yes

 ** [ReputationEntityType](#API_UpdateReputationEntityCustomerManagedStatus_RequestSyntax) **   <a name="SES-UpdateReputationEntityCustomerManagedStatus-request-uri-ReputationEntityType"></a>
The type of reputation entity. Currently, only `RESOURCE` type entities are supported.  
Valid Values: `RESOURCE`   
Required: Yes

## Request Body
<a name="API_UpdateReputationEntityCustomerManagedStatus_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [SendingStatus](#API_UpdateReputationEntityCustomerManagedStatus_RequestSyntax) **   <a name="SES-UpdateReputationEntityCustomerManagedStatus-request-SendingStatus"></a>
The new customer-managed sending status for the reputation entity. This can be one of the following:  
+  `ENABLED` – Allow sending for this entity.
+  `DISABLED` – Prevent sending for this entity.
+  `REINSTATED` – Allow sending even if there are active reputation findings.
Type: String  
Valid Values: `ENABLED | REINSTATED | DISABLED`   
Required: Yes

## Response Syntax
<a name="API_UpdateReputationEntityCustomerManagedStatus_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateReputationEntityCustomerManagedStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateReputationEntityCustomerManagedStatus_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **   
The input you provided is invalid.  
HTTP Status Code: 400

 ** ConflictException **   
If there is already an ongoing account details update under review.  
HTTP Status Code: 409

 ** TooManyRequestsException **   
Too many requests have been made to the operation.  
HTTP Status Code: 429

## See Also
<a name="API_UpdateReputationEntityCustomerManagedStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sesv2-2019-09-27/UpdateReputationEntityCustomerManagedStatus) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sesv2-2019-09-27/UpdateReputationEntityCustomerManagedStatus) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/UpdateReputationEntityCustomerManagedStatus) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sesv2-2019-09-27/UpdateReputationEntityCustomerManagedStatus) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/UpdateReputationEntityCustomerManagedStatus) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sesv2-2019-09-27/UpdateReputationEntityCustomerManagedStatus) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sesv2-2019-09-27/UpdateReputationEntityCustomerManagedStatus) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sesv2-2019-09-27/UpdateReputationEntityCustomerManagedStatus) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sesv2-2019-09-27/UpdateReputationEntityCustomerManagedStatus) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/UpdateReputationEntityCustomerManagedStatus) 