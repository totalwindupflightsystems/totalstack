---
id: "@specs/aws/lambda/docs/runtime-management-shared"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Shared responsibility model"
status: active
depends_on:
  - "@specs/aws/lambda/meta"
---

# Shared responsibility model

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lambda/docs/runtime-management-shared
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Understanding the shared responsibility model for Lambda runtime management
<a name="runtime-management-shared"></a>

Lambda is responsible for curating and publishing security updates for all supported managed runtimes and container images. Responsibility for updating existing functions to use the latest runtime version varies depending on which runtime update mode you use.

Lambda is responsible for applying runtime updates to all functions configured to use the **Auto** runtime update mode.

For functions configured with the **Function update** runtime update mode, you're responsible for regularly updating your function. Lambda is responsible for applying runtime updates when you make those updates. If you don't update your function, then Lambda doesn't update the runtime. If you don't regularly update your function, then we strongly recommend configuring it for automatic runtime updates so that it continues to receive security updates.

For functions configured to use the **Manual** runtime update mode, you're responsible for updating your function to use the latest runtime version. We strongly recommend that you use this mode only to roll back the runtime version as a temporary mitigation in the rare event of runtime update incompatibility. We also recommend that you change to **Auto** mode as quickly as possible to minimize the time in which your functions aren't patched.

If you're [using container images to deploy your functions](images-create.md), then Lambda is responsible for publishing updated base images. In this case, you're responsible for rebuilding your function's container image from the latest base image and redeploying the container image.

This is summarized in the following table:


****  

| Deployment mode | Lambda's responsibility | Customer's responsibility | 
| --- | --- | --- | 
| Managed runtime, Auto mode | Publish new runtime versions containing the latest patches.<br />Apply runtime patches to existing functions. | Roll back to a previous runtime version in the rare event of a runtime update compatibility issue. Follow best practices for [backward compatibility](runtimes-update.md#runtime-update-compatibility). | 
| Managed runtime, Function update mode | Publish new runtime versions containing the latest patches. | Update functions regularly to pick up the latest runtime version.<br />Switch a function to **Auto** mode when you're not regularly updating the function.<br />Roll back to a previous runtime version in the rare event of a runtime update compatibility issue. Follow best practices for [backward compatibility](runtimes-update.md#runtime-update-compatibility). | 
| Managed runtime, Manual mode | Publish new runtime versions containing the latest patches. | Use this mode only for temporary runtime rollback in the rare event of a runtime update compatibility issue.<br />Switch functions to **Auto** or **Function update** mode and the latest runtime version as soon as possible. | 
| Container image | Publish new container images containing the latest patches. | Redeploy functions regularly using the latest container base image to pick up the latest patches. | 

For more information about shared responsibility with AWS, see [Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/).