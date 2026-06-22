---
id: "@specs/aws/sesv2/docs/API_GetDomainDeliverabilityCampaign"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetDomainDeliverabilityCampaign"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# GetDomainDeliverabilityCampaign

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_GetDomainDeliverabilityCampaign
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetDomainDeliverabilityCampaign
<a name="API_GetDomainDeliverabilityCampaign"></a>

Retrieve all the deliverability data for a specific campaign. This data is available for a campaign only if the campaign sent email by using a domain that the Deliverability dashboard is enabled for.

## Request Syntax
<a name="API_GetDomainDeliverabilityCampaign_RequestSyntax"></a>

```
GET /v2/email/deliverability-dashboard/campaigns/{{CampaignId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetDomainDeliverabilityCampaign_RequestParameters"></a>

The request uses the following URI parameters.

 ** [CampaignId](#API_GetDomainDeliverabilityCampaign_RequestSyntax) **   <a name="SES-GetDomainDeliverabilityCampaign-request-uri-CampaignId"></a>
The unique identifier for the campaign. The Deliverability dashboard automatically generates and assigns this identifier to a campaign.  
Required: Yes

## Request Body
<a name="API_GetDomainDeliverabilityCampaign_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetDomainDeliverabilityCampaign_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "DomainDeliverabilityCampaign": { 
      "CampaignId": "string",
      "DeleteRate": number,
      "Esps": [ "string" ],
      "FirstSeenDateTime": number,
      "FromAddress": "string",
      "ImageUrl": "string",
      "InboxCount": number,
      "LastSeenDateTime": number,
      "ProjectedVolume": number,
      "ReadDeleteRate": number,
      "ReadRate": number,
      "SendingIps": [ "string" ],
      "SpamCount": number,
      "Subject": "string"
   }
}
```

## Response Elements
<a name="API_GetDomainDeliverabilityCampaign_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DomainDeliverabilityCampaign](#API_GetDomainDeliverabilityCampaign_ResponseSyntax) **   <a name="SES-GetDomainDeliverabilityCampaign-response-DomainDeliverabilityCampaign"></a>
An object that contains the deliverability data for the campaign.  
Type: [DomainDeliverabilityCampaign](API_DomainDeliverabilityCampaign.md) object

## Errors
<a name="API_GetDomainDeliverabilityCampaign_Errors"></a>

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
<a name="API_GetDomainDeliverabilityCampaign_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sesv2-2019-09-27/GetDomainDeliverabilityCampaign) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sesv2-2019-09-27/GetDomainDeliverabilityCampaign) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/GetDomainDeliverabilityCampaign) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sesv2-2019-09-27/GetDomainDeliverabilityCampaign) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/GetDomainDeliverabilityCampaign) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sesv2-2019-09-27/GetDomainDeliverabilityCampaign) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sesv2-2019-09-27/GetDomainDeliverabilityCampaign) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sesv2-2019-09-27/GetDomainDeliverabilityCampaign) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sesv2-2019-09-27/GetDomainDeliverabilityCampaign) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/GetDomainDeliverabilityCampaign) 