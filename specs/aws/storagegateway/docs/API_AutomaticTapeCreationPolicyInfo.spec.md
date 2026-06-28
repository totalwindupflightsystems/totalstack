---
id: "@specs/aws/storagegateway/docs/API_AutomaticTapeCreationPolicyInfo"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AutomaticTapeCreationPolicyInfo"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# AutomaticTapeCreationPolicyInfo

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_AutomaticTapeCreationPolicyInfo
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AutomaticTapeCreationPolicyInfo
<a name="API_AutomaticTapeCreationPolicyInfo"></a>

Information about the gateway's automatic tape creation policies, including the automatic tape creation rules and the gateway that is using the policies.

## Contents
<a name="API_AutomaticTapeCreationPolicyInfo_Contents"></a>

 ** AutomaticTapeCreationRules **   <a name="StorageGateway-Type-AutomaticTapeCreationPolicyInfo-AutomaticTapeCreationRules"></a>
An automatic tape creation policy consists of a list of automatic tape creation rules. This returns the rules that determine when and how to automatically create new tapes.  
Type: Array of [AutomaticTapeCreationRule](API_AutomaticTapeCreationRule.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 10 items.  
Required: No

 ** GatewayARN **   <a name="StorageGateway-Type-AutomaticTapeCreationPolicyInfo-GatewayARN"></a>
The Amazon Resource Name (ARN) of the gateway. Use the [ListGateways](API_ListGateways.md) operation to return a list of gateways for your account and AWS Region.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Required: No

## See Also
<a name="API_AutomaticTapeCreationPolicyInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/AutomaticTapeCreationPolicyInfo) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/AutomaticTapeCreationPolicyInfo) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/AutomaticTapeCreationPolicyInfo) 