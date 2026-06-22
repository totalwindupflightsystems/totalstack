---
id: "@specs/aws/kafka/docs/update-security-cli"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Update cluster security settings using CLI"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Update cluster security settings using CLI

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/update-security-cli
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Updating Amazon MSK cluster security settings using the AWS CLI
<a name="update-security-cli"></a>

1. Create a JSON file that contains the encryption settings that you want the cluster to have. The following is an example. 
**Note**  
You can only update the client-broker encryption setting. You can't update the in-cluster (broker-to-broker) encryption setting.

   ```
   {"EncryptionInTransit":{"ClientBroker": "TLS"}}
   ```

1. Create a JSON file that contains the authentication settings that you want the cluster to have. The following is an example.

   ```
   {"Sasl":{"Scram":{"Enabled":true}}}
   ```

1. Run the following AWS CLI command:

   ```
   aws kafka update-security --cluster-arn {{ClusterArn}} --current-version {{Current-Cluster-Version}} --client-authentication file://{{Path-to-Authentication-Settings-JSON-File}} --encryption-info file://{{Path-to-Encryption-Settings-JSON-File}}
   ```

   The output of this `update-security` operation looks like the following JSON.

   ```
   {
       
       "ClusterArn": "arn:aws:kafka:us-east-1:012345678012:cluster/exampleClusterName/abcdefab-1234-abcd-5678-cdef0123ab01-2",
       "ClusterOperationArn": "arn:aws:kafka:us-east-1:012345678012:cluster-operation/exampleClusterName/abcdefab-1234-abcd-5678-cdef0123ab01-2/0123abcd-abcd-4f7f-1234-9876543210ef"
   }
   ```

1. To see the status of the `update-security` operation, run the following command, replacing {{ClusterOperationArn}} with the ARN that you obtained in the output of the `update-security` command.

   ```
   aws kafka describe-cluster-operation --cluster-operation-arn {{ClusterOperationArn}}
   ```

   The output of this `describe-cluster-operation` command looks like the following JSON example.

   ```
   {
       "ClusterOperationInfo": {
           "ClientRequestId": "c0b7af47-8591-45b5-9c0c-909a1a2c99ea",
           "ClusterArn": "arn:aws:kafka:us-east-1:012345678012:cluster/exampleClusterName/abcdefab-1234-abcd-5678-cdef0123ab01-2",
           "CreationTime": "2021-09-17T02:35:47.753000+00:00",
           "OperationArn": "arn:aws:kafka:us-east-1:012345678012:cluster-operation/exampleClusterName/abcdefab-1234-abcd-5678-cdef0123ab01-2/0123abcd-abcd-4f7f-1234-9876543210ef",
           "OperationState": "PENDING",
           "OperationType": "UPDATE_SECURITY",
           "SourceClusterInfo": {},
           "TargetClusterInfo": {}
       }
   }
   ```

   If `OperationState` has the value `PENDING` or `UPDATE_IN_PROGRESS`, wait a while, then run the `describe-cluster-operation` command again. 

**Note**  
The AWS CLI and API operations for updating the security settings of a cluster are idempotent. This means that if you invoke the security update operation and specify an authentication or encryption setting that is the same setting that the cluster currently has, that setting won't change.