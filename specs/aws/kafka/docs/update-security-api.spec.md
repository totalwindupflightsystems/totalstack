---
id: "@specs/aws/kafka/docs/update-security-api"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Update cluster security settings using API"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Update cluster security settings using API

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/update-security-api
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Updating a cluster's security settings using the API
<a name="update-security-api"></a>

To update the security settings for a Amazon MSK cluster using the API, see [UpdateSecurity](https://docs.aws.amazon.com//msk/1.0/apireference/clusters-clusterarn-security.html#UpdateSecurity).

**Note**  
The AWS CLI and API operations for updating the security settings of a MSK cluster are idempotent. This means that if you invoke the security update operation and specify an authentication or encryption setting that is the same setting that the cluster currently has, that setting won't change.