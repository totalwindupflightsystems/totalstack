---
id: "@specs/aws/timestream-influxdb/docs/mathematical-functions"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Mathematical functions"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Mathematical functions

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/mathematical-functions
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Mathematical functions
<a name="mathematical-functions"></a>

Timestream for LiveAnalytics supports the following mathematical functions.


| Function | Output data type | Description | 
| --- | --- | --- | 
| abs(x) | [same as input] | Returns the absolute value of x. | 
| cbrt(x) | double | Returns the cube root of x. | 
| ceiling(x) or ceil(x) | [same as input] | Returns x rounded up to the nearest integer. | 
| degrees(x) | double | Converts angle x in radians to degrees. | 
| e() | double | Returns the constant Euler's number. | 
| exp(x) | double | Returns Euler's number raised to the power of x. | 
| floor(x) | [same as input] | Returns x rounded down to the nearest integer. | 
| from\_base(string,radix) | bigint | Returns the value of string interpreted as a base-radix number. | 
| ln(x) | double | Returns the natural logarithm of x. | 
| log2(x) | double | Returns the base 2 logarithm of x. | 
| log10(x) | double | Returns the base 10 logarithm of x. | 
| mod(n,m)  | [same as input] | Returns the modulus (remainder) of n divided by m. | 
| pi()  | double | Returns the constant Pi. | 
| pow(x, p) or power(x, p) | double | Returns x raised to the power of p. | 
| radians(x) | double | Converts angle x in degrees to radians. | 
| rand() or random() | double | Returns a pseudo-random value in the range 0.0 1.0. | 
| random(n) | [same as input] | Returns a pseudo-random number between 0 and n (exclusive). | 
| round(x) | [same as input] | Returns x rounded to the nearest integer. | 
| round(x,d) | [same as input] | Returns x rounded to d decimal places. | 
| sign(x) | [same as input] | Returns the signum function of x, that is:[See the AWS documentation website for more details](http://docs.aws.amazon.com/timestream/latest/developerguide/mathematical-functions.html)<br />For double arguments, the function additionally returns:[See the AWS documentation website for more details](http://docs.aws.amazon.com/timestream/latest/developerguide/mathematical-functions.html) | 
| sqrt(x)  | double | Returns the square root of x. | 
| to\_base(x, radix)  | varchar | Returns the base-radix representation of x. | 
| truncate(x)  | double | Returns x rounded to integer by dropping digits after decimal point. | 
| acos(x) | double | Returns the arc cosine of x. | 
| asin(x)  | double | Returns the arc sine of x. | 
| atan(x)  | double | Returns the arc tangent of x. | 
| atan2(y, x) | double | Returns the arc tangent of y / x. | 
| cos(x) | double | Returns the cosine of x. | 
| cosh(x) | double | Returns the hyperbolic cosine of x. | 
| sin(x)  | double | Returns the sine of x. | 
| tan(x) | double | Returns the tangent of x. | 
| tanh(x) | double | Returns the hyperbolic tangent of x. | 
| infinity() | double | Returns the constant representing positive infinity. | 
| is\_finite(x) | boolean | Determine if x is finite. | 
| is\_infinite(x) | boolean | Determine if x is infinite. | 
| is\_nan(x) | boolean | Determine if x is not-a-number. | 
| nan() | double | Returns the constant representing not-a-number. | 