---
id: "@specs/aws/appmesh/docs/API_CreateVirtualGateway"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateVirtualGateway"
status: active
depends_on:
  - "@specs/aws/appmesh/meta"
---

# CreateVirtualGateway

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appmesh/docs/API_CreateVirtualGateway
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateVirtualGateway
<a name="API_CreateVirtualGateway"></a>

Creates a virtual gateway.

A virtual gateway allows resources outside your mesh to communicate to resources that are inside your mesh. The virtual gateway represents an Envoy proxy running in an Amazon ECS task, in a Kubernetes service, or on an Amazon EC2 instance. Unlike a virtual node, which represents an Envoy running with an application, a virtual gateway represents Envoy deployed by itself.

For more information about virtual gateways, see [Virtual gateways](https://docs.aws.amazon.com/app-mesh/latest/userguide/virtual_gateways.html). 

## Request Syntax
<a name="API_CreateVirtualGateway_RequestSyntax"></a>

```
PUT /v20190125/meshes/{{meshName}}/virtualGateways?meshOwner={{meshOwner}} HTTP/1.1
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
            "portMapping": { 
               "port": {{number}},
               "protocol": "{{string}}"
            },
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
      }
   },
   "tags": [ 
      { 
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ],
   "virtualGatewayName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateVirtualGateway_RequestParameters"></a>

The request uses the following URI parameters.

 ** [meshName](#API_CreateVirtualGateway_RequestSyntax) **   <a name="appmesh-CreateVirtualGateway-request-uri-meshName"></a>
The name of the service mesh to create the virtual gateway in.  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: Yes

 ** [meshOwner](#API_CreateVirtualGateway_RequestSyntax) **   <a name="appmesh-CreateVirtualGateway-request-uri-meshOwner"></a>
The AWS IAM account ID of the service mesh owner. If the account ID is not your own, then the account that you specify must share the mesh with your account before you can create the resource in the service mesh. For more information about mesh sharing, see [Working with shared meshes](https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html).  
Length Constraints: Fixed length of 12.

## Request Body
<a name="API_CreateVirtualGateway_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateVirtualGateway_RequestSyntax) **   <a name="appmesh-CreateVirtualGateway-request-clientToken"></a>
Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Up to 36 letters, numbers, hyphens, and underscores are allowed.  
Type: String  
Required: No

 ** [spec](#API_CreateVirtualGateway_RequestSyntax) **   <a name="appmesh-CreateVirtualGateway-request-spec"></a>
The virtual gateway specification to apply.  
Type: [VirtualGatewaySpec](API_VirtualGatewaySpec.md) object  
Required: Yes

 ** [tags](#API_CreateVirtualGateway_RequestSyntax) **   <a name="appmesh-CreateVirtualGateway-request-tags"></a>
Optional metadata that you can apply to the virtual gateway to assist with categorization and organization. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.  
Type: Array of [TagRef](API_TagRef.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 50 items.  
Required: No

 ** [virtualGatewayName](#API_CreateVirtualGateway_RequestSyntax) **   <a name="appmesh-CreateVirtualGateway-request-virtualGatewayName"></a>
The name to use for the virtual gateway.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: Yes

## Response Syntax
<a name="API_CreateVirtualGateway_ResponseSyntax"></a>

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
            "portMapping": { 
               "port": number,
               "protocol": "string"
            },
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
      }
   },
   "status": { 
      "status": "string"
   },
   "virtualGatewayName": "string"
}
```

## Response Elements
<a name="API_CreateVirtualGateway_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [meshName](#API_CreateVirtualGateway_ResponseSyntax) **   <a name="appmesh-CreateVirtualGateway-response-meshName"></a>
The name of the service mesh that the virtual gateway resides in.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [metadata](#API_CreateVirtualGateway_ResponseSyntax) **   <a name="appmesh-CreateVirtualGateway-response-metadata"></a>
An object that represents metadata for a resource.  
Type: [ResourceMetadata](API_ResourceMetadata.md) object

 ** [spec](#API_CreateVirtualGateway_ResponseSyntax) **   <a name="appmesh-CreateVirtualGateway-response-spec"></a>
The specifications of the virtual gateway.  
Type: [VirtualGatewaySpec](API_VirtualGatewaySpec.md) object

 ** [status](#API_CreateVirtualGateway_ResponseSyntax) **   <a name="appmesh-CreateVirtualGateway-response-status"></a>
The current status of the virtual gateway.  
Type: [VirtualGatewayStatus](API_VirtualGatewayStatus.md) object

 ** [virtualGatewayName](#API_CreateVirtualGateway_ResponseSyntax) **   <a name="appmesh-CreateVirtualGateway-response-virtualGatewayName"></a>
The name of the virtual gateway.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.

## Errors
<a name="API_CreateVirtualGateway_Errors"></a>

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
<a name="API_CreateVirtualGateway_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You need to learn how to sign HTTP requests only if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_CreateVirtualGateway_Example_1"></a>

The following example creates a virtual gateway named `myVirtualGateway` in the `apps` service mesh. The virtual gateway listens for `http2` traffic on port `80`.

#### Sample Request
<a name="API_CreateVirtualGateway_Example_1_Request"></a>

```
PUT /v20190125/meshes/apps/virtualGateways HTTP/1.1
Host: appmesh.us-west-2.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/1.16.298 Python/3.6.0 Windows/10 botocore/1.13.34
X-Amz-Date: 20200706T144617Z
Authorization: AUTHPARAMS
Content-Length: 174

{
	"spec": {
		"listeners": [{
			"portMapping": {
				"port": 80,
				"protocol": "http2"
			}
		}]
	},
	"virtualGatewayName": "myVirtualGateway",
	"clientToken": "1aa1111a-1111-1111-111a-a1a1a1aa111a"
}
```

#### Sample Response
<a name="API_CreateVirtualGateway_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-requestid: 696b569b-3593-446d-832c-0a38ce1c53ac
content-type: application/json
content-length: 513
date: Mon, 06 Jul 2020 14:46:17 GMT
x-envoy-upstream-service-time: 33
server: envoy
Connection: keep-alive

{
	"meshName": "apps",
	"metadata": {
		"arn": "arn:aws:appmesh:us-west-2:123456789012:mesh/apps/virtualGateway/myVirtualGateway",
		"createdAt": 1.594046778215E9,
		"lastUpdatedAt": 1.594046778215E9,
		"meshOwner": "123456789012",
		"resourceOwner": "123456789012,
		"uid": "ff111ff2-33ff-4ff4-ffff-111f111f111f",
		"version": 1
	},
	"spec": {
		"backendDefaults": null,
		"listeners": [{
			"healthCheck": null,
			"portMapping": {
				"port": 80,
				"protocol": "http2"
			},
			"tls": null
		}],
		"logging": null
	},
	"status": {
		"status": "ACTIVE"
	},
	"virtualGatewayName": "myVirtualGateway"
}
```

## See Also
<a name="API_CreateVirtualGateway_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appmesh-2019-01-25/CreateVirtualGateway) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appmesh-2019-01-25/CreateVirtualGateway) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/CreateVirtualGateway) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appmesh-2019-01-25/CreateVirtualGateway) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/CreateVirtualGateway) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appmesh-2019-01-25/CreateVirtualGateway) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appmesh-2019-01-25/CreateVirtualGateway) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appmesh-2019-01-25/CreateVirtualGateway) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appmesh-2019-01-25/CreateVirtualGateway) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/CreateVirtualGateway) 