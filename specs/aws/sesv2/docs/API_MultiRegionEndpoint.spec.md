---
id: "@specs/aws/sesv2/docs/API_MultiRegionEndpoint"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS MultiRegionEndpoint"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# MultiRegionEndpoint

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_MultiRegionEndpoint
> **target_lang:** meta — documentation tier. ALL sections preserved.



# MultiRegionEndpoint
<a name="API_MultiRegionEndpoint"></a>

An object that contains multi-region endpoint (global-endpoint) properties.

## Contents
<a name="API_MultiRegionEndpoint_Contents"></a>

 ** CreatedTimestamp **   <a name="SES-Type-MultiRegionEndpoint-CreatedTimestamp"></a>
The time stamp of when the multi-region endpoint (global-endpoint) was created.  
Type: Timestamp  
Required: No

 ** EndpointId **   <a name="SES-Type-MultiRegionEndpoint-EndpointId"></a>
The ID of the multi-region endpoint (global-endpoint).  
Type: String  
Required: No

 ** EndpointName **   <a name="SES-Type-MultiRegionEndpoint-EndpointName"></a>
The name of the multi-region endpoint (global-endpoint).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `^[\w\-_]+$`   
Required: No

 ** LastUpdatedTimestamp **   <a name="SES-Type-MultiRegionEndpoint-LastUpdatedTimestamp"></a>
The time stamp of when the multi-region endpoint (global-endpoint) was last updated.  
Type: Timestamp  
Required: No

 ** Regions **   <a name="SES-Type-MultiRegionEndpoint-Regions"></a>
Primary and secondary regions between which multi-region endpoint splits sending traffic.  
Type: Array of strings  
Required: No

 ** Status **   <a name="SES-Type-MultiRegionEndpoint-Status"></a>
The status of the multi-region endpoint (global-endpoint).  
+  `CREATING` – The resource is being provisioned.
+  `READY` – The resource is ready to use.
+  `FAILED` – The resource failed to be provisioned.
+  `DELETING` – The resource is being deleted as requested.
Type: String  
Valid Values: `CREATING | READY | FAILED | DELETING`   
Required: No

## See Also
<a name="API_MultiRegionEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/MultiRegionEndpoint) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/MultiRegionEndpoint) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/MultiRegionEndpoint) 