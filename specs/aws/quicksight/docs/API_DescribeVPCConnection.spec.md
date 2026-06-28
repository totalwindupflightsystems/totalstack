---
id: "@specs/aws/quicksight/docs/API_DescribeVPCConnection"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeVPCConnection"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# DescribeVPCConnection

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_DescribeVPCConnection
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeVPCConnection
<a name="API_DescribeVPCConnection"></a>

Describes a VPC connection.

## Request Syntax
<a name="API_DescribeVPCConnection_RequestSyntax"></a>

```
GET /accounts/{{AwsAccountId}}/vpc-connections/{{VPCConnectionId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeVPCConnection_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_DescribeVPCConnection_RequestSyntax) **   <a name="QS-DescribeVPCConnection-request-uri-AwsAccountId"></a>
The AWS account ID of the account that contains the VPC connection that you want described.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

 ** [VPCConnectionId](#API_DescribeVPCConnection_RequestSyntax) **   <a name="QS-DescribeVPCConnection-request-uri-VPCConnectionId"></a>
The ID of the VPC connection that you're creating. This ID is a unique identifier for each AWS Region in an AWS account.  
Length Constraints: Minimum length of 1. Maximum length of 1000.  
Required: Yes

## Request Body
<a name="API_DescribeVPCConnection_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeVPCConnection_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "RequestId": "string",
   "Status": number,
   "VPCConnection": { 
      "Arn": "string",
      "AvailabilityStatus": "string",
      "CreatedTime": number,
      "DnsResolvers": [ "string" ],
      "LastUpdatedTime": number,
      "Name": "string",
      "NetworkInterfaces": [ 
         { 
            "AvailabilityZone": "string",
            "ErrorMessage": "string",
            "NetworkInterfaceId": "string",
            "Status": "string",
            "SubnetId": "string"
         }
      ],
      "RoleArn": "string",
      "SecurityGroupIds": [ "string" ],
      "Status": "string",
      "VPCConnectionId": "string",
      "VPCId": "string"
   }
}
```

## Response Elements
<a name="API_DescribeVPCConnection_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [RequestId](#API_DescribeVPCConnection_ResponseSyntax) **   <a name="QS-DescribeVPCConnection-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

 ** [Status](#API_DescribeVPCConnection_ResponseSyntax) **   <a name="QS-DescribeVPCConnection-response-Status"></a>
The HTTP status of the request.  
Type: Integer

 ** [VPCConnection](#API_DescribeVPCConnection_ResponseSyntax) **   <a name="QS-DescribeVPCConnection-response-VPCConnection"></a>
A response object that provides information for the specified VPC connection.  
Type: [VPCConnection](API_VPCConnection.md) object

## Errors
<a name="API_DescribeVPCConnection_Errors"></a>

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

 ** UnsupportedUserEditionException **   
This error indicates that you are calling an operation on an Amazon Quick Suite subscription where the edition doesn't include support for that operation. Amazon Quick Suite currently has Standard Edition and Enterprise Edition. Not every operation and capability is available in every edition.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 403

## See Also
<a name="API_DescribeVPCConnection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/DescribeVPCConnection) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/DescribeVPCConnection) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DescribeVPCConnection) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/DescribeVPCConnection) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DescribeVPCConnection) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/DescribeVPCConnection) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/DescribeVPCConnection) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/DescribeVPCConnection) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/DescribeVPCConnection) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DescribeVPCConnection) 