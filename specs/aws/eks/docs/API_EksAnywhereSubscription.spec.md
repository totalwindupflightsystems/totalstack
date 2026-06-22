---
id: "@specs/aws/eks/docs/API_EksAnywhereSubscription"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS EksAnywhereSubscription"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# EksAnywhereSubscription

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_EksAnywhereSubscription
> **target_lang:** meta — documentation tier. ALL sections preserved.



# EksAnywhereSubscription
<a name="API_EksAnywhereSubscription"></a>

An EKS Anywhere subscription authorizing the customer to support for licensed clusters and access to EKS Anywhere Curated Packages.

## Contents
<a name="API_EksAnywhereSubscription_Contents"></a>

 ** arn **   <a name="AmazonEKS-Type-EksAnywhereSubscription-arn"></a>
The Amazon Resource Name (ARN) for the subscription.  
Type: String  
Required: No

 ** autoRenew **   <a name="AmazonEKS-Type-EksAnywhereSubscription-autoRenew"></a>
A boolean indicating whether or not a subscription will auto renew when it expires.  
Type: Boolean  
Required: No

 ** createdAt **   <a name="AmazonEKS-Type-EksAnywhereSubscription-createdAt"></a>
The Unix timestamp in seconds for when the subscription was created.  
Type: Timestamp  
Required: No

 ** effectiveDate **   <a name="AmazonEKS-Type-EksAnywhereSubscription-effectiveDate"></a>
The Unix timestamp in seconds for when the subscription is effective.  
Type: Timestamp  
Required: No

 ** expirationDate **   <a name="AmazonEKS-Type-EksAnywhereSubscription-expirationDate"></a>
The Unix timestamp in seconds for when the subscription will expire or auto renew, depending on the auto renew configuration of the subscription object.  
Type: Timestamp  
Required: No

 ** id **   <a name="AmazonEKS-Type-EksAnywhereSubscription-id"></a>
UUID identifying a subscription.  
Type: String  
Required: No

 ** licenseArns **   <a name="AmazonEKS-Type-EksAnywhereSubscription-licenseArns"></a>
 AWS License Manager ARN associated with the subscription.  
Type: Array of strings  
Required: No

 ** licenseQuantity **   <a name="AmazonEKS-Type-EksAnywhereSubscription-licenseQuantity"></a>
The number of licenses included in a subscription. Valid values are between 1 and 100.  
Type: Integer  
Required: No

 ** licenses **   <a name="AmazonEKS-Type-EksAnywhereSubscription-licenses"></a>
Includes all of the claims in the license token necessary to validate the license for extended support.  
Type: Array of [License](API_License.md) objects  
Required: No

 ** licenseType **   <a name="AmazonEKS-Type-EksAnywhereSubscription-licenseType"></a>
The type of licenses included in the subscription. Valid value is CLUSTER. With the CLUSTER license type, each license covers support for a single EKS Anywhere cluster.  
Type: String  
Valid Values: `Cluster`   
Required: No

 ** status **   <a name="AmazonEKS-Type-EksAnywhereSubscription-status"></a>
The status of a subscription.  
Type: String  
Required: No

 ** tags **   <a name="AmazonEKS-Type-EksAnywhereSubscription-tags"></a>
The metadata for a subscription to assist with categorization and organization. Each tag consists of a key and an optional value. Subscription tags do not propagate to any other resources associated with the subscription.  
Type: String to string map  
Map Entries: Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Value Length Constraints: Maximum length of 256.  
Required: No

 ** term **   <a name="AmazonEKS-Type-EksAnywhereSubscription-term"></a>
An EksAnywhereSubscriptionTerm object.   
Type: [EksAnywhereSubscriptionTerm](API_EksAnywhereSubscriptionTerm.md) object  
Required: No

## See Also
<a name="API_EksAnywhereSubscription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/EksAnywhereSubscription) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/EksAnywhereSubscription) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/EksAnywhereSubscription) 