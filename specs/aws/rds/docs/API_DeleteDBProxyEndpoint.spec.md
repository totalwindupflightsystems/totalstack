---
id: "@specs/aws/rds/docs/API_DeleteDBProxyEndpoint"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteDBProxyEndpoint"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# DeleteDBProxyEndpoint

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_DeleteDBProxyEndpoint
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteDBProxyEndpoint
<a name="API_DeleteDBProxyEndpoint"></a>

Deletes a `DBProxyEndpoint`. Doing so removes the ability to access the DB proxy using the endpoint that you defined. The endpoint that you delete might have provided capabilities such as read/write or read-only operations, or using a different VPC than the DB proxy's default VPC.

## Request Parameters
<a name="API_DeleteDBProxyEndpoint_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBProxyEndpointName **   
The name of the DB proxy endpoint to delete.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `[a-zA-Z](?:-?[a-zA-Z0-9]+)*`   
Required: Yes

## Response Elements
<a name="API_DeleteDBProxyEndpoint_ResponseElements"></a>

The following element is returned by the service.

 ** DBProxyEndpoint **   
The data structure representing the details of the DB proxy endpoint that you delete.  
Type: [DBProxyEndpoint](API_DBProxyEndpoint.md) object

## Errors
<a name="API_DeleteDBProxyEndpoint_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBProxyEndpointNotFoundFault **   
The DB proxy endpoint doesn't exist.  
HTTP Status Code: 404

 ** InvalidDBProxyEndpointStateFault **   
You can't perform this operation while the DB proxy endpoint is in a particular state.  
HTTP Status Code: 400

## See Also
<a name="API_DeleteDBProxyEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/DeleteDBProxyEndpoint) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/DeleteDBProxyEndpoint) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DeleteDBProxyEndpoint) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/DeleteDBProxyEndpoint) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DeleteDBProxyEndpoint) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/DeleteDBProxyEndpoint) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/DeleteDBProxyEndpoint) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/DeleteDBProxyEndpoint) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/DeleteDBProxyEndpoint) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DeleteDBProxyEndpoint) 