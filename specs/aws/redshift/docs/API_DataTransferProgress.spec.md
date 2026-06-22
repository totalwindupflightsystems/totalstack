---
id: "@specs/aws/redshift/docs/API_DataTransferProgress"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DataTransferProgress"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# DataTransferProgress

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_DataTransferProgress
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DataTransferProgress
<a name="API_DataTransferProgress"></a>

Describes the status of a cluster while it is in the process of resizing with an incremental resize.

## Contents
<a name="API_DataTransferProgress_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** CurrentRateInMegaBytesPerSecond **   
Describes the data transfer rate in MB's per second.  
Type: Double  
Required: No

 ** DataTransferredInMegaBytes **   
Describes the total amount of data that has been transfered in MB's.  
Type: Long  
Required: No

 ** ElapsedTimeInSeconds **   
Describes the number of seconds that have elapsed during the data transfer.  
Type: Long  
Required: No

 ** EstimatedTimeToCompletionInSeconds **   
Describes the estimated number of seconds remaining to complete the transfer.  
Type: Long  
Required: No

 ** Status **   
Describes the status of the cluster. While the transfer is in progress the status is `transferringdata`.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** TotalDataInMegaBytes **   
Describes the total amount of data to be transfered in megabytes.  
Type: Long  
Required: No

## See Also
<a name="API_DataTransferProgress_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/DataTransferProgress) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/DataTransferProgress) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/DataTransferProgress) 