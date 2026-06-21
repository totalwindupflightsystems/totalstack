---
id: "@specs/aws/cloudtrail/docs/API_ListTags"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListTags"
status: active
depends_on:
  - "@specs/aws/cloudtrail/meta"
---

# ListTags

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudtrail/docs/API_ListTags
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListTags
<a name="API_ListTags"></a>

Lists the tags for the specified trails, event data stores, dashboards, or channels in the current Region.

## Request Syntax
<a name="API_ListTags_RequestSyntax"></a>

```
{
   "NextToken": "{{string}}",
   "ResourceIdList": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_ListTags_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [NextToken](#API_ListTags_RequestSyntax) **   <a name="awscloudtrail-ListTags-request-NextToken"></a>
Reserved for future use.  
Type: String  
Required: No

 ** [ResourceIdList](#API_ListTags_RequestSyntax) **   <a name="awscloudtrail-ListTags-request-ResourceIdList"></a>
Specifies a list of trail, event data store, dashboard, or channel ARNs whose tags will be listed. The list has a limit of 20 ARNs.  
 Example trail ARN format: `arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail`   
Example event data store ARN format: `arn:aws:cloudtrail:us-east-2:123456789012:eventdatastore/EXAMPLE-f852-4e8f-8bd1-bcf6cEXAMPLE`   
Example dashboard ARN format: `arn:aws:cloudtrail:us-east-1:123456789012:dashboard/exampleDash`   
Example channel ARN format: `arn:aws:cloudtrail:us-east-2:123456789012:channel/01234567890`   
Type: Array of strings  
Required: Yes

## Response Syntax
<a name="API_ListTags_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "ResourceTagList": [ 
      { 
         "ResourceId": "string",
         "TagsList": [ 
            { 
               "Key": "string",
               "Value": "string"
            }
         ]
      }
   ]
}
```

## Response Elements
<a name="API_ListTags_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListTags_ResponseSyntax) **   <a name="awscloudtrail-ListTags-response-NextToken"></a>
Reserved for future use.  
Type: String

 ** [ResourceTagList](#API_ListTags_ResponseSyntax) **   <a name="awscloudtrail-ListTags-response-ResourceTagList"></a>
A list of resource tags.  
Type: Array of [ResourceTag](API_ResourceTag.md) objects

## Errors
<a name="API_ListTags_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ChannelARNInvalidException **   
This exception is thrown when the specified value of `ChannelARN` is not valid.  
HTTP Status Code: 400

 ** CloudTrailARNInvalidException **   
This exception is thrown when an operation is called with an ARN that is not valid.  
The following is the format of a trail ARN: `arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail`   
The following is the format of an event data store ARN: `arn:aws:cloudtrail:us-east-2:123456789012:eventdatastore/EXAMPLE-f852-4e8f-8bd1-bcf6cEXAMPLE`   
The following is the format of a dashboard ARN: `arn:aws:cloudtrail:us-east-1:123456789012:dashboard/exampleDash`   
The following is the format of a channel ARN: `arn:aws:cloudtrail:us-east-2:123456789012:channel/01234567890`   
HTTP Status Code: 400

 ** EventDataStoreARNInvalidException **   
The specified event data store ARN is not valid or does not map to an event data store in your account.  
HTTP Status Code: 400

 ** EventDataStoreNotFoundException **   
The specified event data store was not found.  
HTTP Status Code: 400

 ** InactiveEventDataStoreException **   
The event data store is inactive.  
HTTP Status Code: 400

 ** InvalidTokenException **   
Reserved for future use.  
HTTP Status Code: 400

 ** InvalidTrailNameException **   
This exception is thrown when the provided trail name is not valid. Trail names must meet the following requirements:  
+ Contain only ASCII letters (a-z, A-Z), numbers (0-9), periods (.), underscores (\_), or dashes (-)
+ Start with a letter or number, and end with a letter or number
+ Be between 3 and 128 characters
+ Have no adjacent periods, underscores or dashes. Names like `my-_namespace` and `my--namespace` are not valid.
+ Not be in IP address format (for example, 192.168.5.4)
HTTP Status Code: 400

 ** NoManagementAccountSLRExistsException **   
 This exception is thrown when the management account does not have a service-linked role.   
HTTP Status Code: 400

 ** OperationNotPermittedException **   
This exception is thrown when the requested operation is not permitted.  
HTTP Status Code: 400

 ** ResourceNotFoundException **   
This exception is thrown when the specified resource is not found.  
HTTP Status Code: 400

 ** ResourceTypeNotSupportedException **   
This exception is thrown when the specified resource type is not supported by CloudTrail.  
HTTP Status Code: 400

 ** UnsupportedOperationException **   
This exception is thrown when the requested operation is not supported.  
HTTP Status Code: 400

## See Also
<a name="API_ListTags_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudtrail-2013-11-01/ListTags) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudtrail-2013-11-01/ListTags) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/ListTags) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudtrail-2013-11-01/ListTags) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/ListTags) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudtrail-2013-11-01/ListTags) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudtrail-2013-11-01/ListTags) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudtrail-2013-11-01/ListTags) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudtrail-2013-11-01/ListTags) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/ListTags) 