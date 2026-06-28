---
id: "@specs/aws/globalaccelerator/docs/API_ByoipCidr"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ByoipCidr"
status: active
depends_on:
  - "@specs/aws/globalaccelerator/meta"
---

# ByoipCidr

> **source:** AWS Documentation
> **spec:id:** @specs/aws/globalaccelerator/docs/API_ByoipCidr
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ByoipCidr
<a name="API_ByoipCidr"></a>

Information about an IP address range that is provisioned for use with your AWS resources through bring your own IP address (BYOIP).

The following describes each BYOIP `State` that your IP address range can be in.
+  **PENDING\_PROVISIONING** — You’ve submitted a request to provision an IP address range but it is not yet provisioned with AWS Global Accelerator.
+  **READY** — The address range is provisioned with AWS Global Accelerator and can be advertised.
+  **PENDING\_ADVERTISING** — You’ve submitted a request for AWS Global Accelerator to advertise an address range but it is not yet being advertised.
+  **ADVERTISING** — The address range is being advertised by AWS Global Accelerator.
+  **PENDING\_WITHDRAWING** — You’ve submitted a request to withdraw an address range from being advertised but it is still being advertised by AWS Global Accelerator.
+  **PENDING\_DEPROVISIONING** — You’ve submitted a request to deprovision an address range from AWS Global Accelerator but it is still provisioned.
+  **DEPROVISIONED** — The address range is deprovisioned from AWS Global Accelerator.
+  **FAILED\_PROVISION ** — The request to provision the address range from AWS Global Accelerator was not successful. Please make sure that you provide all of the correct information, and try again. If the request fails a second time, contact AWS support.
+  **FAILED\_ADVERTISING** — The request for AWS Global Accelerator to advertise the address range was not successful. Please make sure that you provide all of the correct information, and try again. If the request fails a second time, contact AWS support.
+  **FAILED\_WITHDRAW** — The request to withdraw the address range from advertising by AWS Global Accelerator was not successful. Please make sure that you provide all of the correct information, and try again. If the request fails a second time, contact AWS support.
+  **FAILED\_DEPROVISION ** — The request to deprovision the address range from AWS Global Accelerator was not successful. Please make sure that you provide all of the correct information, and try again. If the request fails a second time, contact AWS support.

## Contents
<a name="API_ByoipCidr_Contents"></a>

 ** Cidr **   <a name="globalaccelerator-Type-ByoipCidr-Cidr"></a>
The address range, in CIDR notation.  
 For more information, see [Bring your own IP addresses (BYOIP)](https://docs.aws.amazon.com/global-accelerator/latest/dg/using-byoip.html) in the AWS Global Accelerator Developer Guide.  
Type: String  
Length Constraints: Maximum length of 255.  
Required: No

 ** Events **   <a name="globalaccelerator-Type-ByoipCidr-Events"></a>
A history of status changes for an IP address range that you bring to AWS Global Accelerator through bring your own IP address (BYOIP).  
Type: Array of [ByoipCidrEvent](API_ByoipCidrEvent.md) objects  
Required: No

 ** State **   <a name="globalaccelerator-Type-ByoipCidr-State"></a>
The state of the address pool.  
Type: String  
Valid Values: `PENDING_PROVISIONING | READY | PENDING_ADVERTISING | ADVERTISING | PENDING_WITHDRAWING | PENDING_DEPROVISIONING | DEPROVISIONED | FAILED_PROVISION | FAILED_ADVERTISING | FAILED_WITHDRAW | FAILED_DEPROVISION`   
Required: No

## See Also
<a name="API_ByoipCidr_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/globalaccelerator-2018-08-08/ByoipCidr) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/globalaccelerator-2018-08-08/ByoipCidr) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/globalaccelerator-2018-08-08/ByoipCidr) 