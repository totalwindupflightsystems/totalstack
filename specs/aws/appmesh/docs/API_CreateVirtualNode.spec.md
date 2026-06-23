---
id: "@specs/aws/appmesh/docs/API_CreateVirtualNode"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateVirtualNode"
status: active
depends_on:
  - "@specs/aws/appmesh/meta"
---

# CreateVirtualNode

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appmesh/docs/API_CreateVirtualNode
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateVirtualNode
<a name="API_CreateVirtualNode"></a>

Creates a virtual node within a service mesh.

 A virtual node acts as a logical pointer to a particular task group, such as an Amazon ECS service or a Kubernetes deployment. When you create a virtual node, you can specify the service discovery information for your task group, and whether the proxy running in a task group will communicate with other proxies using Transport Layer Security (TLS).

You define a `listener` for any inbound traffic that your virtual node expects. Any virtual service that your virtual node expects to communicate to is specified as a `backend`.

The response metadata for your new virtual node contains the `arn` that is associated with the virtual node. Set this value to the full ARN; for example, `arn:aws:appmesh:us-west-2:123456789012:myMesh/default/virtualNode/myApp`) as the `APPMESH_RESOURCE_ARN` environment variable for your task group's Envoy proxy container in your task definition or pod spec. This is then mapped to the `node.id` and `node.cluster` Envoy parameters.

**Note**  
By default, App Mesh uses the name of the resource you specified in `APPMESH_RESOURCE_ARN` when Envoy is referring to itself in metrics and traces. You can override this behavior by setting the `APPMESH_RESOURCE_CLUSTER` environment variable with your own name.

