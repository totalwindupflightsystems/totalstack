---
id: "@specs/aws/appconfig/docs/working-with-appconfig-extensions-creating-custom-permissions"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Step 2: Configure permissions for a custom AWS AppConfig extension"
status: active
depends_on:
  - "@specs/aws/appconfig/meta"
---

# Step 2: Configure permissions for a custom AWS AppConfig extension

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appconfig/docs/working-with-appconfig-extensions-creating-custom-permissions
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Step 2: Configure permissions for a custom AWS AppConfig extension
<a name="working-with-appconfig-extensions-creating-custom-permissions"></a>

Use the following procedure to create and configure an AWS Identity and Access Management (IAM) service role (or *assume role*). AWS AppConfig uses this role to invoke the Lambda function.

**To create an IAM service role and allow AWS AppConfig to assume it**

1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane, choose **Roles**, and then choose **Create role**.

1. Under **Select type of trusted entity**, choose **Custom trust policy**.

1. Paste the following JSON policy into the **Custom trust policy** field.

------
#### [ JSON ]

****  

   ```
   {
     "Version":"2012-10-17",		 	 	 
     "Statement": [
       {
         "Effect": "Allow",
         "Principal": {
           "Service": "appconfig.amazonaws.com"
         },
         "Action": "sts:AssumeRole"
       }
     ]
   }
   ```

------

   Choose **Next**.

1. On the **Add permissions** page, choose **Create policy**. The **Create policy** page opens in a new tab.

1. Choose the **JSON** tab, and then paste the following permission policy into the editor. The `lambda:InvokeFunction` action is used for `PRE_*` action points. The `lambda:InvokeAsync` action is used for `ON_*` action points. Replace {{Your Lambda ARN}} with the Amazon Resource Name (ARN) of your Lambda.

------
#### [ JSON ]

****  

   ```
   {
     "Version":"2012-10-17",		 	 	 
     "Statement": [
       {
         "Sid": "VisualEditor0",
         "Effect": "Allow",
         "Action": [
           "lambda:InvokeFunction",
           "lambda:InvokeAsync"
         ],
         "Resource": "arn:aws:lambda:{{us-east-1}}:{{111122223333}}:function:{{function-name}}"
       }
     ]
   }
   ```

------

1. Choose **Next: Tags**.

1. On the **Add tags (Optional)** page, add one or more key-value pairs and then choose **Next: Review**.

1. On the **Review policy** page enter a name and a description, and then choose **Create policy**.

1. On the browser tab for your custom trust policy, choose the Refresh icon and then search for the permission policy you just created.

1. Select the check box for your permission policy and then choose **Next**.

1. On the **Name, review, and create** page, enter a name in the **Role name** box, and then enter a description.

1. Choose **Create role**. The system returns you to the **Roles** page. Choose **View role** in the banner.

1. Copy the ARN. You specify this ARN when you create the extension.