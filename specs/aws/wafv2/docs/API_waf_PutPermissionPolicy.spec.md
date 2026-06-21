---
id: "@specs/aws/wafv2/docs/API_waf_PutPermissionPolicy"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS PutPermissionPolicy"
status: active
depends_on:
  - "@specs/aws/wafv2/meta"
---

# PutPermissionPolicy

> **source:** AWS Documentation
> **spec:id:** @specs/aws/wafv2/docs/API_waf_PutPermissionPolicy
> **target_lang:** meta — documentation tier. ALL sections preserved.



# PutPermissionPolicy
<a name="API_waf_PutPermissionPolicy"></a>

**Note**  
 AWS WAF Classic support will end on September 30, 2025.   
This is ** AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.  
 **For the latest version of AWS WAF **, use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). With the latest version, AWS WAF has a single set of endpoints for regional and global use. 

Attaches an IAM policy to the specified resource. The only supported use for this action is to share a RuleGroup across accounts.

The `PutPermissionPolicy` is subject to the following restrictions:
+ You can attach only one policy with each `PutPermissionPolicy` request.
+ The policy must include an `Effect`, `Action` and `Principal`. 
+  `Effect` must specify `Allow`.
+ The `Action` in the policy must be `waf:UpdateWebACL`, `waf-regional:UpdateWebACL`, `waf:GetRuleGroup` and `waf-regional:GetRuleGroup` . Any extra or wildcard actions in the policy will be rejected.
+ The policy cannot include a `Resource` parameter.
+ The ARN in the request must be a valid RuleGroup ARN and the RuleGroup must exist in the same region.
+ The user making the request must be the owner of the RuleGroup.
+ Your policy must be composed using IAM Policy version 2012-10-17.

For more information, see [Policies and permissions in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html). 

An example of a valid policy parameter is shown in the Examples section below.

## Request Syntax
<a name="API_waf_PutPermissionPolicy_RequestSyntax"></a>

```
{
   "Policy": "{{string}}",
   "ResourceArn": "{{string}}"
}
```

## Request Parameters
<a name="API_waf_PutPermissionPolicy_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Policy](#API_waf_PutPermissionPolicy_RequestSyntax) **   <a name="WAF-waf_PutPermissionPolicy-request-Policy"></a>
The policy to attach to the specified RuleGroup.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 395000.  
Pattern: `.*\S.*`   
Required: Yes

 ** [ResourceArn](#API_waf_PutPermissionPolicy_RequestSyntax) **   <a name="WAF-waf_PutPermissionPolicy-request-ResourceArn"></a>
The Amazon Resource Name (ARN) of the RuleGroup to which you want to attach the policy.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1224.  
Pattern: `.*\S.*`   
Required: Yes

## Response Elements
<a name="API_waf_PutPermissionPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_waf_PutPermissionPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** WAFInternalErrorException **   
The operation failed because of a system problem, even though the request was valid. Retry your request.  
HTTP Status Code: 500

 ** WAFInvalidPermissionPolicyException **   
The operation failed because the specified policy is not in the proper format.   
The policy is subject to the following restrictions:  
+ You can attach only one policy with each `PutPermissionPolicy` request.
+ The policy must include an `Effect`, `Action` and `Principal`. 
+  `Effect` must specify `Allow`.
+ The `Action` in the policy must be `waf:UpdateWebACL`, `waf-regional:UpdateWebACL`, `waf:GetRuleGroup` and `waf-regional:GetRuleGroup` . Any extra or wildcard actions in the policy will be rejected.
+ The policy cannot include a `Resource` parameter.
+ The ARN in the request must be a valid WAF RuleGroup ARN and the RuleGroup must exist in the same region.
+ The user making the request must be the owner of the RuleGroup.
+ Your policy must be composed using IAM Policy version 2012-10-17.
HTTP Status Code: 400

 ** WAFNonexistentItemException **   
The operation failed because the referenced object doesn't exist.  
HTTP Status Code: 400

 ** WAFStaleDataException **   
The operation failed because you tried to create, update, or delete an object by using a change token that has already been used.  
HTTP Status Code: 400

## Examples
<a name="API_waf_PutPermissionPolicy_Examples"></a>

### Example policy parameter - No escape characters
<a name="API_waf_PutPermissionPolicy_Example_1"></a>

This example illustrates one usage of PutPermissionPolicy.

```
{
   "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
          "Effect": "Allow",
          "Principal": {
          "AWS": "arn:aws:iam::111111111111:user/MyUserName"
                       },
           "Action": [
               "waf:UpdateWebACL",
               "waf-regional:UpdateWebACL",
               "waf:GetRuleGroup",
               "waf-regional:GetRuleGroup"

                     ]
         }
                  ]
}
```

### Example policy parameter - ()
<a name="API_waf_PutPermissionPolicy_Example_2"></a>

This example illustrates one usage of PutPermissionPolicy.

```
{\"Version\":\"2012-10-17\",		 	 	 \"Statement\":[{\"Effect\":\"Allow\",\"Principal\":{\"AWS\":\"arn:aws:iam::111111111111:user\/MyUserName\"},\"Action\":[\"waf:UpdateWebACL\",\"waf-regional:UpdateWebACL\",\"waf:GetRuleGroup\",\"waf-regional:GetRuleGroup\"]}]}
```

## See Also
<a name="API_waf_PutPermissionPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/waf-2015-08-24/PutPermissionPolicy) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/waf-2015-08-24/PutPermissionPolicy) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waf-2015-08-24/PutPermissionPolicy) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/waf-2015-08-24/PutPermissionPolicy) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waf-2015-08-24/PutPermissionPolicy) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/waf-2015-08-24/PutPermissionPolicy) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/waf-2015-08-24/PutPermissionPolicy) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/waf-2015-08-24/PutPermissionPolicy) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/waf-2015-08-24/PutPermissionPolicy) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waf-2015-08-24/PutPermissionPolicy) 