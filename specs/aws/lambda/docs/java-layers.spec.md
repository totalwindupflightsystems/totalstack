---
id: "@specs/aws/lambda/docs/java-layers"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Layers"
status: active
depends_on:
  - "@specs/aws/lambda/meta"
---

# Layers

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lambda/docs/java-layers
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Working with layers for Java Lambda functions
<a name="java-layers"></a>

Use [Lambda layers](chapter-layers.md) to package code and dependencies that you want to reuse across multiple functions. Layers usually contain library dependencies, a [custom runtime](runtimes-custom.md), or configuration files. Creating a layer involves three general steps:

1. Package your layer content. This means creating a .zip file archive that contains the dependencies you want to use in your functions.

1. Create the layer in Lambda.

1. Add the layer to your functions.

**Topics**
+ [Package your layer content](#java-layers-package)
+ [Create the layer in Lambda](#publishing-layer)
+ [Add the layer to your function](#java-layer-adding)

## Package your layer content
<a name="java-layers-package"></a>

To create a layer, bundle your packages into a .zip file archive that meets the following requirements:
+ Ensure that the Java version that Maven or Gradle refers to is the same as the Java version of the function that you intend to deploy. For example, for a Java 25 function, the `mvn -v` command should list Java 25 in the output.
+ Your dependencies must be stored in the `java/lib` directory, at the root of the .zip file. For more information, see [Layer paths for each Lambda runtime](packaging-layers.md#packaging-layers-paths).
+ The packages in your layer must be compatible with Linux. Lambda functions run on Amazon Linux.

You can create layers that contain either third-party Java libraries or your own Java modules and packages. The following procedure uses Maven. You can also use Gradle to package your layer content.

**To create a layer using Maven dependencies**

1. Create an Apache Maven project with a `pom.xml` file that defines your dependencies.

   The following example includes [Jackson Databind](https://mvnrepository.com/artifact/com.fasterxml.jackson.core/jackson-databind) for JSON processing. The `<build>` section uses the [maven-dependency-plugin](https://mvnrepository.com/artifact/org.apache.maven.plugins/maven-dependency-plugin) to create separate JAR files for each dependency instead of bundling them into a single uber-jar. If you want to create an uber-jar, use the [maven-shade-plugin](https://maven.apache.org/plugins/maven-shade-plugin/).  
**Example pom.xml**  

   ```
   <dependencies>
       <dependency>
           <groupId>com.fasterxml.jackson.core</groupId>
           <artifactId>jackson-databind</artifactId>
           <version>2.17.0</version>
       </dependency>
   </dependencies>
   
   <build>
       <plugins>
           <plugin>
               <groupId>org.apache.maven.plugins</groupId>
               <artifactId>maven-compiler-plugin</artifactId>
               <version>3.13.0</version>
               <configuration>
                   <source>21</source>
                   <target>21</target>
                   <release>21</release>
               </configuration>
           </plugin>
           
           <plugin>
               <groupId>org.apache.maven.plugins</groupId>
               <artifactId>maven-dependency-plugin</artifactId>
               <version>3.6.1</version>
               <executions>
                   <execution>
                       <id>copy-dependencies</id>
                       <phase>package</phase>
                       <goals>
                           <goal>copy-dependencies</goal>
                       </goals>
                       <configuration>
                           <outputDirectory>${project.build.directory}/lib</outputDirectory>
                       </configuration>
                   </execution>
               </executions>
           </plugin>
       </plugins>
   </build>
   ```

1. Build the project. This command creates all dependency JAR files in the `target/lib/` directory.

   ```
   mvn clean package
   ```

1. Create the required directory structure for your layer:

   ```
   mkdir -p java/lib
   ```

1. Copy the dependency JAR files to the `java/lib` directory:

   ```
   cp target/lib/*.jar java/lib/
   ```

1. Zip the layer content:

------
#### [ Linux/macOS ]

   ```
   zip -r layer.zip java/
   ```

------
#### [ PowerShell ]

   ```
   Compress-Archive -Path .\java -DestinationPath .\layer.zip
   ```

------

   The directory structure of your .zip file should look like this:

   ```
   java/              
   └── lib/
       ├── jackson-databind-2.17.0.jar
       ├── jackson-core-2.17.0.jar
       └── jackson-annotations-2.17.0.jar
   ```
**Note**  
Make sure your .zip file includes the `java` directory at the root level with `lib` inside it. This structure ensures that Lambda can locate and import your libraries. Each dependency is kept as a separate JAR file rather than bundled into an uber-jar.

## Create the layer in Lambda
<a name="publishing-layer"></a>

You can publish your layer using either the AWS CLI or the Lambda console.

------
#### [ AWS CLI ]

Run the [publish-layer-version](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/publish-layer-version.html) AWS CLI command to create the Lambda layer:

```
aws lambda publish-layer-version --layer-name {{my-layer}} --zip-file fileb://layer.zip --compatible-runtimes {{java25}}
```

The [compatible runtimes](https://docs.aws.amazon.com/lambda/latest/api/API_PublishLayerVersion.html#lambda-PublishLayerVersion-request-CompatibleRuntimes) parameter is optional. When specified, Lambda uses this parameter to filter layers in the Lambda console.

------
#### [ Console ]

**To create a layer (console)**

1. Open the [Layers page](https://console.aws.amazon.com/lambda/home#/layers) of the Lambda console.

1. Choose **Create layer**.

1. Choose **Upload a .zip file**, and then upload the .zip archive that you created earlier.

1. (Optional) For **Compatible runtimes**, choose the Java runtime that corresponds to the Java version you used to build your layer.

1. Choose **Create**.

------

## Add the layer to your function
<a name="java-layer-adding"></a>

------
#### [ AWS CLI ]

To attach the layer to your function, run the [update-function-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/update-function-configuration.html) AWS CLI command. For the `--layers` parameter, use the layer ARN. The ARN must specify the version (for example, `arn:aws:lambda:us-east-1:123456789012:layer:my-layer:{{1}}`). For more information, see [Layers and layer versions](chapter-layers.md#lambda-layer-versions).

```
aws lambda update-function-configuration --function-name {{my-function}} --cli-binary-format raw-in-base64-out --layers "{{arn:aws:lambda:us-east-1:123456789012:layer:my-layer:{{1}}}}"
```

The **cli-binary-format** option is required if you're using AWS CLI version 2. To make this the default setting, run `aws configure set cli-binary-format raw-in-base64-out`. For more information, see [AWS CLI supported global command line options](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-options.html#cli-configure-options-list) in the *AWS Command Line Interface User Guide for Version 2*.

------
#### [ Console ]

**To add a layer to a function**

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions) of the Lambda console.

1. Choose the function.

1. Scroll down to the **Layers** section, and then choose **Add a layer**.

1. Under **Choose a layer**, select **Custom layers**, and then choose your layer.
**Note**  
If you didn't add a [compatible runtime](https://docs.aws.amazon.com/lambda/latest/api/API_PublishLayerVersion.html#lambda-PublishLayerVersion-request-CompatibleRuntimes) when you created the layer, your layer won't be listed here. You can specify the layer ARN instead.

1. Choose **Add**.

------