---
id: "@specs/aws/lightsail/docs/amazon-lightsail-testing-distribution"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Test distribution"
status: active
depends_on:
  - "@specs/aws/lightsail/meta"
---

# Test distribution

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lightsail/docs/amazon-lightsail-testing-distribution
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Validate your Lightsail distribution's content caching
<a name="amazon-lightsail-testing-distribution"></a>

In this guide, you will learn how to test that your Amazon Lightsail distribution is caching and serving content from your origin. You should perform this test after you add your registered domain name to your distribution. For more information about distributions, see [Content delivery network distributions](amazon-lightsail-content-delivery-network-distributions.md).

## Test your distribution
<a name="testing-distributions"></a>

Complete the following procedure to test your distribution. We use the Chrome web browser in this procedure; other browsers may use similar steps.

1. Open the Chrome web browser.

1. Open the **Chrome Menu** in the upper-right-hand corner of the browser window and select **More Tools** > **Developer Tools**.

   You can also use the shortcut Option \+ ⌘ \+ J (on macOS), or Shift \+ CTRL \+ J (on Windows/Linux).

1. In the developer tools pane, choose the **Network** tab.

1. Browse to the domain of your distribution (e.g., `https://www.example.com`).

   The **Network** tab of the Chrome developer tools should will populate with a list of objects from your website. 

1. Choose a static object, such as an image file (.jpg, .png, .gif).

1. In the **Header** panel that appears, you should see that the `via` and `x-cache` headers both mention CloudFront. This confirms that your distribution is caching and serving content from your origin. your   
![Distribution test result](http://docs.aws.amazon.com/lightsail/latest/userguide/images/distribution-test-result.png)