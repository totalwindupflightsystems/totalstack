---
id: "@specs/aws/eks/docs/API_ListAssociatedAccessPolicies"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListAssociatedAccessPolicies"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# ListAssociatedAccessPolicies

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_ListAssociatedAccessPolicies
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListAssociatedAccessPolicies
<a name="API_ListAssociatedAccessPolicies"></a>

Lists the access policies associated with an access entry.

## Request Syntax
<a name="API_ListAssociatedAccessPolicies_RequestSyntax"></a>

```
GET /clusters/{{name}}/access-entries/{{principalArn}}/access-policies?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListAssociatedAccessPolicies_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_ListAssociatedAccessPolicies_RequestSyntax) **   <a name="AmazonEKS-ListAssociatedAccessPolicies-request-uri-clusterName"></a>
The name of your cluster.  
Required: Yes

 ** [maxResults](#API_ListAssociatedAccessPolicies_RequestSyntax) **   <a name="AmazonEKS-ListAssociatedAccessPolicies-request-uri-maxResults"></a>
The maximum number of results, returned in paginated output. You receive `maxResults` in a single page, along with a `nextToken` response element. You can see the remaining results of the initial request by sending another request with the returned `nextToken` value. This value can be between 1 and 100. If you don't use this parameter, 100 results and a `nextToken` value, if applicable, are returned.  
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListAssociatedAccessPolicies_RequestSyntax) **   <a name="AmazonEKS-ListAssociatedAccessPolicies-request-uri-nextToken"></a>
The `nextToken` value returned from a previous paginated request, where `maxResults` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the `nextToken` value. This value is null when there are no more results to return.  
This token should be treated as an opaque identifier that is used only to retrieve the next items in a list and not for other programmatic purposes.

 ** [principalArn](#API_ListAssociatedAccessPolicies_RequestSyntax) **   <a name="AmazonEKS-ListAssociatedAccessPolicies-request-uri-principalArn"></a>
The ARN of the IAM principal for the `AccessEntry`.  
Required: Yes

## Request Body
<a name="API_ListAssociatedAccessPolicies_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListAssociatedAccessPolicies_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "associatedAccessPolicies": [ 
      { 
         "accessScope": { 
            "namespaces": [ "string" ],
            "type": "string"
         },
         "associatedAt": number,
         "modifiedAt": number,
         "policyArn": "string"
      }
   ],
   "clusterName": "string",
   "nextToken": "string",
   "principalArn": "string"
}
```

