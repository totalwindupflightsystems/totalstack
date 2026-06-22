---
id: "@specs/aws/appconfig/docs/appconfig-code-samples-clean-up"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Cleaning up your environment"
status: active
depends_on:
  - "@specs/aws/appconfig/meta"
---

# Cleaning up your environment

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appconfig/docs/appconfig-code-samples-clean-up
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Cleaning up your environment
<a name="appconfig-code-samples-clean-up"></a>

If you ran one or more of the code samples in this section, we recommend you use one of the following samples to locate and delete the AWS AppConfig resources created by those code samples. The samples in this section call the following APIs:
+ [ListApplications](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_ListApplications.html)
+ [DeleteApplication](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_DeleteApplication.html)
+ [ListEnvironments](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_ListEnvironments.html)
+ [DeleteEnvironments](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_DeleteEnvironment.html)
+ [ListConfigurationProfiles](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_ListConfigurationProfiles.html)
+ [DeleteConfigurationProfile](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_DeleteConfigurationProfile.html)
+ [ListHostedConfigurationVersions](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_ListHostedConfigurationVersions.html)
+ [DeleteHostedConfigurationVersion](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_DeleteHostedConfigurationVersion.html)

------
#### [ Java ]

```
/*
    This sample provides cleanup code that deletes all the AWS AppConfig resources created in the samples above.

    WARNING: this code will permanently delete the given application and all of its sub-resources, including
    configuration profiles, hosted configuration versions, and environments. DO NOT run this code against
    an application that you may need in the future.
    */
    
    public void cleanUpDemoResources() {
        AppConfigClient appconfig = AppConfigClient.create();
        
        // The name of the application to delete
        // IMPORTANT: verify this name corresponds to the application you wish to delete
        String applicationToDelete = "MyDemoApp";
        
        appconfig.listApplicationsPaginator(ListApplicationsRequest.builder().build()).items().forEach(app -> {
            if (app.name().equals(applicationToDelete)) {
                System.out.println("Deleting App: " + app);
                appconfig.listConfigurationProfilesPaginator(req -> req.applicationId(app.id())).items().forEach(cp -> {
                    System.out.println("Deleting Profile: " + cp);
                    appconfig
                        .listHostedConfigurationVersionsPaginator(req -> req
                            .applicationId(app.id())
                            .configurationProfileId(cp.id()))
                        .items()
                        .forEach(hcv -> {
                            System.out.println("Deleting HCV: " + hcv);
                            appconfig.deleteHostedConfigurationVersion(req -> req
                                .applicationId(app.id())
                                .configurationProfileId(cp.id())
                                .versionNumber(hcv.versionNumber()));
                        });
                    appconfig.deleteConfigurationProfile(req -> req
                        .applicationId(app.id())
                        .configurationProfileId(cp.id()));
                });

                appconfig.listEnvironmentsPaginator(req->req.applicationId(app.id())).items().forEach(env -> {
                    System.out.println("Deleting Environment: " + env);
                    appconfig.deleteEnvironment(req->req.applicationId(app.id()).environmentId(env.id()));
                });

                appconfig.deleteApplication(req -> req.applicationId(app.id()));
            }
        });
    }
```

------
#### [ Python ]

