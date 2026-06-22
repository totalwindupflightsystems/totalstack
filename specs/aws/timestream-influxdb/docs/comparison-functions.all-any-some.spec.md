---
id: "@specs/aws/timestream-influxdb/docs/comparison-functions.all-any-some"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ALL(), ANY() and SOME()"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# ALL(), ANY() and SOME()

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/comparison-functions.all-any-some
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# ALL(), ANY() and SOME()
<a name="comparison-functions.all-any-some"></a>

The `ALL`, `ANY` and `SOME` quantifiers can be used together with comparison operators in the following way.


| Expression | Meaning | 
| --- | --- | 
| A = ALL(...) | Evaluates to true when A is equal to all values. | 
| A <> ALL(...) | Evaluates to true when A does not match any value. | 
| A < ALL(...) | Evaluates to true when A is smaller than the smallest value. | 
| A = ANY(...) | Evaluates to true when A is equal to any of the values.  | 
| A <> ANY(...) | Evaluates to true when A does not match one or more values. | 
| A < ANY(...) | Evaluates to true when A is smaller than the biggest value. | 

## Examples and usage notes
<a name="comparison-functions.all-any-some.examples-usage"></a>

**Note**  
When using `ALL`, `ANY` or `SOME`, the keyword `VALUES` should be used if the comparison values are a list of literals. 

## Example: `ANY()`
<a name="w2aab7c59c21c11c11"></a>

An example of `ANY()` in a query statement as follows.

```
SELECT 11.7 = ANY (VALUES 12.0, 13.5, 11.7)
```

An alternative syntax for the same operation is as follows.

```
SELECT 11.7 = ANY (SELECT 12.0 UNION ALL SELECT 13.5 UNION ALL SELECT 11.7)
```

In this case, `ANY()` evaluates to `True`.

## Example: `ALL()`
<a name="w2aab7c59c21c11c13"></a>

An example of `ALL()` in a query statement as follows.

```
SELECT 17 < ALL (VALUES 19, 20, 15);
```

An alternative syntax for the same operation is as follows.

```
SELECT 17 < ALL (SELECT 19 UNION ALL SELECT 20 UNION ALL SELECT 15);
```

In this case, `ALL()` evaluates to `False`.

## Example: `SOME()`
<a name="w2aab7c59c21c11c15"></a>

An example of `SOME()` in a query statement as follows.

```
SELECT 50 >= SOME (VALUES 53, 77, 27);
```

An alternative syntax for the same operation is as follows.

```
SELECT 50 >= SOME (SELECT 53 UNION ALL SELECT 77 UNION ALL SELECT 27);
```

In this case, `SOME()` evaluates to `True`.