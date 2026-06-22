---
id: "@specs/aws/redshift/docs/API_Endpoint"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Endpoint"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# Endpoint

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_Endpoint
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Endpoint
<a name="API_Endpoint"></a>

Describes a connection endpoint.

## Contents
<a name="API_Endpoint_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** Address **   
The DNS address of the Cluster.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** Port **   
The port that the database engine is listening on.  
Type: Integer  
Required: No

 ** VpcEndpoints.VpcEndpoint.N **   
Describes a connection endpoint.  
Type: Array of [VpcEndpoint](API_VpcEndpoint.md) objects  
Required: No

## See Also
<a name="API_Endpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/Endpoint) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/Endpoint) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/Endpoint) 