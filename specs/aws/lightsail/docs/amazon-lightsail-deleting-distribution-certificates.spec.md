---
id: "@specs/aws/lightsail/docs/amazon-lightsail-deleting-distribution-certificates"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Delete distribution certificates"
status: active
depends_on:
  - "@specs/aws/lightsail/meta"
---

# Delete distribution certificates

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lightsail/docs/amazon-lightsail-deleting-distribution-certificates
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Delete unused SSL/TLS certificates from Lightsail distributions
<a name="amazon-lightsail-deleting-distribution-certificates"></a>

**Warning**  
Deleting an SSL/TLS certificate is final and can't be undone.

You can delete Amazon Lightsail SSL/TLS certificates that you're no longer using on your distributions. For example, your certificate might be expired and you've already attached an updated certificate that's validated. For more information about certificates, see [SSL/TLS certificates](understanding-tls-ssl-certificates-in-lightsail-https.md). For more information about distributions, see [Content delivery network distributions](amazon-lightsail-content-delivery-network-distributions.md).

You have a quota of certificates that you can create over a 365-day period. For more information, see [Lightsail service quotas](https://docs.aws.amazon.com/general/latest/gr/lightsail.html#limits_lightsail) in the *AWS General Reference*.

## Delete an SSL/TLS certificate for your distribution
<a name="deleting-distribution-certificate"></a>

**Important**  
The **Delete** option is unavailable if the certificate you want to delete is in use. To delete certificates that are in use, you must first change the custom domains of the distribution that are using the certificate, or disable custom domains on the distribution that are using the certificate.

Complete the following procedure to delete an SSL/TLS certificate for your distribution.

1. Sign in to the [Lightsail console](https://lightsail.aws.amazon.com/).

1. In the left navigation pane, choose **Networking**.

1. Choose the name of the distribution from which you want to delete the SSL/TLS certificate. If the certificate is not currently in use, then you can choose any distribution because all of your certificates are listed in every distribution.

1. Choose the **Custom domains** tab on your distribution's management page.

1. In the **Certificates** section of the page, choose the ellipsis icon (⋮) for the certificate that you want to delete, and choose **Delete**.

   The **Delete** option is unavailable if the certificate you want to delete is in use. To delete certificates that are in use, you need to first change the custom domains of the distribution that is using the certificate, or disable custom domains on the distribution that is using the certificate. For more information, see [Change custom domains for your distribution](amazon-lightsail-changing-distribution-custom-domains.md) and [Enable custom domains for your distribution](amazon-lightsail-disabling-distribution-custom-domains.md#amazon-lightsail-disabling-distribution-custom-domains.title).

1. Choose **Yes, delete** to confirm the deletion.