---
id: "@specs/aws/rds/docs/API_DownloadDBLogFilePortion"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DownloadDBLogFilePortion"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# DownloadDBLogFilePortion

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_DownloadDBLogFilePortion
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DownloadDBLogFilePortion
<a name="API_DownloadDBLogFilePortion"></a>

Downloads all or a portion of the specified log file, up to 1 MB in size.

This command doesn't apply to RDS Custom.

**Note**  
This operation uses resources on database instances. Because of this, we recommend publishing database logs to CloudWatch and then using the GetLogEvents operation. For more information, see [GetLogEvents](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_GetLogEvents.html) in the *Amazon CloudWatch Logs API Reference*.

## Request Parameters
<a name="API_DownloadDBLogFilePortion_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBInstanceIdentifier **   
The customer-assigned name of the DB instance that contains the log files you want to list.  
Constraints:  
+ Must match the identifier of an existing DBInstance.
Type: String  
Required: Yes

 ** LogFileName **   
The name of the log file to be downloaded.  
Type: String  
Required: Yes

 ** Marker **   
The pagination token provided in the previous request or "0". If the Marker parameter is specified the response includes only records beyond the marker until the end of the file or up to NumberOfLines.  
Type: String  
Required: No

 ** NumberOfLines **   
The number of lines to download. If the number of lines specified results in a file over 1 MB in size, the file is truncated at 1 MB in size.  
If the NumberOfLines parameter is specified, then the block of lines returned can be from the beginning or the end of the log file, depending on the value of the Marker parameter.  
+ If neither Marker or NumberOfLines are specified, the entire log file is returned up to a maximum of 10000 lines, starting with the most recent log entries first.
+ If NumberOfLines is specified and Marker isn't specified, then the most recent lines from the end of the log file are returned.
+ If Marker is specified as "0", then the specified number of lines from the beginning of the log file are returned.
+ You can download the log file in blocks of lines by specifying the size of the block using the NumberOfLines parameter, and by specifying a value of "0" for the Marker parameter in your first request. Include the Marker value returned in the response as the Marker value for the next request, continuing until the AdditionalDataPending response element returns false.
Type: Integer  
Required: No

## Response Elements
<a name="API_DownloadDBLogFilePortion_ResponseElements"></a>

The following elements are returned by the service.

 ** AdditionalDataPending **   
A Boolean value that, if true, indicates there is more data to be downloaded.  
Type: Boolean

 ** LogFileData **   
Entries from the specified log file.  
Type: String

 ** Marker **   
A pagination token that can be used in a later `DownloadDBLogFilePortion` request.  
Type: String

## Errors
<a name="API_DownloadDBLogFilePortion_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBInstanceNotFound **   
 `DBInstanceIdentifier` doesn't refer to an existing DB instance.  
HTTP Status Code: 404

 ** DBInstanceNotReady **   
An attempt to download or examine log files didn't succeed because an Aurora Serverless v2 instance was paused.  
HTTP Status Code: 400

 ** DBLogFileNotFoundFault **   
 `LogFileName` doesn't refer to an existing DB log file.  
HTTP Status Code: 404

## Examples
<a name="API_DownloadDBLogFilePortion_Examples"></a>

### Example
<a name="API_DownloadDBLogFilePortion_Example_1"></a>

This example illustrates one usage of DownloadDBLogFilePortion.

#### Sample Request
<a name="API_DownloadDBLogFilePortion_Example_1_Request"></a>

```
https://rds.us-west-2.amazonaws.com/
  ?Action=DownloadDBLogFilePortion
  &DBInstanceIdentifier=myexampledb
  &LogFileName=log%2FERROR
  &Marker=0
  &NumberOfLines=50
  &Version=2014-10-31
  &X-Amz-Algorithm=AWS4-HMAC-SHA256
  &X-Amz-Credential=AKIADQKE4SARGYLE/20140127/us-west-2/rds/aws4_request
  &X-Amz-Date=20140127T235259Z
  &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
  &X-Amz-Signature=2171c5a8e91a70202e77de7e81df75787f3bbd6b4ea97f7a426205474fcc446f
```

#### Sample Response
<a name="API_DownloadDBLogFilePortion_Example_1_Response"></a>

```
<DownloadDBLogFilePortionResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/">
  <DownloadDBLogFilePortionResult>
    <Marker>0:4485</Marker>
    <LogFileData>??2014-01-26 23:59:00.01 spid54      Microsoft SQL Server 2012 - 11.0.2100.60 (X64) 
    
    Feb 10 2012 19:39:15 
    
    Copyright (c) Microsoft Corporation
    
    Web Edition (64-bit) on Windows NT 6.1 &lt;X64&gt; (Build 7601: Service Pack 1) (Hypervisor)
    
    
    
2014-01-26 23:59:00.01 spid54      (c) Microsoft Corporation.

2014-01-26 23:59:00.01 spid54      All rights reserved.

2014-01-26 23:59:00.01 spid54      Server process ID is 2976.

2014-01-26 23:59:00.01 spid54      System Manufacturer: 'Xen', System Model: 'HVM domU'.

2014-01-26 23:59:00.01 spid54      Authentication mode is MIXED.

2014-01-26 23:59:00.01 spid54      Logging SQL Server messages in file 'D:\RDSDBDATA\Log\ERROR'.

2014-01-26 23:59:00.01 spid54      The service account is 'WORKGROUP\AMAZONA-NUQUUMV$'. This is an informational message; no user action is required.

2014-01-26 23:59:00.01 spid54      The error log has been reinitialized. See the previous log for older entries.

2014-01-27 00:00:56.42 spid25s     This instance of SQL Server has been using a process ID of 2976 since 10/21/2013 2:16:50 AM (local) 10/21/2013 2:16:50 AM (UTC). This is an informational message only; no user action is required.

2014-01-27 09:35:15.43 spid71      I/O is frozen on database model. No user action is required. However, if I/O is not resumed promptly, you could cancel the backup.

2014-01-27 09:35:15.44 spid72      I/O is frozen on database msdb. No user action is required. However, if I/O is not resumed promptly, you could cancel the backup.

2014-01-27 09:35:15.44 spid74      I/O is frozen on database rdsadmin. No user action is required. However, if I/O is not resumed promptly, you could cancel the backup.

2014-01-27 09:35:15.44 spid73      I/O is frozen on database master. No user action is required. However, if I/O is not resumed promptly, you could cancel the backup.

2014-01-27 09:35:25.57 spid73      I/O was resumed on database master. No user action is required.

2014-01-27 09:35:25.57 spid74      I/O was resumed on database rdsadmin. No user action is required.

2014-01-27 09:35:25.57 spid71      I/O was resumed on database model. No user action is required.

2014-01-27 09:35:25.57 spid72      I/O was resumed on database msdb. No user action is required.


</LogFileData>
    <AdditionalDataPending>false</AdditionalDataPending>
  </DownloadDBLogFilePortionResult>
  <ResponseMetadata>
    <RequestId>27143425-87ae-11e3-acc9-fb64b157268e</RequestId>
  </ResponseMetadata>
</DownloadDBLogFilePortionResponse>
```

## See Also
<a name="API_DownloadDBLogFilePortion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/DownloadDBLogFilePortion) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/DownloadDBLogFilePortion) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DownloadDBLogFilePortion) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/DownloadDBLogFilePortion) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DownloadDBLogFilePortion) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/DownloadDBLogFilePortion) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/DownloadDBLogFilePortion) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/DownloadDBLogFilePortion) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/DownloadDBLogFilePortion) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DownloadDBLogFilePortion) 