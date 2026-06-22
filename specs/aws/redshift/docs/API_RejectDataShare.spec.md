---
id: "@specs/aws/redshift/docs/API_RejectDataShare"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RejectDataShare"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# RejectDataShare

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_RejectDataShare
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RejectDataShare
<a name="API_RejectDataShare"></a>

From a datashare consumer account, rejects the specified datashare.

## Request Parameters
<a name="API_RejectDataShare_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DataShareArn **   
The Amazon Resource Name (ARN) of the datashare to reject.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

## Response Elements
<a name="API_RejectDataShare_ResponseElements"></a>

The following elements are returned by the service.

 ** AllowPubliclyAccessibleConsumers **   
A value that specifies whether the datashare can be shared to a publicly accessible cluster.  
Type: Boolean

 ** DataShareArn **   
The Amazon Resource Name (ARN) of the datashare that the consumer is to use.  
Type: String  
Length Constraints: Maximum length of 2147483647.

 **DataShareAssociations.member.N**   
A value that specifies when the datashare has an association between producer and data consumers.  
Type: Array of [DataShareAssociation](API_DataShareAssociation.md) objects

 ** DataShareType **   
 The type of the datashare created by RegisterNamespace.  
Type: String  
Valid Values: `INTERNAL` 

 ** ManagedBy **   
The identifier of a datashare to show its managing entity.  
Type: String  
Length Constraints: Maximum length of 2147483647.

 ** ProducerArn **   
The Amazon Resource Name (ARN) of the producer namespace.  
Type: String  
Length Constraints: Maximum length of 2147483647.

## Errors
<a name="API_RejectDataShare_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidDataShareFault **   
There is an error with the datashare.  
HTTP Status Code: 400

## Examples
<a name="API_RejectDataShare_Examples"></a>

### Example
<a name="API_RejectDataShare_Example_1"></a>

This example illustrates one usage of RejectDataShare.

#### Sample Request
<a name="API_RejectDataShare_Example_1_Request"></a>

```
https://redshift.us-east-2.amazonaws.com/
        ?Action=RejectDataShare
        &DataShareArn=arn%3Aaws%3Ar&dshift%3Aus-east-1%3A275247490162%3Adatashare%3Afd59653e-4ace-4952-a102-286dad7263ca%2Ftestshare1
        &SignatureMethod=HmacSHA256&SignatureVersion=4
        &Version=2012-12-01
        &X-Amz-Algorithm=AWS4-HMAC-SHA256
        &X-Amz-Credential=AKIAIOSFODNN7EXAMPLE/20190817/us-east-2/redshift/aws4_request
        &X-Amz-Date=20190825T160000Z
        &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
        &X-Amz-Signature=0aa1234bb5cc678ddddd901ee2ff3aa45678b90c12d345e6ff789012345a6b7b
```

#### Sample Response
<a name="API_RejectDataShare_Example_1_Response"></a>

```
<RejectDataShareResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">
            <RejectDataShareResult>
                <ProducerNamespaceArn>arn:aws:redshift:us-east-1:275247490162:namespace:fd59653e-4ace-4952-a102-286dad7263ca</ProducerNamespaceArn>
                <AllowPubliclyAccessibleConsumers>true</AllowPubliclyAccessibleConsumers>
                <DataShareArn>arn:aws:redshift:us-east-1:275247490162:datashare:fd59653e-4ace-4952-a102-286dad7263ca/testshare1</DataShareArn>
                <DataShareAssociations>
                    <member>
                        <StatusChangeDate>2020-10-30T17:43:02.108138</StatusChangeDate>
                        <ConsumerIdentifier>827630067164</ConsumerIdentifier>
                        <CreatedDate>2020-10-29T22:54:27.948849</CreatedDate>
                        <Status>REJECTED</Status>
                    </member>
                </DataShareAssociations>
            </RejectDataShareResult>
            <ResponseMetadata>
                <RequestId>fc19bc1a-18c1-4888-a35e-3e1366775c36</RequestId>
            </ResponseMetadata>
        </RejectDataShareResponse>
```

## See Also
<a name="API_RejectDataShare_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/RejectDataShare) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/RejectDataShare) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/RejectDataShare) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/RejectDataShare) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/RejectDataShare) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/RejectDataShare) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/RejectDataShare) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/RejectDataShare) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/RejectDataShare) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/RejectDataShare) 