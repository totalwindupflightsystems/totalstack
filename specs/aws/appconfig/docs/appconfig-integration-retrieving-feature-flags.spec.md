---
id: "@specs/aws/appconfig/docs/appconfig-integration-retrieving-feature-flags"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Retrieving feature flags"
status: active
depends_on:
  - "@specs/aws/appconfig/meta"
---

# Retrieving feature flags

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appconfig/docs/appconfig-integration-retrieving-feature-flags
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Retrieving basic and multi-variant feature flags
<a name="appconfig-integration-retrieving-feature-flags"></a>

For feature flag configurations (configurations of type `AWS.AppConfig.FeatureFlags`), the AWS AppConfig Agent enables you to retrieve a single flag or a subset of flags in a configuration. Retrieving one or two flags is useful if your use case only needs to use a few flags from the configuration profile. The following examples use cURL.

**Note**  
The ability to call a single feature flag or a subset of flags in a configuration is only available in the AWS AppConfig Agent version 2.0.45 and higher.

You can retrieve AWS AppConfig configuration data from a local HTTP endpoint. To access a specific flag or a list of flags, use the `?flag={{FLAG_KEY}}` query parameter for an AWS AppConfig configuration profile.

**To retrieve a single flag and its attributes**

```
curl "http://localhost:2772/applications/{{APPLICATION_NAME}}/environments/{{ENVIRONMENT_NAME}}/configurations/{{CONFIGURATION_NAME}}?flag={{FLAG_KEY}}"
```

**To retrieve multiple flags and their attributes**

```
curl "http://localhost:2772/applications/{{APPLICATION_NAME}}/environments/{{ENVIRONMENT_NAME}}/configurations/{{CONFIGURATION_NAME}}?flag={{FLAG_KEY_ONE}}&flag={{FLAG_KEY_TWO}}"
```

**To retrieve feature flag variants based on caller context**

The following cURL examples show how to retrieve feature flag variants based on caller context. To best illustrate how to make these calls, this section uses sample calls based on a scenario where a customer created variants similar to the following:

![An example screenshot of a feature flag with variants.](http://docs.aws.amazon.com/appconfig/latest/userguide/images/flag-variant-example.png)


**Note**  
To retrieve flag variants, you must use the latest version of AWS AppConfig Agent in your compute environment. For more information, see the following topics that describe how to update, install, or add the agent for each of the following compute environments:  
For Lambda compute environments: [Adding the AWS AppConfig Agent Lambda extension](appconfig-integration-lambda-extensions-add.md)
For Amazon EC2 compute environments: [Step 2: (Required) Installing and starting AWS AppConfig Agent on Amazon EC2 instances](appconfig-integration-ec2.md#appconfig-integration-ec2-installing)
For Amazon ECS compute environments: [Starting the AWS AppConfig agent for Amazon ECS integration](appconfig-integration-containers-agent-starting-ecs.md)
For Amazon EKS compute environments: [Starting the AWS AppConfig agent for Amazon EKS integration](appconfig-integration-containers-agent-starting-eks.md)

**To retrieve flag data using the caller context of jane\_doe@example.org (who has not opted into the beta program):**

```
curl http://localhost:2772/applications/UIRefresh/environments/Production/configurations/Features \
-H "Context: email=jane_doe@example.org" \
-H "Context: opted_in_to_beta=false"
{
  "ui_refresh": {"_variant":"QA","dark_mode_support":true,"enabled":true}
}
```

**To retrieve flag data using the caller context of jane\_doe@example.org (who *has* opted into the beta program):**

```
curl http://localhost:2772/applications/UIRefresh/environments/Production/configurations/Features \
-H "Context: email=jane_doe@example.org" \
-H "Context: opted_in_to_beta=true"
{
  "ui_refresh": {"_variant":"QA","dark_mode_support":true,"enabled":true}
}
```

**To retrieve flag data using the caller context of jane\_doe@qa-testers.example.org (who is a quality assurance tester at Example Organization):**

```
curl http://localhost:2772/applications/UIRefresh/environments/Production/configurations/Features \
-H "Context: email=jane_doe@qa-testers.example.org" 
{
  "ui_refresh": {"_variant":"QA","dark_mode_support":true,"enabled":true}
}
```

**To retrieve flag data without caller context (which returns the Default variant)**

```
curl http://localhost:2772/applications/UIRefresh/environments/Production/configurations/Features
{
"ui_refresh": {"_variant":"Default Variant","enabled":false}
}
```

**To retrieve flag data for a traffic splitting scenario to determine if 1 out of 10 random callers receive the 'sample population' variant**

```
for i in {0..9} do ; \
curl http://localhost:2772/applications/UIRefresh/environments/Production/configurations/Features \
-H "Context: email=$i@example.org"
{
  "ui_refresh": {"_variant":"Default Variant","enabled":false}
}
{
  "ui_refresh": {"_variant":"Default Variant","enabled":false}
}
{
  "ui_refresh": {"_variant":"Default Variant","enabled":false}
}
{
  "ui_refresh": {"_variant":"Default Variant","enabled":false}
}
{
  "ui_refresh": {"_variant":"Sample Population","dark_mode_support":false,"enabled":true}
}
{
  "ui_refresh": {"_variant":"Default Variant","enabled":false}
}
{
  "ui_refresh": {"_variant":"Default Variant","enabled":false}
}
{
  "ui_refresh": {"_variant":"Default Variant","enabled":false}
}
{
  "ui_refresh": {"_variant":"Default Variant","enabled":false}
}
{
  "ui_refresh": {"_variant":"Default Variant","enabled":false}
}
{
  "ui_refresh": {"_variant":"Default Variant","enabled":false}
}
```