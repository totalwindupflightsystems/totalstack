---
id: "@specs/aws/timestream-influxdb/docs/string-functions"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS String functions"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# String functions

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/string-functions
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# String functions
<a name="string-functions"></a>

**Note**  
The input data type of these functions is assumed to be varchar unless otherwise specified.


| Function | Output data type | Description | 
| --- | --- | --- | 
| chr(n)  | varchar | Returns the Unicode code point n as a varchar. | 
| codepoint(x)  | integer | Returns the Unicode code point of the only character of str. | 
| concat(x1, ..., xN) | varchar | Returns the concatenation of x1, x2, ..., xN. | 
| hamming\_distance(x1,x2)  | bigint | Returns the Hamming distance of x1 and x2, i.e. the number of positions at which the corresponding characters are different. Note that the two varchar inputs must have the same length. | 
| length(x) | bigint | Returns the length of x in characters. | 
| levenshtein\_distance(x1, x2)  | bigint | Returns the Levenshtein edit distance of x1 and x2, i.e. the minimum number of single-character edits (insertions, deletions or substitutions) needed to change x1 into x2. | 
| lower(x) | varchar | Converts x to lowercase. | 
| lpad(x1, bigint size, x2) | varchar | Left pads x1 to size characters with x2. If size is less than the length of x1, the result is truncated to size characters. size must not be negative and x2 must be non-empty. | 
| ltrim(x) | varchar | Removes leading whitespace from x. | 
| replace(x1, x2) | varchar | Removes all instances of x2 from x1. | 
| replace(x1, x2, x3) | varchar | Replaces all instances of x2 with x3 in x1. | 
| Reverse(x)  | varchar | Returns x with the characters in reverse order. | 
| rpad(x1, bigint size, x2) | varchar | Right pads x1 to size characters with x2. If size is less than the length of x1, the result is truncated to size characters. size must not be negative and x2 must be non-empty. | 
| rtrim(x) | varchar | Removes trailing whitespace from x. | 
| split(x1, x2) | array(varchar) | Splits x1 on delimiter x2 and returns an array. | 
| split(x1, x2, bigint limit) | array(varchar) | Splits x1 on delimiter x2 and returns an array. The last element in the array always contain everything left in the x1. limit must be a positive number. | 
| split\_part(x1, x2, bigint pos)  | varchar | Splits x1 on delimiter x2 and returns the varchar field at pos. Field indexes start with 1. If pos is larger than the number of fields, then null is returned. | 
| strpos(x1, x2)  | bigint | Returns the starting position of the first instance of x2 in x1. Positions start with 1. If not found, 0 is returned. | 
| strpos(x1, x2,bigint instance)  | bigint | Returns the position of the Nth instance of x2 in x1. Instance must be a positive number. Positions start with 1. If not found, 0 is returned. | 
| strrpos(x1, x2)  | bigint | Returns the starting position of the last instance of x2 in x1. Positions start with 1. If not found, 0 is returned. | 
| strrpos(x1, x2, bigint instance)  | bigint | Returns the position of the Nth instance of x2 in x1 starting from the end of x1. instance must be a positive number. Positions start with 1. If not found, 0 is returned. | 
| position(x2 IN x1)  | bigint | Returns the starting position of the first instance of x2 in x1. Positions start with 1. If not found, 0 is returned. | 
| substr(x, bigint start)  | varchar | Returns the rest of x from the starting position start. Positions start with 1. A negative starting position is interpreted as being relative to the end of x. | 
| substr(x, bigint start, bigint len)  | varchar | Returns a substring from x of length len from the starting position start. Positions start with 1. A negative starting position is interpreted as being relative to the end of x. | 
| trim(x)  | varchar | Removes leading and trailing whitespace from x. | 
| upper(x)  | varchar | Converts x to uppercase. | 