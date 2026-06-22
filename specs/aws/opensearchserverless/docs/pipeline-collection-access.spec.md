---
id: "@specs/aws/opensearchserverless/docs/pipeline-collection-access"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Granting pipelines access to collections"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Granting pipelines access to collections

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/pipeline-collection-access
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Granting Amazon OpenSearch Ingestion pipelines access to collections
<a name="pipeline-collection-access"></a>

An Amazon OpenSearch Ingestion pipeline can write to an OpenSearch Serverless public collection or VPC collection. To provide access to the collection, you configure an AWS Identity and Access Management (IAM) pipeline role with a permissions policy that grants access to the collection. The pipeline assumes this role in order to sign requests to the OpenSearch Serverless collection sink.

**Important**  
You can choose to manually create the pipeline role, or you can have OpenSearch Ingestion create it for you during pipeline creation. If you choose automatic role creation, OpenSearch Ingestion adds all required permissions to the pipeline role access policy based on the source and sink that you choose. It creates a pipeline role in IAM with the prefix `OpenSearchIngestion-` and the suffix that you enter. For more information, see [Pipeline role](pipeline-security-overview.md#pipeline-security-sink).  
If you have OpenSearch Ingestion create the pipeline role for you, you still need to include the role in the collection's data access policy, either before or after you create the pipeline. See step 2 for instructions. 

During pipeline creation, OpenSearch Ingestion creates an AWS PrivateLink connection between the pipeline and the OpenSearch Serverless collection. All traffic from the pipeline goes through this VPC endpoint and is routed to the collection. In order to reach the collection, the endpoint must be granted access to the collection through a network access policy.

![Pipeline connects to PrivateLink VPC endpoint, then network policy evaluation, then collection.](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/osis-aoss-permissions.png)


**Topics**
+ [Step 1: Create the pipeline role](#pipeline-collection-access-configure)
+ [Step 2: Configure data and network access for the collection](#pipeline-access-collection)

## Step 1: Create the pipeline role
<a name="pipeline-collection-access-configure"></a>

The pipeline role must have an attached permissions policy that allows it to send data to the collection sink. It must also have a trust relationship that allows OpenSearch Ingestion to assume the role. For instructions on how to attach a policy to a role, see [Adding IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html#add-policies-console) in the *IAM User Guide*.

The following sample policy demonstrates the [least privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege) that you can provide in a pipeline role access policy for it to write to collections:

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "Statement1",
            "Effect": "Allow",
            "Action": [
                "aoss:APIAccessAll",
                "aoss:BatchGetCollection",
                "aoss:CreateSecurityPolicy",
                "aoss:GetSecurityPolicy",
                "aoss:UpdateSecurityPolicy"
            ],
            "Resource": "*"
        }
    ]
}
```

------

The role must have the following [trust relationship](https://docs.aws.amazon.com/IAM/latest/UserGuide/roles-managingrole-editing-console.html#roles-managingrole_edit-trust-policy), which allows OpenSearch Ingestion to assume it:

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "osis-pipelines.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
```

------

## Step 2: Configure data and network access for the collection
<a name="pipeline-access-collection"></a>

Create an OpenSearch Serverless collection with the following settings. For instructions to create a collection, see [Creating collections](serverless-create.md).

### Data access policy
<a name="pipeline-data-access"></a>

Create a [data access policy](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-data-access.html) for the collection that grants the required permissions to the pipeline role. For example:

```
[
  {
    "Rules": [
      {
        "Resource": [
          "index/{{collection-name}}/*"
        ],
        "Permission": [
          "aoss:CreateIndex",
          "aoss:UpdateIndex",
          "aoss:DescribeIndex",
          "aoss:WriteDocument"
        ],
        "ResourceType": "index"
      }
    ],
    "Principal": [
      "arn:aws:iam::{{account-id}}:role/{{pipeline-role}}"
    ],
    "Description": "Pipeline role access"
  }
]
```

**Note**  
In the `Principal` element, specify the Amazon Resource Name (ARN) of the pipeline role.

### Network access policy
<a name="pipeline-network-access"></a>

Each collection that you create in OpenSearch Serverless has at least one network access policy associated with it. Network access policies determine whether the collection is accessible over the internet from public networks, or whether it must be accessed privately. For more information about network policies, see [Network access for Amazon OpenSearch Serverless](serverless-network.md).

Within a network access policy, you can only specify OpenSearch Serverless-managed VPC endpoints. For more information, see [Data plane access through AWS PrivateLink](serverless-vpc.md). However, in order for the pipeline to write to the collection, the policy must also grant access to the VPC endpoint that OpenSearch Ingestion automatically creates between the pipeline and the collection. Therefore, if you choose an OpenSearch Serverless collection as the destination sink for a pipeline, you must enter the name of the associated network policy in the **Network policy name** field.

During pipeline creation, OpenSearch Ingestion checks for the existence of the specified network policy. If it doesn't exist, OpenSearch Ingestion creates it. If it does exist, OpenSearch Ingestion updates it by adding a new rule to it. The rule grants access to the VPC endpoint that connects the pipeline and the collection. 

For example:

```
{
   "Rules":[
      {
         "Resource":[
            "collection/{{my-collection}}"
         ],
         "ResourceType":"collection"
      }
   ],
   "SourceVPCEs":[
      "vpce-{{0c510712627e27269}}" # The ID of the VPC endpoint that OpenSearch Ingestion creates between the pipeline and collection
   ],
   "Description":"Created by Data Prepper"
}
```

In the console, any rules that OpenSearch Ingestion adds to your network policies are named **Created by Data Prepper**:

![Created by Data Prepper section showing access type, VPC endpoints, and resource settings.](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/osis-aoss-network.png)


**Note**  
In general, a rule that specifies public access for a collection overrides a rule that specifies private access. Therefore, if the policy already had *public* access configured, this new rule that OpenSearch Ingestion adds doesn't actually change the behavior of the policy. For more information, see [Policy precedence](serverless-network.md#serverless-network-precedence).

If you stop or delete the pipeline, OpenSearch Ingestion deletes the VPC endpoint between the pipeline and the collection. It also modifies the network policy to remove the VPC endpoint from the list of allowed endpoints. If you restart the pipeline, it recreates the VPC endpoint and re-updates the network policy with the endpoint ID.