---
id: "@specs/aws/rds/docs/API_DescribeDBRecommendations"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeDBRecommendations"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# DescribeDBRecommendations

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_DescribeDBRecommendations
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeDBRecommendations
<a name="API_DescribeDBRecommendations"></a>

Describes the recommendations to resolve the issues for your DB instances, DB clusters, and DB parameter groups.

## Request Parameters
<a name="API_DescribeDBRecommendations_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **Filters.Filter.N**   
A filter that specifies one or more recommendations to describe.  
Supported Filters:  
+  `recommendation-id` - Accepts a list of recommendation identifiers. The results list only includes the recommendations whose identifier is one of the specified filter values.
+  `status` - Accepts a list of recommendation statuses.

  Valid values:
  +  `active` - The recommendations which are ready for you to apply.
  +  `pending` - The applied or scheduled recommendations which are in progress.
  +  `resolved` - The recommendations which are completed.
  +  `dismissed` - The recommendations that you dismissed.

  The results list only includes the recommendations whose status is one of the specified filter values.
+  `severity` - Accepts a list of recommendation severities. The results list only includes the recommendations whose severity is one of the specified filter values.

  Valid values:
  +  `high` 
  +  `medium` 
  +  `low` 
  +  `informational` 
+  `type-id` - Accepts a list of recommendation type identifiers. The results list only includes the recommendations whose type is one of the specified filter values.
+  `dbi-resource-id` - Accepts a list of database resource identifiers. The results list only includes the recommendations that generated for the specified databases.
+  `cluster-resource-id` - Accepts a list of cluster resource identifiers. The results list only includes the recommendations that generated for the specified clusters.
+  `pg-arn` - Accepts a list of parameter group ARNs. The results list only includes the recommendations that generated for the specified parameter groups.
+  `cluster-pg-arn` - Accepts a list of cluster parameter group ARNs. The results list only includes the recommendations that generated for the specified cluster parameter groups.
Type: Array of [Filter](API_Filter.md) objects  
Required: No

 ** LastUpdatedAfter **   
A filter to include only the recommendations that were updated after this specified time.  
Type: Timestamp  
Required: No

 ** LastUpdatedBefore **   
A filter to include only the recommendations that were updated before this specified time.  
Type: Timestamp  
Required: No

 ** Locale **   
The language that you choose to return the list of recommendations.  
Valid values:  
+  `en` 
+  `en_UK` 
+  `de` 
+  `es` 
+  `fr` 
+  `id` 
+  `it` 
+  `ja` 
+  `ko` 
+  `pt_BR` 
+  `zh_TW` 
+  `zh_CN` 
Type: String  
Required: No

 ** Marker **   
An optional pagination token provided by a previous `DescribeDBRecommendations` request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.   
Type: String  
Required: No

 ** MaxRecords **   
The maximum number of recommendations to include in the response. If more records exist than the specified `MaxRecords` value, a pagination token called a marker is included in the response so that you can retrieve the remaining results.  
Type: Integer  
Required: No

## Response Elements
<a name="API_DescribeDBRecommendations_ResponseElements"></a>

The following elements are returned by the service.

 **DBRecommendations.member.N**   
A list of recommendations which is returned from `DescribeDBRecommendations` API request.  
Type: Array of [DBRecommendation](API_DBRecommendation.md) objects

 ** Marker **   
An optional pagination token provided by a previous `DBRecommendationsMessage` request. This token can be used later in a `DescribeDBRecomendations` request.   
Type: String

## Errors
<a name="API_DescribeDBRecommendations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeDBRecommendations_Examples"></a>

### Describing all the recommendations in the account
<a name="API_DescribeDBRecommendations_Example_1"></a>

This example illustrates one usage of DescribeDBRecommendations.

#### Sample Request
<a name="API_DescribeDBRecommendations_Example_1_Request"></a>

```
  https://rds.us-east-1.amazonaws.com/
    ?Action=DescribeDBRecommendations
    &SignatureMethod=HmacSHA256
    &SignatureVersion=4
    &Version=2014-10-31
    &X-Amz-Algorithm=AWS4-HMAC-SHA256
    &X-Amz-Credential=AKIADQKE4SARGYLE/20230222/us-east-1/rds/aws4_request
    &X-Amz-Date=20230222T200807Z
    &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
    &X-Amz-Signature=2d4f2b9e8abc31122b5546f94c0499bba47de813cb875f9b9c78e8e19c9afe1b
```

