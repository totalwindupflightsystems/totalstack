---
id: "@specs/aws/lightsail/docs/amazon-lightsail-viewing-container-services-certificates"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS View certificates"
status: active
depends_on:
  - "@specs/aws/lightsail/meta"
---

# View certificates

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lightsail/docs/amazon-lightsail-viewing-container-services-certificates
> **target_lang:** meta — documentation tier. ALL sections preserved.



# View SSL/TLS certificates for Lightsail container services
<a name="amazon-lightsail-viewing-container-services-certificates"></a>

You can view the Amazon Lightsail SSL/TLS certificates that you created for your Lightsail container service. You do this by accessing the management page of any container service in the Lightsail console.

For more information about SSL/TLS certificates, see [SSL/TLS certificates](understanding-tls-ssl-certificates-in-lightsail-https.md).

## Prerequisites
<a name="viewing-container-service-certificates-prerequisites"></a>

Before you get started, you need to create a Lightsail container service. For more information, see [Creating Amazon Lightsail container services](amazon-lightsail-creating-container-services.md) and [Container services](amazon-lightsail-container-services.md).

You also should have created an SSL/TLS certificate for your container service. For more information, see [Create container service SSL/TLS certificates](amazon-lightsail-creating-container-services-certificates.md).

## View your container service SSL/TLS certificates
<a name="view-container-service-certificates"></a>

Complete the following procedure to view your container service SSL/TLS certificates.

1. Sign in to the [Lightsail console](https://lightsail.aws.amazon.com/).

1. In the left navigation pane, choose **Containers**.

1. Choose the name of a container service.

   You can view all of your certificates regardless of the container service you choose.

1. Choose the **Custom domains** tab on your container service management page.

1. Scroll down to the **Attached certificates** section of the page.

   All of your certificates are listed under the **Attached certificates** section of the page. Choose **Details** to view your certificate's important dates, encryption details, identification, and domains. Choose **Validation details** to view your certificate's validation records. Your certificates are valid for 13 months from the date you created them, after which time Lightsail attempts to automatically revalidate them. Don't delete the CNAME records that you added to your domain because they are required when your certificate is re-validated on the **Valid until** date listed.

   After you have a valid SSL/TLS certificate to use with your container service, you should enable custom domains so that you can use the domain names of the certificate on your service. For more information, see [Enable and manage custom domains](amazon-lightsail-enabling-container-services-custom-domains.md).