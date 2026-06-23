---
id: "@specs/aws/appmesh/docs/API_HttpRouteHeader"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS HttpRouteHeader"
status: active
depends_on:
  - "@specs/aws/appmesh/meta"
---

# HttpRouteHeader

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appmesh/docs/API_HttpRouteHeader
> **target_lang:** meta — documentation tier. ALL sections preserved.



# HttpRouteHeader
<a name="API_HttpRouteHeader"></a>

An object that represents the HTTP header in the request.

## Contents
<a name="API_HttpRouteHeader_Contents"></a>

 ** name **   <a name="appmesh-Type-HttpRouteHeader-name"></a>
A name for the HTTP header in the client request that will be matched on.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 50.  
Required: Yes

 ** invert **   <a name="appmesh-Type-HttpRouteHeader-invert"></a>
Specify `True` to match anything except the match criteria. The default value is `False`.  
Type: Boolean  
Required: No

 ** match **   <a name="appmesh-Type-HttpRouteHeader-match"></a>
The `HeaderMatchMethod` object.  
Type: [HeaderMatchMethod](API_HeaderMatchMethod.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

## See Also
<a name="API_HttpRouteHeader_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/HttpRouteHeader) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/HttpRouteHeader) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/HttpRouteHeader) 