---
id: "@specs/aws/opensearchserverless/docs/custom-package-kms-integration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Amazon OpenSearch Service custom package AWS KMS integration"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Amazon OpenSearch Service custom package AWS KMS integration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/custom-package-kms-integration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Amazon OpenSearch Service custom package AWS KMS integration
<a name="custom-package-kms-integration"></a>

Amazon OpenSearch Service custom packages provide encryption by default to protect your `ZIP-PLUGIN` packages at rest using AWS managed keys.
+ **AWS owned keys** – Amazon OpenSearch Service custom packages use these keys by default to automatically encrypt your `ZIP-PLUGIN` packages. You can't view, manage, or use AWS owned keys or audit their use. However, you don't need to take any action or change any programs to protect the keys that encrypt your data. For more information, see [AWS owned keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-owned-cmk) in the *AWS Key Management Service Developer Guide*.
+ **Customer managed keys** – You can add a second layer of encryption over the existing AWS owned keys by choosing a customer managed key when you create your `ZIP-PLUGIN` custom package.

  Amazon OpenSearch Service custom packages support using a symmetric customer managed key that you create, own, and manage to add a second layer of encryption over the existing AWS owned encryption. Because you have full control of this layer of encryption, you can perform the following tasks:
  + Establish and maintain key policies
  + Establish and maintain AWS Identity and Access Management (IAM) policies and grants
  + Enable and disable key policies
  + Rotate key cryptographic material
  + Add tags
  + Create key aliases
  + Schedule keys for deletion

For more information, see [Customer managed keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk) in the *AWS Key Management Service Developer Guide*.

