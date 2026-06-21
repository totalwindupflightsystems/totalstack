---
id: "@specs/aws/rds/docs/API_BlueGreenDeployment"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS BlueGreenDeployment"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# BlueGreenDeployment

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_BlueGreenDeployment
> **target_lang:** meta — documentation tier. ALL sections preserved.



# BlueGreenDeployment
<a name="API_BlueGreenDeployment"></a>

Details about a blue/green deployment.

For more information, see [Using Amazon RDS Blue/Green Deployments for database updates](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/blue-green-deployments.html) in the *Amazon RDS User Guide* and [Using Amazon RDS Blue/Green Deployments for database updates](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/blue-green-deployments.html) in the *Amazon Aurora User Guide*.

## Contents
<a name="API_BlueGreenDeployment_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** BlueGreenDeploymentIdentifier **   
The unique identifier of the blue/green deployment.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[A-Za-z][0-9A-Za-z-:._]*`   
Required: No

 ** BlueGreenDeploymentName **   
The user-supplied name of the blue/green deployment.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 60.  
Pattern: `[a-zA-Z](?:-?[a-zA-Z0-9]+)*`   
Required: No

 ** CreateTime **   
The time when the blue/green deployment was created, in Universal Coordinated Time (UTC).  
Type: Timestamp  
Required: No

 ** DeleteTime **   
The time when the blue/green deployment was deleted, in Universal Coordinated Time (UTC).  
Type: Timestamp  
Required: No

 ** Source **   
The source database for the blue/green deployment.  
Before switchover, the source database is the production database in the blue environment.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:[A-Za-z][0-9A-Za-z-:._]*`   
Required: No

 ** Status **   
The status of the blue/green deployment.  
Valid Values:  
+  `PROVISIONING` - Resources are being created in the green environment.
+  `AVAILABLE` - Resources are available in the green environment.
+  `SWITCHOVER_IN_PROGRESS` - The deployment is being switched from the blue environment to the green environment.
+  `SWITCHOVER_COMPLETED` - Switchover from the blue environment to the green environment is complete.
+  `INVALID_CONFIGURATION` - Resources in the green environment are invalid, so switchover isn't possible.
+  `SWITCHOVER_FAILED` - Switchover was attempted but failed.
+  `DELETING` - The blue/green deployment is being deleted.
Type: String  
Required: No

 ** StatusDetails **   
Additional information about the status of the blue/green deployment.  
Type: String  
Required: No

 ** SwitchoverDetails.member.N **   
The details about each source and target resource in the blue/green deployment.  
Type: Array of [SwitchoverDetail](API_SwitchoverDetail.md) objects  
Required: No

 ** TagList.Tag.N **   
A list of tags.  
For more information, see [Tagging Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html) in the *Amazon RDS User Guide* or [Tagging Amazon Aurora and Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Tagging.html) in the *Amazon Aurora User Guide*.   
Type: Array of [Tag](API_Tag.md) objects  
Required: No

 ** Target **   
The target database for the blue/green deployment.  
Before switchover, the target database is the clone database in the green environment.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:[A-Za-z][0-9A-Za-z-:._]*`   
Required: No

 ** Tasks.member.N **   
Either tasks to be performed or tasks that have been completed on the target database before switchover.  
Type: Array of [BlueGreenDeploymentTask](API_BlueGreenDeploymentTask.md) objects  
Required: No

## See Also
<a name="API_BlueGreenDeployment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/BlueGreenDeployment) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/BlueGreenDeployment) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/BlueGreenDeployment) 