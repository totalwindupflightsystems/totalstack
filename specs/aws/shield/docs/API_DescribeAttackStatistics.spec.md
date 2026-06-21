---
id: "@specs/aws/shield/docs/API_DescribeAttackStatistics"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeAttackStatistics"
status: active
depends_on:
  - "@specs/aws/shield/meta"
---

# DescribeAttackStatistics

> **source:** AWS Documentation
> **spec:id:** @specs/aws/shield/docs/API_DescribeAttackStatistics
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeAttackStatistics
<a name="API_DescribeAttackStatistics"></a>

Provides information about the number and type of attacks AWS Shield has detected in the last year for all resources that belong to your account, regardless of whether you've defined Shield protections for them. This operation is available to Shield customers as well as to Shield Advanced customers.

The operation returns data for the time range of midnight UTC, one year ago, to midnight UTC, today. For example, if the current time is `2020-10-26 15:39:32 PDT`, equal to `2020-10-26 22:39:32 UTC`, then the time range for the attack data returned is from `2019-10-26 00:00:00 UTC` to `2020-10-26 00:00:00 UTC`. 

The time range indicates the period covered by the attack statistics data items.

## Response Syntax
<a name="API_DescribeAttackStatistics_ResponseSyntax"></a>

```
{
   "DataItems": [ 
      { 
         "AttackCount": number,
         "AttackVolume": { 
            "BitsPerSecond": { 
               "Max": number
            },
            "PacketsPerSecond": { 
               "Max": number
            },
            "RequestsPerSecond": { 
               "Max": number
            }
         }
      }
   ],
   "TimeRange": { 
      "FromInclusive": number,
      "ToExclusive": number
   }
}
```

## Response Elements
<a name="API_DescribeAttackStatistics_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DataItems](#API_DescribeAttackStatistics_ResponseSyntax) **   <a name="AWSShield-DescribeAttackStatistics-response-DataItems"></a>
The data that describes the attacks detected during the time period.  
Type: Array of [AttackStatisticsDataItem](API_AttackStatisticsDataItem.md) objects

 ** [TimeRange](#API_DescribeAttackStatistics_ResponseSyntax) **   <a name="AWSShield-DescribeAttackStatistics-response-TimeRange"></a>
The time range of the attack.  
Type: [TimeRange](API_TimeRange.md) object

## Errors
<a name="API_DescribeAttackStatistics_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalErrorException **   
Exception that indicates that a problem occurred with the service infrastructure. You can retry the request.  
HTTP Status Code: 500

## See Also
<a name="API_DescribeAttackStatistics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/shield-2016-06-02/DescribeAttackStatistics) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/shield-2016-06-02/DescribeAttackStatistics) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/shield-2016-06-02/DescribeAttackStatistics) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/shield-2016-06-02/DescribeAttackStatistics) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/shield-2016-06-02/DescribeAttackStatistics) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/shield-2016-06-02/DescribeAttackStatistics) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/shield-2016-06-02/DescribeAttackStatistics) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/shield-2016-06-02/DescribeAttackStatistics) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/shield-2016-06-02/DescribeAttackStatistics) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/shield-2016-06-02/DescribeAttackStatistics) 