---
id: "@specs/aws/appconfig/docs/appconfig-creating-deployment-strategy-create"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Create a deployment strategy"
status: active
depends_on:
  - "@specs/aws/appconfig/meta"
---

# Create a deployment strategy

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appconfig/docs/appconfig-creating-deployment-strategy-create
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Create a deployment strategy
<a name="appconfig-creating-deployment-strategy-create"></a>

If you don't want to use one of the predefined deployment strategies, you can create your own. You can create a maximum of 20 deployment strategies. When you deploy a configuration, you can choose the deployment strategy that works best for the application and the environment.

## Creating an AWS AppConfig deployment strategy (console)
<a name="appconfig-creating-deployment-strategy-create-console"></a>

Use the following procedure to create an AWS AppConfig deployment strategy by using the AWS Systems Manager console.

**To create a deployment strategy**

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/appconfig/](https://console.aws.amazon.com/systems-manager/appconfig/).

1. In the navigation pane, choose **Deployment strategies**, and then choose **Create deployment strategy**.

1. For **Name**, enter a name for the deployment strategy.

1. For **Description**, enter information about the deployment strategy.

1. For **Deployment type**, choose a type.

1. For **Step percentage**, choose the percentage of callers to target during each step of the deployment. 

1. For **Deployment time**, enter the total duration for the deployment in minutes or hours. 

1. For **Bake time**, enter the total time, in minutes or hours, to monitor for Amazon CloudWatch alarms before proceeding to the next step of a deployment or before considering the deployment to be complete. 

1. In the **Tags** section, enter a key and an optional value. You can specify a maximum of 50 tags for a resource. 

1. Choose **Create deployment strategy**.

**Important**  
If you created a configuration profile for AWS CodePipeline, then you must create a pipeline in CodePipeline that specifies AWS AppConfig as the *deploy provider*. You don't need to perform [Deploying a configuration](appconfig-deploying.md). However, you must configure a client to receive application configuration updates as described in [Retrieving configuration data without AWS AppConfig Agent](about-data-plane.md). For information about creating a pipeline that specifies AWS AppConfig as the deploy provider, see [Tutorial: Create a Pipeline that Uses AWS AppConfig as a Deployment Provider](https://docs.aws.amazon.com/codepipeline/latest/userguide/tutorials-AppConfig.html) in the *AWS CodePipeline User Guide*. 

Proceed to [Deploying a configuration](appconfig-deploying.md).

## Creating an AWS AppConfig deployment strategy (command line)
<a name="appconfig-creating-deployment-strategy-create-commandline"></a>

The following procedure describes how to use the AWS CLI (on Linux or Windows) or AWS Tools for PowerShell to create an AWS AppConfig deployment strategy.

**To create a deployment strategy step by step**

1. Open the AWS CLI.

1. Run the following command to create a deployment strategy. 

------
#### [ Linux ]

   ```
   aws appconfig create-deployment-strategy \
     --name {{A_name_for_the_deployment_strategy}} \
     --description {{A_description_of_the_deployment_strategy}} \
     --deployment-duration-in-minutes {{Total_amount_of_time_for_a_deployment_to_last}} \
     --final-bake-time-in-minutes {{Amount_of_time_AWS AppConfig_monitors_for_alarms_before_considering_the_deployment_to_be_complete}} \
     --growth-factor {{The_percentage_of_targets_to_receive_a_deployed_configuration_during_each_interval}} \
     --growth-type {{The_linear_or_exponential_algorithm_used_to_define_how_percentage_grows_over_time}} \
     --replicate-to {{To_save_the_deployment_strategy_to_a_Systems_Manager_(SSM)_document}} \
     --tags {{User_defined_key_value_pair_metadata_of_the_deployment_strategy}}
   ```

------
#### [ Windows ]

   ```
   aws appconfig create-deployment-strategy ^
     --name {{A_name_for_the_deployment_strategy}} ^
     --description {{A_description_of_the_deployment_strategy}} ^
     --deployment-duration-in-minutes {{Total_amount_of_time_for_a_deployment_to_last}} ^
     --final-bake-time-in-minutes {{Amount_of_time_AWS AppConfig_monitors_for_alarms_before_considering_the_deployment_to_be_complete}} ^
     --growth-factor {{The_percentage_of_targets_to_receive_a_deployed_configuration_during_each_interval}} ^
     --growth-type {{The_linear_or_exponential_algorithm_used_to_define_how_percentage_grows_over_time}} ^
     --name {{A_name_for_the_deployment_strategy}} ^
     --replicate-to {{To_save_the_deployment_strategy_to_a_Systems_Manager_(SSM)_document}} ^
     --tags {{User_defined_key_value_pair_metadata_of_the_deployment_strategy}}
   ```

------
#### [ PowerShell ]

   ```
   New-APPCDeploymentStrategy ` 
     --Name {{A_name_for_the_deployment_strategy}} ` 
     --Description {{A_description_of_the_deployment_strategy}} `
     --DeploymentDurationInMinutes {{Total_amount_of_time_for_a_deployment_to_last}} `
     --FinalBakeTimeInMinutes {{Amount_of_time_AWS AppConfig_monitors_for_alarms_before_considering_the_deployment_to_be_complete}} `
     --GrowthFactor {{The_percentage_of_targets_to_receive_a_deployed_configuration_during_each_interval}} `
     --GrowthType {{The_linear_or_exponential_algorithm_used_to_define_how_percentage_grows_over_time}} `
     --ReplicateTo {{To_save_the_deployment_strategy_to_a_Systems_Manager_(SSM)_document}} `
     --Tag {{Hashtable_type_User_defined_key_value_pair_metadata_of_the_deployment_strategy}}
   ```

------

   The system returns information like the following.

------
#### [ Linux ]

   ```
   {
      "Id": "Id of the deployment strategy",
      "Name": "Name of the deployment strategy",
      "Description": "Description of the deployment strategy",
      "DeploymentDurationInMinutes": "Total amount of time the deployment lasted",
      "GrowthType": "The linear or exponential algorithm used to define how percentage grew over time",
      "GrowthFactor": "The percentage of targets that received a deployed configuration during each interval",  
      "FinalBakeTimeInMinutes": "The amount of time AWS AppConfig monitored for alarms before considering the deployment to be complete",
      "ReplicateTo": "The Systems Manager (SSM) document where the deployment strategy is saved"
   }
   ```

------
#### [ Windows ]

   ```
   {
      "Id": "Id of the deployment strategy",
      "Name": "Name of the deployment strategy",
      "Description": "Description of the deployment strategy",
      "DeploymentDurationInMinutes": "Total amount of time the deployment lasted",
      "GrowthType": "The linear or exponential algorithm used to define how percentage grew over time",
      "GrowthFactor": "The percentage of targets that received a deployed configuration during each interval",  
      "FinalBakeTimeInMinutes": "The amount of time AWS AppConfig monitored for alarms before considering the deployment to be complete",
      "ReplicateTo": "The Systems Manager (SSM) document where the deployment strategy is saved"
   }
   ```

------
#### [ PowerShell ]

   ```
   ContentLength               : Runtime of the command
   DeploymentDurationInMinutes : Total amount of time the deployment lasted
   Description                 : Description of the deployment strategy
   FinalBakeTimeInMinutes      : The amount of time AWS AppConfig monitored for alarms before considering the deployment to be complete
   GrowthFactor                : The percentage of targets that received a deployed configuration during each interval
   GrowthType                  : The linear or exponential algorithm used to define how percentage grew over time
   HttpStatusCode              : HTTP Status of the runtime
   Id                          : The deployment strategy ID
   Name                        : Name of the deployment strategy
   ReplicateTo                 : The Systems Manager (SSM) document where the deployment strategy is saved
   ResponseMetadata            : Runtime Metadata
   ```

------