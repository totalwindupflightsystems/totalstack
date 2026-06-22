---
id: "@specs/aws/emr/docs/API_ListInstances"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListInstances"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# ListInstances

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_ListInstances
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListInstances
<a name="API_ListInstances"></a>

Provides information for all active Amazon EC2 instances and Amazon EC2 instances terminated in the last 30 days, up to a maximum of 2,000. Amazon EC2 instances in any of the following states are considered active: AWAITING\_FULFILLMENT, PROVISIONING, BOOTSTRAPPING, RUNNING.

## Request Syntax
<a name="API_ListInstances_RequestSyntax"></a>

```
{
   "ClusterId": "{{string}}",
   "InstanceFleetId": "{{string}}",
   "InstanceFleetType": "{{string}}",
   "InstanceGroupId": "{{string}}",
   "InstanceGroupTypes": [ "{{string}}" ],
   "InstanceStates": [ "{{string}}" ],
   "Marker": "{{string}}"
}
```

## Request Parameters
<a name="API_ListInstances_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClusterId](#API_ListInstances_RequestSyntax) **   <a name="EMR-ListInstances-request-ClusterId"></a>
The identifier of the cluster for which to list the instances.  
Type: String  
Length Constraints: Maximum length of 256.  
Required: Yes

 ** [InstanceFleetId](#API_ListInstances_RequestSyntax) **   <a name="EMR-ListInstances-request-InstanceFleetId"></a>
The unique identifier of the instance fleet.  
Type: String  
Length Constraints: Maximum length of 256.  
Required: No

 ** [InstanceFleetType](#API_ListInstances_RequestSyntax) **   <a name="EMR-ListInstances-request-InstanceFleetType"></a>
The node type of the instance fleet. For example MASTER, CORE, or TASK.  
Type: String  
Valid Values: `MASTER | CORE | TASK`   
Required: No

 ** [InstanceGroupId](#API_ListInstances_RequestSyntax) **   <a name="EMR-ListInstances-request-InstanceGroupId"></a>
The identifier of the instance group for which to list the instances.  
Type: String  
Length Constraints: Maximum length of 256.  
Required: No

 ** [InstanceGroupTypes](#API_ListInstances_RequestSyntax) **   <a name="EMR-ListInstances-request-InstanceGroupTypes"></a>
The type of instance group for which to list the instances.  
Type: Array of strings  
Valid Values: `MASTER | CORE | TASK`   
Required: No

 ** [InstanceStates](#API_ListInstances_RequestSyntax) **   <a name="EMR-ListInstances-request-InstanceStates"></a>
A list of instance states that will filter the instances returned with this request.  
Type: Array of strings  
Valid Values: `AWAITING_FULFILLMENT | PROVISIONING | BOOTSTRAPPING | RUNNING | TERMINATED`   
Required: No

 ** [Marker](#API_ListInstances_RequestSyntax) **   <a name="EMR-ListInstances-request-Marker"></a>
The pagination token that indicates the next set of results to retrieve.  
Type: String  
Required: No

## Response Syntax
<a name="API_ListInstances_ResponseSyntax"></a>

```
{
   "Instances": [ 
      { 
         "EbsVolumes": [ 
            { 
               "Device": "string",
               "VolumeId": "string"
            }
         ],
         "Ec2InstanceId": "string",
         "Id": "string",
         "InstanceFleetId": "string",
         "InstanceGroupId": "string",
         "InstanceType": "string",
         "Market": "string",
         "PrivateDnsName": "string",
         "PrivateIpAddress": "string",
         "PublicDnsName": "string",
         "PublicIpAddress": "string",
         "Status": { 
            "State": "string",
            "StateChangeReason": { 
               "Code": "string",
               "Message": "string"
            },
            "Timeline": { 
               "CreationDateTime": number,
               "EndDateTime": number,
               "ReadyDateTime": number
            }
         }
      }
   ],
   "Marker": "string"
}
```

## Response Elements
<a name="API_ListInstances_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Instances](#API_ListInstances_ResponseSyntax) **   <a name="EMR-ListInstances-response-Instances"></a>
The list of instances for the cluster and given filters.  
Type: Array of [Instance](API_Instance.md) objects

 ** [Marker](#API_ListInstances_ResponseSyntax) **   <a name="EMR-ListInstances-response-Marker"></a>
The pagination token that indicates the next set of results to retrieve.  
Type: String

## Errors
<a name="API_ListInstances_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **   
This exception occurs when there is an internal failure in the Amazon EMR service.    
 ** Message **   
The message associated with the exception.
HTTP Status Code: 500

 ** InvalidRequestException **   
This exception occurs when there is something wrong with user input.    
 ** ErrorCode **   
The error code associated with the exception.  
 ** Message **   
The message associated with the exception.
HTTP Status Code: 400

## See Also
<a name="API_ListInstances_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticmapreduce-2009-03-31/ListInstances) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticmapreduce-2009-03-31/ListInstances) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/ListInstances) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticmapreduce-2009-03-31/ListInstances) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/ListInstances) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticmapreduce-2009-03-31/ListInstances) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticmapreduce-2009-03-31/ListInstances) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticmapreduce-2009-03-31/ListInstances) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticmapreduce-2009-03-31/ListInstances) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/ListInstances) 