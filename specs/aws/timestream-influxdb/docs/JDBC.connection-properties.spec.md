---
id: "@specs/aws/timestream-influxdb/docs/JDBC.connection-properties"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Connection properties"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Connection properties

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/JDBC.connection-properties
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Connection properties
<a name="JDBC.connection-properties"></a>

 The Timestream for LiveAnalytics JDBC driver supports the following options: 

**Topics**
+ [Basic authentication options](#JDBC.connection-properties.basic-auth)
+ [Standard client info option](#JDBC.connection-properties.standard-client)
+ [Driver configuration option](#JDBC.connection-properties.driver-config)
+ [SDK option](#JDBC.connection-properties.sdk-options)
+ [Endpoint configuration option](#JDBC.connection-properties.endpoint-config)
+ [Credential provider options](#JDBC.connection-properties.cred-providers)
+ [SAML-based authentication options for Okta](#JDBC.connection-properties.okta)
+ [SAML-based authentication options for Azure AD](#JDBC.connection-properties.azure-ad)

**Note**  
 If none of the properties are provided, the Timestream for LiveAnalytics JDBC driver will use the default credentials chain to load the credentials. 

**Note**  
 All property keys are case-sensitive. 

## Basic authentication options
<a name="JDBC.connection-properties.basic-auth"></a>

The following table describes the available Basic Authentication options.


| Option | Description | Default | 
| --- | --- | --- | 
| AccessKeyId | The AWS user access key id. | NONE | 
| SecretAccessKey | The AWS user secret access key. | NONE | 
| SessionToken | The temporary session token required to access a database with multi-factor authentication (MFA) enabled. | NONE | 

## Standard client info option
<a name="JDBC.connection-properties.standard-client"></a>

The following table describes the Standard Client Info Option.


| Option | Description | Default | 
| --- | --- | --- | 
| ApplicationName | The name of the application currently utilizing the connection. `ApplicationName` is used for debugging purposes and will not be communicated to the Timestream for LiveAnalytics service. | The application name detected by the driver. | 

## Driver configuration option
<a name="JDBC.connection-properties.driver-config"></a>

The following table describes the Driver Configuration Option.


| Option | Description | Default | 
| --- | --- | --- | 
| EnableMetaDataPreparedStatement | Enables Timestream for LiveAnalytics JDBC driver to return metadata for `PreparedStatements`, but this will incur an additional cost with Timestream for LiveAnalytics when retrieving the metadata. | FALSE | 
| Region | The database's region. | us-east-1 | 

## SDK option
<a name="JDBC.connection-properties.sdk-options"></a>

The following table describes the SDK Option.


| Option | Description | Default | 
| --- | --- | --- | 
| RequestTimeout | The time in milliseconds the AWS SDK will wait for a query request before timing out. Non-positive value disables request timeout. | 0 | 
| SocketTimeout | The time in milliseconds the AWS SDK will wait for data to be transferred over an open connection before timing out. Value must be non-negative. A value of `0` disables socket timeout. | 50000 | 
| MaxRetryCountClient | The maximum number of retry attempts for retryable errors with 5XX error codes in the SDK. The value must be non-negative. | NONE | 
| MaxConnections | The maximum number of allowed concurrently opened HTTP connections to the Timestream for LiveAnalytics service. The value must be positive. | 50 | 

## Endpoint configuration option
<a name="JDBC.connection-properties.endpoint-config"></a>

The following table describes the Endpoint Configuration Option.


| Option | Description | Default | 
| --- | --- | --- | 
| Endpoint | The endpoint for the Timestream for LiveAnalytics service. | NONE | 

## Credential provider options
<a name="JDBC.connection-properties.cred-providers"></a>

The following table describes the available Credential Provider options.


| Option | Description | Default | 
| --- | --- | --- | 
| AwsCredentialsProviderClass | One of `PropertiesFileCredentialsProvider` or `InstanceProfileCredentialsProvider` to use for authentication. | NONE | 
| CustomCredentialsFilePath | The path to a properties file containing AWS security credentials `accessKey` and `secretKey`. This is only required if `AwsCredentialsProviderClass` is specified as `PropertiesFileCredentialsProvider` . | NONE | 

## SAML-based authentication options for Okta
<a name="JDBC.connection-properties.okta"></a>

The following table describes the available SAML-based authentication options for Okta.


| Option | Description | Default | 
| --- | --- | --- | 
| IdpName | The Identity Provider (Idp) name to use for SAML-based authentication. One of `Okta` or `AzureAD`. | NONE | 
| IdpHost | The host name of the specified Idp. | NONE | 
| IdpUserName | The user name for the specified Idp account. | NONE | 
| IdpPassword | The password for the specified Idp account. | NONE | 
| OktaApplicationID | The unique Okta-provided ID associated with the Timestream for LiveAnalytics application. `AppId` can be found in the `entityID` field provided in the application metadata. Consider the following example: `entityID = http://www.okta.com//IdpAppID` | NONE | 
| RoleARN | The Amazon Resource Name (ARN) of the role that the caller is assuming. | NONE | 
| IdpARN | The Amazon Resource Name (ARN) of the SAML provider in IAM that describes the Idp. | NONE | 

## SAML-based authentication options for Azure AD
<a name="JDBC.connection-properties.azure-ad"></a>

The following table describes the available SAML-based authentication options for Azure AD.


| Option | Description | Default | 
| --- | --- | --- | 
| IdpName | The Identity Provider (Idp) name to use for SAML-based authentication. One of `Okta` or `AzureAD` . | NONE | 
| IdpHost | The host name of the specified Idp. | NONE | 
| IdpUserName | The user name for the specified Idp account. | NONE | 
| IdpPassword | The password for the specified Idp account. | NONE | 
| AADApplicationID | The unique id of the registered application on Azure AD. | NONE | 
| AADClientSecret | The client secret associated with the registered application on Azure AD used to authorize fetching tokens. | NONE | 
| AADTenant | The Azure AD Tenant ID. | NONE | 
| IdpARN | The Amazon Resource Name (ARN) of the SAML provider in IAM that describes the Idp. | NONE | 