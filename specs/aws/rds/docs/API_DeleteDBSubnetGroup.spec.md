---
id: "@specs/aws/rds/docs/API_DeleteDBSubnetGroup"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteDBSubnetGroup"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# DeleteDBSubnetGroup

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_DeleteDBSubnetGroup
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteDBSubnetGroup
<a name="API_DeleteDBSubnetGroup"></a>

Deletes a DB subnet group.

**Note**  
The specified database subnet group must not be associated with any DB instances.

## Request Parameters
<a name="API_DeleteDBSubnetGroup_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBSubnetGroupName **   
The name of the database subnet group to delete.  
You can't delete the default subnet group.
Constraints: Must match the name of an existing DBSubnetGroup. Must not be default.  
Example: `mydbsubnetgroup`   
Type: String  
Required: Yes

## Errors
<a name="API_DeleteDBSubnetGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBSubnetGroupNotFoundFault **   
 `DBSubnetGroupName` doesn't refer to an existing DB subnet group.  
HTTP Status Code: 404

 ** InvalidDBSubnetGroupStateFault **   
The DB subnet group cannot be deleted because it's in use.  
HTTP Status Code: 400

 ** InvalidDBSubnetStateFault **   
The DB subnet isn't in the *available* state.  
HTTP Status Code: 400

## Examples
<a name="API_DeleteDBSubnetGroup_Examples"></a>

### Example
<a name="API_DeleteDBSubnetGroup_Example_1"></a>

This example illustrates one usage of DeleteDBSubnetGroup.

#### Sample Request
<a name="API_DeleteDBSubnetGroup_Example_1_Request"></a>

```
https://rds.us-east-1.amazonaws.com/
   ?Action=DeleteDBSubnetGroup
   &DBSubnetGroupName=myawsuser-dbsubnetgroup
   &SignatureMethod=HmacSHA256
   &SignatureVersion=4
   &Version=2014-10-31
   &X-Amz-Algorithm=AWS4-HMAC-SHA256
   &X-Amz-Credential=AKIADQKE4SARGYLE/20140425/us-east-1/rds/aws4_request
   &X-Amz-Date=20140425T180721Z
   &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
   &X-Amz-Signature=0f461da21ec03527fdc98acba8a11c36863a399065f9b4ff891ab7cb5e70de74
```

#### Sample Response
<a name="API_DeleteDBSubnetGroup_Example_1_Response"></a>

```
<DeleteDBSubnetGroupResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/">
  <ResponseMetadata>
    <RequestId>6295e5ab-bbf3-11d3-f4c6-37db295f7674</RequestId>
  </ResponseMetadata>
</DeleteDBSubnetGroupResponse>
```

## See Also
<a name="API_DeleteDBSubnetGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/DeleteDBSubnetGroup) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/DeleteDBSubnetGroup) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DeleteDBSubnetGroup) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/DeleteDBSubnetGroup) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DeleteDBSubnetGroup) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/DeleteDBSubnetGroup) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/DeleteDBSubnetGroup) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/DeleteDBSubnetGroup) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/DeleteDBSubnetGroup) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DeleteDBSubnetGroup) 