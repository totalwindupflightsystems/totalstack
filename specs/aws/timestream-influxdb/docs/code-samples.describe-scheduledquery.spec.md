---
id: "@specs/aws/timestream-influxdb/docs/code-samples.describe-scheduledquery"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Describe scheduled query"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Describe scheduled query

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/code-samples.describe-scheduledquery
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Describe scheduled query
<a name="code-samples.describe-scheduledquery"></a>

You can use the following code snippets to describe a scheduled query.

------
#### [  Java  ]

```
public void describeScheduledQueries(String scheduledQueryArn) {
    System.out.println("Describing Scheduled Query");
    try {
        DescribeScheduledQueryResult describeScheduledQueryResult = queryClient.describeScheduledQuery(new DescribeScheduledQueryRequest().withScheduledQueryArn(scheduledQueryArn));
        System.out.println(describeScheduledQueryResult);
    }
    catch (ResourceNotFoundException e) {
        System.out.println("Scheduled Query doesn't exist");
        throw e;
    }
    catch (Exception e) {
        System.out.println("Describe Scheduled Query failed: " + e);
        throw e;
    }
}
```

------
#### [  Java v2  ]

```
public void describeScheduledQueries(String scheduledQueryArn) {
    System.out.println("Describing Scheduled Query");
    try {
        DescribeScheduledQueryResponse describeScheduledQueryResult =
                queryClient.describeScheduledQuery(DescribeScheduledQueryRequest.builder()
                        .scheduledQueryArn(scheduledQueryArn)
                        .build());
        System.out.println(describeScheduledQueryResult);
    }
    catch (ResourceNotFoundException e) {
        System.out.println("Scheduled Query doesn't exist");
        throw e;
    }
    catch (Exception e) {
        System.out.println("Describe Scheduled Query failed: " + e);
        throw e;
    }
}
```

------
#### [  Go  ]

```
func (timestreamBuilder TimestreamBuilder) DescribeScheduledQuery(scheduledQueryArn string) error {
 
     describeScheduledQueryInput := &timestreamquery.DescribeScheduledQueryInput{
         ScheduledQueryArn: aws.String(scheduledQueryArn),
     }
     describeScheduledQueryOutput, err := timestreamBuilder.QuerySvc.DescribeScheduledQuery(describeScheduledQueryInput)
 
     if err != nil {
         if aerr, ok := err.(awserr.Error); ok {
             switch aerr.Code() {
             case timestreamquery.ErrCodeResourceNotFoundException:
                 fmt.Println(timestreamquery.ErrCodeResourceNotFoundException, aerr.Error())
             default:
                 fmt.Printf("Error: %s", err.Error())
             }
         } else {
             fmt.Printf("Error: %s", aerr.Error())
         }
         return err
     } else {
         fmt.Println("DescribeScheduledQuery is successful, below is the output:")
         fmt.Println(describeScheduledQueryOutput.ScheduledQuery)
         return nil
     }
 }
```

------
#### [  Python  ]

```
def describe_scheduled_query(self, scheduled_query_arn):
    print("\nDescribing Scheduled Query")
    try:
        response = self.query_client.describe_scheduled_query(ScheduledQueryArn=scheduled_query_arn)
        if 'ScheduledQuery' in response:
            response = response['ScheduledQuery']
            for key in response:
                print("{} :{}".format(key, response[key]))
    except self.query_client.exceptions.ResourceNotFoundException as err:
        print("Scheduled Query doesn't exist")
        raise err
    except Exception as err:
        print("Scheduled Query describe failed:", err)
        raise err
```

------
#### [  Node.js  ]

The following snippet uses the AWS SDK for JavaScript V2 style. It is based on the sample application at [Node.js sample Amazon Timestream for LiveAnalytics application on GitHub](https://github.com/awslabs/amazon-timestream-tools/blob/mainline/sample_apps_reinvent2021/js/schedule-query-example.js).

```
async function describeScheduledQuery(scheduledQueryArn) {
     console.log("Describing Scheduled Query");
     var params = {
         ScheduledQueryArn: scheduledQueryArn
     }
     try {
         const data = await queryClient.describeScheduledQuery(params).promise();
         console.log(data.ScheduledQuery);
     } catch (err) {
         console.log("Describe Scheduled Query failed: ", err);
         throw err;
     }
 }
```

------
#### [  .NET  ]

```
private async Task DescribeScheduledQuery(string scheduledQueryArn)
 {
     try
     {
         Console.WriteLine("Describing Scheduled Query");
         DescribeScheduledQueryResponse response = await _amazonTimestreamQuery.DescribeScheduledQueryAsync(
             new DescribeScheduledQueryRequest()
             {
                 ScheduledQueryArn = scheduledQueryArn
             });
         Console.WriteLine($"{JsonConvert.SerializeObject(response.ScheduledQuery)}");
     }
     catch (ResourceNotFoundException e)
     {
         Console.WriteLine($"Scheduled Query doesn't exist: {e}");
         throw;
     }
     catch (Exception e)
     {
         Console.WriteLine($"Describe Scheduled Query failed: {e}");
         throw;
     }
 }
```

------