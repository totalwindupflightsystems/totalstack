---
id: "@specs/aws/timestream-influxdb/docs/DBeaver"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DBeaver"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# DBeaver

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/DBeaver
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Using DBeaver to work with Amazon Timestream
<a name="DBeaver"></a>

[DBeaver](https://dbeaver.io/) is a free universal SQL client that can be used to manage any database that has a JDBC driver. It is widely used among developers and database administrators because of its robust data viewing, editing, and management capabilities.

Using DBeaver's cloud connectivity options, you can connect DBeaver to Amazon Timestream natively. DBeaver provides a comprehensive and intuitive interface to work with time series data directly from within a DBeaver application. Using your credentials, it also gives you full access to any queries that you could execute from another query interface. It even lets you create graphs for better understanding and visualization of query results.

## Setting up DBeaver to work with Timestream
<a name="DBeaver-setup"></a>

Take the following steps to set up DBeaver to work with Timestream:

1. [Download and install DBeaver](https://dbeaver.io/download/) on your local machine.

1. Launch DBeaver, navigate to the database selection area, choose **Timeseries** in the left pane, and then select the **Timestream** icon in the right pane:  
![DBeaver screenshot showing how to select Timestream in the database selection area.](http://docs.aws.amazon.com/timestream/latest/developerguide/images/DBeaver-01.png)

1. In the **Timestream Connection Settings** window, enter all the information necessary to connect to your Amazon Timestream database. Please ensure that the user keys you enter have the permissions necessary to access your Timestream database. Also, be sure to keep the information and keys you input into DBeaver safe and private, as with any sensitive information.  
![DBeaver screenshot showing connection fields for Timestream.](http://docs.aws.amazon.com/timestream/latest/developerguide/images/DBeaver-02.png)

1. Test the connection to ensure that everything is set up correctly:  
![DBeaver screenshot showing a successful connection test.](http://docs.aws.amazon.com/timestream/latest/developerguide/images/DBeaver-03.png)

1. If the connection test is successful, you can now interact with your Amazon Timestream database just as you would with any other database in DBeaver. For example, you can navigate to the SQL editor or to the ER Diagram view to run queries:  
![DBeaver screenshot showing a Timestream query run from the SQL editor.](http://docs.aws.amazon.com/timestream/latest/developerguide/images/DBeaver-04.png)

1. DBeaver also provides powerful data visualization tools. To use them, run your query, then select the graph icon to visualize the result set. The graphing tool can help you better understand data trends over time.

Pairing Amazon Timestream with DBeaver creates an effective environment for managing time series data. You can integrate it seamlessly into your existing workflow to enhance productivity and efficiency.