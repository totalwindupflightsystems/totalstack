---
id: "@specs/aws/sesv2/docs/API_GetContactList"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetContactList"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# GetContactList

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_GetContactList
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetContactList
<a name="API_GetContactList"></a>

Returns contact list metadata. It does not return any information about the contacts present in the list.

## Request Syntax
<a name="API_GetContactList_RequestSyntax"></a>

```
GET /v2/email/contact-lists/{{ContactListName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetContactList_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ContactListName](#API_GetContactList_RequestSyntax) **   <a name="SES-GetContactList-request-uri-ContactListName"></a>
The name of the contact list.  
Required: Yes

## Request Body
<a name="API_GetContactList_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetContactList_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ContactListName": "string",
   "CreatedTimestamp": number,
   "Description": "string",
   "LastUpdatedTimestamp": number,
   "Tags": [ 
      { 
         "Key": "string",
         "Value": "string"
      }
   ],
   "Topics": [ 
      { 
         "DefaultSubscriptionStatus": "string",
         "Description": "string",
         "DisplayName": "string",
         "TopicName": "string"
      }
   ]
}
```

## Response Elements
<a name="API_GetContactList_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ContactListName](#API_GetContactList_ResponseSyntax) **   <a name="SES-GetContactList-response-ContactListName"></a>
The name of the contact list.  
Type: String

 ** [CreatedTimestamp](#API_GetContactList_ResponseSyntax) **   <a name="SES-GetContactList-response-CreatedTimestamp"></a>
A timestamp noting when the contact list was created.  
Type: Timestamp

 ** [Description](#API_GetContactList_ResponseSyntax) **   <a name="SES-GetContactList-response-Description"></a>
A description of what the contact list is about.  
Type: String

 ** [LastUpdatedTimestamp](#API_GetContactList_ResponseSyntax) **   <a name="SES-GetContactList-response-LastUpdatedTimestamp"></a>
A timestamp noting the last time the contact list was updated.  
Type: Timestamp

 ** [Tags](#API_GetContactList_ResponseSyntax) **   <a name="SES-GetContactList-response-Tags"></a>
The tags associated with a contact list.  
Type: Array of [Tag](API_Tag.md) objects

 ** [Topics](#API_GetContactList_ResponseSyntax) **   <a name="SES-GetContactList-response-Topics"></a>
An interest group, theme, or label within a list. A contact list can have multiple topics.  
Type: Array of [Topic](API_Topic.md) objects

## Errors
<a name="API_GetContactList_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **   
The input you provided is invalid.  
HTTP Status Code: 400

 ** NotFoundException **   
The resource you attempted to access doesn't exist.  
HTTP Status Code: 404

 ** TooManyRequestsException **   
Too many requests have been made to the operation.  
HTTP Status Code: 429

## See Also
<a name="API_GetContactList_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sesv2-2019-09-27/GetContactList) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sesv2-2019-09-27/GetContactList) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/GetContactList) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sesv2-2019-09-27/GetContactList) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/GetContactList) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sesv2-2019-09-27/GetContactList) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sesv2-2019-09-27/GetContactList) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sesv2-2019-09-27/GetContactList) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sesv2-2019-09-27/GetContactList) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/GetContactList) 