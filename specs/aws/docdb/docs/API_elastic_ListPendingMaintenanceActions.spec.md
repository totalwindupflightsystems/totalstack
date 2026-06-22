---
id: "@specs/aws/docdb/docs/API_elastic_ListPendingMaintenanceActions"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListPendingMaintenanceActions"
status: active
depends_on:
  - "@specs/aws/docdb/meta"
---

# ListPendingMaintenanceActions

> **source:** AWS Documentation
> **spec:id:** @specs/aws/docdb/docs/API_elastic_ListPendingMaintenanceActions
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListPendingMaintenanceActions
<a name="API_elastic_ListPendingMaintenanceActions"></a>

Retrieves a list of all maintenance actions that are pending.

## Request Syntax
<a name="API_elastic_ListPendingMaintenanceActions_RequestSyntax"></a>

```
GET /pending-actions?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_elastic_ListPendingMaintenanceActions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_elastic_ListPendingMaintenanceActions_RequestSyntax) **   <a name="documentdb-elastic_ListPendingMaintenanceActions-request-uri-maxResults"></a>
The maximum number of results to include in the response. If more records exist than the specified `maxResults` value, a pagination token (marker) is included in the response so that the remaining results can be retrieved.  
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_elastic_ListPendingMaintenanceActions_RequestSyntax) **   <a name="documentdb-elastic_ListPendingMaintenanceActions-request-uri-nextToken"></a>
An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `maxResults`.

## Request Body
<a name="API_elastic_ListPendingMaintenanceActions_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_elastic_ListPendingMaintenanceActions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "resourcePendingMaintenanceActions": [ 
      { 
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
   ]
}
```

## Response Elements
<a name="API_elastic_ListPendingMaintenanceActions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [resourcePendingMaintenanceActions](#API_elastic_ListPendingMaintenanceActions_ResponseSyntax) **   <a name="documentdb-elastic_ListPendingMaintenanceActions-response-resourcePendingMaintenanceActions"></a>
Provides information about a pending maintenance action for a resource.  
Type: Array of [ResourcePendingMaintenanceAction](API_elastic_ResourcePendingMaintenanceAction.md) objects

 ** [nextToken](#API_elastic_ListPendingMaintenanceActions_ResponseSyntax) **   <a name="documentdb-elastic_ListPendingMaintenanceActions-response-nextToken"></a>
An optional pagination token provided by a previous request. If this parameter is displayed, the responses will include only records beyond the marker, up to the value specified by `maxResults`.  
Type: String

## Errors
<a name="API_elastic_ListPendingMaintenanceActions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
An exception that occurs when there are not sufficient permissions to perform an action.    
 ** message **   
An error message explaining why access was denied.
HTTP Status Code: 403

 ** InternalServerException **   
There was an internal server error.  
HTTP Status Code: 500

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
<a name="API_elastic_ListPendingMaintenanceActions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/docdb-elastic-2022-11-28/ListPendingMaintenanceActions) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/docdb-elastic-2022-11-28/ListPendingMaintenanceActions) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/docdb-elastic-2022-11-28/ListPendingMaintenanceActions) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/docdb-elastic-2022-11-28/ListPendingMaintenanceActions) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/docdb-elastic-2022-11-28/ListPendingMaintenanceActions) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/docdb-elastic-2022-11-28/ListPendingMaintenanceActions) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/docdb-elastic-2022-11-28/ListPendingMaintenanceActions) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/docdb-elastic-2022-11-28/ListPendingMaintenanceActions) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/docdb-elastic-2022-11-28/ListPendingMaintenanceActions) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/docdb-elastic-2022-11-28/ListPendingMaintenanceActions) 