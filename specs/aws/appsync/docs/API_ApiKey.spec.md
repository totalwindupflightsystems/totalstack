---
id: "@specs/aws/appsync/docs/API_ApiKey"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ApiKey"
status: active
depends_on:
  - "@specs/aws/appsync/meta"
---

# ApiKey

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appsync/docs/API_ApiKey
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ApiKey
<a name="API_ApiKey"></a>

Describes an API key.

Customers invoke AWS AppSync GraphQL API operations with API keys as an identity mechanism. There are two key versions:

 **da1**: We introduced this version at launch in November 2017. These keys always expire after 7 days. Amazon DynamoDB TTL manages key expiration. These keys ceased to be valid after February 21, 2018, and they should no longer be used.
+  `ListApiKeys` returns the expiration time in milliseconds.
+  `CreateApiKey` returns the expiration time in milliseconds.
+  `UpdateApiKey` is not available for this key version.
+  `DeleteApiKey` deletes the item from the table.
+ Expiration is stored in DynamoDB as milliseconds. This results in a bug where keys are not automatically deleted because DynamoDB expects the TTL to be stored in seconds. As a one-time action, we deleted these keys from the table on February 21, 2018.

 **da2**: We introduced this version in February 2018 when AWS AppSync added support to extend key expiration.
+  `ListApiKeys` returns the expiration time and deletion time in seconds.
+  `CreateApiKey` returns the expiration time and deletion time in seconds and accepts a user-provided expiration time in seconds.
+  `UpdateApiKey` returns the expiration time and and deletion time in seconds and accepts a user-provided expiration time in seconds. Expired API keys are kept for 60 days after the expiration time. You can update the key expiration time as long as the key isn't deleted.
+  `DeleteApiKey` deletes the item from the table.
+ Expiration is stored in DynamoDB as seconds. After the expiration time, using the key to authenticate will fail. However, you can reinstate the key before deletion.
+ Deletion is stored in DynamoDB as seconds. The key is deleted after deletion time.

## Contents
<a name="API_ApiKey_Contents"></a>

 ** deletes **   <a name="appsync-Type-ApiKey-deletes"></a>
The time after which the API key is deleted. The date is represented as seconds since the epoch, rounded down to the nearest hour.  
Type: Long  
Required: No

 ** description **   <a name="appsync-Type-ApiKey-description"></a>
A description of the purpose of the API key.  
Type: String  
Required: No

 ** expires **   <a name="appsync-Type-ApiKey-expires"></a>
The time after which the API key expires. The date is represented as seconds since the epoch, rounded down to the nearest hour.  
Type: Long  
Required: No

 ** id **   <a name="appsync-Type-ApiKey-id"></a>
The API key ID.  
Type: String  
Required: No

## See Also
<a name="API_ApiKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appsync-2017-07-25/ApiKey) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appsync-2017-07-25/ApiKey) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appsync-2017-07-25/ApiKey) 