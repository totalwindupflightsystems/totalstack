---
id: "@specs/aws/cloudtrail/docs/API_ListTrails"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListTrails"
status: active
depends_on:
  - "@specs/aws/cloudtrail/meta"
---

# ListTrails

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudtrail/docs/API_ListTrails
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListTrails
<a name="API_ListTrails"></a>

Lists trails that are in the current account.

## Request Syntax
<a name="API_ListTrails_RequestSyntax"></a>

```
{
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListTrails_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [NextToken](#API_ListTrails_RequestSyntax) **   <a name="awscloudtrail-ListTrails-request-NextToken"></a>
The token to use to get the next page of results after a previous API call. This token must be passed in with the same parameters that were specified in the original call. For example, if the original call specified an AttributeKey of 'Username' with a value of 'root', the call with NextToken should include those same parameters.  
Type: String  
Required: No

## Response Syntax
<a name="API_ListTrails_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "Trails": [ 
      { 
         "HomeRegion": "string",
         "Name": "string",
         "TrailARN": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListTrails_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListTrails_ResponseSyntax) **   <a name="awscloudtrail-ListTrails-response-NextToken"></a>
The token to use to get the next page of results after a previous API call. If the token does not appear, there are no more results to return. The token must be passed in with the same parameters as the previous call. For example, if the original call specified an AttributeKey of 'Username' with a value of 'root', the call with NextToken should include those same parameters.  
Type: String

 ** [Trails](#API_ListTrails_ResponseSyntax) **   <a name="awscloudtrail-ListTrails-response-Trails"></a>
Returns the name, ARN, and home Region of trails in the current account.  
Type: Array of [TrailInfo](API_TrailInfo.md) objects

## Errors
<a name="API_ListTrails_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** OperationNotPermittedException **   
This exception is thrown when the requested operation is not permitted.  
HTTP Status Code: 400

 ** UnsupportedOperationException **   
This exception is thrown when the requested operation is not supported.  
HTTP Status Code: 400

## See Also
<a name="API_ListTrails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudtrail-2013-11-01/ListTrails) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudtrail-2013-11-01/ListTrails) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/ListTrails) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudtrail-2013-11-01/ListTrails) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/ListTrails) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudtrail-2013-11-01/ListTrails) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudtrail-2013-11-01/ListTrails) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudtrail-2013-11-01/ListTrails) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudtrail-2013-11-01/ListTrails) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/ListTrails) 