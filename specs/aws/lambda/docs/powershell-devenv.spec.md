---
id: "@specs/aws/lambda/docs/powershell-devenv"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Development Environment"
status: active
depends_on:
  - "@specs/aws/lambda/meta"
---

# Development Environment

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lambda/docs/powershell-devenv
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Setting Up a PowerShell Development Environment
<a name="powershell-devenv"></a>

Lambda provides a set of tools and libraries for the PowerShell runtime. For installation instructions, see [Lambda tools for PowerShell](https://github.com/aws/aws-lambda-dotnet/tree/master/PowerShell) on GitHub.

The AWSLambdaPSCore module includes the following cmdlets to help author and publish PowerShell Lambda functions:
+ **Get-AWSPowerShellLambdaTemplate** – Returns a list of getting started templates.
+ **New-AWSPowerShellLambda** – Creates an initial PowerShell script based on a template.
+ **Publish-AWSPowerShellLambda** – Publishes a given PowerShell script to Lambda.
+ **New-AWSPowerShellLambdaPackage** – Creates a Lambda deployment package that you can use in a CI/CD system for deployment.