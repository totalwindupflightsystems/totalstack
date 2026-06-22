---
id: "@specs/aws/opensearchserverless/docs/vpc-egress"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Routing domain egress traffic through your VPC"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Routing domain egress traffic through your VPC

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/vpc-egress
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Routing domain egress traffic through your VPC
<a name="vpc-egress"></a>

Learn how to route egress traffic from your Amazon OpenSearch Service VPC domain through your own VPC instead of the public internet.

**Note**  
This option only affects egress traffic from the domain. Ingress to the domain still works the same way, on ports 80 and 443.

## Overview
<a name="vpc-egress-overview"></a>

By default, egress from a VPC domain to custom endpoints leaves over the public internet.

When you enable egress through your VPC, egress traffic from the domain enters your VPC and is subject to your route tables, security groups, and network ACLs. Use this option when you need egress from the domain to be controlled through your VPC, or to reach private endpoints such as VPC endpoints from the domain.

## How it works
<a name="vpc-egress-architecture"></a>

When you enable egress on a VPC domain, OpenSearch Service places an additional *elastic network interface* (ENI) in each subnet you supply for the domain. Egress traffic from the domain leaves through these egress ENIs.

The egress ENIs are requester-managed. OpenSearch Service creates, configures, and deletes them for you, and you can't modify them from your account.

### Components in your VPC
<a name="vpc-egress-components"></a>

When egress is enabled, two resource types are involved in your VPC:
+ **Domain ENIs.** Created and managed by OpenSearch Service for inbound traffic to the domain. These exist on any VPC domain, with or without egress enabled.
+ **Egress ENIs.** Created by OpenSearch Service through its service-linked role and managed by the OpenSearch Service network plane. These carry egress traffic from the domain into your VPC.

In a Multi-AZ domain, egress ENIs are provisioned per Availability Zone, exactly matching the subnets you select for the domain.

### DNS resolution for egress
<a name="vpc-egress-dns"></a>

When egress through your VPC is enabled, the domain resolves hostnames through the default VPC resolver (the "\+2" address on your VPC CIDR). Custom DNS resolvers are not supported at launch.

Because the domain uses the VPC resolver, it can resolve:
+ Records in Amazon Route 53 private hosted zones associated with your VPC.
+ Private DNS names of VPC endpoints in your VPC.

**Important**  
If your VPC DNS is unreachable or misconfigured, the domain's egress integrations will fail. See [Troubleshooting](#vpc-egress-troubleshoot).

## Prerequisites
<a name="vpc-egress-prereqs"></a>

Before you enable egress through your VPC, make sure your VPC meets the following requirements:
+ DNS resolution and DNS hostnames are both enabled on the VPC.
+ The default VPC resolver (the "\+2" address on your VPC CIDR) is reachable from the subnets you plan to use for the domain.

