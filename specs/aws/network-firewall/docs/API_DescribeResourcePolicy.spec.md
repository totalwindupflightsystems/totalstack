---
id: "@specs/aws/network-firewall/docs/API_DescribeResourcePolicy"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeResourcePolicy"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# DescribeResourcePolicy

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_DescribeResourcePolicy
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeResourcePolicy
<a name="API_DescribeResourcePolicy"></a>

Retrieves a resource policy that you created in a [PutResourcePolicy](API_PutResourcePolicy.md) request. 

## Request Syntax
<a name="API_DescribeResourcePolicy_RequestSyntax"></a>

```
{
   "ResourceArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeResourcePolicy_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ResourceArn](#API_DescribeResourcePolicy_RequestSyntax) **   <a name="networkfirewall-DescribeResourcePolicy-request-ResourceArn"></a>
The Amazon Resource Name (ARN) of the rule group or firewall policy whose resource policy you want to retrieve.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^arn:aws.*`   
Required: Yes

## Response Syntax
<a name="API_DescribeResourcePolicy_ResponseSyntax"></a>

```
{
   "Policy": "string"
}
```

## Response Elements
<a name="API_DescribeResourcePolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Policy](#API_DescribeResourcePolicy_ResponseSyntax) **   <a name="networkfirewall-DescribeResourcePolicy-response-Policy"></a>
The IAM policy for the resource.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 395000.  
Pattern: `.*\S.*` 

## Errors
<a name="API_DescribeResourcePolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **   
Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request.   
HTTP Status Code: 500

 ** InvalidRequestException **   
The operation failed because of a problem with your request. Examples include:   
+ You specified an unsupported parameter name or value.
+ You tried to update a property with a value that isn't among the available types.
+ Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.
HTTP Status Code: 400

 ** ResourceNotFoundException **   
Unable to locate a resource using the parameters that you provided.  
HTTP Status Code: 400

 ** ThrottlingException **   
Unable to process the request due to throttling limitations.  
HTTP Status Code: 400

## See Also
<a name="API_DescribeResourcePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/network-firewall-2020-11-12/DescribeResourcePolicy) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/network-firewall-2020-11-12/DescribeResourcePolicy) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/DescribeResourcePolicy) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/network-firewall-2020-11-12/DescribeResourcePolicy) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/DescribeResourcePolicy) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/network-firewall-2020-11-12/DescribeResourcePolicy) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/network-firewall-2020-11-12/DescribeResourcePolicy) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/network-firewall-2020-11-12/DescribeResourcePolicy) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/network-firewall-2020-11-12/DescribeResourcePolicy) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/DescribeResourcePolicy) 