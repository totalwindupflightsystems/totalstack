---
id: "@specs/aws/codepipeline/docs/API_ListRuleTypes"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListRuleTypes"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# ListRuleTypes

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_ListRuleTypes
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListRuleTypes
<a name="API_ListRuleTypes"></a>

Lists the rules for the condition. For more information about conditions, see [Stage conditions](https://docs.aws.amazon.com/codepipeline/latest/userguide/stage-conditions.html) and [How do stage conditions work?](https://docs.aws.amazon.com/codepipeline/latest/userguide/concepts-how-it-works-conditions.html).For more information about rules, see the [AWS CodePipeline rule reference](https://docs.aws.amazon.com/codepipeline/latest/userguide/rule-reference.html).

## Request Syntax
<a name="API_ListRuleTypes_RequestSyntax"></a>

```
{
   "regionFilter": "{{string}}",
   "ruleOwnerFilter": "{{string}}"
}
```

## Request Parameters
<a name="API_ListRuleTypes_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [regionFilter](#API_ListRuleTypes_RequestSyntax) **   <a name="CodePipeline-ListRuleTypes-request-regionFilter"></a>
The rule Region to filter on.  
Type: String  
Length Constraints: Minimum length of 4. Maximum length of 30.  
Required: No

 ** [ruleOwnerFilter](#API_ListRuleTypes_RequestSyntax) **   <a name="CodePipeline-ListRuleTypes-request-ruleOwnerFilter"></a>
The rule owner to filter on.  
Type: String  
Valid Values: `AWS`   
Required: No

## Response Syntax
<a name="API_ListRuleTypes_ResponseSyntax"></a>

```
{
   "ruleTypes": [ 
      { 
         "id": { 
            "category": "string",
            "owner": "string",
            "provider": "string",
            "version": "string"
         },
         "inputArtifactDetails": { 
            "maximumCount": number,
            "minimumCount": number
         },
         "ruleConfigurationProperties": [ 
            { 
               "description": "string",
               "key": boolean,
               "name": "string",
               "queryable": boolean,
               "required": boolean,
               "secret": boolean,
               "type": "string"
            }
         ],
         "settings": { 
            "entityUrlTemplate": "string",
            "executionUrlTemplate": "string",
            "revisionUrlTemplate": "string",
            "thirdPartyConfigurationUrl": "string"
         }
      }
   ]
}
```

## Response Elements
<a name="API_ListRuleTypes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ruleTypes](#API_ListRuleTypes_ResponseSyntax) **   <a name="CodePipeline-ListRuleTypes-response-ruleTypes"></a>
Lists the rules that are configured for the condition.  
Type: Array of [RuleType](API_RuleType.md) objects

## Errors
<a name="API_ListRuleTypes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidNextTokenException **   
The next token was specified in an invalid format. Make sure that the next token you provide is the token returned by a previous call.  
HTTP Status Code: 400

 ** ValidationException **   
The validation was specified in an invalid format.  
HTTP Status Code: 400

## See Also
<a name="API_ListRuleTypes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codepipeline-2015-07-09/ListRuleTypes) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codepipeline-2015-07-09/ListRuleTypes) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/ListRuleTypes) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codepipeline-2015-07-09/ListRuleTypes) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/ListRuleTypes) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codepipeline-2015-07-09/ListRuleTypes) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codepipeline-2015-07-09/ListRuleTypes) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codepipeline-2015-07-09/ListRuleTypes) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codepipeline-2015-07-09/ListRuleTypes) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/ListRuleTypes) 