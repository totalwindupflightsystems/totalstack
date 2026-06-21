---
id: "@specs/aws/shield/docs/API_DescribeProtectionGroup"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeProtectionGroup"
status: active
depends_on:
  - "@specs/aws/shield/meta"
---

# DescribeProtectionGroup

> **source:** AWS Documentation
> **spec:id:** @specs/aws/shield/docs/API_DescribeProtectionGroup
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeProtectionGroup
<a name="API_DescribeProtectionGroup"></a>

Returns the specification for the specified protection group.

## Request Syntax
<a name="API_DescribeProtectionGroup_RequestSyntax"></a>

```
{
   "ProtectionGroupId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeProtectionGroup_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ProtectionGroupId](#API_DescribeProtectionGroup_RequestSyntax) **   <a name="AWSShield-DescribeProtectionGroup-request-ProtectionGroupId"></a>
The name of the protection group. You use this to identify the protection group in lists and to manage the protection group, for example to update, delete, or describe it.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 36.  
Pattern: `[a-zA-Z0-9\\-]*`   
Required: Yes

## Response Syntax
<a name="API_DescribeProtectionGroup_ResponseSyntax"></a>

```
{
   "ProtectionGroup": { 
      "Aggregation": "string",
      "Members": [ "string" ],
      "Pattern": "string",
      "ProtectionGroupArn": "string",
      "ProtectionGroupId": "string",
      "ResourceType": "string"
   }
}
```

## Response Elements
<a name="API_DescribeProtectionGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ProtectionGroup](#API_DescribeProtectionGroup_ResponseSyntax) **   <a name="AWSShield-DescribeProtectionGroup-response-ProtectionGroup"></a>
A grouping of protected resources that you and AWS Shield Advanced can monitor as a collective. This resource grouping improves the accuracy of detection and reduces false positives.   
Type: [ProtectionGroup](API_ProtectionGroup.md) object

## Errors
<a name="API_DescribeProtectionGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalErrorException **   
Exception that indicates that a problem occurred with the service infrastructure. You can retry the request.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
Exception indicating the specified resource does not exist. If available, this exception includes details in additional properties.     
 ** resourceType **   
Type of resource.
HTTP Status Code: 400

## See Also
<a name="API_DescribeProtectionGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/shield-2016-06-02/DescribeProtectionGroup) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/shield-2016-06-02/DescribeProtectionGroup) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/shield-2016-06-02/DescribeProtectionGroup) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/shield-2016-06-02/DescribeProtectionGroup) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/shield-2016-06-02/DescribeProtectionGroup) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/shield-2016-06-02/DescribeProtectionGroup) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/shield-2016-06-02/DescribeProtectionGroup) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/shield-2016-06-02/DescribeProtectionGroup) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/shield-2016-06-02/DescribeProtectionGroup) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/shield-2016-06-02/DescribeProtectionGroup) 