---
id: "@specs/aws/kafka/docs/msk-connect-plugins"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Create custom plugins"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Create custom plugins

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/msk-connect-plugins
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Create custom plugins
<a name="msk-connect-plugins"></a>

A plugin is an AWS resource that contains the code that defines your connector logic. You upload a JAR file (or a ZIP file that contains one or more JAR files) to an S3 bucket, and specify the location of the bucket when you create the plugin. When the plugin is created, MSK Connect copies the contents of the S3 object at that point in time. It does not maintain a link to the S3 object, so any subsequent modifications to the object will not affect the plugin or its connectors. When you create a connector, you specify the plugin that you want MSK Connect to use for it. The relationship of plugins to connectors is one-to-many: you can create one or more connectors from the same plugin.

**Note**  
Custom plugins cannot be updated in place. To use a new version of your plugin code, delete all connectors that reference the plugin, delete the plugin, and then recreate it.

**Dependency packaging for custom plugins**  
We recommend that you include all required JAR files and dependencies for your plugin. Package your connector as one of the following:  
A ZIP file that contains all required JAR files and dependencies for the plugin.
A single uber JAR that contains all the class files for the plugin and its dependencies.
Not bundling your plugin dependencies may impact availability or compatibility in the runtime environment and cause unexpected errors.

The following table shows the Java runtime version used for each supported Apache Kafka Connect version. Ensure that your custom plugin is compatible with the Java runtime version for your selected Kafka Connect version.


**Java runtime versions for Apache Kafka Connect**  

| Apache Kafka Connect version | Java runtime | 
| --- | --- | 
| 2.7.1 | Java 11 | 
| 3.7.x | Java 17 | 

For information on how to develop the code for a connector, see the [Connector Development Guide](https://kafka.apache.org/documentation/#connect_development)in the Apache Kafka documentation.

**Creating a custom plugin using the AWS Management Console**

1. Open the Amazon MSK console at [https://console.aws.amazon.com/msk/](https://console.aws.amazon.com/msk/).

1. In the left pane, under **MSK Connect**, choose **Custom plugins**.

1. Choose **Create custom plugin**.

1. Choose **Browse S3**.

1. In the list of S3 buckets, choose the bucket that has the JAR or ZIP file for the plugin.

1. In the list of object, select the box to the left of the JAR or ZIP file for the plugin, then choose **Choose**.

1. Choose **Create custom plugin**.

To use the MSK Connect API to create a custom plugin, see [CreateCustomPlugin](https://docs.aws.amazon.com/MSKC/latest/mskc/API_CreateCustomPlugin.html).