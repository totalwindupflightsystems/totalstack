---
id: "@specs/aws/network-firewall/docs/API_ProxyConfigDefaultRulePhaseActionsRequest"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ProxyConfigDefaultRulePhaseActionsRequest"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# ProxyConfigDefaultRulePhaseActionsRequest

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_ProxyConfigDefaultRulePhaseActionsRequest
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ProxyConfigDefaultRulePhaseActionsRequest
<a name="API_ProxyConfigDefaultRulePhaseActionsRequest"></a>

Evaluation points in the traffic flow where rules are applied. There are three phases in a traffic where the rule match is applied. 

This data type is used specifically for the [CreateProxyConfiguration](API_CreateProxyConfiguration.md) and [UpdateProxyConfiguration](API_UpdateProxyConfiguration.md) APIs.

## Contents
<a name="API_ProxyConfigDefaultRulePhaseActionsRequest_Contents"></a>

 ** PostRESPONSE **   <a name="networkfirewall-Type-ProxyConfigDefaultRulePhaseActionsRequest-PostRESPONSE"></a>
After receiving response.  
Type: String  
Valid Values: `ALLOW | DENY | ALERT`   
Required: No

 ** PreDNS **   <a name="networkfirewall-Type-ProxyConfigDefaultRulePhaseActionsRequest-PreDNS"></a>
Before domain resolution.   
Type: String  
Valid Values: `ALLOW | DENY | ALERT`   
Required: No

 ** PreREQUEST **   <a name="networkfirewall-Type-ProxyConfigDefaultRulePhaseActionsRequest-PreREQUEST"></a>
After DNS, before request.  
Type: String  
Valid Values: `ALLOW | DENY | ALERT`   
Required: No

## See Also
<a name="API_ProxyConfigDefaultRulePhaseActionsRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/ProxyConfigDefaultRulePhaseActionsRequest) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/ProxyConfigDefaultRulePhaseActionsRequest) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/ProxyConfigDefaultRulePhaseActionsRequest) 