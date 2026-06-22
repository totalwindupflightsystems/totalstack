---
id: "@specs/aws/timestream-influxdb/docs/regex-functions"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Regular expression functions"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Regular expression functions

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/regex-functions
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Regular expression functions
<a name="regex-functions"></a>

The regular expression functions in Timestream for LiveAnalytics support the [Java pattern syntax](http://docs.oracle.com/javase/8/docs/api/java/util/regex/Pattern.html). Timestream for LiveAnalytics supports the following regular expression functions.


| Function | Output data type | Description | 
| --- | --- | --- | 
| regexp\_extract\_all(string, pattern) | array(varchar) | Returns the substring(s) matched by the regular expression pattern in string.<pre>SELECT regexp_extract_all('example expect complex', 'ex\w')</pre><br />Example result: `[ exa,exp ]` | 
| regexp\_extract\_all(string, pattern, group) | array(varchar) | Finds all occurrences of the regular expression pattern in string and returns the [capturing group number](http://docs.oracle.com/javase/8/docs/api/java/util/regex/Pattern.html#gnumber) group.<pre>SELECT regexp_extract_all('example expect complex', '(ex)(\w)', 2)</pre><br />Example result: `[ a,p ]` | 
| regexp\_extract(string, pattern) | varchar | Returns the first substring matched by the regular expression pattern in string.<pre>SELECT regexp_extract('example expect', 'ex\w')</pre><br />Example result: `exa` | 
| regexp\_extract(string, pattern, group)  | varchar | Finds the first occurrence of the regular expression pattern in string and returns the [capturing group number](http://docs.oracle.com/javase/8/docs/api/java/util/regex/Pattern.html#gnumber) group.<pre>SELECT regexp_extract('example expect', '(ex)(\w)', 2)</pre><br />Example result: `a` | 
| regexp\_like(string, pattern)  | boolean | Evaluates the regular expression pattern and determines if it is contained within string. This function is similar to the LIKE operator, except that the pattern only needs to be contained within string, rather than needing to match all of string. In other words, this performs a contains operation rather than a match operation. You can match the entire string by anchoring the pattern using ^ and $.<pre>SELECT regexp_like('example', 'ex')</pre><br />Example result: `true` | 
| regexp\_replace(string, pattern) | varchar | Removes every instance of the substring matched by the regular expression pattern from string.<pre>SELECT regexp_replace('example expect', 'expect')</pre><br />Example result: `example` | 
| regexp\_replace(string, pattern, replacement)  | varchar | Replaces every instance of the substring matched by the regex pattern in string with replacement. Capturing groups can be referenced in replacement using $g for a numbered group or ${name} for a named group. A dollar sign ($) may be included in the replacement by escaping it with a backslash (\\$).<pre>SELECT regexp_replace('example expect', 'expect', 'surprise')</pre><br />Example result: `example surprise` | 
| regexp\_replace(string, pattern, function)  | varchar | Replaces every instance of the substring matched by the regular expression pattern in string using function. The [lambda expression](https://prestodb.io/docs/current/functions/lambda.html) function is invoked for each match with the capturing groups passed as an array. Capturing group numbers start at one; there is no group for the entire match (if you need this, surround the entire expression with parenthesis).<pre>SELECT regexp_replace('example', '(\w)', x -> upper(x[1]))</pre><br />Example result: `EXAMPLE` | 
| regexp\_split(string, pattern)  | array(varchar) | Splits string using the regular expression pattern and returns an array. Trailing empty strings are preserved.<pre>SELECT regexp_split('example', 'x')</pre><br />Example result: `[ e,ample ]` | 