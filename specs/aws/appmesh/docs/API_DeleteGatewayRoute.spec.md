---
id: "@specs/aws/appmesh/docs/API_DeleteGatewayRoute"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteGatewayRoute"
status: active
depends_on:
  - "@specs/aws/appmesh/meta"
---

# DeleteGatewayRoute

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appmesh/docs/API_DeleteGatewayRoute
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteGatewayRoute
<a name="API_DeleteGatewayRoute"></a>

Deletes an existing gateway route.

## Request Syntax
<a name="API_DeleteGatewayRoute_RequestSyntax"></a>

```
DELETE /v20190125/meshes/{{meshName}}/virtualGateway/{{virtualGatewayName}}/gatewayRoutes/{{gatewayRouteName}}?meshOwner={{meshOwner}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteGatewayRoute_RequestParameters"></a>

The request uses the following URI parameters.

 ** [gatewayRouteName](#API_DeleteGatewayRoute_RequestSyntax) **   <a name="appmesh-DeleteGatewayRoute-request-uri-gatewayRouteName"></a>
The name of the gateway route to delete.  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: Yes

 ** [meshName](#API_DeleteGatewayRoute_RequestSyntax) **   <a name="appmesh-DeleteGatewayRoute-request-uri-meshName"></a>
The name of the service mesh to delete the gateway route from.  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: Yes

 ** [meshOwner](#API_DeleteGatewayRoute_RequestSyntax) **   <a name="appmesh-DeleteGatewayRoute-request-uri-meshOwner"></a>
The AWS IAM account ID of the service mesh owner. If the account ID is not your own, then it's the ID of the account that shared the mesh with your account. For more information about mesh sharing, see [Working with shared meshes](https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html).  
Length Constraints: Fixed length of 12.

 ** [virtualGatewayName](#API_DeleteGatewayRoute_RequestSyntax) **   <a name="appmesh-DeleteGatewayRoute-request-uri-virtualGatewayName"></a>
The name of the virtual gateway to delete the route from.  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: Yes

## Request Body
<a name="API_DeleteGatewayRoute_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteGatewayRoute_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "gatewayRouteName": "string",
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
      "grpcRoute": { 
         "action": { 
            "rewrite": { 
               "hostname": { 
                  "defaultTargetHostname": "string"
               }
            },
            "target": { 
               "port": number,
               "virtualService": { 
                  "virtualServiceName": "string"
               }
            }
         },
         "match": { 
            "hostname": { 
               "exact": "string",
               "suffix": "string"
            },
            "metadata": [ 
               { 
                  "invert": boolean,
                  "match": { ... },
                  "name": "string"
               }
            ],
            "port": number,
            "serviceName": "string"
         }
      },
      "http2Route": { 
         "action": { 
            "rewrite": { 
               "hostname": { 
                  "defaultTargetHostname": "string"
               },
               "path": { 
                  "exact": "string"
               },
               "prefix": { 
                  "defaultPrefix": "string",
                  "value": "string"
               }
            },
            "target": { 
               "port": number,
               "virtualService": { 
                  "virtualServiceName": "string"
               }
            }
         },
         "match": { 
            "headers": [ 
               { 
                  "invert": boolean,
                  "match": { ... },
                  "name": "string"
               }
            ],
            "hostname": { 
               "exact": "string",
               "suffix": "string"
            },
            "method": "string",
            "path": { 
               "exact": "string",
               "regex": "string"
            },
            "port": number,
            "prefix": "string",
            "queryParameters": [ 
               { 
                  "match": { 
                     "exact": "string"
                  },
                  "name": "string"
               }
            ]
         }
      },
      "httpRoute": { 
         "action": { 
            "rewrite": { 
               "hostname": { 
                  "defaultTargetHostname": "string"
               },
               "path": { 
                  "exact": "string"
               },
               "prefix": { 
                  "defaultPrefix": "string",
                  "value": "string"
               }
            },
            "target": { 
               "port": number,
               "virtualService": { 
                  "virtualServiceName": "string"
               }
            }
         },
         "match": { 
            "headers": [ 
               { 
                  "invert": boolean,
                  "match": { ... },
                  "name": "string"
               }
            ],
            "hostname": { 
               "exact": "string",
               "suffix": "string"
            },
            "method": "string",
            "path": { 
               "exact": "string",
               "regex": "string"
            },
            "port": number,
            "prefix": "string",
            "queryParameters": [ 
               { 
                  "match": { 
                     "exact": "string"
                  },
                  "name": "string"
               }
            ]
         }
      },
      "priority": number
   },
   "status": { 
      "status": "string"
   },
   "virtualGatewayName": "string"
}
```

