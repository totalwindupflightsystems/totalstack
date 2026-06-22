---
id: "@specs/aws/redshift/docs/API_AuthorizeDataShare"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AuthorizeDataShare"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# AuthorizeDataShare

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_AuthorizeDataShare
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AuthorizeDataShare
<a name="API_AuthorizeDataShare"></a>

From a data producer account, authorizes the sharing of a datashare with one or more consumer accounts or managing entities. To authorize a datashare for a data consumer, the producer account must have the correct access permissions.

## Request Parameters
<a name="API_AuthorizeDataShare_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ConsumerIdentifier **   
The identifier of the data consumer that is authorized to access the datashare. This identifier is an AWS account ID or a keyword, such as ADX.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

 ** DataShareArn **   
The Amazon Resource Name (ARN) of the datashare namespace that producers are to authorize sharing for.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

 ** AllowWrites **   
If set to true, allows write operations for a datashare.  
Type: Boolean  
Required: No

## Response Elements
<a name="API_AuthorizeDataShare_ResponseElements"></a>

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
<a name="API_AuthorizeDataShare_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidDataShareFault **   
There is an error with the datashare.  
HTTP Status Code: 400

## Examples
<a name="API_AuthorizeDataShare_Examples"></a>

### Example
<a name="API_AuthorizeDataShare_Example_1"></a>

This example illustrates one usage of AuthorizeDataShare.

#### Sample Request
<a name="API_AuthorizeDataShare_Example_1_Request"></a>

```
https://redshift.us-east-2.amazonaws.com/
        ?Action=AuthorizeDataShare
        &ConsumerIdentifier=275247490162
        &DataShareArn=arn%3Aaws%3Aredshift%3Aus-east-1%3A827630067164%3Adatashare%3Aaf06285e-8a45-4ee9-b598-648c218c8ff1%2Ftestshare2
        &SignatureMethod=HmacSHA256&SignatureVersion=4
        &Version=2012-12-01
        &X-Amz-Algorithm=AWS4-HMAC-SHA256
        &X-Amz-Credential=AKIAIOSFODNN7EXAMPLE/20190817/us-east-2/redshift/aws4_request
        &X-Amz-Date=20190825T160000Z
        &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
        &X-Amz-Signature=0aa1234bb5cc678ddddd901ee2ff3aa45678b90c12d345e6ff789012345a6b7b
```

#### Sample Response
<a name="API_AuthorizeDataShare_Example_1_Response"></a>

```
<AuthorizeDataShareResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">
            <AuthorizeDataShareResult>
                <AllowPubliclyAccessibleConsumers>false</AllowPubliclyAccessibleConsumers>
                <ProducerNamespaceArn>arn:aws:redshift:us-east-1:827630067164:namespace:af06285e-8a45-4ee9-b598-648c218c8ff1</ProducerNamespaceArn>
                <DataShareArn>arn:aws:redshift:us-east-1:827630067164:datashare:af06285e-8a45-4ee9-b598-648c218c8ff1/testshare2</DataShareArn>
                <DataShareAssociations>
                    <member>
                        <ConsumerIdentifier>275247490162</ConsumerIdentifier>
                        <StatusChangeDate>2020-10-30T17:39:04.021910</StatusChangeDate>
                        <CreatedDate>2020-10-29T22:31:53.495665</CreatedDate>
                        <Status>PENDING_ACCEPTANCE</Status>
                    </member>
                </DataShareAssociations>
            </AuthorizeDataShareResult>
            <ResponseMetadata>
                <RequestId>7c915a04-fe35-4be1-b71d-363efaa95a08</RequestId>
            </ResponseMetadata>
        </AuthorizeDataShareResponse>
```

## See Also
<a name="API_AuthorizeDataShare_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/AuthorizeDataShare) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/AuthorizeDataShare) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/AuthorizeDataShare) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/AuthorizeDataShare) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/AuthorizeDataShare) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/AuthorizeDataShare) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/AuthorizeDataShare) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/AuthorizeDataShare) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/AuthorizeDataShare) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/AuthorizeDataShare) 