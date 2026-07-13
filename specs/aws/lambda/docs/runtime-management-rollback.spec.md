---
id: "@specs/aws/lambda/docs/runtime-management-rollback"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Runtime version roll-back"
status: active
depends_on:
  - "@specs/aws/lambda/meta"
---

# Runtime version roll-back

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lambda/docs/runtime-management-rollback
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Rolling back a Lambda runtime version
<a name="runtime-management-rollback"></a>

In the rare event that a new runtime version is incompatible with your existing function, you can roll back its runtime version to an earlier one. This keeps your application working and minimizes disruption, providing time to remedy the incompatibility before returning to the latest runtime version.

Lambda doesn't impose a time limit on how long you can use any particular runtime version. However, we strongly recommend updating to the latest runtime version as soon as possible to benefit from the latest security patches, performance improvements, and features. Lambda provides the option to roll back to an earlier runtime version only as a temporary mitigation in the rare event of a runtime update compatibility issue. Functions using an earlier runtime version for an extended period may eventually experience degraded performance or issues, such as a certificate expiry, which can cause them to stop working properly.

You can roll back a runtime version in the following ways:
+ [Using the Manual runtime update mode](#runtime-management-rollback-manual)
+ [Using published function versions](#runtime-management-rollback-published)

For more information, see [Introducing AWS Lambda runtime management controls](https://aws.amazon.com/blogs/compute/introducing-aws-lambda-runtime-management-controls/) on the AWS Compute Blog.

## Roll back a runtime version using Manual runtime update mode
<a name="runtime-management-rollback-manual"></a>

If you're using the **Auto** runtime version update mode, or you're using the `$LATEST` runtime version, you can roll back your runtime version using the **Manual** mode. For the [function version](configuration-versions.md) you want to roll back, change the runtime version update mode to **Manual** and specify the ARN of the previous runtime version. For more information about finding the ARN of the previous runtime version, see [Identifying Lambda runtime version changes](runtime-management-identify.md).

**Note**  
If the `$LATEST` version of your function is configured to use **Manual** mode, then you can't change the CPU architecture or runtime version that your function uses. To make these changes, you must change to **Auto** or **Function update** mode.

## Roll back a runtime version using published function versions
<a name="runtime-management-rollback-published"></a>

Published [function versions](configuration-versions.md) are an immutable snapshot of the `$LATEST` function code and configuration at the time that you created them. In **Auto** mode, Lambda automatically updates the runtime version of published function versions during phase two of the runtime version rollout. In **Function update** mode, Lambda doesn't update the runtime version of published function versions.

Published function versions using **Function update** mode therefore create a static snapshot of the function code, configuration, and runtime version. By using **Function update** mode with function versions, you can synchronize runtime updates with your deployments. You can also coordinate rollback of code, configuration, and runtime versions by redirecting traffic to an earlier published function version. You can integrate this approach into your continuous integration and continuous delivery (CI/CD) for fully automatic rollback in the rare event of runtime update incompatibility. When using this approach, you must update your function regularly and publish new function versions to pick up the latest runtime updates. For more information, see [Understanding the shared responsibility model for Lambda runtime management](runtime-management-shared.md).