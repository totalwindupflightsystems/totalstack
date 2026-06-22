---
id: "@specs/aws/redshift/docs/API_DescribeDataShares"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeDataShares"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# DescribeDataShares

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_DescribeDataShares
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeDataShares
<a name="API_DescribeDataShares"></a>

Shows the status of any inbound or outbound datashares available in the specified account.

## Request Parameters
<a name="API_DescribeDataShares_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DataShareArn **   
The Amazon resource name (ARN) of the datashare to describe details of.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** Marker **   
An optional parameter that specifies the starting point to return a set of response records. When the results of a [DescribeDataShares](#API_DescribeDataShares) request exceed the value specified in `MaxRecords`, AWS returns a value in the `Marker` field of the response. You can retrieve the next set of response records by providing the returned marker value in the `Marker` parameter and retrying the request.   
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** MaxRecords **   
The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified `MaxRecords` value, a value is returned in a `marker` field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.   
Type: Integer  
Required: No

## Response Elements
<a name="API_DescribeDataShares_ResponseElements"></a>

The following elements are returned by the service.

 **DataShares.member.N**   
The results returned from describing datashares.  
Type: Array of [DataShare](API_DataShare.md) objects

 ** Marker **   
An optional parameter that specifies the starting point to return a set of response records. When the results of a [DescribeDataShares](#API_DescribeDataShares) request exceed the value specified in `MaxRecords`, AWS returns a value in the `Marker` field of the response. You can retrieve the next set of response records by providing the returned marker value in the `Marker` parameter and retrying the request.   
Type: String  
Length Constraints: Maximum length of 2147483647.

## Errors
<a name="API_DescribeDataShares_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidDataShareFault **   
There is an error with the datashare.  
HTTP Status Code: 400

## Examples
<a name="API_DescribeDataShares_Examples"></a>

### Example
<a name="API_DescribeDataShares_Example_1"></a>

This example illustrates one usage of DescribeDataShares.

#### Sample Request
<a name="API_DescribeDataShares_Example_1_Request"></a>

```
https://redshift.us-east-2.amazonaws.com/
        ?Action=DescribeDataShares
        &NamespaceArn=arn%3Aaws%3Aredshift%3Aus-east-2%3A827630067164%3Adatashare%3Aaf06285e-8a45-4ee9-b598-648c218c8ff1
        &DataShareRelationship=PRODUCER
        &SignatureMethod=HmacSHA256&SignatureVersion=4
        &Version=2012-12-01
        &X-Amz-Algorithm=AWS4-HMAC-SHA256
        &X-Amz-Credential=AKIAIOSFODNN7EXAMPLE/20190817/us-east-2/redshift/aws4_request
        &X-Amz-Date=20190825T160000Z
        &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
        &X-Amz-Signature=0aa1234bb5cc678ddddd901ee2ff3aa45678b90c12d345e6ff789012345a6b7b
```

#### Sample Response
<a name="API_DescribeDataShares_Example_1_Response"></a>

```
<DescribeDataSharesResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">
            <DescribeDataSharesResult>
                <DataShares>
                    <member>
                        <ProducerNamespaceArn>arn:aws:redshift:us-east-1:275247490162:namespace:fd59653e-4ace-4952-a102-286dad7263ca</ProducerNamespaceArn>
                        <AllowPubliclyAccessibleConsumers>true</AllowPubliclyAccessibleConsumers>
                        <DataShareArn>arn:aws:redshift:us-east-1:275247490162:datashare:fd59653e-4ace-4952-a102-286dad7263ca/testshare2</DataShareArn>
                        <DataShareAssociations>
                            <member>
                                <StatusChangeDate>2020-10-29T22:55:58.971101</StatusChangeDate>
                                <ConsumerIdentifier>827630067164</ConsumerIdentifier>
                                <CreatedDate>2020-10-29T22:54:34.187829</CreatedDate>
                                <Status>PENDING_ACCEPTANCE</Status>
                            </member>
                        </DataShareAssociations>
                    </member>
                    <member>
                        <ProducerNamespaceArn>arn:aws:redshift:us-east-1:275247490162:namespace:fd59653e-4ace-4952-a102-286dad7263ca</ProducerNamespaceArn>
                        <AllowPubliclyAccessibleConsumers>=>true</AllowPubliclyAccessibleConsumers>
                        <DataShareArn>arn:aws:redshift:us-east-1:275247490162:datashare:fd59653e-4ace-4952-a102-286dad7263ca/testshare</DataShareArn>
                        <DataShareAssociations>
                            <member>
                                <StatusChangeDate>2020-10-30T16:05:51.137152</StatusChangeDate>
                                <ConsumerIdentifier>827630067164</ConsumerIdentifier>
                                <CreatedDate>2020-10-29T22:51:42.639841</CreatedDate>
                                <Status>ACTIVE</Status>
                            </member>
                        </DataShareAssociations>
                    </member>
                    <member>
                        <ProducerNamespaceArn>arn:aws:redshift:us-east-1:275247490162:namespace:fd59653e-4ace-4952-a102-286dad7263ca</ProducerNamespaceArn>
                        <AllowPubliclyAccessibleConsumers>true</AllowPubliclyAccessibleConsumers>
                        <DataShareArn>arn:aws:redshift:us-east-1:275247490162:datashare:fd59653e-4ace-4952-a102-286dad7263ca/testshare1</DataShareArn>
                        <DataShareAssociations>
                            <member>
                                <StatusChangeDate>2020-10-30T17:43:02.108138</StatusChangeDate>
                                <ConsumerIdentifier<827630067164</ConsumerIdentifier>
                                <CreatedDate>2020-10-29T22:54:27.948849</CreatedDate>
                                <Status>ACTIVE</Status>
                            </member>
                        </DataShareAssociations>
                    </member>
                </DataShares>
            </DescribeDataSharesResult>
            <ResponseMetadata>
                <RequestId>1acb9710-0880-4703-9fd7-60863b5c7ddc</RequestId>
            <ResponseMetadata>
        </DescribeDataSharesResponse>
```

## See Also
<a name="API_DescribeDataShares_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/DescribeDataShares) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/DescribeDataShares) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/DescribeDataShares) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/DescribeDataShares) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/DescribeDataShares) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/DescribeDataShares) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/DescribeDataShares) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/DescribeDataShares) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/DescribeDataShares) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/DescribeDataShares) 