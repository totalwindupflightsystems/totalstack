---
id: "@specs/aws/fsx/docs/API_DeleteFileCache"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteFileCache"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# DeleteFileCache

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_DeleteFileCache
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteFileCache
<a name="API_DeleteFileCache"></a>

Deletes an Amazon File Cache resource. After deletion, the cache no longer exists, and its data is gone.

The `DeleteFileCache` operation returns while the cache has the `DELETING` status. You can check the cache deletion status by calling the [DescribeFileCaches](https://docs.aws.amazon.com/fsx/latest/APIReference/API_DescribeFileCaches.html) operation, which returns a list of caches in your account. If you pass the cache ID for a deleted cache, the `DescribeFileCaches` operation returns a `FileCacheNotFound` error.

**Important**  
The data in a deleted cache is also deleted and can't be recovered by any means.

## Request Syntax
<a name="API_DeleteFileCache_RequestSyntax"></a>

```
{
   "ClientRequestToken": "{{string}}",
   "FileCacheId": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteFileCache_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientRequestToken](#API_DeleteFileCache_RequestSyntax) **   <a name="FSx-DeleteFileCache-request-ClientRequestToken"></a>
(Optional) An idempotency token for resource creation, in a string of up to 63 ASCII characters. This token is automatically filled on your behalf when you use the AWS Command Line Interface (AWS CLI) or an AWS SDK.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `[A-za-z0-9_.-]{0,63}$`   
Required: No

 ** [FileCacheId](#API_DeleteFileCache_RequestSyntax) **   <a name="FSx-DeleteFileCache-request-FileCacheId"></a>
The ID of the cache that's being deleted.  
Type: String  
Length Constraints: Minimum length of 11. Maximum length of 21.  
Pattern: `^(fc-[0-9a-f]{8,})$`   
Required: Yes

## Response Syntax
<a name="API_DeleteFileCache_ResponseSyntax"></a>

```
{
   "FileCacheId": "string",
   "Lifecycle": "string"
}
```

## Response Elements
<a name="API_DeleteFileCache_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FileCacheId](#API_DeleteFileCache_ResponseSyntax) **   <a name="FSx-DeleteFileCache-response-FileCacheId"></a>
The ID of the cache that's being deleted.  
Type: String  
Length Constraints: Minimum length of 11. Maximum length of 21.  
Pattern: `^(fc-[0-9a-f]{8,})$` 

 ** [Lifecycle](#API_DeleteFileCache_ResponseSyntax) **   <a name="FSx-DeleteFileCache-response-Lifecycle"></a>
The cache lifecycle for the deletion request. If the `DeleteFileCache` operation is successful, this status is `DELETING`.  
Type: String  
Valid Values: `AVAILABLE | CREATING | DELETING | UPDATING | FAILED` 

## Errors
<a name="API_DeleteFileCache_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequest **   
A generic error indicating a failure with a client request.    
 ** Message **   
A detailed error message.
HTTP Status Code: 400

 ** FileCacheNotFound **   
No caches were found based upon supplied parameters.    
 ** Message **   
A detailed error message.
HTTP Status Code: 400

 ** IncompatibleParameterError **   
The error returned when a second request is received with the same client request token but different parameters settings. A client request token should always uniquely identify a single request.    
 ** Message **   
A detailed error message.  
 ** Parameter **   
A parameter that is incompatible with the earlier request.
HTTP Status Code: 400

 ** InternalServerError **   
A generic error indicating a server-side failure.    
 ** Message **   
A detailed error message.
HTTP Status Code: 500

 ** ServiceLimitExceeded **   
An error indicating that a particular service limit was exceeded. You can increase some service limits by contacting AWS Support.    
 ** Limit **   
Enumeration of the service limit that was exceeded.   
 ** Message **   
A detailed error message.
HTTP Status Code: 400

## See Also
<a name="API_DeleteFileCache_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/fsx-2018-03-01/DeleteFileCache) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/fsx-2018-03-01/DeleteFileCache) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/DeleteFileCache) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/fsx-2018-03-01/DeleteFileCache) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/DeleteFileCache) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/fsx-2018-03-01/DeleteFileCache) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/fsx-2018-03-01/DeleteFileCache) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/fsx-2018-03-01/DeleteFileCache) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/fsx-2018-03-01/DeleteFileCache) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/DeleteFileCache) 