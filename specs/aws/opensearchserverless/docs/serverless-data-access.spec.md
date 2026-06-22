---
id: "@specs/aws/opensearchserverless/docs/serverless-data-access"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Data access control"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Data access control

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/serverless-data-access
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Data access control for Amazon OpenSearch Serverless
<a name="serverless-data-access"></a>

With data access control in Amazon OpenSearch Serverless, you can allow users to access collections and indexes, regardless of their access mechanism or network source. You can provide access to IAM roles and [SAML identities](serverless-saml.md).

You manage access permissions through *data access policies*, which apply to collections and index resources. Data access policies help you manage collections at scale by automatically assigning access permissions to collections and indexes that match a specific pattern. Multiple data access policies can apply to a single resource. Note that you must have a data access policy for your collection in order to access your OpenSearch Dashboards URL.

**Topics**
+ [Data access policies versus IAM policies](#serverless-data-access-vs-iam)
+ [IAM permissions required to configure data access policies](#serverless-data-access-permissions)
+ [Policy syntax](#serverless-data-access-syntax)
+ [Supported policy permissions](#serverless-data-supported-permissions)
+ [Sample datasets on OpenSearch Dashboards](#serverless-data-sample-index)
+ [Creating data access policies (console)](#serverless-data-access-console)
+ [Creating data access policies (AWS CLI)](#serverless-data-access-cli)
+ [Viewing data access policies](#serverless-data-access-list)
+ [Updating data access policies](#serverless-data-access-update)
+ [Deleting data access policies](#serverless-data-access-delete)
+ [Cross-account data access](#serverless-data-access-cross)

## Data access policies versus IAM policies
<a name="serverless-data-access-vs-iam"></a>

Data access policies are logically separate from AWS Identity and Access Management (IAM) policies. IAM permissions control access to the [serverless API operations](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/Welcome.html), such as `CreateCollection` and `ListAccessPolicies`. Data access policies control access to the [OpenSearch operations](#serverless-data-supported-permissions) that OpenSearch Serverless supports, such as `PUT <index>` or `GET _cat/indices`.

The IAM permissions that control access to data access policy API operations, such as `aoss:CreateAccessPolicy` and `aoss:GetAccessPolicy` (described in the next section), don't affect the permission specified in a data access policy.

For example, suppose an IAM policy denies a user from creating data access policies for `collection-a`, but allows them to create data access policies for all collections (`*`):

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Deny",
            "Action": [
                "aoss:CreateAccessPolicy"
            ],
            "Resource": "*",
            "Condition": {
                "StringLike": {
                    "aoss:collection": "collection-a"
                }
            }
        },
        {
            "Effect": "Allow",
            "Action": [
                "aoss:CreateAccessPolicy"
            ],
            "Resource": "*"
        }
    ]
}
```

------

If the user creates a data access policy that allows certain permission to *all* collections (`collection/*` or `index/*/*`) the policy will apply to all collections, including collection A.

**Important**  
Being granted permissions within a data access policy is not sufficient to access data in your OpenSearch Serverless collection. An associated principal must *also* be granted access to the IAM permissions `aoss:APIAccessAll` and `aoss:DashboardsAccessAll`. Both permissions grant full access to collection resources, while the Dashboards permission also provides access to OpenSearch Dashboards. If a principal doesn't have both of these IAM permissions, they will receive 403 errors when attempting to send requests to the collection. For more information, see [Using OpenSearch API operations](security-iam-serverless.md#security_iam_id-based-policy-examples-data-plane).

## IAM permissions required to configure data access policies
<a name="serverless-data-access-permissions"></a>

Data access control for OpenSearch Serverless uses the following IAM permissions. You can specify IAM conditions to restrict users to specific access policy names. Amazon OpenSearch Service also supports global IAM condition keys in resource-based access policies, including `aws:SecureTransport`. You can use `aws:SecureTransport` to require that requests to your domain be made over HTTPS. For example:

```
"Condition": {"Bool": {"aws:SecureTransport": "true"}}
```
+ `aoss:CreateAccessPolicy` – Create an access policy.
+ `aoss:ListAccessPolicies` – List all access policies.
+ `aoss:GetAccessPolicy` – See details about a specific access policy.
+ `aoss:UpdateAccessPolicy` – Modify an access policy.
+ `aoss:DeleteAccessPolicy` – Delete an access policy.

The following identity-based access policy allows a user to view all access policies, and update policies that contain the resource pattern `collection/logs`.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Action": [
                "aoss:ListAccessPolicies",
                "aoss:GetAccessPolicy"
            ],
            "Effect": "Allow",
            "Resource": "*"
        },
        {
            "Action": [
                "aoss:UpdateAccessPolicy"
            ],
            "Effect": "Allow",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "aoss:collection": [
                        "{{logs}}"
                    ]
                }
            }
        }
    ]
}
```

------

**Note**  
In addition, OpenSearch Serverless requires the `aoss:APIAccessAll` and `aoss:DashboardsAccessAll` permissions for collection resources. For more information, see [Using OpenSearch API operations](security-iam-serverless.md#security_iam_id-based-policy-examples-data-plane).

## Policy syntax
<a name="serverless-data-access-syntax"></a>

A data access policy includes a set of rules, each with the following elements:


| Element | Description | 
| --- | --- | 
| ResourceType | The type of resource (collection or index) that the permissions apply to. Alias and template permissions are at the collection level, while permissions for creating, modifying, and searching data are at the index level. For more information, see [Supported policy permissions](#serverless-data-supported-permissions). | 
| Resource | A list of resource names and/or patterns. Patterns are prefixes followed by a wildcard (\*), which allow the associated permissions to apply to multiple resources.[See the AWS documentation website for more details](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-data-access.html) | 
| Permission | A list of permissions to grant for the specified resources. For a complete list of permissions and the API operations they allow, see [Supported OpenSearch API operations and permissions](serverless-genref.md#serverless-operations). | 
| Principal | A list of one or more principals to grant access to. Principals can be IAM role ARNs or SAML identities. These principals must be within the current AWS account. Data access policies don't directly support cross-account access, but you can include a role in your policy that a user from a different AWS account can assume in the collection-owning account. For more information, see [Cross-account data access](#serverless-data-access-cross). | 

The following example policy grants alias and template permissions to the collection called `autopartsinventory`, as well as any collections that begin with the prefix `sales*`. It also grants read and write permissions to all indexes within the `autopartsinventory` collection, and any indexes in the `salesorders` collection that begin with the prefix `orders*`.

```
[
   {
      "Description": "Rule 1",
      "Rules":[
         {
            "ResourceType":"collection",
            "Resource":[
               "collection/{{autopartsinventory}}",
               "collection/{{sales*}}"
            ],
            "Permission":[
               "aoss:CreateCollectionItems",
               "aoss:UpdateCollectionItems",
               "aoss:DescribeCollectionItems"
            ]
         },
         {
            "ResourceType":"index",
            "Resource":[
               "index/{{autopartsinventory}}/{{*}}",
               "index/{{salesorders}}/{{orders*}}"
            ],
            "Permission":[
               "aoss:*"
            ]
         }
      ],
      "Principal":[
         "arn:aws:iam::{{123456789012}}:user/{{Dale}}",
         "arn:aws:iam::{{123456789012}}:role/{{RegulatoryCompliance}}",
         "saml/{{123456789012}}/{{myprovider}}/user/{{Annie}}",
         "saml/{{123456789012}}/{{anotherprovider}}/group/{{Accounting}}"
      ]
   }
]
```

You can't explicitly deny access within a policy. Therefore, all policy permissions are additive. For example, if one policy grants a user `aoss:ReadDocument`, and another policy grants `aoss:WriteDocument`, the user will have *both* permissions. If a third policy grants the same user `aoss:*`, then the user can perform *all* actions on the associated index; more restrictive permissions don't override less restrictive ones.

## Supported policy permissions
<a name="serverless-data-supported-permissions"></a>

The following permissions are supported in data access policies. For the OpenSearch API operations that each permission allows, see [Supported OpenSearch API operations and permissions](serverless-genref.md#serverless-operations).

**Collection permissions**
+ `aoss:CreateCollectionItems`
+ `aoss:DeleteCollectionItems`
+ `aoss:UpdateCollectionItems`
+ `aoss:DescribeCollectionItems`
+ `aoss:*`

**Index permissions**
+ `aoss:ReadDocument`
+ `aoss:WriteDocument`
+ `aoss:CreateIndex`
+ `aoss:DeleteIndex`
+ `aoss:UpdateIndex`
+ `aoss:DescribeIndex`
+ `aoss:*`

## Sample datasets on OpenSearch Dashboards
<a name="serverless-data-sample-index"></a>

OpenSearch Dashboards provides [sample datasets](https://opensearch.org/docs/latest/dashboards/quickstart-dashboards/#adding-sample-data) that come with visualizations, dashboards, and other tools to help you explore Dashboards before you add your own data. To create indexes from this sample data, you need a data access policy that provides permissions to the dataset that you want to work with. The following policy uses a wildcard (`*`) to provide permissions to all three sample datasets.

```
[
  {
    "Rules": [
      {
        "Resource": [
          "index/{{<collection-name>}}/opensearch_dashboards_sample_data_*"
        ],
        "Permission": [
          "aoss:CreateIndex",
          "aoss:DescribeIndex",
          "aoss:ReadDocument"
        ],
        "ResourceType": "index"
      }
    ],
    "Principal": [
      "arn:aws:iam::{{<account-id>}}:user/{{<user>}}"
    ]
  }
]
```

## Creating data access policies (console)
<a name="serverless-data-access-console"></a>

You can create a data access policy using the visual editor, or in JSON format. Any new collections that match one of the patterns defined in the policy will be assigned the corresponding permissions when you create the collection.

**To create an OpenSearch Serverless data access policy**

1. Open the Amazon OpenSearch Service console at [https://console.aws.amazon.com/aos/home](https://console.aws.amazon.com/aos/home ).

1. In the left navigation pane, expand **Serverless** and under **Security**, choose **Data access policies**.

1. Choose **Create access policy**.

1. Provide a name and description for the policy.

1. Provide a name for the first rule in your policy. For example, "Logs collection access".

1. Choose **Add principals** and select one or more IAM roles or [SAML users and groups](serverless-saml.md) to provide data access to.
**Note**  
In order to select principals from the dropdown menus, you must have the `iam:ListUsers` and `iam:ListRoles` permissions (for IAM principals) and `aoss:ListSecurityConfigs` permission (for SAML identities). 

1. Choose **Grant** and select the alias, template, and index permissions to grant the associated principals. For a full list of permissions and the access they allow, see [Supported OpenSearch API operations and permissions](serverless-genref.md#serverless-operations).

1. (Optional) Configure additional rules for the policy.

1. Choose **Create**. There might be about a minute of lag time between when you create the policy and when the permissions are enforced. If it takes more than 5 minutes, contact [Support](https://console.aws.amazon.com/support/home).

**Important**  
If your policy only includes index permissions (and no collection permissions), you might still see a message for matching collections stating `Collection cannot be accessed yet. Configure data access policies so that users can access the data within this collection`. You can ignore this warning. Allowed principals can still perform their assigned index-related operations on the collection.

## Creating data access policies (AWS CLI)
<a name="serverless-data-access-cli"></a>

To create a data access policy using the OpenSearch Serverless API, use the `CreateAccessPolicy` command. The command accepts both inline policies and .json files. Inline policies must be encoded as a [JSON escaped string](https://www.freeformatter.com/json-escape.html).

The following request creates a data access policy:

```
aws opensearchserverless create-access-policy \
    --name {{marketing}} \
    --type data \
    --policy "[{\"Rules\":[{\"ResourceType\":\"collection\",\"Resource\":[\"collection/autopartsinventory\",\"collection/sales*\"],\"Permission\":[\"aoss:UpdateCollectionItems\"]},{\"ResourceType\":\"index\",\"Resource\":[\"index/autopartsinventory/*\",\"index/salesorders/orders*\"],\"Permission\":[\"aoss:ReadDocument\",\"aoss:DescribeIndex\"]}],\"Principal\":[\"arn:aws:iam::123456789012:user/Shaheen\"]}]"
```

To provide the policy within a .json file, use the format `--policy file://{{my-policy}}.json`.

The principals included in the policy can now use the [OpenSearch operations](#serverless-data-supported-permissions) that they were granted access to.

## Viewing data access policies
<a name="serverless-data-access-list"></a>

Before you create a collection, you might want to preview the existing data access policies in your account to see which one has a resource pattern that matches your collection's name. The following [ListAccessPolicies](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_ListAccessPolicies.html) request lists all data access policies in your account:

```
aws opensearchserverless list-access-policies --type data
```

The request returns information about all configured data access policies. To view the pattern rules defined in the one specific policy, find the policy information in the contents of the `accessPolicySummaries` element in the response. Note the `name` and `type` of this policy and use these properties in a [GetAccessPolicy](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_GetAccessPolicy.html) request to receive a response with the following policy details: 

```
{
    "accessPolicyDetails": [
        {
            "type": "data",
            "name": "my-policy",
            "policyVersion": "MTY2NDA1NDE4MDg1OF8x",
            "description": "My policy",
            "policy": "[{\"Rules\":[{\"ResourceType\":\"collection\",\"Resource\":[\"collection/autopartsinventory\",\"collection/sales*\"],\"Permission\":[\"aoss:UpdateCollectionItems\"]},{\"ResourceType\":\"index\",\"Resource\":[\"index/autopartsinventory/*\",\"index/salesorders/orders*\"],\"Permission\":[\"aoss:ReadDocument\",\"aoss:DescribeIndex\"]}],\"Principal\":[\"arn:aws:iam::123456789012:user/Shaheen\"]}]",
            "createdDate": 1664054180858,
            "lastModifiedDate": 1664054180858
        }
    ]
}
```

You can include resource filters to limit the results to policies that contain specific collections or indexes:

```
aws opensearchserverless list-access-policies --type data --resource "index/{{autopartsinventory}}/{{*}}"
```

To view details about a specific policy, use the [GetAccessPolicy](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_GetAccessPolicy.html) command.

## Updating data access policies
<a name="serverless-data-access-update"></a>

When you update a data access policy, all associated collections are impacted. To update a data access policy in the OpenSearch Serverless console, choose **Data access control**, select the policy to modify, and choose **Edit**. Make your changes and choose **Save**.

To update a data access policy using the OpenSearch Serverless API, send an `UpdateAccessPolicy` request. You must include a policy version, which you can retrieve using the `ListAccessPolicies` or `GetAccessPolicy` commands. Including the most recent policy version ensures that you don't inadvertently override a change made by someone else.

The following [UpdateAccessPolicy](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_UpdateAccessPolicy.html) request updates a data access policy with a new policy JSON document:

```
aws opensearchserverless update-access-policy \
    --name sales-inventory \
    --type data \
    --policy-version {{MTY2NDA1NDE4MDg1OF8x}} \
    --policy file://{{my-new-policy}}.json
```

There might be a few minutes of lag time between when you update the policy and when the new permissions are enforced.

## Deleting data access policies
<a name="serverless-data-access-delete"></a>

When you delete a data access policy, all associated collections lose the access that is defined in the policy. Make sure that your IAM and SAML users have the appropriate access to the collection before you delete a policy. To delete a policy in the OpenSearch Serverless console, select the policy and choose **Delete**.

You can also use the [DeleteAccessPolicy](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_DeleteAccessPolicy.html) command:

```
aws opensearchserverless delete-access-policy --name {{my-policy}} --type data
```

## Cross-account data access
<a name="serverless-data-access-cross"></a>

While you can't create a data access policy with cross-account identity or cross-account collections, you can still set up cross-account access with the assume role option. For example, if `{{account-a}}` owns a collection that `{{account-b}}` needs access to, the user from `{{account-b}}` can assume a role in `{{account-a}}`. The role must have the IAM permissions `aoss:APIAccessAll` and `aoss:DashboardsAccessAll`, and be included in the data access policy on `{{account-a}}`.