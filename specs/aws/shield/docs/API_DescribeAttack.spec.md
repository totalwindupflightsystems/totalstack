---
id: "@specs/aws/shield/docs/API_DescribeAttack"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeAttack"
status: active
depends_on:
  - "@specs/aws/shield/meta"
---

# DescribeAttack

> **source:** AWS Documentation
> **spec:id:** @specs/aws/shield/docs/API_DescribeAttack
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeAttack
<a name="API_DescribeAttack"></a>

Describes the details of a DDoS attack. 

## Request Syntax
<a name="API_DescribeAttack_RequestSyntax"></a>

```
{
   "AttackId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeAttack_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AttackId](#API_DescribeAttack_RequestSyntax) **   <a name="AWSShield-DescribeAttack-request-AttackId"></a>
The unique identifier (ID) for the attack.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[a-zA-Z0-9\\-]*`   
Required: Yes

## Response Syntax
<a name="API_DescribeAttack_ResponseSyntax"></a>

```
{
   "Attack": { 
      "AttackCounters": [ 
         { 
            "Average": number,
            "Max": number,
            "N": number,
            "Name": "string",
            "Sum": number,
            "Unit": "string"
         }
      ],
      "AttackId": "string",
      "AttackProperties": [ 
         { 
            "AttackLayer": "string",
            "AttackPropertyIdentifier": "string",
            "TopContributors": [ 
               { 
                  "Name": "string",
                  "Value": number
               }
            ],
            "Total": number,
            "Unit": "string"
         }
      ],
      "EndTime": number,
      "Mitigations": [ 
         { 
            "MitigationName": "string"
         }
      ],
      "ResourceArn": "string",
      "StartTime": number,
      "SubResources": [ 
         { 
            "AttackVectors": [ 
               { 
                  "VectorCounters": [ 
                     { 
                        "Average": number,
                        "Max": number,
                        "N": number,
                        "Name": "string",
                        "Sum": number,
                        "Unit": "string"
                     }
                  ],
                  "VectorType": "string"
               }
            ],
            "Counters": [ 
               { 
                  "Average": number,
                  "Max": number,
                  "N": number,
                  "Name": "string",
                  "Sum": number,
                  "Unit": "string"
               }
            ],
            "Id": "string",
            "Type": "string"
         }
      ]
   }
}
```

## Response Elements
<a name="API_DescribeAttack_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Attack](#API_DescribeAttack_ResponseSyntax) **   <a name="AWSShield-DescribeAttack-response-Attack"></a>
The attack that you requested.   
Type: [AttackDetail](API_AttackDetail.md) object

## Errors
<a name="API_DescribeAttack_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
Exception that indicates the specified `AttackId` does not exist, or the requester does not have the appropriate permissions to access the `AttackId`.  
HTTP Status Code: 400

 ** InternalErrorException **   
Exception that indicates that a problem occurred with the service infrastructure. You can retry the request.  
HTTP Status Code: 500

## See Also
<a name="API_DescribeAttack_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/shield-2016-06-02/DescribeAttack) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/shield-2016-06-02/DescribeAttack) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/shield-2016-06-02/DescribeAttack) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/shield-2016-06-02/DescribeAttack) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/shield-2016-06-02/DescribeAttack) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/shield-2016-06-02/DescribeAttack) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/shield-2016-06-02/DescribeAttack) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/shield-2016-06-02/DescribeAttack) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/shield-2016-06-02/DescribeAttack) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/shield-2016-06-02/DescribeAttack) 