---
id: "@specs/aws/timestream-influxdb/docs/JDBC.url-examples"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS JDBC URL examples"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# JDBC URL examples

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/JDBC.url-examples
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# JDBC URL examples
<a name="JDBC.url-examples"></a>

 This section describes how to create a JDBC connection URL, and provides examples. To specify the [optional connection properties](JDBC.connection-properties.md), use the following URL format:

```
jdbc:timestream://PropertyName1=value1;PropertyName2=value2... 
```

**Note**  
All connection properties are optional. All property keys are case-sensitive.

Below are some examples of JDBC connection URLs.

*Example with basic authentication options and region:*  

```
jdbc:timestream://AccessKeyId=<myAccessKeyId>;SecretAccessKey=<mySecretAccessKey>;SessionToken=<mySessionToken>;Region=us-east-1
```

*Example with client info, region and SDK options:*  

```
jdbc:timestream://ApplicationName=MyApp;Region=us-east-1;MaxRetryCountClient=10;MaxConnections=5000;RequestTimeout=20000
```

*Connect using the default credential provider chain with AWS credential set in environment variables:*  

```
jdbc:timestream
```

*Connect using the default credential provider chain with AWS credential set in the connection URL:*  

```
jdbc:timestream://AccessKeyId=<myAccessKeyId>;SecretAccessKey=<mySecretAccessKey>;SessionToken=<mySessionToken>
```

*Connect using the PropertiesFileCredentialsProvider as the authentication method:*  

```
jdbc:timestream://AwsCredentialsProviderClass=PropertiesFileCredentialsProvider;CustomCredentialsFilePath=<path to properties file>
```

*Connect using the InstanceProfileCredentialsProvider as the authentication method:*  

```
jdbc:timestream://AwsCredentialsProviderClass=InstanceProfileCredentialsProvider
```

*Connect using the Okta credentials as the authentication method:*  

```
jdbc:timestream://IdpName=Okta;IdpHost=<host>;IdpUserName=<name>;IdpPassword=<password>;OktaApplicationID=<id>;RoleARN=<roleARN>;IdpARN=<IdpARN>
```

*Connect using the Azure AD credentials as the authentication method:*  

```
jdbc:timestream://IdpName=AzureAD;IdpUserName=<name>;IdpPassword=<password>;AADApplicationID=<id>;AADClientSecret=<secret>;AADTenant=<tenantID>;IdpARN=<IdpARN>
```

*Connect with a specific endpoint:*  

```
jdbc:timestream://Endpoint=abc.us-east-1.amazonaws.com;Region=us-east-1
```