---
id: "@specs/aws/docdb/docs/API_RemoveSourceIdentifierFromSubscription"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RemoveSourceIdentifierFromSubscription"
status: active
depends_on:
  - "@specs/aws/docdb/meta"
---

# RemoveSourceIdentifierFromSubscription

> **source:** AWS Documentation
> **spec:id:** @specs/aws/docdb/docs/API_RemoveSourceIdentifierFromSubscription
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RemoveSourceIdentifierFromSubscription
<a name="API_RemoveSourceIdentifierFromSubscription"></a>

Removes a source identifier from an existing Amazon DocumentDB event notification subscription.

## Request Parameters
<a name="API_RemoveSourceIdentifierFromSubscription_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** SourceIdentifier **   
 The source identifier to be removed from the subscription, such as the instance identifier for an instance, or the name of a security group.   
Type: String  
Required: Yes

 ** SubscriptionName **   
The name of the Amazon DocumentDB event notification subscription that you want to remove a source identifier from.  
Type: String  
Required: Yes

## Response Elements
<a name="API_RemoveSourceIdentifierFromSubscription_ResponseElements"></a>

The following element is returned by the service.

 ** EventSubscription **   
Detailed information about an event to which you have subscribed.  
Type: [EventSubscription](API_EventSubscription.md) object

## Errors
<a name="API_RemoveSourceIdentifierFromSubscription_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** SourceNotFound **   
The requested source could not be found.   
HTTP Status Code: 404

 ** SubscriptionNotFound **   
The subscription name does not exist.   
HTTP Status Code: 404

## See Also
<a name="API_RemoveSourceIdentifierFromSubscription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/docdb-2014-10-31/RemoveSourceIdentifierFromSubscription) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/docdb-2014-10-31/RemoveSourceIdentifierFromSubscription) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/docdb-2014-10-31/RemoveSourceIdentifierFromSubscription) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/docdb-2014-10-31/RemoveSourceIdentifierFromSubscription) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/docdb-2014-10-31/RemoveSourceIdentifierFromSubscription) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/docdb-2014-10-31/RemoveSourceIdentifierFromSubscription) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/docdb-2014-10-31/RemoveSourceIdentifierFromSubscription) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/docdb-2014-10-31/RemoveSourceIdentifierFromSubscription) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/docdb-2014-10-31/RemoveSourceIdentifierFromSubscription) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/docdb-2014-10-31/RemoveSourceIdentifierFromSubscription) 