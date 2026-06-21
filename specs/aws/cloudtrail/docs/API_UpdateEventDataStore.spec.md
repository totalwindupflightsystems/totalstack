---
id: "@specs/aws/cloudtrail/docs/API_UpdateEventDataStore"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateEventDataStore"
status: active
depends_on:
  - "@specs/aws/cloudtrail/meta"
---

# UpdateEventDataStore

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudtrail/docs/API_UpdateEventDataStore
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateEventDataStore
<a name="API_UpdateEventDataStore"></a>

**Important**  
CloudTrail Lake will no longer be open to new customers starting May 31, 2026. If you would like to use CloudTrail Lake, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [CloudTrail Lake availability change](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake-service-availability-change.html).

Updates an event data store. The required `EventDataStore` value is an ARN or the ID portion of the ARN. Other parameters are optional, but at least one optional parameter must be specified, or CloudTrail throws an error. `RetentionPeriod` is in days, and valid values are integers between 7 and 3653 if the `BillingMode` is set to `EXTENDABLE_RETENTION_PRICING`, or between 7 and 2557 if `BillingMode` is set to `FIXED_RETENTION_PRICING`. By default, `TerminationProtection` is enabled.

For event data stores for CloudTrail events, `AdvancedEventSelectors` includes or excludes management, data, or network activity events in your event data store. For more information about `AdvancedEventSelectors`, see [AdvancedEventSelectors](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_AdvancedEventSelector.html).

 For event data stores for CloudTrail Insights events, AWS Config configuration items, Audit Manager evidence, or non-AWS events, `AdvancedEventSelectors` includes events of that type in your event data store.

## Request Syntax
<a name="API_UpdateEventDataStore_RequestSyntax"></a>

```
{
   "AdvancedEventSelectors": [ 
      { 
         "FieldSelectors": [ 
            { 
               "EndsWith": [ "{{string}}" ],
               "Equals": [ "{{string}}" ],
               "Field": "{{string}}",
               "NotEndsWith": [ "{{string}}" ],
               "NotEquals": [ "{{string}}" ],
               "NotStartsWith": [ "{{string}}" ],
               "StartsWith": [ "{{string}}" ]
            }
         ],
         "Name": "{{string}}"
      }
   ],
   "BillingMode": "{{string}}",
   "EventDataStore": "{{string}}",
   "KmsKeyId": "{{string}}",
   "MultiRegionEnabled": {{boolean}},
   "Name": "{{string}}",
   "OrganizationEnabled": {{boolean}},
   "RetentionPeriod": {{number}},
   "TerminationProtectionEnabled": {{boolean}}
}
```

