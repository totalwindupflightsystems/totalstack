---
id: "@specs/aws/rds/docs/API_CreateDBProxy"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateDBProxy"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# CreateDBProxy

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_CreateDBProxy
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateDBProxy
<a name="API_CreateDBProxy"></a>

Creates a new DB proxy.

## Request Parameters
<a name="API_CreateDBProxy_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBProxyName **   
The identifier for the proxy. This name must be unique for all proxies owned by your AWS account in the specified AWS Region. An identifier must begin with a letter and must contain only ASCII letters, digits, and hyphens; it can't end with a hyphen or contain two consecutive hyphens.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `[a-zA-Z](?:-?[a-zA-Z0-9]+)*`   
Required: Yes

 ** EngineFamily **   
The kinds of databases that the proxy can connect to. This value determines which database network protocol the proxy recognizes when it interprets network traffic to and from the database. For Aurora MySQL, RDS for MariaDB, and RDS for MySQL databases, specify `MYSQL`. For Aurora PostgreSQL and RDS for PostgreSQL databases, specify `POSTGRESQL`. For RDS for Microsoft SQL Server, specify `SQLSERVER`.  
Type: String  
Valid Values: `MYSQL | POSTGRESQL | SQLSERVER`   
Required: Yes

 ** RoleArn **   
The Amazon Resource Name (ARN) of the IAM role that the proxy uses to access secrets in AWS Secrets Manager.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Required: Yes

 **VpcSubnetIds.member.N**   
One or more VPC subnet IDs to associate with the new proxy.  
Type: Array of strings  
Required: Yes

 **Auth.member.N**   
The authorization mechanism that the proxy uses.  
Type: Array of [UserAuthConfig](API_UserAuthConfig.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 200 items.  
Required: No

 ** DebugLogging **   
Specifies whether the proxy logs detailed connection and query information. When you enable `DebugLogging`, the proxy captures connection details and connection pool behavior from your queries. Debug logging increases CloudWatch costs and can impact proxy performance. Enable this option only when you need to troubleshoot connection or performance issues.  
Type: Boolean  
Required: No

 ** DefaultAuthScheme **   
The default authentication scheme that the proxy uses for client connections to the proxy and connections from the proxy to the underlying database. Valid values are `NONE` and `IAM_AUTH`. When set to `IAM_AUTH`, the proxy uses end-to-end IAM authentication to connect to the database. If you don't specify `DefaultAuthScheme` or specify this parameter as `NONE`, you must specify the `Auth` option.  
Type: String  
Valid Values: `IAM_AUTH | NONE`   
Required: No

 ** EndpointNetworkType **   
The network type of the DB proxy endpoint. The network type determines the IP version that the proxy endpoint supports.  
Valid values:  
+  `IPV4` - The proxy endpoint supports IPv4 only.
+  `IPV6` - The proxy endpoint supports IPv6 only.
+  `DUAL` - The proxy endpoint supports both IPv4 and IPv6.
Default: `IPV4`   
Constraints:  
+ If you specify `IPV6` or `DUAL`, the VPC and all subnets must have an IPv6 CIDR block.
+ If you specify `IPV6` or `DUAL`, the VPC tenancy cannot be `dedicated`.
Type: String  
Valid Values: `IPV4 | IPV6 | DUAL`   
Required: No

 ** IdleClientTimeout **   
The number of seconds that a connection to the proxy can be inactive before the proxy disconnects it. You can set this value higher or lower than the connection timeout limit for the associated database.  
Type: Integer  
Required: No

 ** RequireTLS **   
Specifies whether Transport Layer Security (TLS) encryption is required for connections to the proxy. By enabling this setting, you can enforce encrypted TLS connections to the proxy.  
Type: Boolean  
Required: No

 **Tags.Tag.N**   
An optional set of key-value pairs to associate arbitrary data of your choosing with the proxy.  
Type: Array of [Tag](API_Tag.md) objects  
Required: No

 ** TargetConnectionNetworkType **   
The network type that the proxy uses to connect to the target database. The network type determines the IP version that the proxy uses for connections to the database.  
Valid values:  
+  `IPV4` - The proxy connects to the database using IPv4 only.
+  `IPV6` - The proxy connects to the database using IPv6 only.
Default: `IPV4`   
Constraints:  
+ If you specify `IPV6`, the database must support dual-stack mode. RDS doesn't support IPv6-only databases.
+ All targets registered with the proxy must be compatible with the specified network type.
Type: String  
Valid Values: `IPV4 | IPV6`   
Required: No

 **VpcSecurityGroupIds.member.N**   
One or more VPC security group IDs to associate with the new proxy.  
Type: Array of strings  
Required: No

## Response Elements
<a name="API_CreateDBProxy_ResponseElements"></a>

The following element is returned by the service.

 ** DBProxy **   
The `DBProxy` structure corresponding to the new proxy.  
Type: [DBProxy](API_DBProxy.md) object

## Errors
<a name="API_CreateDBProxy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBProxyAlreadyExistsFault **   
The specified proxy name must be unique for all proxies owned by your AWS account in the specified AWS Region.  
HTTP Status Code: 400

 ** DBProxyQuotaExceededFault **   
Your AWS account already has the maximum number of proxies in the specified AWS Region.  
HTTP Status Code: 400

 ** InvalidSubnet **   
The requested subnet is invalid, or multiple subnets were requested that are not all in a common VPC.  
HTTP Status Code: 400

## See Also
<a name="API_CreateDBProxy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/CreateDBProxy) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/CreateDBProxy) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/CreateDBProxy) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/CreateDBProxy) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/CreateDBProxy) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/CreateDBProxy) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/CreateDBProxy) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/CreateDBProxy) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/CreateDBProxy) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/CreateDBProxy) 