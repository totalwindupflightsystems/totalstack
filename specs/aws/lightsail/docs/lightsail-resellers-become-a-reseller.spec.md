---
id: "@specs/aws/lightsail/docs/lightsail-resellers-become-a-reseller"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Become a Lightsail reseller"
status: active
depends_on:
  - "@specs/aws/lightsail/meta"
---

# Become a Lightsail reseller

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lightsail/docs/lightsail-resellers-become-a-reseller
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Become a Lightsail reseller
<a name="lightsail-resellers-become-a-reseller"></a>

You must submit a form to be considered for becoming an Amazon Lightsail reseller. The request will be filed using the AWS account that you are logged in with at the time you complete the form. If you use AWS Organizations to help centrally manage your AWS accounts, you should submit the request while using your management account to become a reseller. By using your management account, you get increased default Lightsail instance quotas across the member accounts in your organization. For more information on how Lightsail reseller benefits affect your AWS accounts, see [How Lightsail reseller benefits and increased default quotas apply to your accounts](lightsail-resellers.md#lightsail-resellers-how-accounts-benefit).

If your request is approved, and you have multiple organizations, you can submit an additional request to add the AWS account ID of each organization's management account to scale the increased default Lightsail instance quotas to the member accounts of those organizations as well. For more information about Organizations, see [What is AWS Organizations?](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html) in the *AWS Organizations User Guide*.

**Topics**
+ [Required information to become a Lightsail reseller](#lightsail-resellers-become-a-reseller-required-information)
+ [Request to become a Lightsail reseller](#lightsail-resellers-become-a-reseller-submit-request)
+ [Request additional accounts to become Lightsail resellers](#lightsail-resellers-become-a-reseller-request-additional-accounts)

## Required information to become a Lightsail reseller
<a name="lightsail-resellers-become-a-reseller-required-information"></a>

We will require some information about your planned usage and use case to consider your request to become an Amazon Lightsail reseller. A form is available on the Lightsail console that you can complete and submit for consideration. In addition to details about your business, you should have the following information to complete the form:
+ Size and quantity of instance bundles for the Lightsail resources you plan to use. For more information on the available bundles, see [Amazon Lightsail pricing](https://aws.amazon.com/lightsail/pricing/).
+ AWS account IDs that you want to enroll. If you are using AWS Organizations, you should only specify your management account in the request. This also enrolls the respective member accounts in the organization. For more information, see [Terminology and concepts for AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html) in the *AWS Organizations User Guide*.

## Request to become a Lightsail reseller
<a name="lightsail-resellers-become-a-reseller-submit-request"></a>

The following steps will submit a request to become a reseller. The AWS account ID that you are authenticated with will be used as the account that you'd like to have reseller benefits for. If your request is approved, you can then request additional accounts to be added.

**Tip**  
If you are using AWS Organizations, you should perform this procedure as the management account for your organization so that your member accounts also receive increased default Lightsail instance quotas.

**To request to become a reseller**

1. Sign in to the [Lightsail console](https://lightsail.aws.amazon.com/).

1. On the Lightsail home page, choose your user or role on the top navigation menu.

1. Choose **Account** in the dropdown menu.  
![Lightsail account page.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-console-account-menu.png)

1. On the **Profile** tab, under the Lightsail reseller section, choose **Become a Lightsail reseller**.  
![How to open the request form to become a Lightsail reseller.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/lightsail-reseller-account-console-section-become-a-reseller-initial.png)

1. On the registration form, enter your information into the fields and choose **Submit**.

![Lightsail reseller request form.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/lightsail-reseller-request-form.png)


You will receive a confirmation of your submission to your account's email regarding your interest in becoming a reseller. If your request is approved, your **Account** page in the Lightsail console will have a revised **Lightsail reseller** section with options to manage your reseller accounts and to contact the Lightsail team for feedback or queries as a Lightsail reseller. This section is only visible to the account that submitted the request to become a Lightsail reseller. You will also receive the higher service quotas for Lightsail instances and be able to request adding additional AWS accounts to become Lightsail resellers.

![Lightsail reseller section in the Lightsail console.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/lightsail-reseller-account-console-section.png)


## Request additional accounts to become Lightsail resellers
<a name="lightsail-resellers-become-a-reseller-request-additional-accounts"></a>

The following steps will submit a request for additional AWS accounts to become resellers.

**Tip**  
If you are using AWS Organizations, you should specify your management accounts as the AWS accounts to add. This approach scales the increased default Lightsail instance quotas to all of your member accounts in the organization of the management account.

**To request additional accounts to become Lightsail resellers**

1. Sign in to the [Lightsail console](https://lightsail.aws.amazon.com/).

1. On the Lightsail home page, choose your user or role on the top navigation menu.

1. Choose **Account** in the dropdown menu.  
![Lightsail account page.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-console-account-menu.png)

1. On the **Profile** tab, in the Lightsail reseller section, choose **Add accounts**.
**Important**  
The **Add accounts** action is only available to the account that requested to become a Lightsail reseller and was accepted.  
![Add additional accounts to become Lightsail resellers.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/lightsail-reseller-add-additional-accounts.png)

1. In the registration form, enter any additional AWS account IDs or management accounts for your organizations that you'd like to register.
**Note**  
If you are using Organizations, you don't need to request your member accounts.  
![Register additional accounts to become Lightsail resellers.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/lightsail-reseller-register-additional-accounts.png)

1. Choose **Submit**.