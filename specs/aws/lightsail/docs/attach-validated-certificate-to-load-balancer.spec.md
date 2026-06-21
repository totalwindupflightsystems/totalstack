---
id: "@specs/aws/lightsail/docs/attach-validated-certificate-to-load-balancer"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Attach certificate to load balancer"
status: active
depends_on:
  - "@specs/aws/lightsail/meta"
---

# Attach certificate to load balancer

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lightsail/docs/attach-validated-certificate-to-load-balancer
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Attach a validated SSL/TLS certificate to your Lightsail load balancer
<a name="attach-validated-certificate-to-load-balancer"></a>

After you verify that you control your domain, the certificate's status will change to **Valid**.

![Successful validation of domain](http://docs.aws.amazon.com/lightsail/latest/userguide/images/example-com-verified-and-ready-to-use.png)


Your next step is to attach the certificate to your Lightsail load balancer.

1. From the Lightsail home page, choose **Networking**.

1. Choose your load balancer.

1. Choose the **Custom domains** tab.

1. In the **Certificates** section, choose **Attach certificate**.

1. Select a certificate from the dropdown list.

1. Choose **Attach**, to attach the certificate.