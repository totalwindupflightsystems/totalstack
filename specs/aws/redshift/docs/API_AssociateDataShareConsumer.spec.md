---
id: "@specs/aws/redshift/docs/API_AssociateDataShareConsumer"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AssociateDataShareConsumer"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# AssociateDataShareConsumer

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_AssociateDataShareConsumer
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AssociateDataShareConsumer
<a name="API_AssociateDataShareConsumer"></a>

From a datashare consumer account, associates a datashare with the account (AssociateEntireAccount) or the specified namespace (ConsumerArn). If you make this association, the consumer can consume the datashare.

## Request Parameters
<a name="API_AssociateDataShareConsumer_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DataShareArn **   
The Amazon Resource Name (ARN) of the datashare that the consumer is to use.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

 ** AllowWrites **   
If set to true, allows write operations for a datashare.  
Type: Boolean  
Required: No

 ** AssociateEntireAccount **   
A value that specifies whether the datashare is associated with the entire account.  
Type: Boolean  
Required: No

 ** ConsumerArn **   
The Amazon Resource Name (ARN) of the consumer namespace associated with the datashare.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** ConsumerRegion **   
From a datashare consumer account, associates a datashare with all existing and future namespaces in the specified AWS Region.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

## Response Elements
<a name="API_AssociateDataShareConsumer_ResponseElements"></a>

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
<a name="API_AssociateDataShareConsumer_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidDataShareFault **   
There is an error with the datashare.  
HTTP Status Code: 400

 ** InvalidNamespaceFault **   
The namespace isn't valid because the namespace doesn't exist. Provide a valid namespace.  
HTTP Status Code: 400

## Examples
<a name="API_AssociateDataShareConsumer_Examples"></a>

### Example
<a name="API_AssociateDataShareConsumer_Example_1"></a>

This example illustrates one usage of AssociateDataShareConsumer.

#### Sample Request
<a name="API_AssociateDataShareConsumer_Example_1_Request"></a>

```
AssociateDataShareConsumer&AssociateEntireAccount=true&DataShareArn=arn%3Aaws%3Aredshift%3Aus-east-1%3A827630067164%3Adatashare%3Aa1c54ed4-8323-4d14-b5dd-927cb596dc0e%2Ftestshare&Version=2012-12-01
```

#### Sample Response
<a name="API_AssociateDataShareConsumer_Example_1_Response"></a>

```
<AssociateDataShareConsumerResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">
  <AssociateDataShareConsumerResult>
    <ProducerNamespaceArn>arn:aws:redshift:us-east-1:827630067164:namespace:a1c54ed4-8323-4d14-b5dd-927cb596dc0e</ProducerNamespaceArn>
    <AllowPubliclyAccessibleConsumers>false</AllowPubliclyAccessibleConsumers>
    <DataShareArn>arn:aws:redshift:us-east-1:827630067164:datashare:a1c54ed4-8323-4d14-b5dd-927cb596dc0e/testshare</DataShareArn>
    <DataShareAssociations>
      <member>
        <StatusChangeDate>2021-01-11T23:39:25.485605</StatusChangeDate>
        <ConsumerIdentifier>827630067164</ConsumerIdentifier>
        <CreatedDate>2021-01-11T22:12:23.038612</CreatedDate>
        <Status>ACTIVE</Status>
      </member>
    </DataShareAssociations>
  </AssociateDataShareConsumerResult>
  <ResponseMetadata>
    <RequestId>c125d0e3-72de-4938-a919-e6a0c3f8489d</RequestId>
  </ResponseMetadata>
</AssociateDataShareConsumerResponse>
```

## See Also
<a name="API_AssociateDataShareConsumer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/AssociateDataShareConsumer) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/AssociateDataShareConsumer) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/AssociateDataShareConsumer) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/AssociateDataShareConsumer) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/AssociateDataShareConsumer) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/AssociateDataShareConsumer) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/AssociateDataShareConsumer) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/AssociateDataShareConsumer) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/AssociateDataShareConsumer) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/AssociateDataShareConsumer) 