#### Sample Response
<a name="API_DescribeDBRecommendations_Example_1_Response"></a>

```
  <DescribeDBRecommendationsResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/">
  <DescribeDBRecommendationsResult>
    <DBRecommendations>
      <member>
        <RecommendationId>15e811d7-ec23-4d94-8d28-74cd2e7729ad</RecommendationId>
        <TypeId>config_recommendation::multi_az_instance</TypeId>
        <Severity>low</Severity>
        <ResourceArn>arn:aws:rds:us-west-2:636812126935:db:mariadb-instance</ResourceArn>
        <Status>active</Status>
        <CreatedTime>2023-10-05T18:04:04.017000+00:00</CreatedTime>
        <UpdatedTime>2023-10-20T18:35:46+00:00</UpdatedTime>
        <Detection>**1 resource** is not a Multi-AZ instance</Detection>
        <Recommendation>Set up Multi-AZ for the impacted DB instances</Recommendation>
        <Description>We recommend that you use Multi-AZ deployment. The Multi-AZ deployments enhance the availability and durability of the DB instance. Click Info for more details about Multi-AZ deployment and pricing.</Description>
        <RecommendedActions>
          <member>
            <ActionId>806effbdc8853c4bf0e794c0c240ee8e</ActionId>
            <Operation>modifyDbInstance</Operation>
            <Parameters>
              <member>
                <Key>MultiAZ</Key>
                <Value>true</Value>
              </member>
              <member>
                <Key>DBInstanceIdentifier</Key>
                <Value>mariadb-instance</Value>
              </member>
            </Parameters>
            <ApplyModes>
              <member>immediately</member>
              <member>next-maintenance-window</member>
            </ApplyModes>
            <Status>ready</Status>
            <ContextAttributes>
              <member>
                <Key>resourceArn</Key>
                <Value>arn:aws:rds:us-west-2:636812126935:db:mariadb-instance</Value>
              </member>
            </ContextAttributes>
            <ContextAttributes>
              <member>
                <Key>engineName</Key>
                <Value>mariadb</Value>
              </member>
            </ContextAttributes>
          </member>
        </RecommendedActions>
        <Category>reliability</Category>
        <Source>RDS</Source>
        <TypeDetection>**[resource-count] resources** are not Multi-AZ instances</TypeDetection>
        <TypeRecommendation>Set up Multi-AZ for the impacted DB instances</TypeRecommendation>
        <Impact>Data availability at risk</Impact>
        <AdditionalInfo>In an Amazon RDS Multi-AZ deployment, Amazon RDS automatically creates a primary database instance and replicates the data to an instance in a different availability zone. When it detects a failure, Amazon RDS automatically fails over to a standby instance without manual intervention.</AdditionalInfo>
        <Links>
          <member>
            <Text>Pricing for Amazon RDS Multi-AZ</Text>
            <Url>https://aws.amazon.com/rds/features/multi-az/#Pricing</Url>
          </member>
        </Links>
      </member>
      <member>
        <RecommendationId>8c9132b0-267d-4493-b3c4-aedd0920809d</RecommendationId>
        <TypeId>config_recommendation::enhanced_monitoring_off</TypeId>
        <Severity>low</Severity>
        <ResourceArn>arn:aws:rds:us-west-2:636812126935:db:mariadb-instance</ResourceArn>
        <Status>active</Status>
        <CreatedTime>2023-10-05T18:04:03.957000+00:00</CreatedTime>
        <UpdatedTime>2023-10-20T18:35:46+00:00</UpdatedTime>
        <Detection>**1 resource** doesn't have Enhanced Monitoring enabled</Detection>
        <Recommendation>Turn on Enhanced Monitoring</Recommendation>
        <Description>Your database resources don't have Enhanced Monitoring turned on. Enhanced Monitoring provides real-time operating system metrics for monitoring and troubleshooting.</Description>
        <RecommendedActions>
          <member>
            <ActionId>a2e5e55f28854f9ec12f45c227d85f48</ActionId>
            <Operation>modifyDbInstance</Operation>
            <Parameters>
              <member>
                <Key>MonitoringInterval</Key>
                <Value>60</Value>
              </member>
              <member>
                <Key>DBInstanceIdentifier</Key>
                <Value>mariadb-instance</Value>
              </member>
            </Parameters>
            <ApplyModes>
              <member>immediately</member>
            </ApplyModes>
            <Status>ready</Status>
            <ContextAttributes>
              <member>
                <Key>resourceArn</Key>
                <Value>arn:aws:rds:us-west-2:636812126935:db:mariadb-instance</Value>
              </member>
              <member>
                <Key>engineName</Key>
                <Value>mariadb</Value>
              </member>
              <member>
                <Key>recommendedValue</Key>
                <Value>60</Value>
              </member>
            </ContextAttributes>
          </member>
        </RecommendedActions>
        <Category>reliability</Category>
        <Source>RDS</Source>
        <TypeDetection>**[resource-count] resources** don't have Enhanced Monitoring enabled</TypeDetection>
        <TypeRecommendation>Turn on Enhanced Monitoring</TypeRecommendation>
        <Impact>Reduced operational visibility</Impact>
        <AdditionalInfo>Enhanced Monitoring for Amazon RDS provides additional visibility on the health of your DB instances. We recommend that you turn on Enhanced Monitoring. When the Enhanced Monitoring option is turned on for your DB instance, it collects vital operating system metrics and process information.</AdditionalInfo>
        <Links>
          <member>
            <Text>Turning Enhanced Monitoring on and off</Text>
            <Url>https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.OS.html</Url>
          </member>
        </Links>
      </member>
      <member>
        <RecommendationId>bdbda802-2472-406f-a7bc-e17ee5836a76</RecommendationId>
        <TypeId>performance_recommendation::temp_tables_on_disk</TypeId>
        <Severity>high</Severity>
        <ResourceArn>arn:aws:rds:us-west-2:636812126935:db:mysql-instance</ResourceArn>
        <Status>active</Status>
        <CreatedTime>2023-10-05T17:11:07.307000+00:00</CreatedTime>
        <UpdatedTime>2023-10-13T18:40:33+00:00</UpdatedTime>
        <Detection>Instance [resource-name] is creating temporary tables on disk</Detection>
        <Recommendation>Review memory parameters and tune queries</Recommendation>
        <Description>Based on your usage, we recommend the following:  \n  \n* Review memory parameters and tune queries. For example:\n\t* Use the TempTable storage engine in MySQL 8.0.\n\t* Tune the database parameters tmp_table_size and max_heap_table_size.\n\t* Select only necessary columns and avoid using BLOB and TEXT columns.\n\t* Index columns involved in sorting and grouping.\n\t* Reduce the data returned by your queries. Investigate them by querying sys.statements_with_temp_table.\n* [View troubleshooting doc](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/proactive-insights.temp-tables.html)  \n  \n@> Why do we recommend this?  \nWhen temporary data can't fit in memory, the database uses on-disk temporary tables. These tables can decrease performance, increase the duration of scheduled upgrades, and increase the IOPS rate.  \n  \nWithin 15 minutes, the database created more than 2 temporary tables per second and more than 50% of all temporary tables used disk.  \n@></Description>
        <RecommendedActions/>
        <Category>performance</Category>
        <Source>RDS</Source>
        <Impact>Database performance degradation</Impact>
        <IssueDetails>
          <PerformanceIssueDetails>
            <StartTime>2023-09-11T19:00:21+00:00</StartTime>
            <Metrics>
              <member>
                <Name>Temporary Tables On Disk</Name>
                <References>
                  <member>
                    <Name>Temp Tables on Disk Rate</Name>
                    <ReferenceDetails>
                      <ScalarReferenceDetails>
                        <Value>2</Value>
                      </ScalarReferenceDetails>
                    </ReferenceDetails>
                  </member>
                </References>
                <StatisticsDetails>==Peak value: 3==  \nMedium severity threshold: 2  \nHigh severity threshold: -</StatisticsDetails>
                <MetricQuery>
                  <PerformanceInsightsMetricQuery>
                    <Metric>db.Temp.Created_tmp_disk_tables.avg</Metric>
                  </PerformanceInsightsMetricQuery>
                </MetricQuery>
              </member>
              <member>
                <Name>Percentage of the temporary tables created that use disk</Name>
                <References>
                  <member>
                    <Name>Temp Tables on Disk Percent</Name>
                    <ReferenceDetails>
                      <ScalarReferenceDetails>
                        <Value>50</Value>
                      </ScalarReferenceDetails>
                    </ReferenceDetails>
                  </member>
                </References>
                <StatisticsDetails>==Peak value: 59==  \nMedium severity threshold: 50  \nHigh severity threshold: -</StatisticsDetails>
                <MetricQuery>
                  <PerformanceInsightsMetricQuery>
                    <Metric>db.Temp.temp_disk_tables_percent.avg</Metric>
                  </PerformanceInsightsMetricQuery>
                </MetricQuery>
              </member>
              <member>
                <Name>Total Created Temporary Tables</Name>
                <StatisticsDetails>==Peak value: -==  \nMedium severity threshold: -  \nHigh severity threshold: -</StatisticsDetails>
                <MetricQuery>
                  <PerformanceInsightsMetricQuery>
                    <Metric>db.Temp.Created_tmp_tables.max</Metric>
                  </PerformanceInsightsMetricQuery>
                </MetricQuery>
              </member>
            </Metrics>
            <Analysis>Starting on 09/11/2023 19:00:21, your recent on-disk temporary table usage increased significantly, up to 58.82 percent. The database is creating up to 3 temporary tables per second on disk, which might impact performance. This insight appears because both the percentage of temporary tables on disk and the rate of temporary tables on disk created per second exceeded their thresholds.</Analysis>
          </PerformanceIssueDetails>
        </IssueDetails>
      </member>
    </DBRecommendations>
  </DescribeDBRecommendationsResult>
</DescribeDBRecommendationsResponse>
```