**Note**  
Amazon OpenSearch Service custom packages automatically enables encryption at rest using AWS owned keys at no charge. However, AWS KMS charges apply when you use a customer managed key. For more information about pricing, see [AWS Key Management Service pricing](https://aws.amazon.com/kms/pricing/).

## How Amazon OpenSearch Service custom packages service uses grants in AWS KMS
<a name="custom-package-kms-grants"></a>

OpenSearch Service custom packages require a grant to use your customer managed key.

When you create a `ZIP-PLUGIN` package encrypted with a customer managed key, the Amazon OpenSearch Service custom packages service creates a grant on your behalf by sending a [CreateGrant](https://docs.aws.amazon.com/kms/latest/APIReference/API_CreateGrant.html) request to AWS KMS. Grants in AWS KMS give OpenSearch Service access to a AWS KMS key in your account. The grants created by OpenSearch Service custom packages have a constraint that allows operations only when the request includes an encryption context with your custom package ID.

Amazon OpenSearch Service custom packages require the grant to use your customer managed key for the following internal operations:


| Operation | Description | 
| --- | --- | 
| DescribeKey | Sends DescribeKey requests to AWS KMS to verify that the symmetric customer managed key ID entered when creating the plugin package is valid. | 
| GenerateDataKeyWithoutPlaintext | Sends GenerateDataKeyWithoutPlaintext requests to AWS KMS to generate data keys encrypted by your customer managed key. | 
| GenerateDataKey | Sends GenerateDataKey requests to AWS KMS to generate data keys to encrypt the package when copying it internally. | 
| Decrypt | Sends Decrypt requests to AWS KMS to decrypt the encrypted data keys so they can be used to decrypt your data. | 

You can revoke access to the grant or remove the service's access to the customer managed key at any time. If you do, OpenSearch Service won't be able to access any data encrypted by the customer managed key, which affects operations that depend on that data. For example, if you attempt to associate a plugin package that OpenSearch Service can't access, the operation returns an `AccessDeniedException` error.

## Create a customer managed key
<a name="custom-package-create-cmk"></a>

You can create a symmetric customer managed key by using the AWS Management Console or the AWS KMS APIs.

**To create a symmetric customer managed key**
+ Follow the steps in [Creating a KMS key](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html#create-symmetric-cmk) in the *AWS Key Management Service Developer Guide*.

### Key policy
<a name="custom-package-key-policy"></a>

Key policies control access to your customer managed key. Every customer managed key must have exactly one key policy, which contains statements that determine who can use the key and how they can use it. When you create your customer managed key, you can specify a key policy. For more information, see [Key policies in AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html) in the *AWS Key Management Service Developer Guide*.

To use your customer managed key with your plugin resources, you must permit the following API operations in the key policy:
+ `kms:CreateGrant` – Adds a grant to a customer managed key. Grants control access to a specified AWS KMS key, allowing access to grant operations that OpenSearch Service custom packages require. For more information about using grants, see the [AWS KMS Developer Guide](https://docs.aws.amazon.com/kms/latest/developerguide/grants.html).

  This allows OpenSearch Service to do the following:
  + Call `GenerateDataKeyWithoutPlainText` to generate an encrypted data key and store it for further validations.
  + Call `GenerateDataKey` to copy the plugin package internally.
  + Call `Decrypt` to access the plugin package internally.
  + Set up a retiring principal to allow the service to `RetireGrant`.
+ `kms:DescribeKey` – Provides the customer managed key details to allow OpenSearch Service to validate the key.
+ `kms:GenerateDataKey`, `kms:GenerateDataKeyWithoutPlaintext`, `kms:Decrypt` – Gives OpenSearch Service custom packages access to use these operations in the grant.

The following are policy statement examples you can add for OpenSearch Service custom packages:

```
"Statement" : [
  {
    "Sid" : "Allow access to principals authorized to use OpenSearch Service custom packages",
    "Effect" : "Allow",
    "Principal" : {
      "AWS" : "*"
    },
    "Action" : [
      "kms:CreateGrant",
      "kms:GenerateDataKey",
      "kms:GenerateDataKeyWithoutPlaintext",
      "kms:Decrypt"
    ],
    "Resource" : "*",
    "Condition" : {
      "StringEquals" : {
        "kms:ViaService" : "custom-packages.region.amazonaws.com"
      },
      "StringEquals" : {
        "kms:EncryptionContext:packageId": "Id of the package"
      }
    }
  },
  {
    "Sid" : "Allow access to principals authorized to use Amazon OpenSearch Service custom packages",
    "Effect" : "Allow",
    "Principal" : {
      "AWS" : "*"
    },
    "Action" : [
      "kms:DescribeKey"
    ],
    "Resource" : "*",
    "Condition" : {
      "StringEquals" : {
        "kms:ViaService" : "custom-packages.region.amazonaws.com"
      }
    }
  }
]
```

For more information about specifying permissions in a policy, see [Key policies in AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html) in the *AWS Key Management Service Developer Guide*.

For more information about troubleshooting key access, see [Troubleshooting AWS KMS permissions](https://docs.aws.amazon.com/kms/latest/developerguide/policy-evaluation.html) in the *AWS Key Management Service Developer Guide*.

## Specify a customer managed key for Amazon OpenSearch Service custom packages
<a name="custom-package-specify-cmk"></a>

You can specify a customer managed key as a second layer of encryption for your `ZIP-PLUGIN` packages.

When you create a plugin package, you can specify the data key by entering a AWS KMS key ID, which OpenSearch Service custom packages use to encrypt the plugin package.

*AWS KMS key ID* — A key identifier for a AWS KMS customer managed key. Enter a key ID, key ARN, alias name, or alias ARN.

## Amazon OpenSearch Service custom packages encryption context
<a name="custom-package-encryption-context"></a>

An encryption context is an optional set of key-value pairs that contain additional contextual information about the data.

AWS KMS uses the encryption context as additional authenticated data to support authenticated encryption. When you include an encryption context in a request to encrypt data, AWS KMS binds the encryption context to the encrypted data. To decrypt data, you include the same encryption context in the request.

### Amazon OpenSearch Service custom packages encryption context
<a name="custom-package-encryption-context-details"></a>

Amazon OpenSearch Service custom packages use the same encryption context in all AWS KMS cryptographic operations, where the key is `packageId` and the value is the `package-id` of your plugin package.

### Use encryption context for monitoring
<a name="custom-package-encryption-context-monitoring"></a>

When you use a symmetric customer managed key to encrypt your plugin package, you can use the encryption context in audit records and logs to identify how the customer managed key is being used. The encryption context also appears in logs generated by AWS CloudTrail or Amazon CloudWatch Logs.

### Using encryption context to control access to your customer managed key
<a name="custom-package-encryption-context-access-control"></a>

You can use the encryption context in key policies and IAM policies as conditions to control access to your symmetric customer managed key. You can also use encryption context constraints in a grant.

OpenSearch Service custom packages use an encryption context constraint in grants to control access to the customer managed key in your account or Region. The grant constraint requires that the operations that the grant allows use the specified encryption context.

The following are example key policy statements to grant access to a customer managed key for a specific encryption context. The condition in this policy statement requires that the grants have an encryption context constraint that specifies the encryption context.

```
{
    "Sid": "Enable DescribeKey",
    "Effect": "Allow",
    "Principal": {
        "AWS": "arn:aws:iam::111122223333:role/ExampleReadOnlyRole"
    },
    "Action": "kms:DescribeKey",
    "Resource": "*"
},
{
    "Sid": "Enable OpenSearch Service custom packages to use the key",
    "Effect": "Allow",
    "Principal": {
        "AWS": "arn:aws:iam::111122223333:role/ExampleReadOnlyRole"
    },
    "Action" : [
         "kms:CreateGrant",
        "kms:GenerateDataKey",
        "kms:GenerateDataKeyWithoutPlaintext",
        "kms:Decrypt"
    ],
    "Resource": "*",
    "Condition": {
        "StringEquals" : {
            "kms:EncryptionContext:packageId": "ID of the package"
         }
    }
}
```

## Monitoring your encryption keys for OpenSearch custom packages service
<a name="custom-package-monitoring-keys"></a>

When you use an AWS KMS customer managed key with your OpenSearch Service custom packages service resources, you can use CloudTrail or CloudWatch Logs to track requests that OpenSearch custom packages send to AWS KMS.

**Learn more**  
The following resources provide more information about data encryption at rest.
+ For more information about AWS KMS basic concepts, see [AWS KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html) in the *AWS Key Management Service Developer Guide*.
+ For more information about security best practices for AWS KMS, see the *AWS Prescriptive Guidance* guide for [AWS Key Management Service best practices](https://docs.aws.amazon.com/kms/latest/developerguide/best-practices.html).