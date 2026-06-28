---
id: "@specs/aws/network-firewall/docs/API_ProxyRulesByRequestPhase"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ProxyRulesByRequestPhase"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# ProxyRulesByRequestPhase

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_ProxyRulesByRequestPhase
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ProxyRulesByRequestPhase
<a name="API_ProxyRulesByRequestPhase"></a>

Evaluation points in the traffic flow where rules are applied. There are three phases in a traffic where the rule match is applied. 

## Contents
<a name="API_ProxyRulesByRequestPhase_Contents"></a>

 ** PostRESPONSE **   <a name="networkfirewall-Type-ProxyRulesByRequestPhase-PostRESPONSE"></a>
After receiving response.  
Type: Array of [ProxyRule](API_ProxyRule.md) objects  
Required: No

 ** PreDNS **   <a name="networkfirewall-Type-ProxyRulesByRequestPhase-PreDNS"></a>
Before domain resolution.   
Type: Array of [ProxyRule](API_ProxyRule.md) objects  
Required: No

 ** PreREQUEST **   <a name="networkfirewall-Type-ProxyRulesByRequestPhase-PreREQUEST"></a>
After DNS, before request.  
Type: Array of [ProxyRule](API_ProxyRule.md) objects  
Required: No

## See Also
<a name="API_ProxyRulesByRequestPhase_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/ProxyRulesByRequestPhase) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/ProxyRulesByRequestPhase) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/ProxyRulesByRequestPhase) 