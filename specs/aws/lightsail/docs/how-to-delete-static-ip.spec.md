---
id: "@specs/aws/lightsail/docs/how-to-delete-static-ip"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Delete a static IP address"
status: active
depends_on:
  - "@specs/aws/lightsail/meta"
---

# Delete a static IP address

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lightsail/docs/how-to-delete-static-ip
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Delete a static IP address in Lightsail
<a name="how-to-delete-static-ip"></a>

You can create up to five static IPs per AWS Region in your Amazon Lightsail account. If you delete an instance that has a static IP address attached to it, the static IP address remains in your account. If you no longer need the static IP address, you can delete it using the Lightsail console or the AWS Command Line Interface (AWS CLI). In this guide, we show you how to delete a static IP address from your Lightsail account. For more information about static IPs, see [IP addresses](understanding-public-ip-and-private-ip-addresses-in-amazon-lightsail.md).

**Important**  
Deleting a static IP will completely remove the static IP from your Lightsail account. Resources that use that static IP, such as instances, will be impacted. You will not be able to get the static IP back after you delete it.

## Delete a static IP using the Lightsail console
<a name="delete-static-ip-from-home-page-of-console"></a>

Complete the following procedure to delete a static IP using the Lightsail console.

1. Sign in to the [Lightsail console](https://lightsail.aws.amazon.com/).

1. In the left navigation pane, choose **Networking**.

1. On the **Networking** page choose the vertical ellipsis (⋮) icon next to the static IP address that you want to delete, and then choose **Delete**.  
![Delete a static IP in the Networking page](http://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-delete-static-ip-from-manage-static-ip-menu.png)

## Delete a static IP using the AWS CLI
<a name="delete-static-ip-using-aws-cli"></a>

Complete the following procedure to delete a static IP using the AWS CLI. The command to delete a static IP from your Lightsail account is [release-static-ip](https://docs.aws.amazon.com/cli/latest/reference/lightsail/release-static-ip.html). When you create a static IP, you're actually *allocating* it. So, instead of deleting the static IP, you're actually *releasing* it.

 **Prerequisites** 

First, if you haven't already, you need to install the AWS CLI. To learn more, see [Installing the AWS Command Line Interface](http://docs.aws.amazon.com/cli/latest/userguide/installing.html). Be sure [you configure the AWS CLI](lightsail-how-to-set-up-and-configure-aws-cli.md).

You will need the name of your static IP to release it. You can get that by using the `get-static-ips` AWS CLI command.

1. Type the following command:

   ```
   aws lightsail get-static-ips
   ```

   You should see output similar to the following.

   ```
   {
       "staticIps": [
           {
               "name": "Example-StaticIP",
               "resourceType": "StaticIp",
               "attachedTo": "MyInstance",
               "arn": "arn:aws:lightsail:us-east-2:123456789101:StaticIp/5282f35e-c720-4e5a-1234-12345EXAMPLE",
               "isAttached": true,
               "ipAddress": "192.0.2.0",
               "createdAt": 1489750629.026,
               "location": {
                   "availabilityZone": "all",
                   "regionName": "us-east-2"
               }
           },
           {
               "name": "my-other-static-ip",
               "resourceType": "StaticIp",
               "arn": "arn:aws:lightsail:us-east-2:123456789101:StaticIp/f5885e14-8984-49e5-1234-12345EXAMPLE",
               "isAttached": false,
               "ipAddress": "192.0.2.2",
               "createdAt": 1483653597.815,
               "location": {
                   "availabilityZone": "all",
                   "regionName": "us-east-2"
               }
           }
       ]
   }
   ```

1. Select the **name** value of the static IP you wish to release and make a note of it so you can use it in the next step.

   For example, you can copy the value to the clipboard.

1. Type the following command.

   ```
   aws lightsail release-static-ip --static-ip-name {{StaticIpName}}
   ```

   In the command, replace {{StaticIpName}} with the name of your static IP.

   If successful, you should see output similar to the following.

   ```
   {
       "operations": [
           {
               "status": "Succeeded",
               "resourceType": "StaticIp",
               "isTerminal": true,
               "statusChangedAt": 1489860944.19,
               "location": {
                   "availabilityZone": "all",
                   "regionName": "us-east-2"
               },
               "operationType": "ReleaseStaticIp",
               "resourceName": "Example-StaticIP",
               "id": "92a2f0d2-eef2-4e6f-1234-12345EXAMPLE",
               "createdAt": 1489860944.19
           }
       ]
   }
   ```