---
id: "@specs/aws/sesv2/docs/API_DeleteContactList"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteContactList"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# DeleteContactList

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_DeleteContactList
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteContactList
<a name="API_DeleteContactList"></a>

Deletes a contact list and all of the contacts on that list.

## Request Syntax
<a name="API_DeleteContactList_RequestSyntax"></a>

```
DELETE /v2/email/contact-lists/{{ContactListName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteContactList_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ContactListName](#API_DeleteContactList_RequestSyntax) **   <a name="SES-DeleteContactList-request-uri-ContactListName"></a>
The name of the contact list.  
Required: Yes

## Request Body
<a name="API_DeleteContactList_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteContactList_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteContactList_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteContactList_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **   
The input you provided is invalid.  
HTTP Status Code: 400

 ** ConcurrentModificationException **   
The resource is being modified by another operation or thread.  
HTTP Status Code: 500

 ** NotFoundException **   
The resource you attempted to access doesn't exist.  
HTTP Status Code: 404

 ** TooManyRequestsException **   
Too many requests have been made to the operation.  
HTTP Status Code: 429

## See Also
<a name="API_DeleteContactList_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sesv2-2019-09-27/DeleteContactList) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sesv2-2019-09-27/DeleteContactList) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/DeleteContactList) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sesv2-2019-09-27/DeleteContactList) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/DeleteContactList) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sesv2-2019-09-27/DeleteContactList) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sesv2-2019-09-27/DeleteContactList) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sesv2-2019-09-27/DeleteContactList) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sesv2-2019-09-27/DeleteContactList) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/DeleteContactList) 