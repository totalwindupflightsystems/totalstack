---
id: "@specs/aws/cloudtrail/docs/API_RestoreEventDataStore"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RestoreEventDataStore"
status: active
depends_on:
  - "@specs/aws/cloudtrail/meta"
---

# RestoreEventDataStore

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudtrail/docs/API_RestoreEventDataStore
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RestoreEventDataStore
<a name="API_RestoreEventDataStore"></a>

**Important**  
CloudTrail Lake will no longer be open to new customers starting May 31, 2026. If you would like to use CloudTrail Lake, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [CloudTrail Lake availability change](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake-service-availability-change.html).

Restores a deleted event data store specified by `EventDataStore`, which accepts an event data store ARN. You can only restore a deleted event data store within the seven-day wait period after deletion. Restoring an event data store can take several minutes, depending on the size of the event data store.

## Request Syntax
<a name="API_RestoreEventDataStore_RequestSyntax"></a>

```
{
   "EventDataStore": "{{string}}"
}
```

## Request Parameters
<a name="API_RestoreEventDataStore_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [EventDataStore](#API_RestoreEventDataStore_RequestSyntax) **   <a name="awscloudtrail-RestoreEventDataStore-request-EventDataStore"></a>
The ARN (or the ID suffix of the ARN) of the event data store that you want to restore.  
Type: String  
Length Constraints: Minimum length of 3. Maximum length of 256.  
Pattern: `^[a-zA-Z0-9._/\-:]+$`   
Required: Yes

## Response Syntax
<a name="API_RestoreEventDataStore_ResponseSyntax"></a>

```
{
   "AdvancedEventSelectors": [ 
      { 
         "FieldSelectors": [ 
            { 
               "EndsWith": [ "string" ],
               "Equals": [ "string" ],
               "Field": "string",
               "NotEndsWith": [ "string" ],
               "NotEquals": [ "string" ],
               "NotStartsWith": [ "string" ],
               "StartsWith": [ "string" ]
            }
         ],
         "Name": "string"
      }
   ],
   "BillingMode": "string",
   "CreatedTimestamp": number,
   "EventDataStoreArn": "string",
   "KmsKeyId": "string",
   "MultiRegionEnabled": boolean,
   "Name": "string",
   "OrganizationEnabled": boolean,
   "RetentionPeriod": number,
   "Status": "string",
   "TerminationProtectionEnabled": boolean,
   "UpdatedTimestamp": number
}
```

