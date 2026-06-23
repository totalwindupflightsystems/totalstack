---
id: "@specs/aws/appmesh/docs/API_CreateRoute"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateRoute"
status: active
depends_on:
  - "@specs/aws/appmesh/meta"
---

# CreateRoute

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appmesh/docs/API_CreateRoute
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateRoute
<a name="API_CreateRoute"></a>

Creates a route that is associated with a virtual router.

 You can route several different protocols and define a retry policy for a route. Traffic can be routed to one or more virtual nodes.

For more information about routes, see [Routes](https://docs.aws.amazon.com/app-mesh/latest/userguide/routes.html).

## Request Syntax
<a name="API_CreateRoute_RequestSyntax"></a>

```
PUT /v20190125/meshes/{{meshName}}/virtualRouter/{{virtualRouterName}}/routes?meshOwner={{meshOwner}} HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "routeName": "{{string}}",
   "spec": { 
      "grpcRoute": { 
         "action": { 
            "weightedTargets": [ 
               { 
                  "port": {{number}},
                  "virtualNode": "{{string}}",
                  "weight": {{number}}
               }
            ]
         },
         "match": { 
            "metadata": [ 
               { 
                  "invert": {{boolean}},
                  "match": { ... },
                  "name": "{{string}}"
               }
            ],
            "methodName": "{{string}}",
            "port": {{number}},
            "serviceName": "{{string}}"
         },
         "retryPolicy": { 
            "grpcRetryEvents": [ "{{string}}" ],
            "httpRetryEvents": [ "{{string}}" ],
            "maxRetries": {{number}},
            "perRetryTimeout": { 
               "unit": "{{string}}",
               "value": {{number}}
            },
            "tcpRetryEvents": [ "{{string}}" ]
         },
         "timeout": { 
            "idle": { 
               "unit": "{{string}}",
               "value": {{number}}
            },
            "perRequest": { 
               "unit": "{{string}}",
               "value": {{number}}
            }
         }
      },
      "http2Route": { 
         "action": { 
            "weightedTargets": [ 
               { 
                  "port": {{number}},
                  "virtualNode": "{{string}}",
                  "weight": {{number}}
               }
            ]
         },
         "match": { 
            "headers": [ 
               { 
                  "invert": {{boolean}},
                  "match": { ... },
                  "name": "{{string}}"
               }
            ],
            "method": "{{string}}",
            "path": { 
               "exact": "{{string}}",
               "regex": "{{string}}"
            },
            "port": {{number}},
            "prefix": "{{string}}",
            "queryParameters": [ 
               { 
                  "match": { 
                     "exact": "{{string}}"
                  },
                  "name": "{{string}}"
               }
            ],
            "scheme": "{{string}}"
         },
         "retryPolicy": { 
            "httpRetryEvents": [ "{{string}}" ],
            "maxRetries": {{number}},
            "perRetryTimeout": { 
               "unit": "{{string}}",
               "value": {{number}}
            },
            "tcpRetryEvents": [ "{{string}}" ]
         },
         "timeout": { 
            "idle": { 
               "unit": "{{string}}",
               "value": {{number}}
            },
            "perRequest": { 
               "unit": "{{string}}",
               "value": {{number}}
            }
         }
      },
      "httpRoute": { 
         "action": { 
            "weightedTargets": [ 
               { 
                  "port": {{number}},
                  "virtualNode": "{{string}}",
                  "weight": {{number}}
               }
            ]
         },
         "match": { 
            "headers": [ 
               { 
                  "invert": {{boolean}},
                  "match": { ... },
                  "name": "{{string}}"
               }
            ],
            "method": "{{string}}",
            "path": { 
               "exact": "{{string}}",
               "regex": "{{string}}"
            },
            "port": {{number}},
            "prefix": "{{string}}",
            "queryParameters": [ 
               { 
                  "match": { 
                     "exact": "{{string}}"
                  },
                  "name": "{{string}}"
               }
            ],
            "scheme": "{{string}}"
         },
         "retryPolicy": { 
            "httpRetryEvents": [ "{{string}}" ],
            "maxRetries": {{number}},
            "perRetryTimeout": { 
               "unit": "{{string}}",
               "value": {{number}}
            },
            "tcpRetryEvents": [ "{{string}}" ]
         },
         "timeout": { 
            "idle": { 
               "unit": "{{string}}",
               "value": {{number}}
            },
            "perRequest": { 
               "unit": "{{string}}",
               "value": {{number}}
            }
         }
      },
      "priority": {{number}},
      "tcpRoute": { 
         "action": { 
            "weightedTargets": [ 
               { 
                  "port": {{number}},
                  "virtualNode": "{{string}}",
                  "weight": {{number}}
               }
            ]
         },
         "match": { 
            "port": {{number}}
         },
         "timeout": { 
            "idle": { 
               "unit": "{{string}}",
               "value": {{number}}
            }
         }
      }
   },
   "tags": [ 
      { 
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_CreateRoute_RequestParameters"></a>

The request uses the following URI parameters.

 ** [meshName](#API_CreateRoute_RequestSyntax) **   <a name="appmesh-CreateRoute-request-uri-meshName"></a>
The name of the service mesh to create the route in.  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: Yes

 ** [meshOwner](#API_CreateRoute_RequestSyntax) **   <a name="appmesh-CreateRoute-request-uri-meshOwner"></a>
The AWS IAM account ID of the service mesh owner. If the account ID is not your own, then the account that you specify must share the mesh with your account before you can create the resource in the service mesh. For more information about mesh sharing, see [Working with shared meshes](https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html).  
Length Constraints: Fixed length of 12.

 ** [virtualRouterName](#API_CreateRoute_RequestSyntax) **   <a name="appmesh-CreateRoute-request-uri-virtualRouterName"></a>
The name of the virtual router in which to create the route. If the virtual router is in a shared mesh, then you must be the owner of the virtual router resource.  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: Yes

## Request Body
<a name="API_CreateRoute_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateRoute_RequestSyntax) **   <a name="appmesh-CreateRoute-request-clientToken"></a>
Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Up to 36 letters, numbers, hyphens, and underscores are allowed.  
Type: String  
Required: No

 ** [routeName](#API_CreateRoute_RequestSyntax) **   <a name="appmesh-CreateRoute-request-routeName"></a>
The name to use for the route.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: Yes

 ** [spec](#API_CreateRoute_RequestSyntax) **   <a name="appmesh-CreateRoute-request-spec"></a>
The route specification to apply.  
Type: [RouteSpec](API_RouteSpec.md) object  
Required: Yes

 ** [tags](#API_CreateRoute_RequestSyntax) **   <a name="appmesh-CreateRoute-request-tags"></a>
Optional metadata that you can apply to the route to assist with categorization and organization. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.  
Type: Array of [TagRef](API_TagRef.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 50 items.  
Required: No

## Response Syntax
<a name="API_CreateRoute_ResponseSyntax"></a>

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
   "routeName": "string",
   "spec": { 
      "grpcRoute": { 
         "action": { 
            "weightedTargets": [ 
               { 
                  "port": number,
                  "virtualNode": "string",
                  "weight": number
               }
            ]
         },
         "match": { 
            "metadata": [ 
               { 
                  "invert": boolean,
                  "match": { ... },
                  "name": "string"
               }
            ],
            "methodName": "string",
            "port": number,
            "serviceName": "string"
         },
         "retryPolicy": { 
            "grpcRetryEvents": [ "string" ],
            "httpRetryEvents": [ "string" ],
            "maxRetries": number,
            "perRetryTimeout": { 
               "unit": "string",
               "value": number
            },
            "tcpRetryEvents": [ "string" ]
         },
         "timeout": { 
            "idle": { 
               "unit": "string",
               "value": number
            },
            "perRequest": { 
               "unit": "string",
               "value": number
            }
         }
      },
      "http2Route": { 
         "action": { 
            "weightedTargets": [ 
               { 
                  "port": number,
                  "virtualNode": "string",
                  "weight": number
               }
            ]
         },
         "match": { 
            "headers": [ 
               { 
                  "invert": boolean,
                  "match": { ... },
                  "name": "string"
               }
            ],
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
            ],
            "scheme": "string"
         },
         "retryPolicy": { 
            "httpRetryEvents": [ "string" ],
            "maxRetries": number,
            "perRetryTimeout": { 
               "unit": "string",
               "value": number
            },
            "tcpRetryEvents": [ "string" ]
         },
         "timeout": { 
            "idle": { 
               "unit": "string",
               "value": number
            },
            "perRequest": { 
               "unit": "string",
               "value": number
            }
         }
      },
      "httpRoute": { 
         "action": { 
            "weightedTargets": [ 
               { 
                  "port": number,
                  "virtualNode": "string",
                  "weight": number
               }
            ]
         },
         "match": { 
            "headers": [ 
               { 
                  "invert": boolean,
                  "match": { ... },
                  "name": "string"
               }
            ],
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
            ],
            "scheme": "string"
         },
         "retryPolicy": { 
            "httpRetryEvents": [ "string" ],
            "maxRetries": number,
            "perRetryTimeout": { 
               "unit": "string",
               "value": number
            },
            "tcpRetryEvents": [ "string" ]
         },
         "timeout": { 
            "idle": { 
               "unit": "string",
               "value": number
            },
            "perRequest": { 
               "unit": "string",
               "value": number
            }
         }
      },
      "priority": number,
      "tcpRoute": { 
         "action": { 
            "weightedTargets": [ 
               { 
                  "port": number,
                  "virtualNode": "string",
                  "weight": number
               }
            ]
         },
         "match": { 
            "port": number
         },
         "timeout": { 
            "idle": { 
               "unit": "string",
               "value": number
            }
         }
      }
   },
   "status": { 
      "status": "string"
   },
   "virtualRouterName": "string"
}
```

## Response Elements
<a name="API_CreateRoute_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [meshName](#API_CreateRoute_ResponseSyntax) **   <a name="appmesh-CreateRoute-response-meshName"></a>
The name of the service mesh that the route resides in.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [metadata](#API_CreateRoute_ResponseSyntax) **   <a name="appmesh-CreateRoute-response-metadata"></a>
The associated metadata for the route.  
Type: [ResourceMetadata](API_ResourceMetadata.md) object

 ** [routeName](#API_CreateRoute_ResponseSyntax) **   <a name="appmesh-CreateRoute-response-routeName"></a>
The name of the route.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [spec](#API_CreateRoute_ResponseSyntax) **   <a name="appmesh-CreateRoute-response-spec"></a>
The specifications of the route.  
Type: [RouteSpec](API_RouteSpec.md) object

 ** [status](#API_CreateRoute_ResponseSyntax) **   <a name="appmesh-CreateRoute-response-status"></a>
The status of the route.  
Type: [RouteStatus](API_RouteStatus.md) object

 ** [virtualRouterName](#API_CreateRoute_ResponseSyntax) **   <a name="appmesh-CreateRoute-response-virtualRouterName"></a>
The virtual router that the route is associated with.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.

## Errors
<a name="API_CreateRoute_Errors"></a>

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
<a name="API_CreateRoute_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You need to learn how to sign HTTP requests only if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_CreateRoute_Example_1"></a>

The following example creates a route named `colorgateway-route` for the `colorgateway-vr` virtual router in the `ecs-mesh` service mesh. The route directs all traffic to the `colorgateway-vn` virtual node.

#### Sample Request
<a name="API_CreateRoute_Example_1_Request"></a>

```
PUT /v20190125/meshes/ecs-mesh/virtualRouter/colorgateway-vr/routes HTTP/1.1
Host: appmesh.us-east-1.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/1.16.56 Python/3.7.0 Darwin/17.7.0 botocore/1.12.46
X-Amz-Date: 20190227T192454Z
Authorization: AUTHPARAMS

{
  "routeName": "colorgateway-route",
  "spec": {
    "httpRoute": {
      "action": {
        "weightedTargets": [
          {
            "virtualNode": "colorgateway-vn",
            "weight": 100
          }
        ]
      },
      "match": {
        "prefix": "/"
      }
    }
  },
  "clientToken": "a785b959-201d-49d7-b81d-32e7f393968f"
}
```

#### Sample Response
<a name="API_CreateRoute_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-requestid: 159941a8-18be-423c-89fe-3beb9542ca3f
content-type: application/json
content-length: 511
date: Wed, 27 Feb 2019 19:24:54 GMT
x-envoy-upstream-service-time: 59
server: envoy
Connection: keep-alive

{
	"meshName": "ecs-mesh",
	"metadata": {
		"arn": "arn:aws:appmesh:us-east-1:123456789012:mesh/ecs-mesh/virtualRouter/colorgateway-vr/route/colorgateway-route",
		"createdAt": 1.551295495004E9,
		"lastUpdatedAt": 1.551295495004E9,
		"uid": "3251bf37-2d01-4b79-be96-d0c36c61511f",
		"version": 1
	},
	"routeName": "colorgateway-route",
	"spec": {
		"httpRoute": {
			"action": {
				"weightedTargets": [{
					"virtualNode": "colorgateway-vn",
					"weight": 100
				}]
			},
			"match": {
				"prefix": "/"
			}
		},
		"tcpRoute": null
	},
	"status": {
		"status": "ACTIVE"
	},
	"virtualRouterName": "colorgateway-vr"
}
```

## See Also
<a name="API_CreateRoute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appmesh-2019-01-25/CreateRoute) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appmesh-2019-01-25/CreateRoute) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/CreateRoute) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appmesh-2019-01-25/CreateRoute) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/CreateRoute) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appmesh-2019-01-25/CreateRoute) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appmesh-2019-01-25/CreateRoute) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appmesh-2019-01-25/CreateRoute) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appmesh-2019-01-25/CreateRoute) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/CreateRoute) 