---
id: "@specs/aws/lightsail/docs/create-powershell-script-that-runs-when-you-create-windows-based-instance-in-lightsail"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS PowerShell scripts"
status: active
depends_on:
  - "@specs/aws/lightsail/meta"
---

# PowerShell scripts

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lightsail/docs/create-powershell-script-that-runs-when-you-create-windows-based-instance-in-lightsail
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Configure Windows Lightsail instances with PowerShell and batch scripts
<a name="create-powershell-script-that-runs-when-you-create-windows-based-instance-in-lightsail"></a>

When you create a Windows-based instance, you can configure it using a Windows PowerShell script or any other batch script. This is a one-time script that runs right after your instance launches. This topic shows the syntax of the scripts and provides an example to get you started. We also show you how to test your script to see if it ran successfully.

## Create an instance that launches and runs a PowerShell script
<a name="windows-powershell-create-instance"></a>

The following procedure installs a tool called *chocolatey* on a new instance, right after the instance launches.

1. In the left navigation pane, choose **Create instance**.

1. Choose the AWS Region and Availability Zone where you want to create your instance.

1. Under **Select a platform**, choose **Microsoft Windows**.

1. Choose **OS Only**, and then choose **Windows Server 2022**, **Windows Server 2019**, **Windows Server 2016**.

1. Choose **Add launch script**.

1. Type the following:

   ```
   <powershell>
   iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
   </powershell>
   ```
**Note**  
You must always wrap your PowerShell scripts in `<powershell></powershell>` tags. You can enter non-PowerShell commands or batch scripts using `<script></script>` tags or without any tags at all.

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

## Verify that your script ran successfully
<a name="windows-powershell-verify-script-ran-successfully"></a>

You can log in to your instance to verify that the script ran successfully. It can take up to 15 minutes for a Windows-based instance to be ready to accept RDP connections. Once it's ready, log in using the browser-based RDP client or configure your own RDP client. For more information, see [Connect to your Windows-based instance](connect-to-your-windows-based-instance-using-amazon-lightsail.md).

1. Once you can connect to your Lightsail instance, open a command prompt (or open Windows Explorer).

1. Change to the `Log` directory by typing the following:

   ```
   cd C:\ProgramData\Amazon\EC2-Windows\Launch\Log
   ```

1. Open `UserdataExecution.log` in a text editor, or type the following: `type UserdataExecution.log`.

   You should see the following in your log file.

   ```
   2017/10/11 20:32:12Z: <powershell> tag was provided.. running powershell content
   2017/10/11 20:32:13Z: Message: The output from user scripts: iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
   
   2017/10/11 20:32:13Z: Userdata execution done
   ```