## Response Elements
<a name="API_ListAssociatedAccessPolicies_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [associatedAccessPolicies](#API_ListAssociatedAccessPolicies_ResponseSyntax) **   <a name="AmazonEKS-ListAssociatedAccessPolicies-response-associatedAccessPolicies"></a>
The list of access policies associated with the access entry.  
Type: Array of [AssociatedAccessPolicy](API_AssociatedAccessPolicy.md) objects

 ** [clusterName](#API_ListAssociatedAccessPolicies_ResponseSyntax) **   <a name="AmazonEKS-ListAssociatedAccessPolicies-response-clusterName"></a>
The name of your cluster.  
Type: String

 ** [nextToken](#API_ListAssociatedAccessPolicies_ResponseSyntax) **   <a name="AmazonEKS-ListAssociatedAccessPolicies-response-nextToken"></a>
The `nextToken` value returned from a previous paginated request, where `maxResults` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the `nextToken` value. This value is null when there are no more results to return.  
This token should be treated as an opaque identifier that is used only to retrieve the next items in a list and not for other programmatic purposes.
Type: String

 ** [principalArn](#API_ListAssociatedAccessPolicies_ResponseSyntax) **   <a name="AmazonEKS-ListAssociatedAccessPolicies-response-principalArn"></a>
The ARN of the IAM principal for the `AccessEntry`.  
Type: String

## Errors
<a name="API_ListAssociatedAccessPolicies_Errors"></a>

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md).

 ** InvalidRequestException **   
The request is invalid given the state of the cluster. Check the state of the cluster and the associated operations.    
 ** addonName **   
The request is invalid given the state of the add-on name. Check the state of the cluster and the associated operations.  
 ** clusterName **   
The Amazon EKS cluster associated with the exception.  
 ** message **   
The Amazon EKS add-on name associated with the exception.  
 ** nodegroupName **   
The Amazon EKS managed node group associated with the exception.  
 ** subscriptionId **   
The Amazon EKS subscription ID with the exception.
HTTP Status Code: 400

 ** ResourceNotFoundException **   
The specified resource could not be found. You can view your available clusters with `ListClusters`. You can view your available managed node groups with `ListNodegroups`. Amazon EKS clusters and node groups are AWS Region specific.    
 ** addonName **   
The Amazon EKS add-on name associated with the exception.  
 ** clusterName **   
The Amazon EKS cluster associated with the exception.  
 ** fargateProfileName **   
The Fargate profile associated with the exception.  
 ** message **   
The Amazon EKS message associated with the exception.  
 ** nodegroupName **   
The Amazon EKS managed node group associated with the exception.  
 ** subscriptionId **   
The Amazon EKS subscription ID with the exception.
HTTP Status Code: 404

 ** ServerException **   
These errors are usually caused by a server-side issue.    
 ** addonName **   
The Amazon EKS add-on name associated with the exception.  
 ** clusterName **   
The Amazon EKS cluster associated with the exception.  
 ** message **   
These errors are usually caused by a server-side issue.  
 ** nodegroupName **   
The Amazon EKS managed node group associated with the exception.  
 ** subscriptionId **   
The Amazon EKS subscription ID with the exception.
HTTP Status Code: 500

## Examples
<a name="API_ListAssociatedAccessPolicies_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the *Amazon EKS General Reference*.

You need to learn how to sign HTTP requests only if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_ListAssociatedAccessPolicies_Example_1"></a>

The following example lists the access policies that are associated with an access entry.

#### Sample Request
<a name="API_ListAssociatedAccessPolicies_Example_1_Request"></a>

```
GET /clusters/my-cluster/access-entries/arn%3Aaws%3Aiam%3A%3A012345678910%3Arole%2Fmy-role/access-policies HTTP/1.1
Host: eks.us-west-2.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/2.9.0 Python/3.9.11 Windows/10 exe/AMD64 prompt/off command/eks.list-associated-access-policies
X-Amz-Date: 20230531T155324Z
Authorization: AUTHPARAMS
```

#### Sample Response
<a name="API_ListAssociatedAccessPolicies_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Wed, 31 May 2023 15:53:34 GMT
Content-Type: application/json
Content-Length: 306
x-amzn-RequestId: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx
Access-Control-Allow-Origin: *
Access-Control-Allow-Headers: *,Authorization,Date,X-Amz-Date,X-Amz-Security-Token,X-Amz-Target,content-type,x-amz-content-sha256,x-amz-user-agent,x-amzn-platform-id,x-amzn-trace-id
x-amz-apigw-id: Fy4KSHE1vHcFWCQ=
Access-Control-Allow-Methods: GET,HEAD,PUT,POST,DELETE,OPTIONS
Access-Control-Expose-Headers: x-amzn-errortype,x-amzn-errormessage,x-amzn-trace-id,x-amzn-requestid,x-amz-apigw-id,date
X-Amzn-Trace-Id: Root=1-xxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxxx
Connection: keep-alive


{
	"clusterName": "my-cluster",
	"principalArn": "arn:aws:iam::012345678910:role/my-role",
	"nextToken": null,
	"associatedAccessPolicies": [{
		"policyArn": "arn:aws:eks::aws:cluster-access-policy/AmazonEKSAdminPolicy",
		"accessScope": {
			"type": "cluster",
			"namespaces": []
		},
		"associatedAt": 1685540747.281,
		"modifiedAt": 1685540747.281
	}]
}
```

## See Also
<a name="API_ListAssociatedAccessPolicies_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eks-2017-11-01/ListAssociatedAccessPolicies) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eks-2017-11-01/ListAssociatedAccessPolicies) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/ListAssociatedAccessPolicies) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eks-2017-11-01/ListAssociatedAccessPolicies) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/ListAssociatedAccessPolicies) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eks-2017-11-01/ListAssociatedAccessPolicies) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eks-2017-11-01/ListAssociatedAccessPolicies) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eks-2017-11-01/ListAssociatedAccessPolicies) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/eks-2017-11-01/ListAssociatedAccessPolicies) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/ListAssociatedAccessPolicies) 