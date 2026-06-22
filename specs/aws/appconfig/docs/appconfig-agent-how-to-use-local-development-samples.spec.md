---
id: "@specs/aws/appconfig/docs/appconfig-agent-how-to-use-local-development-samples"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Samples for local development mode"
status: active
depends_on:
  - "@specs/aws/appconfig/meta"
---

# Samples for local development mode

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appconfig/docs/appconfig-agent-how-to-use-local-development-samples
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Feature flag samples for AWS AppConfig Agent local development mode
<a name="appconfig-agent-how-to-use-local-development-samples"></a>

This section includes feature flag samples you can use with AWS AppConfig Agent in local development mode. Local development mode expects feature flag data in the data's retrieval-time format. *Retrieval-time format* is the format returned when the flag is retrieved from the [GetLatestConfiguration](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_appconfigdata_GetLatestConfiguration.html) API, which only contains the flag's value. Retrieval-time format doesn't include a flag's complete definition (as passed to the [CreateHostedConfigurationVersion](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_CreateHostedConfigurationVersion.html) API). The complete definition for a flag also contains information such as attribute names and values, constraints, and the flag's enabled state. 

**Topics**
+ [Basic feature flag samples](#appconfig-agent-how-to-use-local-development-samples-basic)
+ [Multi-variant feature flag samples](#appconfig-agent-how-to-use-local-development-samples-multi-variant)

## Basic feature flag samples
<a name="appconfig-agent-how-to-use-local-development-samples-basic"></a>

Use the following basic feature flag samples with AWS AppConfig Agent in local development mode.

**Note**  
If you want the agent to report the content type of your local feature flag data as `application/json` (as it would when retrieving flag data from AWS AppConfig in an environment that isn't local development mode), your local feature flag files must use the .json extension. For example, `Local:MyFeatureFlags:SampleB1.json`.

**Sample 1**: A single flag representing a UI refresh.

```
{
    "ui_refresh": {
        "enabled": true,
        "new_styleguide_colors": true
    }
}
```

**Sample 2**: Multiple flags representing operational feature flags.

```
{
   "background_worker": {
        "enabled": true,
        "num_threads": 4,
        "queue_name": "MyWorkQueue"
   },
   "emergency_shutoff_switch": {
        "enabled": false
   },
   "logger_settings": {
        "enabled": true,
        "level": "INFO"
   }
}
```

## Multi-variant feature flag samples
<a name="appconfig-agent-how-to-use-local-development-samples-multi-variant"></a>

The retrieval-time format of a feature flag configuration that contains at least one multi-variant feature flag is represented as [Amazon Ion](https://amazon-ion.github.io/ion-docs/) data instead of JSON data. In this format, multi-variant flags are represented as an annotated list, and basic flags are represented as an annotated string. The list elements of a multi-variant flag are either a tuple (a list with a length of two), which represents a single variant, or a string, which represents the default variant. Within a variant tuple, the first element is an s-expression that represents the variant's rule, and the second element is a string that represents the variant's content.

In order for the agent to properly interpret these files, your local feature flag files must use the following extension: .`application%ion%type=AWS.AppConfig.FeatureFlags`. For example, `Local:MyFeatureFlags:SampleMV1.application%ion%type=AWS.AppConfig.FeatureFlags`.

**Sample 1**: A multi-variant flag representing a tiered release of a new feature.

```
'tiered_release'::[
  [
    (or (and (eq $group "Tier1") (split by::$userId pct::1 seed::"2025.01.01")) (and (eq $group "Tier2") (split by::$userId pct::7 seed::"2025.01.01"))),
    '''{"_variant": "ShowFeature", "enabled": true}'''
  ],
  '''{"_variant": "HideFeature", "enabled": false}'''
]
```

**Sample 2**: Multiple flags representing different UX displays based on the user’s ID. The first two flags are multi-variant and the final flag is basic.

```
'colorway'::[
  [
    (contains $userId "beta"),
    '''{"_variant": "BetaTesters", "enabled": true, "background": "blue", "foreground": "red"}''',
  ],
  [
    (split by::$userId pct::10),
    '''{"_variant": "SplitRollOutRedAndBlue", "enabled": true, "background": "blue", "foreground": "red"}''',
  ],
  '''{"_variant": "default", "enabled": true, "background": "green", "foreground": "green"}''',
]

'simple_feature'::[
  [
    (contains $userId "beta"),
    '''{"_variant": "BetaTesters", "enabled": true}'''
  ],
  '''{"_variant": "default", "enabled": false}'''
]

'button_color'::'''{"enabled": true, "color": "orange"}'''
```