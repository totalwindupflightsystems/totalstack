---
id: "@specs/aws/lambda/docs/runtime-management-identify"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Runtime version updates"
status: active
depends_on:
  - "@specs/aws/lambda/meta"
---

# Runtime version updates

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lambda/docs/runtime-management-identify
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Identifying Lambda runtime version changes
<a name="runtime-management-identify"></a>

The [runtime version number](runtimes-update.md) and ARN are logged in the `INIT_START` log line, which Lambda emits to CloudWatch Logs each time that it creates a new [execution environment](concepts-basics.md#gettingstarted-concepts-runtime). Because the execution environment uses the same runtime version for all function invocations, Lambda emits the `INIT_START` log line only when Lambda executes the init phase. Lambda doesn't emit this log line for each function invocation. Lambda emits the log line to CloudWatch Logs, but it is not visible in the console. 

**Note**  
Runtime version numbers are not always sequential. For example, version 42 might be followed by version 45.

**Example INIT\_START log line**  

```
INIT_START Runtime Version: python:3.13.v14    Runtime Version ARN: arn:aws:lambda:eu-south-1::runtime:7b620fc2e66107a1046b140b9d320295811af3ad5d4c6a011fad1fa65127e9e6I
```

Rather than working directly with the logs, you can use [Amazon CloudWatch Contributor Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContributorInsights-CreateRule.html) to identify transitions between runtime versions. The following rule counts the distinct runtime versions from each `INIT_START` log line. To use the rule, replace the example log group name `/aws/lambda/*` with the appropriate prefix for your function or group of functions.

```
{
  "Schema": {
    "Name": "CloudWatchLogRule",
    "Version": 1
  },
  "AggregateOn": "Count",
  "Contribution": {
    "Filters": [
      {
        "Match": "eventType",
        "In": [
          "INIT_START"
        ]
      }
    ],
    "Keys": [
      "runtimeVersion",
      "runtimeVersionArn"
    ]
  },
  "LogFormat": "CLF",
  "LogGroupNames": [
    "{{/aws/lambda/*}}"
  ],
  "Fields": {
    "1": "eventType",
    "4": "runtimeVersion",
    "8": "runtimeVersionArn"
  }
}
```

The following CloudWatch Contributor Insights report shows an example of a runtime version transition as captured by the preceding rule. The orange line shows execution environment initialization for the earlier runtime version (**python:3.13.v12**), and the blue line shows execution environment initialization for the new runtime version (**python:3.13.v14**).

![Graph showing the transition from one runtime version to another.](http://docs.aws.amazon.com/lambda/latest/dg/images/runtime_version_graph.png)
