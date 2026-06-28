---
id: "@specs/aws/globalaccelerator/docs/API_DeleteCustomRoutingAccelerator"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteCustomRoutingAccelerator"
status: active
depends_on:
  - "@specs/aws/globalaccelerator/meta"
---

# DeleteCustomRoutingAccelerator

> **source:** AWS Documentation
> **spec:id:** @specs/aws/globalaccelerator/docs/API_DeleteCustomRoutingAccelerator
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteCustomRoutingAccelerator
<a name="API_DeleteCustomRoutingAccelerator"></a>

Delete a custom routing accelerator. Before you can delete an accelerator, you must disable it and remove all dependent resources (listeners and endpoint groups). To disable the accelerator, update the accelerator to set `Enabled` to false.

**Important**  
When you create a custom routing accelerator, by default, Global Accelerator provides you with a set of two static IP addresses.   
The IP addresses are assigned to your accelerator for as long as it exists, even if you disable the accelerator and it no longer accepts or routes traffic. However, when you *delete* an accelerator, you lose the static IP addresses that are assigned to the accelerator, so you can no longer route traffic by using them. As a best practice, ensure that you have permissions in place to avoid inadvertently deleting accelerators. You can use IAM policies with Global Accelerator to limit the users who have permissions to delete an accelerator. For more information, see [Identity and access management](https://docs.aws.amazon.com/global-accelerator/latest/dg/auth-and-access-control.html) in the * AWS Global Accelerator Developer Guide*.

## Request Syntax
<a name="API_DeleteCustomRoutingAccelerator_RequestSyntax"></a>

```
{
   "AcceleratorArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteCustomRoutingAccelerator_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AcceleratorArn](#API_DeleteCustomRoutingAccelerator_RequestSyntax) **   <a name="globalaccelerator-DeleteCustomRoutingAccelerator-request-AcceleratorArn"></a>
The Amazon Resource Name (ARN) of the custom routing accelerator to delete.  
Type: String  
Length Constraints: Maximum length of 255.  
Required: Yes

## Response Elements
<a name="API_DeleteCustomRoutingAccelerator_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteCustomRoutingAccelerator_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AcceleratorNotDisabledException **   
The accelerator that you specified could not be disabled.  
HTTP Status Code: 400

 ** AcceleratorNotFoundException **   
The accelerator that you specified doesn't exist.  
HTTP Status Code: 400

 ** AssociatedListenerFoundException **   
The accelerator that you specified has a listener associated with it. You must remove all dependent resources from an accelerator before you can delete it.  
HTTP Status Code: 400

 ** InternalServiceErrorException **   
There was an internal error for AWS Global Accelerator.  
HTTP Status Code: 400

 ** InvalidArgumentException **   
An argument that you specified is invalid.  
HTTP Status Code: 400

 ** TransactionInProgressException **   
There's already a transaction in progress. Another transaction can't be processed.  
HTTP Status Code: 400

## See Also
<a name="API_DeleteCustomRoutingAccelerator_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/globalaccelerator-2018-08-08/DeleteCustomRoutingAccelerator) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/globalaccelerator-2018-08-08/DeleteCustomRoutingAccelerator) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/globalaccelerator-2018-08-08/DeleteCustomRoutingAccelerator) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/globalaccelerator-2018-08-08/DeleteCustomRoutingAccelerator) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/globalaccelerator-2018-08-08/DeleteCustomRoutingAccelerator) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/globalaccelerator-2018-08-08/DeleteCustomRoutingAccelerator) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/globalaccelerator-2018-08-08/DeleteCustomRoutingAccelerator) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/globalaccelerator-2018-08-08/DeleteCustomRoutingAccelerator) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/globalaccelerator-2018-08-08/DeleteCustomRoutingAccelerator) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/globalaccelerator-2018-08-08/DeleteCustomRoutingAccelerator) 