## Request Parameters
<a name="API_UpdateEventDataStore_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AdvancedEventSelectors](#API_UpdateEventDataStore_RequestSyntax) **   <a name="awscloudtrail-UpdateEventDataStore-request-AdvancedEventSelectors"></a>
The advanced event selectors used to select events for the event data store. You can configure up to five advanced event selectors for each event data store.  
Type: Array of [AdvancedEventSelector](API_AdvancedEventSelector.md) objects  
Required: No

 ** [BillingMode](#API_UpdateEventDataStore_RequestSyntax) **   <a name="awscloudtrail-UpdateEventDataStore-request-BillingMode"></a>
You can't change the billing mode from `EXTENDABLE_RETENTION_PRICING` to `FIXED_RETENTION_PRICING`. If `BillingMode` is set to `EXTENDABLE_RETENTION_PRICING` and you want to use `FIXED_RETENTION_PRICING` instead, you'll need to stop ingestion on the event data store and create a new event data store that uses `FIXED_RETENTION_PRICING`.
The billing mode for the event data store determines the cost for ingesting events and the default and maximum retention period for the event data store.  
The following are the possible values:  
+  `EXTENDABLE_RETENTION_PRICING` - This billing mode is generally recommended if you want a flexible retention period of up to 3653 days (about 10 years). The default retention period for this billing mode is 366 days.
+  `FIXED_RETENTION_PRICING` - This billing mode is recommended if you expect to ingest more than 25 TB of event data per month and need a retention period of up to 2557 days (about 7 years). The default retention period for this billing mode is 2557 days.
For more information about CloudTrail pricing, see [AWS CloudTrail Pricing](http://aws.amazon.com/cloudtrail/pricing/) and [Managing CloudTrail Lake costs](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake-manage-costs.html).  
Type: String  
Valid Values: `EXTENDABLE_RETENTION_PRICING | FIXED_RETENTION_PRICING`   
Required: No

 ** [EventDataStore](#API_UpdateEventDataStore_RequestSyntax) **   <a name="awscloudtrail-UpdateEventDataStore-request-EventDataStore"></a>
The ARN (or the ID suffix of the ARN) of the event data store that you want to update.  
Type: String  
Length Constraints: Minimum length of 3. Maximum length of 256.  
Pattern: `^[a-zA-Z0-9._/\-:]+$`   
Required: Yes

 ** [KmsKeyId](#API_UpdateEventDataStore_RequestSyntax) **   <a name="awscloudtrail-UpdateEventDataStore-request-KmsKeyId"></a>
Specifies the AWS KMS key ID to use to encrypt the events delivered by CloudTrail. The value can be an alias name prefixed by `alias/`, a fully specified ARN to an alias, a fully specified ARN to a key, or a globally unique identifier.  
Disabling or deleting the KMS key, or removing CloudTrail permissions on the key, prevents CloudTrail from logging events to the event data store, and prevents users from querying the data in the event data store that was encrypted with the key. After you associate an event data store with a KMS key, the KMS key cannot be removed or changed. Before you disable or delete a KMS key that you are using with an event data store, delete or back up your event data store.
CloudTrail also supports AWS KMS multi-Region keys. For more information about multi-Region keys, see [Using multi-Region keys](https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html) in the * AWS Key Management Service Developer Guide*.  
Examples:  
+  `alias/MyAliasName` 
+  `arn:aws:kms:us-east-2:123456789012:alias/MyAliasName` 
+  `arn:aws:kms:us-east-2:123456789012:key/12345678-1234-1234-1234-123456789012` 
+  `12345678-1234-1234-1234-123456789012` 
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 350.  
Pattern: `^[a-zA-Z0-9._/\-:]+$`   
Required: No

 ** [MultiRegionEnabled](#API_UpdateEventDataStore_RequestSyntax) **   <a name="awscloudtrail-UpdateEventDataStore-request-MultiRegionEnabled"></a>
Specifies whether an event data store collects events from all Regions, or only from the Region in which it was created.  
Type: Boolean  
Required: No

 ** [Name](#API_UpdateEventDataStore_RequestSyntax) **   <a name="awscloudtrail-UpdateEventDataStore-request-Name"></a>
The event data store name.  
Type: String  
Length Constraints: Minimum length of 3. Maximum length of 128.  
Pattern: `^[a-zA-Z0-9._\-]+$`   
Required: No

 ** [OrganizationEnabled](#API_UpdateEventDataStore_RequestSyntax) **   <a name="awscloudtrail-UpdateEventDataStore-request-OrganizationEnabled"></a>
Specifies whether an event data store collects events logged for an organization in AWS Organizations.  
Only the management account for the organization can convert an organization event data store to a non-organization event data store, or convert a non-organization event data store to an organization event data store.
Type: Boolean  
Required: No

 ** [RetentionPeriod](#API_UpdateEventDataStore_RequestSyntax) **   <a name="awscloudtrail-UpdateEventDataStore-request-RetentionPeriod"></a>
The retention period of the event data store, in days. If `BillingMode` is set to `EXTENDABLE_RETENTION_PRICING`, you can set a retention period of up to 3653 days, the equivalent of 10 years. If `BillingMode` is set to `FIXED_RETENTION_PRICING`, you can set a retention period of up to 2557 days, the equivalent of seven years.  
CloudTrail Lake determines whether to retain an event by checking if the `eventTime` of the event is within the specified retention period. For example, if you set a retention period of 90 days, CloudTrail will remove events when the `eventTime` is older than 90 days.  
If you decrease the retention period of an event data store, CloudTrail will remove any events with an `eventTime` older than the new retention period. For example, if the previous retention period was 365 days and you decrease it to 100 days, CloudTrail will remove events with an `eventTime` older than 100 days.
Type: Integer  
Valid Range: Minimum value of 7. Maximum value of 3653.  
Required: No

 ** [TerminationProtectionEnabled](#API_UpdateEventDataStore_RequestSyntax) **   <a name="awscloudtrail-UpdateEventDataStore-request-TerminationProtectionEnabled"></a>
Indicates that termination protection is enabled and the event data store cannot be automatically deleted.  
Type: Boolean  
Required: No

## Response Syntax
<a name="API_UpdateEventDataStore_ResponseSyntax"></a>

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
   "FederationRoleArn": "string",
   "FederationStatus": "string",
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
<a name="API_UpdateEventDataStore_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AdvancedEventSelectors](#API_UpdateEventDataStore_ResponseSyntax) **   <a name="awscloudtrail-UpdateEventDataStore-response-AdvancedEventSelectors"></a>
The advanced event selectors that are applied to the event data store.  
Type: Array of [AdvancedEventSelector](API_AdvancedEventSelector.md) objects

 ** [BillingMode](#API_UpdateEventDataStore_ResponseSyntax) **   <a name="awscloudtrail-UpdateEventDataStore-response-BillingMode"></a>
The billing mode for the event data store.  
Type: String  
Valid Values: `EXTENDABLE_RETENTION_PRICING | FIXED_RETENTION_PRICING` 

 ** [CreatedTimestamp](#API_UpdateEventDataStore_ResponseSyntax) **   <a name="awscloudtrail-UpdateEventDataStore-response-CreatedTimestamp"></a>
The timestamp that shows when an event data store was first created.  
Type: Timestamp

 ** [EventDataStoreArn](#API_UpdateEventDataStore_ResponseSyntax) **   <a name="awscloudtrail-UpdateEventDataStore-response-EventDataStoreArn"></a>
The ARN of the event data store.  
Type: String  
Length Constraints: Minimum length of 3. Maximum length of 256.  
Pattern: `^[a-zA-Z0-9._/\-:]+$` 

 ** [FederationRoleArn](#API_UpdateEventDataStore_ResponseSyntax) **   <a name="awscloudtrail-UpdateEventDataStore-response-FederationRoleArn"></a>
 If Lake query federation is enabled, provides the ARN of the federation role used to access the resources for the federated event data store.   
Type: String  
Length Constraints: Minimum length of 3. Maximum length of 125.  
Pattern: `^[a-zA-Z0-9._/\-:@=\+,\.]+$` 

 ** [FederationStatus](#API_UpdateEventDataStore_ResponseSyntax) **   <a name="awscloudtrail-UpdateEventDataStore-response-FederationStatus"></a>
 Indicates the [Lake query federation](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/query-federation.html) status. The status is `ENABLED` if Lake query federation is enabled, or `DISABLED` if Lake query federation is disabled. You cannot delete an event data store if the `FederationStatus` is `ENABLED`.   
Type: String  
Valid Values: `ENABLING | ENABLED | DISABLING | DISABLED` 

 ** [KmsKeyId](#API_UpdateEventDataStore_ResponseSyntax) **   <a name="awscloudtrail-UpdateEventDataStore-response-KmsKeyId"></a>
Specifies the AWS KMS key ID that encrypts the events delivered by CloudTrail. The value is a fully specified ARN to a AWS KMS key in the following format.  
 `arn:aws:kms:us-east-2:123456789012:key/12345678-1234-1234-1234-123456789012`   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 350.  
Pattern: `^[a-zA-Z0-9._/\-:]+$` 

 ** [MultiRegionEnabled](#API_UpdateEventDataStore_ResponseSyntax) **   <a name="awscloudtrail-UpdateEventDataStore-response-MultiRegionEnabled"></a>
Indicates whether the event data store includes events from all Regions, or only from the Region in which it was created.  
Type: Boolean

 ** [Name](#API_UpdateEventDataStore_ResponseSyntax) **   <a name="awscloudtrail-UpdateEventDataStore-response-Name"></a>
The name of the event data store.  
Type: String  
Length Constraints: Minimum length of 3. Maximum length of 128.  
Pattern: `^[a-zA-Z0-9._\-]+$` 

 ** [OrganizationEnabled](#API_UpdateEventDataStore_ResponseSyntax) **   <a name="awscloudtrail-UpdateEventDataStore-response-OrganizationEnabled"></a>
Indicates whether an event data store is collecting logged events for an organization in AWS Organizations.  
Type: Boolean

 ** [RetentionPeriod](#API_UpdateEventDataStore_ResponseSyntax) **   <a name="awscloudtrail-UpdateEventDataStore-response-RetentionPeriod"></a>
The retention period, in days.  
Type: Integer  
Valid Range: Minimum value of 7. Maximum value of 3653.

 ** [Status](#API_UpdateEventDataStore_ResponseSyntax) **   <a name="awscloudtrail-UpdateEventDataStore-response-Status"></a>
The status of an event data store.  
Type: String  
Valid Values: `CREATED | ENABLED | PENDING_DELETION | STARTING_INGESTION | STOPPING_INGESTION | STOPPED_INGESTION` 

 ** [TerminationProtectionEnabled](#API_UpdateEventDataStore_ResponseSyntax) **   <a name="awscloudtrail-UpdateEventDataStore-response-TerminationProtectionEnabled"></a>
Indicates whether termination protection is enabled for the event data store.  
Type: Boolean

 ** [UpdatedTimestamp](#API_UpdateEventDataStore_ResponseSyntax) **   <a name="awscloudtrail-UpdateEventDataStore-response-UpdatedTimestamp"></a>
The timestamp that shows when the event data store was last updated. `UpdatedTimestamp` is always either the same or newer than the time shown in `CreatedTimestamp`.  
Type: Timestamp

## Errors
<a name="API_UpdateEventDataStore_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CloudTrailAccessNotEnabledException **   
This exception is thrown when trusted access has not been enabled between AWS CloudTrail and AWS Organizations. For more information, see [How to enable or disable trusted access](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html#orgs_how-to-enable-disable-trusted-access) in the * AWS Organizations User Guide* and [Prepare For Creating a Trail For Your Organization](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/creating-an-organizational-trail-prepare.html) in the * AWS CloudTrail User Guide*.  
HTTP Status Code: 400

 ** ConflictException **   
This exception is thrown when the specified resource is not ready for an operation. This can occur when you try to run an operation on a resource before CloudTrail has time to fully load the resource, or because another operation is modifying the resource. If this exception occurs, wait a few minutes, and then try the operation again.  
HTTP Status Code: 400

 ** EventDataStoreAlreadyExistsException **   
An event data store with that name already exists.  
HTTP Status Code: 400

 ** EventDataStoreARNInvalidException **   
The specified event data store ARN is not valid or does not map to an event data store in your account.  
HTTP Status Code: 400

 ** EventDataStoreHasOngoingImportException **   
 This exception is thrown when you try to update or delete an event data store that currently has an import in progress.   
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

 ** InsufficientEncryptionPolicyException **   
For the `CreateTrail` `PutInsightSelectors`, `UpdateTrail`, `StartQuery`, and `StartImport` operations, this exception is thrown when the policy on the S3 bucket or AWS KMS key does not have sufficient permissions for the operation.  
For all other operations, this exception is thrown when the policy for the AWS KMS key does not have sufficient permissions for the operation.  
HTTP Status Code: 400

 ** InvalidEventSelectorsException **   
This exception is thrown when the `PutEventSelectors` operation is called with a number of event selectors, advanced event selectors, or data resources that is not valid. The combination of event selectors or advanced event selectors and data resources is not valid. A trail can have up to 5 event selectors. If a trail uses advanced event selectors, a maximum of 500 total values for all conditions in all advanced event selectors is allowed. A trail is limited to 250 data resources. These data resources can be distributed across event selectors, but the overall total cannot exceed 250.  
You can:  
+ Specify a valid number of event selectors (1 to 5) for a trail.
+ Specify a valid number of data resources (1 to 250) for an event selector. The limit of number of resources on an individual event selector is configurable up to 250. However, this upper limit is allowed only if the total number of data resources does not exceed 250 across all event selectors for a trail.
+ Specify up to 500 values for all conditions in all advanced event selectors for a trail.
+ Specify a valid value for a parameter. For example, specifying the `ReadWriteType` parameter with a value of `read-only` is not valid.
HTTP Status Code: 400

 ** InvalidInsightSelectorsException **   
For `PutInsightSelectors`, this exception is thrown when the formatting or syntax of the `InsightSelectors` JSON statement is not valid, or the specified `InsightType` in the `InsightSelectors` statement is not valid. Valid values for `InsightType` are `ApiCallRateInsight` and `ApiErrorRateInsight`. To enable Insights on an event data store, the destination event data store specified by the `InsightsDestination` parameter must log Insights events and the source event data store specified by the `EventDataStore` parameter must log management events.  
For `UpdateEventDataStore`, this exception is thrown if Insights are enabled on the event data store and the updated advanced event selectors are not compatible with the configured `InsightSelectors`. If the `InsightSelectors` includes an `InsightType` of `ApiCallRateInsight`, the source event data store must log `write` management events. If the `InsightSelectors` includes an `InsightType` of `ApiErrorRateInsight`, the source event data store must log management events.  
HTTP Status Code: 400

 ** InvalidKmsKeyIdException **   
This exception is thrown when the AWS KMS key ARN is not valid.  
HTTP Status Code: 400

 ** InvalidParameterException **   
The request includes a parameter that is not valid.  
HTTP Status Code: 400

 ** KmsException **   
This exception is thrown when there is an issue with the specified AWS KMS key and the trail or event data store can't be updated.  
HTTP Status Code: 400

 ** KmsKeyNotFoundException **   
This exception is thrown when the AWS KMS key does not exist, when the S3 bucket and the AWS KMS key are not in the same Region, or when the AWS KMS key associated with the Amazon SNS topic either does not exist or is not in the same Region.  
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

 ** ThrottlingException **   
 This exception is thrown when the request rate exceeds the limit.   
HTTP Status Code: 400

 ** UnsupportedOperationException **   
This exception is thrown when the requested operation is not supported.  
HTTP Status Code: 400

## See Also
<a name="API_UpdateEventDataStore_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudtrail-2013-11-01/UpdateEventDataStore) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudtrail-2013-11-01/UpdateEventDataStore) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/UpdateEventDataStore) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudtrail-2013-11-01/UpdateEventDataStore) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/UpdateEventDataStore) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudtrail-2013-11-01/UpdateEventDataStore) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudtrail-2013-11-01/UpdateEventDataStore) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudtrail-2013-11-01/UpdateEventDataStore) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudtrail-2013-11-01/UpdateEventDataStore) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/UpdateEventDataStore) 