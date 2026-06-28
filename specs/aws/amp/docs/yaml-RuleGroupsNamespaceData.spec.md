---
id: "@specs/aws/amp/docs/yaml-RuleGroupsNamespaceData"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RuleGroupsNamespaceData"
status: active
depends_on:
  - "@specs/aws/amp/meta"
---

# RuleGroupsNamespaceData

> **source:** AWS Documentation
> **spec:id:** @specs/aws/amp/docs/yaml-RuleGroupsNamespaceData
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RuleGroupsNamespaceData YAML structure
<a name="yaml-RuleGroupsNamespaceData"></a>

The `RuleGroupsNamespaceData` structure contains the rule groups file as a base64-encoded blob of the YAML file. The following is an example of an rules file YAML.

```
groups:
  - name: test
    rules:
    - record: metric:recording_rule
      expr: avg(rate(container_cpu_usage_seconds_total[5m]))
  - name: alert-test
    rules:
    - alert: metric:alerting_rule
      expr: avg(rate(container_cpu_usage_seconds_total[5m])) > 0
      for: 2m
```

For more details about rules, see [Recording rules and alerting rules](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-Ruler.html) in the *Amazon Managed Service for Prometheus User Guide*.