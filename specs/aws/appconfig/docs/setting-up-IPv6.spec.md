---
id: "@specs/aws/appconfig/docs/setting-up-IPv6"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Understanding IPv6 support"
status: active
depends_on:
  - "@specs/aws/appconfig/meta"
---

# Understanding IPv6 support

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appconfig/docs/setting-up-IPv6
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Understanding IPv6 support
<a name="setting-up-IPv6"></a>

All AWS AppConfig APIs fully support IPv4 and IPv6 calls.

**Control plane APIs**

Use the following endpoint for IPv4 and IPv6 dual-stack calls to the [control plane](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_Operations_Amazon_AppConfig.html):

```
appconfig.{{Region}}.api.aws
```

For example: appconfig.us-east-1.api.aws

For IPv4 only, use the following URL:

```
appconfig.{{Region}}.amazonaws.com
```

**Data plane APIs**

For dual-stack calls to the [data plane](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_Operations_AWS_AppConfig_Data.html), use the following endpoint:

```
appconfigdata.{{Region}}.api.aws
```

For example: appconfig.us-east-1.api.aws

For IPv4 only, use the following URL:

```
appconfigdata.{{Region}}.amazonaws.com
```

**Note**  
For more information, see [AWS AppConfig endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/appconfig.html) in the *AWS General Reference*.