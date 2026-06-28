---
id: "@specs/aws/quicksight/docs/API_DescribeBrandAssignment"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeBrandAssignment"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# DescribeBrandAssignment

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_DescribeBrandAssignment
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeBrandAssignment
<a name="API_DescribeBrandAssignment"></a>

Describes a brand assignment.

## Request Syntax
<a name="API_DescribeBrandAssignment_RequestSyntax"></a>

```
GET /accounts/{{AwsAccountId}}/brandassignments HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeBrandAssignment_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_DescribeBrandAssignment_RequestSyntax) **   <a name="QS-DescribeBrandAssignment-request-uri-AwsAccountId"></a>
The ID of the AWS account that owns the brand assignment.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

## Request Body
<a name="API_DescribeBrandAssignment_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeBrandAssignment_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "BrandArn": "string",
   "RequestId": "string"
}
```

## Response Elements
<a name="API_DescribeBrandAssignment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [BrandArn](#API_DescribeBrandAssignment_ResponseSyntax) **   <a name="QS-DescribeBrandAssignment-response-BrandArn"></a>
The Amazon Resource Name (ARN) of the brand.  
Type: String

 ** [RequestId](#API_DescribeBrandAssignment_ResponseSyntax) **   <a name="QS-DescribeBrandAssignment-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

## Errors
<a name="API_DescribeBrandAssignment_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
You don't have access to this item. The provided credentials couldn't be validated. You might not be authorized to carry out the request. Make sure that your account is authorized to use the Amazon Quick Sight service, that your policies have the correct permissions, and that you are using the correct credentials.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 401

 ** ConflictException **   
Updating or deleting a resource can cause an inconsistent state.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 409

 ** InternalServerException **   
An internal service exception.  
HTTP Status Code: 500

 ** InvalidRequestException **   
You don't have this feature activated for your account. To fix this issue, contact AWS support.    
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
<a name="API_DescribeBrandAssignment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/DescribeBrandAssignment) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/DescribeBrandAssignment) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DescribeBrandAssignment) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/DescribeBrandAssignment) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DescribeBrandAssignment) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/DescribeBrandAssignment) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/DescribeBrandAssignment) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/DescribeBrandAssignment) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/DescribeBrandAssignment) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DescribeBrandAssignment) 