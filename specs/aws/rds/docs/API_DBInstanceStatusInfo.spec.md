---
id: "@specs/aws/rds/docs/API_DBInstanceStatusInfo"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DBInstanceStatusInfo"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# DBInstanceStatusInfo

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_DBInstanceStatusInfo
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DBInstanceStatusInfo
<a name="API_DBInstanceStatusInfo"></a>

Provides a list of status information for a DB instance.

## Contents
<a name="API_DBInstanceStatusInfo_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** Message **   
Details of the error if there is an error for the instance. If the instance isn't in an error state, this value is blank.  
Type: String  
Required: No

 ** Normal **   
Indicates whether the instance is operating normally (TRUE) or is in an error state (FALSE).  
Type: Boolean  
Required: No

 ** Status **   
The status of the DB instance. For a StatusType of read replica, the values can be replicating, replication stop point set, replication stop point reached, error, stopped, or terminated.  
Type: String  
Required: No

 ** StatusType **   
This value is currently "read replication."  
Type: String  
Required: No

## See Also
<a name="API_DBInstanceStatusInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DBInstanceStatusInfo) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DBInstanceStatusInfo) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DBInstanceStatusInfo) 