---
id: "@specs/aws/fsx/docs/API_DescribeDataRepositoryAssociations"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeDataRepositoryAssociations"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# DescribeDataRepositoryAssociations

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_DescribeDataRepositoryAssociations
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeDataRepositoryAssociations
<a name="API_DescribeDataRepositoryAssociations"></a>

Returns the description of specific Amazon FSx for Lustre or Amazon File Cache data repository associations, if one or more `AssociationIds` values are provided in the request, or if filters are used in the request. Data repository associations are supported on Amazon File Cache resources and all FSx for Lustre 2.12 and 2,15 file systems, excluding `scratch_1` deployment type.

You can use filters to narrow the response to include just data repository associations for specific file systems (use the `file-system-id` filter with the ID of the file system) or caches (use the `file-cache-id` filter with the ID of the cache), or data repository associations for a specific repository type (use the `data-repository-type` filter with a value of `S3` or `NFS`). If you don't use filters, the response returns all data repository associations owned by your AWS account in the AWS Region of the endpoint that you're calling.

When retrieving all data repository associations, you can paginate the response by using the optional `MaxResults` parameter to limit the number of data repository associations returned in a response. If more data repository associations remain, a `NextToken` value is returned in the response. In this case, send a later request with the `NextToken` request parameter set to the value of `NextToken` from the last response.

## Request Syntax
<a name="API_DescribeDataRepositoryAssociations_RequestSyntax"></a>

```
{
   "AssociationIds": [ "{{string}}" ],
   "Filters": [ 
      { 
         "Name": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeDataRepositoryAssociations_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AssociationIds](#API_DescribeDataRepositoryAssociations_RequestSyntax) **   <a name="FSx-DescribeDataRepositoryAssociations-request-AssociationIds"></a>
IDs of the data repository associations whose descriptions you want to retrieve (String).  
Type: Array of strings  
Array Members: Maximum number of 50 items.  
Length Constraints: Minimum length of 13. Maximum length of 23.  
Pattern: `^(dra-[0-9a-f]{8,})$`   
Required: No

 ** [Filters](#API_DescribeDataRepositoryAssociations_RequestSyntax) **   <a name="FSx-DescribeDataRepositoryAssociations-request-Filters"></a>
A list of `Filter` elements.  
Type: Array of [Filter](API_Filter.md) objects  
Array Members: Maximum number of 10 items.  
Required: No

 ** [MaxResults](#API_DescribeDataRepositoryAssociations_RequestSyntax) **   <a name="FSx-DescribeDataRepositoryAssociations-request-MaxResults"></a>
The maximum number of resources to return in the response. This value must be an integer greater than zero.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 25.  
Required: No

 ** [NextToken](#API_DescribeDataRepositoryAssociations_RequestSyntax) **   <a name="FSx-DescribeDataRepositoryAssociations-request-NextToken"></a>
(Optional) Opaque pagination token returned from a previous operation (String). If present, this token indicates from what point you can continue processing the request, where the previous `NextToken` value left off.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$`   
Required: No

## Response Syntax
<a name="API_DescribeDataRepositoryAssociations_ResponseSyntax"></a>

```
{
   "Associations": [ 
      { 
         "AssociationId": "string",
         "BatchImportMetaDataOnCreate": boolean,
         "CreationTime": number,
         "DataRepositoryPath": "string",
         "DataRepositorySubdirectories": [ "string" ],
         "FailureDetails": { 
            "Message": "string"
         },
         "FileCacheId": "string",
         "FileCachePath": "string",
         "FileSystemId": "string",
         "FileSystemPath": "string",
         "ImportedFileChunkSize": number,
         "Lifecycle": "string",
         "NFS": { 
            "AutoExportPolicy": { 
               "Events": [ "string" ]
            },
            "DnsIps": [ "string" ],
            "Version": "string"
         },
         "ResourceARN": "string",
         "S3": { 
            "AutoExportPolicy": { 
               "Events": [ "string" ]
            },
            "AutoImportPolicy": { 
               "Events": [ "string" ]
            }
         },
         "Tags": [ 
            { 
               "Key": "string",
               "Value": "string"
            }
         ]
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_DescribeDataRepositoryAssociations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Associations](#API_DescribeDataRepositoryAssociations_ResponseSyntax) **   <a name="FSx-DescribeDataRepositoryAssociations-response-Associations"></a>
An array of one or more data repository association descriptions.  
Type: Array of [DataRepositoryAssociation](API_DataRepositoryAssociation.md) objects  
Array Members: Maximum number of 100 items.

 ** [NextToken](#API_DescribeDataRepositoryAssociations_ResponseSyntax) **   <a name="FSx-DescribeDataRepositoryAssociations-response-NextToken"></a>
(Optional) Opaque pagination token returned from a previous operation (String). If present, this token indicates from what point you can continue processing the request, where the previous `NextToken` value left off.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$` 

## Errors
<a name="API_DescribeDataRepositoryAssociations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequest **   
A generic error indicating a failure with a client request.    
 ** Message **   
A detailed error message.
HTTP Status Code: 400

 ** DataRepositoryAssociationNotFound **   
No data repository associations were found based upon the supplied parameters.    
 ** Message **   
A detailed error message.
HTTP Status Code: 400

 ** FileSystemNotFound **   
No Amazon FSx file systems were found based upon supplied parameters.    
 ** Message **   
A detailed error message.
HTTP Status Code: 400

 ** InternalServerError **   
A generic error indicating a server-side failure.    
 ** Message **   
A detailed error message.
HTTP Status Code: 500

 ** InvalidDataRepositoryType **   
You have filtered the response to a data repository type that is not supported.    
 ** Message **   
A detailed error message.
HTTP Status Code: 400

## See Also
<a name="API_DescribeDataRepositoryAssociations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/fsx-2018-03-01/DescribeDataRepositoryAssociations) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/fsx-2018-03-01/DescribeDataRepositoryAssociations) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/DescribeDataRepositoryAssociations) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/fsx-2018-03-01/DescribeDataRepositoryAssociations) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/DescribeDataRepositoryAssociations) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/fsx-2018-03-01/DescribeDataRepositoryAssociations) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/fsx-2018-03-01/DescribeDataRepositoryAssociations) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/fsx-2018-03-01/DescribeDataRepositoryAssociations) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/fsx-2018-03-01/DescribeDataRepositoryAssociations) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/DescribeDataRepositoryAssociations) 