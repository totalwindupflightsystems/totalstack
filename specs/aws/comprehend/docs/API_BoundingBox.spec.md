---
id: "@specs/aws/comprehend/docs/API_BoundingBox"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS BoundingBox"
status: active
depends_on:
  - "@specs/aws/comprehend/meta"
---

# BoundingBox

> **source:** AWS Documentation
> **spec:id:** @specs/aws/comprehend/docs/API_BoundingBox
> **target_lang:** meta — documentation tier. ALL sections preserved.



# BoundingBox
<a name="API_BoundingBox"></a>

The bounding box around the detected page or around an element on a document page. The left (x-coordinate) and top (y-coordinate) are coordinates that represent the top and left sides of the bounding box. Note that the upper-left corner of the image is the origin (0,0). 

For additional information, see [BoundingBox](https://docs.aws.amazon.com/textract/latest/dg/API_BoundingBox.html) in the Amazon Textract API reference.

## Contents
<a name="API_BoundingBox_Contents"></a>

 ** Height **   <a name="comprehend-Type-BoundingBox-Height"></a>
The height of the bounding box as a ratio of the overall document page height.  
Type: Float  
Required: No

 ** Left **   <a name="comprehend-Type-BoundingBox-Left"></a>
The left coordinate of the bounding box as a ratio of overall document page width.  
Type: Float  
Required: No

 ** Top **   <a name="comprehend-Type-BoundingBox-Top"></a>
The top coordinate of the bounding box as a ratio of overall document page height.  
Type: Float  
Required: No

 ** Width **   <a name="comprehend-Type-BoundingBox-Width"></a>
The width of the bounding box as a ratio of the overall document page width.  
Type: Float  
Required: No

## See Also
<a name="API_BoundingBox_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehend-2017-11-27/BoundingBox) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehend-2017-11-27/BoundingBox) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehend-2017-11-27/BoundingBox) 