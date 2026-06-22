---
id: "@specs/aws/appconfig/docs/appconfig-creating-configuration-and-profile-iam-role"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Understanding the configuration profile IAM role"
status: active
depends_on:
  - "@specs/aws/appconfig/meta"
---

# Understanding the configuration profile IAM role

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appconfig/docs/appconfig-creating-configuration-and-profile-iam-role
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Understanding the configuration profile IAM role
<a name="appconfig-creating-configuration-and-profile-iam-role"></a>

You can create the IAM role that provides access to the configuration data by using AWS AppConfig. Or you can create the IAM role yourself. If you create the role by using AWS AppConfig, the system creates the role and specifies one of the following permissions policies, depending on which type of configuration source you choose.

 **Configuration source is a Secrets Manager secret** 

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
                "secretsmanager:GetSecretValue"
             ],
            "Resource": [
                "arn:aws:secretsmanager:{{us-east-1}}:{{111122223333}}:secret:{{secret_name-a1b2c3}}"
            ]
        }
    ]
}
```

------

 **Configuration source is a Parameter Store parameter** 

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
                "ssm:GetParameter"
            ],
            "Resource": [
                "arn:aws:ssm:{{us-east-1}}:{{111122223333}}:parameter/{{parameter_name}}"
            ]
        }
    ]
    }
```

------

 **Configuration source is an SSM document** 

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
                "ssm:GetDocument"
            ],
            "Resource": [
                "arn:aws:ssm:{{us-east-1}}:{{111122223333}}:document/{{document_name}}"
            ]
        }
    ]
}
```

------

If you create the role by using AWS AppConfig, the system also creates the following trust relationship for the role. 

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