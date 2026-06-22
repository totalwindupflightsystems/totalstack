---
id: "@specs/aws/redshift/docs/API_DeleteTags"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteTags"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# DeleteTags

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_DeleteTags
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteTags
<a name="API_DeleteTags"></a>

Deletes tags from a resource. You must provide the ARN of the resource from which you want to delete the tag or tags.

## Request Parameters
<a name="API_DeleteTags_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ResourceName **   
The Amazon Resource Name (ARN) from which you want to remove the tag or tags. For example, `arn:aws:redshift:us-east-2:123456789:cluster:t1`.   
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

 **TagKeys.TagKey.N**   
The tag key that you want to delete.  
Type: Array of strings  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

## Errors
<a name="API_DeleteTags_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidTagFault **   
The tag is invalid.  
HTTP Status Code: 400

 ** ResourceNotFoundFault **   
The resource could not be found.  
HTTP Status Code: 404

## Examples
<a name="API_DeleteTags_Examples"></a>

### Example
<a name="API_DeleteTags_Example_1"></a>

This example illustrates one usage of DeleteTags.

#### Sample Request
<a name="API_DeleteTags_Example_1_Request"></a>

```
https://redshift.us-east-2.amazonaws.com/
       ?Action=DeleteTags
&ResourceName=arn%3Aaws%3Aredshift%3Aus-east-2%3A123456789012%3Acluster%3Amycluster
&TagKeys.TagKey.1=mytag
&TagKeys.TagKey.2=newtag
&SignatureMethod=HmacSHA256&SignatureVersion=4
&Version=2012-12-01
&X-Amz-Algorithm=AWS4-HMAC-SHA256
&X-Amz-Credential=AKIAIOSFODNN7EXAMPLE/20190817/us-east-2/redshift/aws4_request
&X-Amz-Date=20190825T160000Z
&X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
&X-Amz-Signature=0aa1234bb5cc678ddddd901ee2ff3aa45678b90c12d345e6ff789012345a6b7b
```

#### Sample Response
<a name="API_DeleteTags_Example_1_Response"></a>

```
<DeleteTagsResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">
  <ResponseMetadata>
    <RequestId>bd69e08c-283d-11ea-9939-5fccefa818c0</RequestId>
  </ResponseMetadata>
</DeleteTagsResponse>
```

## See Also
<a name="API_DeleteTags_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/DeleteTags) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/DeleteTags) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/DeleteTags) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/DeleteTags) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/DeleteTags) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/DeleteTags) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/DeleteTags) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/DeleteTags) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/DeleteTags) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/DeleteTags) 