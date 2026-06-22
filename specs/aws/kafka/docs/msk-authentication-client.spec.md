---
id: "@specs/aws/kafka/docs/msk-authentication-client"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Set up a client to use authentication"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Set up a client to use authentication

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/msk-authentication-client
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Set up a client to use authentication
<a name="msk-authentication-client"></a>

This process describes how to set up an Amazon EC2 instance to use as a client to use authentication.

This process describes how to produce and consume messages using authentication by creating a client machine, creating a topic, and configuring the required security settings.

1. Create an Amazon EC2 instance to use as a client machine. For simplicity, create this instance in the same VPC you used for the cluster. See [Step 3: Create a client machine](create-client-machine.md) for an example of how to create such a client machine.

1. Create a topic. For an example, see the instructions under [Step 4: Create a topic in the Amazon MSK cluster](create-topic.md).

1. On a machine where you have the AWS CLI installed, run the following command to get the bootstrap brokers of the cluster. Replace {{Cluster-ARN}} with the ARN of your cluster.

   ```
   aws kafka get-bootstrap-brokers --cluster-arn {{Cluster-ARN}}
   ```

   Save the string associated with `BootstrapBrokerStringTls` in the response.

1. On your client machine, run the following command to use the JVM trust store to create your client trust store. If your JVM path is different, adjust the command accordingly.

   ```
   cp /usr/lib/jvm/java-1.8.0-openjdk-1.8.0.201.b09-0.amzn2.x86_64/jre/lib/security/cacerts kafka.client.truststore.jks
   ```

1. On your client machine, run the following command to create a private key for your client. Replace {{Distinguished-Name}}, {{Example-Alias}}, {{Your-Store-Pass}}, and {{Your-Key-Pass}} with strings of your choice.

   ```
   keytool -genkey -keystore kafka.client.keystore.jks -validity 300 -storepass {{Your-Store-Pass}} -keypass {{Your-Key-Pass}} -dname "CN={{Distinguished-Name}}" -alias {{Example-Alias}} -storetype pkcs12 -keyalg rsa
   ```

1. On your client machine, run the following command to create a certificate request with the private key you created in the previous step.

   ```
   keytool -keystore kafka.client.keystore.jks -certreq -file client-cert-sign-request -alias {{Example-Alias}} -storepass {{Your-Store-Pass}} -keypass {{Your-Key-Pass}}
   ```

1. Open the `client-cert-sign-request` file and ensure that it starts with `-----BEGIN CERTIFICATE REQUEST-----` and ends with `-----END CERTIFICATE REQUEST-----`. If it starts with `-----BEGIN NEW CERTIFICATE REQUEST-----`, delete the word `NEW` (and the single space that follows it) from the beginning and the end of the file.

1. On a machine where you have the AWS CLI installed, run the following command to sign your certificate request. Replace {{Private-CA-ARN}} with the ARN of your PCA. You can change the validity value if you want. Here we use 300 as an example.

   ```
   aws acm-pca issue-certificate --certificate-authority-arn {{Private-CA-ARN}} --csr fileb://client-cert-sign-request --signing-algorithm "SHA256WITHRSA" --validity Value=300,Type="DAYS"
   ```

   Save the certificate ARN provided in the response.
**Note**  
To retrieve your client certificate, use the `acm-pca get-certificate` command and specify your certificate ARN. For more information, see [get-certificate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/get-certificate.html) in the *AWS CLI Command Reference*.

1. Run the following command to get the certificate that AWS Private CA signed for you. Replace {{Certificate-ARN}} with the ARN you obtained from the response to the previous command.

   ```
   aws acm-pca get-certificate --certificate-authority-arn {{Private-CA-ARN}} --certificate-arn {{Certificate-ARN}}
   ```

1. From the JSON result of running the previous command, copy the strings associated with `Certificate` and `CertificateChain`. Paste these two strings in a new file named signed-certificate-from-acm. Paste the string associated with `Certificate` first, followed by the string associated with `CertificateChain`. Replace the `\n` characters with new lines. The following is the structure of the file after you paste the certificate and certificate chain in it.

   ```
   -----BEGIN CERTIFICATE-----
   ...
   -----END CERTIFICATE-----
   -----BEGIN CERTIFICATE-----
   ...
   -----END CERTIFICATE-----
   -----BEGIN CERTIFICATE-----
   ...
   -----END CERTIFICATE-----
   ```

1. Run the following command on the client machine to add this certificate to your keystore so you can present it when you talk to the MSK brokers.

   ```
   keytool -keystore kafka.client.keystore.jks -import -file signed-certificate-from-acm -alias {{Example-Alias}} -storepass {{Your-Store-Pass}} -keypass {{Your-Key-Pass}}
   ```

1. Create a file named `client.properties` with the following contents. Adjust the truststore and keystore locations to the paths where you saved `kafka.client.truststore.jks`. Substitute your Kafka client version for the {{{YOUR KAFKA VERSION}}} placeholders.

   ```
   security.protocol=SSL
   ssl.truststore.location=/tmp/kafka_2.12-{{{YOUR KAFKA VERSION}}}/kafka.client.truststore.jks
   ssl.keystore.location=/tmp/kafka_2.12-{{{YOUR KAFKA VERSION}}}/kafka.client.keystore.jks
   ssl.keystore.password={{Your-Store-Pass}}
   ssl.key.password={{Your-Key-Pass}}
   ```