---
id: "@specs/aws/redshift/docs/API_DisassociateDataShareConsumer"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DisassociateDataShareConsumer"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# DisassociateDataShareConsumer

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_DisassociateDataShareConsumer
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DisassociateDataShareConsumer
<a name="API_DisassociateDataShareConsumer"></a>

From a datashare consumer account, remove association for the specified datashare. 

## Request Parameters
<a name="API_DisassociateDataShareConsumer_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DataShareArn **   
The Amazon Resource Name (ARN) of the datashare to remove association for.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

 ** ConsumerArn **   
The Amazon Resource Name (ARN) of the consumer namespace that association for the datashare is removed from.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** ConsumerRegion **   
From a datashare consumer account, removes association of a datashare from all the existing and future namespaces in the specified AWS Region.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** DisassociateEntireAccount **   
A value that specifies whether association for the datashare is removed from the entire account.  
Type: Boolean  
Required: No

## Response Elements
<a name="API_DisassociateDataShareConsumer_ResponseElements"></a>

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
<a name="API_DisassociateDataShareConsumer_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidDataShareFault **   
There is an error with the datashare.  
HTTP Status Code: 400

 ** InvalidNamespaceFault **   
The namespace isn't valid because the namespace doesn't exist. Provide a valid namespace.  
HTTP Status Code: 400

## Examples
<a name="API_DisassociateDataShareConsumer_Examples"></a>

### Example
<a name="API_DisassociateDataShareConsumer_Example_1"></a>

This example illustrates one usage of DisassociateDataShareConsumer.

#### Sample Request
<a name="API_DisassociateDataShareConsumer_Example_1_Request"></a>

```
https://redshift.us-east-2.amazonaws.com/
    ?Action=DisassociateDataShareConsumer
    &DataShareArn=arn%3Aaws%3Aredshift%3Aus-east-1%3A275247490162%3Adatashare%3Afd59653e-4ace-4952-a102-286dad7263ca%2Ftestshare1
    &ConsumerArn=arn%3Aaws%3Aredshift%3Aus-east-1%3A275247490162%3Anamespace%3A57beacb3-2f8a-4c22-a3e3-d2d73da7ee6a
    &DisassociateEntireAccount=false
    &SignatureMethod=HmacSHA256&SignatureVersion=4
    &Version=2012-12-01
    &X-Amz-Algorithm=AWS4-HMAC-SHA256
    &X-Amz-Credential=AKIAIOSFODNN7EXAMPLE/20190817/us-east-2/redshift/aws4_request
    &X-Amz-Date=20190825T160000Z
    &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
    &X-Amz-Signature=0aa1234bb5cc678ddddd901ee2ff3aa45678b90c12d345e6ff789012345a6b7b
```

#### Sample Response
<a name="API_DisassociateDataShareConsumer_Example_1_Response"></a>

```
<DisassociateDataShareConsumerResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">
  <DisassociateDataShareConsumerResult>
    <ProducerNamespaceArn>arn:aws:redshift:us-east-1:827630067164:namespace:73ff3b6a-0fab-4122-8ba4-c6613d707a6e</ProducerNamespaceArn>
    <AllowPubliclyAccessibleConsumers>true</AllowPubliclyAccessibleConsumers>
    <DataShareArn>arn:aws:redshift:us-east-1:827630067164:datashare:73ff3b6a-0fab-4122-8ba4-c6613d707a6e/share_data</DataShareArn>
    <DataShareAssociations/>
  </DisassociateDataShareConsumerResult>
  <ResponseMetadata>
    <RequestId>183c52e9-ba40-472c-9b31-66bfd7b20d88</RequestId>
  </ResponseMetadata>
</DisassociateDataShareConsumerResponse>
```

## See Also
<a name="API_DisassociateDataShareConsumer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/DisassociateDataShareConsumer) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/DisassociateDataShareConsumer) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/DisassociateDataShareConsumer) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/DisassociateDataShareConsumer) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/DisassociateDataShareConsumer) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/DisassociateDataShareConsumer) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/DisassociateDataShareConsumer) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/DisassociateDataShareConsumer) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/DisassociateDataShareConsumer) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/DisassociateDataShareConsumer) 