---
id: "@specs/aws/opensearchserverless/docs/fgac-http-auth"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Tutorial: Internal user database with basic authentication"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Tutorial: Internal user database with basic authentication

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/fgac-http-auth
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Tutorial: Configure a domain with the internal user database and HTTP basic authentication
<a name="fgac-http-auth"></a>

This tutorial covers another popular [fine-grained access control](fgac.md) use case: a master user in the internal user database and HTTP basic authentication for OpenSearch Dashboards. The master user can then sign in to OpenSearch Dashboards, create an internal user, map the user to a role, and use fine-grained access control to limit the user's permissions.

You'll complete the following steps in this tutorial:

1. [Create a domain with a master user](#fgac-http-auth-domain)

1. [Configure an internal user in OpenSearch Dashboards](#fgac-http-auth-dashboards-user)

1. [Map roles in OpenSearch Dashboards](#fgac-http-auth-dashboards-map)

1. [Test the permissions](#fgac-http-auth-test)

## Step 1: Create a domain
<a name="fgac-http-auth-domain"></a>

Navigate to the Amazon OpenSearch Service console at [https://console.aws.amazon.com/aos/home/](https://console.aws.amazon.com/aos/home/) and [create a domain](createupdatedomains.md) with the following settings:
+ OpenSearch 1.0 or later, or Elasticsearch 7.9 or later
+ Public access
+ Fine-grained access control with a master user in the internal user database (`TheMasterUser` for the rest of this tutorial)
+ Amazon Cognito authentication for Dashboards *disabled*
+ The following access policy:

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
          "AWS": "arn:aws:iam::{{111122223333}}:root"
        },
        "Action": [
          "es:ESHttp*"
        ],
        "Resource": "arn:aws:es:{{us-east-1}}:{{111122223333}}:domain/{{{domain-name}}}/*"
      }
    ]
  }
  ```

------
+ HTTPS required for all traffic to the domain
+ Node-to-node encryption
+ Encryption of data at rest

## Step 2: Create an internal user in OpenSearch Dashboards
<a name="fgac-http-auth-dashboards-user"></a>

Now that you have a domain, you can sign in to OpenSearch Dashboards and create an internal user.

1. Go back to the OpenSearch Service console and navigate to the OpenSearch Dashboards URL for the domain you created. The URL follows this format: `{{domain-endpoint}}/_dashboards/`.

1. Sign in with the `TheMasterUser`.

1. Choose **Add sample data** and add the sample flight data.

1. In the left navigation pane, choose **Security**, **Internal users**, **Create internal user**.

1. Name the user `new-user` and specify a password. Then choose **Create**.

## Step 3: Map roles in OpenSearch Dashboards
<a name="fgac-http-auth-dashboards-map"></a>

Now that your user is configured, you can map your user to a role.

1. Stay in the **Security** section of OpenSearch Dashboards and choose **Roles**, **Create role**.

1. Name the role `new-role`.

1. For **Index**, specify `opensearch_dashboards_sample_data_fli*` (`kibana_sample_data_fli*` on Elasticsearch domains) for the index pattern.

1. For the action group, choose **read**.

1. For **Document level security**, specify the following query:

   ```
   {
     "match": {
       "FlightDelay": true
     }
   }
   ```

1. For field-level security, choose **Exclude** and specify `FlightNum`.

1. For **Anonymization**, specify `Dest`.

1. Choose **Create**.

1. Choose **Mapped users**, **Manage mapping**. Then add `new-user` to **Users** and choose **Map**.

## Step 4: Test the permissions
<a name="fgac-http-auth-test"></a>

When your roles are mapped correctly, you can sign in as the limited user and test the permissions.

1. In a new, private browser window, navigate to the OpenSearch Dashboards URL for the domain, sign in using the `new-user` credentials, and choose **Explore on my own**.

1. Go to **Dev Tools** and run the default search:

   ```
   GET _search
   {
     "query": {
       "match_all": {}
     }
   }
   ```

   Note the permissions error. `new-user` doesn't have permissions to run cluster-wide searches.

1. Run another search:

   ```
   GET dashboards_sample_data_flights/_search
   {
     "query": {
       "match_all": {}
     }
   }
   ```

   Note that all matching documents have a `FlightDelay` field of `true`, an anonymized `Dest` field, and no `FlightNum` field.

1. In your original browser window, signed in as `TheMasterUser`, choose **Dev Tools** and perform the same searches. Note the difference in permissions, number of hits, matching documents, and included fields.