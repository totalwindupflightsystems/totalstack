---
id: "@specs/aws/timestream-influxdb/docs/code-samples.delete-db"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Delete database"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Delete database

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/code-samples.delete-db
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Delete database
<a name="code-samples.delete-db"></a>

You can use the following code snippet to delete a database.

**Note**  
These code snippets are based on full sample applications on [GitHub](https://github.com/awslabs/amazon-timestream-tools/blob/master/sample_apps). For more information about how to get started with the sample applications, see [Sample application](sample-apps.md).

------
#### [  Java  ]

```
    public void deleteDatabase() {
        System.out.println("Deleting database");
        final DeleteDatabaseRequest deleteDatabaseRequest = new DeleteDatabaseRequest();
        deleteDatabaseRequest.setDatabaseName(DATABASE_NAME);
        try {
            DeleteDatabaseResult result =
                    amazonTimestreamWrite.deleteDatabase(deleteDatabaseRequest);
            System.out.println("Delete database status: " + result.getSdkHttpMetadata().getHttpStatusCode());
        } catch (final ResourceNotFoundException e) {
            System.out.println("Database " + DATABASE_NAME + " doesn't exist = " + e);
            throw e;
        } catch (final Exception e) {
            System.out.println("Could not delete Database " + DATABASE_NAME + " = " + e);
            throw e;
        }
    }
```

------
#### [  Java v2  ]

```
    public void deleteDatabase() {
        System.out.println("Deleting database");
        final DeleteDatabaseRequest deleteDatabaseRequest = new DeleteDatabaseRequest();
        deleteDatabaseRequest.setDatabaseName(DATABASE_NAME);
        try {
            DeleteDatabaseResult result =
                    amazonTimestreamWrite.deleteDatabase(deleteDatabaseRequest);
            System.out.println("Delete database status: " + result.getSdkHttpMetadata().getHttpStatusCode());
        } catch (final ResourceNotFoundException e) {
            System.out.println("Database " + DATABASE_NAME + " doesn't exist = " + e);
            throw e;
        } catch (final Exception e) {
            System.out.println("Could not delete Database " + DATABASE_NAME + " = " + e);
            throw e;
        }
    }
```

------
#### [  Go  ]

```
deleteDatabaseInput := &timestreamwrite.DeleteDatabaseInput{
        DatabaseName:   aws.String(*databaseName),
    }

    _, err = writeSvc.DeleteDatabase(deleteDatabaseInput)

    if err != nil {
        fmt.Println("Error:")
        fmt.Println(err)
    } else {
        fmt.Println("Database deleted:", *databaseName)
    }
```

------
#### [  Python  ]

```
    def delete_database(self):
        print("Deleting Database")
        try:
            result = self.client.delete_database(DatabaseName=Constant.DATABASE_NAME)
            print("Delete database status [%s]" % result['ResponseMetadata']['HTTPStatusCode'])
        except self.client.exceptions.ResourceNotFoundException:
            print("database [%s] doesn't exist" % Constant.DATABASE_NAME)
        except Exception as err:
            print("Delete database failed:", err)
```

------
#### [  Node.js  ]

The following snippet uses AWS SDK for JavaScript v3. For more information about how to install the client and usage, see [Timestream Write Client - AWS SDK for JavaScript v3](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/clients/client-timestream-write/index.html).

Also see [Class DeleteDatabaseCommand](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/clients/client-timestream-write/classes/deletedatabasecommand.html) and [DeleteDatabase](https://docs.aws.amazon.com/timestream/latest/developerguide/API_DeleteDatabase.html).

```
import { TimestreamWriteClient, DeleteDatabaseCommand } from "@aws-sdk/client-timestream-write";
const writeClient = new TimestreamWriteClient({ region: "us-east-1" });

const params = {
    DatabaseName: "testDbFromNode"
};

const command = new DeleteDatabaseCommand(params);

try {
    const data = await writeClient.send(command);
    console.log("Deleted database"); 
} catch (error) {
    if (error.code === 'ResourceNotFoundException') { 
        console.log(`Database ${params.DatabaseName} doesn't exists.`); 
    } else { 
        console.log("Delete database failed.", error); 
        throw error; 
    } 
}
```

The following snippet uses the AWS SDK for JavaScript V2 style. It is based on the sample application at [Node.js sample Amazon Timestream for LiveAnalytics application on GitHub](https://github.com/awslabs/amazon-timestream-tools/tree/mainline/sample_apps/js).

```
async function deleteDatabase() { 
    console.log("Deleting Database"); 
    const params = { 
        DatabaseName: constants.DATABASE_NAME 
    }; 
 
    const promise = writeClient.deleteDatabase(params).promise(); 
 
    await promise.then( 
        function (data) { 
            console.log("Deleted database"); 
         }, 
        function(err) { 
            if (err.code === 'ResourceNotFoundException') { 
                console.log(`Database ${params.DatabaseName} doesn't exists.`); 
            } else { 
                console.log("Delete database failed.", err); 
                throw err; 
            } 
        } 
    ); 
}
```

------
#### [  .NET  ]

```
        public async Task DeleteDatabase()
        {
            Console.WriteLine("Deleting database");
            try
            {
                var deleteDatabaseRequest = new DeleteDatabaseRequest
                {
                    DatabaseName = Constants.DATABASE_NAME
                };
                DeleteDatabaseResponse response = await writeClient.DeleteDatabaseAsync(deleteDatabaseRequest);
                Console.WriteLine($"Database {Constants.DATABASE_NAME} delete request status:{response.HttpStatusCode}");
            }
            catch (ResourceNotFoundException)
            {
                Console.WriteLine($"Database {Constants.DATABASE_NAME} does not exists");
            }
            catch (Exception e)
            {
                Console.WriteLine("Exception while deleting database:" + e.ToString());
            }
        }
```

------