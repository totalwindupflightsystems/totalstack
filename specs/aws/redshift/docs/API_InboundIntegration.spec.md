---
id: "@specs/aws/redshift/docs/API_InboundIntegration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS InboundIntegration"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# InboundIntegration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_InboundIntegration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# InboundIntegration
<a name="API_InboundIntegration"></a>

The content of an inbound integration.

## Contents
<a name="API_InboundIntegration_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** CreateTime **   
The creation time of an inbound integration.  
Type: Timestamp  
Required: No

 ** Errors.IntegrationError.N **   
The outstanding errors of an inbound integration. Each item is an "IntegrationError". This is null if there is no error.  
Type: Array of [IntegrationError](API_IntegrationError.md) objects  
Required: No

 ** IntegrationArn **   
The Amazon Resource Name (ARN) of an inbound integration.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `^arn:aws[a-z\-]*:.+:[a-z0-9\-]*:[0-9]*:integration:[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`   
Required: No

 ** SourceArn **   
The Amazon Resource Name (ARN) of the source of an inbound integration.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** Status **   
The status of an inbound integration.  
Type: String  
Valid Values: `creating | active | modifying | failed | deleting | syncing | needs_attention`   
Required: No

 ** TargetArn **   
The Amazon Resource Name (ARN) of the target of an inbound integration.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `^arn:aws[a-z\-]*:redshift(-serverless)?:[a-z0-9\-]+:[0-9]{12}:(namespace\/|namespace:)[a-z0-9\-]+$`   
Required: No

## See Also
<a name="API_InboundIntegration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/InboundIntegration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/InboundIntegration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/InboundIntegration) 