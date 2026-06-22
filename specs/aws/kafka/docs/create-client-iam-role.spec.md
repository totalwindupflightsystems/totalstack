---
id: "@specs/aws/kafka/docs/create-client-iam-role"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Create an IAM role"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Create an IAM role

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/create-client-iam-role
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Step 2: Create an IAM role granting access to create topics on the Amazon MSK cluster
<a name="create-client-iam-role"></a>

In this step, you perform two tasks. The first task is to create an IAM policy that grants access to create topics on the cluster and to send data to those topics. The second task is to create an IAM role and associate this policy with it. In a later step, you create a client machine that assumes this role and uses it to create a topic on the cluster and to send data to that topic.

**To create an IAM policy that makes it possible to create topics and write to them**Create an IAM policy

1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. On the navigation pane, choose **Policies**.

1. Choose **Create policy**.

1. In **Policy editor**, choose **JSON**, and then replace the JSON in the editor window with the following JSON.

   In the following example, replace the following:
   + {{region}} with the code of the AWS Region where you created your cluster.
   + Example account ID, {{123456789012}}, with your AWS account ID.
   + {{MSKTutorialCluster}} and {{MSKTutorialCluster}}/{{7d7131e1-25c5-4e9a-9ac5-ea85bee4da11-14}}, with the name of your cluster and its ID.

------
#### [ JSON ]

****  

   ```
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": [
           {
               "Effect": "Allow",
               "Action": [
                   "kafka-cluster:Connect",
                   "kafka-cluster:AlterCluster",
                   "kafka-cluster:DescribeCluster"
               ],
               "Resource": [
                   "arn:aws:kafka:{{us-east-1}}:{{123456789012}}:cluster/{{MSKTutorialCluster}}/{{7d7131e1-25c5-4e9a-9ac5-ea85bee4da11-14}}"
               ]
           },
           {
               "Effect": "Allow",
               "Action": [
                   "kafka-cluster:*Topic*",
                   "kafka-cluster:WriteData",
                   "kafka-cluster:ReadData"
               ],
               "Resource": [
               "arn:aws:kafka:{{us-east-1}}:{{123456789012}}:topic/{{MSKTutorialCluster}}/*"
               ]
           },
           {
               "Effect": "Allow",
               "Action": [
                   "kafka-cluster:AlterGroup",
                   "kafka-cluster:DescribeGroup"
               ],
               "Resource": [
               "arn:aws:kafka:{{us-east-1}}:{{123456789012}}:group/{{MSKTutorialCluster}}/*"
               ]
           }
       ]
   }
   ```

------

   For instructions about how to write secure policies, see [IAM access control](iam-access-control.md).

1. Choose **Next**.

1. On the **Review and create** page, do the following:

   1. For **Policy name**, enter a descriptive name, such as **msk-tutorial-policy**.

   1. In **Permissions defined in this policy**, review and/or edit the permissions defined in your policy.

   1. (Optional) To help identify, organize, or search for the policy, choose **Add new tag** to add tags as key-value pairs. For example, add a tag to your policy with the key-value pair of **Environment** and **Test**.

      For more information about using tags, see [Tags for AWS Identity and Access Management resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html) in the *IAM User Guide*.

1. Choose **Create policy**.

**To create an IAM role and attach the policy to it**

1. On the navigation pane, choose **Roles**, and then choose **Create role**.

1. On the **Select trusted entity** page, do the following:

   1. For **Trusted entity type**, choose **AWS service**.

   1. For **Service or use case**, choose **EC2**.

   1. Under **Use case**, choose **EC2**.

1. Choose **Next**.

1. On the **Add permissions** page, do the following:

   1. In the search box under **Permissions policies**, enter the name of the policy that you previously created for this tutorial. Then, choose the box to the left of the policy name.

   1. (Optional) Set a [permissions boundary](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html). This is an advanced feature that is available for service roles, but not service-linked roles. For information about setting a permissions boundary, see [Creating roles and attaching policies (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions_create-policies.html) in the *IAM User Guide*.

1. Choose **Next**.

1. On the **Name, review, and create** page, do the following:

   1. For **Role name**, enter a descriptive name, such as **msk-tutorial-role**.
**Important**  
When you name a role, note the following:  
Role names must be unique within your AWS account, and can't be made unique by case.  
For example, don't create roles named both **PRODROLE** and **prodrole**. When a role name is used in a policy or as part of an ARN, the role name is case sensitive, however when a role name appears to customers in the console, such as during the sign-in process, the role name is case insensitive.
You can't edit the name of the role after it's created because other entities might reference the role.

   1. (Optional) For **Description**, enter a description for the role.

   1. (Optional) To edit the use cases and permissions for the role, in **Step 1: Select trusted entities** or **Step 2: Add permissions** sections, choose **Edit**.

   1. (Optional) To help identify, organize, or search for the role, choose **Add new tag** to add tags as key-value pairs. For example, add a tag to your role with the key-value pair of **ProductManager** and **John**.

      For more information about using tags, see [Tags for AWS Identity and Access Management resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html) in the *IAM User Guide*.

1. Review the role, and then choose **Create role**.

**Next Step**

[Step 3: Create a client machine](create-client-machine.md)