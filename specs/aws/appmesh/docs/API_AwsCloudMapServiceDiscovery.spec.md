---
id: "@specs/aws/appmesh/docs/API_AwsCloudMapServiceDiscovery"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AwsCloudMapServiceDiscovery"
status: active
depends_on:
  - "@specs/aws/appmesh/meta"
---

# AwsCloudMapServiceDiscovery

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appmesh/docs/API_AwsCloudMapServiceDiscovery
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AwsCloudMapServiceDiscovery
<a name="API_AwsCloudMapServiceDiscovery"></a>

An object that represents the AWS Cloud Map service discovery information for your virtual node.

**Note**  
 AWS Cloud Map is not available in the eu-south-1 Region.

## Contents
<a name="API_AwsCloudMapServiceDiscovery_Contents"></a>

 ** namespaceName **   <a name="appmesh-Type-AwsCloudMapServiceDiscovery-namespaceName"></a>
The HTTP name of the AWS Cloud Map namespace to use.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Required: Yes

 ** serviceName **   <a name="appmesh-Type-AwsCloudMapServiceDiscovery-serviceName"></a>
The name of the AWS Cloud Map service to use.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Required: Yes

 ** attributes **   <a name="appmesh-Type-AwsCloudMapServiceDiscovery-attributes"></a>
A string map that contains attributes with values that you can use to filter instances by any custom attribute that you specified when you registered the instance. Only instances that match all of the specified key/value pairs will be returned.  
Type: Array of [AwsCloudMapInstanceAttribute](API_AwsCloudMapInstanceAttribute.md) objects  
Required: No

 ** ipPreference **   <a name="appmesh-Type-AwsCloudMapServiceDiscovery-ipPreference"></a>
The preferred IP version that this virtual node uses. Setting the IP preference on the virtual node only overrides the IP preference set for the mesh on this specific node.  
Type: String  
Valid Values: `IPv6_PREFERRED | IPv4_PREFERRED | IPv4_ONLY | IPv6_ONLY`   
Required: No

## See Also
<a name="API_AwsCloudMapServiceDiscovery_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/AwsCloudMapServiceDiscovery) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/AwsCloudMapServiceDiscovery) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/AwsCloudMapServiceDiscovery) 