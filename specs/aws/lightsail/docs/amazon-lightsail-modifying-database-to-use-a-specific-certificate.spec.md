---
id: "@specs/aws/lightsail/docs/amazon-lightsail-modifying-database-to-use-a-specific-certificate"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Update CA certificate"
status: active
depends_on:
  - "@specs/aws/lightsail/meta"
---

# Update CA certificate

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lightsail/docs/amazon-lightsail-modifying-database-to-use-a-specific-certificate
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Update the CA certificate version for your Lightsail database
<a name="amazon-lightsail-modifying-database-to-use-a-specific-certificate"></a>

Amazon Lightsail has published new Certificate Authority (CA) certificates for connecting to your managed database using SSL/TLS. This guide describes how to upgrade to the new CA certificate. You can upgrade the certificate only by using the [https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_UpdateRelationalDatabase.html](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_UpdateRelationalDatabase.html) API action. The new certificates are referred to as `rds-ca-rsa2048-g1`, `rds-ca-rsa4096-g1`, and `rds-ca-ecc384-g1`. The old certificate is referred to as `rds-ca-2019`. We provide the CA certificates as an AWS security best practice. For information about the CA certificates for your managed database, and the supported AWS Regions, see [Downloading an SSL certificate for your managed database](amazon-lightsail-download-ssl-certificate-for-managed-database.md).

The old CA certificate (`rds-ca-2019`) expires on August 22, 2024. Therefore, we strongly recommend completing the steps in this guide as soon as possible to modify your managed database to use the new certificate. If your applications do not connect to your Lightsail managed database using SSL/TLS, no action is required. If these steps are not completed, your applications will fail to connect to your managed database using SSL/TLS after August 22, 2024.

New managed databases created after January 26, 2024 will use the `rds-ca-rsa2048-g1` certificate by default. If you want to temporarily modify new managed databases to use the old certificate (`rds-ca-2019`), you can do so using the AWS Command Line Interface (AWS CLI). Any managed databases created prior to January 26, 2024 uses the `rds-ca-2019` certificate until you update them to the `rds-ca-rsa2048-g1`, `rds-ca-rsa4096-g1`, and `rds-ca-ecc384-g1` certificates.



**Note**  
Test the steps in this guide on a development or staging environment before using them on your production environments.

## Prerequisites
<a name="modifying-database-prerequisites"></a>
+ Update your database client applications to use the new SSL/TLS certificate before completing the steps in this procedure.

  The methods for updating applications for new SSL/TLS certificates depend on your specific applications. Work with your application developers to update the SSL/TLS certificates for your applications. To learn more about updating applications for new SSL/TLS certificates, see [Updating Applications to Connect to MySQL DB Instances Using New SSL/TLS Certificates](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/ssl-certificate-rotation-mysql.html) or [Updating Applications to Connect to PostgreSQL DB Instances Using New SSL/TLS Certificates](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/ssl-certificate-rotation-postgresql.html) in the *Amazon Relational Database Service User Guide*.
+ In this guide, you will use AWS CloudShell to perform the upgrade. CloudShell is a browser-based, pre-authenticated shell that you can launch directly from the Lightsail console. With CloudShell, you can run AWS Command Line Interface (AWS CLI) commands using your preferred shell, such as Bash, PowerShell, or Z shell. You can do this without downloading or installing command line tools. For more information about how to set up and use CloudShell, see [AWS CloudShell in Lightsail](amazon-lightsail-cloudshell.md).

## Identify the active CA certificate for your managed database
<a name="checking-database-certificate-version"></a>

Complete the following steps to identify the active CA certificate for your Lightsail database instance.

1. Open a Terminal, [AWS CloudShell](amazon-lightsail-cloudshell.md), or Command Prompt window.

1. Enter the following command to identify the active CA certificate for your managed database.

   ```
   aws lightsail get-relational-database --relational-database-name {{DatabaseName}} --region {{DatabaseRegion}} | grep "caCertificateIdentifier"
   ```

   In the command, replace {{DatabaseName}} with the name of the database you want to modify, and {{DatabaseRegion}} with the AWS Region that the database instance is in.

   **Example**

   ```
   aws lightsail get-relational-database --relational-database-name {{Database-1}} --region {{us-east-1}} | grep "caCertificateIdentifier"
   ```

   The command will return the ID of the active CA certificate for your database.

   **Example**

   ```
   "caCertificateIdentifier": "rds-ca-rsa2048-g1"
   ```

## Modify your managed database to use the new CA certificate
<a name="modifying-database-new-certificate"></a>

Complete the following steps to modify your managed database in Lightsail to use one of the new CA certificates (`rds-ca-rsa2048-g1`, `rds-ca-rsa4096-g1`, and `rds-ca-ecc384-g1`).

**Important**  
Update any client applications that use the CA certificate before you update the CA certificate on your database.

1. Open a Terminal, [AWS CloudShell](amazon-lightsail-cloudshell.md), or Command Prompt window.

1. Enter the following command to use the new certificate on your managed database.

   ```
   aws lightsail update-relational-database --relational-database-name {{DatabaseName}} --region {{DatabaseRegion}} --ca-certificate-identifier rds-ca-rsa2048-g1
   ```

   In the command, replace {{DatabaseName}} with the name of the database you want to modify, and {{DatabaseRegion}} with the AWS Region that the database instance is in.

   **Example**

   ```
   aws lightsail update-relational-database --relational-database-name {{Database-1}} --region {{us-east-1}} --ca-certificate-identifier rds-ca-rsa2048-g1
   ```

   The CA certificate used by your managed database will be updated during your database’s next maintenance window, or immediately if you add the `--apply-immediately` parameter to the end of the command.

## Modify your managed database to use the old CA certificate
<a name="modifying-database-old-certificate"></a>

Complete the following steps to modify your managed database in Lightsail to use the old CA certificate (`rds-ca-2019`). Do this only if you experience a critical issue with one of the new certificates (`rds-ca-rsa2048-g1`, `rds-ca-rsa4096-g1`, and `rds-ca-ecc384-g1`) and need to temporarily revert the old one.

**Important**  
Update any client applications that use the CA certificate before you update the CA certificate on your database.

1. Open a Terminal, [AWS CloudShell](amazon-lightsail-cloudshell.md), or Command Prompt window.

1. Enter the following command to use the `rds-ca-2019` on your managed database.

   ```
   aws lightsail update-relational-database --relational-database-name {{DatabaseName}} --region {{DatabaseRegion}} --ca-certificate-identifier rds-ca-2019
   ```

   In the command, replace {{DatabaseName}} with the name of the database you want to modify, and {{DatabaseRegion}} with the AWS Region that the database instance is in.

   **Example**

   ```
   aws lightsail update-relational-database --relational-database-name {{Database-1}} --region {{us-east-1}} --ca-certificate-identifier rds-ca-2019
   ```

   The CA certificate used by your managed database will be updated during your database’s next maintenance window, or immediately if you add the `--apply-immediately` parameter to the end of the command.