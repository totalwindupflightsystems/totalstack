---
id: "@specs/aws/kafka/docs/msk-authentication-cluster"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Create a Amazon MSK cluster that supports client authentication"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Create a Amazon MSK cluster that supports client authentication

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/msk-authentication-cluster
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Create a Amazon MSK cluster that supports client authentication
<a name="msk-authentication-cluster"></a>

This procedure shows you how to enable client authentication using a AWS Private CA.
**Note**  
We highly recommend using independent AWS Private CA for each MSK cluster when you use mutual TLS to control access. Doing so will ensure that TLS certificates signed by PCAs only authenticate with a single MSK cluster.

1. Create a file named `clientauthinfo.json` with the following contents. Replace {{Private-CA-ARN}} with the ARN of your PCA.

   ```
   {
      "Tls": {
          "CertificateAuthorityArnList": ["{{Private-CA-ARN}}"]
       }
   }
   ```

1. Create a file named `brokernodegroupinfo.json` as described in [Create a provisioned Amazon MSK cluster using the AWS CLI](create-cluster-cli.md).

1. Client authentication requires that you also enable encryption in transit between clients and brokers. Create a file named `encryptioninfo.json` with the following contents. Replace {{KMS-Key-ARN}} with the ARN of your KMS key. You can set `ClientBroker` to `TLS` or `TLS_PLAINTEXT`.

   ```
   {
      "EncryptionAtRest": {
          "DataVolumeKMSKeyId": "{{KMS-Key-ARN}}"
       },
      "EncryptionInTransit": {
           "InCluster": true,
           "ClientBroker": "TLS"
       }
   }
   ```

   For more information about encryption, see [Amazon MSK encryption](msk-encryption.md).

1. On a machine where you have the AWS CLI installed, run the following command to create a cluster with authentication and in-transit encryption enabled. Save the cluster ARN provided in the response.

   ```
   aws kafka create-cluster --cluster-name "AuthenticationTest" --broker-node-group-info file://brokernodegroupinfo.json --encryption-info file://encryptioninfo.json --client-authentication file://clientauthinfo.json --kafka-version "{{{YOUR KAFKA VERSION}}}" --number-of-broker-nodes 3
   ```