---
id: "@specs/aws/appsync/docs/API_ListDataSources"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListDataSources"
status: active
depends_on:
  - "@specs/aws/appsync/meta"
---

# ListDataSources

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appsync/docs/API_ListDataSources
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListDataSources
<a name="API_ListDataSources"></a>

Lists the data sources for a given API.

## Request Syntax
<a name="API_ListDataSources_RequestSyntax"></a>

```
GET /v1/apis/{{apiId}}/datasources?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListDataSources_RequestParameters"></a>

The request uses the following URI parameters.

 ** [apiId](#API_ListDataSources_RequestSyntax) **   <a name="appsync-ListDataSources-request-uri-apiId"></a>
The API ID.  
Required: Yes

 ** [maxResults](#API_ListDataSources_RequestSyntax) **   <a name="appsync-ListDataSources-request-uri-maxResults"></a>
The maximum number of results that you want the request to return.  
Valid Range: Minimum value of 0. Maximum value of 25.

 ** [nextToken](#API_ListDataSources_RequestSyntax) **   <a name="appsync-ListDataSources-request-uri-nextToken"></a>
An identifier that was returned from the previous call to this operation, which you can use to return the next set of items in the list.  
Length Constraints: Minimum length of 1. Maximum length of 65536.  
Pattern: `[\S]+` 

## Request Body
<a name="API_ListDataSources_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListDataSources_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "dataSources": [ 
      { 
         "dataSourceArn": "string",
         "description": "string",
         "dynamodbConfig": { 
            "awsRegion": "string",
            "deltaSyncConfig": { 
               "baseTableTTL": number,
               "deltaSyncTableName": "string",
               "deltaSyncTableTTL": number
            },
            "tableName": "string",
            "useCallerCredentials": boolean,
            "versioned": boolean
         },
         "elasticsearchConfig": { 
            "awsRegion": "string",
            "endpoint": "string"
         },
         "eventBridgeConfig": { 
            "eventBusArn": "string"
         },
         "httpConfig": { 
            "authorizationConfig": { 
               "authorizationType": "string",
               "awsIamConfig": { 
                  "signingRegion": "string",
                  "signingServiceName": "string"
               }
            },
            "endpoint": "string"
         },
         "lambdaConfig": { 
            "lambdaFunctionArn": "string"
         },
         "metricsConfig": "string",
         "name": "string",
         "openSearchServiceConfig": { 
            "awsRegion": "string",
            "endpoint": "string"
         },
         "relationalDatabaseConfig": { 
            "rdsHttpEndpointConfig": { 
               "awsRegion": "string",
               "awsSecretStoreArn": "string",
               "databaseName": "string",
               "dbClusterIdentifier": "string",
               "schema": "string"
            },
            "relationalDatabaseSourceType": "string"
         },
         "serviceRoleArn": "string",
         "type": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListDataSources_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [dataSources](#API_ListDataSources_ResponseSyntax) **   <a name="appsync-ListDataSources-response-dataSources"></a>
The `DataSource` objects.  
Type: Array of [DataSource](API_DataSource.md) objects

 ** [nextToken](#API_ListDataSources_ResponseSyntax) **   <a name="appsync-ListDataSources-response-nextToken"></a>
An identifier to pass in the next request to this operation to return the next set of items in the list.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 65536.  
Pattern: `[\S]+` 

## Errors
<a name="API_ListDataSources_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **   
The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and then try again.    
 ** detail **   
Provides further details for the reason behind the bad request. For reason type `CODE_ERROR`, the detail will contain a list of code errors.  
 ** reason **   
Provides context for the cause of the bad request. The only supported value is `CODE_ERROR`.
HTTP Status Code: 400

 ** InternalFailureException **   
An internal AWS AppSync error occurred. Try your request again.  
HTTP Status Code: 500

 ** NotFoundException **   
The resource specified in the request was not found. Check the resource, and then try again.  
HTTP Status Code: 404

 ** UnauthorizedException **   
You aren't authorized to perform this operation.  
HTTP Status Code: 401

## See Also
<a name="API_ListDataSources_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appsync-2017-07-25/ListDataSources) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appsync-2017-07-25/ListDataSources) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appsync-2017-07-25/ListDataSources) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appsync-2017-07-25/ListDataSources) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appsync-2017-07-25/ListDataSources) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appsync-2017-07-25/ListDataSources) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appsync-2017-07-25/ListDataSources) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appsync-2017-07-25/ListDataSources) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appsync-2017-07-25/ListDataSources) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appsync-2017-07-25/ListDataSources) 