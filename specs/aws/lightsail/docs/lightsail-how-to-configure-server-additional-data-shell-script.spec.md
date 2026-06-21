---
id: "@specs/aws/lightsail/docs/lightsail-how-to-configure-server-additional-data-shell-script"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Linux shell scripts"
status: active
depends_on:
  - "@specs/aws/lightsail/meta"
---

# Linux shell scripts

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lightsail/docs/lightsail-how-to-configure-server-additional-data-shell-script
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Configure Linux/Unix instances with launch scripts in Lightsail
<a name="lightsail-how-to-configure-server-additional-data-shell-script"></a>

When you create a Linux or Unix-based instance, you can add a launch script to add or update software, or configure your instance in some other way. To configure a Windows-based instance with additional data, see [Configure your new Lightsail instance using Windows PowerShell](create-powershell-script-that-runs-when-you-create-windows-based-instance-in-lightsail.md).

**Note**  
Depending on the machine image you choose, the command to get software on your instance varies. Amazon Linux uses `yum`, while Debian and Ubuntu both use `apt-get`. WordPress and other application images use `apt-get` because they run Debian as their operating system. FreeBSD and openSUSE require additional user configuration to use custom tools such as `freebsd-update` or `zypper` (openSUSE).

## Example: Configure an Ubuntu server to install Node.js
<a name="example-configure-ubuntu-using-apt-get-install-node-js"></a>

The following example updates the package list and then installs Node.js through the `apt-get` command.

1. On the **Create an instance** page, choose **Ubuntu** on the **OS Only** tab.

1. Scroll down and choose **Add launch script**.

1. Type the following:

   ```
   # update package list
   apt-get update -y
   # install some of my favorite tools
   apt-get install nodejs -y
   ```
**Note**  
Commands you send to configure your server are run as root, so you don't need to include `sudo` before your commands.

1. Choose **Create instance**.

## Example: Configure a WordPress server to download and install a plugin
<a name="example-configure-wordpress-install-plugins"></a>

The following example updates the package list, and then downloads and installs the [BuddyPress plugin](https://wordpress.org/plugins/buddypress/) for WordPress.

1. On the **Create an instance** page, choose **WordPress**.

1. Choose **Add launch script**.

1. Type the following:

   ```
   # update package list
   apt-get update
   # download wordpress plugin
   wget "https://downloads.wordpress.org/plugin/buddypress.14.0.0.zip"
   apt-get install unzip
   # unzip into wordpress plugin directory
   unzip buddypress.14.0.0.zip -d /bitnami/wordpress/wp-content/plugins
   ```

1. Choose **Create instance**.