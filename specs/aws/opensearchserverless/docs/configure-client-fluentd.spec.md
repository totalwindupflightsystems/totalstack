---
id: "@specs/aws/opensearchserverless/docs/configure-client-fluentd"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Fluentd"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Fluentd

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/configure-client-fluentd
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Using an OpenSearch Ingestion pipeline with Fluentd
<a name="configure-client-fluentd"></a>

Fluentd is an open-source data collection ecosystem that provides SDKs for different languages and sub-projects like Fluent Bit. This sample [Fluentd configuration file](https://docs.fluentd.org/output/http#example-configuration) sends log data from Fluentd to an OpenSearch Ingestion pipeline. For more information about ingesting log data, see [Log Analytics](https://github.com/opensearch-project/data-prepper/blob/main/docs/log_analytics.md) in the Data Prepper documentation.

Note the following:
+ The `endpoint` value must be your pipeline endpoint. For example, `{{pipeline-endpoint}}.{{us-east-1}}osis.amazonaws.com/apache-log-pipeline/logs`.
+ The `aws_service` value must be `osis`.
+ The `aws_role_arn` value is the ARN of the AWS IAM role for the client to assume and use for Signature Version 4 authentication.

```
<source>
  @type tail
  path logs/sample.log
  path_key log
  tag apache
  <parse>
    @type none
  </parse>
</source>

<filter apache>
  @type record_transformer
  <record>
    log ${record["message"]}
  </record>
</filter>

<filter apache>
  @type record_transformer
  remove_keys message
</filter>

<match apache>
  @type http
  endpoint {{pipeline-endpoint}}.{{us-east-1}}osis.amazonaws.com/apache-log-pipeline/logs
  json_array true

  <auth>
    method aws_sigv4
    aws_service osis
    aws_region {{region}}
    aws_role_arn arn:aws:iam::{{account-id}}:role/{{ingestion-role}}
  </auth>

  <format>
    @type json
  </format>

  <buffer>
    flush_interval 1s
  </buffer>
</match>
```

You can then configure an OpenSearch Ingestion pipeline like the following, which has HTTP as the source:

```
version: "2"
apache-log-pipeline:
  source:
    http:
      path: "/${pipelineName}/logs"
  processor:
    - grok:
        match:
          log:
            - "%{TIMESTAMP_ISO8601:timestamp} %{NOTSPACE:network_node} %{NOTSPACE:network_host} %{IPORHOST:source_ip}:%{NUMBER:source_port:int} -> %{IPORHOST:destination_ip}:%{NUMBER:destination_port:int} %{GREEDYDATA:details}"
  sink:
    - opensearch:
        hosts: ["https://search-{{domain-endpoint}}.{{us-east-1}}es.amazonaws.com"]
        index: "{{index_name}}"
        aws_region: "{{region}}"
        aws_sigv4: true
```