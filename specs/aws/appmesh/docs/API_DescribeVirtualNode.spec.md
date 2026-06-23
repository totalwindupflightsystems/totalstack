---
id: "@specs/aws/appmesh/docs/API_DescribeVirtualNode"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeVirtualNode"
status: active
depends_on:
  - "@specs/aws/appmesh/meta"
---

# DescribeVirtualNode

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appmesh/docs/API_DescribeVirtualNode
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeVirtualNode
<a name="API_DescribeVirtualNode"></a>

Describes an existing virtual node.

## Request Syntax
<a name="API_DescribeVirtualNode_RequestSyntax"></a>

```
GET /v20190125/meshes/{{meshName}}/virtualNodes/{{virtualNodeName}}?meshOwner={{meshOwner}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeVirtualNode_RequestParameters"></a>

The request uses the following URI parameters.

 ** [meshName](#API_DescribeVirtualNode_RequestSyntax) **   <a name="appmesh-DescribeVirtualNode-request-uri-meshName"></a>
The name of the service mesh that the virtual node resides in.  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: Yes

 ** [meshOwner](#API_DescribeVirtualNode_RequestSyntax) **   <a name="appmesh-DescribeVirtualNode-request-uri-meshOwner"></a>
The AWS IAM account ID of the service mesh owner. If the account ID is not your own, then it's the ID of the account that shared the mesh with your account. For more information about mesh sharing, see [Working with shared meshes](https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html).  
Length Constraints: Fixed length of 12.

 ** [virtualNodeName](#API_DescribeVirtualNode_RequestSyntax) **   <a name="appmesh-DescribeVirtualNode-request-uri-virtualNodeName"></a>
The name of the virtual node to describe.  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: Yes

## Request Body
<a name="API_DescribeVirtualNode_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeVirtualNode_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "meshName": "string",
   "metadata": { 
      "arn": "string",
      "createdAt": number,
      "lastUpdatedAt": number,
      "meshOwner": "string",
      "resourceOwner": "string",
      "uid": "string",
      "version": number
   },
   "spec": { 
      "backendDefaults": { 
         "clientPolicy": { 
            "tls": { 
               "certificate": { ... },
               "enforce": boolean,
               "ports": [ number ],
               "validation": { 
                  "subjectAlternativeNames": { 
                     "match": { 
                        "exact": [ "string" ]
                     }
                  },
                  "trust": { ... }
               }
            }
         }
      },
      "backends": [ 
         { ... }
      ],
      "listeners": [ 
         { 
            "connectionPool": { ... },
            "healthCheck": { 
               "healthyThreshold": number,
               "intervalMillis": number,
               "path": "string",
               "port": number,
               "protocol": "string",
               "timeoutMillis": number,
               "unhealthyThreshold": number
            },
            "outlierDetection": { 
               "baseEjectionDuration": { 
                  "unit": "string",
                  "value": number
               },
               "interval": { 
                  "unit": "string",
                  "value": number
               },
               "maxEjectionPercent": number,
               "maxServerErrors": number
            },
            "portMapping": { 
               "port": number,
               "protocol": "string"
            },
            "timeout": { ... },
            "tls": { 
               "certificate": { ... },
               "mode": "string",
               "validation": { 
                  "subjectAlternativeNames": { 
                     "match": { 
                        "exact": [ "string" ]
                     }
                  },
                  "trust": { ... }
               }
            }
         }
      ],
      "logging": { 
         "accessLog": { ... }
      },
      "serviceDiscovery": { ... }
   },
   "status": { 
      "status": "string"
   },
   "virtualNodeName": "string"
}
```

