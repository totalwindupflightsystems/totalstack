---
id: "@specs/aws/timestream-influxdb/docs/customer-defined-partition-keys-checking-configuration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Checking partitioning schema configuration"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Checking partitioning schema configuration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/customer-defined-partition-keys-checking-configuration
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Checking partitioning schema configuration
<a name="customer-defined-partition-keys-checking-configuration"></a>

You can check how a table configuration for partitioning schema in a couple of ways. From the console, choose **Databases** and choose the table to check. You can also use an SDK to access the `DescribeTable` action.

## Describe a table with a partition key
<a name="code-samples.describe-table-checking-partition-key"></a>

You can use the following code snippets to describe a table with a partition key.

------
#### [  Java  ]

```
    public void describeTable() {
        System.out.println("Describing table");
        final DescribeTableRequest describeTableRequest = new DescribeTableRequest();
        describeTableRequest.setDatabaseName(DATABASE_NAME);
        describeTableRequest.setTableName(TABLE_NAME);
        try {
            DescribeTableResult result = amazonTimestreamWrite.describeTable(describeTableRequest);
            String tableId = result.getTable().getArn();
            System.out.println("Table " + TABLE_NAME + " has id " + tableId);
            // If table is created with composite partition key, it can be described with
            // System.out.println(result.getTable().getSchema().getCompositePartitionKey());
        } catch (final Exception e) {
            System.out.println("Table " + TABLE_NAME + " doesn't exist = " + e);
            throw e;
        }
    }
```

The following is an example output.

1. Table has dimension type partition key

   ```
   [{Type: DIMENSION,Name: hostId,EnforcementInRecord: OPTIONAL}]
   ```

1. Table has measure name type partition key

   ```
   [{Type: MEASURE,}]
   ```

1. Getting composite partition key from a table created without specifying composite partition key

   ```
   [{Type: MEASURE,}]
   ```

------
#### [  Java v2  ]

```
  public void describeTable() {
        System.out.println("Describing table");
        final DescribeTableRequest describeTableRequest = DescribeTableRequest.builder()
                .databaseName(DATABASE_NAME).tableName(TABLE_NAME).build();
        try {
            DescribeTableResponse response = writeClient.describeTable(describeTableRequest);
            String tableId = response.table().arn();
            System.out.println("Table " + TABLE_NAME + " has id " + tableId);
            // If table is created with composite partition key, it can be described with
            // System.out.println(response.table().schema().compositePartitionKey());
        } catch (final Exception e) {
            System.out.println("Table " + TABLE_NAME + " doesn't exist = " + e);
            throw e;
        }
    }
```

The following is an example output.

1. Table has dimension type partition key

   ```
   [PartitionKey(Type=DIMENSION, Name=hostId, EnforcementInRecord=OPTIONAL)]
   ```

1. Table has measure name type partition key

   ```
   [PartitionKey(Type=MEASURE)]
   ```

1. Getting composite partition key from a table created without specifying composite partition key will return

   ```
   [PartitionKey(Type=MEASURE)]
   ```

------
#### [  Go v1 ]

```
    <tablistentry>
     <tabname> Go </tabname>
     <tabcontent>
      <programlisting language="go"></programlisting>
     </tabcontent>
    </tablistentry>
```

The following is an example output.

```
{
  Table: {
    Arn: "arn:aws:timestream:us-west-2:533139590831:database/devops/table/host_metrics_dim_pk_1",
    CreationTime: 2023-05-31 01:52:00.511 +0000 UTC,
    DatabaseName: "devops",
    LastUpdatedTime: 2023-05-31 01:52:00.511 +0000 UTC,
    MagneticStoreWriteProperties: {
      EnableMagneticStoreWrites: true,
      MagneticStoreRejectedDataLocation: {
        S3Configuration: {
          BucketName: "timestream-sample-bucket-west",
          EncryptionOption: "SSE_S3",
          ObjectKeyPrefix: "TimeStreamCustomerSampleGo"
        }
      }
    },
    RetentionProperties: {
      MagneticStoreRetentionPeriodInDays: 73000,
      MemoryStoreRetentionPeriodInHours: 6
    },
    Schema: {
      CompositePartitionKey: [{
          EnforcementInRecord: "OPTIONAL",
          Name: "hostId",
          Type: "DIMENSION"
        }]
    },
    TableName: "host_metrics_dim_pk_1",
    TableStatus: "ACTIVE"
  }
}
```

------
#### [  Go v2 ]

```
 func (timestreamBuilder TimestreamBuilder) DescribeTable() (*timestreamwrite.DescribeTableOutput, error) {
         describeTableInput := &timestreamwrite.DescribeTableInput{
             DatabaseName: aws.String(databaseName),
             TableName:    aws.String(tableName),
         }
        describeTableOutput, err := timestreamBuilder.WriteSvc.DescribeTable(context.TODO(), describeTableInput)
    
        if err != nil {
            fmt.Printf("Failed to describe table with Error: %s", err.Error())
        } else {
            fmt.Printf("Describe table is successful : %s\n", JsonMarshalIgnoreError(*describeTableOutput))
            // If table is created with composite partition key, it will be included in the output
        }
    
        return describeTableOutput, err
    }
```

The following is an example output.

```
{
  "Table": {
    "Arn":"arn:aws:timestream:us-east-1:351861611069:database/cdpk-wr-db/table/host_metrics_dim_pk",
    "CreationTime":"2023-05-31T22:36:10.66Z",
    "DatabaseName":"cdpk-wr-db",
    "LastUpdatedTime":"2023-05-31T22:36:10.66Z",
    "MagneticStoreWriteProperties":{
      "EnableMagneticStoreWrites":true,
      "MagneticStoreRejectedDataLocation":{
        "S3Configuration":{
          "BucketName":"error-configuration-sample-s3-bucket-cq8my",
          "EncryptionOption":"SSE_S3",
          "KmsKeyId":null,"ObjectKeyPrefix":null
        }
      }
    },
    "RetentionProperties":{
      "MagneticStoreRetentionPeriodInDays":73000,
      "MemoryStoreRetentionPeriodInHours":6
    },
    "Schema":{
      "CompositePartitionKey":[{
        "Type":"DIMENSION",
        "EnforcementInRecord":"OPTIONAL",
        "Name":"hostId"
      }]
    },
    "TableName":"host_metrics_dim_pk",
    "TableStatus":"ACTIVE"
  },
  "ResultMetadata":{}
}
```

------
#### [  Python  ]

```
  def describe_table(self):
        print('Describing table')
        try:
            result = self.client.describe_table(DatabaseName=DATABASE_NAME, TableName=TABLE_NAME)
            print("Table [%s] has id [%s]" % (TABLE_NAME, result['Table']['Arn']))
            # If table is created with composite partition key, it can be described with
            # print(result['Table']['Schema'])
        except self.client.exceptions.ResourceNotFoundException:
            print("Table doesn't exist")
        except Exception as err:
            print("Describe table failed:", err)
```

The following is an example output.

1. Table has dimension type partition key

   ```
   [{'CompositePartitionKey': [{'Type': 'DIMENSION', 'Name': 'hostId', 'EnforcementInRecord': 'OPTIONAL'}]}]
   ```

1. Table has measure name type partition key

   ```
   [{'CompositePartitionKey': [{'Type': 'MEASURE'}]}]
   ```

1. Getting composite partition key from a table created without specifying composite partition key 

   ```
   [{'CompositePartitionKey': [{'Type': 'MEASURE'}]}]
   ```

------