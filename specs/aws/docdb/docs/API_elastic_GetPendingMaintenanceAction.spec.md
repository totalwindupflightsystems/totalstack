---
id: "@specs/aws/docdb/docs/API_elastic_GetPendingMaintenanceAction"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetPendingMaintenanceAction"
status: active
depends_on:
  - "@specs/aws/docdb/meta"
---

# GetPendingMaintenanceAction

> **source:** AWS Documentation
> **spec:id:** @specs/aws/docdb/docs/API_elastic_GetPendingMaintenanceAction
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetPendingMaintenanceAction
<a name="API_elastic_GetPendingMaintenanceAction"></a>

Retrieves all maintenance actions that are pending.

## Request Syntax
<a name="API_elastic_GetPendingMaintenanceAction_RequestSyntax"></a>

```
GET /pending-action/{{resourceArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_elastic_GetPendingMaintenanceAction_RequestParameters"></a>

The request uses the following URI parameters.

 ** [resourceArn](#API_elastic_GetPendingMaintenanceAction_RequestSyntax) **   <a name="documentdb-elastic_GetPendingMaintenanceAction-request-uri-resourceArn"></a>
Retrieves pending maintenance actions for a specific Amazon Resource Name (ARN).  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Required: Yes

## Request Body
<a name="API_elastic_GetPendingMaintenanceAction_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_elastic_GetPendingMaintenanceAction_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "resourcePendingMaintenanceAction": { 
      "pendingMaintenanceActionDetails": [ 
         { 
            "action": "string",
            "autoAppliedAfterDate": "string",
            "currentApplyDate": "string",
            "description": "string",
            "forcedApplyDate": "string",
            "optInStatus": "string"
         }
      ],
      "resourceArn": "string"
   }
}
```

## Response Elements
<a name="API_elastic_GetPendingMaintenanceAction_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [resourcePendingMaintenanceAction](#API_elastic_GetPendingMaintenanceAction_ResponseSyntax) **   <a name="documentdb-elastic_GetPendingMaintenanceAction-response-resourcePendingMaintenanceAction"></a>
Provides information about a pending maintenance action for a resource.  
Type: [ResourcePendingMaintenanceAction](API_elastic_ResourcePendingMaintenanceAction.md) object

## Errors
<a name="API_elastic_GetPendingMaintenanceAction_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
An exception that occurs when there are not sufficient permissions to perform an action.    
 ** message **   
An error message explaining why access was denied.
HTTP Status Code: 403

 ** ConflictException **   
There was an access conflict.    
 ** resourceId **   
The ID of the resource where there was an access conflict.  
 ** resourceType **   
The type of the resource where there was an access conflict.
HTTP Status Code: 409

 ** InternalServerException **   
There was an internal server error.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The specified resource could not be located.    
 ** message **   
An error message describing the failure.  
 ** resourceId **   
The ID of the resource that could not be located.  
 ** resourceType **   
The type of the resource that could not be found.
HTTP Status Code: 404

 ** ThrottlingException **   
ThrottlingException will be thrown when request was denied due to request throttling.    
 ** retryAfterSeconds **   
The number of seconds to wait before retrying the operation.
HTTP Status Code: 429

 ** ValidationException **   
A structure defining a validation exception.    
 ** fieldList **   
A list of the fields in which the validation exception occurred.  
 ** message **   
An error message describing the validation exception.  
 ** reason **   
The reason why the validation exception occurred (one of `unknownOperation`, `cannotParse`, `fieldValidationFailed`, or `other`).
HTTP Status Code: 400

## See Also
<a name="API_elastic_GetPendingMaintenanceAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/docdb-elastic-2022-11-28/GetPendingMaintenanceAction) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/docdb-elastic-2022-11-28/GetPendingMaintenanceAction) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/docdb-elastic-2022-11-28/GetPendingMaintenanceAction) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/docdb-elastic-2022-11-28/GetPendingMaintenanceAction) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/docdb-elastic-2022-11-28/GetPendingMaintenanceAction) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/docdb-elastic-2022-11-28/GetPendingMaintenanceAction) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/docdb-elastic-2022-11-28/GetPendingMaintenanceAction) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/docdb-elastic-2022-11-28/GetPendingMaintenanceAction) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/docdb-elastic-2022-11-28/GetPendingMaintenanceAction) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/docdb-elastic-2022-11-28/GetPendingMaintenanceAction) 