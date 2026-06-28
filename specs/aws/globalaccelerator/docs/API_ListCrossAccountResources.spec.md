---
id: "@specs/aws/globalaccelerator/docs/API_ListCrossAccountResources"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListCrossAccountResources"
status: active
depends_on:
  - "@specs/aws/globalaccelerator/meta"
---

# ListCrossAccountResources

> **source:** AWS Documentation
> **spec:id:** @specs/aws/globalaccelerator/docs/API_ListCrossAccountResources
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListCrossAccountResources
<a name="API_ListCrossAccountResources"></a>

List the cross-account resources available to work with.

## Request Syntax
<a name="API_ListCrossAccountResources_RequestSyntax"></a>

```
{
   "AcceleratorArn": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "ResourceOwnerAwsAccountId": "{{string}}"
}
```

## Request Parameters
<a name="API_ListCrossAccountResources_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AcceleratorArn](#API_ListCrossAccountResources_RequestSyntax) **   <a name="globalaccelerator-ListCrossAccountResources-request-AcceleratorArn"></a>
The Amazon Resource Name (ARN) of an accelerator in a cross-account attachment.  
Type: String  
Length Constraints: Maximum length of 255.  
Required: No

 ** [MaxResults](#API_ListCrossAccountResources_RequestSyntax) **   <a name="globalaccelerator-ListCrossAccountResources-request-MaxResults"></a>
The number of cross-account resource objects that you want to return with this call. The default value is 10.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 100.  
Required: No

 ** [NextToken](#API_ListCrossAccountResources_RequestSyntax) **   <a name="globalaccelerator-ListCrossAccountResources-request-NextToken"></a>
The token for the next set of results. You receive this token from a previous call.  
Type: String  
Length Constraints: Maximum length of 255.  
Required: No

 ** [ResourceOwnerAwsAccountId](#API_ListCrossAccountResources_RequestSyntax) **   <a name="globalaccelerator-ListCrossAccountResources-request-ResourceOwnerAwsAccountId"></a>
The account ID of a resource owner in a cross-account attachment.  
Type: String  
Length Constraints: Fixed length of 12.  
Pattern: `^\d{12}$`   
Required: Yes

## Response Syntax
<a name="API_ListCrossAccountResources_ResponseSyntax"></a>

```
{
   "CrossAccountResources": [ 
      { 
         "AttachmentArn": "string",
         "Cidr": "string",
         "EndpointId": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListCrossAccountResources_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CrossAccountResources](#API_ListCrossAccountResources_ResponseSyntax) **   <a name="globalaccelerator-ListCrossAccountResources-response-CrossAccountResources"></a>
The cross-account resources used with an accelerator.  
Type: Array of [CrossAccountResource](API_CrossAccountResource.md) objects

 ** [NextToken](#API_ListCrossAccountResources_ResponseSyntax) **   <a name="globalaccelerator-ListCrossAccountResources-response-NextToken"></a>
The token for the next set of results. You receive this token from a previous call.  
Type: String  
Length Constraints: Maximum length of 255.

## Errors
<a name="API_ListCrossAccountResources_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AcceleratorNotFoundException **   
The accelerator that you specified doesn't exist.  
HTTP Status Code: 400

 ** AccessDeniedException **   
You don't have access permission.  
HTTP Status Code: 400

 ** InternalServiceErrorException **   
There was an internal error for AWS Global Accelerator.  
HTTP Status Code: 400

 ** InvalidArgumentException **   
An argument that you specified is invalid.  
HTTP Status Code: 400

 ** InvalidNextTokenException **   
There isn't another item to return.  
HTTP Status Code: 400

## See Also
<a name="API_ListCrossAccountResources_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/globalaccelerator-2018-08-08/ListCrossAccountResources) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/globalaccelerator-2018-08-08/ListCrossAccountResources) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/globalaccelerator-2018-08-08/ListCrossAccountResources) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/globalaccelerator-2018-08-08/ListCrossAccountResources) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/globalaccelerator-2018-08-08/ListCrossAccountResources) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/globalaccelerator-2018-08-08/ListCrossAccountResources) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/globalaccelerator-2018-08-08/ListCrossAccountResources) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/globalaccelerator-2018-08-08/ListCrossAccountResources) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/globalaccelerator-2018-08-08/ListCrossAccountResources) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/globalaccelerator-2018-08-08/ListCrossAccountResources) 