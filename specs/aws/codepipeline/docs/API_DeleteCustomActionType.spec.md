---
id: "@specs/aws/codepipeline/docs/API_DeleteCustomActionType"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteCustomActionType"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# DeleteCustomActionType

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_DeleteCustomActionType
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteCustomActionType
<a name="API_DeleteCustomActionType"></a>

Marks a custom action as deleted. `PollForJobs` for the custom action fails after the action is marked for deletion. Used for custom actions only.

**Important**  
To re-create a custom action after it has been deleted you must use a string in the version field that has never been used before. This string can be an incremented version number, for example. To restore a deleted custom action, use a JSON file that is identical to the deleted action, including the original string in the version field.

## Request Syntax
<a name="API_DeleteCustomActionType_RequestSyntax"></a>

```
{
   "category": "{{string}}",
   "provider": "{{string}}",
   "version": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteCustomActionType_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [category](#API_DeleteCustomActionType_RequestSyntax) **   <a name="CodePipeline-DeleteCustomActionType-request-category"></a>
The category of the custom action that you want to delete, such as source or deploy.  
Type: String  
Valid Values: `Source | Build | Deploy | Test | Invoke | Approval | Compute`   
Required: Yes

 ** [provider](#API_DeleteCustomActionType_RequestSyntax) **   <a name="CodePipeline-DeleteCustomActionType-request-provider"></a>
The provider of the service used in the custom action, such as CodeDeploy.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 35.  
Pattern: `[0-9A-Za-z_-]+`   
Required: Yes

 ** [version](#API_DeleteCustomActionType_RequestSyntax) **   <a name="CodePipeline-DeleteCustomActionType-request-version"></a>
The version of the custom action to delete.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 9.  
Pattern: `[0-9A-Za-z_-]+`   
Required: Yes

## Response Elements
<a name="API_DeleteCustomActionType_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteCustomActionType_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConcurrentModificationException **   
Unable to modify the tag due to a simultaneous update request.  
HTTP Status Code: 400

 ** ValidationException **   
The validation was specified in an invalid format.  
HTTP Status Code: 400

## Examples
<a name="API_DeleteCustomActionType_Examples"></a>

### Example
<a name="API_DeleteCustomActionType_Example_1"></a>

This example illustrates one usage of DeleteCustomActionType.

#### Sample Request
<a name="API_DeleteCustomActionType_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: codepipeline.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 68
X-Amz-Target: CodePipeline_20150709.DeleteCustomActionType
X-Amz-Date: 20151030T233944Z
User-Agent: aws-cli/1.7.38 Python/2.7.9 Windows/7
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAI44QH8DHBEXAMPLE/20151030/us-east-1/codepipeline/aws4_request, SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=8d9b5998EXAMPLE

{
  "category": "Build",
  "version": "1",
  "provider": "JenkinsProviderName"
}
```

#### Sample Response
<a name="API_DeleteCustomActionType_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 620484b7-88cb-11e5-b497-75c49EXAMPLE
Content-Type: application/x-amz-json-1.1
Content-Length: 0
```

## See Also
<a name="API_DeleteCustomActionType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codepipeline-2015-07-09/DeleteCustomActionType) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codepipeline-2015-07-09/DeleteCustomActionType) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/DeleteCustomActionType) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codepipeline-2015-07-09/DeleteCustomActionType) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/DeleteCustomActionType) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codepipeline-2015-07-09/DeleteCustomActionType) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codepipeline-2015-07-09/DeleteCustomActionType) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codepipeline-2015-07-09/DeleteCustomActionType) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codepipeline-2015-07-09/DeleteCustomActionType) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/DeleteCustomActionType) 