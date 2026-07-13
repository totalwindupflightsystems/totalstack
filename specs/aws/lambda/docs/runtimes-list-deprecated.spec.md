---
id: "@specs/aws/lambda/docs/runtimes-list-deprecated"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Get data about functions by runtime"
status: active
depends_on:
  - "@specs/aws/lambda/meta"
---

# Get data about functions by runtime

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lambda/docs/runtimes-list-deprecated
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Retrieve data about Lambda functions that use a deprecated runtime
<a name="runtimes-list-deprecated"></a>

When a Lambda runtime is approaching deprecation, Lambda alerts you through email and provides notifications in the Health Dashboard and Trusted Advisor. These emails and notifications list the $LATEST versions of functions using the runtime. To list all of your function versions that use a particular runtime, you can use the AWS Command Line Interface (AWS CLI) or one of the AWS SDKs.

If you have a large number of functions which use a runtime that is due to be deprecated, you can also use the AWS CLI or AWS SDKs to help you prioritize updates to your most commonly invoked functions.

Refer to the following sections to learn how to use the AWS CLI and AWS SDKs to gather data about functions that use a particular runtime.

## Listing function versions that use a particular runtime
<a name="runtimes-list-deprecated-versions"></a>

To use the AWS CLI to list all of your function versions that use a particular runtime, run the following command. Replace `RUNTIME_IDENTIFIER` with the name of the runtime that’s being deprecated and choose your own AWS Region. To list only $LATEST function versions, omit `--function-version ALL` from the command.

```
aws lambda list-functions --function-version ALL --region {{us-east-1}} --output text --query "Functions[?Runtime=='{{RUNTIME_IDENTIFIER}}'].FunctionArn" 
```

**Tip**  
The example command lists functions in the `us-east-1` region for a particular AWS account You’ll need to repeat this command for each region in which your account has functions and for each of your AWS accounts.

