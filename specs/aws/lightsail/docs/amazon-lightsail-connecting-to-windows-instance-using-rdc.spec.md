---
id: "@specs/aws/lightsail/docs/amazon-lightsail-connecting-to-windows-instance-using-rdc"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Windows RDC client"
status: active
depends_on:
  - "@specs/aws/lightsail/meta"
---

# Windows RDC client

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lightsail/docs/amazon-lightsail-connecting-to-windows-instance-using-rdc
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Connect to a Lightsail Windows instance from Windows with Remote Desktop
<a name="amazon-lightsail-connecting-to-windows-instance-using-rdc"></a>

You can use the Remote Desktop Connection (RDC) client included with the Windows operating system to connect to your Windows instance in Amazon Lightsail. RDC requires that you use the administrator user name and password for the Windows instance, which could be the default password assigned to the instance when it’s created or your own password if you changed the default password.

This topic walks you through the steps to obtain your default administrator password from the Lightsail console, and configure RDC to connect to your Windows instance. You can also connect to your instance from within the Lightsail console using your browser. For more information, see [Connect to your Windows instance with the web-based RDP client](connect-to-your-windows-based-instance-using-amazon-lightsail.md).

## Get the default administrator password for your Windows instance
<a name="get-the-default-admin-password"></a>

Complete the following steps to get the default administrator password for your Windows instance, which is required to connect to the instance using RDC.

**Note**  
If you changed the default administrator password, then the password that is displayed in Lightsail console for your instance will not work. You’ll need to remember your password. You cannot connect to your instance using RDC without your administrator password.

1. Sign in to the [Lightsail console](https://lightsail.aws.amazon.com/).

1. Choose the Windows instance that you want to connect to.

1. In the **Connect** tab of the instance management page, choose **Show default password**.

1. Highlight the default password that is displayed, and copy it by pressing **Ctl\+C**or **Cmd\+C**. The password is now in your clipboard.

   Continue to the next section of this guide to configure RDC, and paste the password into the client.

## Configure RDC and connect to your Windows instance
<a name="configure-rdc-and-connect"></a>

Complete the following steps to configure RDC and connect to your Windows instance.

1. Open the Windows menu, and then search for `Remote Desktop Connection` or `RDC`.

1. Choose **Remote Desktop Connection** in the search results.  
![RDC in the start menu search results.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-rdc-in-start-menu.png)

1. In the **Computer** text box, enter your Windows instance’s public IP address.  
![RDC configuration.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-remote-desktop-connection-configuration.png)

   The public IP is displayed next to your instance in the Lightsail console, as shown in the following example:  
![Public IP address of an instance in the Lightsail console.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-public-ip-address.png)

1. Choose **Show Options** to view additional connection options.

1. In the **User Name** text box, enter `Administrator`, which is the default user name for all Windows instances in Lightsail.  
![RDC options.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-remote-desktop-connection-options.png)

1. Choose **Connect**.

1. In the prompt that appears, enter or paste the default administrator password that you copied from the Lightsail console earlier in this procedure, and then choose **OK**.  
![Credentials for RDC connection.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-rdc-credentials.png)

1. In the prompt that appears, choose **Yes** to connect to the Windows instance despite certificate errors.  
![RDC certificate confirmation.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-rdc-certificate-confirmation.png)

   After you’re connected to the instance, you should see a screen similar to the following example:  
![The desktop background for a Lightsail Windows instance in the Microsoft Remote Desktop application.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/connect-using-remote-desktop-mac-08.png)