**Subnet IP capacity.** Reserve the usual number of IP addresses for the domain ENIs (see [Reserving IP addresses in a VPC subnet](vpc.md#reserving-ip-vpc-endpoints)), plus additional IP addresses per subnet for the egress ENIs.

**Service-linked role.** The existing Amazon OpenSearch Service service-linked role gains the permissions needed to create and manage the egress ENIs. If you already use VPC domains, you don't need to recreate the role. To learn more, see [Using service-linked roles for Amazon OpenSearch Service](slr.md).

**Region availability.** Egress through your VPC is available in the Regions listed on the Amazon OpenSearch Service endpoints and quotas page.

## Enabling egress on a domain
<a name="vpc-egress-enable"></a>

You can enable egress on a VPC domain when you create the domain, or by updating an existing VPC domain. You can't enable egress on a public-endpoint domain. Enabling or disabling this option triggers a blue/green deployment.

### Console
<a name="vpc-egress-enable-console"></a>

1. Open the Amazon OpenSearch Service console.

1. Start creating a new domain, or select an existing VPC domain and choose **Edit**.

1. Under **Network**, choose **VPC access**, then select your VPC, subnets, and security groups as you would today.

1. Under **VPC Egress**, select **Enable Egress**.

1. Complete the remaining steps, and then submit the change.

### AWS CLI
<a name="vpc-egress-enable-cli"></a>

To create a domain with egress enabled, include `EgressEnabled` in `--vpc-options`:

```
aws opensearch create-domain \
  --domain-name example-domain \
  --engine-version OpenSearch_2.15 \
  --cluster-config InstanceType=r6g.large.search,InstanceCount=3,ZoneAwarenessEnabled=true \
  --vpc-options '{
      "SubnetIds": ["subnet-EXAMPLEAZ1", "subnet-EXAMPLEAZ2", "subnet-EXAMPLEAZ3"],
      "SecurityGroupIds": ["sg-EXAMPLE"],
      "EgressEnabled": true
  }'
```

To toggle egress on an existing VPC domain, use `update-domain-config`:

```
aws opensearch update-domain-config \
  --domain-name example-domain \
  --vpc-options '{
      "SubnetIds": ["subnet-EXAMPLEAZ1", "subnet-EXAMPLEAZ2", "subnet-EXAMPLEAZ3"],
      "SecurityGroupIds": ["sg-EXAMPLE"],
      "EgressEnabled": true
  }'
```

### API
<a name="vpc-egress-enable-api"></a>

To enable egress through your VPC, set `EgressEnabled` to `true` in `VPCOptions` on `CreateDomain` or `UpdateDomainConfig`. The value is returned in `VPCOptions` on `DescribeDomain` and `DescribeDomainConfig`.

```
{
  "SubnetIds": ["subnet-EXAMPLEAZ1", "subnet-EXAMPLEAZ2", "subnet-EXAMPLEAZ3"],
  "SecurityGroupIds": ["sg-EXAMPLE"],
  "EgressEnabled": true
}
```

For the full schema, see [VPCOptions](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_VPCOptions.html) in the *Amazon OpenSearch Service API Reference*.

## Updating or disabling
<a name="vpc-egress-update"></a>

You can turn egress on when you create a domain or at any time afterwards, and you can turn it off on a domain that has it enabled. You can also add or remove Availability Zones while egress stays enabled. A change to `EgressEnabled` triggers a blue/green deployment, the same as other VPC configuration changes. For more information, see [Making configuration changes in Amazon OpenSearch Service](managedomains-configuration-changes.md).

When you disable egress, OpenSearch Service removes the egress ENIs and related service-managed resources from your VPC. Deleting the domain cleans up all egress resources automatically.

## Verifying and monitoring
<a name="vpc-egress-monitor"></a>

After you enable egress, confirm that the egress ENIs exist in your selected subnets by viewing them in the Amazon EC2 console. Their descriptions identify the OpenSearch Service domain. To observe egress traffic leaving the domain, enable VPC Flow Logs on the egress ENIs. Check domain health in the OpenSearch Service console, and rely on the existing success and failure signals from your egress integrations (alerting destinations, machine learning connectors, snapshot repositories) for integration-level status.

## Troubleshooting
<a name="vpc-egress-troubleshoot"></a>

**An egress integration stopped working after you enabled egress.** Confirm that your VPC route table permits traffic from the egress ENIs to the destination, and that the VPC resolver is reachable and can resolve the destination hostname.

**Hostname resolution fails.** Confirm that DNS resolution and DNS hostnames are enabled on the VPC. If you use Route 53 private hosted zones or a Route 53 Resolver outbound endpoint, confirm the associated rules cover the destination.

**Not enough IP addresses in the subnet.** Expand the subnet or use a dedicated subnet for the domain. See [Reserving IP addresses in a VPC subnet](vpc.md#reserving-ip-vpc-endpoints).

**Service-linked role is missing permissions.** Recreate the service-linked role or attach the updated policy. See [Using service-linked roles for Amazon OpenSearch Service](slr.md).

**You can't enable egress on a public-endpoint domain.** Egress through your VPC is only available on VPC domains. Convert the domain first. See [Migrating from public access to VPC access](vpc.md#migrating-public-to-vpc).

**Warning**  
The egress ENIs are service-managed. Don't detach or delete them manually. To remove them, disable the egress option on the domain or delete the domain.

## Limits and considerations
<a name="vpc-egress-limits"></a>

Egress through your VPC is available in the Regions listed on the Amazon OpenSearch Service endpoints and quotas page. It's supported on Amazon OpenSearch Service domains that have VPC enabled.

## Usage and billing
<a name="vpc-egress-billing"></a>

To monitor the data transfer associated with egress through your VPC, review your [AWS Billing](https://console.aws.amazon.com/billing/home) dashboard for usage type `DataTransfer-Regional-Bytes`, operation `VPCConnectionUsage`, and product code `AmazonES`. For current rates, see [Amazon OpenSearch Service pricing](https://aws.amazon.com/opensearch-service/pricing/).