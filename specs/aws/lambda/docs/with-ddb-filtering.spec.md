---
id: "@specs/aws/lambda/docs/with-ddb-filtering"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Event filtering"
status: active
depends_on:
  - "@specs/aws/lambda/meta"
---

# Event filtering

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lambda/docs/with-ddb-filtering
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Using event filtering with a DynamoDB event source
<a name="with-ddb-filtering"></a>

You can use event filtering to control which records from a stream or queue Lambda sends to your function. For general information about how event filtering works, see [Control which events Lambda sends to your function](invocation-eventfiltering.md).

This section focuses on event filtering for DynamoDB event sources.

**Note**  
DynamoDB event source mappings only support filtering on the `dynamodb` key.

**Topics**
+ [DynamoDB event](#filtering-ddb)
+ [Filtering with table attributes](#filtering-ddb-attributes)
+ [Filtering with Boolean expressions](#filtering-ddb-boolean)
+ [Using the Exists operator](#filtering-ddb-exists)
+ [JSON format for DynamoDB filtering](#filtering-ddb-JSON-format)

## DynamoDB event
<a name="filtering-ddb"></a>

Suppose you have a DynamoDB table with the primary key `CustomerName` and attributes `AccountManager` and `PaymentTerms`. The following shows an example record from your DynamoDB table’s stream.

```
{
      "eventID": "1",
      "eventVersion": "1.0",
      "dynamodb": {
          "ApproximateCreationDateTime": "1678831218.0",
          "Keys": {
              "CustomerName": {
                  "S": "AnyCompany Industries"
              }
          },
          "NewImage": {
              "AccountManager": {
                  "S": "Pat Candella"
              },
              "PaymentTerms": {
                  "S": "60 days"
              },
              "CustomerName": {
                  "S": "AnyCompany Industries"
              }
          },
          "SequenceNumber": "111",
          "SizeBytes": 26,
          "StreamViewType": "NEW_IMAGE"
      }
  }
```

To filter based on the key and attribute values in your DynamoDB table, use the `dynamodb` key in the record. The following sections provide examples for different filter types.

### Filtering with table keys
<a name="filtering-ddb-keys"></a>

Suppose you want your function to process only those records where the primary key `CustomerName` is “AnyCompany Industries.” The `FilterCriteria` object would be as follows.

```
{
     "Filters": [
          {
              "Pattern": "{ \"dynamodb\" : { \"Keys\" : { \"CustomerName\" : { \"S\" : [ \"AnyCompany Industries\" ] } } } }"
          }
      ]
 }
```

For added clarity, here is the value of the filter's `Pattern` expanded in plain JSON. 

```
{
     "dynamodb": {
          "Keys": {
              "CustomerName": {
                  "S": [ "AnyCompany Industries" ]
                  }
              }
          }
 }
```

You can add your filter using the console, AWS CLI or an AWS SAM template.

------
#### [ Console ]

To add this filter using the console, follow the instructions in [Attaching filter criteria to an event source mapping (console)](invocation-eventfiltering.md#filtering-console) and enter the following string for the **Filter criteria**.

```
{ "dynamodb" : { "Keys" : { "CustomerName" : { "S" : [ "AnyCompany Industries" ] } } } }
```

------
#### [ AWS CLI ]

To create a new event source mapping with these filter criteria using the AWS Command Line Interface (AWS CLI), run the following command.

```
aws lambda create-event-source-mapping \
    --function-name {{my-function}} \
    --event-source-arn {{arn:aws:dynamodb:us-east-2:123456789012:table/my-table}} \
    --filter-criteria '{"Filters": [{"Pattern": "{ \"dynamodb\" : { \"Keys\" : { \"CustomerName\" : { \"S\" : [ \"AnyCompany Industries\" ] } } } }"}]}'
```

To add these filter criteria to an existing event source mapping, run the following command.

```
aws lambda update-event-source-mapping \
    --uuid {{"a1b2c3d4-5678-90ab-cdef-11111EXAMPLE"}} \
    --filter-criteria '{"Filters": [{"Pattern": "{ \"dynamodb\" : { \"Keys\" : { \"CustomerName\" : { \"S\" : [ \"AnyCompany Industries\" ] } } } }"}]}'
```

------
#### [ AWS SAM ]

To add this filter using AWS SAM, add the following snippet to the YAML template for your event source.

```
FilterCriteria:
   Filters:
     - Pattern: '{ "dynamodb" : { "Keys" : { "CustomerName" : { "S" : [ "AnyCompany Industries" ] } } } }'
```

------

## Filtering with table attributes
<a name="filtering-ddb-attributes"></a>

With DynamoDB, you can also use the `NewImage` and `OldImage` keys to filter for attribute values. Suppose you want to filter records where the `AccountManager` attribute in the latest table image is “Pat Candella” or "Shirley Rodriguez." The `FilterCriteria` object would be as follows.

```
{
    "Filters": [
        {
            "Pattern": "{ \"dynamodb\" : { \"NewImage\" : { \"AccountManager\" : { \"S\" : [ \"Pat Candella\", \"Shirley Rodriguez\" ] } } } }"
        }
    ]
}
```

For added clarity, here is the value of the filter's `Pattern` expanded in plain JSON.

```
{
    "dynamodb": {
        "NewImage": {
            "AccountManager": {
                "S": [ "Pat Candella", "Shirley Rodriguez" ]
            }
        }
    }
}
```

You can add your filter using the console, AWS CLI or an AWS SAM template.

------
#### [ Console ]

To add this filter using the console, follow the instructions in [Attaching filter criteria to an event source mapping (console)](invocation-eventfiltering.md#filtering-console) and enter the following string for the **Filter criteria**.

```
{ "dynamodb" : { "NewImage" : { "AccountManager" : { "S" : [ "Pat Candella", "Shirley Rodriguez" ] } } } }
```

------
#### [ AWS CLI ]

To create a new event source mapping with these filter criteria using the AWS Command Line Interface (AWS CLI), run the following command.

```
aws lambda create-event-source-mapping \
    --function-name {{my-function}} \
    --event-source-arn {{arn:aws:dynamodb:us-east-2:123456789012:table/my-table}} \
    --filter-criteria '{"Filters": [{"Pattern": "{ \"dynamodb\" : { \"NewImage\" : { \"AccountManager\" : { \"S\" : [ \"Pat Candella\", \"Shirley Rodriguez\" ] } } } }"}]}'
```

To add these filter criteria to an existing event source mapping, run the following command.

```
aws lambda update-event-source-mapping \
    --uuid {{"a1b2c3d4-5678-90ab-cdef-11111EXAMPLE"}} \
    --filter-criteria '{"Filters": [{"Pattern": "{ \"dynamodb\" : { \"NewImage\" : { \"AccountManager\" : { \"S\" : [ \"Pat Candella\", \"Shirley Rodriguez\" ] } } } }"}]}'
```

------
#### [ AWS SAM ]

To add this filter using AWS SAM, add the following snippet to the YAML template for your event source.

```
FilterCriteria:
  Filters:
    - Pattern: '{ "dynamodb" : { "NewImage" : { "AccountManager" : { "S" : [ "Pat Candella", "Shirley Rodriguez" ] } } } }'
```

------

## Filtering with Boolean expressions
<a name="filtering-ddb-boolean"></a>

You can also create filters using Boolean AND expressions. These expressions can include both your table's key and attribute parameters. Suppose you want to filter records where the `NewImage` value of `AccountManager` is "Pat Candella" and the `OldImage` value is "Terry Whitlock". The `FilterCriteria` object would be as follows.

```
{
    "Filters": [
        {
            "Pattern": "{ \"dynamodb\" : { \"NewImage\" : { \"AccountManager\" : { \"S\" : [ \"Pat Candella\" ] } } } , \"dynamodb\" : { \"OldImage\" : { \"AccountManager\" : { \"S\" : [ \"Terry Whitlock\" ] } } } }"
        }
    ]
}
```

For added clarity, here is the value of the filter's `Pattern` expanded in plain JSON.

```
{ 
    "dynamodb" : { 
        "NewImage" : { 
            "AccountManager" : { 
                "S" : [ 
                    "Pat Candella" 
                ] 
            } 
        } 
    }, 
    "dynamodb": { 
        "OldImage": { 
            "AccountManager": { 
                "S": [ 
                    "Terry Whitlock" 
                ] 
            } 
        } 
    } 
}
```

You can add your filter using the console, AWS CLI or an AWS SAM template.

------
#### [ Console ]

To add this filter using the console, follow the instructions in [Attaching filter criteria to an event source mapping (console)](invocation-eventfiltering.md#filtering-console) and enter the following string for the **Filter criteria**.

```
{ "dynamodb" : { "NewImage" : { "AccountManager" : { "S" : [ "Pat Candella" ] } } } , "dynamodb" : { "OldImage" : { "AccountManager" : { "S" : [ "Terry Whitlock" ] } } } }
```

------
#### [ AWS CLI ]

To create a new event source mapping with these filter criteria using the AWS Command Line Interface (AWS CLI), run the following command.

```
aws lambda create-event-source-mapping \
    --function-name {{my-function}} \
    --event-source-arn {{arn:aws:dynamodb:us-east-2:123456789012:table/my-table}} \
    --filter-criteria '{"Filters": [{"Pattern": "{ \"dynamodb\" : { \"NewImage\" : { \"AccountManager\" : { \"S\" : [ \"Pat Candella\" ] } } } , \"dynamodb\" : { \"OldImage\" : { \"AccountManager\" : { \"S\" : [ \"Terry Whitlock\" ] } } } } "}]}'
```

To add these filter criteria to an existing event source mapping, run the following command.

```
aws lambda update-event-source-mapping \
    --uuid {{"a1b2c3d4-5678-90ab-cdef-11111EXAMPLE"}} \
    --filter-criteria '{"Filters": [{"Pattern": "{ \"dynamodb\" : { \"NewImage\" : { \"AccountManager\" : { \"S\" : [ \"Pat Candella\" ] } } } , \"dynamodb\" : { \"OldImage\" : { \"AccountManager\" : { \"S\" : [ \"Terry Whitlock\" ] } } } } "}]}'
```

------
#### [ AWS SAM ]

To add this filter using AWS SAM, add the following snippet to the YAML template for your event source.

```
FilterCriteria:
  Filters:
    - Pattern: '{ "dynamodb" : { "NewImage" : { "AccountManager" : { "S" : [ "Pat Candella" ] } } } , "dynamodb" : { "OldImage" : { "AccountManager" : { "S" : [ "Terry Whitlock" ] } } } }'
```

------

**Note**  
DynamoDB event filtering doesn’t support the use of numeric operators (numeric equals and numeric range). Even if items in your table are stored as numbers, these parameters are converted to strings in the JSON record object.

## Using the Exists operator
<a name="filtering-ddb-exists"></a>

Because of the way that JSON event objects from DynamoDB are structured, using the Exists operator requires special care. The Exists operator only works on leaf nodes in the event JSON, so if your filter pattern uses Exists to test for an intermediate node, it won't work. Consider the following DynamoDB table item:

```
{
  "UserID": {"S": "12345"},
  "Name": {"S": "John Doe"},
  "Organizations": {"L": [
      {"S":"Sales"},
      {"S":"Marketing"},
      {"S":"Support"}
    ]
  }
}
```

You might want to create a filter pattern like the following that would test for events containing `"Organizations"`:

```
{ "dynamodb" : { "NewImage" : { "Organizations" : [ { "exists": true } ] } } }
```

However, this filter pattern would never return a match because `"Organizations"` is not a leaf node. The following example shows how to properly use the Exists operator to construct the desired filter pattern:

```
{ "dynamodb" : { "NewImage" : {"Organizations": {"L": {"S": [ {"exists": true } ] } } } } }
```

## JSON format for DynamoDB filtering
<a name="filtering-ddb-JSON-format"></a>

To properly filter events from DynamoDB sources, both the data field and your filter criteria for the data field (`dynamodb`) must be in valid JSON format. If either field isn't in a valid JSON format, Lambda drops the message or throws an exception. The following table summarizes the specific behavior: 


| Incoming data format | Filter pattern format for data properties | Resulting action | 
| --- | --- | --- | 
| Valid JSON | Valid JSON | Lambda filters based on your filter criteria. | 
| Valid JSON | No filter pattern for data properties | Lambda filters (on the other metadata properties only) based on your filter criteria. | 
| Valid JSON | Non-JSON | Lambda throws an exception at the time of the event source mapping creation or update. The filter pattern for data properties must be in a valid JSON format. | 
| Non-JSON | Valid JSON | Lambda drops the record. | 
| Non-JSON | No filter pattern for data properties | Lambda filters (on the other metadata properties only) based on your filter criteria. | 
| Non-JSON | Non-JSON | Lambda throws an exception at the time of the event source mapping creation or update. The filter pattern for data properties must be in a valid JSON format. | 