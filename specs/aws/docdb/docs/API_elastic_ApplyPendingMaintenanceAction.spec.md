---
id: "@specs/aws/docdb/docs/API_elastic_ApplyPendingMaintenanceAction"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ApplyPendingMaintenanceAction"
status: active
depends_on:
  - "@specs/aws/docdb/meta"
---

# ApplyPendingMaintenanceAction

> **source:** AWS Documentation
> **spec:id:** @specs/aws/docdb/docs/API_elastic_ApplyPendingMaintenanceAction
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ApplyPendingMaintenanceAction
<a name="API_elastic_ApplyPendingMaintenanceAction"></a>

The type of pending maintenance action to be applied to the resource.

## Request Syntax
<a name="API_elastic_ApplyPendingMaintenanceAction_RequestSyntax"></a>

```
POST /pending-action HTTP/1.1
Content-type: application/json

{
   "applyAction": "{{string}}",
   "applyOn": "{{string}}",
   "optInType": "{{string}}",
   "resourceArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_elastic_ApplyPendingMaintenanceAction_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_elastic_ApplyPendingMaintenanceAction_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [applyAction](#API_elastic_ApplyPendingMaintenanceAction_RequestSyntax) **   <a name="documentdb-elastic_ApplyPendingMaintenanceAction-request-applyAction"></a>
The pending maintenance action to apply to the resource.  
Valid actions are:  
+  `ENGINE_UPDATE ` 
+  `ENGINE_UPGRADE` 
+  `SECURITY_UPDATE` 
+  `OS_UPDATE` 
+  `MASTER_USER_PASSWORD_UPDATE` 
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Required: Yes

 ** [optInType](#API_elastic_ApplyPendingMaintenanceAction_RequestSyntax) **   <a name="documentdb-elastic_ApplyPendingMaintenanceAction-request-optInType"></a>
A value that specifies the type of opt-in request, or undoes an opt-in request. An opt-in request of type `IMMEDIATE` can't be undone.  
Type: String  
Valid Values: `IMMEDIATE | NEXT_MAINTENANCE | APPLY_ON | UNDO_OPT_IN`   
Required: Yes

 ** [resourceArn](#API_elastic_ApplyPendingMaintenanceAction_RequestSyntax) **   <a name="documentdb-elastic_ApplyPendingMaintenanceAction-request-resourceArn"></a>
The Amazon DocumentDB Amazon Resource Name (ARN) of the resource to which the pending maintenance action applies.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Required: Yes

 ** [applyOn](#API_elastic_ApplyPendingMaintenanceAction_RequestSyntax) **   <a name="documentdb-elastic_ApplyPendingMaintenanceAction-request-applyOn"></a>
A specific date to apply the pending maintenance action. Required if opt-in-type is `APPLY_ON`. Format: `yyyy/MM/dd HH:mm-yyyy/MM/dd HH:mm`   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Required: No

## Response Syntax
<a name="API_elastic_ApplyPendingMaintenanceAction_ResponseSyntax"></a>

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
<a name="API_elastic_ApplyPendingMaintenanceAction_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [resourcePendingMaintenanceAction](#API_elastic_ApplyPendingMaintenanceAction_ResponseSyntax) **   <a name="documentdb-elastic_ApplyPendingMaintenanceAction-response-resourcePendingMaintenanceAction"></a>
The output of the pending maintenance action being applied.  
Type: [ResourcePendingMaintenanceAction](API_elastic_ResourcePendingMaintenanceAction.md) object

## Errors
<a name="API_elastic_ApplyPendingMaintenanceAction_Errors"></a>

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
<a name="API_elastic_ApplyPendingMaintenanceAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/docdb-elastic-2022-11-28/ApplyPendingMaintenanceAction) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/docdb-elastic-2022-11-28/ApplyPendingMaintenanceAction) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/docdb-elastic-2022-11-28/ApplyPendingMaintenanceAction) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/docdb-elastic-2022-11-28/ApplyPendingMaintenanceAction) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/docdb-elastic-2022-11-28/ApplyPendingMaintenanceAction) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/docdb-elastic-2022-11-28/ApplyPendingMaintenanceAction) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/docdb-elastic-2022-11-28/ApplyPendingMaintenanceAction) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/docdb-elastic-2022-11-28/ApplyPendingMaintenanceAction) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/docdb-elastic-2022-11-28/ApplyPendingMaintenanceAction) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/docdb-elastic-2022-11-28/ApplyPendingMaintenanceAction) 