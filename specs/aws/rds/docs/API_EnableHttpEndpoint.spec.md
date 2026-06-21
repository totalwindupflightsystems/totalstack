---
id: "@specs/aws/rds/docs/API_EnableHttpEndpoint"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS EnableHttpEndpoint"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# EnableHttpEndpoint

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_EnableHttpEndpoint
> **target_lang:** meta — documentation tier. ALL sections preserved.



# EnableHttpEndpoint
<a name="API_EnableHttpEndpoint"></a>

Enables the HTTP endpoint for the DB cluster. By default, the HTTP endpoint isn't enabled.

When enabled, this endpoint provides a connectionless web service API (RDS Data API) for running SQL queries on the Aurora DB cluster. You can also query your database from inside the RDS console with the RDS query editor.

For more information, see [Using RDS Data API](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/data-api.html) in the *Amazon Aurora User Guide*.

**Note**  
This operation applies only to Aurora Serverless v2 and provisioned DB clusters. To enable the HTTP endpoint for Aurora Serverless v1 DB clusters, use the `EnableHttpEndpoint` parameter of the `ModifyDBCluster` operation.

## Request Parameters
<a name="API_EnableHttpEndpoint_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ResourceArn **   
The Amazon Resource Name (ARN) of the DB cluster.  
Type: String  
Required: Yes

## Response Elements
<a name="API_EnableHttpEndpoint_ResponseElements"></a>

The following elements are returned by the service.

 ** HttpEndpointEnabled **   
Indicates whether the HTTP endpoint is enabled or disabled for the DB cluster.  
Type: Boolean

 ** ResourceArn **   
The ARN of the DB cluster.  
Type: String

## Errors
<a name="API_EnableHttpEndpoint_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidResourceStateFault **   
The operation can't be performed because another operation is in progress.  
HTTP Status Code: 400

 ** ResourceNotFoundFault **   
The specified resource ID was not found.  
HTTP Status Code: 404

## See Also
<a name="API_EnableHttpEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/EnableHttpEndpoint) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/EnableHttpEndpoint) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/EnableHttpEndpoint) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/EnableHttpEndpoint) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/EnableHttpEndpoint) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/EnableHttpEndpoint) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/EnableHttpEndpoint) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/EnableHttpEndpoint) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/EnableHttpEndpoint) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/EnableHttpEndpoint) 