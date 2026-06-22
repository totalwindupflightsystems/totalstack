---
id: "@specs/aws/redshift/docs/API_DeleteScheduledAction"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteScheduledAction"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# DeleteScheduledAction

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_DeleteScheduledAction
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteScheduledAction
<a name="API_DeleteScheduledAction"></a>

Deletes a scheduled action. 

## Request Parameters
<a name="API_DeleteScheduledAction_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ScheduledActionName **   
The name of the scheduled action to delete.   
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

## Errors
<a name="API_DeleteScheduledAction_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ScheduledActionNotFound **   
The scheduled action cannot be found.   
HTTP Status Code: 400

 ** UnauthorizedOperation **   
Your account is not authorized to perform the requested operation.  
HTTP Status Code: 400

## Examples
<a name="API_DeleteScheduledAction_Examples"></a>

### Example
<a name="API_DeleteScheduledAction_Example_1"></a>

This example illustrates one usage of DeleteScheduledAction.

#### Sample Request
<a name="API_DeleteScheduledAction_Example_1_Request"></a>

```
https://redshift.us-east-2.amazonaws.com/
       ?Action=DeleteScheduledAction
&ScheduledActionName=myscheduledaction
&SignatureMethod=HmacSHA256&SignatureVersion=4
&Version=2012-12-01
&X-Amz-Algorithm=AWS4-HMAC-SHA256
&X-Amz-Credential=AKIAIOSFODNN7EXAMPLE/20190817/us-east-2/redshift/aws4_request
&X-Amz-Date=20190825T160000Z
&X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
&X-Amz-Signature=0aa1234bb5cc678ddddd901ee2ff3aa45678b90c12d345e6ff789012345a6b7b
```

#### Sample Response
<a name="API_DeleteScheduledAction_Example_1_Response"></a>

```
<DeleteScheduledActionResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">
  <ResponseMetadata>
    <RequestId>2c20099c-283b-11ea-9caa-c956bec1ce87</RequestId>
  </ResponseMetadata>
</DeleteScheduledActionResponse>
```

## See Also
<a name="API_DeleteScheduledAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/DeleteScheduledAction) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/DeleteScheduledAction) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/DeleteScheduledAction) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/DeleteScheduledAction) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/DeleteScheduledAction) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/DeleteScheduledAction) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/DeleteScheduledAction) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/DeleteScheduledAction) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/DeleteScheduledAction) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/DeleteScheduledAction) 