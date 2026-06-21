---
id: "@specs/aws/rds/docs/API_DescribePendingMaintenanceActions"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribePendingMaintenanceActions"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# DescribePendingMaintenanceActions

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_DescribePendingMaintenanceActions
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribePendingMaintenanceActions
<a name="API_DescribePendingMaintenanceActions"></a>

Returns a list of resources (for example, DB instances) that have at least one pending maintenance action.

This API follows an eventual consistency model. This means that the result of the `DescribePendingMaintenanceActions` command might not be immediately visible to all subsequent RDS commands. Keep this in mind when you use `DescribePendingMaintenanceActions` immediately after using a previous API command such as `ApplyPendingMaintenanceActions`.

## Request Parameters
<a name="API_DescribePendingMaintenanceActions_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **Filters.Filter.N**   
A filter that specifies one or more resources to return pending maintenance actions for.  
Supported filters:  
+  `db-cluster-id` - Accepts DB cluster identifiers and DB cluster Amazon Resource Names (ARNs). The results list only includes pending maintenance actions for the DB clusters identified by these ARNs.
+  `db-instance-id` - Accepts DB instance identifiers and DB instance ARNs. The results list only includes pending maintenance actions for the DB instances identified by these ARNs.
Type: Array of [Filter](API_Filter.md) objects  
Required: No

 ** Marker **   
An optional pagination token provided by a previous `DescribePendingMaintenanceActions` request. If this parameter is specified, the response includes only records beyond the marker, up to a number of records specified by `MaxRecords`.  
Type: String  
Required: No

 ** MaxRecords **   
The maximum number of records to include in the response. If more records exist than the specified `MaxRecords` value, a pagination token called a marker is included in the response so that you can retrieve the remaining results.  
Default: 100  
Constraints: Minimum 20, maximum 100.  
Type: Integer  
Required: No

 ** ResourceIdentifier **   
The ARN of a resource to return pending maintenance actions for.  
Type: String  
Required: No

## Response Elements
<a name="API_DescribePendingMaintenanceActions_ResponseElements"></a>

The following elements are returned by the service.

 ** Marker **   
An optional pagination token provided by a previous `DescribePendingMaintenanceActions` request. If this parameter is specified, the response includes only records beyond the marker, up to a number of records specified by `MaxRecords`.  
Type: String

 **PendingMaintenanceActions.ResourcePendingMaintenanceActions.N**   
A list of the pending maintenance actions for the resource.  
Type: Array of [ResourcePendingMaintenanceActions](API_ResourcePendingMaintenanceActions.md) objects

## Errors
<a name="API_DescribePendingMaintenanceActions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundFault **   
The specified resource ID was not found.  
HTTP Status Code: 404

## Examples
<a name="API_DescribePendingMaintenanceActions_Examples"></a>

### Example
<a name="API_DescribePendingMaintenanceActions_Example_1"></a>

This example illustrates one usage of DescribePendingMaintenanceActions.

#### Sample Request
<a name="API_DescribePendingMaintenanceActions_Example_1_Request"></a>

```
https://rds.us-west-2.amazonaws.com/
   ?Action=DescribePendingMaintenanceActions
   &SignatureMethod=HmacSHA256
   &SignatureVersion=4
   &Version=2014-10-31
   &X-Amz-Algorithm=AWS4-HMAC-SHA256
   &X-Amz-Credential=AKIADQKE4SARGYLE/20141216/us-west-2/rds/aws4_request
   &X-Amz-Date=20140421T194732Z
   &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
   &X-Amz-Signature=6e25c542bf96fe24b28c12976ec92d2f856ab1d2a158e21c35441a736e4fde2b
```

#### Sample Response
<a name="API_DescribePendingMaintenanceActions_Example_1_Response"></a>

```
<DescribePendingMaintenanceActionsResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/">
  <DescribePendingMaintenanceActionsResult>
    <PendingMaintenanceActions>
      <ResourcePendingMaintenanceActions>
        <ResourceIdentifier>arn:aws:rds:us-east-1:123456781234:db:my-instance</ResourceIdentifier>
        <PendingMaintenanceActionDetails>
          <PendingMaintenanceAction>
            <Action>system-update</Action>
          </PendingMaintenanceAction>
        </PendingMaintenanceActionDetails>
      </ResourcePendingMaintenanceActions>
      <ResourcePendingMaintenanceActions>
        <ResourceIdentifier>arn:aws:rds:us-east-1:123456781234:db:another-instance</ResourceIdentifier>
        <PendingMaintenanceActionDetails>
          <PendingMaintenanceAction>
            <Action>system-update</Action>
          </PendingMaintenanceAction>
        </PendingMaintenanceActionDetails>
      </ResourcePendingMaintenanceActions>
    </PendingMaintenanceActions>
  </DescribePendingMaintenanceActionsResult>
  <ResponseMetadata>
    <RequestId>dcfe0682-870c-11e4-9833-b3ad657ea9da</RequestId>
  </ResponseMetadata>
</DescribePendingMaintenanceActionsResponse>
```

## See Also
<a name="API_DescribePendingMaintenanceActions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/DescribePendingMaintenanceActions) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/DescribePendingMaintenanceActions) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DescribePendingMaintenanceActions) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/DescribePendingMaintenanceActions) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DescribePendingMaintenanceActions) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/DescribePendingMaintenanceActions) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/DescribePendingMaintenanceActions) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/DescribePendingMaintenanceActions) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/DescribePendingMaintenanceActions) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DescribePendingMaintenanceActions) 