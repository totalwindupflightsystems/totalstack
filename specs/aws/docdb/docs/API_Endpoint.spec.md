---
id: "@specs/aws/docdb/docs/API_Endpoint"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Endpoint"
status: active
depends_on:
  - "@specs/aws/docdb/meta"
---

# Endpoint

> **source:** AWS Documentation
> **spec:id:** @specs/aws/docdb/docs/API_Endpoint
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Endpoint
<a name="API_Endpoint"></a>

Network information for accessing a cluster or instance. Client programs must specify a valid endpoint to access these Amazon DocumentDB resources.

## Contents
<a name="API_Endpoint_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** Address **   
Specifies the DNS address of the instance.  
Type: String  
Required: No

 ** HostedZoneId **   
Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.  
Type: String  
Required: No

 ** Port **   
Specifies the port that the database engine is listening on.  
Type: Integer  
Required: No

## See Also
<a name="API_Endpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/docdb-2014-10-31/Endpoint) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/docdb-2014-10-31/Endpoint) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/docdb-2014-10-31/Endpoint) 