---
id: "@specs/aws/rds/docs/API_DeleteOptionGroup"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteOptionGroup"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# DeleteOptionGroup

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_DeleteOptionGroup
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteOptionGroup
<a name="API_DeleteOptionGroup"></a>

Deletes an existing option group.

## Request Parameters
<a name="API_DeleteOptionGroup_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** OptionGroupName **   
The name of the option group to be deleted.  
You can't delete default option groups.
Type: String  
Required: Yes

## Errors
<a name="API_DeleteOptionGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidOptionGroupStateFault **   
The option group isn't in the *available* state.  
HTTP Status Code: 400

 ** OptionGroupNotFoundFault **   
The specified option group could not be found.  
HTTP Status Code: 404

## Examples
<a name="API_DeleteOptionGroup_Examples"></a>

### Example
<a name="API_DeleteOptionGroup_Example_1"></a>

This example illustrates one usage of DeleteOptionGroup.

#### Sample Request
<a name="API_DeleteOptionGroup_Example_1_Request"></a>

```
https://rds.us-east-1.amazonaws.com/
   ?Action=DeleteOptionGroup
   &OptionGroupName=myawsuser-og00
   &SignatureMethod=HmacSHA256
   &SignatureVersion=4
   &Version=2014-10-31
   &X-Amz-Algorithm=AWS4-HMAC-SHA256
   &X-Amz-Credential=AKIADQKE4SARGYLE/20140425/us-east-1/rds/aws4_request
   &X-Amz-Date=20140425T181205Z
   &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
   &X-Amz-Signature=8a684aebe6d5219bb3572316a341963324d6ef339bd0dcfa5854f1a01d401214
```

#### Sample Response
<a name="API_DeleteOptionGroup_Example_1_Response"></a>

```
<DeleteOptionGroupResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/">
  <ResponseMetadata>
    <RequestId>0ac9cda2-bbf4-11d3-f92b-31fa5e8dbc99</RequestId>
  </ResponseMetadata>
</DeleteOptionGroupResponse>
```

## See Also
<a name="API_DeleteOptionGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/DeleteOptionGroup) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/DeleteOptionGroup) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DeleteOptionGroup) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/DeleteOptionGroup) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DeleteOptionGroup) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/DeleteOptionGroup) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/DeleteOptionGroup) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/DeleteOptionGroup) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/DeleteOptionGroup) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DeleteOptionGroup) 