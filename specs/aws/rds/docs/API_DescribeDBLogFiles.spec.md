---
id: "@specs/aws/rds/docs/API_DescribeDBLogFiles"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeDBLogFiles"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# DescribeDBLogFiles

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_DescribeDBLogFiles
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeDBLogFiles
<a name="API_DescribeDBLogFiles"></a>

Returns a list of DB log files for the DB instance.

This command doesn't apply to RDS Custom.

## Request Parameters
<a name="API_DescribeDBLogFiles_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBInstanceIdentifier **   
The customer-assigned name of the DB instance that contains the log files you want to list.  
Constraints:  
+ Must match the identifier of an existing DBInstance.
Type: String  
Required: Yes

 ** FileLastWritten **   
Filters the available log files for files written since the specified date, in POSIX timestamp format with milliseconds.  
Type: Long  
Required: No

 ** FilenameContains **   
Filters the available log files for log file names that contain the specified string.  
Type: String  
Required: No

 ** FileSize **   
Filters the available log files for files larger than the specified size.  
Type: Long  
Required: No

 **Filters.Filter.N**   
This parameter isn't currently supported.  
Type: Array of [Filter](API_Filter.md) objects  
Required: No

 ** Marker **   
The pagination token provided in the previous request. If this parameter is specified the response includes only records beyond the marker, up to MaxRecords.  
Type: String  
Required: No

 ** MaxRecords **   
The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so you can retrieve the remaining results.  
Type: Integer  
Required: No

## Response Elements
<a name="API_DescribeDBLogFiles_ResponseElements"></a>

The following elements are returned by the service.

 **DescribeDBLogFiles.DescribeDBLogFilesDetails.N**   
The DB log files returned.  
Type: Array of [DescribeDBLogFilesDetails](API_DescribeDBLogFilesDetails.md) objects

 ** Marker **   
A pagination token that can be used in a later `DescribeDBLogFiles` request.  
Type: String

## Errors
<a name="API_DescribeDBLogFiles_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBInstanceNotFound **   
 `DBInstanceIdentifier` doesn't refer to an existing DB instance.  
HTTP Status Code: 404

 ** DBInstanceNotReady **   
An attempt to download or examine log files didn't succeed because an Aurora Serverless v2 instance was paused.  
HTTP Status Code: 400

## Examples
<a name="API_DescribeDBLogFiles_Examples"></a>

### Example
<a name="API_DescribeDBLogFiles_Example_1"></a>

This example illustrates one usage of DescribeDBLogFiles.

#### Sample Request
<a name="API_DescribeDBLogFiles_Example_1_Request"></a>

```
https://rds.us-east-1.amazonaws.com/
   ?Action=DescribeDBLogFiles
   &DBInstanceIdentifier=mysqldb
   &MaxRecords=100
   &SignatureMethod=HmacSHA256
   &SignatureVersion=4 
   &Version=2014-10-31
   &X-Amz-Algorithm=AWS4-HMAC-SHA256
   &X-Amz-Credential=AKIADQKE4SARGYLE/20140421/us-east-1/rds/aws4_request
   &X-Amz-Date=20140421T225750Z
   &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
   &X-Amz-Signature=9020fd1bcd658614e058cd2eb8c58572cf6c11460b1e96380635ee428a52e8a1
```

#### Sample Response
<a name="API_DescribeDBLogFiles_Example_1_Response"></a>

```
<DescribeDBLogFilesResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/">
  <DescribeDBLogFilesResult>
    <DescribeDBLogFiles>
      <DescribeDBLogFilesDetails>
        <LastWritten>1398119101000</LastWritten>
        <LogFileName>error/mysql-error-running.log</LogFileName>
        <Size>1599</Size>
      </DescribeDBLogFilesDetails>
      <DescribeDBLogFilesDetails>
        <LastWritten>1398120900000</LastWritten>
        <LogFileName>error/mysql-error.log</LogFileName>
        <Size>0</Size>
      </DescribeDBLogFilesDetails>
    </DescribeDBLogFiles>
  </DescribeDBLogFilesResult>
  <ResponseMetadata>
    <RequestId>4c6ed648-b9f7-11d3-97bd-7999dd5a8f72</RequestId>
  </ResponseMetadata>
</DescribeDBLogFilesResponse>
```

## See Also
<a name="API_DescribeDBLogFiles_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/DescribeDBLogFiles) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/DescribeDBLogFiles) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DescribeDBLogFiles) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/DescribeDBLogFiles) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DescribeDBLogFiles) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/DescribeDBLogFiles) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/DescribeDBLogFiles) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/DescribeDBLogFiles) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/DescribeDBLogFiles) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DescribeDBLogFiles) 