---
id: "@specs/aws/sesv2/docs/API_ReputationEntity"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ReputationEntity"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# ReputationEntity

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_ReputationEntity
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ReputationEntity
<a name="API_ReputationEntity"></a>

An object that contains information about a reputation entity, including its reference, type, policy, status records, and reputation impact.

## Contents
<a name="API_ReputationEntity_Contents"></a>

 ** AwsSesManagedStatus **   <a name="SES-Type-ReputationEntity-AwsSesManagedStatus"></a>
The AWS Amazon SES-managed status record for this reputation entity, including the current status, cause description, and last updated timestamp.  
Type: [StatusRecord](API_StatusRecord.md) object  
Required: No

 ** CustomerManagedStatus **   <a name="SES-Type-ReputationEntity-CustomerManagedStatus"></a>
The customer-managed status record for this reputation entity, including the current status, cause description, and last updated timestamp.  
Type: [StatusRecord](API_StatusRecord.md) object  
Required: No

 ** ReputationEntityReference **   <a name="SES-Type-ReputationEntity-ReputationEntityReference"></a>
The unique identifier for the reputation entity. For resource-type entities, this is the Amazon Resource Name (ARN) of the resource.  
Type: String  
Length Constraints: Minimum length of 1.  
Required: No

 ** ReputationEntityType **   <a name="SES-Type-ReputationEntity-ReputationEntityType"></a>
The type of reputation entity. Currently, only `RESOURCE` type entities are supported.  
Type: String  
Valid Values: `RESOURCE`   
Required: No

 ** ReputationImpact **   <a name="SES-Type-ReputationEntity-ReputationImpact"></a>
The reputation impact level for this entity, representing the highest impact reputation finding currently active. Reputation findings can be retrieved using the `ListRecommendations` operation.  
Type: String  
Valid Values: `LOW | HIGH`   
Required: No

 ** ReputationManagementPolicy **   <a name="SES-Type-ReputationEntity-ReputationManagementPolicy"></a>
The Amazon Resource Name (ARN) of the reputation management policy applied to this entity. This is an AWS Amazon SES-managed policy.  
Type: String  
Length Constraints: Minimum length of 1.  
Required: No

 ** SendingStatusAggregate **   <a name="SES-Type-ReputationEntity-SendingStatusAggregate"></a>
The aggregate sending status that determines whether the entity is allowed to send emails. This status is derived from both the customer-managed and AWS Amazon SES-managed statuses. If either the customer-managed status or the AWS Amazon SES-managed status is `DISABLED`, the aggregate status will be `DISABLED` and the entity will not be allowed to send emails. When the customer-managed status is set to `REINSTATED`, the entity can continue sending even if there are active reputation findings, provided the AWS Amazon SES-managed status also permits sending. The entity can only send emails when both statuses permit sending.  
Type: String  
Valid Values: `ENABLED | REINSTATED | DISABLED`   
Required: No

## See Also
<a name="API_ReputationEntity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/ReputationEntity) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/ReputationEntity) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/ReputationEntity) 