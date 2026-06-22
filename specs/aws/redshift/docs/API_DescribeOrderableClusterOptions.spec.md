---
id: "@specs/aws/redshift/docs/API_DescribeOrderableClusterOptions"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeOrderableClusterOptions"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# DescribeOrderableClusterOptions

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_DescribeOrderableClusterOptions
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeOrderableClusterOptions
<a name="API_DescribeOrderableClusterOptions"></a>

Returns a list of orderable cluster options. Before you create a new cluster you can use this operation to find what options are available, such as the EC2 Availability Zones (AZ) in the specific AWS Region that you can specify, and the node types you can request. The node types differ by available storage, memory, CPU and price. With the cost involved you might want to obtain a list of cluster options in the specific region and specify values when creating a cluster. For more information about managing clusters, go to [Amazon Redshift Clusters](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html) in the *Amazon Redshift Cluster Management Guide*.

## Request Parameters
<a name="API_DescribeOrderableClusterOptions_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ClusterVersion **   
The version filter value. Specify this parameter to show only the available offerings matching the specified version.  
Default: All versions.  
Constraints: Must be one of the version returned from [DescribeClusterVersions](API_DescribeClusterVersions.md).  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** Marker **   
An optional parameter that specifies the starting point to return a set of response records. When the results of a [DescribeOrderableClusterOptions](#API_DescribeOrderableClusterOptions) request exceed the value specified in `MaxRecords`, AWS returns a value in the `Marker` field of the response. You can retrieve the next set of response records by providing the returned marker value in the `Marker` parameter and retrying the request.   
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** MaxRecords **   
The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified `MaxRecords` value, a value is returned in a `marker` field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.   
Default: `100`   
Constraints: minimum 20, maximum 100.  
Type: Integer  
Required: No

 ** NodeType **   
The node type filter value. Specify this parameter to show only the available offerings matching the specified node type.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

## Response Elements
<a name="API_DescribeOrderableClusterOptions_ResponseElements"></a>

The following elements are returned by the service.

 ** Marker **   
A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the `Marker` parameter and retrying the command. If the `Marker` field is empty, all response records have been retrieved for the request.   
Type: String  
Length Constraints: Maximum length of 2147483647.

 **OrderableClusterOptions.OrderableClusterOption.N**   
An `OrderableClusterOption` structure containing information about orderable options for the cluster.  
Type: Array of [OrderableClusterOption](API_OrderableClusterOption.md) objects

## Errors
<a name="API_DescribeOrderableClusterOptions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeOrderableClusterOptions_Examples"></a>

### Example
<a name="API_DescribeOrderableClusterOptions_Example_1"></a>

This example illustrates one usage of DescribeOrderableClusterOptions.

#### Sample Request
<a name="API_DescribeOrderableClusterOptions_Example_1_Request"></a>

```
https://redshift.us-east-2.amazonaws.com/
       ?Action=DescribeOrderableClusterOptions
&SignatureMethod=HmacSHA256&SignatureVersion=4
&Version=2012-12-01
&X-Amz-Algorithm=AWS4-HMAC-SHA256
&X-Amz-Credential=AKIAIOSFODNN7EXAMPLE/20190817/us-east-2/redshift/aws4_request
&X-Amz-Date=20190825T160000Z
&X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
&X-Amz-Signature=0aa1234bb5cc678ddddd901ee2ff3aa45678b90c12d345e6ff789012345a6b7b
```

#### Sample Response
<a name="API_DescribeOrderableClusterOptions_Example_1_Response"></a>

```
<DescribeOrderableClusterOptionsResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">
  <DescribeOrderableClusterOptionsResult>
    <OrderableClusterOptions>
      <OrderableClusterOption>
        <ClusterType>multi-node</ClusterType>
        <AvailabilityZones>
          <AvailabilityZone>
            <Name>us-east-2a</Name>
            <SupportedPlatforms>
              <SupportedPlatform>
                <Name>VPC</Name>
              </SupportedPlatform>
            </SupportedPlatforms>
          </AvailabilityZone>
          <AvailabilityZone>
            <Name>us-east-2b</Name>
            <SupportedPlatforms>
              <SupportedPlatform>
                <Name>VPC</Name>
              </SupportedPlatform>
            </SupportedPlatforms>
          </AvailabilityZone>
          <AvailabilityZone>
            <Name>us-east-2c</Name>
            <SupportedPlatforms>
              <SupportedPlatform>
                <Name>VPC</Name>
              </SupportedPlatform>
            </SupportedPlatforms>
          </AvailabilityZone>
          <AvailabilityZone>
            <Name>us-east-2d</Name>
            <SupportedPlatforms>
              <SupportedPlatform>
                <Name>VPC</Name>
              </SupportedPlatform>
            </SupportedPlatforms>
          </AvailabilityZone>
          <AvailabilityZone>
            <Name>us-east-2e</Name>
            <SupportedPlatforms>
              <SupportedPlatform>
                <Name>VPC</Name>
              </SupportedPlatform>
            </SupportedPlatforms>
          </AvailabilityZone>
          <AvailabilityZone>
            <Name>us-east-2f</Name>
            <SupportedPlatforms>
              <SupportedPlatform>
                <Name>VPC</Name>
              </SupportedPlatform>
            </SupportedPlatforms>
          </AvailabilityZone>
        </AvailabilityZones>
        <NodeType>dc2.8xlarge</NodeType>
        <ClusterVersion>1.0</ClusterVersion>
      </OrderableClusterOption>
        <ClusterType>multi-node</ClusterType>
        <AvailabilityZones>
          <AvailabilityZone>
            <Name>us-east-2a</Name>
            <SupportedPlatforms>
              <SupportedPlatform>
                <Name>VPC</Name>
              </SupportedPlatform>
            </SupportedPlatforms>
          </AvailabilityZone>
          <AvailabilityZone>
            <Name>us-east-2b</Name>
            <SupportedPlatforms>
              <SupportedPlatform>
                <Name>VPC</Name>
              </SupportedPlatform>
            </SupportedPlatforms>
          </AvailabilityZone>
          <AvailabilityZone>
            <Name>us-east-2c</Name>
            <SupportedPlatforms>
              <SupportedPlatform>
                <Name>VPC</Name>
              </SupportedPlatform>
            </SupportedPlatforms>
          </AvailabilityZone>
          <AvailabilityZone>
            <Name>us-east-2f</Name>
            <SupportedPlatforms>
              <SupportedPlatform>
                <Name>VPC</Name>
              </SupportedPlatform>
            </SupportedPlatforms>
          </AvailabilityZone>
        </AvailabilityZones>
        <NodeType>ra3.16xlarge</NodeType>
        <ClusterVersion>1.0</ClusterVersion>
      </OrderableClusterOption>
    </OrderableClusterOptions>
  </DescribeOrderableClusterOptionsResult>
  <ResponseMetadata>
    <RequestId>28e69ca9-28cd-11ea-8a28-2fd1719d0e86</RequestId>
  </ResponseMetadata>
</DescribeOrderableClusterOptionsResponse>
```

## See Also
<a name="API_DescribeOrderableClusterOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/DescribeOrderableClusterOptions) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/DescribeOrderableClusterOptions) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/DescribeOrderableClusterOptions) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/DescribeOrderableClusterOptions) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/DescribeOrderableClusterOptions) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/DescribeOrderableClusterOptions) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/DescribeOrderableClusterOptions) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/DescribeOrderableClusterOptions) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/DescribeOrderableClusterOptions) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/DescribeOrderableClusterOptions) 