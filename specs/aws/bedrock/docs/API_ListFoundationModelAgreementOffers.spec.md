---
id: "@specs/aws/bedrock/docs/API_ListFoundationModelAgreementOffers"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListFoundationModelAgreementOffers"
status: active
depends_on:
  - "@specs/aws/bedrock/meta"
---

# ListFoundationModelAgreementOffers

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock/docs/API_ListFoundationModelAgreementOffers
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListFoundationModelAgreementOffers
<a name="API_ListFoundationModelAgreementOffers"></a>

Get the offers associated with the specified model.

## Request Syntax
<a name="API_ListFoundationModelAgreementOffers_RequestSyntax"></a>

```
GET /list-foundation-model-agreement-offers/{{modelId}}?offerType={{offerType}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListFoundationModelAgreementOffers_RequestParameters"></a>

The request uses the following URI parameters.

 ** [modelId](#API_ListFoundationModelAgreementOffers_RequestSyntax) **   <a name="bedrock-ListFoundationModelAgreementOffers-request-uri-modelId"></a>
Model Id of the foundation model.  
Length Constraints: Minimum length of 0. Maximum length of 140.  
Pattern: `[a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([a-z0-9-]{1,63}[.]){0,2}[a-z0-9-]{1,63}([:][a-z0-9-]{1,63}){0,2}(/[a-z0-9]{12}|)`   
Required: Yes

 ** [offerType](#API_ListFoundationModelAgreementOffers_RequestSyntax) **   <a name="bedrock-ListFoundationModelAgreementOffers-request-uri-offerType"></a>
 Type of offer associated with the model.   
Valid Values: `ALL | PUBLIC` 

## Request Body
<a name="API_ListFoundationModelAgreementOffers_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListFoundationModelAgreementOffers_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "modelId": "string",
   "offers": [ 
      { 
         "offerId": "string",
         "offerToken": "string",
         "termDetails": { 
            "legalTerm": { 
               "url": "string"
            },
            "supportTerm": { 
               "refundPolicyDescription": "string"
            },
            "usageBasedPricingTerm": { 
               "rateCard": [ 
                  { 
                     "description": "string",
                     "dimension": "string",
                     "price": "string",
                     "unit": "string"
                  }
               ]
            },
            "validityTerm": { 
               "agreementDuration": "string"
            }
         }
      }
   ]
}
```

## Response Elements
<a name="API_ListFoundationModelAgreementOffers_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [modelId](#API_ListFoundationModelAgreementOffers_ResponseSyntax) **   <a name="bedrock-ListFoundationModelAgreementOffers-response-modelId"></a>
Model Id of the foundation model.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 140.  
Pattern: `[a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([a-z0-9-]{1,63}[.]){0,2}[a-z0-9-]{1,63}([:][a-z0-9-]{1,63}){0,2}(/[a-z0-9]{12}|)` 

 ** [offers](#API_ListFoundationModelAgreementOffers_ResponseSyntax) **   <a name="bedrock-ListFoundationModelAgreementOffers-response-offers"></a>
List of the offers associated with the specified model.  
Type: Array of [Offer](API_Offer.md) objects

## Errors
<a name="API_ListFoundationModelAgreementOffers_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
The request is denied because of missing access permissions.  
HTTP Status Code: 403

 ** InternalServerException **   
An internal server error occurred. Retry your request.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.  
HTTP Status Code: 404

 ** ThrottlingException **   
The number of requests exceeds the limit. Resubmit your request later.  
HTTP Status Code: 429

 ** ValidationException **   
Input validation failed. Check your request parameters and retry the request.  
HTTP Status Code: 400

## See Also
<a name="API_ListFoundationModelAgreementOffers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/ListFoundationModelAgreementOffers) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/ListFoundationModelAgreementOffers) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/ListFoundationModelAgreementOffers) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/ListFoundationModelAgreementOffers) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/ListFoundationModelAgreementOffers) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/ListFoundationModelAgreementOffers) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/ListFoundationModelAgreementOffers) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/ListFoundationModelAgreementOffers) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/ListFoundationModelAgreementOffers) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/ListFoundationModelAgreementOffers) 