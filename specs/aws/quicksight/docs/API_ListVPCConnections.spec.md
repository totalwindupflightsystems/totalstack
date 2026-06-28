---
id: "@specs/aws/quicksight/docs/API_ListVPCConnections"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListVPCConnections"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# ListVPCConnections

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_ListVPCConnections
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListVPCConnections
<a name="API_ListVPCConnections"></a>

Lists all of the VPC connections in the current set AWS Region of an AWS account.

## Request Syntax
<a name="API_ListVPCConnections_RequestSyntax"></a>

```
GET /accounts/{{AwsAccountId}}/vpc-connections?max-results={{MaxResults}}&next-token={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListVPCConnections_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_ListVPCConnections_RequestSyntax) **   <a name="QS-ListVPCConnections-request-uri-AwsAccountId"></a>
The AWS account ID of the account that contains the VPC connections that you want to list.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

 ** [MaxResults](#API_ListVPCConnections_RequestSyntax) **   <a name="QS-ListVPCConnections-request-uri-MaxResults"></a>
The maximum number of results to be returned per request.  
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_ListVPCConnections_RequestSyntax) **   <a name="QS-ListVPCConnections-request-uri-NextToken"></a>
The token for the next set of results, or null if there are no more results.

## Request Body
<a name="API_ListVPCConnections_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListVPCConnections_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "NextToken": "string",
   "RequestId": "string",
   "VPCConnectionSummaries": [ 
      { 
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
   ]
}
```

## Response Elements
<a name="API_ListVPCConnections_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_ListVPCConnections_ResponseSyntax) **   <a name="QS-ListVPCConnections-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListVPCConnections_ResponseSyntax) **   <a name="QS-ListVPCConnections-response-NextToken"></a>
The token for the next set of results, or null if there are no more results.  
Type: String

 ** [RequestId](#API_ListVPCConnections_ResponseSyntax) **   <a name="QS-ListVPCConnections-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

 ** [VPCConnectionSummaries](#API_ListVPCConnections_ResponseSyntax) **   <a name="QS-ListVPCConnections-response-VPCConnectionSummaries"></a>
A `VPCConnectionSummaries` object that returns a summary of VPC connection objects.  
Type: Array of [VPCConnectionSummary](API_VPCConnectionSummary.md) objects

## Errors
<a name="API_ListVPCConnections_Errors"></a>

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

 ** InvalidNextTokenException **   
The `NextToken` value isn't valid.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 400

 ** InvalidParameterValueException **   
One or more parameters has a value that isn't valid.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 400

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
<a name="API_ListVPCConnections_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/ListVPCConnections) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/ListVPCConnections) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ListVPCConnections) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/ListVPCConnections) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ListVPCConnections) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/ListVPCConnections) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/ListVPCConnections) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/ListVPCConnections) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/ListVPCConnections) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ListVPCConnections) 