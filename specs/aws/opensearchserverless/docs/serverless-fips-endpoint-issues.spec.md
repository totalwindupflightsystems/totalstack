---
id: "@specs/aws/opensearchserverless/docs/serverless-fips-endpoint-issues"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Troubleshoot FIPS Private Hosted Zones"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Troubleshoot FIPS Private Hosted Zones

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/serverless-fips-endpoint-issues
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Resolve FIPS endpoint connectivity issues in private hosted zones
<a name="serverless-fips-endpoint-issues"></a>

FIPS endpoints work with Amazon OpenSearch Serverless collections that have public access. For newly created VPC collections that use newly created VPC endpoints, FIPS endpoints function as expected. For other VPC collections, you might need to perform manual setup to ensure FIPS endpoints operate correctly.

**To configure FIPS private hosted zones in Amazon Route 53**

1. Open the Route 53 console at [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/).

1. Review your hosted zones:

   1. Locate the hosted zones for the AWS Regions your collections are in.

   1. Verify the hosted zone naming patterns:
      + Non-FIPS format: `{{region}}.aoss.amazonaws.com`.
      + FIPS format: `{{region}}.aoss-fips.amazonaws.com`.

   1. Confirm the **Type** for all of your hosted zones is set to **Private hosted zone**.

1. If the FIPS private hosted zone is missing:

   1. Select the corresponding non-FIPS private hosted zone.

   1. Copy the **Associated VPCs** information. For example: `vpc-1234567890abcdef0 | us-east-2`.

   1. Find the wildcard domain record. For example: `*.us-east-2.aoss.amazonaws.com`.

   1. Copy the **Value/Route traffic to** information. For example:`uoc1c1qsw7poexampleewjeno1pte3rw.3ym756xh7yj.aoss.searchservices.aws`.

1. Create the FIPS private hosted zone:

   1. Create a new private hosted zone with the FIPS format. For example: `us-east-2.aoss-fips.amazonaws.com`.

   1. For **Associated VPCs**, enter the VPC information you copied from the non-FIPS private hosted zone.

1. Add a new record with the following settings:

   1. Record name: \*

   1. Record type: CNAME

   1. Value: Enter the **Value/Route traffic to** information you copied earlier.

## Common Issues
<a name="serverless-fips-endpoint-common-problems"></a>

If you experience connectivity issues with your FIPS-compliant VPC endpoints, use the following information to help resolve the problem.
+ DNS resolution failures - You cannot resolve the FIPS endpoint domain name within your VPC
+ Connection timeouts - Your requests to the FIPS endpoint time out
+ Access denied errors - Authentication or authorization fails when using FIPS endpoints
+ Missing private hosted zone records for VPC-only collections

**To troubleshoot FIPS endpoint connectivity**

1. Verify your Private Hosted Zone configuration:

   1. Confirm that a Private Hosted Zone exists for the FIPS endpoint domain (`*.region.aoss-fips.amazonaws.com`.

   1. Verify that the private hosted zone is associated with the correct VPC.

      For more information, see [Private hosted zones](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted- zones-private.html) in the *Amazon Route 53 Developer Guide*, and [Manage DNS names](https://docs.aws.amazon.com/vpc/latest/privatelink/manage-dns-names.html) in the *AWS PrivateLink Guide*.

1. Test DNS resolution:

   1. Connect to an EC2 instance in your VPC.

   1. Run the following command:

      ```
      nslookup collection-id.region.aoss-fips.amazonaws.com
      ```

   1. Confirm that the response includes the private IP address of your VPC endpoint.

      For more information, see [Endpoint policies](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints- access.html#endpoint-dns-verification), and [DNS attributes](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-dns.html#vpc- dns-troubleshooting) in the *Amazon VPC User Guide*.

1. Check your security group settings:

   1. Verify that the security group attached to the VPC endpoint permits HTTPS traffic (port 443) from your resources.

   1. Confirm that security groups for your resources permit outbound traffic to the VPC endpoint.

   For more information, see [Endpoint policies](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html#vpc-endpoint-security-groups) in the *AWS PrivateLink Guide*, and [Security groups](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html#SecurityGroupRules) in the *Amazon VPC User Guide *.

1. Review your network ACL configuration:

   1. Verify that network ACLs permit traffic between your resources and the VPC endpoint.

     For more information, see [Network ACLs](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network- acls.html#nacl-troubleshooting) in the *Amazon VPC User Guide*.

1. Review your endpoint policy:

   1. Check that the VPC endpoint policy permits the required actions on your OpenSearch Serverless resources.

     For more information, see [VPC endpoint permissions required](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-vpc.html#serverless-vpc-permissions), and [Endpoints policies](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints- access.html#vpc-endpoint-policies) in the *AWS PrivateLink Guide*.

**Tip**  
If you use custom DNS resolvers in your VPC, configure them to forward requests for `*.amazonaws.com` domains to the AWS servers.