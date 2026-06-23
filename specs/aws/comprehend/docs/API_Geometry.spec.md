---
id: "@specs/aws/comprehend/docs/API_Geometry"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Geometry"
status: active
depends_on:
  - "@specs/aws/comprehend/meta"
---

# Geometry

> **source:** AWS Documentation
> **spec:id:** @specs/aws/comprehend/docs/API_Geometry
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Geometry
<a name="API_Geometry"></a>

Information about the location of items on a document page.

For additional information, see [Geometry](https://docs.aws.amazon.com/textract/latest/dg/API_Geometry.html) in the Amazon Textract API reference.

## Contents
<a name="API_Geometry_Contents"></a>

 ** BoundingBox **   <a name="comprehend-Type-Geometry-BoundingBox"></a>
An axis-aligned coarse representation of the location of the recognized item on the document page.  
Type: [BoundingBox](API_BoundingBox.md) object  
Required: No

 ** Polygon **   <a name="comprehend-Type-Geometry-Polygon"></a>
Within the bounding box, a fine-grained polygon around the recognized item.  
Type: Array of [Point](API_Point.md) objects  
Required: No

## See Also
<a name="API_Geometry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehend-2017-11-27/Geometry) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehend-2017-11-27/Geometry) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehend-2017-11-27/Geometry) 