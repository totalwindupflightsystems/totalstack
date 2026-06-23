---
id: "@specs/aws/appmesh/docs/API_ServiceDiscovery"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ServiceDiscovery"
status: active
depends_on:
  - "@specs/aws/appmesh/meta"
---

# ServiceDiscovery

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appmesh/docs/API_ServiceDiscovery
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ServiceDiscovery
<a name="API_ServiceDiscovery"></a>

An object that represents the service discovery information for a virtual node.

## Contents
<a name="API_ServiceDiscovery_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** awsCloudMap **   <a name="appmesh-Type-ServiceDiscovery-awsCloudMap"></a>
Specifies any AWS Cloud Map information for the virtual node.  
Type: [AwsCloudMapServiceDiscovery](API_AwsCloudMapServiceDiscovery.md) object  
Required: No

 ** dns **   <a name="appmesh-Type-ServiceDiscovery-dns"></a>
Specifies the DNS information for the virtual node.  
Type: [DnsServiceDiscovery](API_DnsServiceDiscovery.md) object  
Required: No

## See Also
<a name="API_ServiceDiscovery_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/ServiceDiscovery) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/ServiceDiscovery) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/ServiceDiscovery) 