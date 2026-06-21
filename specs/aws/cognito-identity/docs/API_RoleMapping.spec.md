---
id: "@specs/aws/cognito-identity/docs/API_RoleMapping"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RoleMapping"
status: active
depends_on:
  - "@specs/aws/cognito-identity/meta"
---

# RoleMapping

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cognito-identity/docs/API_RoleMapping
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RoleMapping
<a name="API_RoleMapping"></a>

A role mapping.

## Contents
<a name="API_RoleMapping_Contents"></a>

 ** Type **   <a name="CognitoIdentity-Type-RoleMapping-Type"></a>
The role mapping type. Token will use `cognito:roles` and `cognito:preferred_role` claims from the Cognito identity provider token to map groups to roles. Rules will attempt to match claims from the token to map to a role.  
Type: String  
Valid Values: `Token | Rules`   
Required: Yes

 ** AmbiguousRoleResolution **   <a name="CognitoIdentity-Type-RoleMapping-AmbiguousRoleResolution"></a>
If you specify Token or Rules as the `Type`, `AmbiguousRoleResolution` is required.  
Specifies the action to be taken if either no rules match the claim value for the `Rules` type, or there is no `cognito:preferred_role` claim and there are multiple `cognito:roles` matches for the `Token` type.  
Type: String  
Valid Values: `AuthenticatedRole | Deny`   
Required: No

 ** RulesConfiguration **   <a name="CognitoIdentity-Type-RoleMapping-RulesConfiguration"></a>
The rules to be used for mapping users to roles.  
If you specify Rules as the role mapping type, `RulesConfiguration` is required.  
Type: [RulesConfigurationType](API_RulesConfigurationType.md) object  
Required: No

## See Also
<a name="API_RoleMapping_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-identity-2014-06-30/RoleMapping) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-identity-2014-06-30/RoleMapping) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-identity-2014-06-30/RoleMapping) 