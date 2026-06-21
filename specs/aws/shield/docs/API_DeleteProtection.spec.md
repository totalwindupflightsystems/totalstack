---
id: "@specs/aws/shield/docs/API_DeleteProtection"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteProtection"
status: active
depends_on:
  - "@specs/aws/shield/meta"
---

# DeleteProtection

> **source:** AWS Documentation
> **spec:id:** @specs/aws/shield/docs/API_DeleteProtection
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteProtection
<a name="API_DeleteProtection"></a>

Deletes an AWS Shield Advanced [Protection](API_Protection.md).

## Request Syntax
<a name="API_DeleteProtection_RequestSyntax"></a>

```
{
   "ProtectionId": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteProtection_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ProtectionId](#API_DeleteProtection_RequestSyntax) **   <a name="AWSShield-DeleteProtection-request-ProtectionId"></a>
The unique identifier (ID) for the [Protection](API_Protection.md) object to be deleted.  
Type: String  
Length Constraints: Fixed length of 36.  
Pattern: `[a-zA-Z0-9\\-]*`   
Required: Yes

## Response Elements
<a name="API_DeleteProtection_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteProtection_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalErrorException **   
Exception that indicates that a problem occurred with the service infrastructure. You can retry the request.  
HTTP Status Code: 500

 ** OptimisticLockException **   
Exception that indicates that the resource state has been modified by another client. Retrieve the resource and then retry your request.  
HTTP Status Code: 400

 ** ResourceNotFoundException **   
Exception indicating the specified resource does not exist. If available, this exception includes details in additional properties.     
 ** resourceType **   
Type of resource.
HTTP Status Code: 400

## See Also
<a name="API_DeleteProtection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/shield-2016-06-02/DeleteProtection) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/shield-2016-06-02/DeleteProtection) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/shield-2016-06-02/DeleteProtection) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/shield-2016-06-02/DeleteProtection) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/shield-2016-06-02/DeleteProtection) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/shield-2016-06-02/DeleteProtection) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/shield-2016-06-02/DeleteProtection) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/shield-2016-06-02/DeleteProtection) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/shield-2016-06-02/DeleteProtection) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/shield-2016-06-02/DeleteProtection) 