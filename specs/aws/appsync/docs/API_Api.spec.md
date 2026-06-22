---
id: "@specs/aws/appsync/docs/API_Api"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Api"
status: active
depends_on:
  - "@specs/aws/appsync/meta"
---

# Api

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appsync/docs/API_Api
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Api
<a name="API_Api"></a>

Describes an AWS AppSync API. You can use `Api` for an AWS AppSync API with your preferred configuration, such as an Event API that provides real-time message publishing and message subscriptions over WebSockets.

## Contents
<a name="API_Api_Contents"></a>

 ** apiArn **   <a name="appsync-Type-Api-apiArn"></a>
The Amazon Resource Name (ARN) for the `Api`.  
Type: String  
Required: No

 ** apiId **   <a name="appsync-Type-Api-apiId"></a>
The `Api` ID.  
Type: String  
Required: No

 ** created **   <a name="appsync-Type-Api-created"></a>
The date and time that the `Api` was created.  
Type: Timestamp  
Required: No

 ** dns **   <a name="appsync-Type-Api-dns"></a>
The DNS records for the API. This will include an HTTP and a real-time endpoint.  
Type: String to string map  
Required: No

 ** eventConfig **   <a name="appsync-Type-Api-eventConfig"></a>
The Event API configuration. This includes the default authorization configuration for connecting, publishing, and subscribing to an Event API.  
Type: [EventConfig](API_EventConfig.md) object  
Required: No

 ** name **   <a name="appsync-Type-Api-name"></a>
The name of the `Api`.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 50.  
Pattern: `[A-Za-z0-9_\-\ ]+`   
Required: No

 ** ownerContact **   <a name="appsync-Type-Api-ownerContact"></a>
The owner contact information for the `Api`   
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 250.  
Pattern: `[A-Za-z0-9_\-\ \.]+`   
Required: No

 ** tags **   <a name="appsync-Type-Api-tags"></a>
A map with keys of `TagKey` objects and values of `TagValue` objects.  
Type: String to string map  
Map Entries: Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `^(?!aws:)[ a-zA-Z+-=._:/]+$`   
Value Length Constraints: Maximum length of 256.  
Value Pattern: `^[\s\w+-=\.:/@]*$`   
Required: No

 ** wafWebAclArn **   <a name="appsync-Type-Api-wafWebAclArn"></a>
The Amazon Resource Name (ARN) of the AWS WAF web access control list (web ACL) associated with this `Api`, if one exists.  
Type: String  
Required: No

 ** xrayEnabled **   <a name="appsync-Type-Api-xrayEnabled"></a>
A flag indicating whether to use AWS X-Ray tracing for this `Api`.  
Type: Boolean  
Required: No

## See Also
<a name="API_Api_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appsync-2017-07-25/Api) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appsync-2017-07-25/Api) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appsync-2017-07-25/Api) 