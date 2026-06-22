---
id: "@specs/aws/timestream-influxdb/docs/customer-defined-partition-keys-updating-configuration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Updating partitioning schema configuration"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Updating partitioning schema configuration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/customer-defined-partition-keys-updating-configuration
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Updating partitioning schema configuration
<a name="customer-defined-partition-keys-updating-configuration"></a>

You can update table configuration for partitioning schema with an SDK with access the `UpdateTable` action.

## Update a table with a partition key
<a name="code-samples.update-table-updating-partition-key"></a>

You can use the following code snippets to update a table with a partition key.

------
#### [  Java  ]

```
    public void updateTableCompositePartitionKeyEnforcement() {
        System.out.println("Updating table");

        UpdateTableRequest updateTableRequest = new UpdateTableRequest();
        updateTableRequest.setDatabaseName(DATABASE_NAME);
        updateTableRequest.setTableName(TABLE_NAME);

        // Can update enforcement level for dimension type partition key with OPTIONAL or REQUIRED enforcement
        final List<PartitionKey> partitionKeyWithDimensionAndRequiredEnforcement = Collections.singletonList(new PartitionKey()
            .withName(COMPOSITE_PARTITION_KEY_DIM_NAME)
            .withType(PartitionKeyType.DIMENSION)
            .withEnforcementInRecord(PartitionKeyEnforcementLevel.REQUIRED));
        Schema schema = new Schema();
        schema.setCompositePartitionKey(partitionKeyWithDimensionAndRequiredEnforcement);
        updateTableRequest.withSchema(schema);

        writeClient.updateTable(updateTableRequest);
        System.out.println("Table updated");
```

------
#### [  Java v2  ]

```
    public void updateTableCompositePartitionKeyEnforcement() {
        System.out.println("Updating table");
        // Can update enforcement level for dimension type partition key with OPTIONAL or REQUIRED enforcement
        final List<PartitionKey> partitionKeyWithDimensionAndRequiredEnforcement = Collections.singletonList(PartitionKey
            .builder()
            .name(COMPOSITE_PARTITION_KEY_DIM_NAME)
            .type(PartitionKeyType.DIMENSION)
            .enforcementInRecord(PartitionKeyEnforcementLevel.REQUIRED)
            .build());
        final Schema schema = Schema.builder()
                .compositePartitionKey(partitionKeyWithDimensionAndRequiredEnforcement).build();
        final UpdateTableRequest updateTableRequest = UpdateTableRequest.builder()
                .databaseName(DATABASE_NAME).tableName(TABLE_NAME).schema(schema).build();

        writeClient.updateTable(updateTableRequest);
        System.out.println("Table updated");
```

------
#### [  Go v1 ]

```
 // Update table partition key enforcement attribute
    updateTableInput := &timestreamwrite.UpdateTableInput{
         DatabaseName: aws.String(*databaseName),
         TableName:    aws.String(*tableName),
         // Can update enforcement level for dimension type partition key with OPTIONAL or REQUIRED enforcement
         Schema: &timestreamwrite.Schema{
             CompositePartitionKey: []*timestreamwrite.PartitionKey{
                 {
                         Name:                aws.String(CompositePartitionKeyDimName),
                         EnforcementInRecord: aws.String("REQUIRED"),
                         Type:                aws.String("DIMENSION"),
                 },
             }},
     }
     updateTableOutput, err := writeSvc.UpdateTable(updateTableInput)
         if err != nil {
             fmt.Println("Error:")
             fmt.Println(err)
         } else {
             fmt.Println("Update table is successful, below is the output:")
             fmt.Println(updateTableOutput)
         }
```

------
#### [  Go v2 ]

```
 // Update table partition key enforcement attribute
         updateTableInput := &timestreamwrite.UpdateTableInput{
             DatabaseName: aws.String(*databaseName),
             TableName:    aws.String(*tableName),
             // Can update enforcement level for dimension type partition key with OPTIONAL or REQUIRED enforcement
             Schema: &types.Schema{
                 CompositePartitionKey: []types.PartitionKey{
                     {
                         Name:                aws.String(CompositePartitionKeyDimName),
                         EnforcementInRecord: types.PartitionKeyEnforcementLevelRequired,
                         Type:                types.PartitionKeyTypeDimension,
                     },
                 }},
         }
         updateTableOutput, err := timestreamBuilder.WriteSvc.UpdateTable(context.TODO(), updateTableInput)
         if err != nil {
             fmt.Println("Error:")
             fmt.Println(err)
         } else {
             fmt.Println("Update table is successful, below is the output:")
             fmt.Println(updateTableOutput)
         }
```

------
#### [  Python  ]

```
    def update_table(self):
        print('Updating table')
        try:
            # Can update enforcement level for dimension type partition key with OPTIONAL or REQUIRED enforcement
            partition_key_with_dimension_and_required_enforcement = [
                {
                    'Type': 'DIMENSION', 
                    'Name': COMPOSITE_PARTITION_KEY_DIM_NAME, 
                    'EnforcementInRecord': 'REQUIRED'
                }
            ]
            schema = {
                'CompositePartitionKey': partition_key_with_dimension_and_required_enforcement
            }
            self.client.update_table(DatabaseName=DATABASE_NAME, TableName=TABLE_NAME,
                                     Schema=schema)
            print('Table updated.')
        except Exception as err:
            print('Update table failed:', err)
```

------