## Response Elements
<a name="API_RestoreEventDataStore_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AdvancedEventSelectors](#API_RestoreEventDataStore_ResponseSyntax) **   <a name="awscloudtrail-RestoreEventDataStore-response-AdvancedEventSelectors"></a>
The advanced event selectors that were used to select events.  
Type: Array of [AdvancedEventSelector](API_AdvancedEventSelector.md) objects

 ** [BillingMode](#API_RestoreEventDataStore_ResponseSyntax) **   <a name="awscloudtrail-RestoreEventDataStore-response-BillingMode"></a>
The billing mode for the event data store.  
Type: String  
Valid Values: `EXTENDABLE_RETENTION_PRICING | FIXED_RETENTION_PRICING` 

 ** [CreatedTimestamp](#API_RestoreEventDataStore_ResponseSyntax) **   <a name="awscloudtrail-RestoreEventDataStore-response-CreatedTimestamp"></a>
The timestamp of an event data store's creation.  
Type: Timestamp

 ** [EventDataStoreArn](#API_RestoreEventDataStore_ResponseSyntax) **   <a name="awscloudtrail-RestoreEventDataStore-response-EventDataStoreArn"></a>
The event data store ARN.  
Type: String  
Length Constraints: Minimum length of 3. Maximum length of 256.  
Pattern: `^[a-zA-Z0-9._/\-:]+$` 

 ** [KmsKeyId](#API_RestoreEventDataStore_ResponseSyntax) **   <a name="awscloudtrail-RestoreEventDataStore-response-KmsKeyId"></a>
Specifies the AWS KMS key ID that encrypts the events delivered by CloudTrail. The value is a fully specified ARN to a AWS KMS key in the following format.  
 `arn:aws:kms:us-east-2:123456789012:key/12345678-1234-1234-1234-123456789012`   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 350.  
Pattern: `^[a-zA-Z0-9._/\-:]+$` 

 ** [MultiRegionEnabled](#API_RestoreEventDataStore_ResponseSyntax) **   <a name="awscloudtrail-RestoreEventDataStore-response-MultiRegionEnabled"></a>
Indicates whether the event data store is collecting events from all Regions, or only from the Region in which the event data store was created.  
Type: Boolean

 ** [Name](#API_RestoreEventDataStore_ResponseSyntax) **   <a name="awscloudtrail-RestoreEventDataStore-response-Name"></a>
The name of the event data store.  
Type: String  
Length Constraints: Minimum length of 3. Maximum length of 128.  
Pattern: `^[a-zA-Z0-9._\-]+$` 

 ** [OrganizationEnabled](#API_RestoreEventDataStore_ResponseSyntax) **   <a name="awscloudtrail-RestoreEventDataStore-response-OrganizationEnabled"></a>
Indicates whether an event data store is collecting logged events for an organization in AWS Organizations.  
Type: Boolean

 ** [RetentionPeriod](#API_RestoreEventDataStore_ResponseSyntax) **   <a name="awscloudtrail-RestoreEventDataStore-response-RetentionPeriod"></a>
The retention period, in days.  
Type: Integer  
Valid Range: Minimum value of 7. Maximum value of 3653.

 ** [Status](#API_RestoreEventDataStore_ResponseSyntax) **   <a name="awscloudtrail-RestoreEventDataStore-response-Status"></a>
The status of the event data store.  
Type: String  
Valid Values: `CREATED | ENABLED | PENDING_DELETION | STARTING_INGESTION | STOPPING_INGESTION | STOPPED_INGESTION` 

 ** [TerminationProtectionEnabled](#API_RestoreEventDataStore_ResponseSyntax) **   <a name="awscloudtrail-RestoreEventDataStore-response-TerminationProtectionEnabled"></a>
Indicates that termination protection is enabled and the event data store cannot be automatically deleted.  
Type: Boolean

 ** [UpdatedTimestamp](#API_RestoreEventDataStore_ResponseSyntax) **   <a name="awscloudtrail-RestoreEventDataStore-response-UpdatedTimestamp"></a>
The timestamp that shows when an event data store was updated, if applicable. `UpdatedTimestamp` is always either the same or newer than the time shown in `CreatedTimestamp`.  
Type: Timestamp

## Errors
<a name="API_RestoreEventDataStore_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CloudTrailAccessNotEnabledException **   
This exception is thrown when trusted access has not been enabled between AWS CloudTrail and AWS Organizations. For more information, see [How to enable or disable trusted access](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html#orgs_how-to-enable-disable-trusted-access) in the * AWS Organizations User Guide* and [Prepare For Creating a Trail For Your Organization](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/creating-an-organizational-trail-prepare.html) in the * AWS CloudTrail User Guide*.  
HTTP Status Code: 400

 ** EventDataStoreARNInvalidException **   
The specified event data store ARN is not valid or does not map to an event data store in your account.  
HTTP Status Code: 400

 ** EventDataStoreMaxLimitExceededException **   
Your account has used the maximum number of event data stores.  
HTTP Status Code: 400

 ** EventDataStoreNotFoundException **   
The specified event data store was not found.  
HTTP Status Code: 400

 ** InsufficientDependencyServiceAccessPermissionException **   
This exception is thrown when the IAM identity that is used to create the organization resource lacks one or more required permissions for creating an organization resource in a required service.  
HTTP Status Code: 400

 ** InvalidEventDataStoreStatusException **   
The event data store is not in a status that supports the operation.  
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

## See Also
<a name="API_RestoreEventDataStore_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudtrail-2013-11-01/RestoreEventDataStore) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudtrail-2013-11-01/RestoreEventDataStore) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/RestoreEventDataStore) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudtrail-2013-11-01/RestoreEventDataStore) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/RestoreEventDataStore) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudtrail-2013-11-01/RestoreEventDataStore) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudtrail-2013-11-01/RestoreEventDataStore) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudtrail-2013-11-01/RestoreEventDataStore) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudtrail-2013-11-01/RestoreEventDataStore) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/RestoreEventDataStore) 