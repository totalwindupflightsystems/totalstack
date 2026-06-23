---
id: "@specs/aws/appmesh/docs/API_UpdateVirtualGateway"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateVirtualGateway"
status: active
depends_on:
  - "@specs/aws/appmesh/meta"
---

# UpdateVirtualGateway

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appmesh/docs/API_UpdateVirtualGateway
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateVirtualGateway
<a name="API_UpdateVirtualGateway"></a>

Updates an existing virtual gateway in a specified service mesh.

## Request Syntax
<a name="API_UpdateVirtualGateway_RequestSyntax"></a>

```
PUT /v20190125/meshes/{{meshName}}/virtualGateways/{{virtualGatewayName}}?meshOwner={{meshOwner}} HTTP/1.1
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
   }
}
```

## URI Request Parameters
<a name="API_UpdateVirtualGateway_RequestParameters"></a>

The request uses the following URI parameters.

 ** [meshName](#API_UpdateVirtualGateway_RequestSyntax) **   <a name="appmesh-UpdateVirtualGateway-request-uri-meshName"></a>
The name of the service mesh that the virtual gateway resides in.  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: Yes

 ** [meshOwner](#API_UpdateVirtualGateway_RequestSyntax) **   <a name="appmesh-UpdateVirtualGateway-request-uri-meshOwner"></a>
The AWS IAM account ID of the service mesh owner. If the account ID is not your own, then it's the ID of the account that shared the mesh with your account. For more information about mesh sharing, see [Working with shared meshes](https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html).  
Length Constraints: Fixed length of 12.

 ** [virtualGatewayName](#API_UpdateVirtualGateway_RequestSyntax) **   <a name="appmesh-UpdateVirtualGateway-request-uri-virtualGatewayName"></a>
The name of the virtual gateway to update.  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: Yes

## Request Body
<a name="API_UpdateVirtualGateway_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_UpdateVirtualGateway_RequestSyntax) **   <a name="appmesh-UpdateVirtualGateway-request-clientToken"></a>
Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Up to 36 letters, numbers, hyphens, and underscores are allowed.  
Type: String  
Required: No

 ** [spec](#API_UpdateVirtualGateway_RequestSyntax) **   <a name="appmesh-UpdateVirtualGateway-request-spec"></a>
The new virtual gateway specification to apply. This overwrites the existing data.  
Type: [VirtualGatewaySpec](API_VirtualGatewaySpec.md) object  
Required: Yes

## Response Syntax
<a name="API_UpdateVirtualGateway_ResponseSyntax"></a>

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
<a name="API_UpdateVirtualGateway_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [meshName](#API_UpdateVirtualGateway_ResponseSyntax) **   <a name="appmesh-UpdateVirtualGateway-response-meshName"></a>
The name of the service mesh that the virtual gateway resides in.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [metadata](#API_UpdateVirtualGateway_ResponseSyntax) **   <a name="appmesh-UpdateVirtualGateway-response-metadata"></a>
An object that represents metadata for a resource.  
Type: [ResourceMetadata](API_ResourceMetadata.md) object

 ** [spec](#API_UpdateVirtualGateway_ResponseSyntax) **   <a name="appmesh-UpdateVirtualGateway-response-spec"></a>
The specifications of the virtual gateway.  
Type: [VirtualGatewaySpec](API_VirtualGatewaySpec.md) object

 ** [status](#API_UpdateVirtualGateway_ResponseSyntax) **   <a name="appmesh-UpdateVirtualGateway-response-status"></a>
The current status of the virtual gateway.  
Type: [VirtualGatewayStatus](API_VirtualGatewayStatus.md) object

 ** [virtualGatewayName](#API_UpdateVirtualGateway_ResponseSyntax) **   <a name="appmesh-UpdateVirtualGateway-response-virtualGatewayName"></a>
The name of the virtual gateway.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.

## Errors
<a name="API_UpdateVirtualGateway_Errors"></a>

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
<a name="API_UpdateVirtualGateway_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You need to learn how to sign HTTP requests only if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_UpdateVirtualGateway_Example_1"></a>

The following example updates a virtual gateway named `myVirtualGateway` in the `apps` service mesh. 

#### Sample Request
<a name="API_UpdateVirtualGateway_Example_1_Request"></a>

```
PUT /v20190125/meshes/apps/virtualGateways/myVirtualGateway HTTP/1.1
Host: appmesh.us-west-2.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/1.16.298 Python/3.6.0 Windows/10 botocore/1.13.34
X-Amz-Date: 20200706T151140Z
Authorization: AUTHPARAMS

{
	"spec": {
		"listeners": [{
			"portMapping": {
				"port": 8080,
				"protocol": "http2"
			}
		}]
	},
	"clientToken": "1aa1111a-1111-1111-111a-a1a1a1aa111a"
}
```

#### Sample Response
<a name="API_UpdateVirtualGateway_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-requestid: 009bf6b9-c86a-40ba-b6a4-45cb41badc77
content-type: application/json
content-length: 515
date: Mon, 06 Jul 2020 15:11:40 GMT
x-envoy-upstream-service-time: 34
server: envoy
Connection: keep-alive

{
	"meshName": "apps",
	"metadata": {
		"arn": "arn:aws:appmesh:us-west-2:123456789012:mesh/apps/virtualGateway/myVirtualGateway",
		"createdAt": 1.594048239495E9,
		"lastUpdatedAt": 1.594048300694E9,
		"meshOwner": "123456789012",
		"resourceOwner": "123456789012",
		"uid": "ff111ff2-33ff-4ff4-ffff-111f111f111f",
		"version": 2
	},
	"spec": {
		"backendDefaults": null,
		"listeners": [{
			"healthCheck": null,
			"portMapping": {
				"port": 8080,
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
<a name="API_UpdateVirtualGateway_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appmesh-2019-01-25/UpdateVirtualGateway) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appmesh-2019-01-25/UpdateVirtualGateway) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/UpdateVirtualGateway) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appmesh-2019-01-25/UpdateVirtualGateway) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/UpdateVirtualGateway) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appmesh-2019-01-25/UpdateVirtualGateway) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appmesh-2019-01-25/UpdateVirtualGateway) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appmesh-2019-01-25/UpdateVirtualGateway) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appmesh-2019-01-25/UpdateVirtualGateway) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/UpdateVirtualGateway) 