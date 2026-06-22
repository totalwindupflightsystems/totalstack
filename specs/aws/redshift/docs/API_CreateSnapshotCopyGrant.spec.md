---
id: "@specs/aws/redshift/docs/API_CreateSnapshotCopyGrant"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateSnapshotCopyGrant"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# CreateSnapshotCopyGrant

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_CreateSnapshotCopyGrant
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateSnapshotCopyGrant
<a name="API_CreateSnapshotCopyGrant"></a>

Creates a snapshot copy grant that permits Amazon Redshift to use an encrypted symmetric key from AWS Key Management Service (KMS) to encrypt copied snapshots in a destination region.

 For more information about managing snapshot copy grants, go to [Amazon Redshift Database Encryption](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-db-encryption.html) in the *Amazon Redshift Cluster Management Guide*. 

## Request Parameters
<a name="API_CreateSnapshotCopyGrant_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** SnapshotCopyGrantName **   
The name of the snapshot copy grant. This name must be unique in the region for the AWS account.  
Constraints:  
+ Must contain from 1 to 63 alphanumeric characters or hyphens.
+ Alphabetic characters must be lowercase.
+ First character must be a letter.
+ Cannot end with a hyphen or contain two consecutive hyphens.
+ Must be unique for all clusters within an AWS account.
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

 ** KmsKeyId **   
The unique identifier of the encrypted symmetric key to which to grant Amazon Redshift permission. If no key is specified, the default key is used.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 **Tags.Tag.N**   
A list of tag instances.  
Type: Array of [Tag](API_Tag.md) objects  
Required: No

## Response Elements
<a name="API_CreateSnapshotCopyGrant_ResponseElements"></a>

The following element is returned by the service.

 ** SnapshotCopyGrant **   
The snapshot copy grant that grants Amazon Redshift permission to encrypt copied snapshots with the specified encrypted symmetric key from AWS KMS in the destination region.  
 For more information about managing snapshot copy grants, go to [Amazon Redshift Database Encryption](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-db-encryption.html) in the *Amazon Redshift Cluster Management Guide*.   
Type: [SnapshotCopyGrant](API_SnapshotCopyGrant.md) object

## Errors
<a name="API_CreateSnapshotCopyGrant_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DependentServiceRequestThrottlingFault **   
The request cannot be completed because a dependent service is throttling requests made by Amazon Redshift on your behalf. Wait and retry the request.  
HTTP Status Code: 400

 ** InvalidTagFault **   
The tag is invalid.  
HTTP Status Code: 400

 ** LimitExceededFault **   
The encryption key has exceeded its grant limit in AWS KMS.  
HTTP Status Code: 400

 ** SnapshotCopyGrantAlreadyExistsFault **   
The snapshot copy grant can't be created because a grant with the same name already exists.  
HTTP Status Code: 400

 ** SnapshotCopyGrantQuotaExceededFault **   
The AWS account has exceeded the maximum number of snapshot copy grants in this region.  
HTTP Status Code: 400

 ** TagLimitExceededFault **   
You have exceeded the number of tags allowed.  
HTTP Status Code: 400

## Examples
<a name="API_CreateSnapshotCopyGrant_Examples"></a>

### Example
<a name="API_CreateSnapshotCopyGrant_Example_1"></a>

This example illustrates one usage of CreateSnapshotCopyGrant.

#### Sample Request
<a name="API_CreateSnapshotCopyGrant_Example_1_Request"></a>

```
https://redshift.us-east-2.amazonaws.com/
       ?Action=CreateSnapshotCopyGrant
&SnapshotCopyGrantName=mysnapshotcopygrantnew
&SignatureMethod=HmacSHA256&SignatureVersion=4
&Version=2012-12-01
&X-Amz-Algorithm=AWS4-HMAC-SHA256
&X-Amz-Credential=AKIAIOSFODNN7EXAMPLE/20190817/us-east-2/redshift/aws4_request
&X-Amz-Date=20190825T160000Z
&X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
&X-Amz-Signature=0aa1234bb5cc678ddddd901ee2ff3aa45678b90c12d345e6ff789012345a6b7b
```

#### Sample Response
<a name="API_CreateSnapshotCopyGrant_Example_1_Response"></a>

```
<CreateSnapshotCopyGrantResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">
  <CreateSnapshotCopyGrantResult>
    <SnapshotCopyGrant>
      <SnapshotCopyGrantName>mysnapshotcopygrantnew</SnapshotCopyGrantName>
      <KmsKeyId>arn:aws:kms:us-east-2:123456789012:key/bPxRfih3yCo8nvbEXAMPLEKEY</KmsKeyId>
      <Tags/>
    </SnapshotCopyGrant>
  </CreateSnapshotCopyGrantResult>
  <ResponseMetadata>
    <RequestId>085f3206-2837-11ea-9939-5fccefa818c0</RequestId>
  </ResponseMetadata>
</CreateSnapshotCopyGrantResponse>
```

## See Also
<a name="API_CreateSnapshotCopyGrant_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/CreateSnapshotCopyGrant) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/CreateSnapshotCopyGrant) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/CreateSnapshotCopyGrant) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/CreateSnapshotCopyGrant) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/CreateSnapshotCopyGrant) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/CreateSnapshotCopyGrant) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/CreateSnapshotCopyGrant) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/CreateSnapshotCopyGrant) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/CreateSnapshotCopyGrant) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/CreateSnapshotCopyGrant) 