### Filtering the recommendations by last updated time
<a name="API_DescribeDBRecommendations_Example_2"></a>

This example illustrates one usage of DescribeDBRecommendations.

#### Sample Request
<a name="API_DescribeDBRecommendations_Example_2_Request"></a>

```
https://rds.us-east-1.amazonaws.com/
    ?Action=DescribeDBRecommendations
    &LastUpdatedBefore=2023-10-21
    &LastUpdatedAfter=2023-10-19
    &SignatureMethod=HmacSHA256
    &SignatureVersion=4
    &Version=2014-10-31
    &X-Amz-Algorithm=AWS4-HMAC-SHA256
    &X-Amz-Credential=AKIADQKE4SARGYLE/20230222/us-east-1/rds/aws4_request
    &X-Amz-Date=20230222T200807Z
    &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
    &X-Amz-Signature=2d4f2b9e8abc31122b5546f94c0499bba47de813cb875f9b9c78e8e19c9afe1b
```

#### Sample Response
<a name="API_DescribeDBRecommendations_Example_2_Response"></a>

```
<DescribeDBRecommendationsResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/">
  <DescribeDBRecommendationsResult>
    <DBRecommendations>
      <member>
        <RecommendationId>15e811d7-ec23-4d94-8d28-74cd2e7729ad</RecommendationId>
        <TypeId>config_recommendation::multi_az_instance</TypeId>
        <Severity>low</Severity>
        <ResourceArn>arn:aws:rds:us-west-2:636812126935:db:mariadb-instance</ResourceArn>
        <Status>active</Status>
        <CreatedTime>2023-10-05T18:04:04.017000+00:00</CreatedTime>
        <UpdatedTime>2023-10-20T18:35:46+00:00</UpdatedTime>
        <Detection>**1 resource** is not a Multi-AZ instance</Detection>
        <Recommendation>Set up Multi-AZ for the impacted DB instances</Recommendation>
        <Description>We recommend that you use Multi-AZ deployment. The Multi-AZ deployments enhance the availability and durability of the DB instance. Click Info for more details about Multi-AZ deployment and pricing.</Description>
        <RecommendedActions>
          <member>
            <ActionId>806effbdc8853c4bf0e794c0c240ee8e</ActionId>
            <Operation>modifyDbInstance</Operation>
            <Parameters>
              <member>
                <Key>MultiAZ</Key>
                <Value>true</Value>
              </member>
              <member>
                <Key>DBInstanceIdentifier</Key>
                <Value>mariadb-instance</Value>
              </member>
            </Parameters>
            <ApplyModes>
              <member>immediately</member>
              <member>next-maintenance-window</member>
            </ApplyModes>
            <Status>ready</Status>
            <ContextAttributes>
              <member>
                <Key>resourceArn</Key>
                <Value>arn:aws:rds:us-west-2:636812126935:db:mariadb-instance</Value>
              </member>
            </ContextAttributes>
            <ContextAttributes>
              <member>
                <Key>engineName</Key>
                <Value>mariadb</Value>
              </member>
            </ContextAttributes>
          </member>
        </RecommendedActions>
        <Category>reliability</Category>
        <Source>RDS</Source>
        <TypeDetection>**[resource-count] resources** are not Multi-AZ instances</TypeDetection>
        <TypeRecommendation>Set up Multi-AZ for the impacted DB instances</TypeRecommendation>
        <Impact>Data availability at risk</Impact>
        <AdditionalInfo>In an Amazon RDS Multi-AZ deployment, Amazon RDS automatically creates a primary database instance and replicates the data to an instance in a different availability zone. When it detects a failure, Amazon RDS automatically fails over to a standby instance without manual intervention.</AdditionalInfo>
        <Links>
          <member>
            <Text>Pricing for Amazon RDS Multi-AZ</Text>
            <Url>https://aws.amazon.com/rds/features/multi-az/#Pricing</Url>
          </member>
        </Links>
      </member>
      <member>
        <RecommendationId>8c9132b0-267d-4493-b3c4-aedd0920809d</RecommendationId>
        <TypeId>config_recommendation::enhanced_monitoring_off</TypeId>
        <Severity>low</Severity>
        <ResourceArn>arn:aws:rds:us-west-2:636812126935:db:mariadb-instance</ResourceArn>
        <Status>active</Status>
        <CreatedTime>2023-10-05T18:04:03.957000+00:00</CreatedTime>
        <UpdatedTime>2023-10-20T18:35:46+00:00</UpdatedTime>
        <Detection>**1 resource** doesn't have Enhanced Monitoring enabled</Detection>
        <Recommendation>Turn on Enhanced Monitoring</Recommendation>
        <Description>Your database resources don't have Enhanced Monitoring turned on. Enhanced Monitoring provides real-time operating system metrics for monitoring and troubleshooting.</Description>
        <RecommendedActions>
          <member>
            <ActionId>a2e5e55f28854f9ec12f45c227d85f48</ActionId>
            <Operation>modifyDbInstance</Operation>
            <Parameters>
              <member>
                <Key>MonitoringInterval</Key>
                <Value>60</Value>
              </member>
              <member>
                <Key>DBInstanceIdentifier</Key>
                <Value>mariadb-instance</Value>
              </member>
            </Parameters>
            <ApplyModes>
              <member>immediately</member>
            </ApplyModes>
            <Status>ready</Status>
            <ContextAttributes>
              <member>
                <Key>resourceArn</Key>
                <Value>arn:aws:rds:us-west-2:636812126935:db:mariadb-instance</Value>
              </member>
              <member>
                <Key>engineName</Key>
                <Value>mariadb</Value>
              </member>
              <member>
                <Key>recommendedValue</Key>
                <Value>60</Value>
              </member>
            </ContextAttributes>
          </member>
        </RecommendedActions>
        <Category>reliability</Category>
        <Source>RDS</Source>
        <TypeDetection>**[resource-count] resources** don't have Enhanced Monitoring enabled</TypeDetection>
        <TypeRecommendation>Turn on Enhanced Monitoring</TypeRecommendation>
        <Impact>Reduced operational visibility</Impact>
        <AdditionalInfo>Enhanced Monitoring for Amazon RDS provides additional visibility on the health of your DB instances. We recommend that you turn on Enhanced Monitoring. When the Enhanced Monitoring option is turned on for your DB instance, it collects vital operating system metrics and process information.</AdditionalInfo>
        <Links>
          <member>
            <Text>Turning Enhanced Monitoring on and off</Text>
            <Url>https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.OS.html</Url>
          </member>
        </Links>
      </member>
    </DBRecommendations>
  </DescribeDBRecommendationsResult>
</DescribeDBRecommendationsResponse>
```

## See Also
<a name="API_DescribeDBRecommendations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/DescribeDBRecommendations) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/DescribeDBRecommendations) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DescribeDBRecommendations) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/DescribeDBRecommendations) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DescribeDBRecommendations) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/DescribeDBRecommendations) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/DescribeDBRecommendations) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/DescribeDBRecommendations) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/DescribeDBRecommendations) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DescribeDBRecommendations) 