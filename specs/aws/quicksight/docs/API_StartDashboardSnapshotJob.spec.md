---
id: "@specs/aws/quicksight/docs/API_StartDashboardSnapshotJob"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS StartDashboardSnapshotJob"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# StartDashboardSnapshotJob

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_StartDashboardSnapshotJob
> **target_lang:** meta — documentation tier. ALL sections preserved.



# StartDashboardSnapshotJob
<a name="API_StartDashboardSnapshotJob"></a>

Starts an asynchronous job that generates a snapshot of a dashboard's output. You can request one or several of the following format configurations in each API call.
+ 1 PDF
+ 1 Excel workbook that includes up to 5 table or pivot table visuals
+ 5 CSVs from table or pivot table visuals

**Note**  
Exporting CSV, Excel, or Pixel Perfect PDF reports requires Pixel Perfect Report Add-on.

The status of a submitted job can be polled with the `DescribeDashboardSnapshotJob` API. When you call the `DescribeDashboardSnapshotJob` API, check the `JobStatus` field in the response. Once the job reaches a `COMPLETED` or `FAILED` status, use the `DescribeDashboardSnapshotJobResult` API to obtain the URLs for the generated files. If the job fails, the `DescribeDashboardSnapshotJobResult` API returns detailed information about the error that occurred.

 **StartDashboardSnapshotJob API throttling** 

Quick Sight utilizes API throttling to create a more consistent user experience within a time span for customers when they call the `StartDashboardSnapshotJob`. By default, 12 jobs can run simlutaneously in one AWS account and users can submit up 10 API requests per second before an account is throttled. If an overwhelming number of API requests are made by the same user in a short period of time, Quick Sight throttles the API calls to maintin an optimal experience and reliability for all Quick Sight users.

 **Common throttling scenarios** 

The following list provides information about the most commin throttling scenarios that can occur.
+  **A large number of `SnapshotExport` API jobs are running simultaneously on an AWS account.** When a new `StartDashboardSnapshotJob` is created and there are already 12 jobs with the `RUNNING` status, the new job request fails and returns a `LimitExceededException` error. Wait for a current job to comlpete before you resubmit the new job.
+  **A large number of API requests are submitted on an AWS account.** When a user makes more than 10 API calls to the Quick Sight API in one second, a `ThrottlingException` is returned.

