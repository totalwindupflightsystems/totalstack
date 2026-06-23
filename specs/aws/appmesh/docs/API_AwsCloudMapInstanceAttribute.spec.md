---
id: "@specs/aws/appmesh/docs/API_AwsCloudMapInstanceAttribute"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AwsCloudMapInstanceAttribute"
status: active
depends_on:
  - "@specs/aws/appmesh/meta"
---

# AwsCloudMapInstanceAttribute

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appmesh/docs/API_AwsCloudMapInstanceAttribute
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AwsCloudMapInstanceAttribute
<a name="API_AwsCloudMapInstanceAttribute"></a>

An object that represents the AWS Cloud Map attribute information for your virtual node.

**Note**  
 AWS Cloud Map is not available in the eu-south-1 Region.

## Contents
<a name="API_AwsCloudMapInstanceAttribute_Contents"></a>

 ** key **   <a name="appmesh-Type-AwsCloudMapInstanceAttribute-key"></a>
The name of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map service instance that contains the specified key and value is returned.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[a-zA-Z0-9!-~]+`   
Required: Yes

 ** value **   <a name="appmesh-Type-AwsCloudMapInstanceAttribute-value"></a>
The value of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map service instance that contains the specified key and value is returned.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `([a-zA-Z0-9!-~][ a-zA-Z0-9!-~]*){0,1}[a-zA-Z0-9!-~]{0,1}`   
Required: Yes

## See Also
<a name="API_AwsCloudMapInstanceAttribute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/AwsCloudMapInstanceAttribute) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/AwsCloudMapInstanceAttribute) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/AwsCloudMapInstanceAttribute) 