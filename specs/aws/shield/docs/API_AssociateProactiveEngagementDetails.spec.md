---
id: "@specs/aws/shield/docs/API_AssociateProactiveEngagementDetails"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AssociateProactiveEngagementDetails"
status: active
depends_on:
  - "@specs/aws/shield/meta"
---

# AssociateProactiveEngagementDetails

> **source:** AWS Documentation
> **spec:id:** @specs/aws/shield/docs/API_AssociateProactiveEngagementDetails
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AssociateProactiveEngagementDetails
<a name="API_AssociateProactiveEngagementDetails"></a>

Initializes proactive engagement and sets the list of contacts for the Shield Response Team (SRT) to use. You must provide at least one phone number in the emergency contact list. 

After you have initialized proactive engagement using this call, to disable or enable proactive engagement, use the calls `DisableProactiveEngagement` and `EnableProactiveEngagement`. 

**Note**  
This call defines the list of email addresses and phone numbers that the SRT can use to contact you for escalations to the SRT and to initiate proactive customer support.  
The contacts that you provide in the request replace any contacts that were already defined. If you already have contacts defined and want to use them, retrieve the list using `DescribeEmergencyContactSettings` and then provide it to this call. 

## Request Syntax
<a name="API_AssociateProactiveEngagementDetails_RequestSyntax"></a>

```
{
   "EmergencyContactList": [ 
      { 
         "ContactNotes": "{{string}}",
         "EmailAddress": "{{string}}",
         "PhoneNumber": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_AssociateProactiveEngagementDetails_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [EmergencyContactList](#API_AssociateProactiveEngagementDetails_RequestSyntax) **   <a name="AWSShield-AssociateProactiveEngagementDetails-request-EmergencyContactList"></a>
A list of email addresses and phone numbers that the Shield Response Team (SRT) can use to contact you for escalations to the SRT and to initiate proactive customer support.   
To enable proactive engagement, the contact list must include at least one phone number.  
The contacts that you provide here replace any contacts that were already defined. If you already have contacts defined and want to use them, retrieve the list using `DescribeEmergencyContactSettings` and then provide it here. 
Type: Array of [EmergencyContact](API_EmergencyContact.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 10 items.  
Required: Yes

## Response Elements
<a name="API_AssociateProactiveEngagementDetails_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_AssociateProactiveEngagementDetails_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalErrorException **   
Exception that indicates that a problem occurred with the service infrastructure. You can retry the request.  
HTTP Status Code: 500

 ** InvalidOperationException **   
Exception that indicates that the operation would not cause any change to occur.  
HTTP Status Code: 400

 ** InvalidParameterException **   
Exception that indicates that the parameters passed to the API are invalid. If available, this exception includes details in additional properties.     
 ** fields **   
Fields that caused the exception.  
 ** reason **   
Additional information about the exception.
HTTP Status Code: 400

 ** OptimisticLockException **   
Exception that indicates that the resource state has been modified by another client. Retrieve the resource and then retry your request.  
HTTP Status Code: 400

 ** ResourceNotFoundException **   
Exception indicating the specified resource does not exist. If available, this exception includes details in additional properties.     
 ** resourceType **   
Type of resource.
HTTP Status Code: 400

## See Also
<a name="API_AssociateProactiveEngagementDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/shield-2016-06-02/AssociateProactiveEngagementDetails) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/shield-2016-06-02/AssociateProactiveEngagementDetails) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/shield-2016-06-02/AssociateProactiveEngagementDetails) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/shield-2016-06-02/AssociateProactiveEngagementDetails) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/shield-2016-06-02/AssociateProactiveEngagementDetails) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/shield-2016-06-02/AssociateProactiveEngagementDetails) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/shield-2016-06-02/AssociateProactiveEngagementDetails) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/shield-2016-06-02/AssociateProactiveEngagementDetails) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/shield-2016-06-02/AssociateProactiveEngagementDetails) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/shield-2016-06-02/AssociateProactiveEngagementDetails) 