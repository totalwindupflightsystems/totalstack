---
id: "@specs/aws/timestream-influxdb/docs/Quicksight"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Amazon Quick"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Amazon Quick

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/Quicksight
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Amazon Quick
<a name="Quicksight"></a>

You can use Amazon Quick to analyze and publish data dashboards that contain your Amazon Timestream data. This section describes how you can create a new QuickSight data source connection, modify permissions, create new datasets, and perform an analysis. This [video tutorial ](https://youtu.be/TzW4HWl-L8s) describes how to work with Timestream and Quick. 

**Note**  
 All datasets in Quick are read-only. You can't make any changes to your actual data in Timestream by using Quick to remove the data source, dataset, or fields. 

**Topics**
+ [Accessing Amazon Timestream from QuickSight](#Quicksight.accessing)
+ [Create a new QuickSight data source connection for Timestream](#Quicksight.create-connection)
+ [Edit permissions for the QuickSight data source connection for Timestream](#Quicksight.permissions)
+ [Create a new QuickSight dataset for Timestream](#Quicksight.create-data)
+ [Create a new analysis for Timestream](#Quicksight.create-analysis)
+ [Video tutorial](#Quicksight.video-tutorial)

## Accessing Amazon Timestream from QuickSight
<a name="Quicksight.accessing"></a>

 Before you can proceed, Amazon QuickSight needs to be authorized to connect to Amazon Timestream. If connections are not enabled, you will receive an error when you try to connect. A QuickSight administrator can authorize connections to AWS resources. To authorize a connection from QuickSight to Timestream, follow the procedure at [Using Other AWS Services: Scoping Down Access](https://docs.aws.amazon.com/quicksight/latest/user/scoping-policies-for-access-to-aws-resources.html), choosing Amazon Timestream in step 5. 

## Create a new QuickSight data source connection for Timestream
<a name="Quicksight.create-connection"></a>

**Note**  
The connection between Amazon QuickSight and Amazon Timestream is encrypted in transit using SSL (TLS 1.2). You cannot create an unencrypted connection.

1. Ensure you have configured the appropriate permissions for Amazon QuickSight to access Amazon Timestream, as described in [Accessing Amazon Timestream from QuickSight](#Quicksight.accessing).

1. Begin by creating a new dataset. Choose **Datasets** from the navigation pane, then choose **New Dataset**. 

1. Select the Timestream data source card.

1. For **Data source name**, enter a name for your Timestream data source connection, for example `US Timestream Data`. 
**Note**  
Because you can create many datasets from a connection to Timestream, it's best to keep the name simple.

1. Choose **Validate connection** to check that you can successfully connect to Timestream.
**Note**  
 **Validate connection** only validates that you can connect. However, it doesn't validate a specific table or query. 

1. Choose **Create data source** to proceed.

1. For **Database**, choose **Select...** to view the list of available options. Choose the one you want to use. 

1. Choose **Select** to continue. 

1. Choose one of the following:
   + To import your data into QuickSight's in-memory engine (called SPICE), choose **Import to SPICE for quicker analytics**. 
   + To allow QuickSight to run a query against your data each time you refresh the dataset or use the analysis or dashboard, choose **Directly query your data**. 

1. Choose **Edit/Preview** and then **Save** to save your dataset and close it.

## Edit permissions for the QuickSight data source connection for Timestream
<a name="Quicksight.permissions"></a>

 The following procedure describes how to view, add, and revoke permissions for other QuickSight users so that they can access the same Timestream data source. The people need to be active users in QuickSight before you can add them. 

**Note**  
In QuickSight, data sources have two permissions levels: user and owner.  
Choose *user* to allow read access. 
Choose *owner* to allow that user to edit, share, or delete this QuickSight data source. 

1. Ensure you have configured the appropriate permissions for Amazon QuickSight to access Amazon Timestream, as described in [Accessing Amazon Timestream from QuickSight](#Quicksight.accessing).

1. Choose **Datasets** at left, then scroll down to find the data source card for your Timestream connection. For example `US Timestream Data`.

1. Choose the `Timestream` data source card.

1. Choose `Share data source`. A list of current permissions displays. 

1. (Optional) To edit permissions, you can choose `user` or `owner`. 

1. (Optional) To revoke permissions, choose `Revoke access`. People you revoke can't create new datasets from this data source. However, their existing datasets will still have access to this data source.

1. To add permissions, choose `Invite users`, then follow these steps to add a user:

   1. Add people to allow them to use the same data source.

   1. For each, choose the `Permission` that you want to apply.

1. When you are finished, choose `Close`.

## Create a new QuickSight dataset for Timestream
<a name="Quicksight.create-data"></a>

1. Ensure you have configured the appropriate permissions for Amazon QuickSight to access Amazon Timestream, as described in [Accessing Amazon Timestream from QuickSight](#Quicksight.accessing).

1. Choose **Datasets** at left, then scroll down to find the data source card for your Timestream connection. If you have many data sources, you can use the search bar at the top of the page to find it with a partial match on the name.

1. Choose the **Timestream** data source card. Then choose **Create data set**.

1. For **Database**, choose **Select** to view the list of available options. Choose the database that you want to use. 

1. For **Tables**, choose the table that you want to use.

1. Choose **Edit/Preview**.

1. (Optional) To add more data, choose **Add data** at top right. 

   1. Choose **Switch data source**, and choose a different data source. 

   1. Follow the UI prompts to finish adding data. 

   1. After adding new data to the same dataset, choose **Configure this join **(the two red dots). Set up a join for each additional table. 

   1. If you want to add calculated fields, choose **Add calculated field**. 

   1. To use Sagemaker, choose **Augment with SageMaker**. This option is only available in QuickSight Enterprise edition.

   1. Uncheck any fields you want to omit.

   1. Update any data types you want to change.

1. When you are done, choose **Save** to save and close the dataset. 

## Create a new analysis for Timestream
<a name="Quicksight.create-analysis"></a>

1. Ensure you have configured the appropriate permissions for Amazon QuickSight to access Amazon Timestream, as described in [Accessing Amazon Timestream from QuickSight](#Quicksight.accessing).

1. Choose **Analyses** at left.

1. Choose one of the following:
   + To create a new analysis, choose **New analysis** at right.
   + To add the Timestream dataset to an existing analysis, open the analysis you want to edit. Choose the pencil icon near at top left, then **Add data set**.

1. Start the first data visualization by choosing fields on the left. 

1. For more information, see [ Working with Analyses - Amazon QuickSight ](https://docs.aws.amazon.com/quicksight/latest/user/working-with-analyses.html)

## Video tutorial
<a name="Quicksight.video-tutorial"></a>

This [video](https://youtu.be/TzW4HWl-L8s) explains how Quick works with Timestream.