---
id: "@specs/aws/opensearchserverless/docs/serverless-collection-groups-procedures"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Create collection groups"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Create collection groups

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/serverless-collection-groups-procedures
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Create collection groups
<a name="serverless-collection-groups-procedures"></a>

This topic describes how to create, configure, and manage collection groups in Amazon OpenSearch Serverless. Use collection groups to organize collections and share compute resources to optimize costs. Set minimum and maximum OCU limits at the collection group level to control performance and spending.

## Create a collection group
<a name="collection-groups-create"></a>

Use the following procedures to create a new collection group and configure its settings. You can create a collection group using the OpenSearch Serverless console, AWS CLI, or the AWS SDKs. When you create a collection group, you specify capacity limits and other configuration options.

------
#### [ Console ]

1. Open the Amazon OpenSearch Service console at [https://console.aws.amazon.com/aos/](https://console.aws.amazon.com/aos/).

1. In the left navigation pane, expand **Serverless** and choose **Collection groups**.

1. Choose **Create collection group**. The NextGen collection group creation form opens by default.
**Tip**  
To create a Classic collection group instead, choose **Switch to Classic**. Classic collection groups support a **Deployment type** option that is not available for NextGen collection groups. To switch back to the NextGen form, choose **Switch to NextGen**.

1. For **Collection group name**, enter a name for your collection group. The name must meet the following criteria:
   + Contains only lowercase letters a–z, the numbers 0–9, and hyphens (-)
   + Must be 3–32 characters

1. (Optional) For **Description**, enter a description for your collection group.

1. In the **Capacity management** section, configure the OCU limits:
   + **Minimum indexing capacity** (in OCUs) – Optional. Leave blank for no minimum.
   + **Maximum indexing capacity** (in OCUs) – Default is 96.
   + **Minimum search capacity** (in OCUs) – Optional. Leave blank for no minimum.
   + **Maximum search capacity** (in OCUs) – Default is 96.

1. (Optional) In the **Tags** section, add tags to help organize and identify your collection group.

1. Choose **Create collection group**.

------
#### [ AWS CLI ]
+ Use the [create-collection-group](https://docs.aws.amazon.com/cli/latest/reference/opensearchserverless/create-collection-group.html) command to create a new collection group. In the command, replace the {{example}} content with your own specific information.

  ```
  aws opensearchserverless create-collection-group \
      --name {{my-collection-group}} \
      --description "{{Collection group for production workloads}}" \
      --capacity-limits maxIndexingCapacityInOCU={{20}},maxSearchCapacityInOCU={{20}},minIndexingCapacityInOCU={{2}},minSearchCapacityInOCU={{2}} \
      --tags key={{Environment}},value={{Production}} key={{Team}},value={{DataEngineering}}
  ```

  The command returns details about the created collection group, including its unique ID and ARN.

------

## Add a collection to a collection group
<a name="create-collection-in-group"></a>

When you create a collection, you assign it to a collection group.

------
#### [ Console ]

**To add a collection to a collection group**

1. Open the Amazon OpenSearch Service console at [https://console.aws.amazon.com/aos/](https://console.aws.amazon.com/aos/).

1. In the left navigation pane, choose **Serverless**, then choose **Collections**.

1. Choose **Create collection**.

1. For **Collection name**, enter a name for your collection. The name must be 3–32 characters long, start with a lowercase letter, and contain only lowercase letters, numbers, and hyphens.

1. (Optional) For **Description**, enter a description for your collection.

1. Assign the collection to a collection group. The process differs depending on the collection type:
   + **NextGen – Express Create** – OpenSearch Serverless automatically assigns a collection group. For a first-time user, a default collection group is generated based on the collection name. For a returning user, an existing compatible collection group is selected by default. To change the assignment, choose a different group from the dropdown.
   + **NextGen – Standard Create** – Select an existing compatible collection group from the dropdown, or create a new collection group with custom capacity limits.
   + **Classic** – In the **Collection group** section, select the collection group that you want to assign the collection to. A collection can belong to only one collection group at a time. (Optional) To create a new group, choose **Create a new group**. This opens the Create collection group workflow.

1. Complete the remaining steps in the workflow to create the collection.
**Important**  
Do not navigate away from the Create collection workflow.

------
#### [ AWS CLI ]
+ Use the [create-collection](https://docs.aws.amazon.com/cli/latest/reference/opensearchserverless/create-collection.html) command to create a collection and add it to an existing collection group. In the command, replace the {{example}} content with your own information.

  ```
  aws opensearchserverless create-collection \
      --name {{my-collection}} \
      --type SEARCH \
      --collection-group-name {{my-collection-group}} \
      --description "{{Collection for search workloads}}"
  ```

------