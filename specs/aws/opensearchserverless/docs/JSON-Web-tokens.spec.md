---
id: "@specs/aws/opensearchserverless/docs/JSON-Web-tokens"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS JSON Web Tokens"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# JSON Web Tokens

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/JSON-Web-tokens
> **target_lang:** meta — documentation tier. ALL sections preserved.



# JWT authentication and authorization for Amazon OpenSearch Service
<a name="JSON-Web-tokens"></a>

Amazon OpenSearch Service now allows you to use JSON Web Tokens (JWTs) for authentication and authorization. JWTs are JSON-based access tokens used to grant single sign-on (SSO) access. You can use JWTs in OpenSearch Service to create single sign-on tokens to validate requests to your OpenSearch Service domain. To use JWTs, you must have fine-grained access control enabled, and you must provide a valid RSA or ECDSA PEM formatted public key. For more information on fine-grained access control, see [Fine-grained access control in Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/fgac.html).

You can configure JSON Web Tokens by using the OpenSearch Service console, the AWS Command Line Interface (AWS CLI), or the AWS SDKs.

## Considerations
<a name="consider"></a>

Before you use JWTs with Amazon OpenSearch Service you must consider the following:
+ Due to the size of RSA public keys in PEM formatting, we recommend using the AWS console to configure JWT authentication and authorization. 
+ You must provide valid users and roles when specifying the subjects and roles fields for your JWTs, otherwise, requests will be denied. 
+ OpenSearch 2.11 is the earliest compatible version that can be used for JWT authentication.

## Modifying the domain access policy
<a name="modifying"></a>

Before you can configure your domain to use JWT authentication and authorization, you must update your domain access policy to allow JWT users to access the domain. Otherwise, all incoming JWT authorized requests are denied. The recommended domain access policy to provide full access to the sub resources (/\*) is: 

------
#### [ JSON ]

****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
      {
      "Effect": "Allow",
      "Principal": {
        "AWS": "*"
      },
      "Action": "es:ESHttp*",
      "Resource": "arn:aws:es:{{us-east-1}}:{{111122223333}}:domain/{{domain-name}}/*"
    }
  ]
}
```

------

## Configuring JWT authentication and authorization
<a name="configuration"></a>

You can enable JWT authentication and authorization during the domain creation process or by updating an existing domain. The set-up steps vary slightly depending on which option you choose. 

The following steps explain how to configure an existing domain for JWT authentication and authorization in the OpenSearch Service console:

1. Under **Domain configuration**, navigate to **JWT authentication and authorization for OpenSearch**, select **Enable JWT authentication and authorization**. 

1. Configure the public key to use for your domain. To do this, you can either upload a PEM file, containing a public key, or manually enter it. 
**Note**  
If the uploaded or entered key is not valid, a warning will appear above the text box specifying the issue.

1. (Optional) Under Additional settings, you can configure the following optional fields
   + **Subject key** — you can leave this field empty to use the default `sub` key for your JWTs. 
   +  **Roles key** — you can leave this field empty to use the default `roles` key for your JWTs.

   After you've made your changes, save your domain.

## Using a JWKS endpoint to validate a JWT
<a name="jwks-endpoint"></a>

Instead of configuring a static public key, you can configure a JSON Web Key Set (JWKS) endpoint URL to dynamically retrieve public keys from your identity provider. When a JWKS endpoint is configured, OpenSearch Service automatically fetches and caches the public keys used to validate JWT signatures, eliminating the need to manually update keys when your identity provider rotates signing keys.

JWKS endpoint configuration requires OpenSearch version 3.3 or later.

**Note**  
When both a JWKS URL and a static public key are configured, the JWKS URL takes precedence and the static public key is ignored.

### Backward compatibility
<a name="jwks-backward-compatibility"></a>

This feature maintains full backward compatibility:
+ When `JwksUrl` is not specified or set to null, the system uses the existing static public key mechanism.
+ Existing JWT configurations continue to work without modification.
+ You can switch between static keys and JWKS by updating the domain configuration.

### Configuring a JWKS endpoint
<a name="jwks-configuring"></a>

You can configure a JWKS endpoint using the OpenSearch Service console, the AWS CLI, or the configuration API.

#### Console
<a name="jwks-console"></a>

**To configure a JWKS endpoint**

1. Under **Domain configuration**, navigate to **JWT authentication and authorization for OpenSearch**.

1. Select **Enable JWT authentication and authorization**.

1. For **Key source**, select **JWKS URL**.

1. Enter the JWKS endpoint URL provided by your identity provider (for example, `https://example.com/.well-known/jwks.json`).

