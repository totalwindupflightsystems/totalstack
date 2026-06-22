---
id: "@specs/aws/redshift/docs/API_DescribeIntegrationsFilter"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeIntegrationsFilter"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# DescribeIntegrationsFilter

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_DescribeIntegrationsFilter
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeIntegrationsFilter
<a name="API_DescribeIntegrationsFilter"></a>

A set of elements to filter the returned integrations.

## Contents
<a name="API_DescribeIntegrationsFilter_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** Name **   
Specifies the type of integration filter.  
Type: String  
Valid Values: `integration-arn | source-arn | source-types | status`   
Required: Yes

 ** Values.Value.N **   
Specifies the values to filter on.  
Type: Array of strings  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

## See Also
<a name="API_DescribeIntegrationsFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/DescribeIntegrationsFilter) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/DescribeIntegrationsFilter) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/DescribeIntegrationsFilter) 