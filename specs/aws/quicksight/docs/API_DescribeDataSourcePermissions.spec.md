---
id: "@specs/aws/quicksight/docs/API_DescribeDataSourcePermissions"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeDataSourcePermissions"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# DescribeDataSourcePermissions

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_DescribeDataSourcePermissions
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeDataSourcePermissions
<a name="API_DescribeDataSourcePermissions"></a>

Describes the resource permissions for a data source.

## Request Syntax
<a name="API_DescribeDataSourcePermissions_RequestSyntax"></a>

```
GET /accounts/{{AwsAccountId}}/data-sources/{{DataSourceId}}/permissions HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeDataSourcePermissions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_DescribeDataSourcePermissions_RequestSyntax) **   <a name="QS-DescribeDataSourcePermissions-request-uri-AwsAccountId"></a>
The AWS account ID.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

 ** [DataSourceId](#API_DescribeDataSourcePermissions_RequestSyntax) **   <a name="QS-DescribeDataSourcePermissions-request-uri-DataSourceId"></a>
The ID of the data source. This ID is unique per AWS Region for each AWS account.  
Required: Yes

## Request Body
<a name="API_DescribeDataSourcePermissions_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeDataSourcePermissions_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "DataSourceArn": "string",
   "DataSourceId": "string",
   "Permissions": [ 
      { 
         "Actions": [ "string" ],
         "Principal": "string"
      }
   ],
   "RequestId": "string"
}
```

## Response Elements
<a name="API_DescribeDataSourcePermissions_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_DescribeDataSourcePermissions_ResponseSyntax) **   <a name="QS-DescribeDataSourcePermissions-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [DataSourceArn](#API_DescribeDataSourcePermissions_ResponseSyntax) **   <a name="QS-DescribeDataSourcePermissions-response-DataSourceArn"></a>
The Amazon Resource Name (ARN) of the data source.  
Type: String

 ** [DataSourceId](#API_DescribeDataSourcePermissions_ResponseSyntax) **   <a name="QS-DescribeDataSourcePermissions-response-DataSourceId"></a>
The ID of the data source. This ID is unique per AWS Region for each AWS account.  
Type: String

 ** [Permissions](#API_DescribeDataSourcePermissions_ResponseSyntax) **   <a name="QS-DescribeDataSourcePermissions-response-Permissions"></a>
A list of resource permissions on the data source.  
Type: Array of [ResourcePermission](API_ResourcePermission.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 64 items.

 ** [RequestId](#API_DescribeDataSourcePermissions_ResponseSyntax) **   <a name="QS-DescribeDataSourcePermissions-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

## Errors
<a name="API_DescribeDataSourcePermissions_Errors"></a>

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

## Examples
<a name="API_DescribeDataSourcePermissions_Examples"></a>

### Example
<a name="API_DescribeDataSourcePermissions_Example_1"></a>

This example illustrates one usage of DescribeDataSourcePermissions.

#### Sample Request
<a name="API_DescribeDataSourcePermissions_Example_1_Request"></a>

```
GET /accounts/{AwsAccountId}/data-sources/{DataSourceId}/permissions HTTP/1.1
Content-type: application/json
```

## See Also
<a name="API_DescribeDataSourcePermissions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/DescribeDataSourcePermissions) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/DescribeDataSourcePermissions) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DescribeDataSourcePermissions) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/DescribeDataSourcePermissions) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DescribeDataSourcePermissions) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/DescribeDataSourcePermissions) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/DescribeDataSourcePermissions) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/DescribeDataSourcePermissions) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/DescribeDataSourcePermissions) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DescribeDataSourcePermissions) 