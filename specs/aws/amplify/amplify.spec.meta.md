# Amplify meta spec

AWS Amplify — frontend hosting and CI/CD. Entity hierarchy:

- App (root) — CreateApp(name), GetApp(appId), ListApps, DeleteApp(appId), UpdateApp(appId)
- Branch (child of App) — CreateBranch(appId, branchName), GetBranch, ListBranches, DeleteBranch, UpdateBranch
- BackendEnvironment (child of App) — CreateBackendEnvironment(appId, environmentName), Get, List, Delete
- DomainAssociation (child of App) — CreateDomainAssociation(appId, domainName, subDomainSettings), Get, List, Delete, Update
- Webhook (child of App) — CreateWebhook(appId, branchName), Get(webhookId), List, Delete, Update
- Tags — TagResource, UntagResource, ListTagsForResource
