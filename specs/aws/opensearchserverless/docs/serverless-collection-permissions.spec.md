---
id: "@specs/aws/opensearchserverless/docs/serverless-collection-permissions"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Configuring permissions for collections"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Configuring permissions for collections

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/serverless-collection-permissions
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Configuring permissions for collections
<a name="serverless-collection-permissions"></a>

OpenSearch Serverless uses the following AWS Identity and Access Management (IAM) permissions for creating and managing collections. You can specify IAM conditions to restrict users to specific collections.
+ `aoss:CreateCollection` – Create a collection.
+ `aoss:ListCollections` – List collections in the current account.
+ `aoss:BatchGetCollection` – Get details about one or more collections.
+ `aoss:UpdateCollection` – Modify a collection.
+ `aoss:DeleteCollection` – Delete a collection.

The following sample identity-based access policy provides the minimum permissions necessary for a user to manage a single collection named `Logs`:

```
[
   {
      "Sid":"Allows managing logs collections",
      "Effect":"Allow",
      "Action":[
         "aoss:CreateCollection",
         "aoss:ListCollections",
         "aoss:BatchGetCollection",
         "aoss:UpdateCollection",
         "aoss:DeleteCollection",
         "aoss:CreateAccessPolicy",
         "aoss:CreateSecurityPolicy"
      ],
      "Resource":"*",
      "Condition":{
         "StringEquals":{
            "aoss:collection":"{{Logs}}"
         }
      }
   }
]
```

`aoss:CreateAccessPolicy` and `aoss:CreateSecurityPolicy` are included because encryption, network, and data access policies are required for a collection to function properly. For more information, see [Identity and Access Management for Amazon OpenSearch Serverless](security-iam-serverless.md).

**Note**  
If you're creating the first collection in your account, you also require the `iam:CreateServiceLinkedRole` permission. For more information, see [Using service-linked roles to create OpenSearch Serverless collections](serverless-service-linked-roles.md).