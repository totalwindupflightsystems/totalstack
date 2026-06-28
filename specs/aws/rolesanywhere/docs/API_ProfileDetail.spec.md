---
id: "@specs/aws/rolesanywhere/docs/API_ProfileDetail"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ProfileDetail"
status: active
depends_on:
  - "@specs/aws/rolesanywhere/meta"
---

# ProfileDetail

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rolesanywhere/docs/API_ProfileDetail
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ProfileDetail
<a name="API_ProfileDetail"></a>

The state of the profile after a read or write operation.

## Contents
<a name="API_ProfileDetail_Contents"></a>

 ** acceptRoleSessionName **   <a name="rolesanywhere-Type-ProfileDetail-acceptRoleSessionName"></a>
Used to determine if a custom role session name will be accepted in a temporary credential request.  
Type: Boolean  
Required: No

 ** attributeMappings **   <a name="rolesanywhere-Type-ProfileDetail-attributeMappings"></a>
A mapping applied to the authenticating end-entity certificate.  
Type: Array of [AttributeMapping](API_AttributeMapping.md) objects  
Required: No

 ** createdAt **   <a name="rolesanywhere-Type-ProfileDetail-createdAt"></a>
The ISO-8601 timestamp when the profile was created.   
Type: Timestamp  
Required: No

 ** createdBy **   <a name="rolesanywhere-Type-ProfileDetail-createdBy"></a>
The AWS account that created the profile.  
Type: String  
Required: No

 ** durationSeconds **   <a name="rolesanywhere-Type-ProfileDetail-durationSeconds"></a>
 Used to determine how long sessions vended using this profile are valid for. See the `Expiration` section of the [CreateSession API documentation](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/authentication-create-session.html#credentials-object) page for more details. In requests, if this value is not provided, the default value will be 3600.   
Type: Integer  
Required: No

 ** enabled **   <a name="rolesanywhere-Type-ProfileDetail-enabled"></a>
Indicates whether the profile is enabled.  
Type: Boolean  
Required: No

 ** managedPolicyArns **   <a name="rolesanywhere-Type-ProfileDetail-managedPolicyArns"></a>
A list of managed policy ARNs that apply to the vended session credentials.   
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 50 items.  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Required: No

 ** name **   <a name="rolesanywhere-Type-ProfileDetail-name"></a>
The name of the profile.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[ a-zA-Z0-9-_]*`   
Required: No

 ** profileArn **   <a name="rolesanywhere-Type-ProfileDetail-profileArn"></a>
The ARN of the profile.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1011.  
Pattern: `arn:aws(-[^:]+)?:rolesanywhere(:.*){2}(:profile.*)`   
Required: No

 ** profileId **   <a name="rolesanywhere-Type-ProfileDetail-profileId"></a>
The unique identifier of the profile.  
Type: String  
Length Constraints: Fixed length of 36.  
Pattern: `.*[a-f0-9]{8}-([a-z0-9]{4}-){3}[a-z0-9]{12}.*`   
Required: No

 ** requireInstanceProperties **   <a name="rolesanywhere-Type-ProfileDetail-requireInstanceProperties"></a>
Unused, saved for future use. Will likely specify whether instance properties are required in temporary credential requests with this profile.   
Type: Boolean  
Required: No

 ** roleArns **   <a name="rolesanywhere-Type-ProfileDetail-roleArns"></a>
A list of IAM roles that this profile can assume in a temporary credential request.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 250 items.  
Length Constraints: Minimum length of 1. Maximum length of 1011.  
Pattern: `arn:aws(-[^:]+)?:iam(:.*){2}(:role.*)`   
Required: No

 ** sessionPolicy **   <a name="rolesanywhere-Type-ProfileDetail-sessionPolicy"></a>
A session policy that applies to the trust boundary of the vended session credentials.   
Type: String  
Required: No

 ** updatedAt **   <a name="rolesanywhere-Type-ProfileDetail-updatedAt"></a>
The ISO-8601 timestamp when the profile was last updated.   
Type: Timestamp  
Required: No

## See Also
<a name="API_ProfileDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rolesanywhere-2018-05-10/ProfileDetail) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rolesanywhere-2018-05-10/ProfileDetail) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rolesanywhere-2018-05-10/ProfileDetail) 