```
# this sample provides cleanup code that deletes all the AWS AppConfig resources created in the samples above.
#
# WARNING: this code will permanently delete the given application and all of its sub-resources, including
#   configuration profiles, hosted configuration versions, and environments. DO NOT run this code against
#   an application that you may need in the future.
#

import boto3 

# the name of the application to delete
# IMPORTANT: verify this name corresponds to the application you wish to delete
application_name = 'MyDemoApp'

# create and iterate over a list paginator such that we end up with a list of pages, which are themselves lists of applications
# e.g. [ [{'Name':'MyApp1',...},{'Name':'MyApp2',...}], [{'Name':'MyApp3',...}] ]
list_of_app_lists = [page['Items'] for page in appconfig.get_paginator('list_applications').paginate()]
# retrieve the target application from the list of lists
application = [app for apps in list_of_app_lists for app in apps if app['Name'] == application_name][0]
print(f"deleting application {application['Name']} (id={application['Id']})")

# delete all configuration profiles
list_of_config_lists = [page['Items'] for page in appconfig.get_paginator('list_configuration_profiles').paginate(ApplicationId=application['Id'])]
for config_profile in [config for configs in list_of_config_lists for config in configs]:
    print(f"\tdeleting configuration profile {config_profile['Name']} (Id={config_profile['Id']})")

    # delete all hosted configuration versions
    list_of_hcv_lists = [page['Items'] for page in appconfig.get_paginator('list_hosted_configuration_versions').paginate(ApplicationId=application['Id'], ConfigurationProfileId=config_profile['Id'])]
    for hcv in [hcv for hcvs in list_of_hcv_lists for hcv in hcvs]:
        appconfig.delete_hosted_configuration_version(ApplicationId=application['Id'], ConfigurationProfileId=config_profile['Id'], VersionNumber=hcv['VersionNumber'])
        print(f"\t\tdeleted hosted configuration version {hcv['VersionNumber']}")

    # delete the config profile itself
    appconfig.delete_configuration_profile(ApplicationId=application['Id'], ConfigurationProfileId=config_profile['Id'])
    print(f"\tdeleted configuration profile {config_profile['Name']} (Id={config_profile['Id']})")

# delete all environments
list_of_env_lists = [page['Items'] for page in appconfig.get_paginator('list_environments').paginate(ApplicationId=application['Id'])]
for environment in [env for envs in list_of_env_lists for env in envs]:
    appconfig.delete_environment(ApplicationId=application['Id'], EnvironmentId=environment['Id'])
    print(f"\tdeleted environment {environment['Name']} (Id={environment['Id']})")

# delete the application itself
appconfig.delete_application(ApplicationId=application['Id'])
print(f"deleted application {application['Name']} (id={application['Id']})")
```

------
#### [ JavaScript ]

```
// this sample provides cleanup code that deletes all the AWS AppConfig resources created in the samples above.

// WARNING: this code will permanently delete the given application and all of its sub-resources, including
//   configuration profiles, hosted configuration versions, and environments. DO NOT run this code against
//   an application that you may need in the future.

import {
  AppConfigClient,
  paginateListApplications,
  DeleteApplicationCommand,
  paginateListConfigurationProfiles,
  DeleteConfigurationProfileCommand,
  paginateListHostedConfigurationVersions,
  DeleteHostedConfigurationVersionCommand,
  paginateListEnvironments,
  DeleteEnvironmentCommand,
} from "@aws-sdk/client-appconfig";

const client = new AppConfigClient();

// the name of the application to delete
// IMPORTANT: verify this name corresponds to the application you wish to delete
const application_name = "MyDemoApp";

// iterate over all applications, deleting ones that have the name defined above
for await (const app_page of paginateListApplications({ client }, {})) {
  for (const application of app_page.Items) {

    // skip applications that dont have the name thats set
    if (application.Name !== application_name) continue;

    console.log( `deleting application ${application.Name} (id=${application.Id})`);

    // delete all configuration profiles
    for await (const config_page of paginateListConfigurationProfiles({ client }, { ApplicationId: application.Id })) {
      for (const config_profile of config_page.Items) {
        console.log(`\tdeleting configuration profile ${config_profile.Name} (Id=${config_profile.Id})`);

        // delete all hosted configuration versions
        for await (const hosted_page of paginateListHostedConfigurationVersions({ client },
          { ApplicationId: application.Id, ConfigurationProfileId: config_profile.Id }
        )) {
          for (const hosted_config_version of hosted_page.Items) {
            await client.send(
              new DeleteHostedConfigurationVersionCommand({
                ApplicationId: application.Id,
                ConfigurationProfileId: config_profile.Id,
                VersionNumber: hosted_config_version.VersionNumber,
              })
            );
            console.log(`\t\tdeleted hosted configuration version ${hosted_config_version.VersionNumber}`);
          }
        }

        // delete the config profile itself
        await client.send(
          new DeleteConfigurationProfileCommand({
            ApplicationId: application.Id,
            ConfigurationProfileId: config_profile.Id,
          })
        );
        console.log(`\tdeleted configuration profile ${config_profile.Name} (Id=${config_profile.Id})`)
      }

      // delete all environments
      for await (const env_page of paginateListEnvironments({ client }, { ApplicationId: application.Id })) {
        for (const environment of env_page.Items) {
          await client.send(
            new DeleteEnvironmentCommand({
              ApplicationId: application.Id,
              EnvironmentId: environment.Id,
            })
          );
          console.log(`\tdeleted environment ${environment.Name} (Id=${environment.Id})`)
        }
      }
    }

    // delete the application itself
    await client.send(
      new DeleteApplicationCommand({ ApplicationId: application.Id })
    );
    console.log(`deleted application ${application.Name} (id=${application.Id})`)
  }
}
```

------