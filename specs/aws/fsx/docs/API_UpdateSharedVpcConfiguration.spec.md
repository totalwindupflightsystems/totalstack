---
id: "@specs/aws/fsx/docs/API_UpdateSharedVpcConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateSharedVpcConfiguration"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# UpdateSharedVpcConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_UpdateSharedVpcConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateSharedVpcConfiguration
<a name="API_UpdateSharedVpcConfiguration"></a>

Configures whether participant accounts in your organization can create Amazon FSx for NetApp ONTAP Multi-AZ file systems in subnets that are shared by a virtual private cloud (VPC) owner. For more information, see the [Amazon FSx for NetApp ONTAP User Guide](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/maz-shared-vpc.html).

**Note**  
We strongly recommend that participant-created Multi-AZ file systems in the shared VPC are deleted before you disable this feature. Once the feature is disabled, these file systems will enter a `MISCONFIGURED` state and behave like Single-AZ file systems. For more information, see [Important considerations before disabling shared VPC support for Multi-AZ file systems](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/maz-shared-vpc.html#disabling-maz-vpc-sharing).

## Request Syntax
<a name="API_UpdateSharedVpcConfiguration_RequestSyntax"></a>

```
{
   "ClientRequestToken": "{{string}}",
   "EnableFsxRouteTableUpdatesFromParticipantAccounts": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateSharedVpcConfiguration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientRequestToken](#API_UpdateSharedVpcConfiguration_RequestSyntax) **   <a name="FSx-UpdateSharedVpcConfiguration-request-ClientRequestToken"></a>
(Optional) An idempotency token for resource creation, in a string of up to 63 ASCII characters. This token is automatically filled on your behalf when you use the AWS Command Line Interface (AWS CLI) or an AWS SDK.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `[A-za-z0-9_.-]{0,63}$`   
Required: No

 ** [EnableFsxRouteTableUpdatesFromParticipantAccounts](#API_UpdateSharedVpcConfiguration_RequestSyntax) **   <a name="FSx-UpdateSharedVpcConfiguration-request-EnableFsxRouteTableUpdatesFromParticipantAccounts"></a>
Specifies whether participant accounts can create FSx for ONTAP Multi-AZ file systems in shared subnets. Set to `true` to enable or `false` to disable.  
Type: String  
Length Constraints: Minimum length of 4. Maximum length of 5.  
Pattern: `^(?i)(true|false)$`   
Required: No

## Response Syntax
<a name="API_UpdateSharedVpcConfiguration_ResponseSyntax"></a>

```
{
   "EnableFsxRouteTableUpdatesFromParticipantAccounts": "string"
}
```

## Response Elements
<a name="API_UpdateSharedVpcConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EnableFsxRouteTableUpdatesFromParticipantAccounts](#API_UpdateSharedVpcConfiguration_ResponseSyntax) **   <a name="FSx-UpdateSharedVpcConfiguration-response-EnableFsxRouteTableUpdatesFromParticipantAccounts"></a>
Indicates whether participant accounts can create FSx for ONTAP Multi-AZ file systems in shared subnets.  
Type: String  
Length Constraints: Minimum length of 4. Maximum length of 5.  
Pattern: `^(?i)(true|false)$` 

## Errors
<a name="API_UpdateSharedVpcConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequest **   
A generic error indicating a failure with a client request.    
 ** Message **   
A detailed error message.
HTTP Status Code: 400

 ** IncompatibleParameterError **   
The error returned when a second request is received with the same client request token but different parameters settings. A client request token should always uniquely identify a single request.    
 ** Message **   
A detailed error message.  
 ** Parameter **   
A parameter that is incompatible with the earlier request.
HTTP Status Code: 400

 ** InternalServerError **   
A generic error indicating a server-side failure.    
 ** Message **   
A detailed error message.
HTTP Status Code: 500

## See Also
<a name="API_UpdateSharedVpcConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/fsx-2018-03-01/UpdateSharedVpcConfiguration) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/fsx-2018-03-01/UpdateSharedVpcConfiguration) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/UpdateSharedVpcConfiguration) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/fsx-2018-03-01/UpdateSharedVpcConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/UpdateSharedVpcConfiguration) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/fsx-2018-03-01/UpdateSharedVpcConfiguration) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/fsx-2018-03-01/UpdateSharedVpcConfiguration) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/fsx-2018-03-01/UpdateSharedVpcConfiguration) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/fsx-2018-03-01/UpdateSharedVpcConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/UpdateSharedVpcConfiguration) 