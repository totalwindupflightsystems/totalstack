---
id: "@specs/aws/quicksight/docs/API_DescribeIpRestriction"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeIpRestriction"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# DescribeIpRestriction

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_DescribeIpRestriction
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeIpRestriction
<a name="API_DescribeIpRestriction"></a>

Provides a summary and status of IP rules.

## Request Syntax
<a name="API_DescribeIpRestriction_RequestSyntax"></a>

```
GET /accounts/{{AwsAccountId}}/ip-restriction HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeIpRestriction_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_DescribeIpRestriction_RequestSyntax) **   <a name="QS-DescribeIpRestriction-request-uri-AwsAccountId"></a>
The ID of the AWS account that contains the IP rules.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

## Request Body
<a name="API_DescribeIpRestriction_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeIpRestriction_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "AwsAccountId": "string",
   "Enabled": boolean,
   "IpRestrictionRuleMap": { 
      "string" : "string" 
   },
   "RequestId": "string",
   "VpcEndpointIdRestrictionRuleMap": { 
      "string" : "string" 
   },
   "VpcIdRestrictionRuleMap": { 
      "string" : "string" 
   }
}
```

## Response Elements
<a name="API_DescribeIpRestriction_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_DescribeIpRestriction_ResponseSyntax) **   <a name="QS-DescribeIpRestriction-response-Status"></a>
The HTTP status of the request. 

The following data is returned in JSON format by the service.

 ** [AwsAccountId](#API_DescribeIpRestriction_ResponseSyntax) **   <a name="QS-DescribeIpRestriction-response-AwsAccountId"></a>
The ID of the AWS account that contains the IP rules.  
Type: String  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$` 

 ** [Enabled](#API_DescribeIpRestriction_ResponseSyntax) **   <a name="QS-DescribeIpRestriction-response-Enabled"></a>
A value that specifies whether IP rules are turned on.  
Type: Boolean

 ** [IpRestrictionRuleMap](#API_DescribeIpRestriction_ResponseSyntax) **   <a name="QS-DescribeIpRestriction-response-IpRestrictionRuleMap"></a>
A map that describes the IP rules with CIDR range and description.  
Type: String to string map  
Key Pattern: `^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\/(3[0-2]|[1-2][0-9]|[1-9]))$`   
Value Length Constraints: Minimum length of 0. Maximum length of 150.

 ** [RequestId](#API_DescribeIpRestriction_ResponseSyntax) **   <a name="QS-DescribeIpRestriction-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

 ** [VpcEndpointIdRestrictionRuleMap](#API_DescribeIpRestriction_ResponseSyntax) **   <a name="QS-DescribeIpRestriction-response-VpcEndpointIdRestrictionRuleMap"></a>
A map of allowed VPC endpoint IDs and their rule descriptions.  
Type: String to string map  
Key Length Constraints: Minimum length of 1. Maximum length of 255.  
Key Pattern: `^vpce-[0-9a-z]*$`   
Value Length Constraints: Minimum length of 0. Maximum length of 150.

 ** [VpcIdRestrictionRuleMap](#API_DescribeIpRestriction_ResponseSyntax) **   <a name="QS-DescribeIpRestriction-response-VpcIdRestrictionRuleMap"></a>
A map of allowed VPC IDs and their rule descriptions.  
Type: String to string map  
Key Length Constraints: Minimum length of 1. Maximum length of 255.  
Key Pattern: `^vpc-[0-9a-z]*$`   
Value Length Constraints: Minimum length of 0. Maximum length of 150.

## Errors
<a name="API_DescribeIpRestriction_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
You don't have access to this item. The provided credentials couldn't be validated. You might not be authorized to carry out the request. Make sure that your account is authorized to use the Amazon Quick Sight service, that your policies have the correct permissions, and that you are using the correct credentials.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 401

 ** InternalFailureException **   
An internal failure occurred.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 500

 ** InvalidParameterValueException **   
One or more parameters has a value that isn't valid.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 400

 ** ResourceNotFoundException **   
One or more resources can't be found.    
 ** RequestId **   
The AWS request ID for this request.  
 ** ResourceType **   
The resource type for this request.
HTTP Status Code: 404

 ** ThrottlingException **   
Access is throttled.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 429

## See Also
<a name="API_DescribeIpRestriction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/DescribeIpRestriction) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/DescribeIpRestriction) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DescribeIpRestriction) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/DescribeIpRestriction) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DescribeIpRestriction) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/DescribeIpRestriction) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/DescribeIpRestriction) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/DescribeIpRestriction) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/DescribeIpRestriction) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DescribeIpRestriction) 