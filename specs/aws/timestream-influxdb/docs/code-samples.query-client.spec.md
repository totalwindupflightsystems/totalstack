---
id: "@specs/aws/timestream-influxdb/docs/code-samples.query-client"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Query SDK client"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Query SDK client

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/code-samples.query-client
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Query SDK client
<a name="code-samples.query-client"></a>

You can use the following code snippets to create a Timestream client for the Query SDK. The Query SDK is used to query your existing time series data stored in Timestream.

**Note**  
These code snippets are based on full sample applications on [GitHub](https://github.com/awslabs/amazon-timestream-tools/blob/master/sample_apps). For more information about how to get started with the sample applications, see [Sample application](sample-apps.md).

------
#### [  Java  ]

```
    private static AmazonTimestreamQuery buildQueryClient() {
        AmazonTimestreamQuery client = AmazonTimestreamQueryClient.builder().withRegion("us-east-1").build();
        return client;
    }
```

------
#### [  Java v2  ]

```
    private static TimestreamQueryClient buildQueryClient() {
        return TimestreamQueryClient.builder()
                .region(Region.US_EAST_1)
                .build();
    }
```

------
#### [  Go  ]

```
sess, err := session.NewSession(&aws.Config{Region: aws.String("us-east-1")})
```

------
#### [  Python  ]

```
query_client = session.client('timestream-query')
```

------
#### [  Node.js  ]

The following snippet uses AWS SDK for JavaScript v3. For more information about how to install the client and usage, see [Timestream Query Client - ,AWS SDK for JavaScript v3](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/clients/client-timestream-query/index.html).

An additional command import is shown here. The `QueryCommand` import is not required to create the client.

```
import { TimestreamQueryClient, QueryCommand } from "@aws-sdk/client-timestream-query";
const queryClient = new TimestreamQueryClient({ region: "us-east-1" });
```

The following snippet uses the AWS SDK for JavaScript V2 style. It is based on the sample application at [Node.js sample Amazon Timestream for LiveAnalytics application on GitHub](https://github.com/awslabs/amazon-timestream-tools/tree/mainline/sample_apps/js).

```
queryClient = new AWS.TimestreamQuery();
```

------
#### [  .NET  ]

```
var queryClientConfig = new AmazonTimestreamQueryConfig 
{ 
    RegionEndpoint = RegionEndpoint.USEast1 
}; 

var queryClient = new AmazonTimestreamQueryClient(queryClientConfig);
```

------