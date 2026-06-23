---
id: "@specs/aws/amplify/docs/API_ListDomainAssociations"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListDomainAssociations"
status: active
depends_on:
  - "@specs/aws/amplify/meta"
---

# ListDomainAssociations

> **source:** AWS Documentation
> **spec:id:** @specs/aws/amplify/docs/API_ListDomainAssociations
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListDomainAssociations
<a name="API_ListDomainAssociations"></a>

Returns the domain associations for an Amplify app. 

## Request Syntax
<a name="API_ListDomainAssociations_RequestSyntax"></a>

```
GET /apps/{{appId}}/domains?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListDomainAssociations_RequestParameters"></a>

The request uses the following URI parameters.

 ** [appId](#API_ListDomainAssociations_RequestSyntax) **   <a name="amplify-ListDomainAssociations-request-uri-appId"></a>
 The unique ID for an Amplify app.   
Length Constraints: Minimum length of 1. Maximum length of 20.  
Pattern: `d[a-z0-9]+`   
Required: Yes

 ** [maxResults](#API_ListDomainAssociations_RequestSyntax) **   <a name="amplify-ListDomainAssociations-request-uri-maxResults"></a>
 The maximum number of records to list in a single response.   
Valid Range: Minimum value of 0. Maximum value of 50.

 ** [nextToken](#API_ListDomainAssociations_RequestSyntax) **   <a name="amplify-ListDomainAssociations-request-uri-nextToken"></a>
 A pagination token. Set to null to start listing apps from the start. If non-null, a pagination token is returned in a result. Pass its value in here to list more projects.   
Length Constraints: Maximum length of 2000.  
Pattern: `(?s).*` 

## Request Body
<a name="API_ListDomainAssociations_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListDomainAssociations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "domainAssociations": [ 
      { 
         "autoSubDomainCreationPatterns": [ "string" ],
         "autoSubDomainIAMRole": "string",
         "certificate": { 
            "certificateVerificationDNSRecord": "string",
            "customCertificateArn": "string",
            "type": "string"
         },
         "certificateVerificationDNSRecord": "string",
         "domainAssociationArn": "string",
         "domainName": "string",
         "domainStatus": "string",
         "enableAutoSubDomain": boolean,
         "statusReason": "string",
         "subDomains": [ 
            { 
               "dnsRecord": "string",
               "subDomainSetting": { 
                  "branchName": "string",
                  "prefix": "string"
               },
               "verified": boolean
            }
         ],
         "updateStatus": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListDomainAssociations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [domainAssociations](#API_ListDomainAssociations_ResponseSyntax) **   <a name="amplify-ListDomainAssociations-response-domainAssociations"></a>
 A list of domain associations.   
Type: Array of [DomainAssociation](API_DomainAssociation.md) objects  
Array Members: Maximum number of 255 items.

 ** [nextToken](#API_ListDomainAssociations_ResponseSyntax) **   <a name="amplify-ListDomainAssociations-response-nextToken"></a>
 A pagination token. If non-null, a pagination token is returned in a result. Pass its value in another request to retrieve more entries.   
Type: String  
Length Constraints: Maximum length of 2000.  
Pattern: `(?s).*` 

## Errors
<a name="API_ListDomainAssociations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **   
A request contains unexpected data.   
HTTP Status Code: 400

 ** InternalFailureException **   
The service failed to perform an operation due to an internal issue.   
HTTP Status Code: 500

 ** UnauthorizedException **   
An operation failed due to a lack of access.   
HTTP Status Code: 401

## See Also
<a name="API_ListDomainAssociations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/amplify-2017-07-25/ListDomainAssociations) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/amplify-2017-07-25/ListDomainAssociations) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amplify-2017-07-25/ListDomainAssociations) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/amplify-2017-07-25/ListDomainAssociations) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amplify-2017-07-25/ListDomainAssociations) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/amplify-2017-07-25/ListDomainAssociations) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/amplify-2017-07-25/ListDomainAssociations) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/amplify-2017-07-25/ListDomainAssociations) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/amplify-2017-07-25/ListDomainAssociations) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amplify-2017-07-25/ListDomainAssociations) 