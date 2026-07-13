---
id: "@specs/aws/lambda/docs/invocation-eventfiltering"
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
> **spec:id:** @specs/aws/lambda/docs/invocation-eventfiltering
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Control which events Lambda sends to your function
<a name="invocation-eventfiltering"></a>

You can use event filtering to control which records from a stream or queue Lambda sends to your function. For example, you can add a filter so that your function only processes Amazon SQS messages containing certain data parameters. Event filtering works only with certain event source mappings. You can add filters to event source mappings for the following AWS services:
+ Amazon DynamoDB
+ Amazon Kinesis Data Streams
+ Amazon MQ
+ Amazon Managed Streaming for Apache Kafka (Amazon MSK)
+ Self-managed Apache Kafka
+ Amazon Simple Queue Service (Amazon SQS)

For specific information about filtering with specific event sources, see [Using filters with different AWS services](#filtering-by-service). Lambda doesn't support event filtering for Amazon DocumentDB.

By default, you can define up to five different filters for a single event source mapping. Your filters are logically ORed together. If a record from your event source satisfies one or more of your filters, Lambda includes the record in the next event it sends to your function. If none of your filters are satisfied, Lambda discards the record.

**Note**  
If you need to define more than five filters for an event source, you can request a quota increase for up to 10 filters for each event source. If you attempt to add more filters than your current quota permits, Lambda will return an error when you try to create the event source.

**Topics**
+ [Understanding event filtering basics](#filtering-basics)
+ [Handling records that don't meet filter criteria](#filtering-criteria-not-met)
+ [Filter rule syntax](#filtering-syntax)
+ [Attaching filter criteria to an event source mapping (console)](#filtering-console)
+ [Attaching filter criteria to an event source mapping (AWS CLI)](#filtering-cli)
+ [Attaching filter criteria to an event source mapping (AWS SAM)](#filtering-sam)
+ [Encryption of filter criteria](#filter-criteria-encryption)
+ [Using filters with different AWS services](#filtering-by-service)

## Understanding event filtering basics
<a name="filtering-basics"></a>

A filter criteria (`FilterCriteria`) object is a structure that consists of a list of filters (`Filters`). Each filter is a structure that defines an event filtering pattern (`Pattern`). A pattern is a string representation of a JSON filter rule. The structure of a `FilterCriteria` object is as follows.

```
{
   "Filters": [
        {
            "Pattern": "{ \"Metadata1\": [ rule1 ], \"data\": { \"Data1\": [ rule2 ] }}"
        }
    ]
}
```

For added clarity, here is the value of the filter's `Pattern` expanded in plain JSON.

```
{
    "Metadata1": [ rule1 ],
    "data": {
        "Data1": [ rule2 ]
    }
}
```

Your filter pattern can include metadata properties, data properties, or both. The available metadata parameters and the format of the data parameters vary according to the AWS service which is acting as the event source. For example, suppose your event source mapping receives the following record from an Amazon SQS queue:

```
{
    "messageId": "059f36b4-87a3-44ab-83d2-661975830a7d",
    "receiptHandle": "AQEBwJnKyrHigUMZj6rYigCgxlaS3SLy0a...",
    "body": "{\\n \"City\": \"Seattle\",\\n \"State\": \"WA\",\\n \"Temperature\": \"46\"\\n}",
    "attributes": {
        "ApproximateReceiveCount": "1",
        "SentTimestamp": "1545082649183",
        "SenderId": "AIDAIENQZJOLO23YVJ4VO",
        "ApproximateFirstReceiveTimestamp": "1545082649185"
    },
    "messageAttributes": {},
    "md5OfBody": "e4e68fb7bd0e697a0ae8f1bb342846b3",
    "eventSource": "aws:sqs",
    "eventSourceARN": "arn:aws:sqs:us-east-2:123456789012:my-queue",
    "awsRegion": "us-east-2"
}
```
+ **Metadata properties** are the fields containing information about the event that created the record. In the example Amazon SQS record, the metadata properties include fields such as `messageID`, `eventSourceArn`, and `awsRegion`.
+ **Data properties** are the fields of the record containing the data from your stream or queue. In the Amazon SQS event example, the key for the data field is `body`, and the data properties are the fields `City` `State`, and `Temperature`.

Different types of event source use different key values for their data fields. To filter on data properties, make sure that you use the correct key in your filter’s pattern. For a list of data filtering keys, and to see examples of filter patterns for each supported AWS service, refer to [Using filters with different AWS services](#filtering-by-service).

Event filtering can handle multi-level JSON filtering. For example, consider the following fragment of a record from a DynamoDB stream:

```
"dynamodb": {
    "Keys": {
        "ID": {
            "S": "ABCD"
        }
        "Number": {
            "N": "1234"
    },
    ...
}
```

Suppose you want to process only those records where the value of the sort key `Number` is 4567. In this case, your `FilterCriteria` object would look like this:

```
{
    "Filters": [
        {
            "Pattern": "{ \"dynamodb\": { \"Keys\": { \"Number\": { \"N\": [ "4567" ] } } } }"
        }
    ]
}
```

For added clarity, here is the value of the filter's `Pattern` expanded in plain JSON. 

```
{
    "dynamodb": {
        "Keys": {
            "Number": {
                "N": [ "4567" ]
                }
            }
        }
}
```

## Handling records that don't meet filter criteria
<a name="filtering-criteria-not-met"></a>

How Lambda handles records that don't meet your filter criteria depends on the event source.
+ For **Amazon SQS**, if a message doesn't satisfy your filter criteria, Lambda automatically removes the message from the queue. You don't have to manually delete these messages in Amazon SQS.
+ For **Kinesis** and **DynamoDB**, after your filter criteria evaluates a record, the streams iterator advances past this record. If the record doesn't satisfy your filter criteria, you don't have to manually delete the record from your event source. After the retention period, Kinesis and DynamoDB automatically delete these old records. If you want records to be deleted sooner, see [Changing the Data Retention Period](https://docs.aws.amazon.com/streams/latest/dev/kinesis-extended-retention.html).
+ For **Amazon MSK**, **self-managed Apache Kafka**, and **Amazon MQ** messages, Lambda drops messages that don't match all fields included in the filter. For Amazon MSK and self-managed Apache Kafka, Lambda commits offsets for matched and unmatched messages after successfully invoking the function. For Amazon MQ, Lambda acknowledges matched messages after successfully invoking the function, and acknowledges unmatched messages when filtering them.

## Filter rule syntax
<a name="filtering-syntax"></a>

For filter rules, Lambda supports the Amazon EventBridge rules and uses the same syntax as EventBridge. For more information, see [ Amazon EventBridge event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html) in the *Amazon EventBridge User Guide*.

The following is a summary of all the comparison operators available for Lambda event filtering.


| Comparison operator | Example | Rule syntax | 
| --- | --- | --- | 
| Null | UserID is null | "UserID": [ null ] | 
| Empty | LastName is empty | "LastName": [""] | 
| Equals | Name is "Alice" | "Name": [ "Alice" ] | 
| Equals (ignore case) | Name is "Alice" | "Name": [ { "equals-ignore-case": "alice" } ] | 
| And | Location is "New York" and Day is "Monday" | "Location": [ "New York" ], "Day": ["Monday"] | 
| Or | PaymentType is "Credit" or "Debit" | "PaymentType": [ "Credit", "Debit"] | 
| Or (multiple fields) | Location is "New York", or Day is "Monday". | "$or": [ { "Location": [ "New York" ] }, { "Day": [ "Monday" ] } ]  | 
| Not | Weather is anything but "Raining" | "Weather": [ { "anything-but": [ "Raining" ] } ] | 
| Numeric (equals) | Price is 100 | "Price": [ { "numeric": [ "=", 100 ] } ] | 
| Numeric (range) | Price is more than 10, and less than or equal to 20 | "Price": [ { "numeric": [ ">", 10, "<=", 20 ] } ] | 
| Exists | ProductName exists | "ProductName": [ { "exists": true } ] | 
| Does not exist | ProductName does not exist | "ProductName": [ { "exists": false } ] | 
| Begins with | Region is in the US | "Region": [ {"prefix": "us-" } ] | 
| Ends with | FileName ends with a .png extension. | "FileName": [ { "suffix": ".png" } ]  | 

**Note**  
Like EventBridge, for strings, Lambda uses exact character-by-character matching without case-folding or any other string normalization. For numbers, Lambda also uses string representation. For example, 300, 300.0, and 3.0e2 are not considered equal.

Note that the Exists operator only works on leaf nodes in your event source JSON. It doesn't match intermediate nodes. For example, with the following JSON, the filter pattern `{ "person": { "address": [ { "exists": true } ] } }"` wouldn't find a match because `"address"` is an intermediate node.

```
{
  "person": {
    "name": "John Doe",
    "age": 30,
    "address": {
      "street": "123 Main St",
      "city": "Anytown",
      "country": "USA"
    }
  }
}
```

## Attaching filter criteria to an event source mapping (console)
<a name="filtering-console"></a>

Follow these steps to create a new event source mapping with filter criteria using the Lambda console.

**To create a new event source mapping with filter criteria (console)**

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions) of the Lambda console.

1. Choose the name of a function to create an event source mapping for.

1. Under **Function overview**, choose **Add trigger**.

1. For **Trigger configuration**, choose a trigger type that supports event filtering. For a list of supported services, refer to the list at the beginning of this page.

1. Expand **Additional settings**.

1. Under **Filter criteria**, choose **Add**, and then define and enter your filters. For example, you can enter the following.

   ```
   { "Metadata" : [ 1, 2 ] }
   ```

   This instructs Lambda to process only the records where field `Metadata` is equal to 1 or 2. You can continue to select **Add** to add more filters up to the maximum allowed amount.

1. When you have finished adding your filters, choose **Save**.

When you enter filter criteria using the console, you enter only the filter pattern and don't need to provide the `Pattern` key or escape quotes. In step 6 of the preceding instructions, `{ "Metadata" : [ 1, 2 ] }` corresponds to the following `FilterCriteria`.

```
{
   "Filters": [
      {
          "Pattern": "{ \"Metadata\" : [ 1, 2 ] }"
      }
   ]
}
```

After creating your event source mapping in the console, you can see the formatted `FilterCriteria` in the trigger details. For more examples of creating event filters using the console, see [Using filters with different AWS services](#filtering-by-service).

## Attaching filter criteria to an event source mapping (AWS CLI)
<a name="filtering-cli"></a>

Suppose you want an event source mapping to have the following `FilterCriteria`:

```
{
   "Filters": [
      {
          "Pattern": "{ \"Metadata\" : [ 1, 2 ] }"
      }
   ]
}
```

To create a new event source mapping with these filter criteria using the AWS Command Line Interface (AWS CLI), run the following command.

```
aws lambda create-event-source-mapping \
    --function-name {{my-function}} \
    --event-source-arn {{arn:aws:sqs:us-east-2:123456789012:my-queue}} \
    --filter-criteria '{"Filters": [{"Pattern": "{ \"Metadata\" : [ 1, 2 ]}"}]}'
```

This [ create-event-source-mapping](https://docs.aws.amazon.com/cli/latest/reference/lambda/create-event-source-mapping.html) command creates a new Amazon SQS event source mapping for function `my-function` with the specified `FilterCriteria`.

To add these filter criteria to an existing event source mapping, run the following command.

```
aws lambda update-event-source-mapping \
    --uuid {{"a1b2c3d4-5678-90ab-cdef-11111EXAMPLE"}} \
    --filter-criteria '{"Filters": [{"Pattern": "{ \"Metadata\" : [ 1, 2 ]}"}]}'
```

Note that to update an event source mapping, you need its UUID. You can get the UUID from a [ list-event-source-mappings](https://docs.aws.amazon.com/cli/latest/reference/lambda/list-event-source-mappings.html) call. Lambda also returns the UUID in the [ create-event-source-mapping](https://docs.aws.amazon.com/cli/latest/reference/lambda/create-event-source-mapping.html) CLI response.

To remove filter criteria from an event source, you can run the following [ update-event-source-mapping](https://docs.aws.amazon.com/cli/latest/reference/lambda/update-event-source-mapping.html) command with an empty `FilterCriteria` object.

```
aws lambda update-event-source-mapping \
    --uuid {{"a1b2c3d4-5678-90ab-cdef-11111EXAMPLE"}} \
    --filter-criteria "{}"
```

For more examples of creating event filters using the AWS CLI, see [Using filters with different AWS services](#filtering-by-service).

## Attaching filter criteria to an event source mapping (AWS SAM)
<a name="filtering-sam"></a>

 Suppose you want to configure an event source in AWS SAM to use the following filter criteria: 

```
{
   "Filters": [
      {
          "Pattern": "{ \"Metadata\" : [ 1, 2 ] }"
      }
   ]
}
```

 To add these filter criteria to your event source mapping, insert the following snippet into the YAML template for your event source.

```
FilterCriteria: 
  Filters: 
    - Pattern: '{"Metadata": [1, 2]}'
```

 For more information on creating and configuring an AWS SAM template for an event source mapping, see the [ EventSource](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-function-eventsource.html) section of the AWS SAM Developer Guide. Fore more examples of creating event filters using AWS SAM templates, see [Using filters with different AWS services](#filtering-by-service). 

## Encryption of filter criteria
<a name="filter-criteria-encryption"></a>

By default, Lambda doesn't encrypt your filter criteria object. For use cases where you may include sensitive information in your filter criteria object, you can use your own [KMS key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#kms_keys) to encrypt it.

After you encrypt your filter criteria object, you can view its plaintext version using a [GetEventSourceMapping](https://docs.aws.amazon.com/lambda/latest/api/API_GetEventSourceMapping.html) API call. You must have `kms:Decrypt` permissions to be able to successfully view the filter criteria in plaintext.

**Note**  
If your filter criteria object is encrypted, Lambda redacts the value of the `FilterCriteria` field in the response of [ListEventSourceMappings](https://docs.aws.amazon.com/lambda/latest/api/API_ListEventSourceMappings.html) calls. Instead, this field displays as `null`. To see the true value of `FilterCriteria`, use the [GetEventSourceMapping](https://docs.aws.amazon.com/lambda/latest/api/API_GetEventSourceMapping.html) API.  
To view the decrypted value of `FilterCriteria` in the console, ensure that your IAM role contains permissions for [GetEventSourceMapping](https://docs.aws.amazon.com/lambda/latest/api/API_GetEventSourceMapping.html).

You can specify your own KMS key via the console, API/CLI, or CloudFormation.

**To encrypt filter criteria with a customer-owned KMS key (console)**

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions) of the Lambda console.

1. Choose **Add trigger**. If you already have an existing trigger, choose the **Configuration** tab, and then choose ** Triggers**. Select the existing trigger, and choose **Edit**.

1. Select the checkbox next to **Encrypt with customer managed KMS key**.

1. For **Choose a customer managed KMS encryption key**, select an existing enabled key or create a new key. Depending on the operation, you need some or all of the following permissions: `kms:DescribeKey`, `kms:GenerateDataKey`, and `kms:Decrypt`. Use the KMS key policy to grant these permissions.

If you use your own KMS key, the following API operations must be permitted in the [key policy](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html):
+ `kms:Decrypt` – Must be granted to the regional Lambda service principal (`lambda.{{AWS_region}}.amazonaws.com`). This allows Lambda to decrypt data with this KMS key.
  + To prevent a [ cross-service confused deputy problem](https://docs.aws.amazon.com/IAM/latest/UserGuide/confused-deputy.html), the key policy uses the [https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-sourcearn](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-sourcearn) global condition key. The correct value of the `aws:SourceArn` key is the ARN of your event source mapping resource, so you can add this to your policy only after you know its ARN. Lambda also forwards the `aws:lambda:FunctionArn` and `aws:lambda:EventSourceArn` keys and their respective values in the [encryption context](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#encrypt_context) when making a decryption request to KMS. These values must match the specified conditions in the key policy for the decryption request to succeed. You don't need to include EventSourceArn for Self-managed Kafka event sources since they don't have an EventSourceArn.
+ `kms:Decrypt` – Must also be granted to the principal that intends to use the key to view the plaintext filter criteria in [GetEventSourceMapping](https://docs.aws.amazon.com/lambda/latest/api/API_GetEventSourceMapping.html) or [DeleteEventSourceMapping](https://docs.aws.amazon.com/lambda/latest/api/API_DeleteEventSourceMapping.html) API calls.
+ `kms:DescribeKey` – Provides the customer managed key details to allow the specified principal to use the key.
+ `kms:GenerateDataKey` – Provides permissions for Lambda to generate a data key to encrypt the filter criteria, on behalf of the specified principal ([envelope encryption](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#enveloping)).

You can use AWS CloudTrail to track AWS KMS requests that Lambda makes on your behalf. For sample CloudTrail events, see [Monitoring your encryption keys for Lambda](security-encryption-at-rest.md#encryption-key-monitoring).

We also recommend using the [https://docs.aws.amazon.com/kms/latest/developerguide/conditions-kms.html#conditions-kms-via-service](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-kms.html#conditions-kms-via-service) condition key to limit the use of the KMS key to requests from Lambda only. The value of this key is the regional Lambda service principal (`lambda.{{AWS_region}}.amazonaws.com`). The following is a sample key policy that grants all the relevant permissions:

**Example AWS KMS key policy**    
****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Id": "example-key-policy-1",
    "Statement": [
        {
            "Sid": "Allow Lambda to decrypt using the key",
            "Effect": "Allow",
            "Principal": {
                "Service": {{"lambda.us-east-1.amazonaws.com"}}
            },
            "Action": [
                "kms:Decrypt"
            ],
            "Resource": "*",
            "Condition": {
                "ArnEquals" : {
                    "aws:SourceArn": [
                        {{"arn:aws:lambda:us-east-1:123456789012:event-source-mapping:<esm_uuid>"}}
                    ]
                },
                "StringEquals": {
                    "kms:EncryptionContext:aws:lambda:FunctionArn": {{"arn:aws:lambda:us-east-1:123456789012:function:test-function"}},
                    "kms:EncryptionContext:aws:lambda:EventSourceArn": {{"arn:aws:sqs:us-east-1:123456789012:test-queue"}}
                }
            }
        },
        {
            "Sid": "Allow actions by an AWS account on the key",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::123456789012:root"
            },
            "Action": "kms:*",
            "Resource": "*"
        },
        {
            "Sid": "Allow use of the key to specific roles",
            "Effect": "Allow",
            "Principal": {
                "AWS": {{"arn:aws:iam::123456789012:role/ExampleRole"}}
            },
            "Action": [
                "kms:Decrypt",
                "kms:DescribeKey",
                "kms:GenerateDataKey"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals" : {
                    "kms:ViaService": {{"lambda.us-east-1.amazonaws.com"}}
                }
            }
        }
    ]
}
```

To use your own KMS key to encrypt filter criteria, you can also use the following [CreateEventSourceMapping](https://docs.aws.amazon.com/lambda/latest/api/API_CreateEventSourceMapping.html) AWS CLI command. Specify the KMS key ARN with the `--kms-key-arn` flag.

```
aws lambda create-event-source-mapping --function-name my-function \
    --maximum-batching-window-in-seconds 60 \
    --event-source-arn {{arn:aws:sqs:us-east-1:123456789012:my-queue}} \
    --filter-criteria "{\"filters\": [{\"pattern\": \"{\"a\": [\"1\", \"2\"]}\" }]}" \
    --kms-key-arn {{arn:aws:kms:us-east-1:123456789012:key/055efbb4-xmpl-4336-ba9c-538c7d31f599}}
```

If you have an existing event source mapping, use the [UpdateEventSourceMapping](https://docs.aws.amazon.com/lambda/latest/api/API_UpdateEventSourceMapping.html) AWS CLI command instead. Specify the KMS key ARN with the `--kms-key-arn` flag.

```
aws lambda update-event-source-mapping --function-name my-function \
    --maximum-batching-window-in-seconds 60 \
    --event-source-arn {{arn:aws:sqs:us-east-1:123456789012:my-queue}} \
    --filter-criteria "{\"filters\": [{\"pattern\": \"{\"a\": [\"1\", \"2\"]}\" }]}" \
    --kms-key-arn {{arn:aws:kms:us-east-1:123456789012:key/055efbb4-xmpl-4336-ba9c-538c7d31f599}}
```

This operation overwrites any KMS key that was previously specified. If you specify the `--kms-key-arn` flag along with an empty argument, Lambda stops using your KMS key to encrypt filter criteria. Instead, Lambda defaults back to using an Amazon-owned key.

To specify your own KMS key in a CloudFormation template, use the `KMSKeyArn` property of the `AWS::Lambda::EventSourceMapping` resource type. For example, you can insert the following snippet into the YAML template for your event source.

```
MyEventSourceMapping:
  Type: AWS::Lambda::EventSourceMapping
  Properties:
    ...
    FilterCriteria:
      Filters:
        - Pattern: '{"a": [1, 2]}'
    KMSKeyArn: "{{arn:aws:kms:us-east-1:123456789012:key/055efbb4-xmpl-4336-ba9c-538c7d31f599}}"
    ...
```

To be able to view your encrypted filter criteria in plaintext in a [GetEventSourceMapping](https://docs.aws.amazon.com/lambda/latest/api/API_GetEventSourceMapping.html) or [DeleteEventSourceMapping](https://docs.aws.amazon.com/lambda/latest/api/API_DeleteEventSourceMapping.html) API call, you must have `kms:Decrypt` permissions.

Starting August 6, 2024, the `FilterCriteria` field no longer shows up in AWS CloudTrail logs from [CreateEventSourceMapping](https://docs.aws.amazon.com/lambda/latest/api/API_CreateEventSourceMapping.html), [UpdateEventSourceMapping](https://docs.aws.amazon.com/lambda/latest/api/API_UpdateEventSourceMapping.html), and [DeleteEventSourceMapping](https://docs.aws.amazon.com/lambda/latest/api/API_DeleteEventSourceMapping.html) API calls if your function doesn't use event filtering. If your function does use event filtering, the `FilterCriteria` field shows up as empty (`{}`). You can still view your filter criteria in plaintext in the response of [GetEventSourceMapping](https://docs.aws.amazon.com/lambda/latest/api/API_GetEventSourceMapping.html) API calls if you have `kms:Decrypt` permissions for the correct KMS key.

### Sample CloudTrail log entry for Create/Update/DeleteEventSourceMapping calls
<a name="filter-criteria-encryption-cloudtrail"></a>

In the following AWS CloudTrail sample log entry for a CreateEventSourceMapping call, `FilterCriteria` shows up as empty (`{}`) because the function uses event filtering. This is the case even if `FilterCriteria` object contains valid filter criteria that your function is actively using. If the function doesn't use event filtering, CloudTrail won't display the `FilterCriteria` field at all in log entries.

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AROA123456789EXAMPLE:userid1",
        "arn": "arn:aws:sts::123456789012:assumed-role/Example/example-role",
        "accountId": "123456789012",
        "accessKeyId": "ASIAIOSFODNN7EXAMPLE",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AROA987654321EXAMPLE",
                "arn": "arn:aws:iam::123456789012:role/User1",
                "accountId": "123456789012",
                "userName": "User1"
            },
            "webIdFederationData": {},
            "attributes": {
                "creationDate": "2024-05-09T20:35:01Z",
                "mfaAuthenticated": "false"
            }
        },
        "invokedBy": "AWS Internal"
    },
    "eventTime": "2024-05-09T21:05:41Z",
    "eventSource": "lambda.amazonaws.com",
    "eventName": "CreateEventSourceMapping20150331",
    "awsRegion": "us-east-2",
    "sourceIPAddress": "AWS Internal",
    "userAgent": "AWS Internal",
    "requestParameters": {
        "eventSourceArn": "arn:aws:sqs:us-east-2:123456789012:example-queue",
        "functionName": "example-function",
        "enabled": true,
        "batchSize": 10,
        "filterCriteria": {},
        "kMSKeyArn": "arn:aws:kms:us-east-2:123456789012:key/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
        "scalingConfig": {},
        "maximumBatchingWindowInSeconds": 0,
        "sourceAccessConfigurations": []
    },
    "responseElements": {
        "uUID": "a1b2c3d4-5678-90ab-cdef-EXAMPLEaaaaa",
        "batchSize": 10,
        "maximumBatchingWindowInSeconds": 0,
        "eventSourceArn": "arn:aws:sqs:us-east-2:123456789012:example-queue",
        "filterCriteria": {},
        "kMSKeyArn": "arn:aws:kms:us-east-2:123456789012:key/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
        "functionArn": "arn:aws:lambda:us-east-2:123456789012:function:example-function",
        "lastModified": "May 9, 2024, 9:05:41 PM",
        "state": "Creating",
        "stateTransitionReason": "USER_INITIATED",
        "functionResponseTypes": [],
        "eventSourceMappingArn": "arn:aws:lambda:us-east-2:123456789012:event-source-mapping:a1b2c3d4-5678-90ab-cdef-EXAMPLEbbbbb"
    },
    "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
    "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "123456789012",
    "eventCategory": "Management",
    "sessionCredentialFromConsole": "true"
}
```

## Using filters with different AWS services
<a name="filtering-by-service"></a>

Different types of event source use different key values for their data fields. To filter on data properties, make sure that you use the correct key in your filter’s pattern. The following table gives the filtering keys for each supported AWS service.


| AWS service | Filtering key | 
| --- | --- | 
| DynamoDB | dynamodb | 
| Kinesis | data | 
| Amazon MQ | data | 
| Amazon MSK | value | 
| Self-managed Apache Kafka | value | 
| Amazon SQS | body | 

The following sections give examples of filter patterns for different types of event sources. They also provide definitions of supported incoming data formats and filter pattern body formats for each supported service.
+ [Using event filtering with a DynamoDB event source](with-ddb-filtering.md)
+ [Using event filtering with a Kinesis event source](with-kinesis-filtering.md)
+ [Filter events from an Amazon MQ event source](with-mq-filtering.md)
+ [Filtering events from Amazon MSK and self-managed Apache Kafka event sources](kafka-filtering.md)
+ [Using event filtering with an Amazon SQS event source](with-sqs-filtering.md)