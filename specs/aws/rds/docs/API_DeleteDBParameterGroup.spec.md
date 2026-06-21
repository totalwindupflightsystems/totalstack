---
id: "@specs/aws/rds/docs/API_DeleteDBParameterGroup"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteDBParameterGroup"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# DeleteDBParameterGroup

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_DeleteDBParameterGroup
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteDBParameterGroup
<a name="API_DeleteDBParameterGroup"></a>

Deletes a specified DB parameter group. The DB parameter group to be deleted can't be associated with any DB instances.

## Request Parameters
<a name="API_DeleteDBParameterGroup_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBParameterGroupName **   
The name of the DB parameter group.  
Constraints:  
+ Must be the name of an existing DB parameter group
+ You can't delete a default DB parameter group
+ Can't be associated with any DB instances
Type: String  
Required: Yes

## Errors
<a name="API_DeleteDBParameterGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBParameterGroupNotFound **   
 `DBParameterGroupName` doesn't refer to an existing DB parameter group.  
HTTP Status Code: 404

 ** InvalidDBParameterGroupState **   
The DB parameter group is in use or is in an invalid state. If you are attempting to delete the parameter group, you can't delete it when the parameter group is in this state.  
HTTP Status Code: 400

## Examples
<a name="API_DeleteDBParameterGroup_Examples"></a>

### Example
<a name="API_DeleteDBParameterGroup_Example_1"></a>

This example illustrates one usage of DeleteDBParameterGroup.

#### Sample Request
<a name="API_DeleteDBParameterGroup_Example_1_Request"></a>

```
https://rds.us-east-1.amazonaws.com/
   ?Action=DeleteDBParameterGroup
   &DBParameterGroupName=mydbparamgroup3
   &SignatureMethod=HmacSHA256
   &SignatureVersion=4
   &Version=2014-10-31
   &X-Amz-Algorithm=AWS4-HMAC-SHA256
   &X-Amz-Credential=AKIADQKE4SARGYLE/20140423/us-east-1/rds/aws4_request
   &X-Amz-Date=20140423T203550Z
   &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
   &X-Amz-Signature=7364d4d88b4200d14da46aac748781a6da08bc18c5fdc468ee18780e6f84b19e
```

#### Sample Response
<a name="API_DeleteDBParameterGroup_Example_1_Response"></a>

```
<DeleteDBParameterGroupResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/">
  <ResponseMetadata>
    <RequestId>cad6c267-ba25-11d3-fe11-33d33a9bb7e3</RequestId>
  </ResponseMetadata>
</DeleteDBParameterGroupResponse>
```

## See Also
<a name="API_DeleteDBParameterGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/DeleteDBParameterGroup) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/DeleteDBParameterGroup) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DeleteDBParameterGroup) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/DeleteDBParameterGroup) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DeleteDBParameterGroup) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/DeleteDBParameterGroup) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/DeleteDBParameterGroup) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/DeleteDBParameterGroup) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/DeleteDBParameterGroup) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DeleteDBParameterGroup) 