---
id: "@specs/aws/timestream-influxdb/docs/customer-defined-partition-keys-getting-started"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Getting started with customer-defined partition keys"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Getting started with customer-defined partition keys

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/customer-defined-partition-keys-getting-started
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Getting started with customer-defined partition keys
<a name="customer-defined-partition-keys-getting-started"></a>

From the console, choose **Tables** and create a new table. You can also use an SDK to access the `CreateTable` action to create new tables that can include a customer-defined partition key.

## Create a table with a dimension type partition key
<a name="code-samples.create-table-with-dimension-type-partition-key"></a>

You can use the following code snippets to create a table with a dimension type partition key.

------
#### [  Java  ]

```
public void createTableWithDimensionTypePartitionKeyExample() {
        System.out.println("Creating table");
        CreateTableRequest createTableRequest = new CreateTableRequest();
        createTableRequest.setDatabaseName(DATABASE_NAME);
        createTableRequest.setTableName(TABLE_NAME);
        final RetentionProperties retentionProperties = new RetentionProperties()
                .withMemoryStoreRetentionPeriodInHours(HT_TTL_HOURS)
                .withMagneticStoreRetentionPeriodInDays(CT_TTL_DAYS);
        createTableRequest.setRetentionProperties(retentionProperties);

        // Can specify enforcement level with OPTIONAL or REQUIRED
        final List<PartitionKey> partitionKeyWithDimensionAndOptionalEnforcement = Collections.singletonList(new PartitionKey()
            .withName(COMPOSITE_PARTITION_KEY_DIM_NAME)
            .withType(PartitionKeyType.DIMENSION)
            .withEnforcementInRecord(PartitionKeyEnforcementLevel.OPTIONAL));
        Schema schema = new Schema();
        schema.setCompositePartitionKey(partitionKeyWithDimensionAndOptionalEnforcement);
        createTableRequest.setSchema(schema);
        
        try {
            writeClient.createTable(createTableRequest);
            System.out.println("Table [" + TABLE_NAME + "] successfully created.");
        } catch (ConflictException e) {
            System.out.println("Table [" + TABLE_NAME + "] exists on database [" + DATABASE_NAME + "] . Skipping database creation");
        }
    }
```

------
#### [  Java v2  ]

```
public void createTableWithDimensionTypePartitionKeyExample() {
        System.out.println("Creating table"); 
        final RetentionProperties retentionProperties = RetentionProperties.builder()
                .memoryStoreRetentionPeriodInHours(HT_TTL_HOURS)
                .magneticStoreRetentionPeriodInDays(CT_TTL_DAYS)
                .build();
        // Can specify enforcement level with OPTIONAL or REQUIRED
        final List<PartitionKey> partitionKeyWithDimensionAndOptionalEnforcement = Collections.singletonList(PartitionKey
                .builder()
                .name(COMPOSITE_PARTITION_KEY_DIM_NAME)
                .type(PartitionKeyType.DIMENSION)
                .enforcementInRecord(PartitionKeyEnforcementLevel.OPTIONAL)
                .build());
        final Schema schema = Schema.builder()
                .compositePartitionKey(partitionKeyWithDimensionAndOptionalEnforcement).build();
        final CreateTableRequest createTableRequest = CreateTableRequest.builder()
                .databaseName(DATABASE_NAME)
                .tableName(TABLE_NAME)
                .retentionProperties(retentionProperties)
                .schema(schema)
                .build();

        try {
            writeClient.createTable(createTableRequest);
            System.out.println("Table [" + TABLE_NAME + "] successfully created.");
        } catch (ConflictException e) {
            System.out.println("Table [" + TABLE_NAME + "] exists on database [" + DATABASE_NAME + "] . Skipping database creation");
        }
    }
```

------
#### [  Go v1 ]

