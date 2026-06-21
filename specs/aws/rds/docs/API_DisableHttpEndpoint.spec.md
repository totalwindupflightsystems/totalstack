---
id: "@specs/aws/rds/docs/API_DisableHttpEndpoint"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DisableHttpEndpoint"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# DisableHttpEndpoint

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_DisableHttpEndpoint
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DisableHttpEndpoint
<a name="API_DisableHttpEndpoint"></a>

Disables the HTTP endpoint for the specified DB cluster. Disabling this endpoint disables RDS Data API.

For more information, see [Using RDS Data API](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/data-api.html) in the *Amazon Aurora User Guide*.

**Note**  
This operation applies only to Aurora Serverless v2 and provisioned DB clusters. To disable the HTTP endpoint for Aurora Serverless v1 DB clusters, use the `EnableHttpEndpoint` parameter of the `ModifyDBCluster` operation.

## Request Parameters
<a name="API_DisableHttpEndpoint_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ResourceArn **   
The Amazon Resource Name (ARN) of the DB cluster.  
Type: String  
Required: Yes

## Response Elements
<a name="API_DisableHttpEndpoint_ResponseElements"></a>

The following elements are returned by the service.

 ** HttpEndpointEnabled **   
Indicates whether the HTTP endpoint is enabled or disabled for the DB cluster.  
Type: Boolean

 ** ResourceArn **   
The ARN of the DB cluster.  
Type: String

## Errors
<a name="API_DisableHttpEndpoint_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidResourceStateFault **   
The operation can't be performed because another operation is in progress.  
HTTP Status Code: 400

 ** ResourceNotFoundFault **   
The specified resource ID was not found.  
HTTP Status Code: 404

## See Also
<a name="API_DisableHttpEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/DisableHttpEndpoint) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/DisableHttpEndpoint) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DisableHttpEndpoint) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/DisableHttpEndpoint) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DisableHttpEndpoint) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/DisableHttpEndpoint) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/DisableHttpEndpoint) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/DisableHttpEndpoint) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/DisableHttpEndpoint) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DisableHttpEndpoint) 