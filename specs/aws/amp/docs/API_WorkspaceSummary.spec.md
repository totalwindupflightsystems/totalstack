---
id: "@specs/aws/amp/docs/API_WorkspaceSummary"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS WorkspaceSummary"
status: active
depends_on:
  - "@specs/aws/amp/meta"
---

# WorkspaceSummary

> **source:** AWS Documentation
> **spec:id:** @specs/aws/amp/docs/API_WorkspaceSummary
> **target_lang:** meta — documentation tier. ALL sections preserved.



# WorkspaceSummary
<a name="API_WorkspaceSummary"></a>

The information about one Amazon Managed Service for Prometheus workspace in your account. 

## Contents
<a name="API_WorkspaceSummary_Contents"></a>

 ** arn **   <a name="prometheus-Type-WorkspaceSummary-arn"></a>
The ARN of the workspace.  
Type: String  
Pattern: `arn:aws[-a-z]*:aps:[-a-z0-9]+:[0-9]{12}:workspace/.+`   
Required: Yes

 ** createdAt **   <a name="prometheus-Type-WorkspaceSummary-createdAt"></a>
The date and time that the workspace was created.  
Type: Timestamp  
Required: Yes

 ** status **   <a name="prometheus-Type-WorkspaceSummary-status"></a>
The current status of the workspace.  
Type: [WorkspaceStatus](API_WorkspaceStatus.md) object  
Required: Yes

 ** workspaceId **   <a name="prometheus-Type-WorkspaceSummary-workspaceId"></a>
The unique ID for the workspace.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `.*[0-9A-Za-z][-.0-9A-Z_a-z]*.*`   
Required: Yes

 ** alias **   <a name="prometheus-Type-WorkspaceSummary-alias"></a>
The alias that is assigned to this workspace to help identify it. It does not need to be unique.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Required: No

 ** kmsKeyArn **   <a name="prometheus-Type-WorkspaceSummary-kmsKeyArn"></a>
(optional) If the workspace was created with a customer managed AWS KMS key, the ARN for the key used.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `arn:aws[-a-z]*:kms:[-a-z0-9]+:[0-9]{12}:key/[-a-f0-9]+`   
Required: No

 ** tags **   <a name="prometheus-Type-WorkspaceSummary-tags"></a>
The list of tag keys and values that are associated with the workspace.  
Type: String to string map  
Map Entries: Minimum number of 0 items. Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`   
Value Length Constraints: Minimum length of 0. Maximum length of 256.  
Value Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`   
Required: No

## See Also
<a name="API_WorkspaceSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amp-2020-08-01/WorkspaceSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amp-2020-08-01/WorkspaceSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amp-2020-08-01/WorkspaceSummary) 