For more information about virtual nodes, see [Virtual nodes](https://docs.aws.amazon.com/app-mesh/latest/userguide/virtual_nodes.html). You must be using `1.15.0` or later of the Envoy image when setting these variables. For more information aboutApp Mesh Envoy variables, see [Envoy image](https://docs.aws.amazon.com/app-mesh/latest/userguide/envoy.html) in the AWS App Mesh User Guide.

## Request Syntax
<a name="API_CreateVirtualNode_RequestSyntax"></a>

```
PUT /v20190125/meshes/{{meshName}}/virtualNodes?meshOwner={{meshOwner}} HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "spec": { 
      "backendDefaults": { 
         "clientPolicy": { 
            "tls": { 
               "certificate": { ... },
               "enforce": {{boolean}},
               "ports": [ {{number}} ],
               "validation": { 
                  "subjectAlternativeNames": { 
                     "match": { 
                        "exact": [ "{{string}}" ]
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
               "healthyThreshold": {{number}},
               "intervalMillis": {{number}},
               "path": "{{string}}",
               "port": {{number}},
               "protocol": "{{string}}",
               "timeoutMillis": {{number}},
               "unhealthyThreshold": {{number}}
            },
            "outlierDetection": { 
               "baseEjectionDuration": { 
                  "unit": "{{string}}",
                  "value": {{number}}
               },
               "interval": { 
                  "unit": "{{string}}",
                  "value": {{number}}
               },
               "maxEjectionPercent": {{number}},
               "maxServerErrors": {{number}}
            },
            "portMapping": { 
               "port": {{number}},
               "protocol": "{{string}}"
            },
            "timeout": { ... },
            "tls": { 
               "certificate": { ... },
               "mode": "{{string}}",
               "validation": { 
                  "subjectAlternativeNames": { 
                     "match": { 
                        "exact": [ "{{string}}" ]
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
   "tags": [ 
      { 
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ],
   "virtualNodeName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateVirtualNode_RequestParameters"></a>

The request uses the following URI parameters.

 ** [meshName](#API_CreateVirtualNode_RequestSyntax) **   <a name="appmesh-CreateVirtualNode-request-uri-meshName"></a>
The name of the service mesh to create the virtual node in.  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: Yes

 ** [meshOwner](#API_CreateVirtualNode_RequestSyntax) **   <a name="appmesh-CreateVirtualNode-request-uri-meshOwner"></a>
The AWS IAM account ID of the service mesh owner. If the account ID is not your own, then the account that you specify must share the mesh with your account before you can create the resource in the service mesh. For more information about mesh sharing, see [Working with shared meshes](https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html).  
Length Constraints: Fixed length of 12.

## Request Body
<a name="API_CreateVirtualNode_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateVirtualNode_RequestSyntax) **   <a name="appmesh-CreateVirtualNode-request-clientToken"></a>
Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Up to 36 letters, numbers, hyphens, and underscores are allowed.  
Type: String  
Required: No

 ** [spec](#API_CreateVirtualNode_RequestSyntax) **   <a name="appmesh-CreateVirtualNode-request-spec"></a>
The virtual node specification to apply.  
Type: [VirtualNodeSpec](API_VirtualNodeSpec.md) object  
Required: Yes

 ** [tags](#API_CreateVirtualNode_RequestSyntax) **   <a name="appmesh-CreateVirtualNode-request-tags"></a>
Optional metadata that you can apply to the virtual node to assist with categorization and organization. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.  
Type: Array of [TagRef](API_TagRef.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 50 items.  
Required: No

 ** [virtualNodeName](#API_CreateVirtualNode_RequestSyntax) **   <a name="appmesh-CreateVirtualNode-request-virtualNodeName"></a>
The name to use for the virtual node.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: Yes

## Response Syntax
<a name="API_CreateVirtualNode_ResponseSyntax"></a>

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
<a name="API_CreateVirtualNode_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [meshName](#API_CreateVirtualNode_ResponseSyntax) **   <a name="appmesh-CreateVirtualNode-response-meshName"></a>
The name of the service mesh that the virtual node resides in.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [metadata](#API_CreateVirtualNode_ResponseSyntax) **   <a name="appmesh-CreateVirtualNode-response-metadata"></a>
The associated metadata for the virtual node.  
Type: [ResourceMetadata](API_ResourceMetadata.md) object

 ** [spec](#API_CreateVirtualNode_ResponseSyntax) **   <a name="appmesh-CreateVirtualNode-response-spec"></a>
The specifications of the virtual node.  
Type: [VirtualNodeSpec](API_VirtualNodeSpec.md) object

 ** [status](#API_CreateVirtualNode_ResponseSyntax) **   <a name="appmesh-CreateVirtualNode-response-status"></a>
The current status for the virtual node.  
Type: [VirtualNodeStatus](API_VirtualNodeStatus.md) object

 ** [virtualNodeName](#API_CreateVirtualNode_ResponseSyntax) **   <a name="appmesh-CreateVirtualNode-response-virtualNodeName"></a>
The name of the virtual node.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.

## Errors
<a name="API_CreateVirtualNode_Errors"></a>

 ** BadRequestException **   
The request syntax was malformed. Check your request syntax and try again.  
HTTP Status Code: 400

 ** ConflictException **   
The request contains a client token that was used for a previous update resource call with different specifications. Try the request again with a new client token.  
HTTP Status Code: 409

 ** ForbiddenException **   
You don't have permissions to perform this action.  
HTTP Status Code: 403

 ** InternalServerErrorException **   
The request processing has failed because of an unknown error, exception, or failure.  
HTTP Status Code: 500

 ** LimitExceededException **   
You have exceeded a service limit for your account. For more information, see [Service Limits](https://docs.aws.amazon.com/app-mesh/latest/userguide/service-quotas.html) in the * AWS App Mesh User Guide*.  
HTTP Status Code: 400

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
<a name="API_CreateVirtualNode_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You need to learn how to sign HTTP requests only if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_CreateVirtualNode_Example_1"></a>

The following example creates a virtual node named `colorgateway-vn` in the `ecs-mesh` service mesh.

#### Sample Request
<a name="API_CreateVirtualNode_Example_1_Request"></a>

```
PUT /v20190125/meshes/ecs-mesh/virtualNodes HTTP/1.1
Host: appmesh.us-east-1.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/1.16.56 Python/3.7.0 Darwin/17.7.0 botocore/1.12.46
X-Amz-Date: 20190227T192431Z
Authorization: AUTHPARAMS

{
  "spec": {
    "listeners": [
      {
        "portMapping": {
          "port": 9080,
          "protocol": "http"
        }
      }
    ],
    "serviceDiscovery": {
      "dns": {
        "hostname": "colorgateway.default.svc.cluster.local"
      }
    },
    "backends": [
      {
        "virtualService": {
          "virtualServiceName": "tcpecho.default.svc.cluster.local"
        }
      },
      {
        "virtualService": {
          "virtualServiceName": "colorteller.default.svc.cluster.local"
        }
      }
    ]
  },
  "virtualNodeName": "colorgateway-vn",
  "clientToken": "c148ccbb-3619-49da-bb3e-4561eb5370c4"
}
```

#### Sample Response
<a name="API_CreateVirtualNode_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-requestid: cc29e2dd-e4c4-4d6e-9424-e9211580f70e
content-type: application/json
content-length: 687
date: Wed, 27 Feb 2019 19:24:31 GMT
x-envoy-upstream-service-time: 132
server: envoy
Connection: keep-alive

{
	"meshName": "ecs-mesh",
	"metadata": {
		"arn": "arn:aws:appmesh:us-east-1:123456789012:mesh/ecs-mesh/virtualNode/colorgateway-vn",
		"createdAt": 1.551295471546E9,
		"lastUpdatedAt": 1.551295471546E9,
		"uid": "887cfab8-a727-41b2-8cd7-2fdebfd6304e",
		"version": 1
	},
	"spec": {
		"backends": [{
			"virtualService": {
				"virtualServiceName": "tcpecho.default.svc.cluster.local"
			}
		}, {
			"virtualService": {
				"virtualServiceName": "colorteller.default.svc.cluster.local"
			}
		}],
		"listeners": [{
			"healthCheck": null,
			"portMapping": {
				"port": 9080,
				"protocol": "http"
			}
		}],
		"logging": null,
		"serviceDiscovery": {
			"dns": {
				"hostname": "colorgateway.default.svc.cluster.local"
			}
		}
	},
	"status": {
		"status": "ACTIVE"
	},
	"virtualNodeName": "colorgateway-vn"
}
```

## See Also
<a name="API_CreateVirtualNode_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appmesh-2019-01-25/CreateVirtualNode) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appmesh-2019-01-25/CreateVirtualNode) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/CreateVirtualNode) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appmesh-2019-01-25/CreateVirtualNode) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/CreateVirtualNode) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appmesh-2019-01-25/CreateVirtualNode) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appmesh-2019-01-25/CreateVirtualNode) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appmesh-2019-01-25/CreateVirtualNode) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appmesh-2019-01-25/CreateVirtualNode) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/CreateVirtualNode) 