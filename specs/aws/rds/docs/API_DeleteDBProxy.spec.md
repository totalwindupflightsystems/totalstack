---
id: "@specs/aws/rds/docs/API_DeleteDBProxy"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteDBProxy"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# DeleteDBProxy

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_DeleteDBProxy
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteDBProxy
<a name="API_DeleteDBProxy"></a>

Deletes an existing DB proxy.

## Request Parameters
<a name="API_DeleteDBProxy_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBProxyName **   
The name of the DB proxy to delete.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `[a-zA-Z](?:-?[a-zA-Z0-9]+)*`   
Required: Yes

## Response Elements
<a name="API_DeleteDBProxy_ResponseElements"></a>

The following element is returned by the service.

 ** DBProxy **   
The data structure representing the details of the DB proxy that you delete.  
Type: [DBProxy](API_DBProxy.md) object

## Errors
<a name="API_DeleteDBProxy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBProxyNotFoundFault **   
The specified proxy name doesn't correspond to a proxy owned by your AWS account in the specified AWS Region.  
HTTP Status Code: 404

 ** InvalidDBProxyStateFault **   
The requested operation can't be performed while the proxy is in this state.  
HTTP Status Code: 400

## See Also
<a name="API_DeleteDBProxy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/DeleteDBProxy) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/DeleteDBProxy) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DeleteDBProxy) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/DeleteDBProxy) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DeleteDBProxy) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/DeleteDBProxy) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/DeleteDBProxy) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/DeleteDBProxy) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/DeleteDBProxy) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DeleteDBProxy) 