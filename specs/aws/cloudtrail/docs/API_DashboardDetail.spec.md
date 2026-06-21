---
id: "@specs/aws/cloudtrail/docs/API_DashboardDetail"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DashboardDetail"
status: active
depends_on:
  - "@specs/aws/cloudtrail/meta"
---

# DashboardDetail

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudtrail/docs/API_DashboardDetail
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DashboardDetail
<a name="API_DashboardDetail"></a>

 Provides information about a CloudTrail Lake dashboard. 

## Contents
<a name="API_DashboardDetail_Contents"></a>

 ** DashboardArn **   <a name="awscloudtrail-Type-DashboardDetail-DashboardArn"></a>
 The ARN for the dashboard.   
Type: String  
Pattern: `^[a-zA-Z0-9._/\-:]+$`   
Required: No

 ** Type **   <a name="awscloudtrail-Type-DashboardDetail-Type"></a>
 The type of dashboard.   
Type: String  
Valid Values: `MANAGED | CUSTOM`   
Required: No

## See Also
<a name="API_DashboardDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/DashboardDetail) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/DashboardDetail) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/DashboardDetail) 