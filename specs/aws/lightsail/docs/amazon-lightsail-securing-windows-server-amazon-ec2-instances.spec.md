---
id: "@specs/aws/lightsail/docs/amazon-lightsail-securing-windows-server-amazon-ec2-instances"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Secure Windows EC2 instances"
status: active
depends_on:
  - "@specs/aws/lightsail/meta"
---

# Secure Windows EC2 instances

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lightsail/docs/amazon-lightsail-securing-windows-server-amazon-ec2-instances
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Secure Windows Server Amazon EC2 instances launched from Lightsail snapshots
<a name="amazon-lightsail-securing-windows-server-amazon-ec2-instances"></a>

To improve the security of a Windows Server instance in Amazon Elastic Compute Cloud (Amazon EC2) created from an Amazon Lightsail snapshot, we recommend that you change the default administrator password. This removes the association between your Lightsail key pairs and your new Windows Server instance in Amazon EC2.

**Note**  
If you created Linux or Unix instances in Amazon EC2 from a Lightsail snapshot, then you should perform a few steps to secure those instances. For more information, see [Secure an Amazon EC2 Linux or Unix instance that was created from a Lightsail snapshot](amazon-lightsail-securing-linux-unix-amazon-ec2-instances.md).

**Contents**
+ [Connect to your Windows Server instance in Amazon EC2](#connect-to-your-windows-server-instance-in-ec2)
+ [Change the default administrator password of your Windows Server instance in Amazon EC2](#change-the-password-of-your-windows-server-instance-in-ec2)

## Connect to your Windows Server instance in Amazon EC2
<a name="connect-to-your-windows-server-instance-in-ec2"></a>

To change your Windows Server administrator password, connect to your Windows Service instance in Amazon EC2 using Remote Desktop Protocol (RDP). To learn how to connect to your instance, see [Connect to a Windows Server instance in Amazon EC2 created from a Lightsail snapshot](amazon-lightsail-connecting-to-windows-server-amazon-ec2-instances.md).

Continue to the [Change the default administrator password of your Windows Server instance in Amazon EC2](#change-the-password-of-your-windows-server-instance-in-ec2) section of this guide after you’re connected to your instance in Amazon EC2.

## Change the default administrator password of your Windows Server instance in Amazon EC2
<a name="change-the-password-of-your-windows-server-instance-in-ec2"></a>

Change the default password on your Windows Server instance to remove the association between your Lightsail key pairs and your new Windows Server instance in Amazon EC2.

**To change the default administrator password of your Windows Server instance in Amazon EC2**

1. After you establish an RDP connection to your instance, open a Command Prompt and enter the following command.

   ```
   net user Administrator "{{Password}}"
   ```

   In the command, replace {{Password}} with your new password.

   **Example:**

   ```
   net user Administrator "{{EXAMPLE%4=Bwk^GEAg8$u@5}}"
   ```

   You should see a result similar to the following:  
![Password reset on Windows Server in Amazon EC2.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-ec2-window-server-password-reset.png)

1. Store the new password in a safe place. You cannot retrieve the new password using the Amazon EC2 console. The console can retrieve only the default password. If you attempt to connect to the instance using the default password after changing it, an error message appears stating that your credentials did not work.

   If you lose your password or it expires, you can generate a new password. For password reset procedures, see [Resetting a Lost or Expired Windows Administrator Password](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/ResettingAdminPassword.html) in the Amazon EC2 documentation.