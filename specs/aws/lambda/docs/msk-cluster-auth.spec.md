---
id: "@specs/aws/lambda/docs/msk-cluster-auth"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Cluster authentication"
status: active
depends_on:
  - "@specs/aws/lambda/meta"
---

# Cluster authentication

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lambda/docs/msk-cluster-auth
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Configuring Amazon MSK cluster authentication methods in Lambda
<a name="msk-cluster-auth"></a>

Lambda needs permission to access your Amazon MSK cluster, retrieve records, and perform other tasks. Amazon MSK supports several ways to authenticate with your MSK cluster.

**Topics**
+ [Unauthenticated access](#msk-unauthenticated)
+ [SASL/SCRAM authentication](#msk-sasl-scram)
+ [Mutual TLS authentication](#msk-mtls)
+ [IAM authentication](#msk-iam-auth)
+ [How Lambda chooses a bootstrap broker](#msk-bootstrap-brokers)

## Unauthenticated access
<a name="msk-unauthenticated"></a>

If no clients access the cluster over the internet, you can use unauthenticated access.

## SASL/SCRAM authentication
<a name="msk-sasl-scram"></a>

Lambda supports [ Simple Authentication and Security Layer/Salted Challenge Response Authentication Mechanism (SASL/SCRAM)](https://docs.aws.amazon.com/msk/latest/developerguide/msk-password-tutorial.html) authentication, with the SHA-512 hash function and Transport Layer Security (TLS) encryption. For Lambda to connect to the cluster, store the authentication credentials (username and password) in a Secrets Manager secret, and reference this secret when configuring your event source mapping.

For more information about using Secrets Manager, see [Sign-in credentials authentication with Secrets Manager](https://docs.aws.amazon.com/msk/latest/developerguide/msk-password.html) in the *Amazon Managed Streaming for Apache Kafka Developer Guide*.

**Note**  
Amazon MSK doesn't support SASL/PLAIN authentication.

## Mutual TLS authentication
<a name="msk-mtls"></a>

Mutual TLS (mTLS) provides two-way authentication between the client and the server. The client sends a certificate to the server for the server to verify the client. The server also sends a certificate to the client for the client to verify the server.

For Amazon MSK integrations with Lambda, your MSK cluster acts as the server, and Lambda acts as the client.
+ For Lambda to verify your MSK cluster, you configure a client certificate as a secret in Secrets Manager, and reference this certificate in your event source mapping configuration. The client certificate must be signed by a certificate authority (CA) in the server's trust store.
+ The MSK cluster also sends a server certificate to Lambda. The server certificate must be signed by a certificate authority (CA) in the AWS trust store.

Amazon MSK doesn't support self-signed server certificates. All brokers in Amazon MSK use [public certificates](https://docs.aws.amazon.com/msk/latest/developerguide/msk-encryption.html) signed by [Amazon Trust Services CAs](https://www.amazontrust.com/repository/), which Lambda trusts by default.

### Configuring the mTLS secret
<a name="mtls-auth-secret"></a>

The CLIENT\_CERTIFICATE\_TLS\_AUTH secret requires a certificate field and a private key field. For an encrypted private key, the secret requires a private key password. Both the certificate and private key must be in PEM format.

**Note**  
Lambda supports the [PBES1](https://datatracker.ietf.org/doc/html/rfc2898/#section-6.1) (but not PBES2) private key encryption algorithms.

The certificate field must contain a list of certificates, beginning with the client certificate, followed by any intermediate certificates, and ending with the root certificate. Each certificate must start on a new line with the following structure:

```
-----BEGIN CERTIFICATE-----  
        <certificate contents>
-----END CERTIFICATE-----
```

Secrets Manager supports secrets up to 65,536 bytes, which is enough space for long certificate chains.

The private key must be in [PKCS \#8](https://datatracker.ietf.org/doc/html/rfc5208) format, with the following structure:

```
-----BEGIN PRIVATE KEY-----  
         <private key contents>
-----END PRIVATE KEY-----
```

For an encrypted private key, use the following structure:

```
-----BEGIN ENCRYPTED PRIVATE KEY-----  
          <private key contents>
-----END ENCRYPTED PRIVATE KEY-----
```

The following example shows the contents of a secret for mTLS authentication using an encrypted private key. For an encrypted private key, you include the private key password in the secret.

```
{
 "privateKeyPassword": "testpassword",
 "certificate": "-----BEGIN CERTIFICATE-----
MIIE5DCCAsygAwIBAgIRAPJdwaFaNRrytHBto0j5BA0wDQYJKoZIhvcNAQELBQAw
...
j0Lh4/+1HfgyE2KlmII36dg4IMzNjAFEBZiCRoPimO40s1cRqtFHXoal0QQbIlxk
cmUuiAii9R0=
-----END CERTIFICATE-----
-----BEGIN CERTIFICATE-----
MIIFgjCCA2qgAwIBAgIQdjNZd6uFf9hbNC5RdfmHrzANBgkqhkiG9w0BAQsFADBb
...
rQoiowbbk5wXCheYSANQIfTZ6weQTgiCHCCbuuMKNVS95FkXm0vqVD/YpXKwA/no
c8PH3PSoAaRwMMgOSA2ALJvbRz8mpg==
-----END CERTIFICATE-----",
 "privateKey": "-----BEGIN ENCRYPTED PRIVATE KEY-----
MIIFKzBVBgkqhkiG9w0BBQ0wSDAnBgkqhkiG9w0BBQwwGgQUiAFcK5hT/X7Kjmgp
...
QrSekqF+kWzmB6nAfSzgO9IaoAaytLvNgGTckWeUkWn/V0Ck+LdGUXzAC4RxZnoQ
zp2mwJn2NYB7AZ7+imp0azDZb+8YG2aUCiyqb6PnnA==
-----END ENCRYPTED PRIVATE KEY-----"
}
```

For more information about mTLS for Amazon MSK, and instructions on how to generate a client certificate, see [Mutual TLS client authentication for Amazon MSK](https://docs.aws.amazon.com/msk/latest/developerguide/msk-authentication.html) in the *Amazon Managed Streaming for Apache Kafka Developer Guide*.

## IAM authentication
<a name="msk-iam-auth"></a>

You can use AWS Identity and Access Management (IAM) to authenticate the identity of clients that connect to the MSK cluster. With IAM auth, Lambda relies on the permissions in your function's [execution role](lambda-intro-execution-role.md) to connect to the cluster, retrieve records, and perform other required actions. For a sample policy that contains the necessary permissions, see [ Create authorization policies for the IAM role](https://docs.aws.amazon.com/msk/latest/developerguide/create-iam-access-control-policies.html) in the *Amazon Managed Streaming for Apache Kafka Developer Guide*.

If IAM auth is active on your MSK cluster, and you don't provide a secret, Lambda automatically defaults to using IAM auth.

For more information about IAM authentication in Amazon MSK, see [IAM access control](https://docs.aws.amazon.com/msk/latest/developerguide/iam-access-control.html).

## How Lambda chooses a bootstrap broker
<a name="msk-bootstrap-brokers"></a>

Lambda chooses a [ bootstrap broker](https://docs.aws.amazon.com/msk/latest/developerguide/msk-get-bootstrap-brokers.html) based on the authentication methods available on your cluster, and whether you provide a secret for authentication. If you provide a secret for mTLS or SASL/SCRAM, Lambda automatically chooses that auth method. If you don't provide a secret, Lambda selects the strongest auth method that's active on your cluster. The following is the order of priority in which Lambda selects a broker, from strongest to weakest auth:
+ mTLS (secret provided for mTLS)
+ SASL/SCRAM (secret provided for SASL/SCRAM)
+ SASL IAM (no secret provided, and IAM auth active)
+ Unauthenticated TLS (no secret provided, and IAM auth not active)
+ Plaintext (no secret provided, and both IAM auth and unauthenticated TLS are not active)

**Note**  
If Lambda can't connect to the most secure broker type, Lambda doesn't attempt to connect to a different (weaker) broker type. If you want Lambda to choose a weaker broker type, deactivate all stronger auth methods on your cluster.