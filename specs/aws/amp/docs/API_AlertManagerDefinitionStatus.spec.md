---
id: "@specs/aws/amp/docs/API_AlertManagerDefinitionStatus"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AlertManagerDefinitionStatus"
status: active
depends_on:
  - "@specs/aws/amp/meta"
---

# AlertManagerDefinitionStatus

> **source:** AWS Documentation
> **spec:id:** @specs/aws/amp/docs/API_AlertManagerDefinitionStatus
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AlertManagerDefinitionStatus
<a name="API_AlertManagerDefinitionStatus"></a>

The status of the alert manager. 

## Contents
<a name="API_AlertManagerDefinitionStatus_Contents"></a>

 ** statusCode **   <a name="prometheus-Type-AlertManagerDefinitionStatus-statusCode"></a>
The current status of the alert manager.   
Type: String  
Valid Values: `CREATING | ACTIVE | UPDATING | DELETING | CREATION_FAILED | UPDATE_FAILED`   
Required: Yes

 ** statusReason **   <a name="prometheus-Type-AlertManagerDefinitionStatus-statusReason"></a>
If there is a failure, the reason for the failure.  
Type: String  
Required: No

## See Also
<a name="API_AlertManagerDefinitionStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amp-2020-08-01/AlertManagerDefinitionStatus) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amp-2020-08-01/AlertManagerDefinitionStatus) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amp-2020-08-01/AlertManagerDefinitionStatus) 