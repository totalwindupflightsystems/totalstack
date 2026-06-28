---
id: "@specs/aws/network-firewall/docs/API_CreateProxyRulesByRequestPhase"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateProxyRulesByRequestPhase"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# CreateProxyRulesByRequestPhase

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_CreateProxyRulesByRequestPhase
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateProxyRulesByRequestPhase
<a name="API_CreateProxyRulesByRequestPhase"></a>

Evaluation points in the traffic flow where rules are applied. There are three phases in a traffic where the rule match is applied. 

This data type is used specifically for the [CreateProxyRules](API_CreateProxyRules.md) API.

Pre-DNS - before domain resolution.

Pre-Request - after DNS, before request.

Post-Response - after receiving response.

## Contents
<a name="API_CreateProxyRulesByRequestPhase_Contents"></a>

 ** PostRESPONSE **   <a name="networkfirewall-Type-CreateProxyRulesByRequestPhase-PostRESPONSE"></a>
After receiving response.  
Type: Array of [CreateProxyRule](API_CreateProxyRule.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 50 items.  
Required: No

 ** PreDNS **   <a name="networkfirewall-Type-CreateProxyRulesByRequestPhase-PreDNS"></a>
Before domain resolution.   
Type: Array of [CreateProxyRule](API_CreateProxyRule.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 50 items.  
Required: No

 ** PreREQUEST **   <a name="networkfirewall-Type-CreateProxyRulesByRequestPhase-PreREQUEST"></a>
After DNS, before request.  
Type: Array of [CreateProxyRule](API_CreateProxyRule.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 50 items.  
Required: No

## See Also
<a name="API_CreateProxyRulesByRequestPhase_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/CreateProxyRulesByRequestPhase) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/CreateProxyRulesByRequestPhase) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/CreateProxyRulesByRequestPhase) 