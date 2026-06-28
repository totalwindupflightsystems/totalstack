---
id: "@specs/aws/quicksight/docs/API_DescribeDashboardPermissions"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeDashboardPermissions"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# DescribeDashboardPermissions

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_DescribeDashboardPermissions
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeDashboardPermissions
<a name="API_DescribeDashboardPermissions"></a>

Describes read and write permissions for a dashboard.

## Request Syntax
<a name="API_DescribeDashboardPermissions_RequestSyntax"></a>

```
GET /accounts/{{AwsAccountId}}/dashboards/{{DashboardId}}/permissions HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeDashboardPermissions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_DescribeDashboardPermissions_RequestSyntax) **   <a name="QS-DescribeDashboardPermissions-request-uri-AwsAccountId"></a>
The ID of the AWS account that contains the dashboard that you're describing permissions for.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

 ** [DashboardId](#API_DescribeDashboardPermissions_RequestSyntax) **   <a name="QS-DescribeDashboardPermissions-request-uri-DashboardId"></a>
The ID for the dashboard, also added to the IAM policy.  
Length Constraints: Minimum length of 1. Maximum length of 512.  
Pattern: `[\w\-]+`   
Required: Yes

## Request Body
<a name="API_DescribeDashboardPermissions_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeDashboardPermissions_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "DashboardArn": "string",
   "DashboardId": "string",
   "LinkSharingConfiguration": { 
      "Permissions": [ 
         { 
            "Actions": [ "string" ],
            "Principal": "string"
         }
      ]
   },
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
<a name="API_DescribeDashboardPermissions_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_DescribeDashboardPermissions_ResponseSyntax) **   <a name="QS-DescribeDashboardPermissions-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [DashboardArn](#API_DescribeDashboardPermissions_ResponseSyntax) **   <a name="QS-DescribeDashboardPermissions-response-DashboardArn"></a>
The Amazon Resource Name (ARN) of the dashboard.  
Type: String

 ** [DashboardId](#API_DescribeDashboardPermissions_ResponseSyntax) **   <a name="QS-DescribeDashboardPermissions-response-DashboardId"></a>
The ID for the dashboard.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 512.  
Pattern: `[\w\-]+` 

 ** [LinkSharingConfiguration](#API_DescribeDashboardPermissions_ResponseSyntax) **   <a name="QS-DescribeDashboardPermissions-response-LinkSharingConfiguration"></a>
A structure that contains the configuration of a shareable link that grants access to the dashboard. Your users can use the link to view and interact with the dashboard, if the dashboard has been shared with them. For more information about sharing dashboards, see [Sharing Dashboards](https://docs.aws.amazon.com/quicksight/latest/user/sharing-a-dashboard.html).  
Type: [LinkSharingConfiguration](API_LinkSharingConfiguration.md) object

 ** [Permissions](#API_DescribeDashboardPermissions_ResponseSyntax) **   <a name="QS-DescribeDashboardPermissions-response-Permissions"></a>
A structure that contains the permissions for the dashboard.  
Type: Array of [ResourcePermission](API_ResourcePermission.md) objects  
Array Members: Maximum number of 100 items.

 ** [RequestId](#API_DescribeDashboardPermissions_ResponseSyntax) **   <a name="QS-DescribeDashboardPermissions-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

## Errors
<a name="API_DescribeDashboardPermissions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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
<a name="API_DescribeDashboardPermissions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/DescribeDashboardPermissions) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/DescribeDashboardPermissions) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DescribeDashboardPermissions) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/DescribeDashboardPermissions) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DescribeDashboardPermissions) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/DescribeDashboardPermissions) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/DescribeDashboardPermissions) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/DescribeDashboardPermissions) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/DescribeDashboardPermissions) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DescribeDashboardPermissions) 