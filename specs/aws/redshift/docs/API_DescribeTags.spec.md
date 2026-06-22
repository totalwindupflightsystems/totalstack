---
id: "@specs/aws/redshift/docs/API_DescribeTags"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeTags"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# DescribeTags

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_DescribeTags
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeTags
<a name="API_DescribeTags"></a>

Returns a list of tags. You can return tags from a specific resource by specifying an ARN, or you can return all tags for a given type of resource, such as clusters, snapshots, and so on.

The following are limitations for `DescribeTags`: 
+ You cannot specify an ARN and a resource-type value together in the same request.
+ You cannot use the `MaxRecords` and `Marker` parameters together with the ARN parameter.
+ The `MaxRecords` parameter can be a range from 10 to 50 results to return in a request.

If you specify both tag keys and tag values in the same request, Amazon Redshift returns all resources that match any combination of the specified keys and values. For example, if you have `owner` and `environment` for tag keys, and `admin` and `test` for tag values, all resources that have any combination of those values are returned.

If both tag keys and values are omitted from the request, resources are returned regardless of whether they have tag keys or values associated with them.

## Request Parameters
<a name="API_DescribeTags_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** Marker **   
A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the `marker` parameter and retrying the command. If the `marker` field is empty, all response records have been retrieved for the request.   
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** MaxRecords **   
The maximum number or response records to return in each call. If the number of remaining response records exceeds the specified `MaxRecords` value, a value is returned in a `marker` field of the response. You can retrieve the next set of records by retrying the command with the returned `marker` value.   
Type: Integer  
Required: No

 ** ResourceName **   
The Amazon Resource Name (ARN) for which you want to describe the tag or tags. For example, `arn:aws:redshift:us-east-2:123456789:cluster:t1`.   
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** ResourceType **   
The type of resource with which you want to view tags. Valid resource types are:   
+ Cluster
+ CIDR/IP
+ EC2 security group
+ Snapshot
+ Cluster security group
+ Subnet group
+ HSM connection
+ HSM certificate
+ Parameter group
+ Snapshot copy grant
+ Integration (zero-ETL integration or S3 event integration)
**Note**  
To describe the tags associated with an `integration`, don't specify `ResourceType`, instead specify the `ResourceName` of the integration.
For more information about Amazon Redshift resource types and constructing ARNs, go to [Specifying Policy Elements: Actions, Effects, Resources, and Principals](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-overview.html#redshift-iam-access-control-specify-actions) in the Amazon Redshift Cluster Management Guide.   
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 **TagKeys.TagKey.N**   
A tag key or keys for which you want to return all matching resources that are associated with the specified key or keys. For example, suppose that you have resources tagged with keys called `owner` and `environment`. If you specify both of these tag keys in the request, Amazon Redshift returns a response with all resources that have either or both of these tag keys associated with them.  
Type: Array of strings  
Length Constraints: Maximum length of 2147483647.  
Required: No

 **TagValues.TagValue.N**   
A tag value or values for which you want to return all matching resources that are associated with the specified value or values. For example, suppose that you have resources tagged with values called `admin` and `test`. If you specify both of these tag values in the request, Amazon Redshift returns a response with all resources that have either or both of these tag values associated with them.  
Type: Array of strings  
Length Constraints: Maximum length of 2147483647.  
Required: No

## Response Elements
<a name="API_DescribeTags_ResponseElements"></a>

The following elements are returned by the service.

 ** Marker **   
A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the `Marker` parameter and retrying the command. If the `Marker` field is empty, all response records have been retrieved for the request.   
Type: String  
Length Constraints: Maximum length of 2147483647.

 **TaggedResources.TaggedResource.N**   
A list of tags with their associated resources.  
Type: Array of [TaggedResource](API_TaggedResource.md) objects

## Errors
<a name="API_DescribeTags_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidTagFault **   
The tag is invalid.  
HTTP Status Code: 400

 ** ResourceNotFoundFault **   
The resource could not be found.  
HTTP Status Code: 404

## Examples
<a name="API_DescribeTags_Examples"></a>

### Example
<a name="API_DescribeTags_Example_1"></a>

This example illustrates one usage of DescribeTags.

#### Sample Request
<a name="API_DescribeTags_Example_1_Request"></a>

```
https://redshift.us-east-2.amazonaws.com/
       ?Action=DescribeTags
&ResourceName=arn%3Aaws%3Aredshift%3Aus-east-2%3A123456789012%3Acluster%3Amycluster
&TagKeys.TagKey.1=mytag
&TagValues.TagValue.1=newtag
&SignatureMethod=HmacSHA256&SignatureVersion=4
&Version=2012-12-01
&X-Amz-Algorithm=AWS4-HMAC-SHA256
&X-Amz-Credential=AKIAIOSFODNN7EXAMPLE/20190817/us-east-2/redshift/aws4_request
&X-Amz-Date=20190825T160000Z
&X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
&X-Amz-Signature=0aa1234bb5cc678ddddd901ee2ff3aa45678b90c12d345e6ff789012345a6b7b
```

#### Sample Response
<a name="API_DescribeTags_Example_1_Response"></a>

```
<DescribeTagsResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">
  <DescribeTagsResult>
    <TaggedResources>
      <TaggedResource>
        <ResourceName>arn:aws:redshift:us-east-2:123456789012:cluster:mycluster</ResourceName>
        <Tag>
          <Value>newtag</Value>
          <Key>mytag</Key>
        </Tag>
        <ResourceType>cluster</ResourceType>
      </TaggedResource>
    </TaggedResources>
  </DescribeTagsResult>
  <ResponseMetadata>
    <RequestId>09b7e6a0-28da-11ea-8314-974e2ba81189</RequestId>
  </ResponseMetadata>
</DescribeTagsResponse>
```

## See Also
<a name="API_DescribeTags_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/DescribeTags) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/DescribeTags) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/DescribeTags) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/DescribeTags) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/DescribeTags) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/DescribeTags) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/DescribeTags) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/DescribeTags) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/DescribeTags) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/DescribeTags) 