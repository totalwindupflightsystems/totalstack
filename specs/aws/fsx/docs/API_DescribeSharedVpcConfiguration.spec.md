---
id: "@specs/aws/fsx/docs/API_DescribeSharedVpcConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeSharedVpcConfiguration"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# DescribeSharedVpcConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_DescribeSharedVpcConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeSharedVpcConfiguration
<a name="API_DescribeSharedVpcConfiguration"></a>

Indicates whether participant accounts in your organization can create Amazon FSx for NetApp ONTAP Multi-AZ file systems in subnets that are shared by a virtual private cloud (VPC) owner. For more information, see [Creating FSx for ONTAP file systems in shared subnets](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/creating-file-systems.html#fsxn-vpc-shared-subnets). 

## Response Syntax
<a name="API_DescribeSharedVpcConfiguration_ResponseSyntax"></a>

```
{
   "EnableFsxRouteTableUpdatesFromParticipantAccounts": "string"
}
```

## Response Elements
<a name="API_DescribeSharedVpcConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EnableFsxRouteTableUpdatesFromParticipantAccounts](#API_DescribeSharedVpcConfiguration_ResponseSyntax) **   <a name="FSx-DescribeSharedVpcConfiguration-response-EnableFsxRouteTableUpdatesFromParticipantAccounts"></a>
Indicates whether participant accounts can create FSx for ONTAP Multi-AZ file systems in shared subnets.  
Type: String  
Length Constraints: Minimum length of 4. Maximum length of 5.  
Pattern: `^(?i)(true|false)$` 

## Errors
<a name="API_DescribeSharedVpcConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequest **   
A generic error indicating a failure with a client request.    
 ** Message **   
A detailed error message.
HTTP Status Code: 400

 ** InternalServerError **   
A generic error indicating a server-side failure.    
 ** Message **   
A detailed error message.
HTTP Status Code: 500

## See Also
<a name="API_DescribeSharedVpcConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/fsx-2018-03-01/DescribeSharedVpcConfiguration) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/fsx-2018-03-01/DescribeSharedVpcConfiguration) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/DescribeSharedVpcConfiguration) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/fsx-2018-03-01/DescribeSharedVpcConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/DescribeSharedVpcConfiguration) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/fsx-2018-03-01/DescribeSharedVpcConfiguration) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/fsx-2018-03-01/DescribeSharedVpcConfiguration) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/fsx-2018-03-01/DescribeSharedVpcConfiguration) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/fsx-2018-03-01/DescribeSharedVpcConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/DescribeSharedVpcConfiguration) 