You can also list functions that use a particular runtime using one of the AWS SDKs. The following example code uses the V3 AWS SDK for JavaScript and the AWS SDK for Python (Boto3) to return a list of the function ARNs for functions using a particular runtime. The example code also returns the CloudWatch log group for each of the listed functions. You can use this log group to find the last invocation date for the function. See the following section [Identifying most commonly and most recently invoked functions](#runtimes-list-deprecated-statistics) for more information.

------
#### [ Node.js ]

**Example JavaScript code to list functions using a particular runtime**  

```
import { LambdaClient, ListFunctionsCommand } from "@aws-sdk/client-lambda";
const lambdaClient = new LambdaClient();

const command = new ListFunctionsCommand({
    FunctionVersion: "ALL",
    MaxItems: 50
});
const response = await lambdaClient.send(command);

for (const f of response.Functions){
    if (f.Runtime == '{{<your_runtime>}}'){ // Use the runtime id, e.g. 'nodejs24.x' or 'python3.14'
        console.log(f.FunctionArn);
        // get the CloudWatch log group of the function to
        // use later for finding the last invocation date
        console.log(f.LoggingConfig.LogGroup);
    }   
}
// If your account has more functions than the specified
// MaxItems, use the returned pagination token in the 
// next request with the 'Marker' parameter
if ('NextMarker' in response){
    let paginationToken = response.NextMarker;
  }
```

------
#### [ Python ]

**Example Python code to list functions using a particular runtime**  

```
import boto3
from botocore.exceptions import ClientError

def list_lambda_functions(target_runtime):

    lambda_client = boto3.client('lambda')
    
    response = lambda_client.list_functions(
        FunctionVersion='ALL',
        MaxItems=50
    )
    if not response['Functions']:
            print("No Lambda functions found")
    else: 
        for function in response['Functions']:   
            if function['PackageType']=='Zip' and function['Runtime'] == target_runtime: 
                print(function['FunctionArn'])
                # Print the CloudWatch log group of the function
                # to use later for finding last invocation date
                print(function['LoggingConfig']['LogGroup'])

    if 'NextMarker' in response:
       pagination_token = response['NextMarker']

if __name__ == "__main__":
    # Replace python3.12 with the appropriate runtime ID for your Lambda functions
    list_lambda_functions('{{python3.12}}')
```

------

To learn more about using an AWS SDK to list your functions using the [ListFunctions](https://docs.aws.amazon.com/lambda/latest/api/API_ListFunctions.html) action, see the [SDK documentation](https://aws.amazon.com/developer/tools/) for your preferred programming language.

You can also use the AWS Config Advanced queries feature to list all your functions that use an affected runtime. This query only returns function $LATEST versions, but you can aggregate queries to list function across all regions and multiple AWS accounts with a single command. To learn more, see [Querying the Current Configuration State of AWS Auto Scaling Resources](https://docs.aws.amazon.com/config/latest/developerguide/querying-AWS-resources.html) in the *AWS Config Developer Guide*.

## Identifying most commonly and most recently invoked functions
<a name="runtimes-list-deprecated-statistics"></a>

If your AWS account contains functions that use a runtime that's due to be deprecated, you might want to prioritize updating functions that are frequently invoked or functions that have been invoked recently.

If you have only a few functions, you can use the CloudWatch Logs console to gather this information by looking at your functions' log streams. See [View log data sent to CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html#ViewingLogData) for more information.

To see the number of recent function invocations, you can also use the CloudWatch metrics information shown in the Lambda console. To view this information, do the following:

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions) of the Lambda console.

1. Select the function you want to see invocation statistics for.

1. Choose the **Monitor** tab.

1. Set the time period you wish to view statistics for using the date range picker. Recent invocations are displayed in the **Invocations** pane.

For accounts with larger numbers of functions, it can be more efficient to gather this data programmatically using the AWS CLI or one of the AWS SDKs using the [DescribeLogStreams](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DescribeLogStreams.html) and [GetMetricStatistics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricStatistics.html) API actions.

The following examples provide code snippets using the V3 AWS SDK for JavaScript and the AWS SDK for Python (Boto3) to identify the last invoke date for a particular function and to determine the number of invocations for a particular function in the last 14 days.

------
#### [ Node.js ]

**Example JavaScript code to find last invocation time for a function**  

```
import { CloudWatchLogsClient, DescribeLogStreamsCommand } from "@aws-sdk/client-cloudwatch-logs";
const cloudWatchLogsClient = new CloudWatchLogsClient();
const command = new DescribeLogStreamsCommand({
    logGroupName: '{{<your_log_group_name>}}',
    orderBy: 'LastEventTime',
    descending: true,
    limit: 1
});
try {
    const response = await cloudWatchLogsClient.send(command);
    const lastEventTimestamp = response.logStreams.length > 0 ? 
        response.logStreams[0].lastEventTimestamp : null;
    // Convert the UNIX timestamp to a human-readable format for display
    const date = new Date(lastEventTimestamp).toLocaleDateString();
    const time = new Date(lastEventTimestamp).toLocaleTimeString();
    console.log(`${date} ${time}`);
    
} catch (e){
    console.error('Log group not found.')
}
```

------
#### [ Python ]

**Example Python code to find last invocation time for a function**  

```
import boto3
from datetime import datetime

cloudwatch_logs_client  = boto3.client('logs')

response = cloudwatch_logs_client.describe_log_streams(
    logGroupName='{{<your_log_group_name>}}',
    orderBy='LastEventTime',
    descending=True,
    limit=1
)

try:
    if len(response['logStreams']) > 0:
        last_event_timestamp = response['logStreams'][0]['lastEventTimestamp']
        print(datetime.fromtimestamp(last_event_timestamp/1000)) # Convert timestamp from ms to seconds
    else:
        last_event_timestamp = None
except:
    print('Log group not found')
```

------

**Tip**  
You can find your function's log group name using the [ListFunctions](https://docs.aws.amazon.com/lambda/latest/api/API_ListFunctions.html) API operation. See the code in [Listing function versions that use a particular runtime](#runtimes-list-deprecated-versions) for an example of how to do this.

------
#### [ Node.js ]

**Example JavaScript code to find number of invocations in last 14 days**  

```
import { CloudWatchClient, GetMetricStatisticsCommand } from "@aws-sdk/client-cloudwatch";
const cloudWatchClient = new CloudWatchClient();
const command = new GetMetricStatisticsCommand({
    Namespace: 'AWS/Lambda',
    MetricName: 'Invocations',
    StartTime: new Date(Date.now()-86400*1000*14), // 14 days ago
    EndTime: new Date(Date.now()),
    Period: 86400 * 14, // 14 days.
    Statistics: ['Sum'],
    Dimensions: [{
        Name: 'FunctionName',
        Value: '{{<your_function_name>}}'
    }]
});
const response = await cloudWatchClient.send(command);
const invokesInLast14Days = response.Datapoints.length > 0 ? 
    response.Datapoints[0].Sum : 0;

console.log('Number of invocations: ' + invokesInLast14Days);
```

------
#### [ Python ]

**Example Python code to find number of invocations in last 14 days**  

```
import boto3
from datetime import datetime, timedelta

cloudwatch_client = boto3.client('cloudwatch')

response = cloudwatch_client.get_metric_statistics(
    Namespace='AWS/Lambda',
    MetricName='Invocations',
    Dimensions=[
        {
            'Name': 'FunctionName',
            'Value': '{{<your_function_name>}}'
        },
    ],
    StartTime=datetime.now() - timedelta(days=14),
    EndTime=datetime.now(),
    Period=86400 * 14, # 14 days
    Statistics=[
        'Sum'
    ]
)

if len(response['Datapoints']) > 0:
    invokes_in_last_14_days = int(response['Datapoints'][0]['Sum'])
else:
    invokes_in_last_14_days = 0

print(f'Number of invocations: {invokes_in_last_14_days}')
```

------