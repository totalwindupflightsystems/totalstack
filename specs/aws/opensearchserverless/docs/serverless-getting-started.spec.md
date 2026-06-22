---
id: "@specs/aws/opensearchserverless/docs/serverless-getting-started"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Tutorial: Getting started with OpenSearch Serverless"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Tutorial: Getting started with OpenSearch Serverless

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/serverless-getting-started
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Tutorial: Getting started with Amazon OpenSearch Serverless
<a name="serverless-getting-started"></a>

This tutorial shows you the basic steps to get an Amazon OpenSearch Serverless *search* collection up and running quickly. With a search collection, you can power applications in your internal networks and internet-facing applications, such as ecommerce website search and content search. 

To learn how to use a *vector search* collection, see [Working with vector search collections](serverless-vector-search.md). For more detailed information about using collections, see [Managing Amazon OpenSearch Serverless collections](serverless-manage.md) and the other topics within this guide.

You complete the following steps in this tutorial:

1. [Configure permissions](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-getting-started.html#serverless-gsg-permissions)

1. [Create a collection](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-getting-started.html#serverless-gsg-create)

1. [Upload and search data](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-getting-started.html#serverless-gsg-index)

1. [Delete the collection](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-getting-started.html#serverless-gsg-delete)
**Note**  
Use only ASCII characters for your `IndexName`. If you do not use ASCII characters for your `IndexName`, the `IndexName` in CloudWatch metrics is converted to a URL encoded format for non-ASCII characters.

## Step 1: Configure permissions
<a name="serverless-gsg-permissions"></a>

To complete this tutorial and to use OpenSearch Serverless in general, you must have the correct IAM permissions. In this tutorial, you create a collection, upload and search data, and then delete the collection.

Your user or role must have an attached [identity-based policy](security-iam-serverless.md#security-iam-serverless-id-based-policies) with the following minimum permissions:

------
#### [ JSON ]

****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Action": [
        "aoss:CreateCollection",
        "aoss:ListCollections",
        "aoss:BatchGetCollection",
        "aoss:DeleteCollection",
        "aoss:CreateAccessPolicy",
        "aoss:ListAccessPolicies",
        "aoss:UpdateAccessPolicy",
        "aoss:CreateSecurityPolicy",
        "aoss:GetSecurityPolicy",
        "aoss:UpdateSecurityPolicy",
        "iam:ListUsers",
        "iam:ListRoles"
      ],
      "Effect": "Allow",
      "Resource": "*"
    }
  ]
}
```

------

For more information about OpenSearch Serverless IAM permissions, see [Identity and Access Management for Amazon OpenSearch Serverless](security-iam-serverless.md).

## Step 2: Create a collection
<a name="serverless-gsg-create"></a>

A collection is a group of OpenSearch indexes that work together to support a specific workload or use case.

**To create an OpenSearch Serverless collection**

1. Open the Amazon OpenSearch Service console at [https://console.aws.amazon.com/aos/home](https://console.aws.amazon.com/aos/home).

1. In the left navigation pane, choose **Collections**.

1. Choose **Create collection**.

1. For **Name**, enter `movies`.

1. For **Collection type**, choose **Search**. For more information, see [Choosing a collection type](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-overview.html#serverless-usecase).

1. For **Collection creation method**, choose **Express Create**.

1. Review the default settings. These include the collection group, OpenSearch UI application settings, encryption with an AWS owned key, public network access, and the auto-generated data access policy.

1. Choose **Create collection**.

1. Wait for the collection status to change to `Active`. This might take several minutes.

**Tip**  
This tutorial uses the NextGen Express Create method. You can also access Express Create from the **Express create** button in the info banner on the landing page for a quicker path. For more control over encryption, network, and data access settings, use **Standard Create**. To use the Classic collection creation wizard, choose **Switch to Classic**. For more information, see [Creating collections](serverless-create.md).

## Step 3: Upload and search data
<a name="serverless-gsg-index"></a>

You can upload data to an OpenSearch Serverless collection using [Postman](https://www.postman.com/downloads/) or cURL. For simplicity, these examples use **Dev Tools** within the OpenSearch Dashboards console.

**To index and search data in the movies collection**

1. Choose **Collections** in the left navigation pane and choose the **movies** collection to open its details page.

1. Choose the OpenSearch Dashboards URL for the collection. The URL takes the format `https://dashboards.{{{region}}}.aoss.amazonaws.com/_login/?collectionId={{{collection-id}}}`. 

1. Within OpenSearch Dashboards, open the left navigation pane and choose **Dev Tools**.

1. To create a single index called *movies-index*, send the following request:

   ```
   PUT movies-index{{ }}
   ```  
![OpenSearch Dashboards console showing PUT request to movies-index with response status 200.](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/serverless-gsg-create.png)

1. To index a single document into *movies-index*, send the following request:

   ```
   PUT movies-index/_doc/1
   { 
     "title": "Shawshank Redemption",
     "genre": "Drama",
     "year": 1994
   }
   ```

1. To search data in OpenSearch Dashboards, you need to configure at least one index pattern. OpenSearch uses these patterns to identify which indexes you want to analyze. Open the left navigation pane, choose **Stack Management**, choose **Index Patterns**, and then choose **Create index pattern**. For this tutorial, enter *movies*.

1. Choose **Next step** and then choose **Create index pattern**. After the pattern is created, you can view the various document fields such as `title` and `genre`.

1. To begin searching your data, open the left navigation pane again and choose **Discover**, or use the [search API](https://opensearch.org/docs/latest/api-reference/search/) within **Dev Tools**.

## Handling errors
<a name="serverless-gsg-data-plane-errors"></a>

When you run index and search operations, you might get the following error responses:
+ `HTTP 507` – Indicates that an internal server error occurred. This error generally indicates that your OpenSearch compute units (OCUs) are overloaded by the volume or complexity of your requests. Although OpenSearch Serverless scales automatically to manage the load, there can be a delay in deploying additional resources. 

  To mitigate this error, implement an exponential backoff retry policy. This approach temporarily reduces the request rate to effectively manage the load. For more details, refer to [Retry behavior](https://docs.aws.amazon.com/sdkref/latest/guide/feature-retry-behavior.html) in the *AWS SDKs and Tools Reference Guide*.
+ `HTTP 402` – Indicates that you reached the maximum OpenSearch compute unit (OCU) capacity limit. Optimize your workload to reduce the OCU usage or request a quota increase.

## Step 4: Delete the collection
<a name="serverless-gsg-delete"></a>

Because the *movies* collection is for test purposes, delete it when you're done experimenting.

**To delete an OpenSearch Serverless collection**

1. Go back to the Amazon OpenSearch Service console.

1. Choose **Collections** in the left navigation pane and select the **movies** collection.

1. Choose **Delete** and confirm deletion.

## Next steps
<a name="serverless-gsg-next"></a>

Now that you know how to create a collection and index data, you might want to try the following:
+ Explore more advanced options for creating a collection. For more information, see [Managing Amazon OpenSearch Serverless collections](serverless-manage.md).
+ Configure security policies to manage collection security at scale. For more information, see [Overview of security in Amazon OpenSearch Serverless](serverless-security.md).
+ Use other methods to index data into collections. For more information, see [Ingesting data into Amazon OpenSearch Serverless collections](serverless-clients.md).