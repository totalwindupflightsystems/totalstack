---
id: "@specs/aws/docdb/docs/API_DBInstanceStatusInfo"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DBInstanceStatusInfo"
status: active
depends_on:
  - "@specs/aws/docdb/meta"
---

# DBInstanceStatusInfo

> **source:** AWS Documentation
> **spec:id:** @specs/aws/docdb/docs/API_DBInstanceStatusInfo
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DBInstanceStatusInfo
<a name="API_DBInstanceStatusInfo"></a>

Provides a list of status information for an instance.

## Contents
<a name="API_DBInstanceStatusInfo_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** Message **   
Details of the error if there is an error for the instance. If the instance is not in an error state, this value is blank.  
Type: String  
Required: No

 ** Normal **   
A Boolean value that is `true` if the instance is operating normally, or `false` if the instance is in an error state.  
Type: Boolean  
Required: No

 ** Status **   
Status of the instance. For a `StatusType` of read replica, the values can be `replicating`, error, `stopped`, or `terminated`.  
Type: String  
Required: No

 ** StatusType **   
This value is currently "`read replication`."  
Type: String  
Required: No

## See Also
<a name="API_DBInstanceStatusInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/docdb-2014-10-31/DBInstanceStatusInfo) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/docdb-2014-10-31/DBInstanceStatusInfo) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/docdb-2014-10-31/DBInstanceStatusInfo) 