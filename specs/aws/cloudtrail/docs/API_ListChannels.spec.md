---
id: "@specs/aws/cloudtrail/docs/API_ListChannels"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListChannels"
status: active
depends_on:
  - "@specs/aws/cloudtrail/meta"
---

# ListChannels

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudtrail/docs/API_ListChannels
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListChannels
<a name="API_ListChannels"></a>

**Important**  
CloudTrail Lake will no longer be open to new customers starting May 31, 2026. If you would like to use CloudTrail Lake, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [CloudTrail Lake availability change](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake-service-availability-change.html).

 Lists the channels in the current account, and their source names. 

## Request Syntax
<a name="API_ListChannels_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListChannels_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListChannels_RequestSyntax) **   <a name="awscloudtrail-ListChannels-request-MaxResults"></a>
 The maximum number of CloudTrail channels to display on a single page.   
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 1000.  
Required: No

 ** [NextToken](#API_ListChannels_RequestSyntax) **   <a name="awscloudtrail-ListChannels-request-NextToken"></a>
The token to use to get the next page of results after a previous API call. This token must be passed in with the same parameters that were specified in the original call. For example, if the original call specified an AttributeKey of 'Username' with a value of 'root', the call with NextToken should include those same parameters.  
Type: String  
Length Constraints: Minimum length of 4. Maximum length of 1000.  
Pattern: `.*`   
Required: No

## Response Syntax
<a name="API_ListChannels_ResponseSyntax"></a>

```
{
   "Channels": [ 
      { 
         "ChannelArn": "string",
         "Name": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListChannels_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Channels](#API_ListChannels_ResponseSyntax) **   <a name="awscloudtrail-ListChannels-response-Channels"></a>
 The list of channels in the account.   
Type: Array of [Channel](API_Channel.md) objects

 ** [NextToken](#API_ListChannels_ResponseSyntax) **   <a name="awscloudtrail-ListChannels-response-NextToken"></a>
The token to use to get the next page of results after a previous API call.  
Type: String  
Length Constraints: Minimum length of 4. Maximum length of 1000.  
Pattern: `.*` 

## Errors
<a name="API_ListChannels_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidNextTokenException **   
A token that is not valid, or a token that was previously used in a request with different parameters. This exception is thrown if the token is not valid.  
HTTP Status Code: 400

 ** OperationNotPermittedException **   
This exception is thrown when the requested operation is not permitted.  
HTTP Status Code: 400

 ** UnsupportedOperationException **   
This exception is thrown when the requested operation is not supported.  
HTTP Status Code: 400

## See Also
<a name="API_ListChannels_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudtrail-2013-11-01/ListChannels) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudtrail-2013-11-01/ListChannels) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/ListChannels) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudtrail-2013-11-01/ListChannels) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/ListChannels) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudtrail-2013-11-01/ListChannels) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudtrail-2013-11-01/ListChannels) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudtrail-2013-11-01/ListChannels) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudtrail-2013-11-01/ListChannels) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/ListChannels) 