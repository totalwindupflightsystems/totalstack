---
id: "@specs/aws/emr/docs/API_ModifyInstanceGroups"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ModifyInstanceGroups"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# ModifyInstanceGroups

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_ModifyInstanceGroups
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ModifyInstanceGroups
<a name="API_ModifyInstanceGroups"></a>

ModifyInstanceGroups modifies the number of nodes and configuration settings of an instance group. The input parameters include the new target instance count for the group and the instance group ID. The call will either succeed or fail atomically.

## Request Syntax
<a name="API_ModifyInstanceGroups_RequestSyntax"></a>

```
{
   "ClusterId": "{{string}}",
   "InstanceGroups": [ 
      { 
         "Configurations": [ 
            { 
               "Classification": "{{string}}",
               "Configurations": [ 
                  "Configuration"
               ],
               "Properties": { 
                  "{{string}}" : "{{string}}" 
               }
            }
         ],
         "EC2InstanceIdsToTerminate": [ "{{string}}" ],
         "InstanceCount": {{number}},
         "InstanceGroupId": "{{string}}",
         "ReconfigurationType": "{{string}}",
         "ShrinkPolicy": { 
            "DecommissionTimeout": {{number}},
            "InstanceResizePolicy": { 
               "InstancesToProtect": [ "{{string}}" ],
               "InstancesToTerminate": [ "{{string}}" ],
               "InstanceTerminationTimeout": {{number}}
            }
         }
      }
   ]
}
```

## Request Parameters
<a name="API_ModifyInstanceGroups_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClusterId](#API_ModifyInstanceGroups_RequestSyntax) **   <a name="EMR-ModifyInstanceGroups-request-ClusterId"></a>
The ID of the cluster to which the instance group belongs.  
Type: String  
Length Constraints: Maximum length of 256.  
Required: No

 ** [InstanceGroups](#API_ModifyInstanceGroups_RequestSyntax) **   <a name="EMR-ModifyInstanceGroups-request-InstanceGroups"></a>
Instance groups to change.  
Type: Array of [InstanceGroupModifyConfig](API_InstanceGroupModifyConfig.md) objects  
Required: No

## Response Elements
<a name="API_ModifyInstanceGroups_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_ModifyInstanceGroups_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **   
Indicates that an error occurred while processing the request and that the request was not completed.  
HTTP Status Code: 400

## Examples
<a name="API_ModifyInstanceGroups_Examples"></a>

### Example
<a name="API_ModifyInstanceGroups_Example_1"></a>

This example illustrates one usage of ModifyInstanceGroups.

#### Sample Request
<a name="API_ModifyInstanceGroups_Example_1_Request"></a>

```
POST / HTTP/1.1
Content-Type: application/x-amz-json-1.1
X-Amz-Target: ElasticMapReduce.ModifyInstanceGroups
Content-Length: 77
User-Agent: aws-sdk-ruby/1.9.2 ruby/1.9.3 i386-mingw32
Host: us-east-1.elasticmapreduce.amazonaws.com
X-Amz-Date: 20130716T205843Z
X-Amz-Content-Sha256: bb1af3d0c6c6a1a09f21ccd7f04a0e2e6c9ce5b5810b0f6777560fe4f81bda8c
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20130716/us-east-1/elasticmapreduce/aws4_request, SignedHeaders=content-length;content-type;host;user-agent;x-amz-content-sha256;x-amz-date;x-amz-target, Signature=17bbbb4448a1f47a14d5657445e9de5cadf16bed58b850585f80865882133b33
Accept: */*

{"InstanceGroups": [{
    "InstanceGroupId": "ig-1S8NWT31S2OVG",
    "InstanceCount": 5
}]}
```

#### Sample Response
<a name="API_ModifyInstanceGroups_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 80a74808-ee5a-11e2-90db-69a5154aeb8d
Content-Type: application/x-amz-json-1.1
Content-Length: 0
Date: Tue, 16 Jul 2013 20:58:44 GMT
```

## See Also
<a name="API_ModifyInstanceGroups_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticmapreduce-2009-03-31/ModifyInstanceGroups) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticmapreduce-2009-03-31/ModifyInstanceGroups) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/ModifyInstanceGroups) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticmapreduce-2009-03-31/ModifyInstanceGroups) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/ModifyInstanceGroups) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticmapreduce-2009-03-31/ModifyInstanceGroups) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticmapreduce-2009-03-31/ModifyInstanceGroups) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticmapreduce-2009-03-31/ModifyInstanceGroups) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticmapreduce-2009-03-31/ModifyInstanceGroups) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/ModifyInstanceGroups) 