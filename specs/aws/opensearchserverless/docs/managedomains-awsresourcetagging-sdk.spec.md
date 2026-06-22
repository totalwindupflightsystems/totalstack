---
id: "@specs/aws/opensearchserverless/docs/managedomains-awsresourcetagging-sdk"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Tagging domains (AWS SDKs)"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Tagging domains (AWS SDKs)

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/managedomains-awsresourcetagging-sdk
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Tagging domains (AWS SDKs)
<a name="managedomains-awsresourcetagging-sdk"></a>

The AWS SDKs (except the Android and iOS SDKs) support all the actions defined in the [Amazon OpenSearch Service API Reference](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/Welcome.html), including the `AddTags`, `ListTags`, and `RemoveTags` operations. For more information about installing and using the AWS SDKs, see [AWS Software Development Kits](https://aws.amazon.com/code). 

## **Python**
<a name="pythonsample"></a>

This example uses the [OpenSearchService](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch.html) low-level Python client from the AWS SDK for Python (Boto) to add a tag to a domain, list the tag attached to the domain, and remove a tag from the domain. You must provide values for `DOMAIN_ARN`, `TAG_KEY`, and `TAG_VALUE`.

```
import boto3
from botocore.config import Config  # import configuration

DOMAIN_ARN = ''  # ARN for the domain. i.e "arn:aws:es:us-east-1:123456789012:domain/my-domain
TAG_KEY = ''  # The name of the tag key. i.e 'Smileyface'
TAG_VALUE = ''  # The value assigned to the tag. i.e 'Practicetag'

# defines the configurations parameters such as region

my_config = Config(region_name='us-east-1')
client = boto3.client('opensearch', config=my_config)


# defines the client variable

def addTags():
    """Adds tags to the domain"""

    response = client.add_tags(ARN=DOMAIN_ARN,
                               TagList=[{'Key': TAG_KEY,
                                         'Value': TAG_VALUE}])

    print(response)


def listTags():
    """List tags that have been added to the domain"""

    response = client.list_tags(ARN=DOMAIN_ARN)
    print(response)


def removeTags():
    """Remove tags that have been added to the domain"""

    response = client.remove_tags(ARN=DOMAIN_ARN, TagKeys=[TAG_KEY])

    print('Tag removed')
    return response
```