---
id: "@specs/aws/cloudtrail/docs/API_DeleteEventDataStore"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteEventDataStore"
status: active
depends_on:
  - "@specs/aws/cloudtrail/meta"
---

# DeleteEventDataStore

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudtrail/docs/API_DeleteEventDataStore
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteEventDataStore
<a name="API_DeleteEventDataStore"></a>

**Important**  
CloudTrail Lake will no longer be open to new customers starting May 31, 2026. If you would like to use CloudTrail Lake, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [CloudTrail Lake availability change](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake-service-availability-change.html).

Disables the event data store specified by `EventDataStore`, which accepts an event data store ARN. After you run `DeleteEventDataStore`, the event data store enters a `PENDING_DELETION` state, and is automatically deleted after a wait period of seven days. `TerminationProtectionEnabled` must be set to `False` on the event data store and the `FederationStatus` must be `DISABLED`. You cannot delete an event data store if `TerminationProtectionEnabled` is `True` or the `FederationStatus` is `ENABLED`.

After you run `DeleteEventDataStore` on an event data store, you cannot run `ListQueries`, `DescribeQuery`, or `GetQueryResults` on queries that are using an event data store in a `PENDING_DELETION` state. An event data store in the `PENDING_DELETION` state does not incur costs.

## Request Syntax
<a name="API_DeleteEventDataStore_RequestSyntax"></a>

```
{
   "EventDataStore": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteEventDataStore_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [EventDataStore](#API_DeleteEventDataStore_RequestSyntax) **   <a name="awscloudtrail-DeleteEventDataStore-request-EventDataStore"></a>
The ARN (or the ID suffix of the ARN) of the event data store to delete.  
Type: String  
Length Constraints: Minimum length of 3. Maximum length of 256.  
Pattern: `^[a-zA-Z0-9._/\-:]+$`   
Required: Yes

## Response Elements
<a name="API_DeleteEventDataStore_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteEventDataStore_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ChannelExistsForEDSException **   
This exception is thrown when the specified event data store cannot yet be deleted because it is in use by a channel.  
HTTP Status Code: 400

 ** ConflictException **   
This exception is thrown when the specified resource is not ready for an operation. This can occur when you try to run an operation on a resource before CloudTrail has time to fully load the resource, or because another operation is modifying the resource. If this exception occurs, wait a few minutes, and then try the operation again.  
HTTP Status Code: 400

 ** EventDataStoreARNInvalidException **   
The specified event data store ARN is not valid or does not map to an event data store in your account.  
HTTP Status Code: 400

 ** EventDataStoreFederationEnabledException **   
 You cannot delete the event data store because Lake query federation is enabled. To delete the event data store, run the `DisableFederation` operation to disable Lake query federation on the event data store.   
HTTP Status Code: 400

 ** EventDataStoreHasOngoingImportException **   
 This exception is thrown when you try to update or delete an event data store that currently has an import in progress.   
HTTP Status Code: 400

 ** EventDataStoreNotFoundException **   
The specified event data store was not found.  
HTTP Status Code: 400

 ** EventDataStoreTerminationProtectedException **   
The event data store cannot be deleted because termination protection is enabled for it.  
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

 ** UnsupportedOperationException **   
This exception is thrown when the requested operation is not supported.  
HTTP Status Code: 400

## See Also
<a name="API_DeleteEventDataStore_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudtrail-2013-11-01/DeleteEventDataStore) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudtrail-2013-11-01/DeleteEventDataStore) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/DeleteEventDataStore) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudtrail-2013-11-01/DeleteEventDataStore) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/DeleteEventDataStore) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudtrail-2013-11-01/DeleteEventDataStore) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudtrail-2013-11-01/DeleteEventDataStore) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudtrail-2013-11-01/DeleteEventDataStore) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudtrail-2013-11-01/DeleteEventDataStore) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/DeleteEventDataStore) 