1. (Optional) Configure the **Subject key** and **Roles key** fields under **Additional settings**.

1. Choose **Save changes**.

#### AWS CLI
<a name="jwks-cli"></a>

The following AWS CLI command configures a JWKS endpoint for JWT authentication on an existing domain:

```
aws opensearch update-domain-config \
  --domain-name {{my-domain}} \
  --advanced-security-options '{"JWTOptions":{"Enabled":true, "JwksUrl":"{{https://example.com/.well-known/jwks.json}}", "SubjectKey":"{{sub}}", "RolesKey":"{{roles}}"}}'
```

#### Configuration API
<a name="jwks-api"></a>

The following request to the configuration API configures a JWKS endpoint for JWT authentication on an existing domain:

```
POST https://es.{{us-east-1}}.amazonaws.com/2021-01-01/opensearch/domain/{{my-domain}}/config
{
  "AdvancedSecurityOptions": {
    "JWTOptions": {
      "Enabled": true,
      "JwksUrl": "{{https://example.com/.well-known/jwks.json}}",
      "RolesKey": "{{optional-roles-key}}",
      "SubjectKey": "{{optional-subject-key}}"
    }
  }
}
```

### JWT header requirements
<a name="jwks-header-requirements"></a>

When using a JWKS endpoint, your JWT header must include a key ID (`kid`) that identifies the specific key to use for verification:

```
{
  "alg": "RS256",
  "typ": "JWT",
  "kid": "V-diposfUJIk5jDBFi_QRouiVinG5PowskcSWy5EuCo"
}
```

The `kid` value must match a key identifier in the JWKS endpoint response.

For more information about JWKS configuration options and security settings, see [Using a JWKS endpoint to validate a JWT](https://docs.opensearch.org/latest/security/authentication-backends/jwt/#using-a-jwks-endpoint-to-validate-a-jwt) in the OpenSearch documentation.

## Using a JWT to send a test request
<a name="test"></a>

After creating a new JWT with a specified a subject and role pair, you can send a test request. To do this, use the private key to sign your request through the tool that created the JWT. OpenSearch Service is able to validate the incoming request by verifying this signature. 

**Note**  
If you specified a custom subject key or roles key for your JWT, you must use the correct claims names for your JWT.

The following is an example of how to use a JWT token to access OpenSearch Service through your domain's search endpoint:

```
curl -XGET "$search_endpoint" -H "Authorization: Bearer <JWT>"
```

### Configuring JWT authentication and authorization (AWS CLI)
<a name="cli"></a>

The following AWS CLI command enables JWT authentication and authorization for OpenSearch provided that the domain exists:

```
aws opensearch update-domain-config --domain-name <your_domain_name> --advanced-security-options '{"JWTOptions":{"Enabled":true, "PublicKey": "<your_public_key>", "SubjectKey": "<your_subject_key>", "RolesKey": "<your_roles_key>"}}'
```

#### Configuring JWT authentication and authorization (configuration via API)
<a name="API"></a>

The following request to the configuration API enables JWT authentication and authorization for OpenSearch on an existing domain:

```
POST https://es.us-east-1.amazonaws.com/2021-01-01/opensearch/domain/my-domain/config
{
  "AdvancedSecurityOptions": {
    "JWTOptions": {
      "Enabled": true,
      "PublicKey": "public-key",
      "RolesKey": "optional-roles-key",
      "SubjectKey": "optional-subject-key"
   }  
  }
}
```

##### Generating a key pair
<a name="gen-key-pair"></a>

In order to configure JWTs for your OpenSearch domain, you will need to provide a public key in Privacy-Enhanced Mail (PEM) format. Amazon OpenSearch Service currently supports two asymetric encryption algorithms when using JWTs: RSA and ECDSA.

To create an RSA key pair using the common openssl library, follow these steps:

1. `openssl genrsa -out privatekey.pem 2048`

1. `openssl rsa -in privatekey.pem -pubout -out publickey.pem`

In this example, the `publickey.pem` file contains the public key for use with Amazon OpenSearch Service, while `privatekey.pem` contains the private for signing the JWTs sent to the service. Additionally, you have the option to convert the private key into the commonly used `pkcs8` format if you need that to generate your JWTs.

If you use the upload button to add a PEM file directly to the console, the file must have a `.pem` extension, other file extensions such as `.crt`,`.cert`, or `.key` are not supported at this time. 