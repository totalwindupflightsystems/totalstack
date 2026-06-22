---
id: "@specs/aws/redshift/docs/API_CreateTags"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateTags"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# CreateTags

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_CreateTags
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateTags
<a name="API_CreateTags"></a>

Adds tags to a cluster.

A resource can have up to 50 tags. If you try to create more than 50 tags for a resource, you will receive an error and the attempt will fail.

If you specify a key that already exists for the resource, the value for that key will be updated with the new value.

## Request Parameters
<a name="API_CreateTags_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ResourceName **   
The Amazon Resource Name (ARN) to which you want to add the tag or tags. For example, `arn:aws:redshift:us-east-2:123456789:cluster:t1`.   
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

 **Tags.Tag.N**   
One or more name/value pairs to add as tags to the specified resource. Each tag name is passed in with the parameter `Key` and the corresponding value is passed in with the parameter `Value`. The `Key` and `Value` parameters are separated by a comma (,). Separate multiple tags with a space. For example, `--tags "Key"="owner","Value"="admin" "Key"="environment","Value"="test" "Key"="version","Value"="1.0"`.   
Type: Array of [Tag](API_Tag.md) objects  
Required: Yes

## Errors
<a name="API_CreateTags_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidClusterState **   
The specified cluster is not in the `available` state.   
HTTP Status Code: 400

 ** InvalidTagFault **   
The tag is invalid.  
HTTP Status Code: 400

 ** ResourceNotFoundFault **   
The resource could not be found.  
HTTP Status Code: 404

 ** TagLimitExceededFault **   
You have exceeded the number of tags allowed.  
HTTP Status Code: 400

## Examples
<a name="API_CreateTags_Examples"></a>

### Example
<a name="API_CreateTags_Example_1"></a>

This example illustrates one usage of CreateTags.

#### Sample Request
<a name="API_CreateTags_Example_1_Request"></a>

```
https://redshift.us-east-2.amazonaws.com/
       ?Action=CreateTags
&ResourceName=arn%3Aaws%3Aredshift%3Aus-east-2%3A123456789012%3Acluster%3Amycluster
&Tags.Tag.1.Key=mytag
&Tags.Tag.1.Value=newtag
&SignatureMethod=HmacSHA256&SignatureVersion=4
&Version=2012-12-01
&X-Amz-Algorithm=AWS4-HMAC-SHA256
&X-Amz-Credential=AKIAIOSFODNN7EXAMPLE/20190817/us-east-2/redshift/aws4_request
&X-Amz-Date=20190825T160000Z
&X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
&X-Amz-Signature=0aa1234bb5cc678ddddd901ee2ff3aa45678b90c12d345e6ff789012345a6b7b
```

#### Sample Response
<a name="API_CreateTags_Example_1_Response"></a>

```
<CreateTagsResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">
  <ResponseMetadata>
    <RequestId>bf5cbe2f-2837-11ea-9467-b9a67a99da45</RequestId>
  </ResponseMetadata>
</CreateTagsResponse>
```

## See Also
<a name="API_CreateTags_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/CreateTags) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/CreateTags) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/CreateTags) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/CreateTags) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/CreateTags) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/CreateTags) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/CreateTags) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/CreateTags) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/CreateTags) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/CreateTags) 