If your use case requires a higher throttling limit, contact your account admin or [AWSSupport](http://aws.amazon.com/contact-us/) to explore options to tailor a more optimal expereince for your account.

 **Best practices to handle throttling** 

If your use case projects high levels of API traffic, try to reduce the degree of frequency and parallelism of API calls as much as you can to avoid throttling. You can also perform a timing test to calculate an estimate for the total processing time of your projected load that stays within the throttling limits of the Quick Sight APIs. For example, if your projected traffic is 100 snapshot jobs before 12:00 PM per day, start 12 jobs in parallel and measure the amount of time it takes to proccess all 12 jobs. Once you obtain the result, multiply the duration by 9, for example `(12 minutes * 9 = 108 minutes)`. Use the new result to determine the latest time at which the jobs need to be started to meet your target deadline.

The time that it takes to process a job can be impacted by the following factors:
+ The dataset type (Direct Query or SPICE).
+ The size of the dataset.
+ The complexity of the calculated fields that are used in the dashboard.
+ The number of visuals that are on a sheet.
+ The types of visuals that are on the sheet.
+ The number of formats and snapshots that are requested in the job configuration.
+ The size of the generated snapshots.

 **Registered user support** 

You can generate snapshots for registered Quick Sight users by using the Snapshot Job APIs with [identity-enhanced IAM role session credentials](https://docs.aws.amazon.com/singlesignon/latest/userguide/trustedidentitypropagation-identity-enhanced-iam-role-sessions.html). This approach allows you to create snapshots on behalf of specific Quick Sight users while respecting their row-level security (RLS), column-level security (CLS), dynamic default parameters and dashboard parameter/filter settings.

To generate snapshots for registered Quick Sight users, you need to:
+ Obtain identity-enhanced IAM role session credentials from AWS Security Token Service (STS).
+ Use these credentials to call the Snapshot Job APIs.

Identity-enhanced credentials are credentials that contain information about the end user (e.g., registered Quick Sight user).

If your Quick Sight users are backed by [AWS Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html), then you need to set up a [trusted token issuer](https://docs.aws.amazon.com/singlesignon/latest/userguide/setuptrustedtokenissuer.html). Then, getting identity-enhanced IAM credentials for a Quick Sight user will look like the following:
+ Authenticate user with your OIDC compliant Identity Provider. You should get auth tokens back.
+ Use the OIDC API, [CreateTokenWithIAM](https://docs.aws.amazon.com/singlesignon/latest/OIDCAPIReference/API_CreateTokenWithIAM.html), to exchange auth tokens to IAM tokens. One of the resulted tokens will be identity token.
+ Call STS AssumeRole API as you normally would, but provide an extra `ProvidedContexts` parameter in the API request. The list of contexts must have a single trusted context assertion. The `ProviderArn` should be `arn:aws:iam::aws:contextProvider/IdentityCenter` while `ContextAssertion` will be the identity token you received in response from CreateTokenWithIAM

For more details, see [IdC documentation on Identity-enhanced IAM role sessions](https://docs.aws.amazon.com/singlesignon/latest/userguide/trustedidentitypropagation-identity-enhanced-iam-role-sessions.html).

To obtain Identity-enhanced credentials for Quick Sight native users, IAM federated users, or Active Directory users, follow the steps below:
+ Call Quick Sight [GetIdentityContext API](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_GetIdentityContext.html) to get identity token.
+ Call STS AssumeRole API as you normally would, but provide extra `ProvidedContexts` parameter in the API request. The list of contexts must have a single trusted context assertion. The `ProviderArn` should be `arn:aws:iam::aws:contextProvider/QuickSight` while `ContextAssertion` will be the identity token you received in response from GetIdentityContext

After obtaining the identity-enhanced IAM role session credentials, you can use them to start a job, describe the job and describe job result. You can use the same credentials as long as they haven't expired. All API requests made with these credentials are considered to be made by the impersonated Quick Sight user.

**Important**  
When using identity-enhanced session credentials, set the UserConfiguration request attribute to null. Otherwise, the request will be invalid.

 **Possible error scenarios** 

The request fails with an Access Denied error in the following scenarios:
+ The credentials have expired.
+ The impersonated Quick Sight user doesn't have access to the specified dashboard.
+ The impersonated Quick Sight user is restricted from exporting data in the selected formats. For more information about export restrictions, see [Customizing access to Amazon Quick Sight capabilities](https://docs.aws.amazon.com/quicksuite/latest/userguide/create-custom-permisions-profile.html).

## Request Syntax
<a name="API_StartDashboardSnapshotJob_RequestSyntax"></a>

```
POST /accounts/{{AwsAccountId}}/dashboards/{{DashboardId}}/snapshot-jobs HTTP/1.1
Content-type: application/json

{
   "SnapshotConfiguration": { 
      "DestinationConfiguration": { 
         "S3Destinations": [ 
            { 
               "BucketConfiguration": { 
                  "BucketName": "{{string}}",
                  "BucketPrefix": "{{string}}",
                  "BucketRegion": "{{string}}"
               }
            }
         ]
      },
      "FileGroups": [ 
         { 
            "Files": [ 
               { 
                  "FormatType": "{{string}}",
                  "SheetSelections": [ 
                     { 
                        "SelectionScope": "{{string}}",
                        "SheetId": "{{string}}",
                        "VisualIds": [ "{{string}}" ]
                     }
                  ]
               }
            ]
         }
      ],
      "Parameters": { 
         "DateTimeParameters": [ 
            { 
               "Name": "{{string}}",
               "Values": [ {{number}} ]
            }
         ],
         "DecimalParameters": [ 
            { 
               "Name": "{{string}}",
               "Values": [ {{number}} ]
            }
         ],
         "IntegerParameters": [ 
            { 
               "Name": "{{string}}",
               "Values": [ {{number}} ]
            }
         ],
         "StringParameters": [ 
            { 
               "Name": "{{string}}",
               "Values": [ "{{string}}" ]
            }
         ]
      }
   },
   "SnapshotJobId": "{{string}}",
   "UserConfiguration": { 
      "AnonymousUsers": [ 
         { 
            "RowLevelPermissionTags": [ 
               { 
                  "Key": "{{string}}",
                  "Value": "{{string}}"
               }
            ]
         }
      ]
   }
}
```

## URI Request Parameters
<a name="API_StartDashboardSnapshotJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_StartDashboardSnapshotJob_RequestSyntax) **   <a name="QS-StartDashboardSnapshotJob-request-uri-AwsAccountId"></a>
The ID of the AWS account that the dashboard snapshot job is executed in.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

 ** [DashboardId](#API_StartDashboardSnapshotJob_RequestSyntax) **   <a name="QS-StartDashboardSnapshotJob-request-uri-DashboardId"></a>
The ID of the dashboard that you want to start a snapshot job for.   
Length Constraints: Minimum length of 1. Maximum length of 512.  
Pattern: `[\w\-]+`   
Required: Yes

## Request Body
<a name="API_StartDashboardSnapshotJob_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [SnapshotConfiguration](#API_StartDashboardSnapshotJob_RequestSyntax) **   <a name="QS-StartDashboardSnapshotJob-request-SnapshotConfiguration"></a>
A structure that describes the configuration of the dashboard snapshot.  
Type: [SnapshotConfiguration](API_SnapshotConfiguration.md) object  
Required: Yes

 ** [SnapshotJobId](#API_StartDashboardSnapshotJob_RequestSyntax) **   <a name="QS-StartDashboardSnapshotJob-request-SnapshotJobId"></a>
An ID for the dashboard snapshot job. This ID is unique to the dashboard while the job is running. This ID can be used to poll the status of a job with a `DescribeDashboardSnapshotJob` while the job runs. You can reuse this ID for another job 24 hours after the current job is completed.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 512.  
Pattern: `[\w\-]+`   
Required: Yes

 ** [UserConfiguration](#API_StartDashboardSnapshotJob_RequestSyntax) **   <a name="QS-StartDashboardSnapshotJob-request-UserConfiguration"></a>
A structure that contains information about the users that the dashboard snapshot is generated for. The users can be either anonymous users or registered users. Anonymous users cannot be used together with registered users.  
When using identity-enhanced session credentials, set the UserConfiguration request attribute to null. Otherwise, the request will be invalid.
Type: [SnapshotUserConfiguration](API_SnapshotUserConfiguration.md) object  
Required: No

## Response Syntax
<a name="API_StartDashboardSnapshotJob_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "Arn": "string",
   "RequestId": "string",
   "SnapshotJobId": "string"
}
```

## Response Elements
<a name="API_StartDashboardSnapshotJob_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_StartDashboardSnapshotJob_ResponseSyntax) **   <a name="QS-StartDashboardSnapshotJob-response-Status"></a>
The HTTP status of the request

The following data is returned in JSON format by the service.

 ** [Arn](#API_StartDashboardSnapshotJob_ResponseSyntax) **   <a name="QS-StartDashboardSnapshotJob-response-Arn"></a>
The Amazon Resource Name (ARN) for the dashboard snapshot job.  
Type: String

 ** [RequestId](#API_StartDashboardSnapshotJob_ResponseSyntax) **   <a name="QS-StartDashboardSnapshotJob-response-RequestId"></a>
 The AWS request ID for this operation.   
Type: String  
Pattern: `.*\S.*` 

 ** [SnapshotJobId](#API_StartDashboardSnapshotJob_ResponseSyntax) **   <a name="QS-StartDashboardSnapshotJob-response-SnapshotJobId"></a>
The ID of the job. The job ID is set when you start a new job with a `StartDashboardSnapshotJob` API call.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 512.  
Pattern: `[\w\-]+` 

## Errors
<a name="API_StartDashboardSnapshotJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
You don't have access to this item. The provided credentials couldn't be validated. You might not be authorized to carry out the request. Make sure that your account is authorized to use the Amazon Quick Sight service, that your policies have the correct permissions, and that you are using the correct credentials.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 401

 ** InternalFailureException **   
An internal failure occurred.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 500

 ** InvalidParameterValueException **   
One or more parameters has a value that isn't valid.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 400

 ** LimitExceededException **   
A limit is exceeded.    
 ** RequestId **   
The AWS request ID for this request.  
 ** ResourceType **   
Limit exceeded.
HTTP Status Code: 409

 ** ResourceExistsException **   
The resource specified already exists.     
 ** RequestId **   
The AWS request ID for this request.  
 ** ResourceType **   
The resource type for this request.
HTTP Status Code: 409

 ** ResourceNotFoundException **   
One or more resources can't be found.    
 ** RequestId **   
The AWS request ID for this request.  
 ** ResourceType **   
The resource type for this request.
HTTP Status Code: 404

 ** ThrottlingException **   
Access is throttled.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 429

 ** UnsupportedPricingPlanException **   
This error indicates that you are calling an embedding operation in Amazon Quick Sight without the required pricing plan on your AWS account. Before you can use embedding for anonymous users, a Quick Suite administrator needs to add capacity pricing to Quick Sight. You can do this on the **Manage Quick Suite** page.   
After capacity pricing is added, you can use the ` [GetDashboardEmbedUrl](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_GetDashboardEmbedUrl.html) ` API operation with the `--identity-type ANONYMOUS` option.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 403

 ** UnsupportedUserEditionException **   
This error indicates that you are calling an operation on an Amazon Quick Suite subscription where the edition doesn't include support for that operation. Amazon Quick Suite currently has Standard Edition and Enterprise Edition. Not every operation and capability is available in every edition.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 403

## See Also
<a name="API_StartDashboardSnapshotJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/StartDashboardSnapshotJob) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/StartDashboardSnapshotJob) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/StartDashboardSnapshotJob) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/StartDashboardSnapshotJob) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/StartDashboardSnapshotJob) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/StartDashboardSnapshotJob) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/StartDashboardSnapshotJob) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/StartDashboardSnapshotJob) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/StartDashboardSnapshotJob) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/StartDashboardSnapshotJob) 