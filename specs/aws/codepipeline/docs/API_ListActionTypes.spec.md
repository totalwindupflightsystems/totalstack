---
id: "@specs/aws/codepipeline/docs/API_ListActionTypes"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListActionTypes"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# ListActionTypes

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_ListActionTypes
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListActionTypes
<a name="API_ListActionTypes"></a>

Gets a summary of all CodePipeline action types associated with your account.

## Request Syntax
<a name="API_ListActionTypes_RequestSyntax"></a>

```
{
   "actionOwnerFilter": "{{string}}",
   "nextToken": "{{string}}",
   "regionFilter": "{{string}}"
}
```

## Request Parameters
<a name="API_ListActionTypes_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [actionOwnerFilter](#API_ListActionTypes_RequestSyntax) **   <a name="CodePipeline-ListActionTypes-request-actionOwnerFilter"></a>
Filters the list of action types to those created by a specified entity.  
Type: String  
Valid Values: `AWS | ThirdParty | Custom`   
Required: No

 ** [nextToken](#API_ListActionTypes_RequestSyntax) **   <a name="CodePipeline-ListActionTypes-request-nextToken"></a>
An identifier that was returned from the previous list action types call, which can be used to return the next set of action types in the list.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Required: No

 ** [regionFilter](#API_ListActionTypes_RequestSyntax) **   <a name="CodePipeline-ListActionTypes-request-regionFilter"></a>
The Region to filter on for the list of action types.  
Type: String  
Length Constraints: Minimum length of 4. Maximum length of 30.  
Required: No

## Response Syntax
<a name="API_ListActionTypes_ResponseSyntax"></a>

```
{
   "actionTypes": [ 
      { 
         "actionConfigurationProperties": [ 
            { 
               "description": "string",
               "key": boolean,
               "name": "string",
               "queryable": boolean,
               "required": boolean,
               "secret": boolean,
               "type": "string"
            }
         ],
         "id": { 
            "category": "string",
            "owner": "string",
            "provider": "string",
            "version": "string"
         },
         "inputArtifactDetails": { 
            "maximumCount": number,
            "minimumCount": number
         },
         "outputArtifactDetails": { 
            "maximumCount": number,
            "minimumCount": number
         },
         "settings": { 
            "entityUrlTemplate": "string",
            "executionUrlTemplate": "string",
            "revisionUrlTemplate": "string",
            "thirdPartyConfigurationUrl": "string"
         }
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListActionTypes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [actionTypes](#API_ListActionTypes_ResponseSyntax) **   <a name="CodePipeline-ListActionTypes-response-actionTypes"></a>
Provides details of the action types.  
Type: Array of [ActionType](API_ActionType.md) objects

 ** [nextToken](#API_ListActionTypes_ResponseSyntax) **   <a name="CodePipeline-ListActionTypes-response-nextToken"></a>
If the amount of returned information is significantly large, an identifier is also returned. It can be used in a subsequent list action types call to return the next set of action types in the list.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Errors
<a name="API_ListActionTypes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidNextTokenException **   
The next token was specified in an invalid format. Make sure that the next token you provide is the token returned by a previous call.  
HTTP Status Code: 400

 ** ValidationException **   
The validation was specified in an invalid format.  
HTTP Status Code: 400

## Examples
<a name="API_ListActionTypes_Examples"></a>

### Example
<a name="API_ListActionTypes_Example_1"></a>

This example illustrates one usage of ListActionTypes.

#### Sample Request
<a name="API_ListActionTypes_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: codepipeline.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 2
X-Amz-Target: CodePipeline_20150709.ListActionTypes
X-Amz-Date: 20160707T160551Z
User-Agent: aws-cli/1.7.38 Python/2.7.9 Windows/7
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAI44QH8DHBEXAMPLE/20160707/us-east-1/codepipeline/aws4_request, SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=8d9b5998EXAMPLE

{}
```

#### Sample Response
<a name="API_ListActionTypes_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 620484b7-88cb-11e5-b497-75c49EXAMPLE
Content-Type: application/x-amz-json-1.1
Content-Length: 8363

{
    "actionTypes": [
        {
            "inputArtifactDetails": {
                "maximumCount": 0, 
                "minimumCount": 0
            }, 
            "actionConfigurationProperties": [
                {
                    "description": "The S3 Bucket", 
                    "required": true, 
                    "secret": false, 
                    "key": true, 
                    "queryable": false, 
                    "name": "S3Bucket"
                }, 
                {
                    "description": "The Amazon S3 object key", 
                    "required": true, 
                    "secret": false, 
                    "key": true, 
                    "queryable": false, 
                    "name": "S3ObjectKey"
                }
            ], 
            "outputArtifactDetails": {
                "maximumCount": 1, 
                "minimumCount": 1
            }, 
            "id": {
                "category": "Source", 
                "owner": "AWS", 
                "version": "1", 
                "provider": "S3"
            }, 
            "settings": {
                "entityUrlTemplate": "https://console.aws.amazon.com/s3/home?#"
            }
        }, 
        {
            "inputArtifactDetails": {
                "maximumCount": 1, 
                "minimumCount": 1
            }, 
            "actionConfigurationProperties": [
                {
                    "description": "The Elastic Beanstalk Application name", 
                    "required": true, 
                    "secret": false, 
                    "key": true, 
                    "queryable": false, 
                    "name": "ApplicationName"
                }, 
                {
                    "description": "The Elastic Beanstalk Environment name", 
                    "required": true, 
                    "secret": false, 
                    "key": true, 
                    "queryable": false, 
                    "name": "EnvironmentName"
                }
            ], 
            "outputArtifactDetails": {
                "maximumCount": 0, 
                "minimumCount": 0
            }, 
            "id": {
                "category": "Deploy", 
                "owner": "AWS", 
                "version": "1", 
                "provider": "ElasticBeanstalk"
            }, 
            "settings": {
                "entityUrlTemplate": "https://console.aws.amazon.com/elasticbeanstalk/r/application/{Config:ApplicationName}", 
                "executionUrlTemplate": "https://console.aws.amazon.com/elasticbeanstalk/r/application/{Config:ApplicationName}"
            }
        }, 
        {
            "inputArtifactDetails": {
                "maximumCount": 1, 
                "minimumCount": 1
            }, 
            "actionConfigurationProperties": [
                {
                    "description": "The deployment application name", 
                    "required": true, 
                    "secret": false, 
                    "key": true, 
                    "queryable": false, 
                    "name": "ApplicationName"
                }, 
                {
                    "description": "The deployment group name", 
                    "required": true, 
                    "secret": false, 
                    "key": true, 
                    "queryable": false, 
                    "name": "DeploymentGroupName"
                }
            ], 
            "outputArtifactDetails": {
                "maximumCount": 0, 
                "minimumCount": 0
            }, 
            "id": {
                "category": "Deploy", 
                "owner": "AWS", 
                "version": "1", 
                "provider": "CodeDeploy"
            }, 
            "settings": {
                "entityUrlTemplate": "https://console.aws.amazon.com/codedeploy/home?#/applications/{Config:ApplicationName}/deployment-groups/{Config:DeploymentGroupName}", 
                "executionUrlTemplate": "https://console.aws.amazon.com/codedeploy/home?#/deployments/{ExternalExecutionId}"
            }
        }, 
        {
            "inputArtifactDetails": {
                "maximumCount": 0, 
                "minimumCount": 0
            }, 
            "actionConfigurationProperties": [
                {
                    "description": "The repository owner (username or organization)", 
                    "required": true, 
                    "secret": false, 
                    "key": true, 
                    "queryable": false, 
                    "name": "Owner"
                }, 
                {
                    "description": "The name of the repository", 
                    "required": true, 
                    "secret": false, 
                    "key": true, 
                    "queryable": false, 
                    "name": "Repo"
                }, 
                {
                    "description": "The tracked branch", 
                    "required": true, 
                    "secret": false, 
                    "key": true, 
                    "queryable": false, 
                    "name": "Branch"
                }, 
                {
                    "description": "The OAuth2 token", 
                    "required": true, 
                    "secret": true, 
                    "key": false, 
                    "queryable": false, 
                    "name": "OAuthToken"
                }
            ], 
            "outputArtifactDetails": {
                "maximumCount": 1, 
                "minimumCount": 1
            }, 
            "id": {
                "category": "Source", 
                "owner": "ThirdParty", 
                "version": "1", 
                "provider": "GitHub"
            }, 
            "settings": {
                "entityUrlTemplate": "https://github.com/{Config:Owner}/{Config:Repo}/tree/{Config:Branch}", 
                "revisionUrlTemplate": "https://github.com/{Config:Owner}/{Config:Repo}/commit/{RevisionId}"
            }
        }, 
        {
            "inputArtifactDetails": {
                "maximumCount": 5, 
                "minimumCount": 0
            }, 
            "actionConfigurationProperties": [
                {
                    "secret": false, 
                    "required": true, 
                    "name": "JenkinsBuildProject", 
                    "key": true, 
                    "queryable": true
                }
            ], 
            "outputArtifactDetails": {
                "maximumCount": 5, 
                "minimumCount": 0
            }, 
            "id": {
                "category": "Build", 
                "owner": "Custom", 
                "version": "1", 
                "provider": "JenkinsProviderName"
            }, 
            "settings": {
                "entityUrlTemplate": "http://192.0.2.4/job/{Config:ProjectName}", 
                "executionUrlTemplate": "http://192.0.2.4/job/{Config:ProjectName}/{ExternalExecutionId}"
            }
        }, 
        {
            "inputArtifactDetails": {
                "maximumCount": 5, 
                "minimumCount": 0
            }, 
            "actionConfigurationProperties": [
                {
                    "secret": false, 
                    "required": true, 
                    "name": "JenkinsTestProject", 
                    "key": true, 
                    "queryable": true
                }
            ], 
            "outputArtifactDetails": {
                "maximumCount": 5, 
                "minimumCount": 0
            }, 
            "id": {
                "category": "Test", 
                "owner": "Custom", 
                "version": "1", 
                "provider": "JenkinsProviderName"
            }, 
            "settings": {
                "entityUrlTemplate": "http://192.0.2.4/job/{Config:ProjectName}", 
                "executionUrlTemplate": "http://192.0.2.4/job/{Config:ProjectName}/{ExternalExecutionId}"
            }
        }
    ]
}
```

## See Also
<a name="API_ListActionTypes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codepipeline-2015-07-09/ListActionTypes) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codepipeline-2015-07-09/ListActionTypes) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/ListActionTypes) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codepipeline-2015-07-09/ListActionTypes) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/ListActionTypes) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codepipeline-2015-07-09/ListActionTypes) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codepipeline-2015-07-09/ListActionTypes) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codepipeline-2015-07-09/ListActionTypes) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codepipeline-2015-07-09/ListActionTypes) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/ListActionTypes) 