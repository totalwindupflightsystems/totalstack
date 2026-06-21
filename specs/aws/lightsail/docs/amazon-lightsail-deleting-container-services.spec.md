---
id: "@specs/aws/lightsail/docs/amazon-lightsail-deleting-container-services"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Delete a container"
status: active
depends_on:
  - "@specs/aws/lightsail/meta"
---

# Delete a container

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lightsail/docs/amazon-lightsail-deleting-container-services
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Delete a Lightsail container service
<a name="amazon-lightsail-deleting-container-services"></a>

You can delete your Amazon Lightsail container service at any time if you're no longer using it. When you delete your container service, all deployments and registered container images associated with that service are permanently destroyed. However, the SSL/TLS certificates and domains that you created remain in your Lightsail account so that you can use them with another resource. For more information about container services, see [Container services in Amazon Lightsail](amazon-lightsail-container-services.md).

## Delete a container service
<a name="deleting-container-service"></a>

Complete the following procedure to delete your container service.

1. Sign in to the [Lightsail console](https://lightsail.aws.amazon.com/).

1. In the left navigation pane, choose **Containers**.

1. Choose the name of the container service you want to delete.

1. Choose the ellipsis icon in the tab menu, then choose the **Delete**.  
![Delete tab for the container service in the Lightsail console](http://docs.aws.amazon.com/lightsail/latest/userguide/images/continer-service-delete-tab.png)

1. Choose **Delete container service** to delete your service.

1. In the prompt that appears, choose **Yes, delete** to confirm that the deletion is permanent.

   Your container service is deleted after a few moments.