## Response Elements
<a name="API_DescribeVirtualNode_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [meshName](#API_DescribeVirtualNode_ResponseSyntax) **   <a name="appmesh-DescribeVirtualNode-response-meshName"></a>
The name of the service mesh that the virtual node resides in.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [metadata](#API_DescribeVirtualNode_ResponseSyntax) **   <a name="appmesh-DescribeVirtualNode-response-metadata"></a>
The associated metadata for the virtual node.  
Type: [ResourceMetadata](API_ResourceMetadata.md) object

 ** [spec](#API_DescribeVirtualNode_ResponseSyntax) **   <a name="appmesh-DescribeVirtualNode-response-spec"></a>
The specifications of the virtual node.  
Type: [VirtualNodeSpec](API_VirtualNodeSpec.md) object

 ** [status](#API_DescribeVirtualNode_ResponseSyntax) **   <a name="appmesh-DescribeVirtualNode-response-status"></a>
The current status for the virtual node.  
Type: [VirtualNodeStatus](API_VirtualNodeStatus.md) object

 ** [virtualNodeName](#API_DescribeVirtualNode_ResponseSyntax) **   <a name="appmesh-DescribeVirtualNode-response-virtualNodeName"></a>
The name of the virtual node.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.

## Errors
<a name="API_DescribeVirtualNode_Errors"></a>

 ** BadRequestException **   
The request syntax was malformed. Check your request syntax and try again.  
HTTP Status Code: 400

 ** ForbiddenException **   
You don't have permissions to perform this action.  
HTTP Status Code: 403

 ** InternalServerErrorException **   
The request processing has failed because of an unknown error, exception, or failure.  
HTTP Status Code: 500

 ** NotFoundException **   
The specified resource doesn't exist. Check your request syntax and try again.  
HTTP Status Code: 404

 ** ServiceUnavailableException **   
The request has failed due to a temporary failure of the service.  
HTTP Status Code: 503

 ** TooManyRequestsException **   
The maximum request rate permitted by the App Mesh APIs has been exceeded for your account. For best results, use an increasing or variable sleep interval between requests.  
HTTP Status Code: 429

## Examples
<a name="API_DescribeVirtualNode_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You need to learn how to sign HTTP requests only if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_DescribeVirtualNode_Example_1"></a>

This example describes a virtual node named `colorteller-vn` in the `ecs-mesh` service mesh.

#### Sample Request
<a name="API_DescribeVirtualNode_Example_1_Request"></a>

```
GET /v20190125/meshes/ecs-mesh/virtualNodes/colorteller-vn HTTP/1.1
Host: appmesh.us-east-1.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/1.16.56 Python/3.7.0 Darwin/17.7.0 botocore/1.12.46
X-Amz-Date: 20190228T000300Z
Authorization: AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeVirtualNode_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-requestid: 083f9376-9799-4142-978b-42f5966192b8
content-type: application/json
content-length: 654
date: Thu, 28 Feb 2019 00:03:00 GMT
x-envoy-upstream-service-time: 60
server: envoy
Connection: keep-alive

{
	"meshName": "ecs-mesh",
	"metadata": {
		"arn": "arn:aws:appmesh:us-east-1:123456789012:mesh/ecs-mesh/virtualNode/colorteller-vn",
		"createdAt": 1.551311799179E9,
		"lastUpdatedAt": 1.551311799179E9,
		"uid": "0999e53a-8e0e-4c4c-8764-ae8ebecc296d",
		"version": 1
	},
	"spec": {
		"backends": [],
		"listeners": [{
			"healthCheck": {
				"healthyThreshold": 2,
				"intervalMillis": 5000,
				"path": "/ping",
				"port": 9080,
				"protocol": "http",
				"timeoutMillis": 2000,
				"unhealthyThreshold": 2
			},
			"portMapping": {
				"port": 9080,
				"protocol": "http"
			}
		}],
		"logging": null,
		"serviceDiscovery": {
			"dns": {
				"hostname": "colorteller.default.svc.cluster.local"
			}
		}
	},
	"status": {
		"status": "ACTIVE"
	},
	"virtualNodeName": "colorteller-vn"
}
```

## See Also
<a name="API_DescribeVirtualNode_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appmesh-2019-01-25/DescribeVirtualNode) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appmesh-2019-01-25/DescribeVirtualNode) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/DescribeVirtualNode) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appmesh-2019-01-25/DescribeVirtualNode) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/DescribeVirtualNode) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appmesh-2019-01-25/DescribeVirtualNode) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appmesh-2019-01-25/DescribeVirtualNode) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appmesh-2019-01-25/DescribeVirtualNode) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appmesh-2019-01-25/DescribeVirtualNode) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/DescribeVirtualNode) 