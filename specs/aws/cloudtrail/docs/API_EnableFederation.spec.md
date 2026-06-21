---
id: "@specs/aws/cloudtrail/docs/API_EnableFederation"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS EnableFederation"
status: active
depends_on:
  - "@specs/aws/cloudtrail/meta"
---

# EnableFederation

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudtrail/docs/API_EnableFederation
> **target_lang:** meta — documentation tier. ALL sections preserved.



# EnableFederation
<a name="API_EnableFederation"></a>

**Important**  
CloudTrail Lake will no longer be open to new customers starting May 31, 2026. If you would like to use CloudTrail Lake, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [CloudTrail Lake availability change](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake-service-availability-change.html).

 Enables Lake query federation on the specified event data store. Federating an event data store lets you view the metadata associated with the event data store in the AWS Glue [Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/components-overview.html#data-catalog-intro) and run SQL queries against your event data using Amazon Athena. The table metadata stored in the AWS Glue Data Catalog lets the Athena query engine know how to find, read, and process the data that you want to query.

When you enable Lake query federation, CloudTrail creates a managed database named `aws:cloudtrail` (if the database doesn't already exist) and a managed federated table in the AWS Glue Data Catalog. The event data store ID is used for the table name. CloudTrail registers the role ARN and event data store in [AWS Lake Formation](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/query-federation-lake-formation.html), the service responsible for allowing fine-grained access control of the federated resources in the AWS Glue Data Catalog.

For more information about Lake query federation, see [Federate an event data store](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/query-federation.html).

## Request Syntax
<a name="API_EnableFederation_RequestSyntax"></a>

```
{
   "EventDataStore": "{{string}}",
   "FederationRoleArn": "{{string}}"
}
```

## Request Parameters
<a name="API_EnableFederation_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [EventDataStore](#API_EnableFederation_RequestSyntax) **   <a name="awscloudtrail-EnableFederation-request-EventDataStore"></a>
The ARN (or ID suffix of the ARN) of the event data store for which you want to enable Lake query federation.  
Type: String  
Length Constraints: Minimum length of 3. Maximum length of 256.  
Pattern: `^[a-zA-Z0-9._/\-:]+$`   
Required: Yes

 ** [FederationRoleArn](#API_EnableFederation_RequestSyntax) **   <a name="awscloudtrail-EnableFederation-request-FederationRoleArn"></a>
 The ARN of the federation role to use for the event data store. AWS services like AWS Lake Formation use this federation role to access data for the federated event data store. The federation role must exist in your account and provide the [required minimum permissions](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/query-federation.html#query-federation-permissions-role).   
Type: String  
Length Constraints: Minimum length of 3. Maximum length of 125.  
Pattern: `^[a-zA-Z0-9._/\-:@=\+,\.]+$`   
Required: Yes

## Response Syntax
<a name="API_EnableFederation_ResponseSyntax"></a>

```
{
   "EventDataStoreArn": "string",
   "FederationRoleArn": "string",
   "FederationStatus": "string"
}
```

## Response Elements
<a name="API_EnableFederation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EventDataStoreArn](#API_EnableFederation_ResponseSyntax) **   <a name="awscloudtrail-EnableFederation-response-EventDataStoreArn"></a>
 The ARN of the event data store for which you enabled Lake query federation.   
Type: String  
Length Constraints: Minimum length of 3. Maximum length of 256.  
Pattern: `^[a-zA-Z0-9._/\-:]+$` 

 ** [FederationRoleArn](#API_EnableFederation_ResponseSyntax) **   <a name="awscloudtrail-EnableFederation-response-FederationRoleArn"></a>
 The ARN of the federation role.   
Type: String  
Length Constraints: Minimum length of 3. Maximum length of 125.  
Pattern: `^[a-zA-Z0-9._/\-:@=\+,\.]+$` 

 ** [FederationStatus](#API_EnableFederation_ResponseSyntax) **   <a name="awscloudtrail-EnableFederation-response-FederationStatus"></a>
 The federation status.   
Type: String  
Valid Values: `ENABLING | ENABLED | DISABLING | DISABLED` 

## Errors
<a name="API_EnableFederation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
 You do not have sufficient access to perform this action.   
HTTP Status Code: 400

 ** CloudTrailAccessNotEnabledException **   
This exception is thrown when trusted access has not been enabled between AWS CloudTrail and AWS Organizations. For more information, see [How to enable or disable trusted access](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html#orgs_how-to-enable-disable-trusted-access) in the * AWS Organizations User Guide* and [Prepare For Creating a Trail For Your Organization](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/creating-an-organizational-trail-prepare.html) in the * AWS CloudTrail User Guide*.  
HTTP Status Code: 400

 ** ConcurrentModificationException **   
 You are trying to update a resource when another request is in progress. Allow sufficient wait time for the previous request to complete, then retry your request.   
HTTP Status Code: 400

 ** EventDataStoreARNInvalidException **   
The specified event data store ARN is not valid or does not map to an event data store in your account.  
HTTP Status Code: 400

 ** EventDataStoreFederationEnabledException **   
 You cannot delete the event data store because Lake query federation is enabled. To delete the event data store, run the `DisableFederation` operation to disable Lake query federation on the event data store.   
HTTP Status Code: 400

 ** EventDataStoreNotFoundException **   
The specified event data store was not found.  
HTTP Status Code: 400

 ** InactiveEventDataStoreException **   
The event data store is inactive.  
HTTP Status Code: 400

 ** InsufficientDependencyServiceAccessPermissionException **   
This exception is thrown when the IAM identity that is used to create the organization resource lacks one or more required permissions for creating an organization resource in a required service.  
HTTP Status Code: 400

 ** InvalidParameterException **   
The request includes a parameter that is not valid.  
HTTP Status Code: 400

 ** NoManagementAccountSLRExistsException **   
 This exception is thrown when the management account does not have a service-linked role.   
HTTP Status Code: 400

 ** NotOrganizationMasterAccountException **   
This exception is thrown when the AWS account making the request to create or update an organization trail or event data store is not the management account for an organization in AWS Organizations. For more information, see [Prepare For Creating a Trail For Your Organization](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/creating-an-organizational-trail-prepare.html) or [Organization event data stores](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake-organizations.html).  
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

## Examples
<a name="API_EnableFederation_Examples"></a>

### Example
<a name="API_EnableFederation_Example_1"></a>

The following example shows how to enable CloudTrail Lake federation on an event data store.

```
{
   "EventDataStore": "arn:aws:cloudtrail:us-east-2:123456789012:eventdatastore/EXAMPLE-f852-4e8f-8bd1-bcf6cEXAMPLE",
   "FederationRoleArn": "arn:aws:iam::123456789012:role/FederationRole"
}
```

## See Also
<a name="API_EnableFederation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudtrail-2013-11-01/EnableFederation) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudtrail-2013-11-01/EnableFederation) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/EnableFederation) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudtrail-2013-11-01/EnableFederation) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/EnableFederation) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudtrail-2013-11-01/EnableFederation) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudtrail-2013-11-01/EnableFederation) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudtrail-2013-11-01/EnableFederation) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudtrail-2013-11-01/EnableFederation) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/EnableFederation) 