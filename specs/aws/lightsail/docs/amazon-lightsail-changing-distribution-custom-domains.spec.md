---
id: "@specs/aws/lightsail/docs/amazon-lightsail-changing-distribution-custom-domains"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Change custom domain"
status: active
depends_on:
  - "@specs/aws/lightsail/meta"
---

# Change custom domain

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lightsail/docs/amazon-lightsail-changing-distribution-custom-domains
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Update SSL/TLS certificate domains for your Lightsail distribution
<a name="amazon-lightsail-changing-distribution-custom-domains"></a>

You can change the custom domains used by your Amazon Lightsail distribution to another domain or set of domains. To do so, you must first create a new SSL/TLS certificate for the domains that you want to use with your distribution. For more information, see [Create SSL/TLS certificates for your distribution](amazon-lightsail-create-a-distribution-certificate.md). After the new certificate is validated, you swap the old certificate for the new one, thereby changing the custom domains for your distribution.

For more information about distributions, see [Create a distribution](amazon-lightsail-creating-content-delivery-network-distribution.md).

## Change custom domains for your distribution
<a name="changing-distribution-custom-domains"></a>

Complete the following procedure to change the custom domains for your distribution.

1. Sign in to the [Lightsail console](https://lightsail.aws.amazon.com/).

1. In the left navigation pane, choose **Networking**.

1. Choose the name of the distribution for which you want to change the custom domains.

1. Choose the **Custom domains** tab on your distribution's management page.

1. Detach the SSL/TLS certificate that is currently attached to the distribution.

   The status of the distribution will change to **In progress**.

1. After the distribution's status changes back to **Enabled**, choose **Attach certificate**.

1. In the dropdown menu that appears, select a valid certificate for the domain(s) that you want to use with your distribution.

1. Verify the certificate information is correct, then choose **Attach**.

1. Add a domain assignment to the DNS of your domain to point the domain to your distribution.

   The distribution's **Status** will change to **Updating**. After the status changes to **Ready**, the certificate's domain will appear in the **Custom domains** section. Choose **Add domain assignment** to point the domain to your distribution.

1. Choose **Add assignment**. After a few moments, traffic for the domain that you selected will begin to be accepted by your distribution.

1. Choose **Save**.