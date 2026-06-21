---
id: "@specs/aws/lightsail/docs/create-lightsail-load-balancer-and-attach-lightsail-instances"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Create load balancer"
status: active
depends_on:
  - "@specs/aws/lightsail/meta"
---

# Create load balancer

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lightsail/docs/create-lightsail-load-balancer-and-attach-lightsail-instances
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Distribute web traffic with a Lightsail load balancer
<a name="create-lightsail-load-balancer-and-attach-lightsail-instances"></a>

Create a load balancer to add redundancy to your application or to handle more web traffic. After the load balancer is created, you can attach the Lightsail instances that you want to balance. To learn more, see [Load balancers](understanding-lightsail-load-balancers.md)

## Prerequisites
<a name="create-lightsail-load-balancer-prerequisite"></a>

Before you begin, make sure you've prepared your Lightsail instances for load balancing. For more information, see [Configure an instances for load balancing](configure-lightsail-instances-for-load-balancing.md).

## Create a load balancer
<a name="create-lightsail-load-balancer"></a>

1. Sign in to the [Lightsail console](https://lightsail.aws.amazon.com/).

1. Choose the **Networking** tab.

1. Choose **Create load balancer**.

1. Confirm the AWS Region where the load balancer will be created, or choose **Change region** to select a different region.
**Note**  
By default, the load balancer will be created with port 80 open to accept HTTP requests. After the load balancer is created, you can create an SSL/TLS certificate and configure HTTPS. For more information, see [Create an SSL/TLS certificate for your load balancer](create-tls-ssl-certificate-and-attach-to-lightsail-load-balancer-https.md)

1. Enter a name for your load balancer.

   Resource names:
   + Must be unique within each AWS Region in your Lightsail account.
   + Must contain 2 to 255 characters.
   + Must start and end with an alphanumeric character or number.
   + Can include alphanumeric characters, numbers, periods, dashes, and underscores.

1. Choose one of the following options to add tags to your load balancer:
   + **Add key-only tags** or **Manage tags** (if tags have already been added). Enter your new tag into the tag key text box, and press **Enter**. Choose **Save** when you’re done entering your tags to add them, or choose **Cancel** to not add them.  
![Key-only tags in the Lightsail console.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-key-only-tags.png)
   + **Create a key-value tag**, then enter a key into the **Key** text box, and a value into the **Value** text box. Choose **Save** when you’re done entering your tags, or choose **Cancel** to not add them.

     Key-value tags can only be added one at a time before saving. To add more than one key-value tag, repeat the previous steps.  
![Key-value tags in the Lightsail console.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-key-value-tag.png)
**Note**  
For more information about key-only and key-value tags, see [Tags](amazon-lightsail-tags.md).

1. Choose **Create load balancer**.

## Attach an instance to your load balancer
<a name="attach-lightsail-instances-to-load-balancer"></a>

After your load balancer is created, Lightsail takes you to the load balancer management page. If you need to find that page again, choose the **Networking** tab on the Lightsail home page, and then choose the name of your Lightsail load balancer to manage it.

**Note**  
Your Lightsail instance must be running before you can successfully attach it to your load balancer.

1. On the load balancer management page, choose **Target instances**.

1. Choose an instance in the **Target instances** drop-down menu.

1. Choose **Attach**. Attachment can take several minutes.

   Attach another instance to the load balancer by choosing **Attach another**, and then repeating the preceding steps.

## Next steps
<a name="create-load-balancer-attach-instances-next-steps"></a>

After the load balancer is created, and your instances are attached, complete the following next steps to configure your load balancer:
+ [Create an SSL/TLS certificate for your load balancer](create-tls-ssl-certificate-and-attach-to-lightsail-load-balancer-https.md)
+ [Customize health checks for your load balancer](enable-set-up-health-checking-for-lightsail-load-balancer-metrics.md)

If you experience issues with your load balancer, see [Troubleshoot your load balancer](troubleshooting-lightsail-load-balancer-issues.md)