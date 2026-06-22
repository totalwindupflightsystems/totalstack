---
id: "@specs/aws/opensearchserverless/docs/managedomains-snapshot-registerdirectory"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Registering a manual snapshot repository"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Registering a manual snapshot repository

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/managedomains-snapshot-registerdirectory
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Registering a manual snapshot repository
<a name="managedomains-snapshot-registerdirectory"></a>

You need to register a snapshot repository with OpenSearch Service before you can take manual index snapshots. This one-time operation requires that you sign your AWS request with credentials that are allowed to access `TheSnapshotRole`, as described in [Prerequisites](managedomains-snapshots.md#managedomains-snapshot-prerequisites).

## Step 1: Map the snapshot role in OpenSearch Dashboards (if using fine-grained access control)
<a name="managedomains-snapshot-fgac"></a>

Fine-grained access control introduces an additional step when registering a repository. Even if you use HTTP basic authentication for all other purposes, you need to map the `manage_snapshots` role to your IAM role that has `iam:PassRole` permissions to pass `TheSnapshotRole`.

1. Navigate to the OpenSearch Dashboards plugin for your OpenSearch Service domain. You can find the Dashboards endpoint on your domain dashboard on the OpenSearch Service console. 

1. From the main menu choose **Security**, **Roles**, and select the **manage\_snapshots** role.

1. Choose **Mapped users**, **Manage mapping**. 

1. Add the ARN of the role that has permissions to pass `TheSnapshotRole`. Put role ARNs under **Backend roles**.

   ```
   arn:aws:iam::{{123456789123}}:role/{{role-name}}
   ```

1. Select **Map** and confirm the user or role shows up under **Mapped users**.

## Step 2: Register a repository
<a name="managedomains-snapshot-register"></a>

The following **Snapshots** tab demonstrates how to register a snapshot directory. For options specific to encrypting a manual snapshot and registering a snapshot after migrating to a new domain, see the relevant tabs.

------
#### [ Snapshots ]

To register a snapshot repository, send a PUT request to the OpenSearch Service domain endpoint. You can use [curl](https://curl.se/docs/manpage.html#--aws-sigv4), the [sample Python client](#managedomains-snapshot-client-python), [Postman](https://www.getpostman.com/), or some other method to send a signed request to register the snapshot repository. Note that you can't use a PUT request in the OpenSearch Dashboards console to register the repository.

The request takes the following format:

```
PUT {{domain-endpoint}}/_snapshot/{{my-snapshot-repo-name}}
{
  "type": "s3",
  "settings": {
    "bucket": "{{amzn-s3-demo-bucket}}",
    "base_path": "{{my/snapshot/directory}}",
    "region": "{{region}}",
    "role_arn": "arn:aws:iam::{{123456789012}}:role/{{TheSnapshotRole}}"
  }
}
```

**Note**  
Repository names cannot start with "cs-". Additionally, you shouldn't write to the same repository from multiple domains. Only one domain should have write access to the repository.

If your domain resides within a virtual private cloud (VPC), your computer must be connected to the VPC for the request to successfully register the snapshot repository. Accessing a VPC varies by network configuration, but likely involves connecting to a VPN or corporate network. To check that you can reach the OpenSearch Service domain, navigate to `https://{{your-vpc-domain}}.{{region}}.es.amazonaws.com` in a web browser and verify that you receive the default JSON response.

When your Amazon S3 bucket is in another AWS Region than your OpenSearch domain, add the parameter `"endpoint": "s3.amazonaws.com"` to the request.

------
#### [ Encrypted snapshots ]

You currently can't use AWS Key Management Service (KMS) keys to encrypt manual snapshots, but you can protect them using server-side encryption (SSE).

To turn on SSE with S3-managed keys for the bucket you use as a snapshot repository, add `"server_side_encryption": true` to the `"settings"` block of the PUT request. For more information, see [Using server-side encryption with Amazon S3 managed keys (SSE-S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingServerSideEncryption.html) in the *Amazon Simple Storage Service User Guide*.

Alternatively, you can use AWS KMS keys for server-side encryption on the S3 bucket that you use as a snapshot repository. If you use this approach, make sure to provide `TheSnapshotRole` permission to the AWS KMS key used to encrypt the S3 bucket. For more information, see [Key policies in AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html).

------
#### [ Domain migration ]

Registering a snapshot repository is a one-time operation. However, to migrate from one domain to another, you have to register the same snapshot repository on the old domain and the new domain. The repository name is arbitrary.

Consider the following guidelines when migrating to a new domain or registering the same repository with multiple domains:
+ When registering the repository on the new domain, add `"readonly": true` to the `"settings"` block of the PUT request. This setting prevents you from accidentally overwriting data from the old domain. Only one domain should have write access to the repository.
+ If you're migrating data to a domain in a different AWS Region, (for example, from an old domain and bucket located in us-east-2 to a new domain in us-west-2), replace `"region": "{{region}}"` with `"endpoint": "s3.amazonaws.com"` in the PUT statement and retry the request.

------

### Using the sample Python client
<a name="managedomains-snapshot-client-python"></a>

The Python client is easier to automate than a simple HTTP request and has better reusability. If you choose to use this method to register a snapshot repository, save the following sample Python code as a Python file, such as `register-repo.py`. The client requires the [AWS SDK for Python (Boto3)](https://aws.amazon.com/sdk-for-python/), [requests](http://docs.python-requests.org/) and [requests-aws4auth](https://pypi.python.org/pypi/requests-aws4auth) packages. The client contains commented-out examples for other snapshot operations.

Update the following variables in the sample code: `host`, `region`, `path`, and `payload`.

```
import boto3
import requests
from requests_aws4auth import AWS4Auth

host = '' # domain endpoint
region = '' # e.g. us-west-1
service = 'es'
credentials = boto3.Session().get_credentials()
awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service, session_token=credentials.token)

# Register repository

path = '/_snapshot/{{my-snapshot-repo-name}}' # the OpenSearch API endpoint
url = host + path

payload = {
  "type": "s3",
  "settings": {
    "bucket": "{{amzn-s3-demo-bucket}}",
    "base_path": "{{my/snapshot/directory}}",
    "region": "{{us-west-1}}",
    "role_arn": "arn:aws:iam::{{123456789012}}:role/{{snapshot-role}}"
  }
}

headers = {"Content-Type": "application/json"}

r = requests.put(url, auth=awsauth, json=payload, headers=headers)

print(r.status_code)
print(r.text)

# # Take snapshot
#
# path = '/_snapshot/my-snapshot-repo-name/my-snapshot'
# url = host + path
#
# r = requests.put(url, auth=awsauth)
#
# print(r.text)
#
# # Delete index
#
# path = 'my-index'
# url = host + path
#
# r = requests.delete(url, auth=awsauth)
#
# print(r.text)
#
# # Restore snapshot (all indexes except Dashboards and fine-grained access control)
#
# path = '/_snapshot/my-snapshot-repo-name/my-snapshot/_restore'
# url = host + path
#
# payload = {
#   "indices": "-.kibana*,-.opendistro_security,-.opendistro-*",
#   "include_global_state": False
# }
#
# headers = {"Content-Type": "application/json"}
#
# r = requests.post(url, auth=awsauth, json=payload, headers=headers)
#
# print(r.text)
# 
# # Restore snapshot (one index)
#
# path = '/_snapshot/my-snapshot-repo-name/my-snapshot/_restore'
# url = host + path
#
# payload = {"indices": "my-index"}
#
# headers = {"Content-Type": "application/json"}
#
# r = requests.post(url, auth=awsauth, json=payload, headers=headers)
#
# print(r.text)
```