---
id: "@specs/aws/rds/docs/API_ApplyPendingMaintenanceAction"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ApplyPendingMaintenanceAction"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# ApplyPendingMaintenanceAction

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_ApplyPendingMaintenanceAction
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ApplyPendingMaintenanceAction
<a name="API_ApplyPendingMaintenanceAction"></a>

Applies a pending maintenance action to a resource (for example, to a DB instance).

## Request Parameters
<a name="API_ApplyPendingMaintenanceAction_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ApplyAction **   
The pending maintenance action to apply to this resource.  
Valid Values:  
+  `ca-certificate-rotation` 
+  `db-upgrade` 
+  `hardware-maintenance` 
+  `os-upgrade` 
+  `system-update` 
For more information about these actions, see [Maintenance actions for Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.html#maintenance-actions-aurora) or [Maintenance actions for Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Maintenance.html#maintenance-actions-rds).  
Type: String  
Required: Yes

 ** OptInType **   
A value that specifies the type of opt-in request, or undoes an opt-in request. An opt-in request of type `immediate` can't be undone.  
Valid Values:  
+  `immediate` - Apply the maintenance action immediately.
+  `next-maintenance` - Apply the maintenance action during the next maintenance window for the resource.
+  `undo-opt-in` - Cancel any existing `next-maintenance` opt-in requests.
Type: String  
Required: Yes

 ** ResourceIdentifier **   
The RDS Amazon Resource Name (ARN) of the resource that the pending maintenance action applies to. For information about creating an ARN, see [ Constructing an RDS Amazon Resource Name (ARN)](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.ARN.html#USER_Tagging.ARN.Constructing).  
Type: String  
Required: Yes

## Response Elements
<a name="API_ApplyPendingMaintenanceAction_ResponseElements"></a>

The following element is returned by the service.

 ** ResourcePendingMaintenanceActions **   
Describes the pending maintenance actions for a resource.  
Type: [ResourcePendingMaintenanceActions](API_ResourcePendingMaintenanceActions.md) object

## Errors
<a name="API_ApplyPendingMaintenanceAction_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidDBClusterStateFault **   
The requested operation can't be performed while the cluster is in this state.  
HTTP Status Code: 400

 ** InvalidDBInstanceState **   
The DB instance isn't in a valid state.  
HTTP Status Code: 400

 ** ResourceNotFoundFault **   
The specified resource ID was not found.  
HTTP Status Code: 404

## Examples
<a name="API_ApplyPendingMaintenanceAction_Examples"></a>

### Example
<a name="API_ApplyPendingMaintenanceAction_Example_1"></a>

This example illustrates one usage of ApplyPendingMaintenanceAction.

#### Sample Request
<a name="API_ApplyPendingMaintenanceAction_Example_1_Request"></a>

```
https://rds.us-west-2.amazonaws.com/
   ?Action=ApplyPendingMaintenanceAction
   &ResourceIdentifier=arn:aws:rds:us-east-1:123456781234:db:my-instance
   &ApplyAction=system-update
   &OptInType=immediate
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
<a name="API_ApplyPendingMaintenanceAction_Example_1_Response"></a>

```
<ApplyPendingMaintenanceActionResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/">
  <ApplyPendingMaintenanceActionResult>
     <ResourcePendingMaintenanceActions>
      <ResourceIdentifier>arn:aws:rds:us-east-1:123456781234:db:my-instance</ResourceIdentifier>
      <PendingMaintenanceActionDetails>
        <PendingMaintenanceAction>
          <Action>system-update</Action>
          <OptInStatus>immediate</OptInStatus>
        </PendingMaintenanceAction>
      </PendingMaintenanceActionDetails>
     /ResourcePendingMaintenanceActions>
  </ApplyPendingMaintenanceActionResult>
  <ResponseMetadata>
    <RequestId>dcfe0682-870c-11e4-9833-b3ad657ea9da</RequestId>
  </ResponseMetadata>
</ApplyPendingMaintenanceActionResponse>
```

## See Also
<a name="API_ApplyPendingMaintenanceAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/ApplyPendingMaintenanceAction) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/ApplyPendingMaintenanceAction) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/ApplyPendingMaintenanceAction) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/ApplyPendingMaintenanceAction) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/ApplyPendingMaintenanceAction) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/ApplyPendingMaintenanceAction) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/ApplyPendingMaintenanceAction) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/ApplyPendingMaintenanceAction) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/ApplyPendingMaintenanceAction) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/ApplyPendingMaintenanceAction) 