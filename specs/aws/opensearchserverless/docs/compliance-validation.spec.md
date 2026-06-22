---
id: "@specs/aws/opensearchserverless/docs/compliance-validation"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Compliance validation"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Compliance validation

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/compliance-validation
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Compliance validation for Amazon OpenSearch Service
<a name="compliance-validation"></a>

Third-party auditors assess the security and compliance of Amazon OpenSearch Service as part of multiple AWS compliance programs. These programs include SOC, PCI, and HIPAA.

If you have compliance requirements, consider using any version of OpenSearch or Elasticsearch 6.0 or later. Earlier versions of Elasticsearch don't offer a combination of [encryption of data at rest](encryption-at-rest.md) and [node-to-node encryption](ntn.md) and are unlikely to meet your needs. You might also consider using any version of OpenSearch or Elasticsearch 6.7 or later if [fine-grained access control](fgac.md) is important to your use case. Regardless, choosing a particular OpenSearch or Elasticsearch version when you create a domain does not guarantee compliance. 

To learn whether an AWS service is within the scope of specific compliance programs, see [AWS services in Scope by Compliance Program](https://aws.amazon.com/compliance/services-in-scope/) and choose the compliance program that you are interested in. For general information, see [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/).

You can download third-party audit reports using AWS Artifact. For more information, see [Downloading Reports in AWS Artifact](https://docs.aws.amazon.com/artifact/latest/ug/downloading-documents.html).

Your compliance responsibility when using AWS services is determined by the sensitivity of your data, your company's compliance objectives, and applicable laws and regulations. For more information about your compliance responsibility when using AWS services, see [AWS Security Documentation](https://docs.aws.amazon.com/security/).