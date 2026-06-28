---
id: "@specs/aws/storagegateway/docs/API_JoinDomain"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS JoinDomain"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# JoinDomain

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_JoinDomain
> **target_lang:** meta — documentation tier. ALL sections preserved.



# JoinDomain
<a name="API_JoinDomain"></a>

Adds a file gateway to an Active Directory domain. This operation is only supported for file gateways that support the SMB file protocol.

**Note**  
Joining a domain creates an Active Directory computer account in the default organizational unit, using the gateway's **Gateway ID** as the account name (for example, SGW-1234ADE). If your Active Directory environment requires that you pre-stage accounts to facilitate the join domain process, you will need to create this account ahead of time.  
To create the gateway's computer account in an organizational unit other than the default, you must specify the organizational unit when joining the domain.

## Request Syntax
<a name="API_JoinDomain_RequestSyntax"></a>

```
{
   "DomainControllers": [ "{{string}}" ],
   "DomainName": "{{string}}",
   "GatewayARN": "{{string}}",
   "OrganizationalUnit": "{{string}}",
   "Password": "{{string}}",
   "TimeoutInSeconds": {{number}},
   "UserName": "{{string}}"
}
```

## Request Parameters
<a name="API_JoinDomain_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DomainControllers](#API_JoinDomain_RequestSyntax) **   <a name="StorageGateway-JoinDomain-request-DomainControllers"></a>
List of IP addresses, NetBIOS names, or host names of your domain server. If you need to specify the port number include it after the colon (“:”). For example, `mydc.mydomain.com:389`.  
S3 File Gateway supports IPv6 addresses in addition to IPv4 and other existing formats.  
FSx File Gateway does not support IPv6.
Type: Array of strings  
Length Constraints: Minimum length of 2. Maximum length of 1024.  
Pattern: `^(([a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9\-]*[A-Za-z0-9])(:(\d+))?$|^(?:\[(?:(?:(?:[A-Fa-f0-9]{1,4}:){6}|(?=(?:[A-Fa-f0-9]{0,4}:){0,6}(?:[0-9]{1,3}\.){3}[0-9]{1,3}(?![:.\w]))(?:(?:[0-9A-Fa-f]{1,4}:){0,5}|:)(?:(?::[0-9A-Fa-f]{1,4}){1,5}:|:)|::(?:[A-Fa-f0-9]{1,4}:){5})(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)|(?:[A-Fa-f0-9]{1,4}:){7}[A-Fa-f0-9]{1,4}|(?=(?:[A-Fa-f0-9]{0,4}:){0,7}[A-Fa-f0-9]{0,4}(?![:.\w]))(?:(?:[0-9A-Fa-f]{1,4}:){1,7}|:)(?:(:[0-9A-Fa-f]{1,4}){1,7}|:)|(?:[A-Fa-f0-9]{1,4}:){7}:|:(:[A-Fa-f0-9]{1,4}){7})\]:\d+$|^(?:(?:(?:[A-Fa-f0-9]{1,4}:){6}|(?=(?:[A-Fa-f0-9]{0,4}:){0,6}(?:[0-9]{1,3}\.){3}[0-9]{1,3}(?![:.\w]))(?:(?:[0-9A-Fa-f]{1,4}:){0,5}|:)(?:(?::[0-9A-Fa-f]{1,4}){1,5}:|:)|::(?:[A-Fa-f0-9]{1,4}:){5})(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)|(?:[A-Fa-f0-9]{1,4}:){7}[A-Fa-f0-9]{1,4}|(?=(?:[A-Fa-f0-9]{0,4}:){0,7}[A-Fa-f0-9]{0,4}(?![:.\w]))(?:(?:[0-9A-Fa-f]{1,4}:){1,7}|:)(?:(:[0-9A-Fa-f]{1,4}){1,7}|:)|(?:[A-Fa-f0-9]{1,4}:){7}:|:(:[A-Fa-f0-9]{1,4}){7})$)`   
Required: No

 ** [DomainName](#API_JoinDomain_RequestSyntax) **   <a name="StorageGateway-JoinDomain-request-DomainName"></a>
The name of the domain that you want the gateway to join.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `^([a-zA-Z0-9]+[\\.-])+([a-zA-Z0-9])+$`   
Required: Yes

 ** [GatewayARN](#API_JoinDomain_RequestSyntax) **   <a name="StorageGateway-JoinDomain-request-GatewayARN"></a>
The Amazon Resource Name (ARN) of the gateway. Use the `ListGateways` operation to return a list of gateways for your account and AWS Region.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Required: Yes

 ** [OrganizationalUnit](#API_JoinDomain_RequestSyntax) **   <a name="StorageGateway-JoinDomain-request-OrganizationalUnit"></a>
The organizational unit (OU) is a container in an Active Directory that can hold users, groups, computers, and other OUs and this parameter specifies the OU that the gateway will join within the AD domain.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Required: No

 ** [Password](#API_JoinDomain_RequestSyntax) **   <a name="StorageGateway-JoinDomain-request-Password"></a>
Sets the password of the user who has permission to add the gateway to the Active Directory domain.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `^[ -~]+$`   
Required: Yes

 ** [TimeoutInSeconds](#API_JoinDomain_RequestSyntax) **   <a name="StorageGateway-JoinDomain-request-TimeoutInSeconds"></a>
Specifies the time in seconds, in which the `JoinDomain` operation must complete. The default is 20 seconds.  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 3600.  
Required: No

 ** [UserName](#API_JoinDomain_RequestSyntax) **   <a name="StorageGateway-JoinDomain-request-UserName"></a>
Sets the user name of user who has permission to add the gateway to the Active Directory domain. The domain user account should be enabled to join computers to the domain. For example, you can use the domain administrator account or an account with delegated permissions to join computers to the domain.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `^\w[\w\.\- ]*$`   
Required: Yes

## Response Syntax
<a name="API_JoinDomain_ResponseSyntax"></a>

```
{
   "ActiveDirectoryStatus": "string",
   "GatewayARN": "string"
}
```

## Response Elements
<a name="API_JoinDomain_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ActiveDirectoryStatus](#API_JoinDomain_ResponseSyntax) **   <a name="StorageGateway-JoinDomain-response-ActiveDirectoryStatus"></a>
Indicates the status of the gateway as a member of the Active Directory domain.  
This field is only used as part of a `JoinDomain` request. It is not affected by Active Directory connectivity changes that occur after the `JoinDomain` request succeeds.
+  `ACCESS_DENIED`: Indicates that the `JoinDomain` operation failed due to an authentication error.
+  `DETACHED`: Indicates that gateway is not joined to a domain.
+  `JOINED`: Indicates that the gateway has successfully joined a domain.
+  `JOINING`: Indicates that a `JoinDomain` operation is in progress.
+  `INSUFFICIENT_PERMISSIONS`: Indicates that the `JoinDomain` operation failed because the specified user lacks the necessary permissions to join the domain.
+  `NETWORK_ERROR`: Indicates that `JoinDomain` operation failed due to a network or connectivity error.
+  `TIMEOUT`: Indicates that the `JoinDomain` operation failed because the operation didn't complete within the allotted time.
+  `UNKNOWN_ERROR`: Indicates that the `JoinDomain` operation failed due to another type of error.
Type: String  
Valid Values: `ACCESS_DENIED | DETACHED | JOINED | JOINING | NETWORK_ERROR | TIMEOUT | UNKNOWN_ERROR | INSUFFICIENT_PERMISSIONS` 

 ** [GatewayARN](#API_JoinDomain_ResponseSyntax) **   <a name="StorageGateway-JoinDomain-response-GatewayARN"></a>
The unique Amazon Resource Name (ARN) of the gateway that joined the domain.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.

## Errors
<a name="API_JoinDomain_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **   
An internal server error has occurred during the request. For more information, see the error and message fields.    
 ** error **   
A [StorageGatewayError](API_StorageGatewayError.md) that provides more information about the cause of the error.  
 ** message **   
A human-readable message describing the error that occurred.
HTTP Status Code: 400

 ** InvalidGatewayRequestException **   
An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.    
 ** error **   
A [StorageGatewayError](API_StorageGatewayError.md) that provides more detail about the cause of the error.  
 ** message **   
A human-readable message describing the error that occurred.
HTTP Status Code: 400

## See Also
<a name="API_JoinDomain_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/storagegateway-2013-06-30/JoinDomain) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/storagegateway-2013-06-30/JoinDomain) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/JoinDomain) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/storagegateway-2013-06-30/JoinDomain) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/JoinDomain) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/storagegateway-2013-06-30/JoinDomain) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/storagegateway-2013-06-30/JoinDomain) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/storagegateway-2013-06-30/JoinDomain) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/storagegateway-2013-06-30/JoinDomain) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/JoinDomain) 