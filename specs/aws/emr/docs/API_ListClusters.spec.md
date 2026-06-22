---
id: "@specs/aws/emr/docs/API_ListClusters"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListClusters"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# ListClusters

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_ListClusters
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListClusters
<a name="API_ListClusters"></a>

Provides the status of all clusters visible to this AWS account. Allows you to filter the list of clusters based on certain criteria; for example, filtering by cluster creation date and time or by status. This call returns a maximum of 50 clusters in unsorted order per call, but returns a marker to track the paging of the cluster list across multiple ListClusters calls.

## Request Syntax
<a name="API_ListClusters_RequestSyntax"></a>

```
{
   "ClusterStates": [ "{{string}}" ],
   "CreatedAfter": {{number}},
   "CreatedBefore": {{number}},
   "Marker": "{{string}}"
}
```

## Request Parameters
<a name="API_ListClusters_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClusterStates](#API_ListClusters_RequestSyntax) **   <a name="EMR-ListClusters-request-ClusterStates"></a>
The cluster state filters to apply when listing clusters. Clusters that change state while this action runs may be not be returned as expected in the list of clusters.  
Type: Array of strings  
Valid Values: `STARTING | BOOTSTRAPPING | RUNNING | WAITING | TERMINATING | TERMINATED | TERMINATED_WITH_ERRORS`   
Required: No

 ** [CreatedAfter](#API_ListClusters_RequestSyntax) **   <a name="EMR-ListClusters-request-CreatedAfter"></a>
The creation date and time beginning value filter for listing clusters.  
Type: Timestamp  
Required: No

 ** [CreatedBefore](#API_ListClusters_RequestSyntax) **   <a name="EMR-ListClusters-request-CreatedBefore"></a>
The creation date and time end value filter for listing clusters.  
Type: Timestamp  
Required: No

 ** [Marker](#API_ListClusters_RequestSyntax) **   <a name="EMR-ListClusters-request-Marker"></a>
The pagination token that indicates the next set of results to retrieve.  
Type: String  
Required: No

## Response Syntax
<a name="API_ListClusters_ResponseSyntax"></a>

```
{
   "Clusters": [ 
      { 
         "ClusterArn": "string",
         "Id": "string",
         "Name": "string",
         "NormalizedInstanceHours": number,
         "OutpostArn": "string",
         "Status": { 
            "ErrorDetails": [ 
               { 
                  "ErrorCode": "string",
                  "ErrorData": [ 
                     { 
                        "string" : "string" 
                     }
                  ],
                  "ErrorMessage": "string"
               }
            ],
            "State": "string",
            "StateChangeReason": { 
               "Code": "string",
               "Message": "string"
            },
            "Timeline": { 
               "CreationDateTime": number,
               "EndDateTime": number,
               "ReadyDateTime": number
            }
         }
      }
   ],
   "Marker": "string"
}
```

## Response Elements
<a name="API_ListClusters_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Clusters](#API_ListClusters_ResponseSyntax) **   <a name="EMR-ListClusters-response-Clusters"></a>
The list of clusters for the account based on the given filters.  
Type: Array of [ClusterSummary](API_ClusterSummary.md) objects

 ** [Marker](#API_ListClusters_ResponseSyntax) **   <a name="EMR-ListClusters-response-Marker"></a>
The pagination token that indicates the next set of results to retrieve.  
Type: String

## Errors
<a name="API_ListClusters_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **   
This exception occurs when there is an internal failure in the Amazon EMR service.    
 ** Message **   
The message associated with the exception.
HTTP Status Code: 500

 ** InvalidRequestException **   
This exception occurs when there is something wrong with user input.    
 ** ErrorCode **   
The error code associated with the exception.  
 ** Message **   
The message associated with the exception.
HTTP Status Code: 400

## See Also
<a name="API_ListClusters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticmapreduce-2009-03-31/ListClusters) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticmapreduce-2009-03-31/ListClusters) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/ListClusters) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticmapreduce-2009-03-31/ListClusters) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/ListClusters) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticmapreduce-2009-03-31/ListClusters) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticmapreduce-2009-03-31/ListClusters) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticmapreduce-2009-03-31/ListClusters) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticmapreduce-2009-03-31/ListClusters) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/ListClusters) 