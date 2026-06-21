---
id: "@specs/aws/lightsail/docs/amazon-lightsail-route-53-alias-record-for-container-service"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Point Route 53 domain to container"
status: active
depends_on:
  - "@specs/aws/lightsail/meta"
---

# Point Route 53 domain to container

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lightsail/docs/amazon-lightsail-route-53-alias-record-for-container-service
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Route domain traffic to a Lightsail container service using Route 53
<a name="amazon-lightsail-route-53-alias-record-for-container-service"></a>

You can route traffic for a registered domain, such as `example.com`, to the applications running on a Amazon Lightsail container service. You do this by adding an alias record to the hosted zone of your domain that points to the default domain of your Lightsail container service.

In this tutorial, we show you how to add an alias record for your Lightsail container service to a hosted zone in Route 53. You can do this only by using the AWS Command Line Interface (AWS CLI). It cannot be done using the Route 53 console.

**Note**  
If you're using Lightsail to host the DNS of your domain, then you should add the alias record to the DNS zone of your domain in Lightsail. For more information, see [Routing traffic for a domain in Amazon Lightsail to a Lightsail container service](amazon-lightsail-point-domain-to-container-service.md).

**Contents**
+ [Step 1: Complete the prerequisites](#route-53-container-service-prerequisites)
+ [Step 2: Get the hosted zone IDs for Lightsail container services](#route-53-container-service-hosted-zone-ids)
+ [Step 3: Create a record set JSON file](#route-53-container-service-create-record-set-json)
+ [Step 4: Add a record to the hosted zone of your domain in Route 53](#route-53-container-service-add-record-to-hosted-zone)

## Step 1: Complete the prerequisites
<a name="route-53-container-service-prerequisites"></a>

Complete the following prerequisites if you haven't already:
+ Register a domain name in Route 53, or make Route 53 the DNS service for your registered (existing) domain name. For more information, see [Registering domain names using Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/registrar.html) or [Making Amazon Route 53 the DNS service for an existing domain](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/MigratingDNS.html) in the *Amazon Route 53 Developer Guide*.
+ Deploy your applications to your Lightsail container service. For more information, see [Create and manage container service deployments](amazon-lightsail-container-services-deployments.md).
+ Enable your registered domain name on your Lightsail container service. For more information, see [Enable and manage custom domains](amazon-lightsail-enabling-container-services-custom-domains.md).
+ Configure the AWS CLI with your account. For more information, see [Configure the AWS CLI to work with Lightsail](lightsail-how-to-set-up-and-configure-aws-cli.md).

## Step 2: Get the hosted zone IDs for Lightsail container services
<a name="route-53-container-service-hosted-zone-ids"></a>

You must specify a hosted zone ID for your Lightsail container service when you add an alias record to a hosted zone in Route 53. For example, if your Lightsail container service is in the US West (Oregon) (us-west-2) AWS Region, then you must specify hosted zone ID `Z0959753D43BBB908BAV` when adding an alias record for your Lightsail container service to a hosted zone in Route 53.

Following are the hosted zone IDs for each AWS Region in which you can create a Lightsail container service.

**EU (London) (eu-west-2)**: Z0624918ZXDYQZLOXA66

**US East (N. Virginia) (us-east-1)**: Z06246771KYU0IRHI74W4

**Asia Pacific (Singapore) (ap-southeast-1)**: Z0625921354DRJH4EY9V0

**EU (Ireland) (eu-west-1)**: Z0624732FELAMMKW3Y21

**Asia Pacific (Tokyo) (ap-northeast-1)**: Z0626125UAU4JWQ9JSKN

**Asia Pacific (Seoul) (ap-northeast-2)**: Z06260262XZM84B2WPLHH

**Asia Pacific (Hong Kong) (ap-east-1)**: Z08783602ZZF1Q7DYQZ4Q

**Asia Pacific (Jakarta) (ap-southeast-3)**: Z03072883T5HFTY4T7CDL

**Asia Pacific (Malaysia) (ap-southeast-5)**: Z09430204C5DXNNO314Y

**Asia Pacific (Mumbai) (ap-south-1)**: Z10460781IQMISS0I0VVY

**Asia Pacific (Sydney) (ap-southeast-2)**: Z09597943PQQZATPFE96E

**Canada (Central) (ca-central-1)**: Z10450993RIRIJJUUMA5W

**Europe (Frankfurt) (eu-central-1)**: Z06137433FV04OY4EC6L0

**Europe (Stockholm) (eu-north-1)**: Z016970523TDG2TZMUXKK

**Europe (Paris) (eu-west-3)**: Z09594631DSW2QUR7CFGO

**Europe (Spain) (eu-south-2)**: Z09429752610EUUODCNMZ

**US East (Ohio) (us-east-2)**: Z10362273VJ548563IY84

**US West (Oregon) (us-west-2)**: Z0959753D43BBB908BAV

**South America (São Paulo) (sa-east-1)**: Z06385701RRVJGO1IDVWQ

## Step 3: Create a record set JSON file
<a name="route-53-container-service-create-record-set-json"></a>

When you add a DNS record to the hosted zone of your domain in Route 53 using the AWS CLI, you must specify a set of configuration parameters for the record. The easiest way to do this is by creating a JSON (.json) file that contains all of the parameters, and then referencing the JSON file in your AWS CLI request.

Complete the following procedure to create a JSON file with the record set parameters for the alias record:

1. Open a text editor, such as Notepad on Windows or Nano on Linux.

1. Copy and paste the following text into the text editor:

   ```
   {
     "Comment": "{{Comment}}",
     "Changes": [
       {
         "Action": "CREATE",
         "ResourceRecordSet": {
           "Name": "{{Domain}}.",
           "Type": "A",
           "AliasTarget": {
             "HostedZoneId": "{{LightsailContainerServiceHostedZoneID}}",
             "DNSName": " {{LightsailContainerServiceAddress}}.",
             "EvaluateTargetHealth": true
           }
         }
       }
     ]
   }
   ```

   In your file, replace the following example text with your own:
   + {{Comment}} with a personal note or comment about the record set.
   + {{Domain}} with the registered domain name that you want to use with your Lightsail container service (for example, `example.com` or `www.example.com`). To use the root of your domain with your Lightsail container service, you must specify an `@` symbol in the subdomain space of your domain (for example, `@.example.com`).
   + {{LightsailContainerServiceHostedZoneID}} with the hosted zone ID for the AWS Region in which you created your Lightsail container service. For more information, see [Step 2: Get the hosted zone IDs for Lightsail container services](#route-53-container-service-hosted-zone-ids) earlier in this guide.
   + {{LightsailContainerServiceAddress}} with the public domain name of your Lightsail container service. You can get this by signing in to the Lightsail console, browsing to your container service, and copying the **Public domain** listed in the header section of the container service management page (for example, `container-service-1.q8cexampleljs.us-west-2.cs.amazonlightsail.com`).

   Example:

   ```
   {
     "Comment": "{{Alias record for Lightsail container service}}",
     "Changes": [
       {
         "Action": "CREATE",
         "ResourceRecordSet": {
           "Name": "{{@.example.com}}.",
           "Type": "A",
           "AliasTarget": {
             "HostedZoneId": "{{Z0959753D43BBB908BAV}}",
             "DNSName": "{{container-service-1.q8cexampleljs.us-west-2.cs.amazonlightsail.com}}.",
             "EvaluateTargetHealth": true
           }
         }
       }
     ]
   }
   ```

1. Save the file to your local directory as `change-resource-record-sets.json`.

## Step 4: Add a record to the hosted zone of your domain in Route 53
<a name="route-53-container-service-add-record-to-hosted-zone"></a>

Complete the following procedure to add a record to the hosted zone of your domain in Route 53 using the AWS CLI. You do this by using the  `change-resource-record-sets` command. For more information, see [change-resource-record-sets](https://docs.aws.amazon.com/cli/latest/reference/route53/change-resource-record-sets.html) in the *AWS CLI Command Reference*.

**Note**  
You must install the AWS CLI and configure it for Lightsail and Route 53 before continuing with this procedure. For more information, see [Configure the AWS CLI to work with Lightsail](lightsail-how-to-set-up-and-configure-aws-cli.md).

1. Open a Command Prompt or Terminal window.

1. Enter the following command to add a record to the hosted zone of your domain in Route 53.

   ```
   aws route53 change-resource-record-sets --hosted-zone-id {{HostedZoneID}} --change-batch {{PathToJsonFile}}
   ```

   In the command, replace the following example text with your own:
   + {{HostedZoneID}} with the ID of the hosted zone for your registered domain in Route 53. Use the [list-hosted-zones](https://docs.aws.amazon.com/cli/latest/reference/route53/list-hosted-zones.html) command to get a list of IDs for the hosted zones in your Route 53 account.
   + {{PathToJsonFile}} with the local directory folder path on your computer of the .json file that contains the record parameters. For more information, see the [Step 3: Create a record set JSON file](#route-53-container-service-create-record-set-json) section earlier in this guide.

   Examples:

   On a Linux or Unix computer:

   ```
   aws route53 change-resource-record-sets --hosted-zone-id {{Z123456789ABCDEFGHIJ}} --change-batch {{home/user/awscli/route53/change-resource-record-sets.json}}
   ```

   On a Windows computer:

   ```
   aws route53 change-resource-record-sets --hosted-zone-id {{Z123456789ABCDEFGHIJ}} --change-batch {{file://C:\awscli\route53\change-resource-record-sets.json}}
   ```

   You should see a result similar to the following example:  
![Result of the change resource record sets request](http://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-route-53-record-set.png)

   Allow time for the change to propagate through the internet's DNS, which might take several hours. After that is completed, internet traffic for your registered domain in Route 53 should begin routing to your Lightsail container service.