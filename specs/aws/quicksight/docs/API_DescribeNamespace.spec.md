---
id: "@specs/aws/quicksight/docs/API_DescribeNamespace"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeNamespace"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# DescribeNamespace

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_DescribeNamespace
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeNamespace
<a name="API_DescribeNamespace"></a>

Describes the current namespace.

## Request Syntax
<a name="API_DescribeNamespace_RequestSyntax"></a>

```
GET /accounts/{{AwsAccountId}}/namespaces/{{Namespace}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeNamespace_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_DescribeNamespace_RequestSyntax) **   <a name="QS-DescribeNamespace-request-uri-AwsAccountId"></a>
The ID for the AWS account that contains the Quick Sight namespace that you want to describe.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

 ** [Namespace](#API_DescribeNamespace_RequestSyntax) **   <a name="QS-DescribeNamespace-request-uri-Namespace"></a>
The namespace that you want to describe.  
Length Constraints: Maximum length of 64.  
Pattern: `^[a-zA-Z0-9._-]*$`   
Required: Yes

## Request Body
<a name="API_DescribeNamespace_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeNamespace_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "Namespace": { 
      "Arn": "string",
      "CapacityRegion": "string",
      "CreationStatus": "string",
      "IamIdentityCenterApplicationArn": "string",
      "IamIdentityCenterInstanceArn": "string",
      "IdentityStore": "string",
      "Name": "string",
      "NamespaceError": { 
         "Message": "string",
         "Type": "string"
      }
   },
   "RequestId": "string"
}
```

## Response Elements
<a name="API_DescribeNamespace_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_DescribeNamespace_ResponseSyntax) **   <a name="QS-DescribeNamespace-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [Namespace](#API_DescribeNamespace_ResponseSyntax) **   <a name="QS-DescribeNamespace-response-Namespace"></a>
The information about the namespace that you're describing. The response includes the namespace ARN, name, AWS Region, creation status, and identity store. `DescribeNamespace` also works for namespaces that are in the process of being created. For incomplete namespaces, this API operation lists the namespace error types and messages associated with the creation process.  
Type: [NamespaceInfoV2](API_NamespaceInfoV2.md) object

 ** [RequestId](#API_DescribeNamespace_ResponseSyntax) **   <a name="QS-DescribeNamespace-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

## Errors
<a name="API_DescribeNamespace_Errors"></a>

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
<a name="API_DescribeNamespace_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/DescribeNamespace) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/DescribeNamespace) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DescribeNamespace) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/DescribeNamespace) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DescribeNamespace) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/DescribeNamespace) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/DescribeNamespace) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/DescribeNamespace) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/DescribeNamespace) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DescribeNamespace) 