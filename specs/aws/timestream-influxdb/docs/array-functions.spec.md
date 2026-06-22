---
id: "@specs/aws/timestream-influxdb/docs/array-functions"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Array functions"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Array functions

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/array-functions
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Array functions
<a name="array-functions"></a>

Timestream for LiveAnalytics supports the following array functions.


| Function | Output data type | Description | 
| --- | --- | --- | 
| array\_distinct(x) | array | Remove duplicate values from the array x.<pre>SELECT array_distinct(ARRAY[1,2,2,3])</pre><br />Example result: `[ 1,2,3 ]` | 
| array\_intersect(x, y) | array | Returns an array of the elements in the intersection of x and y, without duplicates.<pre>SELECT array_intersect(ARRAY[1,2,3], ARRAY[3,4,5])</pre><br />Example result: `[ 3 ]` | 
| array\_union(x, y) | array | Returns an array of the elements in the union of x and y, without duplicates.<pre>SELECT array_union(ARRAY[1,2,3], ARRAY[3,4,5])</pre><br />Example result: `[ 1,2,3,4,5 ]` | 
| array\_except(x, y) | array | Returns an array of elements in x but not in y, without duplicates.<pre>SELECT array_except(ARRAY[1,2,3], ARRAY[3,4,5])</pre><br />Example result: `[ 1,2 ]` | 
| array\_join(x, delimiter, null\_replacement)  | varchar | Concatenates the elements of the given array using the delimiter and an optional string to replace nulls.<pre>SELECT array_join(ARRAY[1,2,3], ';', '')</pre><br />Example result: `1;2;3` | 
| array\_max(x) | same as array elements | Returns the maximum value of input array.<pre>SELECT array_max(ARRAY[1,2,3])</pre><br />Example result: `3` | 
| array\_min(x) | same as array elements | Returns the minimum value of input array.<pre>SELECT array_min(ARRAY[1,2,3])</pre><br />Example result: `1` | 
| array\_position(x, element) | bigint | Returns the position of the first occurrence of the element in array x (or 0 if not found).<pre>SELECT array_position(ARRAY[3,4,5,9], 5)</pre><br />Example result: `3` | 
| array\_remove(x, element) | array | Remove all elements that equal element from array x.<pre>SELECT array_remove(ARRAY[3,4,5,9], 4)</pre><br />Example result: `[ 3,5,9 ]` | 
| array\_sort(x) | array | Sorts and returns the array x. The elements of x must be orderable. Null elements will be placed at the end of the returned array.<pre>SELECT array_sort(ARRAY[6,8,2,9,3])</pre><br />Example result: `[ 2,3,6,8,9 ]` | 
| arrays\_overlap(x, y)  | boolean | Tests if arrays x and y have any non-null elements in common. Returns null if there are no non-null elements in common but either array contains null.<pre>SELECT arrays_overlap(ARRAY[6,8,2,9,3], ARRAY[6,8])</pre><br />Example result: `true` | 
| cardinality(x) | bigint | Returns the size of the array x.<pre>SELECT cardinality(ARRAY[6,8,2,9,3])</pre><br />Example result: `5` | 
| concat(array1, array2, ..., arrayN) | array | Concatenates the arrays array1, array2, ..., arrayN.<pre>SELECT concat(ARRAY[6,8,2,9,3], ARRAY[11,32], ARRAY[6,8,2,0,14])</pre><br />Example result: `[ 6,8,2,9,3,11,32,6,8,2,0,14 ]` | 
| element\_at(array(E), index) | E | Returns element of array at given index. If index < 0, element\_at accesses elements from the last to the first.<pre>SELECT element_at(ARRAY[6,8,2,9,3], 1)</pre><br />Example result: `6` | 
| repeat(element, count)  | array | Repeat element for count times.<pre>SELECT repeat(1, 3)</pre><br />Example result: `[ 1,1,1 ]` | 
| reverse(x) | array | Returns an array which has the reversed order of array x.<pre>SELECT reverse(ARRAY[6,8,2,9,3])</pre><br />Example result: `[ 3,9,2,8,6 ]` | 
| sequence(start, stop) | array(bigint) | Generate a sequence of integers from start to stop, incrementing by 1 if start is less than or equal to stop, otherwise -1.<pre>SELECT sequence(3, 8)</pre><br />Example result: `[ 3,4,5,6,7,8 ]` | 
| sequence(start, stop, step)  | array(bigint) | Generate a sequence of integers from start to stop, incrementing by step.<pre>SELECT sequence(3, 15, 2)</pre><br />Example result: `[ 3,5,7,9,11,13,15 ]` | 
| sequence(start, stop)  | array(timestamp) | Generate a sequence of timestamps from start date to stop date, incrementing by 1 day.<pre>SELECT sequence('2023-04-02 19:26:12.941000000', '2023-04-06 19:26:12.941000000', 1d)</pre><br />Example result: `[ 2023-04-02 19:26:12.941000000,2023-04-03 19:26:12.941000000,2023-04-04 19:26:12.941000000,2023-04-05 19:26:12.941000000,2023-04-06 19:26:12.941000000 ]` | 
| sequence(start, stop, step)  | array(timestamp) | Generate a sequence of timestamps from start to stop, incrementing by step. The data type of step is interval.<pre>SELECT sequence('2023-04-02 19:26:12.941000000', '2023-04-10 19:26:12.941000000', 2d)</pre><br />Example result: `[ 2023-04-02 19:26:12.941000000,2023-04-04 19:26:12.941000000,2023-04-06 19:26:12.941000000,2023-04-08 19:26:12.941000000,2023-04-10 19:26:12.941000000 ]` | 
| shuffle(x) | array | Generate a random permutation of the given array x.<pre>SELECT shuffle(ARRAY[6,8,2,9,3])</pre><br />Example result: `[ 6,3,2,9,8 ]` | 
| slice(x, start, length) | array | Subsets array x starting from index start (or starting from the end if start is negative) with a length of length.<pre>SELECT slice(ARRAY[6,8,2,9,3], 1, 3)</pre><br />Example result: `[ 6,8,2 ]` | 
| zip(array1, array2[, ...]) | array(row) | Merges the given arrays, element-wise, into a single array of rows. If the arguments have an uneven length, missing values are filled with NULL.<pre>SELECT zip(ARRAY[6,8,2,9,3], ARRAY[15,24])</pre><br />Example result: `[ ( 6, 15 ),( 8, 24 ),( 2, - ),( 9, - ),( 3, - ) ]` | 