---
id: "@specs/aws/emr/docs/API_ListSupportedInstanceTypes"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListSupportedInstanceTypes"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# ListSupportedInstanceTypes

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_ListSupportedInstanceTypes
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListSupportedInstanceTypes
<a name="API_ListSupportedInstanceTypes"></a>

A list of the instance types that Amazon EMR supports. You can filter the list by AWS Region and Amazon EMR release. 

## Request Syntax
<a name="API_ListSupportedInstanceTypes_RequestSyntax"></a>

```
{
   "Marker": "{{string}}",
   "ReleaseLabel": "{{string}}"
}
```

## Request Parameters
<a name="API_ListSupportedInstanceTypes_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Marker](#API_ListSupportedInstanceTypes_RequestSyntax) **   <a name="EMR-ListSupportedInstanceTypes-request-Marker"></a>
The pagination token that marks the next set of results to retrieve.  
Type: String  
Required: No

 ** [ReleaseLabel](#API_ListSupportedInstanceTypes_RequestSyntax) **   <a name="EMR-ListSupportedInstanceTypes-request-ReleaseLabel"></a>
The Amazon EMR release label determines the [versions of open-source application packages](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-release-app-versions-6.x.html) that Amazon EMR has installed on the cluster. Release labels are in the format `emr-x.x.x`, where x.x.x is an Amazon EMR release number such as `emr-6.10.0`. For more information about Amazon EMR releases and their included application versions and features, see the * [Amazon EMR Release Guide](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-release-components.html) *.  
Type: String  
Required: Yes

## Response Syntax
<a name="API_ListSupportedInstanceTypes_ResponseSyntax"></a>

```
{
   "Marker": "string",
   "SupportedInstanceTypes": [ 
      { 
         "Architecture": "string",
         "EbsOptimizedAvailable": boolean,
         "EbsOptimizedByDefault": boolean,
         "EbsStorageOnly": boolean,
         "InstanceFamilyId": "string",
         "Is64BitsOnly": boolean,
         "MemoryGB": number,
         "NumberOfDisks": number,
         "StorageGB": number,
         "Type": "string",
         "VCPU": number
      }
   ]
}
```

## Response Elements
<a name="API_ListSupportedInstanceTypes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Marker](#API_ListSupportedInstanceTypes_ResponseSyntax) **   <a name="EMR-ListSupportedInstanceTypes-response-Marker"></a>
The pagination token that marks the next set of results to retrieve.  
Type: String

 ** [SupportedInstanceTypes](#API_ListSupportedInstanceTypes_ResponseSyntax) **   <a name="EMR-ListSupportedInstanceTypes-response-SupportedInstanceTypes"></a>
The list of instance types that the release specified in `ListSupportedInstanceTypesInput$ReleaseLabel` supports, filtered by AWS Region.  
Type: Array of [SupportedInstanceType](API_SupportedInstanceType.md) objects

## Errors
<a name="API_ListSupportedInstanceTypes_Errors"></a>

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
<a name="API_ListSupportedInstanceTypes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticmapreduce-2009-03-31/ListSupportedInstanceTypes) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticmapreduce-2009-03-31/ListSupportedInstanceTypes) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/ListSupportedInstanceTypes) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticmapreduce-2009-03-31/ListSupportedInstanceTypes) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/ListSupportedInstanceTypes) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticmapreduce-2009-03-31/ListSupportedInstanceTypes) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticmapreduce-2009-03-31/ListSupportedInstanceTypes) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticmapreduce-2009-03-31/ListSupportedInstanceTypes) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticmapreduce-2009-03-31/ListSupportedInstanceTypes) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/ListSupportedInstanceTypes) 