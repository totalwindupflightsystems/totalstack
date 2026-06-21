---
id: "@specs/aws/cloudtrail/docs/API_DeleteChannel"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteChannel"
status: active
depends_on:
  - "@specs/aws/cloudtrail/meta"
---

# DeleteChannel

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudtrail/docs/API_DeleteChannel
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteChannel
<a name="API_DeleteChannel"></a>

**Important**  
CloudTrail Lake will no longer be open to new customers starting May 31, 2026. If you would like to use CloudTrail Lake, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [CloudTrail Lake availability change](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake-service-availability-change.html).

Deletes a channel.

## Request Syntax
<a name="API_DeleteChannel_RequestSyntax"></a>

```
{
   "Channel": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteChannel_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Channel](#API_DeleteChannel_RequestSyntax) **   <a name="awscloudtrail-DeleteChannel-request-Channel"></a>
The ARN or the `UUID` value of the channel that you want to delete.  
Type: String  
Length Constraints: Minimum length of 3. Maximum length of 256.  
Pattern: `^[a-zA-Z0-9._/\-:]+$`   
Required: Yes

## Response Elements
<a name="API_DeleteChannel_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteChannel_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ChannelARNInvalidException **   
This exception is thrown when the specified value of `ChannelARN` is not valid.  
HTTP Status Code: 400

 ** ChannelNotFoundException **   
This exception is thrown when CloudTrail cannot find the specified channel.  
HTTP Status Code: 400

 ** OperationNotPermittedException **   
This exception is thrown when the requested operation is not permitted.  
HTTP Status Code: 400

 ** UnsupportedOperationException **   
This exception is thrown when the requested operation is not supported.  
HTTP Status Code: 400

## See Also
<a name="API_DeleteChannel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudtrail-2013-11-01/DeleteChannel) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudtrail-2013-11-01/DeleteChannel) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/DeleteChannel) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudtrail-2013-11-01/DeleteChannel) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/DeleteChannel) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudtrail-2013-11-01/DeleteChannel) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudtrail-2013-11-01/DeleteChannel) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudtrail-2013-11-01/DeleteChannel) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudtrail-2013-11-01/DeleteChannel) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/DeleteChannel) 