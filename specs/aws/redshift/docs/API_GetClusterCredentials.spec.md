---
id: "@specs/aws/redshift/docs/API_GetClusterCredentials"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetClusterCredentials"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# GetClusterCredentials

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_GetClusterCredentials
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetClusterCredentials
<a name="API_GetClusterCredentials"></a>

Returns a database user name and temporary password with temporary authorization to log on to an Amazon Redshift database. The action returns the database user name prefixed with `IAM:` if `AutoCreate` is `False` or `IAMA:` if `AutoCreate` is `True`. You can optionally specify one or more database user groups that the user will join at log on. By default, the temporary credentials expire in 900 seconds. You can optionally specify a duration between 900 seconds (15 minutes) and 3600 seconds (60 minutes). For more information, see [Using IAM Authentication to Generate Database User Credentials](https://docs.aws.amazon.com/redshift/latest/mgmt/generating-user-credentials.html) in the Amazon Redshift Cluster Management Guide.

The AWS Identity and Access Management (IAM) user or role that runs GetClusterCredentials must have an IAM policy attached that allows access to all necessary actions and resources. For more information about permissions, see [Resource Policies for GetClusterCredentials](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-identity-based.html#redshift-policy-resources.getclustercredentials-resources) in the Amazon Redshift Cluster Management Guide.

If the `DbGroups` parameter is specified, the IAM policy must allow the `redshift:JoinGroup` action with access to the listed `dbgroups`. 

In addition, if the `AutoCreate` parameter is set to `True`, then the policy must include the `redshift:CreateClusterUser` permission.

If the `DbName` parameter is specified, the IAM policy must allow access to the resource `dbname` for the specified database name. 

## Request Parameters
<a name="API_GetClusterCredentials_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DbUser **   
The name of a database user. If a user name matching `DbUser` exists in the database, the temporary user credentials have the same permissions as the existing user. If `DbUser` doesn't exist in the database and `Autocreate` is `True`, a new user is created using the value for `DbUser` with PUBLIC permissions. If a database user matching the value for `DbUser` doesn't exist and `Autocreate` is `False`, then the command succeeds but the connection attempt will fail because the user doesn't exist in the database.  
For more information, see [CREATE USER](https://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_USER.html) in the Amazon Redshift Database Developer Guide.   
Constraints:  
+ Must be 1 to 64 alphanumeric characters or hyphens. The user name can't be `PUBLIC`.
+ Must contain uppercase or lowercase letters, numbers, underscore, plus sign, period (dot), at symbol (@), or hyphen.
+ First character must be a letter.
+ Must not contain a colon ( : ) or slash ( / ). 
+ Cannot be a reserved word. A list of reserved words can be found in [Reserved Words](http://docs.aws.amazon.com/redshift/latest/dg/r_pg_keywords.html) in the Amazon Redshift Database Developer Guide.
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

 ** AutoCreate **   
Create a database user with the name specified for the user named in `DbUser` if one does not exist.  
Type: Boolean  
Required: No

 ** ClusterIdentifier **   
The unique identifier of the cluster that contains the database for which you are requesting credentials. This parameter is case sensitive.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** CustomDomainName **   
The custom domain name for the cluster credentials.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 **DbGroups.DbGroup.N**   
A list of the names of existing database groups that the user named in `DbUser` will join for the current session, in addition to any group memberships for an existing user. If not specified, a new user is added only to PUBLIC.  
Database group name constraints  
+ Must be 1 to 64 alphanumeric characters or hyphens
+ Must contain only lowercase letters, numbers, underscore, plus sign, period (dot), at symbol (@), or hyphen.
+ First character must be a letter.
+ Must not contain a colon ( : ) or slash ( / ). 
+ Cannot be a reserved word. A list of reserved words can be found in [Reserved Words](http://docs.aws.amazon.com/redshift/latest/dg/r_pg_keywords.html) in the Amazon Redshift Database Developer Guide.
Type: Array of strings  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** DbName **   
The name of a database that `DbUser` is authorized to log on to. If `DbName` is not specified, `DbUser` can log on to any existing database.  
Constraints:  
+ Must be 1 to 64 alphanumeric characters or hyphens
+ Must contain uppercase or lowercase letters, numbers, underscore, plus sign, period (dot), at symbol (@), or hyphen.
+ First character must be a letter.
+ Must not contain a colon ( : ) or slash ( / ). 
+ Cannot be a reserved word. A list of reserved words can be found in [Reserved Words](http://docs.aws.amazon.com/redshift/latest/dg/r_pg_keywords.html) in the Amazon Redshift Database Developer Guide.
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** DurationSeconds **   
The number of seconds until the returned temporary password expires.  
Constraint: minimum 900, maximum 3600.  
Default: 900  
Type: Integer  
Required: No

## Response Elements
<a name="API_GetClusterCredentials_ResponseElements"></a>

The following elements are returned by the service.

 ** DbPassword **   
A temporary password that authorizes the user name returned by `DbUser` to log on to the database `DbName`.   
Type: String

 ** DbUser **   
A database user name that is authorized to log on to the database `DbName` using the password `DbPassword`. If the specified DbUser exists in the database, the new user name has the same database permissions as the the user named in DbUser. By default, the user is added to PUBLIC. If the `DbGroups` parameter is specifed, `DbUser` is added to the listed groups for any sessions created using these credentials.  
Type: String  
Length Constraints: Maximum length of 2147483647.

 ** Expiration **   
The date and time the password in `DbPassword` expires.  
Type: Timestamp

## Errors
<a name="API_GetClusterCredentials_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ClusterNotFound **   
The `ClusterIdentifier` parameter does not refer to an existing cluster.   
HTTP Status Code: 404

 ** UnsupportedOperation **   
The requested operation isn't supported.  
HTTP Status Code: 400

## Examples
<a name="API_GetClusterCredentials_Examples"></a>

### Example
<a name="API_GetClusterCredentials_Example_1"></a>

This example illustrates one usage of GetClusterCredentials.

#### Sample Request
<a name="API_GetClusterCredentials_Example_1_Request"></a>

```
https://redshift.us-east-2.amazonaws.com/
       ?Action=GetClusterCredentials
&ClusterIdentifier=mycluster
&DbUser=adminuser
&DbName=dev
&SignatureMethod=HmacSHA256&SignatureVersion=4
&Version=2012-12-01
&X-Amz-Algorithm=AWS4-HMAC-SHA256
&X-Amz-Credential=AKIAIOSFODNN7EXAMPLE/20190817/us-east-2/redshift/aws4_request
&X-Amz-Date=20190825T160000Z
&X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
&X-Amz-Signature=0aa1234bb5cc678ddddd901ee2ff3aa45678b90c12d345e6ff789012345a6b7b
```

#### Sample Response
<a name="API_GetClusterCredentials_Example_1_Response"></a>

```
<GetClusterCredentialsResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">
  <GetClusterCredentialsResult>
    <DbUser>IAM:adminuser</DbUser>
    <Expiration>2019-12-27T19:44:51.001Z</Expiration>
    <DbPassword>AMAFUyyuros/QjxPTtgzcsuQsqzIasdzJEN04aCtWDzXx1O9d6UmpkBtvEeqFly/EXAMPLE==</DbPassword>
  </GetClusterCredentialsResult>
  <ResponseMetadata>
    <RequestId>404b34b9-28df-11ea-a940-1b28a85fd753</RequestId>
  </ResponseMetadata>
</GetClusterCredentialsResponse>
```

## See Also
<a name="API_GetClusterCredentials_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/GetClusterCredentials) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/GetClusterCredentials) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/GetClusterCredentials) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/GetClusterCredentials) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/GetClusterCredentials) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/GetClusterCredentials) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/GetClusterCredentials) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/GetClusterCredentials) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/GetClusterCredentials) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/GetClusterCredentials) 