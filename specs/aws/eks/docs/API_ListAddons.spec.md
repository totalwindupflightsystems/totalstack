---
id: "@specs/aws/eks/docs/API_ListAddons"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListAddons"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# ListAddons

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_ListAddons
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListAddons
<a name="API_ListAddons"></a>

Lists the installed add-ons.

## Request Syntax
<a name="API_ListAddons_RequestSyntax"></a>

```
GET /clusters/{{name}}/addons?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListAddons_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_ListAddons_RequestSyntax) **   <a name="AmazonEKS-ListAddons-request-uri-clusterName"></a>
The name of your cluster.  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `^[0-9A-Za-z][A-Za-z0-9\-_]*`   
Required: Yes

 ** [maxResults](#API_ListAddons_RequestSyntax) **   <a name="AmazonEKS-ListAddons-request-uri-maxResults"></a>
The maximum number of results, returned in paginated output. You receive `maxResults` in a single page, along with a `nextToken` response element. You can see the remaining results of the initial request by sending another request with the returned `nextToken` value. This value can be between 1 and 100. If you don't use this parameter, 100 results and a `nextToken` value, if applicable, are returned.  
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListAddons_RequestSyntax) **   <a name="AmazonEKS-ListAddons-request-uri-nextToken"></a>
The `nextToken` value returned from a previous paginated request, where `maxResults` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the `nextToken` value. This value is null when there are no more results to return.  
This token should be treated as an opaque identifier that is used only to retrieve the next items in a list and not for other programmatic purposes.

## Request Body
<a name="API_ListAddons_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListAddons_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "addons": [ "string" ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListAddons_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [addons](#API_ListAddons_ResponseSyntax) **   <a name="AmazonEKS-ListAddons-response-addons"></a>
A list of installed add-ons.  
Type: Array of strings

 ** [nextToken](#API_ListAddons_ResponseSyntax) **   <a name="AmazonEKS-ListAddons-response-nextToken"></a>
The `nextToken` value to include in a future `ListAddons` request. When the results of a `ListAddons` request exceed `maxResults`, you can use this value to retrieve the next page of results. This value is `null` when there are no more results to return.  
This token should be treated as an opaque identifier that is used only to retrieve the next items in a list and not for other programmatic purposes.
Type: String

## Errors
<a name="API_ListAddons_Errors"></a>

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md).

 ** ClientException **   
These errors are usually caused by a client action. Actions can include using an action or resource on behalf of an [IAM principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html) that doesn't have permissions to use the action or resource or specifying an identifier that is not valid.    
 ** addonName **   
The Amazon EKS add-on name associated with the exception.  
 ** clusterName **   
The Amazon EKS cluster associated with the exception.  
 ** message **   
These errors are usually caused by a client action. Actions can include using an action or resource on behalf of an [IAM principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html) that doesn't have permissions to use the action or resource or specifying an identifier that is not valid.  
 ** nodegroupName **   
The Amazon EKS managed node group associated with the exception.  
 ** subscriptionId **   
The Amazon EKS subscription ID with the exception.
HTTP Status Code: 400

 ** InvalidParameterException **   
The specified parameter is invalid. Review the available parameters for the API request.    
 ** addonName **   
The specified parameter for the add-on name is invalid. Review the available parameters for the API request  
 ** clusterName **   
The Amazon EKS cluster associated with the exception.  
 ** fargateProfileName **   
The Fargate profile associated with the exception.  
 ** message **   
The specified parameter is invalid. Review the available parameters for the API request.  
 ** nodegroupName **   
The Amazon EKS managed node group associated with the exception.  
 ** subscriptionId **   
The Amazon EKS subscription ID with the exception.
HTTP Status Code: 400

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
<a name="API_ListAddons_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the *Amazon EKS General Reference*.

You need to learn how to sign HTTP requests only if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_ListAddons_Example_1"></a>

The following example lists the add-ons installed to a cluster.

#### Sample Request
<a name="API_ListAddons_Example_1_Request"></a>

```
GET /clusters/1-18/addons HTTP/1.1
Host: eks.us-west-2.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/1.16.298 Python/3.6.0 Windows/10 botocore/1.13.34
X-Amz-Date: 20201125T144629Z
Authorization: AUTHPARAMS
```

#### Sample Response
<a name="API_ListAddons_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Wed, 25 Nov 2020 14:46:30 GMT
Content-Type: application/json
Content-Length: 39
x-amzn-RequestId: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx
x-amz-apigw-id: WkYq8HCuvHcFU3Q=
X-Amzn-Trace-Id: Root=1-xxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxxx
Connection: keep-alive

{
	"addons": ["vpc-cni"],
	"nextToken": null
}
```

## See Also
<a name="API_ListAddons_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eks-2017-11-01/ListAddons) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eks-2017-11-01/ListAddons) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/ListAddons) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eks-2017-11-01/ListAddons) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/ListAddons) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eks-2017-11-01/ListAddons) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eks-2017-11-01/ListAddons) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eks-2017-11-01/ListAddons) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/eks-2017-11-01/ListAddons) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/ListAddons) 