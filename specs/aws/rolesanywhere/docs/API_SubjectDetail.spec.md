---
id: "@specs/aws/rolesanywhere/docs/API_SubjectDetail"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS SubjectDetail"
status: active
depends_on:
  - "@specs/aws/rolesanywhere/meta"
---

# SubjectDetail

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rolesanywhere/docs/API_SubjectDetail
> **target_lang:** meta — documentation tier. ALL sections preserved.



# SubjectDetail
<a name="API_SubjectDetail"></a>

The state of the subject after a read or write operation.

## Contents
<a name="API_SubjectDetail_Contents"></a>

 ** createdAt **   <a name="rolesanywhere-Type-SubjectDetail-createdAt"></a>
The ISO-8601 timestamp when the subject was created.   
Type: Timestamp  
Required: No

 ** credentials **   <a name="rolesanywhere-Type-SubjectDetail-credentials"></a>
The temporary session credentials vended at the last authenticating call with this subject.  
Type: Array of [CredentialSummary](API_CredentialSummary.md) objects  
Required: No

 ** enabled **   <a name="rolesanywhere-Type-SubjectDetail-enabled"></a>
The enabled status of the subject.  
Type: Boolean  
Required: No

 ** instanceProperties **   <a name="rolesanywhere-Type-SubjectDetail-instanceProperties"></a>
The specified instance properties associated with the request.  
Type: Array of [InstanceProperty](API_InstanceProperty.md) objects  
Required: No

 ** lastSeenAt **   <a name="rolesanywhere-Type-SubjectDetail-lastSeenAt"></a>
The ISO-8601 timestamp of the last time this subject requested temporary session credentials.  
Type: Timestamp  
Required: No

 ** subjectArn **   <a name="rolesanywhere-Type-SubjectDetail-subjectArn"></a>
The ARN of the resource.  
Type: String  
Required: No

 ** subjectId **   <a name="rolesanywhere-Type-SubjectDetail-subjectId"></a>
The id of the resource  
Type: String  
Length Constraints: Fixed length of 36.  
Pattern: `.*[a-f0-9]{8}-([a-z0-9]{4}-){3}[a-z0-9]{12}.*`   
Required: No

 ** updatedAt **   <a name="rolesanywhere-Type-SubjectDetail-updatedAt"></a>
The ISO-8601 timestamp when the subject was last updated.  
Type: Timestamp  
Required: No

 ** x509Subject **   <a name="rolesanywhere-Type-SubjectDetail-x509Subject"></a>
The x509 principal identifier of the authenticating certificate.  
Type: String  
Required: No

## See Also
<a name="API_SubjectDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rolesanywhere-2018-05-10/SubjectDetail) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rolesanywhere-2018-05-10/SubjectDetail) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rolesanywhere-2018-05-10/SubjectDetail) 