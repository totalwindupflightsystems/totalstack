---
id: "@specs/aws/lightsail/docs/get-started-with-windows-based-instances-in-lightsail"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Windows instances"
status: active
depends_on:
  - "@specs/aws/lightsail/meta"
---

# Windows instances

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lightsail/docs/get-started-with-windows-based-instances-in-lightsail
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Create Windows Server instances in Lightsail
<a name="get-started-with-windows-based-instances-in-lightsail"></a>

**Did you know?**  
 Lightsail stores seven daily snapshots and automatically replaces the oldest with the newest when you enable automatic snapshots for your instance. For more information, see [ Configure automatic snapshots for Lightsail instances and disks ](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-configuring-automatic-snapshots.html) . 

Create Lightsail instances that run the Windows Server operating system (OS). We have three OS blueprints available: Windows Server 2022, Windows Server 2019, and Windows Server 2016. In addition, we have blueprints that come preconfigured with SQL Server 2022, 2019, and 2016 Express.

This topic provides information about choosing your software, creating your Windows Server-based instance, and connecting to it.

Learn more about [Windows Server on AWS](https://aws.amazon.com/windows/)

## Choose a Windows Server-based instance
<a name="choose-windows-based-instance-lightsail"></a>

There are three options for creating a Windows Server-based instance in Lightsail.

**Windows Server 2022**  
Lightsail running Windows Server is a fast and dependable environment for deploying applications using the Microsoft Web Platform. With Lightsail, you can run any compatible Windows-based solution on the high-performance, reliable, cost-effective AWS Cloud computing platform. Common Windows use cases include Enterprise Windows-based application hosting, website and web service hosting, data processing, distributed testing, ASP.NET application hosting, and any other application requiring Windows software.  
 [Learn more about the Windows Server 2022 image](https://aws.amazon.com/marketplace/pp/prodview-dq4sxno5vuy7m) 

 **Windows Server 2019**   
Unless you need to run Windows Server 2016 or Windows Server 2019 for some reason, we recommend using the latest version of Windows Server 2022.  
Lightsail running Windows Server is a fast and dependable environment for deploying applications using the Microsoft Web Platform. Lightsail enables you to run any compatible Windows-based solution on AWS' high-performance, reliable, cost-effective, cloud computing platform. Common Windows use cases include Enterprise Windows-based application hosting, website and web-service hosting, data processing, distributed testing, ASP.NET application hosting, and any other application requiring Windows software.  
 [Learn more about the Windows Server 2019 image](https://aws.amazon.com/marketplace/pp/B07QZ4XZ8F) 

 **Windows Server 2016**   
Unless you need to run Windows Server 2016 or Windows Server 2019 for some reason, we recommend using the latest version of Windows Server 2022.  
Lightsail running Windows Server is a fast and dependable environment for deploying applications using the Microsoft Web Platform. Lightsail enables you to run any compatible Windows-based solution on AWS' high-performance, reliable, cost-effective, cloud computing platform. Common Windows use cases include Enterprise Windows-based application hosting, website and web-service hosting, data processing, distributed testing, ASP.NET application hosting, and any other application requiring Windows software.  
 [Learn more about the Windows Server 2016 image](https://aws.amazon.com/marketplace/pp/B01M7SJEU7) 

 **SQL Server Express 2022**   
SQL Server Express is a relational database management system that is free to download, distribute, and use. It comprises a database specifically targeted for embedded and smaller-scale applications. This Lightsail image runs on a base OS of Windows Server 2022.  
 [Learn more about the SQL Server Express 2022 image](https://aws.amazon.com/marketplace/pp/prodview-c2jz4lr4h2yc6) 

 **SQL Server Express 2019**   
SQL Server Express is a relational database management system that is free to download, distribute, and use. It comprises a database specifically targeted for embedded and smaller-scale applications. This Lightsail image runs on a base OS of Windows Server 2022.  
 [Learn more about the SQL Server Express 2019 image](https://aws.amazon.com/marketplace/pp/prodview-xbikutlmywslu) 

 **SQL Server Express 2016**   
SQL Server Express is a relational database management system that is free to download, distribute, and use. It comprises a database specifically targeted for embedded and smaller-scale applications. This Lightsail image runs on a base OS of Windows Server 2016.  
 [Learn more about the SQL Server Express image](https://aws.amazon.com/marketplace/pp/B01MAZHH98) 

## Create a Windows Server-based instance
<a name="create-windows-based-instance-lightsail"></a>

You can create a Windows Server-based instance using the Lightsail console or by using the AWS Command Line Interface (AWS CLI).

**To create an instance using the console**

1. Sign in to Lightsail, and then go to the home page.

1. Choose **Create instance**.

1. Select an AWS Region where you want to create your Windows Server-based Lightsail instance.

   For example, `Ohio (us-east-2)`.

1. Select the **Microsoft Windows** platform.

1. To choose the Windows Server 2022, Windows Server 2019, Windows Server 2016 blueprint, choose **OS Only**.

   To choose the SQL Server Express blueprint, choose **Apps \+ OS**.

1. Choose your instance plan.

   Choose whether your instance uses dual-stack (IPv4 and IPv6), or IPv6-only networking. Some Lightsail blueprints don't support IPv6-only networking at this time. To see which blueprints support IPv6-only networking see [Review the Lightsail instance blueprint offerings](compare-options-choose-lightsail-instance-image.md).

   A plan also includes a low, predictable cost and a machine configuration (RAM, SSD, vCPU), as well as data transfer.
**Note**  
Some instance plans aren't available for some blueprints. For example, the SQL Server Express blueprint requires that you use a plan with at least 4 GB of memory and 80 GB of SSD storage.

1. Enter a name for your instance.

   Resource names:
   + Must be unique within each AWS Region in your Lightsail account.
   + Must contain 2 to 255 characters.
   + Must start and end with an alphanumeric character or number.
   + Can include alphanumeric characters, numbers, periods, dashes, and underscores.

1. (Optional) Choose **Add new tag** to add a tag to your instance. Repeat this step as needed to add additional tags. For more information on tag usage, see [Tags](amazon-lightsail-tags.md).

   1. For **Key**, enter a tag key.  
![A tag with only the tag key specified in the Lightsail create instance workflow.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-instance-key-name-only-tags.png)

   1. (Optional) For **Value**, enter a tag value.  
![A tag with the tag key and tag value specified in the Lightsail create instance workflow.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-instance-key-name-and-value-tags.png)

1. Choose **Create instance**.

**To create an instance using the AWS CLI**

1. If you haven't done so already, install and configure the AWS CLI.

   For more information, see [Configure the AWS Command Line Interface to work with Amazon Lightsail](lightsail-how-to-set-up-and-configure-aws-cli.md).

1. Open a command prompt or a terminal window.

1. If you haven't done so already, configure the AWS CLI using `aws configure` and select the AWS Region where you want to create your Lightsail resources.

1. Type the following AWS CLI command to create a $44 USD per month Windows Server 2022 instance running in the Ohio region:

   ```
   aws lightsail create-instances --instance-names {{InstanceName}} --availability-zone us-east-2a --blueprint-id windows_server_2022 --bundle-id medium_win_3_0
   ```

   In the command, replace {{InstanceName}} with the name of your new instance.

   If successful, you will see the following output from the AWS CLI.

   ```
   {
       "operations": [
           {
               "status": "Started",
               "resourceType": "Instance",
               "isTerminal": false,
               "statusChangedAt": 1508086226.4,
               "location": {
                   "availabilityZone": "us-east-2a",
                   "regionName": "us-east-2"
               },
               "operationType": "CreateInstance",
               "resourceName": "my-windows-instance",
               "id": "344acdc8-f9c4-4eda-8232-12345EXAMPLE",
               "createdAt": 1508086225.467
           }
       ]
   }
   ```
**Note**  
To get a list of available blueprints, use the [get-blueprints](http://docs.aws.amazon.com/cli/latest/reference/lightsail/get-blueprints.html) command. To get a list of available bundles, use the [get-bundles](http://docs.aws.amazon.com/cli/latest/reference/lightsail/get-bundles.html) command. Learn more about getting the password for your instance using the [get-instance-access-details](http://docs.aws.amazon.com/cli/latest/reference/lightsail/get-instance-access-details.html) command.

## Connect to your instance
<a name="connect-to-windows-based-instance-lightsail"></a>

Once you create your Windows Server-based Lightsail instance, you can connect to it using either the browser-based RDP client or the remote desktop client of your choice.

**Note**  
After you create your instance, you may need to wait up to 15 minutes before you can connect to it.

**To connect using the Lightsail browser-based RDP client**

1. On the home page, choose the **Connect using RDP** icon next to your instance.  
![Lightsail connect.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/connect-to-windows-instance-using-rdp-connection-shortcut.png)

1. Alternately, you can connect to your instance from the shortcut menu or the instance management page.

**To connect using your own RDP client**

1. To get your IP address, go to the Lightsail home page.

1. Copy the IP address to the clipboard.

1. Open an RDP client such as **Remote Desktop Connection** in Windows.

1. Paste the IP address into the **Computer** field.

1. Choose **Show Options**, and then type `Administrator` for your **User name**.  
![Remote Desktop Connection application.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/remote-desktop-connection-windows-server-based-instance-lightsail.png)

1. Choose **Connect**.

1. To get your password, go to the instance management page in Lightsail.

   You can get to the instance management page by choosing the name of your instance (or choosing **Manage** from the shortcut menu) on the Lightsail home page.

1. Choose **Show default password**.

1. Copy the default password to the clipboard.

1. Paste your password into **Remote Desktop Connection**, and then choose **Remember me** to prevent this dialog box from appearing in the future.  
![Remote Desktop Connection settings.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/remote-desktop-connection-enter-credentials-lightsail-windows.png)

1. Choose **OK**.

1. Choose **Don't ask me again for connections to this computer**, and then choose **Yes**.

## Next steps
<a name="windows-next-steps"></a>

Now that you can connect to your instance, what you do next depends on how you plan to use it. For example:
+ [Create a static IP address](lightsail-create-static-ip.md) for your instance to keep the same IP address each time you restart your Lightsail instance.
+ [Create a snapshot of your Lightsail Windows Server instance](prepare-windows-based-instance-and-create-snapshot.md).