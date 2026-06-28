---
id: "@specs/aws/rolesanywhere/docs/API_SubjectSummary"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS SubjectSummary"
status: active
depends_on:
  - "@specs/aws/rolesanywhere/meta"
---

# SubjectSummary

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rolesanywhere/docs/API_SubjectSummary
> **target_lang:** meta — documentation tier. ALL sections preserved.



# SubjectSummary
<a name="API_SubjectSummary"></a>

A summary representation of subjects.

## Contents
<a name="API_SubjectSummary_Contents"></a>

 ** createdAt **   <a name="rolesanywhere-Type-SubjectSummary-createdAt"></a>
The ISO-8601 time stamp of when the certificate was first used in a temporary credential request.  
Type: Timestamp  
Required: No

 ** enabled **   <a name="rolesanywhere-Type-SubjectSummary-enabled"></a>
The enabled status of the subject.   
Type: Boolean  
Required: No

 ** lastSeenAt **   <a name="rolesanywhere-Type-SubjectSummary-lastSeenAt"></a>
The ISO-8601 time stamp of when the certificate was last used in a temporary credential request.  
Type: Timestamp  
Required: No

 ** subjectArn **   <a name="rolesanywhere-Type-SubjectSummary-subjectArn"></a>
The ARN of the resource.  
Type: String  
Required: No

 ** subjectId **   <a name="rolesanywhere-Type-SubjectSummary-subjectId"></a>
The id of the resource.  
Type: String  
Length Constraints: Fixed length of 36.  
Pattern: `.*[a-f0-9]{8}-([a-z0-9]{4}-){3}[a-z0-9]{12}.*`   
Required: No

 ** updatedAt **   <a name="rolesanywhere-Type-SubjectSummary-updatedAt"></a>
The ISO-8601 timestamp when the subject was last updated.   
Type: Timestamp  
Required: No

 ** x509Subject **   <a name="rolesanywhere-Type-SubjectSummary-x509Subject"></a>
The x509 principal identifier of the authenticating certificate.  
Type: String  
Required: No

## See Also
<a name="API_SubjectSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rolesanywhere-2018-05-10/SubjectSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rolesanywhere-2018-05-10/SubjectSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rolesanywhere-2018-05-10/SubjectSummary) 