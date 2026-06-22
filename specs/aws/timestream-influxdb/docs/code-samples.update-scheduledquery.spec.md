---
id: "@specs/aws/timestream-influxdb/docs/code-samples.update-scheduledquery"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Update scheduled query"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Update scheduled query

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/code-samples.update-scheduledquery
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Update scheduled query
<a name="code-samples.update-scheduledquery"></a>

You can use the following code snippets to update a scheduled query.

------
#### [  Java  ]

```
public void updateScheduledQueries(String scheduledQueryArn) {
    System.out.println("Updating Scheduled Query");
    try {
        queryClient.updateScheduledQuery(new UpdateScheduledQueryRequest()
                .withScheduledQueryArn(scheduledQueryArn)
                .withState(ScheduledQueryState.DISABLED));
        System.out.println("Successfully update scheduled query state");
    }
    catch (ResourceNotFoundException e) {
        System.out.println("Scheduled Query doesn't exist");
        throw e;
    }
    catch (Exception e) {
        System.out.println("Execution Scheduled Query failed: " + e);
        throw e;
    }
}
```

------
#### [  Java v2  ]

```
public void updateScheduledQuery(String scheduledQueryArn, ScheduledQueryState state) {
    System.out.println("Updating Scheduled Query");
    try {
        queryClient.updateScheduledQuery(UpdateScheduledQueryRequest.builder()
                .scheduledQueryArn(scheduledQueryArn)
                .state(state)
                .build());
        System.out.println("Successfully update scheduled query state");
    }
    catch (ResourceNotFoundException e) {
        System.out.println("Scheduled Query doesn't exist");
        throw e;
    }
    catch (Exception e) {
        System.out.println("Execution Scheduled Query failed: " + e);
        throw e;
    }
}
```

------
#### [  Go  ]

```
func (timestreamBuilder TimestreamBuilder) UpdateScheduledQuery(scheduledQueryArn string) error {

     updateScheduledQueryInput := &timestreamquery.UpdateScheduledQueryInput{
         ScheduledQueryArn: aws.String(scheduledQueryArn),
         State:             aws.String(timestreamquery.ScheduledQueryStateDisabled),
     }
     _, err := timestreamBuilder.QuerySvc.UpdateScheduledQuery(updateScheduledQueryInput)

     if err != nil {
         if aerr, ok := err.(awserr.Error); ok {
             switch aerr.Code() {
             case timestreamquery.ErrCodeResourceNotFoundException:
                 fmt.Println(timestreamquery.ErrCodeResourceNotFoundException, aerr.Error())
             default:
                 fmt.Printf("Error: %s", aerr.Error())
             }
         } else {
             fmt.Printf("Error: %s", err.Error())
         }
         return err
     } else {
         fmt.Println("UpdateScheduledQuery is successful")
         return nil
     }
 }
```

------
#### [  Python  ]

```
def update_scheduled_query(self, scheduled_query_arn, state):
    print("\nUpdating Scheduled Query")
    try:
        self.query_client.update_scheduled_query(ScheduledQueryArn=scheduled_query_arn,
                                                 State=state)
        print("Successfully update scheduled query state to", state)
    except self.query_client.exceptions.ResourceNotFoundException as err:
        print("Scheduled Query doesn't exist")
        raise err
    except Exception as err:
        print("Scheduled Query deletion failed:", err)
        raise err
```

------
#### [  Node.js  ]

The following snippet uses the AWS SDK for JavaScript V2 style. It is based on the sample application at [Node.js sample Amazon Timestream for LiveAnalytics application on GitHub](https://github.com/awslabs/amazon-timestream-tools/blob/mainline/sample_apps_reinvent2021/js/schedule-query-example.js).

```
async function updateScheduledQueries(scheduledQueryArn) {
     console.log("Updating Scheduled Query");
     var params = {
         ScheduledQueryArn: scheduledQueryArn,
         State: "DISABLED"
     }
     try {
         await queryClient.updateScheduledQuery(params).promise();
         console.log("Successfully update scheduled query state");
     } catch (err) {
         console.log("Update Scheduled Query failed: ", err);
         throw err;
     }
 }
```

------
#### [  .NET  ]

```
private async Task UpdateScheduledQuery(string scheduledQueryArn, ScheduledQueryState state)
 {
     try
     {
         Console.WriteLine("Updating Scheduled Query");
         await _amazonTimestreamQuery.UpdateScheduledQueryAsync(new UpdateScheduledQueryRequest()
         {
             ScheduledQueryArn = scheduledQueryArn,
             State = state
         });
         Console.WriteLine("Successfully update scheduled query state");
     }
     catch (ResourceNotFoundException e)
     {
         Console.WriteLine($"Scheduled Query doesn't exist: {e}");
         throw;
     }
     catch (Exception e)
     {
         Console.WriteLine($"Update Scheduled Query failed: {e}");
         throw;
     }
 }
```

------