---
id: "@specs/aws/shield/docs/API_DescribeEmergencyContactSettings"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeEmergencyContactSettings"
status: active
depends_on:
  - "@specs/aws/shield/meta"
---

# DescribeEmergencyContactSettings

> **source:** AWS Documentation
> **spec:id:** @specs/aws/shield/docs/API_DescribeEmergencyContactSettings
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeEmergencyContactSettings
<a name="API_DescribeEmergencyContactSettings"></a>

A list of email addresses and phone numbers that the Shield Response Team (SRT) can use to contact you if you have proactive engagement enabled, for escalations to the SRT and to initiate proactive customer support.

## Response Syntax
<a name="API_DescribeEmergencyContactSettings_ResponseSyntax"></a>

```
{
   "EmergencyContactList": [ 
      { 
         "ContactNotes": "string",
         "EmailAddress": "string",
         "PhoneNumber": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeEmergencyContactSettings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EmergencyContactList](#API_DescribeEmergencyContactSettings_ResponseSyntax) **   <a name="AWSShield-DescribeEmergencyContactSettings-response-EmergencyContactList"></a>
A list of email addresses and phone numbers that the Shield Response Team (SRT) can use to contact you if you have proactive engagement enabled, for escalations to the SRT and to initiate proactive customer support.  
Type: Array of [EmergencyContact](API_EmergencyContact.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 10 items.

## Errors
<a name="API_DescribeEmergencyContactSettings_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalErrorException **   
Exception that indicates that a problem occurred with the service infrastructure. You can retry the request.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
Exception indicating the specified resource does not exist. If available, this exception includes details in additional properties.     
 ** resourceType **   
Type of resource.
HTTP Status Code: 400

## See Also
<a name="API_DescribeEmergencyContactSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/shield-2016-06-02/DescribeEmergencyContactSettings) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/shield-2016-06-02/DescribeEmergencyContactSettings) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/shield-2016-06-02/DescribeEmergencyContactSettings) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/shield-2016-06-02/DescribeEmergencyContactSettings) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/shield-2016-06-02/DescribeEmergencyContactSettings) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/shield-2016-06-02/DescribeEmergencyContactSettings) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/shield-2016-06-02/DescribeEmergencyContactSettings) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/shield-2016-06-02/DescribeEmergencyContactSettings) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/shield-2016-06-02/DescribeEmergencyContactSettings) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/shield-2016-06-02/DescribeEmergencyContactSettings) 