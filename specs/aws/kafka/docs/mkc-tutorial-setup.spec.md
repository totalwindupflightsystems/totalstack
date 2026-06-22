---
id: "@specs/aws/kafka/docs/mkc-tutorial-setup"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Set up resources required for MSK Connect"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Set up resources required for MSK Connect

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/mkc-tutorial-setup
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Set up resources required for MSK Connect
<a name="mkc-tutorial-setup"></a>

In this step you create the following resources that you need for this getting-started scenario:
+ An Amazon S3 bucket to serve as the destination that receives data from the connector.
+ An MSK cluster to which you will send data. The connector will then read the data from this cluster and send it to the destination S3 bucket.
+ An IAM policy that contains the permissions to write to the destination S3 bucket.
+ An IAM role that allows the connector to write to the destination S3 bucket. You'll add the IAM policy that you create to this role.
+ An Amazon VPC endpoint to make it possible to send data from the Amazon VPC that has the cluster and the connector to Amazon S3.

**To create the S3 bucket**

1. Sign in to the AWS Management Console and open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. Choose **Create bucket**.

1. For the name of the bucket, enter a descriptive name such as `amzn-s3-demo-bucket-mkc-tutorial`.

1. Scroll down and choose **Create bucket**.

1. In the list of buckets, choose the newly created bucket.

1. Choose **Create folder**.

1. Enter `tutorial` for the name of the folder, then scroll down and choose **Create folder**.

**To create the cluster**

1. Open the Amazon MSK console at [https://console.aws.amazon.com/msk/home?region=us-east-1\#/home/](https://console.aws.amazon.com/msk/home?region=us-east-1#/home/).

1. In the left pane, under **MSK Clusters**, choose **Clusters**.

1. Choose **Create cluster**.

1. In **Creation method**, choose **Custom create**.

1. For the cluster name enter **mkc-tutorial-cluster**.

1. In **Cluster type**, choose **Provisioned**.

1. Choose **Next**.

1. Under **Networking**, choose an Amazon VPC. Then select the Availability Zones and subnets that you want to use. Remember the IDs of the Amazon VPC and subnets that you selected because you need them later in this tutorial.

1. Choose **Next**.

1. Under **Access control methods** ensure that only **Unauthenticated access** is selected.

1. Under **Encryption** ensure that only **Plaintext** is selected.

1. Continue through the wizard and then choose **Create cluster**. This takes you to the details page for the cluster. On that page, under **Security groups applied**, find the security group ID. Remember that ID because you need it later in this tutorial.

**To create an IAM policy with permissions to write to the S3 bucket**

1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. On the navigation pane, choose **Policies**.

1. Choose **Create policy**.

1. In **Policy editor**, choose **JSON**, and then replace the JSON in the editor window with the following JSON.

   In the following example, replace {{<amzn-s3-demo-bucket-my-tutorial>}} with the name of your S3 bucket.

------
#### [ JSON ]

****  

   ```
   {
     "Version":"2012-10-17",		 	 	 
     "Statement": [
       {
         "Sid": "AllowListBucket",
         "Effect": "Allow",
         "Action": [
           "s3:ListBucket",
           "s3:GetBucketLocation"
         ],
         "Resource": "arn:aws:s3:::{{<amzn-s3-demo-bucket-my-tutorial>}}"
       },
       {
         "Sid": "AllowObjectActions",
         "Effect": "Allow",
         "Action": [
           "s3:PutObject",
           "s3:GetObject",
           "s3:DeleteObject",
           "s3:AbortMultipartUpload",
           "s3:ListMultipartUploadParts",
           "s3:ListBucketMultipartUploads"
         ],
         "Resource": "arn:aws:s3:::{{<amzn-s3-demo-bucket-my-tutorial>}}/*"
       }
     ]
   }
   ```

------

   For instructions about how to write secure policies, see [IAM access control](iam-access-control.md).

1. Choose **Next**.

1. On the **Review and create** page, do the following:

   1. For **Policy name**, enter a descriptive name, such as **mkc-tutorial-policy**.

   1. In **Permissions defined in this policy**, review and/or edit the permissions defined in your policy.

   1. (Optional) To help identify, organize, or search for the policy, choose **Add new tag** to add tags as key-value pairs. For example, add a tag to your policy with the key-value pair of **Environment** and **Test**.

      For more information about using tags, see [Tags for AWS Identity and Access Management resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html) in the *IAM User Guide*.

1. Choose **Create policy**.

**To create the IAM role that can write to the destination bucket**

1. On the navigation pane of the IAM console, choose **Roles**, and then choose **Create role**.

1. On the **Select trusted entity** page, do the following:

   1. For **Trusted entity type**, choose **AWS service**.

   1. For **Service or use case**, choose **S3**.

   1. Under **Use case**, choose **S3**.

1. Choose **Next**.

1. On the **Add permissions** page, do the following:

   1. In the search box under **Permissions policies**, enter the name of the policy that you previously created for this tutorial. For example, **mkc-tutorial-policy**. Then, choose the box to the left of the policy name.

   1. (Optional) Set a [permissions boundary](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html). This is an advanced feature that is available for service roles, but not service-linked roles. For information about setting a permissions boundary, see [Creating roles and attaching policies (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions_create-policies.html) in the *IAM User Guide*.

1. Choose **Next**.

1. On the **Name, review, and create** page, do the following:

   1. For **Role name**, enter a descriptive name, such as **mkc-tutorial-role**.
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

**To allow MSK Connect to assume the role**

1. In the IAM console, in the left pane, under **Access management**, choose **Roles**.

1. Find the `mkc-tutorial-role` and choose it.

1. Under the role's **Summary**, choose the **Trust relationships** tab.

1. Choose **Edit trust relationship**.

1. Replace the existing trust policy with the following JSON.

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
           "Service": "kafkaconnect.amazonaws.com"
         },
         "Action": "sts:AssumeRole"
       }
     ]
   }
   ```

------

1. Choose **Update Trust Policy**.

**To create an Amazon VPC endpoint from the cluster's VPC to Amazon S3**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the left pane, choose **Endpoints**.

1. Choose **Create endpoint**.

1. Under **Service Name** choose the **com.amazonaws.us-east-1.s3** service and the **Gateway** type.

1. Choose the cluster's VPC and then select the box to the left of the route table that is associated with the cluster's subnets.

1. Choose **Create endpoint**.

**Next Step**

[Create custom plugin](mkc-create-plugin.md)