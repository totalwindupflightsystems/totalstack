---
id: "@specs/aws/fsx/docs/API_UpdateFileCacheLustreConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateFileCacheLustreConfiguration"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# UpdateFileCacheLustreConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_UpdateFileCacheLustreConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateFileCacheLustreConfiguration
<a name="API_UpdateFileCacheLustreConfiguration"></a>

The configuration update for an Amazon File Cache resource.

## Contents
<a name="API_UpdateFileCacheLustreConfiguration_Contents"></a>

 ** WeeklyMaintenanceStartTime **   <a name="FSx-Type-UpdateFileCacheLustreConfiguration-WeeklyMaintenanceStartTime"></a>
The preferred start time to perform weekly maintenance, formatted d:HH:MM in the UTC time zone, where d is the weekday number, from 1 through 7, beginning with Monday and ending with Sunday.  
For example, `1:05:00` specifies maintenance at 5 AM Monday.  
Type: String  
Length Constraints: Fixed length of 7.  
Pattern: `^[1-7]:([01]\d|2[0-3]):?([0-5]\d)$`   
Required: No

## See Also
<a name="API_UpdateFileCacheLustreConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/UpdateFileCacheLustreConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/UpdateFileCacheLustreConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/UpdateFileCacheLustreConfiguration) 