---
id: "@specs/aws/globalaccelerator/docs/API_ListAccelerators"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListAccelerators"
status: active
depends_on:
  - "@specs/aws/globalaccelerator/meta"
---

# ListAccelerators

> **source:** AWS Documentation
> **spec:id:** @specs/aws/globalaccelerator/docs/API_ListAccelerators
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListAccelerators
<a name="API_ListAccelerators"></a>

List the accelerators for an AWS account. 

## Request Syntax
<a name="API_ListAccelerators_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListAccelerators_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListAccelerators_RequestSyntax) **   <a name="globalaccelerator-ListAccelerators-request-MaxResults"></a>
The number of Global Accelerator objects that you want to return with this call. The default value is 10.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 100.  
Required: No

 ** [NextToken](#API_ListAccelerators_RequestSyntax) **   <a name="globalaccelerator-ListAccelerators-request-NextToken"></a>
The token for the next set of results. You receive this token from a previous call.  
Type: String  
Length Constraints: Maximum length of 255.  
Required: No

## Response Syntax
<a name="API_ListAccelerators_ResponseSyntax"></a>

```
{
   "Accelerators": [ 
      { 
         "AcceleratorArn": "string",
         "CreatedTime": number,
         "DnsName": "string",
         "DualStackDnsName": "string",
         "Enabled": boolean,
         "Events": [ 
            { 
               "Message": "string",
               "Timestamp": number
            }
         ],
         "IpAddressType": "string",
         "IpSets": [ 
            { 
               "IpAddresses": [ "string" ],
               "IpAddressFamily": "string",
               "IpFamily": "string"
            }
         ],
         "LastModifiedTime": number,
         "Name": "string",
         "Status": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListAccelerators_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Accelerators](#API_ListAccelerators_ResponseSyntax) **   <a name="globalaccelerator-ListAccelerators-response-Accelerators"></a>
The list of accelerators for a customer account.  
Type: Array of [Accelerator](API_Accelerator.md) objects

 ** [NextToken](#API_ListAccelerators_ResponseSyntax) **   <a name="globalaccelerator-ListAccelerators-response-NextToken"></a>
The token for the next set of results. You receive this token from a previous call.  
Type: String  
Length Constraints: Maximum length of 255.

## Errors
<a name="API_ListAccelerators_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceErrorException **   
There was an internal error for AWS Global Accelerator.  
HTTP Status Code: 400

 ** InvalidArgumentException **   
An argument that you specified is invalid.  
HTTP Status Code: 400

 ** InvalidNextTokenException **   
There isn't another item to return.  
HTTP Status Code: 400

## Examples
<a name="API_ListAccelerators_Examples"></a>

### List accelerators
<a name="API_ListAccelerators_Example_1"></a>

The following is an example for listing the accelerators for an AWS account, and the response.

```
aws globalaccelerator list-accelerators --region us-west-2
```

```
{
"Accelerators": [
        {
            "AcceleratorArn": "arn:aws:globalaccelerator::012345678901:accelerator/5555abcd-abcd-5555-abcd-5555EXAMPLE1",
            "Name": "TestAccelerator",
            "IpAddressType": "IPV4",
            "Enabled": true,
            "IpSets": [
                {
                    "IpFamily": "IPv4",
                    "IpAddresses": [
                        "192.0.2.250",
                        "198.51.100.52"
                    ]
                }
            ],
            "DnsName": "5a5a5a5a5a5a5a5a.awsglobalaccelerator.com",
            "Status": "DEPLOYED",
            "CreatedTime": 1552424416.0,
            "LastModifiedTime": 1569375641.0
        },
        {
            "AcceleratorArn": "arn:aws:globalaccelerator::888888888888:accelerator/8888abcd-abcd-8888-abcd-8888EXAMPLE2",
            "Name": "ExampleAccelerator",
            "IpAddressType": "IPV4",
            "Enabled": true,
            "IpSets": [
                {
                    "IpFamily": "IPv4",
                    "IpAddresses": [
                        "192.0.2.100",
                        "198.51.100.10"
                    ]
                }
            ],
            "DnsName": "6a6a6a6a6a6a6a.awsglobalaccelerator.com",
            "Status": "DEPLOYED",
            "CreatedTime": 1575585564.0,
            "LastModifiedTime": 1579809243.0
        },
    ]
}
```

## See Also
<a name="API_ListAccelerators_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/globalaccelerator-2018-08-08/ListAccelerators) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/globalaccelerator-2018-08-08/ListAccelerators) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/globalaccelerator-2018-08-08/ListAccelerators) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/globalaccelerator-2018-08-08/ListAccelerators) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/globalaccelerator-2018-08-08/ListAccelerators) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/globalaccelerator-2018-08-08/ListAccelerators) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/globalaccelerator-2018-08-08/ListAccelerators) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/globalaccelerator-2018-08-08/ListAccelerators) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/globalaccelerator-2018-08-08/ListAccelerators) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/globalaccelerator-2018-08-08/ListAccelerators) 