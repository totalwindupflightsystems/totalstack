---
id: "@specs/aws/opensearchserverless/docs/serverless-lifecycle"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Using data lifecycle policies"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Using data lifecycle policies

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/serverless-lifecycle
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Using data lifecycle policies with Amazon OpenSearch Serverless
<a name="serverless-lifecycle"></a>

A data lifecycle policy in Amazon OpenSearch Serverless defines how long OpenSearch Serverless retains data in a time series collection. For example, you can set a policy to retain log data for 30 days before OpenSearch Serverless deletes it.

You can configure a separate policy for each index within each time series collection in your AWS account. OpenSearch Serverless retains documents for at least the duration that you specify in the policy. It then deletes the documents automatically on a best-effort basis, typically within 48 hours or 10% of the retention period, whichever is longer.

Only time series collections support data lifecycle policies. Search and vector search collections do not.

**Topics**
+ [Data lifecycle policies](#serverless-lifecycle-policies)
+ [Required permissions](#serverless-lifecycle-permissions)
+ [Policy precedence](#serverless-lifecycle-precedence)
+ [Policy syntax](#serverless-lifecycle-syntax)
+ [Creating data lifecycle policies](#serverless-lifecycle-create)
+ [Updating data lifecycle policies](#serverless-lifecycle-update)
+ [Deleting data lifecycle policies](#serverless-lifecycle-delete)

## Data lifecycle policies
<a name="serverless-lifecycle-policies"></a>

In a data lifecycle policy, you specify a series of rules. The data lifecycle policy lets you manage the retention period of data associated to indexes or collections that match these rules. These rules define the retention period for data in an index or group of indexes. Each rule consists of a resource type (`index`), a retention period, and a list of resources (indexes) that the retention period applies to.

You define the retention period with one of the following formats:
+ `"MinIndexRetention": "24h"` – OpenSearch Serverless retains index data for the specified period in hours or days. You can set this period to be from `24h` to `3650d`.
+ `"NoMinIndexRetention": true` – OpenSearch Serverless retains index data indefinitely.

In the following sample policy, the first rule specifies a retention period of 15 days for all indexes within the collection `marketing`. The second rule specifies that all index names that begin with `log` in the `finance` collection have no retention period set and will be retained indefinitely.

```
{
   "lifeCyclePolicyDetail": {
      "type": "retention",
      "name": "{{my-policy}}",
      "policyVersion": "{{MTY4ODI0NTM2OTk1N18x}}",
      "policy": {
         "Rules": [
            {
            "ResourceType":"index",
            "Resource":[
               "index/{{marketing}}/*"
            ],
            "MinIndexRetention": "15d"
         },
         {
            "ResourceType":"index",
            "Resource":[
               "index/{{finance}}/log*"
            ],
            "NoMinIndexRetention": true
         }
         ]
      },
      "createdDate": 1688245369957,
      "lastModifiedDate": 1688245369957
   }
}
```

In the following sample policy rule, OpenSearch Serverless indefinitely retains the data in all indexes for all collections within the account.

```
{
   "Rules": [
      {
         "ResourceType": "index",
         "Resource": [
            "index/*/*"
         ]
      }
   ],
   "NoMinIndexRetention": true
}
```

## Required permissions
<a name="serverless-lifecycle-permissions"></a>

Lifecycle policies for OpenSearch Serverless use the following AWS Identity and Access Management (IAM) permissions. You can specify IAM conditions to restrict users to data lifecycle policies associated with specific collections and indexes.
+ `aoss:CreateLifecyclePolicy` – Create a data lifecycle policy.
+ `aoss:ListLifecyclePolicies` – List all data lifecycle policies in the current account.
+ `aoss:BatchGetLifecyclePolicy` – View a data lifecycle policy associated with an account or policy name.
+ `aoss:BatchGetEffectiveLifecyclePolicy` – View a data lifecycle policy for a given resource (`index` is the only supported resource).
+ `aoss:UpdateLifecyclePolicy` – Modify a given data lifecycle policy, and change its retention setting or resource.
+ `aoss:DeleteLifecyclePolicy` – Delete a data lifecycle policy.

The following identity-based access policy allows a user to view all data lifecycle policies, and update policies with the resource pattern `index/application-logs`:

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "aoss:UpdateLifecyclePolicy"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "aoss:collection": "{{application-logs}}"
                }
            }
        },
        {
            "Effect": "Allow",
            "Action": [
                "aoss:ListLifecyclePolicies",
                "aoss:BatchGetLifecyclePolicy"
            ],
            "Resource": "*"
        }
    ]
}
```

------

## Policy precedence
<a name="serverless-lifecycle-precedence"></a>

There can be situations where data lifecycle policy rules overlap, within or across policies. When this happens, a rule with a more specific resource name or pattern for an index overrides a rule with a more general resource name or pattern for any indexes that are common to *both* rules.

For example, in the following policy, two rules apply to an index `index/sales/logstash`. In this situation, the second rule takes precedence because `index/sales/log*` is the longest match to `index/sales/logstash`. Therefore, OpenSearch Serverless sets no retention period for the index.

```
{
      "Rules":[
         {
            "ResourceType":"index",
            "Resource":[
               "index/{{sales}}/*",
            ],
            "MinIndexRetention": "15d"
         },
         {
            "ResourceType":"index",
            "Resource":[
               "index/{{sales}}/log*",
            ],
            "NoMinIndexRetention": true
         }
      ]
   }
```

## Policy syntax
<a name="serverless-lifecycle-syntax"></a>

Provide one or more *rules*. These rules define data lifecycle settings for your OpenSearch Serverless indexes.

Each rule contains the following elements. You can either provide `MinIndexRetention` or `NoMinIndexRetention` in each rule, but not both. 


| Element | Description | 
| --- | --- | 
| Resource type | The type of resource that the rule applies to. The only supported option for data lifecycle policies is index. | 
| Resource | A list of resource names and/or patterns. Patterns consist of a prefix and a wildcard (\*), which allow the associated permissions to apply to multiple resources. For example, index/{{<collection-name\|pattern>}}/{{<index-name\|pattern>}}. | 
| MinIndexRetention | The minimum period, in days (d) or hours (h), to retain the document in the index. The lower bound is 24h and the upper bound is 3650d. | 
| NoMinIndexRetention | If true, OpenSearch Serverless retains documents indefinitely. | 

In the following example, the first rule applies to all indexes under the `autoparts-inventory` pattern (`index/autoparts-inventory/*`) and requires data to be retained for at least 20 days before any actions, such as deletion or archiving, can occur. 

The second rule targets indexes matching the `auto*/gear` pattern (`index/auto*/gear`), setting a minimum retention period of 24 hours.

The third rule applies specifically to the `tires` index and has no minimum retention period, meaning that data in this index can be deleted or archived immediately or based on other criteria. These rules help manage the retention of index data with varying retention times or no retention restrictions.

```
{
  "Rules": [
    {
      "ResourceType": "index",
      "Resource": [
        "index/{{autoparts-inventory}}/*"
      ],
      "MinIndexRetention": "20d"
    },
    {
      "ResourceType": "index",
      "Resource": [
        "index/{{auto*}}/{{gear}}"
      ],
      "MinIndexRetention": "24h"
    },
    {
      "ResourceType": "index",
      "Resource": [
        "index/{{autoparts-inventory}}/{{tires}}"
      ],
      "NoMinIndexRetention": true
    }
  ]
}
```

## Creating data lifecycle policies
<a name="serverless-lifecycle-create"></a>

To create a data lifecycle policy, you define rules that manage the retention and deletion of your data based on specified criteria. 

### Console
<a name="serverless-lifecycle-create-console"></a>

**To create a data lifecycle policy**

1. Sign in to the Amazon OpenSearch Service console at [https://console.aws.amazon.com/aos/home](https://console.aws.amazon.com/aos/home).

1. In the left navigation pane, choose **Data lifecycle policies**.

1. Choose **Create data lifecycle policy**.

1. Enter a descriptive name for the policy.

1. For **Data lifecycle**, choose **Add** and select the collections and indexes for the policy. 

   Start by choosing the collections to which the indexes belong. Then, either choose the index from the list or enter an index pattern. To select all collections as sources, enter an asterisk (`*`).

1. For **Data retention**, you can either choose to retain the data indefinitely, or deselect **Unlimited (never delete)** and specify a time period after which OpenSearch Serverless automatically deletes the data from Amazon S3.

1. Choose **Save**, then **Create**.

### AWS CLI
<a name="serverless-lifecycle-create-cli"></a>

To create a data lifecycle policy using the AWS CLI, use the [create-lifecycle-policy](https://docs.aws.amazon.com/cli/latest/reference/opensearchserverless/create-lifecycle-policy.html) command with the following options:
+ `--name` – The name of the policy.
+ `--type` – The type of policy. Currently, the only available value is `retention`.
+ `--policy` – The data lifecycle policy. This parameter accepts both inline policies and .json files. You must encode inline policies as a JSON escaped string. To provide the policy in a file, use the format `--policy file://{{my-policy}}.json`.

**Example**  

```
aws opensearchserverless create-lifecycle-policy \
  --name {{my-policy}} \
  --type retention \
  --policy "{\"Rules\":[{\"ResourceType\":\"index\",\"Resource\":[\"index/{{autoparts-inventory}}/*\"],\"MinIndexRetention\": \"81d\"},{\"ResourceType\":\"index\",\"Resource\":[\"index/{{sales}}/{{orders*}}\"],\"NoMinIndexRetention\":true}]}"
```

## Updating data lifecycle policies
<a name="serverless-lifecycle-update"></a>

To update a data lifecycle policy, you can modify existing rules to reflect changes in your data retention or deletion requirements. This allows you to adapt your policies as your data management needs evolve.

There might be a few minutes of lag time between when you update the policy and when OpenSearch Serverless starts to enforce the new retention periods.

### Console
<a name="serverless-lifecycle-update-console"></a>

**To update a data lifecycle policy**

1. Sign in to the Amazon OpenSearch Service console at [https://console.aws.amazon.com/aos/home](https://console.aws.amazon.com/aos/home).

1. In the left navigation pane, choose **Data lifecycle policies**.

1. Select the data lifecycle policy that you want to update, then choose **Edit**.

1. Modify the policy using the visual editor or the JSON editor.

1. Choose **Save**.

### AWS CLI
<a name="serverless-lifecycle-update-cli"></a>

To update a data lifecycle policy using the AWS CLI, use the [update-lifecycle-policy](https://docs.aws.amazon.com/cli/latest/reference/opensearchserverless/update-lifecycle-policy.html) command. 

You must include the `--policy-version` parameter in the request. You can retrieve the policy version by using the [list-lifecycle-policies](https://docs.aws.amazon.com/cli/latest/reference/opensearchserverless/list-lifecycle-policies.html) or [batch-get-lifecycle-policy](https://docs.aws.amazon.com/cli/latest/reference/opensearchserverless/batch-get-lifecycle-policy.html) commands. We recommend including the most recent policy version to prevent accidentally overwriting changes made by others.

The following request updates a data lifecycle policy with a new policy JSON document.

**Example**  

```
aws opensearchserverless update-lifecycle-policy \
  --name {{my-policy}} \
  --type retention \
  --policy-version {{MTY2MzY5MTY1MDA3Ml8x}} \
  --policy file://{{my-new-policy.json}}
```

## Deleting data lifecycle policies
<a name="serverless-lifecycle-delete"></a>

When you delete a data lifecycle policy, OpenSearch Serverless no longer enforces it on any matching indexes.

### Console
<a name="serverless-lifecycle-delete-console"></a>

**To delete a data lifecycle policy**

1. Sign in to the Amazon OpenSearch Service console at [https://console.aws.amazon.com/aos/home](https://console.aws.amazon.com/aos/home).

1. In the left navigation pane, choose **Data lifecycle policies**.

1. Select the policy that you want to delete, then choose **Delete** and confirm deletion.

### AWS CLI
<a name="serverless-lifecycle-delete-cli"></a>

To delete a data lifecycle policy using the AWS CLI, use the [delete-lifecycle-policy](https://docs.aws.amazon.com/cli/latest/reference/opensearchserverless/delete-lifecycle-policy.html) command.

**Example**  

```
aws opensearchserverless delete-lifecycle-policy \
  --name {{my-policy}} \
  --type retention
```