---
id: "@specs/aws/opensearchserverless/docs/serverless-dashboards"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Accessing OpenSearch Dashboards"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Accessing OpenSearch Dashboards

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/serverless-dashboards
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Accessing OpenSearch Dashboards
<a name="serverless-dashboards"></a>

After you create a collection with the AWS Management Console, you can navigate to the collection's OpenSearch Dashboards URL. You can find the Dashboards URL by choosing **Collections** in the left navigation pane and selecting the collection to open its details page. The URL takes the format `https://dashboards.{{us-east-1}}.aoss.amazonaws.com/_login/?collectionId={{07tjusf2h91cunochc}}`. After you navigate to the URL, you automatically log in to Dashboards.

If you already have the OpenSearch Dashboards URL available but aren't on the AWS Management Console, calling the Dashboards URL from the browser will redirect to the console. After you enter your AWS credentials, you automatically log in to Dashboards. For information about accessing collections for SAML, see [Accessing OpenSearch Dashboards with SAML](serverless-saml.md#serverless-saml-dashboards).

The OpenSearch Dashboards console timeout is one hour and isn't configurable.

**Note**  
On May 10, 2023, OpenSearch introduced a common global endpoint for OpenSearch Dashboards. You can now navigate to OpenSearch Dashboards in the browser with a URL that takes the format `https://dashboards.{{us-east-1}}.aoss.amazonaws.com/_login/?collectionId={{07tjusf2h91cunochc}}`. To ensure backward compatibility, OpenSearch continues to support the existing collection specific OpenSearch Dashboards endpoints with the format `https://{{07tjusf2h91cunochc}}.{{us-east-1}}.aoss.amazonaws.com/_dashboards`.