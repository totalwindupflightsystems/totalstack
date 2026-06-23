---
id: "@specs/aws/amplify/docs/API_JobSummary"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS JobSummary"
status: active
depends_on:
  - "@specs/aws/amplify/meta"
---

# JobSummary

> **source:** AWS Documentation
> **spec:id:** @specs/aws/amplify/docs/API_JobSummary
> **target_lang:** meta — documentation tier. ALL sections preserved.



# JobSummary
<a name="API_JobSummary"></a>

 Describes the summary for an execution job for an Amplify app. 

## Contents
<a name="API_JobSummary_Contents"></a>

 ** commitId **   <a name="amplify-Type-JobSummary-commitId"></a>
 The commit ID from a third-party repository provider for the job.   
Type: String  
Length Constraints: Maximum length of 255.  
Pattern: `(?s).*`   
Required: Yes

 ** commitMessage **   <a name="amplify-Type-JobSummary-commitMessage"></a>
 The commit message from a third-party repository provider for the job.   
Type: String  
Length Constraints: Maximum length of 10000.  
Pattern: `(?s).*`   
Required: Yes

 ** commitTime **   <a name="amplify-Type-JobSummary-commitTime"></a>
The commit date and time for the job.   
Type: Timestamp  
Required: Yes

 ** jobArn **   <a name="amplify-Type-JobSummary-jobArn"></a>
 The Amazon Resource Name (ARN) for the job.   
Type: String  
Length Constraints: Maximum length of 1000.  
Required: Yes

 ** jobId **   <a name="amplify-Type-JobSummary-jobId"></a>
 The unique ID for the job.   
Type: String  
Length Constraints: Maximum length of 255.  
Pattern: `[0-9]+`   
Required: Yes

 ** jobType **   <a name="amplify-Type-JobSummary-jobType"></a>
 The type for the job. If the value is `RELEASE`, the job was manually released from its source by using the `StartJob` API. This value is available only for apps that are connected to a repository.  
If the value is `RETRY`, the job was manually retried using the `StartJob` API. If the value is `WEB_HOOK`, the job was automatically triggered by webhooks. If the value is `MANUAL`, the job is for a manually deployed app. Manually deployed apps are not connected to a Git repository.  
Type: String  
Length Constraints: Maximum length of 10.  
Valid Values: `RELEASE | RETRY | MANUAL | WEB_HOOK`   
Required: Yes

 ** startTime **   <a name="amplify-Type-JobSummary-startTime"></a>
 The start date and time for the job.   
Type: Timestamp  
Required: Yes

 ** status **   <a name="amplify-Type-JobSummary-status"></a>
 The current status for the job.   
Type: String  
Valid Values: `CREATED | PENDING | PROVISIONING | RUNNING | FAILED | SUCCEED | CANCELLING | CANCELLED`   
Required: Yes

 ** endTime **   <a name="amplify-Type-JobSummary-endTime"></a>
 The end date and time for the job.   
Type: Timestamp  
Required: No

 ** sourceUrl **   <a name="amplify-Type-JobSummary-sourceUrl"></a>
The source URL for the files to deploy. The source URL can be either an HTTP GET URL that is publicly accessible and downloads a single .zip file, or an Amazon S3 bucket and prefix.  
Type: String  
Length Constraints: Maximum length of 3000.  
Pattern: `^(s3|https|http)://.*`   
Required: No

 ** sourceUrlType **   <a name="amplify-Type-JobSummary-sourceUrlType"></a>
The type of source specified by the `sourceURL`. If the value is `ZIP`, the source is a .zip file. If the value is `BUCKET_PREFIX`, the source is an Amazon S3 bucket and prefix. If no value is specified, the default is `ZIP`.  
Type: String  
Valid Values: `ZIP | BUCKET_PREFIX`   
Required: No

## See Also
<a name="API_JobSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amplify-2017-07-25/JobSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amplify-2017-07-25/JobSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amplify-2017-07-25/JobSummary) 