## Response Elements
<a name="API_DeleteGatewayRoute_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [gatewayRouteName](#API_DeleteGatewayRoute_ResponseSyntax) **   <a name="appmesh-DeleteGatewayRoute-response-gatewayRouteName"></a>
The name of the gateway route.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [meshName](#API_DeleteGatewayRoute_ResponseSyntax) **   <a name="appmesh-DeleteGatewayRoute-response-meshName"></a>
The name of the service mesh that the resource resides in.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [metadata](#API_DeleteGatewayRoute_ResponseSyntax) **   <a name="appmesh-DeleteGatewayRoute-response-metadata"></a>
An object that represents metadata for a resource.  
Type: [ResourceMetadata](API_ResourceMetadata.md) object

 ** [spec](#API_DeleteGatewayRoute_ResponseSyntax) **   <a name="appmesh-DeleteGatewayRoute-response-spec"></a>
The specifications of the gateway route.  
Type: [GatewayRouteSpec](API_GatewayRouteSpec.md) object

 ** [status](#API_DeleteGatewayRoute_ResponseSyntax) **   <a name="appmesh-DeleteGatewayRoute-response-status"></a>
The status of the gateway route.  
Type: [GatewayRouteStatus](API_GatewayRouteStatus.md) object

 ** [virtualGatewayName](#API_DeleteGatewayRoute_ResponseSyntax) **   <a name="appmesh-DeleteGatewayRoute-response-virtualGatewayName"></a>
The virtual gateway that the gateway route is associated with.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.

## Errors
<a name="API_DeleteGatewayRoute_Errors"></a>

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

 ** ResourceInUseException **   
You can't delete the specified resource because it's in use or required by another resource.  
HTTP Status Code: 409

 ** ServiceUnavailableException **   
The request has failed due to a temporary failure of the service.  
HTTP Status Code: 503

 ** TooManyRequestsException **   
The maximum request rate permitted by the App Mesh APIs has been exceeded for your account. For best results, use an increasing or variable sleep interval between requests.  
HTTP Status Code: 429

## Examples
<a name="API_DeleteGatewayRoute_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You need to learn how to sign HTTP requests only if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_DeleteGatewayRoute_Example_1"></a>

The following example deletes a gateway route named `myGatewayRoute` from the `myVirtualGateway` virtual gateway that is in the `apps` service mesh. 

#### Sample Request
<a name="API_DeleteGatewayRoute_Example_1_Request"></a>

```
DELETE /v20190125/meshes/apps/virtualGateway/myVirtualGateway/gatewayRoutes/myGatewayRoute HTTP/1.1
Host: appmesh.us-west-2.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/1.16.298 Python/3.6.0 Windows/10 botocore/1.13.34
X-Amz-Date: 20200608T193419Z
Authorization: AUTHPARAMS
```

#### Sample Response
<a name="API_DeleteGatewayRoute_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-requestid: a7e8bcc1-0dec-464d-9e69-5cd1f780c9eb
content-type: application/json
content-length: 618
date: Mon, 08 Jun 2020 19:34:19 GMT
x-envoy-upstream-service-time: 49
server: envoy
Connection: keep-alive

{
	"gatewayRouteName": "myGatewayRoute",
	"meshName": "myApps",
	"metadata": {
		"arn": "arn:aws:appmesh:us-west-2:123456789012:mesh/apps/virtualGateway/myVirtualGateway/gatewayRoute/myGatewayRoute",
		"createdAt": 1.591642091122E9,
		"lastUpdatedAt": 1.591644859804E9,
		"meshOwner": "123456789012",
		"resourceOwner": "123456789012",
		"uid": "ff111ff2-33ff-4ff4-ffff-111f111f111f",
		"version": 3
	},
	"spec": {
		"grpcRoute": null,
		"http2Route": {
			"action": {
				"target": {
					"virtualService": {
						"virtualServiceName": "myserviceb.svc.cluster.local"
					}
				}
			},
			"match": {
				"prefix": "/"
			}
		},
		"httpRoute": null
	},
	"status": {
		"status": "DELETED"
	},
	"virtualGatewayName": "myVirtualGateway"
}
```

## See Also
<a name="API_DeleteGatewayRoute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appmesh-2019-01-25/DeleteGatewayRoute) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appmesh-2019-01-25/DeleteGatewayRoute) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/DeleteGatewayRoute) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appmesh-2019-01-25/DeleteGatewayRoute) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/DeleteGatewayRoute) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appmesh-2019-01-25/DeleteGatewayRoute) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appmesh-2019-01-25/DeleteGatewayRoute) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appmesh-2019-01-25/DeleteGatewayRoute) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appmesh-2019-01-25/DeleteGatewayRoute) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/DeleteGatewayRoute) 