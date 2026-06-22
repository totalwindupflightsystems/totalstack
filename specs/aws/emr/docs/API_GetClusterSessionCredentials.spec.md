---
id: "@specs/aws/emr/docs/API_GetClusterSessionCredentials"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetClusterSessionCredentials"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# GetClusterSessionCredentials

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_GetClusterSessionCredentials
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetClusterSessionCredentials
<a name="API_GetClusterSessionCredentials"></a>

Provides temporary, HTTP basic credentials that are associated with a given runtime IAM role and used by a cluster with fine-grained access control activated. You can use these credentials to connect to cluster endpoints that support username and password authentication.

## Request Syntax
<a name="API_GetClusterSessionCredentials_RequestSyntax"></a>

```
{
   "ClusterId": "{{string}}",
   "ExecutionRoleArn": "{{string}}"
}
```

## Request Parameters
<a name="API_GetClusterSessionCredentials_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClusterId](#API_GetClusterSessionCredentials_RequestSyntax) **   <a name="EMR-GetClusterSessionCredentials-request-ClusterId"></a>
The unique identifier of the cluster.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: Yes

 ** [ExecutionRoleArn](#API_GetClusterSessionCredentials_RequestSyntax) **   <a name="EMR-GetClusterSessionCredentials-request-ExecutionRoleArn"></a>
The Amazon Resource Name (ARN) of the runtime role for interactive workload submission on the cluster. The runtime role can be a cross-account IAM role. The runtime role ARN is a combination of account ID, role name, and role type using the following format: `arn:partition:service:region:account:resource`.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Required: No

## Response Syntax
<a name="API_GetClusterSessionCredentials_ResponseSyntax"></a>

```
{
   "Credentials": { ... },
   "ExpiresAt": number
}
```

## Response Elements
<a name="API_GetClusterSessionCredentials_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Credentials](#API_GetClusterSessionCredentials_ResponseSyntax) **   <a name="EMR-GetClusterSessionCredentials-response-Credentials"></a>
The credentials that you can use to connect to cluster endpoints that support username and password authentication.  
Type: [Credentials](API_Credentials.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [ExpiresAt](#API_GetClusterSessionCredentials_ResponseSyntax) **   <a name="EMR-GetClusterSessionCredentials-response-ExpiresAt"></a>
The time when the credentials that are returned by the `GetClusterSessionCredentials` API expire.  
Type: Timestamp

## Errors
<a name="API_GetClusterSessionCredentials_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **   
Indicates that an error occurred while processing the request and that the request was not completed.  
HTTP Status Code: 400

 ** InvalidRequestException **   
This exception occurs when there is something wrong with user input.    
 ** ErrorCode **   
The error code associated with the exception.  
 ** Message **   
The message associated with the exception.
HTTP Status Code: 400

## See Also
<a name="API_GetClusterSessionCredentials_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticmapreduce-2009-03-31/GetClusterSessionCredentials) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticmapreduce-2009-03-31/GetClusterSessionCredentials) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/GetClusterSessionCredentials) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticmapreduce-2009-03-31/GetClusterSessionCredentials) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/GetClusterSessionCredentials) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticmapreduce-2009-03-31/GetClusterSessionCredentials) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticmapreduce-2009-03-31/GetClusterSessionCredentials) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticmapreduce-2009-03-31/GetClusterSessionCredentials) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticmapreduce-2009-03-31/GetClusterSessionCredentials) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/GetClusterSessionCredentials) 