---
id: "@specs/aws/rds/docs/API_ModifyDBProxyEndpoint"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ModifyDBProxyEndpoint"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# ModifyDBProxyEndpoint

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_ModifyDBProxyEndpoint
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ModifyDBProxyEndpoint
<a name="API_ModifyDBProxyEndpoint"></a>

Changes the settings for an existing DB proxy endpoint.

## Request Parameters
<a name="API_ModifyDBProxyEndpoint_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBProxyEndpointName **   
The name of the DB proxy sociated with the DB proxy endpoint that you want to modify.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `[a-zA-Z](?:-?[a-zA-Z0-9]+)*`   
Required: Yes

 ** NewDBProxyEndpointName **   
The new identifier for the `DBProxyEndpoint`. An identifier must begin with a letter and must contain only ASCII letters, digits, and hyphens; it can't end with a hyphen or contain two consecutive hyphens.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `[a-zA-Z](?:-?[a-zA-Z0-9]+)*`   
Required: No

 **VpcSecurityGroupIds.member.N**   
The VPC security group IDs for the DB proxy endpoint. When the DB proxy endpoint uses a different VPC than the original proxy, you also specify a different set of security group IDs than for the original proxy.  
Type: Array of strings  
Required: No

## Response Elements
<a name="API_ModifyDBProxyEndpoint_ResponseElements"></a>

The following element is returned by the service.

 ** DBProxyEndpoint **   
The `DBProxyEndpoint` object representing the new settings for the DB proxy endpoint.  
Type: [DBProxyEndpoint](API_DBProxyEndpoint.md) object

## Errors
<a name="API_ModifyDBProxyEndpoint_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBProxyEndpointAlreadyExistsFault **   
The specified DB proxy endpoint name must be unique for all DB proxy endpoints owned by your AWS account in the specified AWS Region.  
HTTP Status Code: 400

 ** DBProxyEndpointNotFoundFault **   
The DB proxy endpoint doesn't exist.  
HTTP Status Code: 404

 ** InvalidDBProxyEndpointStateFault **   
You can't perform this operation while the DB proxy endpoint is in a particular state.  
HTTP Status Code: 400

 ** InvalidDBProxyStateFault **   
The requested operation can't be performed while the proxy is in this state.  
HTTP Status Code: 400

## See Also
<a name="API_ModifyDBProxyEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/ModifyDBProxyEndpoint) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/ModifyDBProxyEndpoint) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/ModifyDBProxyEndpoint) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/ModifyDBProxyEndpoint) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/ModifyDBProxyEndpoint) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/ModifyDBProxyEndpoint) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/ModifyDBProxyEndpoint) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/ModifyDBProxyEndpoint) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/ModifyDBProxyEndpoint) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/ModifyDBProxyEndpoint) 