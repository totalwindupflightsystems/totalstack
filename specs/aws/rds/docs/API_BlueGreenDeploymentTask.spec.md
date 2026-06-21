---
id: "@specs/aws/rds/docs/API_BlueGreenDeploymentTask"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS BlueGreenDeploymentTask"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# BlueGreenDeploymentTask

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_BlueGreenDeploymentTask
> **target_lang:** meta — documentation tier. ALL sections preserved.



# BlueGreenDeploymentTask
<a name="API_BlueGreenDeploymentTask"></a>

Details about a task for a blue/green deployment.

For more information, see [Using Amazon RDS Blue/Green Deployments for database updates](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/blue-green-deployments.html) in the *Amazon RDS User Guide* and [Using Amazon RDS Blue/Green Deployments for database updates](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/blue-green-deployments.html) in the *Amazon Aurora User Guide*.

## Contents
<a name="API_BlueGreenDeploymentTask_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** Name **   
The name of the blue/green deployment task.  
Type: String  
Required: No

 ** Status **   
The status of the blue/green deployment task.  
Valid Values:  
+  `PENDING` - The resource is being prepared for deployment.
+  `IN_PROGRESS` - The resource is being deployed.
+  `COMPLETED` - The resource has been deployed.
+  `FAILED` - Deployment of the resource failed.
Type: String  
Required: No

## See Also
<a name="API_BlueGreenDeploymentTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/BlueGreenDeploymentTask) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/BlueGreenDeploymentTask) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/BlueGreenDeploymentTask) 