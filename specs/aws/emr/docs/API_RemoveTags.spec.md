---
id: "@specs/aws/emr/docs/API_RemoveTags"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RemoveTags"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# RemoveTags

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_RemoveTags
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RemoveTags
<a name="API_RemoveTags"></a>

Removes tags from an Amazon EMR resource, such as a cluster or Amazon EMR Studio. Tags make it easier to associate resources in various ways, such as grouping clusters to track your Amazon EMR resource allocation costs. For more information, see [Tag Clusters](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-tags.html). 

The following example removes the stack tag with value Prod from a cluster:

## Request Syntax
<a name="API_RemoveTags_RequestSyntax"></a>

```
{
   "ResourceId": "{{string}}",
   "TagKeys": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_RemoveTags_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ResourceId](#API_RemoveTags_RequestSyntax) **   <a name="EMR-RemoveTags-request-ResourceId"></a>
The Amazon EMR resource identifier from which tags will be removed. For example, a cluster identifier or an Amazon EMR Studio ID.  
Type: String  
Required: Yes

 ** [TagKeys](#API_RemoveTags_RequestSyntax) **   <a name="EMR-RemoveTags-request-TagKeys"></a>
A list of tag keys to remove from the resource.  
Type: Array of strings  
Required: Yes

## Response Elements
<a name="API_RemoveTags_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_RemoveTags_Errors"></a>

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

## Examples
<a name="API_RemoveTags_Examples"></a>

### Example
<a name="API_RemoveTags_Example_1"></a>

This example illustrates one usage of RemoveTags.

#### Sample Request
<a name="API_RemoveTags_Example_1_Request"></a>

```
POST / HTTP/1.1                                                                                                                                                
Content-Type: application/x-amz-json-1.1                                                                                                                                                       
X-Amz-Target: ElasticMapReduce.RemoveTags                                                                                                                                                      
AUTHPARAMS                                                                                                                                                                                     
{                                                                                                                                                                                              
  "ResourceId": "j-3U7TSX5GZFD8Y",                                                                                                                                                             
  "Tags": [{                                                                                                                                                                                   
      "Key": "stack",                                                                                                                                                                          
      "Value": "Prod"                                                                                                                                                                          
  }]                                                                                                                                                                                           
}
```

#### Sample Response
<a name="API_RemoveTags_Example_1_Response"></a>

```
HTTP/1.1 200 OK                                                                                                                                               
x-amzn-RequestId: 9da5a349-ed9e-11e2-90db-69a5154aeb8d                                                                                                                                         
Content-Type: application/x-amz-json-1.1                                                                                                                                                       
Content-Length: 71                                                                                                                                                                             
Date: Mon, 15 Jul 2013 22:33:47 GMT                                                                                                                                                            
{                                                                                                                                                                                              
}
```

### Example
<a name="API_RemoveTags_Example_2"></a>

The following example removes the stack and hbase tags from a cluster:

#### Sample Request
<a name="API_RemoveTags_Example_2_Request"></a>

```
POST / HTTP/1.1                                                                                                                                                
Content-Type: application/x-amz-json-1.1                                                                                                                                                       
X-Amz-Target: ElasticMapReduce.RemoveTags                                                                                                                                                      
AUTHPARAMS                                                                                                                                                                                     
{                                                                                                                                                                                              
  "ResourceId": "j-3U7TSX5GZFD8Y",                                                                                                                                                             
  "Tags": [{                                                                                                                                                                                   
      "Key": "stack"                                                                                                                                                                           
  },                                                                                                                                                                                           
  {                                                                                                                                                                                            
      "Key": "hbase"                                                                                                                                                                           
  }]                                                                                                                                                                                           
}
```

#### Sample Response
<a name="API_RemoveTags_Example_2_Response"></a>

```
HTTP/1.1 200 OK                                                                                                                                               
x-amzn-RequestId: 9da5a349-ed9e-11e2-90db-69a5154aeb8d                                                                                                                                         
Content-Type: application/x-amz-json-1.1                                                                                                                                                       
Content-Length: 71                                                                                                                                                                             
Date: Mon, 15 Jul 2013 22:33:47 GMT                                                                                                                                                            
{                                                                                                                                                                                              
}
```

## See Also
<a name="API_RemoveTags_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticmapreduce-2009-03-31/RemoveTags) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticmapreduce-2009-03-31/RemoveTags) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/RemoveTags) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticmapreduce-2009-03-31/RemoveTags) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/RemoveTags) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticmapreduce-2009-03-31/RemoveTags) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticmapreduce-2009-03-31/RemoveTags) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticmapreduce-2009-03-31/RemoveTags) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticmapreduce-2009-03-31/RemoveTags) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/RemoveTags) 