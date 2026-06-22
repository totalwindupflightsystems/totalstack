---
id: "@specs/aws/appconfig/docs/appconfig-agent-how-to-use-additional-features-write-to-disk"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Configuring AWS AppConfig Agent to write configuration copies to disk"
status: active
depends_on:
  - "@specs/aws/appconfig/meta"
---

# Configuring AWS AppConfig Agent to write configuration copies to disk

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appconfig/docs/appconfig-agent-how-to-use-additional-features-write-to-disk
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Configuring AWS AppConfig Agent to write configuration copies to disk
<a name="appconfig-agent-how-to-use-additional-features-write-to-disk"></a>

You can configure AWS AppConfig Agent to automatically store a copy of a configuration to disk in plain text. This feature enables customers with applications that read configuration data from disk to integrate with AWS AppConfig.

This feature is not designed to be used as a configuration backup feature. AWS AppConfig Agent doesn't read from the configuration files copied to disk. If you want to back up configurations to disk, see the `BACKUP_DIRECTORY` and `PRELOAD_BACKUP` environment variables for [Using AWS AppConfig Agent with Amazon EC2](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-integration-ec2.html#appconfig-integration-ec2-configuring) or [Using AWS AppConfig Agent with Amazon ECS and Amazon EKS](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-integration-containers-agent.html#appconfig-integration-containers-agent-configuring).

**Warning**  
Note the following important information about this feature:  
Configurations saved to disk are stored in *plain text* and are human readable. Don't enable this feature for configurations that include sensitive data. 
This feature writes to the local disk. Use the principle of least privilege for filesystem permissions. For more information, see [Implement least privilege access](appconfig-security.md#appconfig-security-least-privilege-access).

**To enable write configuration copy to disk**

1. Edit the manifest.

1. Choose the configuration that you want AWS AppConfig to write to disk and add a `writeTo` element. Here is an example:

   ```
   {
       "{{application_name}}:{{environment_name}}:{{configuration_name}}": {
           "writeTo": {
               "path": "{{path_to_configuration_file}}"
           }
       }
   }
   ```

   Here is an example:

   ```
   {
       "MyTestApp:MyTestEnvironment:MyNewConfiguration": {
           "writeTo": {
               "path": "/tmp/aws-appconfig/mobile-app/beta/enable-mobile-payments"
           }
       }
   }
   ```

1. Save your changes. The configuration.json file will be updated each time new configuration data is deployed.

**Validate that write configuration copy to disk is working**  
You can validate that copies of a configuration are being written to disk by looking by reviewing the AWS AppConfig agent logs. The `INFO` log entry with the phrasing "INFO wrote configuration '{{application}}:{{environment}}:{{configuration}}' to {{file\_path}}" indicates that AWS AppConfig Agent writes configuration copies to disk.

Here is an example:

```
[appconfig agent] 2023/11/13 11:33:27 INFO AppConfig Agent 2.0.x
[appconfig agent] 2023/11/13 11:33:28 INFO serving on localhost:2772
[appconfig agent] 2023/11/13 11:33:28 INFO retrieved initial data for 'MobileApp:Beta:EnableMobilePayments' in XX.Xms
[appconfig agent] 2023/11/13 17:05:49 INFO wrote configuration 'MobileApp:Beta:EnableMobilePayments' to /tmp/configs/your-app/your-env/your-config.json
```