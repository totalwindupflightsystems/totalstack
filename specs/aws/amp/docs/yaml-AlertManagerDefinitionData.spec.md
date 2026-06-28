---
id: "@specs/aws/amp/docs/yaml-AlertManagerDefinitionData"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AlertManagerDefinitionData"
status: active
depends_on:
  - "@specs/aws/amp/meta"
---

# AlertManagerDefinitionData

> **source:** AWS Documentation
> **spec:id:** @specs/aws/amp/docs/yaml-AlertManagerDefinitionData
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AlertManagerDefinitionData YAML structure
<a name="yaml-AlertManagerDefinitionData"></a>

This structure contains the alert manager configuration as a blob (binary data). It is a base64-encoded YAML file. The following is an example of an alert manager configuration file YAML.

```
alertmanager_config: |
  route:
    receiver: 'default'
  receivers:
    - name: 'default'
      sns_configs:
      - topic_arn: arn:aws:sns:us-east-2:123456789012:My-Topic
        sigv4:
          region: us-east-2
        attributes:
          key: key1
          value: value1
```

For more information about alert manager configurations and their use, see [Creating an alert manager configuration file](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-alertmanager-config.html) in the *Amazon Managed Service for Prometheus User Guide*.