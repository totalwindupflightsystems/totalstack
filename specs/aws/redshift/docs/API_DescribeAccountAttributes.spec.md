---
id: "@specs/aws/redshift/docs/API_DescribeAccountAttributes"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeAccountAttributes"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# DescribeAccountAttributes

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_DescribeAccountAttributes
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeAccountAttributes
<a name="API_DescribeAccountAttributes"></a>

Returns a list of attributes attached to an account

## Request Parameters
<a name="API_DescribeAccountAttributes_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **AttributeNames.AttributeName.N**   
A list of attribute names.  
Type: Array of strings  
Length Constraints: Maximum length of 2147483647.  
Required: No

## Response Elements
<a name="API_DescribeAccountAttributes_ResponseElements"></a>

The following element is returned by the service.

 **AccountAttributes.AccountAttribute.N**   
A list of attributes assigned to an account.  
Type: Array of [AccountAttribute](API_AccountAttribute.md) objects

## Errors
<a name="API_DescribeAccountAttributes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeAccountAttributes_Examples"></a>

### Example
<a name="API_DescribeAccountAttributes_Example_1"></a>

This example illustrates one usage of DescribeAccountAttributes.

#### Sample Request
<a name="API_DescribeAccountAttributes_Example_1_Request"></a>

```
https://redshift.us-east-2.amazonaws.com/
       ?Action=DescribeAccountAttributes
&SignatureMethod=HmacSHA256&SignatureVersion=4
&Version=2012-12-01
&X-Amz-Algorithm=AWS4-HMAC-SHA256
&X-Amz-Credential=AKIAIOSFODNN7EXAMPLE/20190817/us-east-2/redshift/aws4_request
&X-Amz-Date=20190825T160000Z
&X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
&X-Amz-Signature=0aa1234bb5cc678ddddd901ee2ff3aa45678b90c12d345e6ff789012345a6b7b
```

#### Sample Response
<a name="API_DescribeAccountAttributes_Example_1_Response"></a>

```
<DescribeAccountAttributesResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">
  <DescribeAccountAttributesResult>
    <AccountAttributes>
      <AccountAttribute>
        <AttributeValues>
          <AttributeValueTarget>
            <AttributeValue>45</AttributeValue>
          </AttributeValueTarget>
        </AttributeValues>
        <AttributeName>max-defer-maintenance-duration</AttributeName>
      </AccountAttribute>
    </AccountAttributes>
  </DescribeAccountAttributesResult>
  <ResponseMetadata>
    <RequestId>fbb48802-283d-11ea-9467-b9a67a99da45</RequestId>
  </ResponseMetadata>
</DescribeAccountAttributesResponse>
```

## See Also
<a name="API_DescribeAccountAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/DescribeAccountAttributes) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/DescribeAccountAttributes) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/DescribeAccountAttributes) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/DescribeAccountAttributes) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/DescribeAccountAttributes) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/DescribeAccountAttributes) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/DescribeAccountAttributes) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/DescribeAccountAttributes) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/DescribeAccountAttributes) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/DescribeAccountAttributes) 