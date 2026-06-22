---
id: "@specs/aws/batch/docs/API_ListConsumableResources"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListConsumableResources"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# ListConsumableResources

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_ListConsumableResources
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListConsumableResources
<a name="API_ListConsumableResources"></a>

Returns a list of AWS Batch consumable resources.

## Request Syntax
<a name="API_ListConsumableResources_RequestSyntax"></a>

```
POST /v1/listconsumableresources HTTP/1.1
Content-type: application/json

{
   "filters": [ 
      { 
         "name": "{{string}}",
         "values": [ "{{string}}" ]
      }
   ],
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListConsumableResources_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListConsumableResources_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filters](#API_ListConsumableResources_RequestSyntax) **   <a name="Batch-ListConsumableResources-request-filters"></a>
The filters to apply to the consumable resource list query. If used, only those consumable resources that match the filter are listed. Filter names and values can be:  
+ name: `CONSUMABLE_RESOURCE_NAME ` 

  values: case-insensitive matches for the consumable resource name. If a filter value ends with an asterisk (\*), it matches any consumable resource name that begins with the string before the '\*'.
Type: Array of [KeyValuesPair](API_KeyValuesPair.md) objects  
Required: No

 ** [maxResults](#API_ListConsumableResources_RequestSyntax) **   <a name="Batch-ListConsumableResources-request-maxResults"></a>
The maximum number of results returned by `ListConsumableResources` in paginated output. When this parameter is used, `ListConsumableResources` only returns `maxResults` results in a single page and a `nextToken` response element. The remaining results of the initial request can be seen by sending another `ListConsumableResources` request with the returned `nextToken` value. This value can be between 1 and 100. If this parameter isn't used, then `ListConsumableResources` returns up to 100 results and a `nextToken` value if applicable.  
Type: Integer  
Required: No

 ** [nextToken](#API_ListConsumableResources_RequestSyntax) **   <a name="Batch-ListConsumableResources-request-nextToken"></a>
The `nextToken` value returned from a previous paginated `ListConsumableResources` request where `maxResults` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the `nextToken` value. This value is `null` when there are no more results to return.  
Treat this token as an opaque identifier that's only used to retrieve the next items in a list and not for other programmatic purposes.
Type: String  
Required: No

## Response Syntax
<a name="API_ListConsumableResources_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "consumableResources": [ 
      { 
         "consumableResourceArn": "string",
         "consumableResourceName": "string",
         "inUseQuantity": number,
         "resourceType": "string",
         "totalQuantity": number
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListConsumableResources_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [consumableResources](#API_ListConsumableResources_ResponseSyntax) **   <a name="Batch-ListConsumableResources-response-consumableResources"></a>
A list of consumable resources that match the request.  
Type: Array of [ConsumableResourceSummary](API_ConsumableResourceSummary.md) objects

 ** [nextToken](#API_ListConsumableResources_ResponseSyntax) **   <a name="Batch-ListConsumableResources-response-nextToken"></a>
The `nextToken` value to include in a future `ListConsumableResources` request. When the results of a `ListConsumableResources` request exceed `maxResults`, this value can be used to retrieve the next page of results. This value is `null` when there are no more results to return.  
Type: String

## Errors
<a name="API_ListConsumableResources_Errors"></a>

 ** ClientException **   
These errors are usually caused by a client action. One example cause is using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Another cause is specifying an identifier that's not valid.  
HTTP Status Code: 400

 ** ServerException **   
These errors are usually caused by a server issue.  
HTTP Status Code: 500

## See Also
<a name="API_ListConsumableResources_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/batch-2016-08-10/ListConsumableResources) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/batch-2016-08-10/ListConsumableResources) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/ListConsumableResources) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/batch-2016-08-10/ListConsumableResources) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/ListConsumableResources) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/batch-2016-08-10/ListConsumableResources) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/batch-2016-08-10/ListConsumableResources) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/batch-2016-08-10/ListConsumableResources) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/batch-2016-08-10/ListConsumableResources) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/ListConsumableResources) 