---
id: "@specs/aws/cloudfront/docs/API_GetInvalidation"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetInvalidation"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# GetInvalidation

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_GetInvalidation
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetInvalidation
<a name="API_GetInvalidation"></a>

Get the information about an invalidation.

## Request Syntax
<a name="API_GetInvalidation_RequestSyntax"></a>

```
GET /2020-05-31/distribution/{{DistributionId}}/invalidation/{{Id}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetInvalidation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DistributionId](#API_GetInvalidation_RequestSyntax) **   <a name="cloudfront-GetInvalidation-request-uri-DistributionId"></a>
The distribution's ID.  
Required: Yes

 ** [Id](#API_GetInvalidation_RequestSyntax) **   <a name="cloudfront-GetInvalidation-request-uri-Id"></a>
The identifier for the invalidation request, for example, `IDFDVBD632BHDS5`.  
Required: Yes

## Request Body
<a name="API_GetInvalidation_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetInvalidation_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<Invalidation>
   <CreateTime>timestamp</CreateTime>
   <Id>string</Id>
   <InvalidationBatch>
      <CallerReference>string</CallerReference>
      <Paths>
         <Items>
            <Path>string</Path>
         </Items>
         <Quantity>integer</Quantity>
      </Paths>
   </InvalidationBatch>
   <Status>string</Status>
</Invalidation>
```

## Response Elements
<a name="API_GetInvalidation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [Invalidation](#API_GetInvalidation_ResponseSyntax) **   <a name="cloudfront-GetInvalidation-response-Invalidation"></a>
Root level tag for the Invalidation parameters.  
Required: Yes

 ** [CreateTime](#API_GetInvalidation_ResponseSyntax) **   <a name="cloudfront-GetInvalidation-response-CreateTime"></a>
The date and time the invalidation request was first made.  
Type: Timestamp

 ** [Id](#API_GetInvalidation_ResponseSyntax) **   <a name="cloudfront-GetInvalidation-response-Id"></a>
The identifier for the invalidation request. For example: `IDFDVBD632BHDS5`.  
Type: String

 ** [InvalidationBatch](#API_GetInvalidation_ResponseSyntax) **   <a name="cloudfront-GetInvalidation-response-InvalidationBatch"></a>
The current invalidation information for the batch request.  
Type: [InvalidationBatch](API_InvalidationBatch.md) object

 ** [Status](#API_GetInvalidation_ResponseSyntax) **   <a name="cloudfront-GetInvalidation-response-Status"></a>
The status of the invalidation request. When the invalidation batch is finished, the status is `Completed`.  
Type: String

## Errors
<a name="API_GetInvalidation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDenied **   
Access denied.  
HTTP Status Code: 403

 ** NoSuchDistribution **   
The specified distribution does not exist.  
HTTP Status Code: 404

 ** NoSuchInvalidation **   
The specified invalidation does not exist.  
HTTP Status Code: 404

## See Also
<a name="API_GetInvalidation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/GetInvalidation) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudfront-2020-05-31/GetInvalidation) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/GetInvalidation) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/GetInvalidation) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/GetInvalidation) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/GetInvalidation) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/GetInvalidation) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/GetInvalidation) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/GetInvalidation) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/GetInvalidation) 