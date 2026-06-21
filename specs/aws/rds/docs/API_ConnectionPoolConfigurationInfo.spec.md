---
id: "@specs/aws/rds/docs/API_ConnectionPoolConfigurationInfo"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ConnectionPoolConfigurationInfo"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# ConnectionPoolConfigurationInfo

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_ConnectionPoolConfigurationInfo
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ConnectionPoolConfigurationInfo
<a name="API_ConnectionPoolConfigurationInfo"></a>

Displays the settings that control the size and behavior of the connection pool associated with a `DBProxyTarget`.

## Contents
<a name="API_ConnectionPoolConfigurationInfo_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** ConnectionBorrowTimeout **   
The number of seconds for a proxy to wait for a connection to become available in the connection pool. Only applies when the proxy has opened its maximum number of connections and all connections are busy with client sessions.  
Type: Integer  
Required: No

 ** InitQuery **   
One or more SQL statements for the proxy to run when opening each new database connection. The setting is typically used with `SET` statements to make sure that each connection has identical settings. The query added here must be valid. For including multiple variables in a single SET statement, use a comma separator. This is an optional field.  
For example: `SET variable1=value1, variable2=value2`   
Since you can access initialization query as part of target group configuration, it is not protected by authentication or cryptographic methods. Anyone with access to view or manage your proxy target group configuration can view the initialization query. You should not add sensitive data, such as passwords or long-lived encryption keys, to this option.
Type: String  
Required: No

 ** MaxConnectionsPercent **   
The maximum size of the connection pool for each target in a target group. The value is expressed as a percentage of the `max_connections` setting for the RDS DB instance or Aurora DB cluster used by the target group.  
Type: Integer  
Required: No

 ** MaxIdleConnectionsPercent **   
Controls how actively the proxy closes idle database connections in the connection pool. The value is expressed as a percentage of the `max_connections` setting for the RDS DB instance or Aurora DB cluster used by the target group. With a high value, the proxy leaves a high percentage of idle database connections open. A low value causes the proxy to close more idle connections and return them to the database.  
Type: Integer  
Required: No

 ** SessionPinningFilters.member.N **   
Each item in the list represents a class of SQL operations that normally cause all later statements in a session using a proxy to be pinned to the same underlying database connection. Including an item in the list exempts that class of SQL operations from the pinning behavior. This setting is only supported for MySQL engine family databases. Currently, the only allowed value is `EXCLUDE_VARIABLE_SETS`.  
Type: Array of strings  
Required: No

## See Also
<a name="API_ConnectionPoolConfigurationInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/ConnectionPoolConfigurationInfo) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/ConnectionPoolConfigurationInfo) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/ConnectionPoolConfigurationInfo) 