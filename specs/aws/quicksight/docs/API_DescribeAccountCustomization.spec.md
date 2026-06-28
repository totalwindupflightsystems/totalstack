---
id: "@specs/aws/quicksight/docs/API_DescribeAccountCustomization"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeAccountCustomization"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# DescribeAccountCustomization

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_DescribeAccountCustomization
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeAccountCustomization
<a name="API_DescribeAccountCustomization"></a>

Describes the customizations associated with the provided AWS account and Amazon Quick Sight namespace. The Quick Sight console evaluates which customizations to apply by running this API operation with the `Resolved` flag included. 

To determine what customizations display when you run this command, it can help to visualize the relationship of the entities involved. 
+  ` AWS account` - The AWS account exists at the top of the hierarchy. It has the potential to use all of the AWS Regions and AWS Services. When you subscribe to Quick Sight, you choose one AWS Region to use as your home Region. That's where your free SPICE capacity is located. You can use Quick Sight in any supported AWS Region. 
+  ` AWS Region ` - You can sign in to Quick Sight in any AWS Region. If you have a user directory, it resides in us-east-1, which is US East (N. Virginia). Generally speaking, these users have access to Quick Sight in any AWS Region, unless they are constrained to a namespace. 

  To run the command in a different AWS Region, you change your Region settings. If you're using the AWS CLI, you can use one of the following options:
  + Use [command line options](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-options.html). 
  + Use [named profiles](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html). 
  + Run `aws configure` to change your default AWS Region. Use Enter to key the same settings for your keys. For more information, see [Configuring the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html).
+  `Namespace` - A Quick Sight namespace is a partition that contains users and assets (data sources, datasets, dashboards, and so on). To access assets that are in a specific namespace, users and groups must also be part of the same namespace. People who share a namespace are completely isolated from users and assets in other namespaces, even if they are in the same AWS account and AWS Region.
+  `Applied customizations` - Quick Sight customizations can apply to an AWS account or to a namespace. Settings that you apply to a namespace override settings that you apply to an AWS account.

## Request Syntax
<a name="API_DescribeAccountCustomization_RequestSyntax"></a>

```
GET /accounts/{{AwsAccountId}}/customizations?namespace={{Namespace}}&resolved={{Resolved}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeAccountCustomization_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_DescribeAccountCustomization_RequestSyntax) **   <a name="QS-DescribeAccountCustomization-request-uri-AwsAccountId"></a>
The ID for the AWS account that you want to describe Quick Sight customizations for.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

 ** [Namespace](#API_DescribeAccountCustomization_RequestSyntax) **   <a name="QS-DescribeAccountCustomization-request-uri-Namespace"></a>
The Quick Sight namespace that you want to describe Quick Sight customizations for.  
Length Constraints: Maximum length of 64.  
Pattern: `^[a-zA-Z0-9._-]*$` 

 ** [Resolved](#API_DescribeAccountCustomization_RequestSyntax) **   <a name="QS-DescribeAccountCustomization-request-uri-Resolved"></a>
The `Resolved` flag works with the other parameters to determine which view of Quick Sight customizations is returned. You can add this flag to your command to use the same view that Quick Sight uses to identify which customizations to apply to the console. Omit this flag, or set it to `no-resolved`, to reveal customizations that are configured at different levels. 

## Request Body
<a name="API_DescribeAccountCustomization_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeAccountCustomization_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "AccountCustomization": { 
      "DefaultEmailCustomizationTemplate": "string",
      "DefaultTheme": "string"
   },
   "Arn": "string",
   "AwsAccountId": "string",
   "Namespace": "string",
   "RequestId": "string"
}
```

## Response Elements
<a name="API_DescribeAccountCustomization_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_DescribeAccountCustomization_ResponseSyntax) **   <a name="QS-DescribeAccountCustomization-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [AccountCustomization](#API_DescribeAccountCustomization_ResponseSyntax) **   <a name="QS-DescribeAccountCustomization-response-AccountCustomization"></a>
The Quick Sight customizations that exist.   
Type: [AccountCustomization](API_AccountCustomization.md) object

 ** [Arn](#API_DescribeAccountCustomization_ResponseSyntax) **   <a name="QS-DescribeAccountCustomization-response-Arn"></a>
The Amazon Resource Name (ARN) of the customization that's associated with this AWS account.  
Type: String

 ** [AwsAccountId](#API_DescribeAccountCustomization_ResponseSyntax) **   <a name="QS-DescribeAccountCustomization-response-AwsAccountId"></a>
The ID for the AWS account that you're describing.  
Type: String  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$` 

 ** [Namespace](#API_DescribeAccountCustomization_ResponseSyntax) **   <a name="QS-DescribeAccountCustomization-response-Namespace"></a>
The Quick Sight namespace that you're describing.   
Type: String  
Length Constraints: Maximum length of 64.  
Pattern: `^[a-zA-Z0-9._-]*$` 

 ** [RequestId](#API_DescribeAccountCustomization_ResponseSyntax) **   <a name="QS-DescribeAccountCustomization-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

## Errors
<a name="API_DescribeAccountCustomization_Errors"></a>

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

 ** ResourceUnavailableException **   
This resource is currently unavailable.    
 ** RequestId **   
The AWS request ID for this request.  
 ** ResourceType **   
The resource type for this request.
HTTP Status Code: 503

 ** ThrottlingException **   
Access is throttled.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 429

## See Also
<a name="API_DescribeAccountCustomization_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/DescribeAccountCustomization) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/DescribeAccountCustomization) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DescribeAccountCustomization) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/DescribeAccountCustomization) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DescribeAccountCustomization) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/DescribeAccountCustomization) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/DescribeAccountCustomization) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/DescribeAccountCustomization) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/DescribeAccountCustomization) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DescribeAccountCustomization) 