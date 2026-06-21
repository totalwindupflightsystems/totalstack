---
id: "@specs/aws/lightsail/docs/amazon-lightsail-connecting-to-windows-instance-using-microsoft-remote-desktop"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS macOS RDC client"
status: active
depends_on:
  - "@specs/aws/lightsail/meta"
---

# macOS RDC client

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lightsail/docs/amazon-lightsail-connecting-to-windows-instance-using-microsoft-remote-desktop
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Connect to a Lightsail Windows instance from macOS with Remote Desktop
<a name="amazon-lightsail-connecting-to-windows-instance-using-microsoft-remote-desktop"></a>

You can use the Microsoft Remote Desktop client to connect to your Windows instance from your macOS computer. Microsoft Remote Desktop requires that you use the administrator user name and password for your Lightsail Windows instance. This can be the default password assigned to the instance when it is created, or your own password if you changed the default password.

This topic walks you through the steps to obtain your default administrator password from the Lightsail console, and configure Microsoft Remote Desktop to connect to your Windows instance. You can also connect to your instance from within the Lightsail console using your browser. For more information, see [Connect to your Windows instance with the Microsoft Remote Desktop client](connect-to-your-windows-based-instance-using-amazon-lightsail.md).

## Get the required connection information for your Windows instance
<a name="get-required-connection-information"></a>

You will need the public IP address, user name, and administrator password for your Windows instance to connect to it using the Microsoft Remote Desktop client.

Complete the following procedure to get the required information.

1. Sign in to the [Lightsail console](https://lightsail.aws.amazon.com/).

1. Choose the **Instances** section on the Lightsail home page.

1. Make note of the public IP address of the instance you want to connect to.

1. Choose the name of the instance you want to connect to.

1. Choose the **Connect** tab.

1. Choose **Show default password** to obtain the Windows administrator password for your instance.  
![The Show default password option in the Lightsail Instance Connect tab.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/connect-using-remote-desktop-mac-01.png)

   The prompt displays the default administrator password for your Windows instance.  
![The default administrator password.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-windows-default-admin-password.png)

1. Copy the administrator password. You will use it to sign in to your instance using the Microsoft Remote Desktop client later in this guide.

## Configure Microsoft Remote Desktop and connect to your instance
<a name="configure-remote-desktop-to-connect-to-instance"></a>

Complete the following procedure to install the Microsoft Remote Desktop client on your Mac, and configure it to connect to your instance.

1. Open the App Store on your Mac, and search for **Microsoft Remote Desktop**.

1. Find the **Microsoft Remote Desktop** app in the search results, and choose **GET** to install the application.  
![The Microsoft Remote Desktop application.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/connect-using-remote-desktop-mac-03.png)

1. Open **Microsoft Remote Desktop** after the installation is complete.

1. At the top, choose the **plus (\+)** icon, and choose **Add PC**.  
![The Add PC option in the Microsoft Remote Desktop application.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/connect-using-remote-desktop-mac-04.png)

1. In the **PC name** text box, paste the public IP address of your instance.

1. Choose **Add**.  
![The Add button.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/connect-using-remote-desktop-mac-05.png)

1. Right-click the icon for your instance, and choose **Connect**.  
![The Connect option in the Microsoft Remote Desktop application.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/connect-using-remote-desktop-mac-06.png)

1. Enter **Administrator** into the **Username** text box, and enter the default administrator password that you got earlier in this guide into the **Password** text box.

1. Choose **Continue** to connect to your instance.  
![The Continue button.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/connect-using-remote-desktop-mac-07.png)

You are now connected to your Lightsail Windows instance.

![The desktop background for a Lightsail Windows instance in the Microsoft Remote Desktop application.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/connect-using-remote-desktop-mac-08.png)
