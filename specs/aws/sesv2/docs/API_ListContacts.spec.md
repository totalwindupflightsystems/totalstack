---
id: "@specs/aws/sesv2/docs/API_ListContacts"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListContacts"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# ListContacts

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_ListContacts
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListContacts
<a name="API_ListContacts"></a>

Lists the contacts present in a specific contact list.

## Request Syntax
<a name="API_ListContacts_RequestSyntax"></a>

```
POST /v2/email/contact-lists/{{ContactListName}}/contacts/list HTTP/1.1
Content-type: application/json

{
   "Filter": { 
      "FilteredStatus": "{{string}}",
      "TopicFilter": { 
         "TopicName": "{{string}}",
         "UseDefaultIfPreferenceUnavailable": {{boolean}}
      }
   },
   "NextToken": "{{string}}",
   "PageSize": {{number}}
}
```

## URI Request Parameters
<a name="API_ListContacts_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ContactListName](#API_ListContacts_RequestSyntax) **   <a name="SES-ListContacts-request-uri-ContactListName"></a>
The name of the contact list.  
Required: Yes

## Request Body
<a name="API_ListContacts_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Filter](#API_ListContacts_RequestSyntax) **   <a name="SES-ListContacts-request-Filter"></a>
A filter that can be applied to a list of contacts.  
Type: [ListContactsFilter](API_ListContactsFilter.md) object  
Required: No

 ** [NextToken](#API_ListContacts_RequestSyntax) **   <a name="SES-ListContacts-request-NextToken"></a>
A string token indicating that there might be additional contacts available to be listed. Use the token provided in the Response to use in the subsequent call to ListContacts with the same parameters to retrieve the next page of contacts.  
Type: String  
Required: No

 ** [PageSize](#API_ListContacts_RequestSyntax) **   <a name="SES-ListContacts-request-PageSize"></a>
The number of contacts that may be returned at once, which is dependent on if there are more or less contacts than the value of the PageSize. Use this parameter to paginate results. If additional contacts exist beyond the specified limit, the `NextToken` element is sent in the response. Use the `NextToken` value in subsequent requests to retrieve additional contacts.  
Type: Integer  
Required: No

## Response Syntax
<a name="API_ListContacts_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Contacts": [ 
      { 
         "EmailAddress": "string",
         "LastUpdatedTimestamp": number,
         "TopicDefaultPreferences": [ 
            { 
               "SubscriptionStatus": "string",
               "TopicName": "string"
            }
         ],
         "TopicPreferences": [ 
            { 
               "SubscriptionStatus": "string",
               "TopicName": "string"
            }
         ],
         "UnsubscribeAll": boolean
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListContacts_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Contacts](#API_ListContacts_ResponseSyntax) **   <a name="SES-ListContacts-response-Contacts"></a>
The contacts present in a specific contact list.  
Type: Array of [Contact](API_Contact.md) objects

 ** [NextToken](#API_ListContacts_ResponseSyntax) **   <a name="SES-ListContacts-response-NextToken"></a>
A string token indicating that there might be additional contacts available to be listed. Copy this token to a subsequent call to `ListContacts` with the same parameters to retrieve the next page of contacts.  
Type: String

## Errors
<a name="API_ListContacts_Errors"></a>

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
<a name="API_ListContacts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sesv2-2019-09-27/ListContacts) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sesv2-2019-09-27/ListContacts) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/ListContacts) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sesv2-2019-09-27/ListContacts) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/ListContacts) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sesv2-2019-09-27/ListContacts) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sesv2-2019-09-27/ListContacts) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sesv2-2019-09-27/ListContacts) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sesv2-2019-09-27/ListContacts) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/ListContacts) 