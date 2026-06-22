---
id: "@specs/aws/appconfig/docs/appconfig-code-samples-secrets-manager"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Creating a configuration profile for a secret stored in Secrets Manager"
status: active
depends_on:
  - "@specs/aws/appconfig/meta"
---

# Creating a configuration profile for a secret stored in Secrets Manager

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appconfig/docs/appconfig-code-samples-secrets-manager
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Creating a configuration profile for a secret stored in Secrets Manager
<a name="appconfig-code-samples-secrets-manager"></a>

Each of the following samples includes comments about the actions performed by the code. The samples in this section call the following APIs:
+ [CreateApplication](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_CreateApplication.html)
+ [CreateConfigurationProfile](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_CreateConfigurationProfile.html)

------
#### [ Java ]

```
private void createSecretsManagerConfigProfile() {
        AppConfigClient appconfig = AppConfigClient.create();

        // Create an application
        CreateApplicationResponse app = appconfig.createApplication(req -> req.name("MyDemoApp"));

        // Create a configuration profile for Secrets Manager Secret
        CreateConfigurationProfileResponse configProfile = appconfig.createConfigurationProfile(req -> req
            .applicationId(app.id())
            .name("MyConfigProfile")
            .locationUri("secretsmanager://MySecret")
            .retrievalRoleArn("arn:aws:iam::000000000000:role/RoleTrustedByAppConfigThatCanRetrieveSecret")
            .type("AWS.Freeform"));
    }
```

------
#### [ Python ]

```
import boto3

appconfig = boto3.client('appconfig')

# create an application
application = appconfig.create_application(Name='MyDemoApp')

# create a configuration profile for Secrets Manager Secret
config_profile = appconfig.create_configuration_profile(
    ApplicationId=application['Id'],
    Name='MyConfigProfile',
    LocationUri='secretsmanager://MySecret',
    RetrievalRoleArn='arn:aws:iam::000000000000:role/RoleTrustedByAppConfigThatCanRetrieveSecret',
    Type='AWS.Freeform')
```

------
#### [ JavaScript ]

```
import {
  AppConfigClient,
  CreateConfigurationProfileCommand,
} from "@aws-sdk/client-appconfig";

const appconfig = new AppConfigClient();

// create an application
const application = await appconfig.send(
  new CreateApplicationCommand({ Name: "MyDemoApp" })
);

// create a configuration profile for Secrets Manager Secret
await appconfig.send(
  new CreateConfigurationProfileCommand({
    ApplicationId: application.Id,
    Name: "MyConfigProfile",
    LocationUri: "secretsmanager://MySecret",
    RetrievalRoleArn: "arn:aws:iam::000000000000:role/RoleTrustedByAppConfigThatCanRetrieveSecret",
    Type: "AWS.Freeform",
  })
);
```

------