```
func createTableWithDimensionTypePartitionKeyExample(){ 
        // Can specify enforcement level with OPTIONAL or REQUIRED
        partitionKeyWithDimensionAndOptionalEnforcement := []*timestreamwrite.PartitionKey{
                {
                    Name:                aws.String(CompositePartitionKeyDimName),
                    EnforcementInRecord: aws.String("OPTIONAL"),
                    Type:                aws.String("DIMENSION"),
                },
        }     
        createTableInput := &timestreamwrite.CreateTableInput{
             DatabaseName: aws.String(*databaseName),
             TableName:    aws.String(*tableName),
             // Enable MagneticStoreWrite for Table
             MagneticStoreWriteProperties: &timestreamwrite.MagneticStoreWriteProperties{
                 EnableMagneticStoreWrites: aws.Bool(true),
                 // Persist MagneticStoreWrite rejected records in S3
                 MagneticStoreRejectedDataLocation: &timestreamwrite.MagneticStoreRejectedDataLocation{
                     S3Configuration: &timestreamwrite.S3Configuration{
                         BucketName:       aws.String("timestream-sample-bucket"),
                         ObjectKeyPrefix:  aws.String("TimeStreamCustomerSampleGo"),
                         EncryptionOption: aws.String("SSE_S3"),
                     },
                 },
             },   
             Schema: &timestreamwrite.Schema{
                 CompositePartitionKey: partitionKeyWithDimensionAndOptionalEnforcement,
             }
         }
         _, err := writeSvc.CreateTable(createTableInput)
    }
```

------
#### [  Go v2 ]

```
  func (timestreamBuilder TimestreamBuilder) CreateTableWithDimensionTypePartitionKeyExample() error {
         partitionKeyWithDimensionAndOptionalEnforcement := []types.PartitionKey{
             {
                 Name:                aws.String(CompositePartitionKeyDimName),
                 EnforcementInRecord: types.PartitionKeyEnforcementLevelOptional,
                 Type:                types.PartitionKeyTypeDimension,
             },
         }
         _, err := timestreamBuilder.WriteSvc.CreateTable(context.TODO(), &timestreamwrite.CreateTableInput{
             DatabaseName: aws.String(databaseName),
             TableName:    aws.String(tableName),
             MagneticStoreWriteProperties: &types.MagneticStoreWriteProperties{
                 EnableMagneticStoreWrites: aws.Bool(true),
                 // Persist MagneticStoreWrite rejected records in S3
                 MagneticStoreRejectedDataLocation: &types.MagneticStoreRejectedDataLocation{
                     S3Configuration: &types.S3Configuration{
                         BucketName:       aws.String(s3BucketName),
                         EncryptionOption: "SSE_S3",
                     },
                 },
             },
             Schema: &types.Schema{
                 CompositePartitionKey: partitionKeyWithDimensionAndOptionalEnforcement,
             },
         })
      
         if err != nil {
             fmt.Println("Error:")
             fmt.Println(err)
         } else {
             fmt.Println("Create table is successful")
         }
         return err
     }
```

------
#### [  Python  ]

```
def create_table_with_measure_name_type_partition_key(self):
        print("Creating table")
        retention_properties = {
            'MemoryStoreRetentionPeriodInHours': HT_TTL_HOURS,
            'MagneticStoreRetentionPeriodInDays': CT_TTL_DAYS
        }
        partitionKey_with_measure_name = [
            {'Type': 'MEASURE'}
        ]
        schema = {
            'CompositePartitionKey': partitionKey_with_measure_name
        }
        try:
            self.client.create_table(DatabaseName=DATABASE_NAME, TableName=TABLE_NAME,
                                     RetentionProperties=retention_properties, Schema=schema)
            print("Table [%s] successfully created." % TABLE_NAME)
        except self.client.exceptions.ConflictException:
            print("Table [%s] exists on database [%s]. Skipping table creation" % (
                TABLE_NAME, DATABASE_NAME))
        except Exception as err:
            print("Create table failed:", err)
```

------