---
id: "@specs/aws/cloudtrail/docs/API_RegisterOrganizationDelegatedAdmin"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RegisterOrganizationDelegatedAdmin"
status: active
depends_on:
  - "@specs/aws/cloudtrail/meta"
---

# RegisterOrganizationDelegatedAdmin

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudtrail/docs/API_RegisterOrganizationDelegatedAdmin
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RegisterOrganizationDelegatedAdmin
<a name="API_RegisterOrganizationDelegatedAdmin"></a>

Registers an organization’s member account as the CloudTrail [delegated administrator](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-delegated-administrator.html).

## Request Syntax
<a name="API_RegisterOrganizationDelegatedAdmin_RequestSyntax"></a>

```
{
   "MemberAccountId": "{{string}}"
}
```

## Request Parameters
<a name="API_RegisterOrganizationDelegatedAdmin_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MemberAccountId](#API_RegisterOrganizationDelegatedAdmin_RequestSyntax) **   <a name="awscloudtrail-RegisterOrganizationDelegatedAdmin-request-MemberAccountId"></a>
An organization member account ID that you want to designate as a delegated administrator.  
Type: String  
Length Constraints: Minimum length of 12. Maximum length of 16.  
Pattern: `\d+`   
Required: Yes

## Response Elements
<a name="API_RegisterOrganizationDelegatedAdmin_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_RegisterOrganizationDelegatedAdmin_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccountNotFoundException **   
This exception is thrown when the specified account is not found or not part of an organization.  
HTTP Status Code: 400

 ** AccountRegisteredException **   
This exception is thrown when the account is already registered as the CloudTrail delegated administrator.  
HTTP Status Code: 400

 ** CannotDelegateManagementAccountException **   
This exception is thrown when the management account of an organization is registered as the CloudTrail delegated administrator.  
HTTP Status Code: 400

 ** CloudTrailAccessNotEnabledException **   
This exception is thrown when trusted access has not been enabled between AWS CloudTrail and AWS Organizations. For more information, see [How to enable or disable trusted access](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html#orgs_how-to-enable-disable-trusted-access) in the * AWS Organizations User Guide* and [Prepare For Creating a Trail For Your Organization](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/creating-an-organizational-trail-prepare.html) in the * AWS CloudTrail User Guide*.  
HTTP Status Code: 400

 ** ConflictException **   
This exception is thrown when the specified resource is not ready for an operation. This can occur when you try to run an operation on a resource before CloudTrail has time to fully load the resource, or because another operation is modifying the resource. If this exception occurs, wait a few minutes, and then try the operation again.  
HTTP Status Code: 400

 ** DelegatedAdminAccountLimitExceededException **   
This exception is thrown when the maximum number of CloudTrail delegated administrators is reached.  
HTTP Status Code: 400

 ** InsufficientDependencyServiceAccessPermissionException **   
This exception is thrown when the IAM identity that is used to create the organization resource lacks one or more required permissions for creating an organization resource in a required service.  
HTTP Status Code: 400

 ** InsufficientIAMAccessPermissionException **   
The task can't be completed because you are signed in with an account that lacks permissions to view or create a service-linked role. Sign in with an account that has the required permissions and then try again.  
HTTP Status Code: 400

 ** InvalidParameterException **   
The request includes a parameter that is not valid.  
HTTP Status Code: 400

 ** NotOrganizationManagementAccountException **   
 This exception is thrown when the account making the request is not the organization's management account.   
HTTP Status Code: 400

 ** OperationNotPermittedException **   
This exception is thrown when the requested operation is not permitted.  
HTTP Status Code: 400

 ** OrganizationNotInAllFeaturesModeException **   
This exception is thrown when AWS Organizations is not configured to support all features. All features must be enabled in Organizations to support creating an organization trail or event data store.  
HTTP Status Code: 400

 ** OrganizationsNotInUseException **   
This exception is thrown when the request is made from an AWS account that is not a member of an organization. To make this request, sign in using the credentials of an account that belongs to an organization.  
HTTP Status Code: 400

 ** UnsupportedOperationException **   
This exception is thrown when the requested operation is not supported.  
HTTP Status Code: 400

## See Also
<a name="API_RegisterOrganizationDelegatedAdmin_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudtrail-2013-11-01/RegisterOrganizationDelegatedAdmin) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudtrail-2013-11-01/RegisterOrganizationDelegatedAdmin) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/RegisterOrganizationDelegatedAdmin) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudtrail-2013-11-01/RegisterOrganizationDelegatedAdmin) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/RegisterOrganizationDelegatedAdmin) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudtrail-2013-11-01/RegisterOrganizationDelegatedAdmin) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudtrail-2013-11-01/RegisterOrganizationDelegatedAdmin) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudtrail-2013-11-01/RegisterOrganizationDelegatedAdmin) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudtrail-2013-11-01/RegisterOrganizationDelegatedAdmin) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/RegisterOrganizationDelegatedAdmin) 