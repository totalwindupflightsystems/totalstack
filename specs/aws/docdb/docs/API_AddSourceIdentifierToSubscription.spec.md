---
id: "@specs/aws/docdb/docs/API_AddSourceIdentifierToSubscription"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AddSourceIdentifierToSubscription"
status: active
depends_on:
  - "@specs/aws/docdb/meta"
---

# AddSourceIdentifierToSubscription

> **source:** AWS Documentation
> **spec:id:** @specs/aws/docdb/docs/API_AddSourceIdentifierToSubscription
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AddSourceIdentifierToSubscription
<a name="API_AddSourceIdentifierToSubscription"></a>

Adds a source identifier to an existing event notification subscription.

## Request Parameters
<a name="API_AddSourceIdentifierToSubscription_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** SourceIdentifier **   
The identifier of the event source to be added:  
+ If the source type is an instance, a `DBInstanceIdentifier` must be provided.
+ If the source type is a security group, a `DBSecurityGroupName` must be provided.
+ If the source type is a parameter group, a `DBParameterGroupName` must be provided.
+ If the source type is a snapshot, a `DBSnapshotIdentifier` must be provided.
Type: String  
Required: Yes

 ** SubscriptionName **   
The name of the Amazon DocumentDB event notification subscription that you want to add a source identifier to.  
Type: String  
Required: Yes

## Response Elements
<a name="API_AddSourceIdentifierToSubscription_ResponseElements"></a>

The following element is returned by the service.

 ** EventSubscription **   
Detailed information about an event to which you have subscribed.  
Type: [EventSubscription](API_EventSubscription.md) object

## Errors
<a name="API_AddSourceIdentifierToSubscription_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** SourceNotFound **   
The requested source could not be found.   
HTTP Status Code: 404

 ** SubscriptionNotFound **   
The subscription name does not exist.   
HTTP Status Code: 404

## See Also
<a name="API_AddSourceIdentifierToSubscription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/docdb-2014-10-31/AddSourceIdentifierToSubscription) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/docdb-2014-10-31/AddSourceIdentifierToSubscription) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/docdb-2014-10-31/AddSourceIdentifierToSubscription) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/docdb-2014-10-31/AddSourceIdentifierToSubscription) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/docdb-2014-10-31/AddSourceIdentifierToSubscription) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/docdb-2014-10-31/AddSourceIdentifierToSubscription) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/docdb-2014-10-31/AddSourceIdentifierToSubscription) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/docdb-2014-10-31/AddSourceIdentifierToSubscription) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/docdb-2014-10-31/AddSourceIdentifierToSubscription) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/docdb-2014-10-31/AddSourceIdentifierToSubscription) 