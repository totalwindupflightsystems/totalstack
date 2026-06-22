---
id: "@specs/aws/batch/docs/API_FairsharePolicy"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS FairsharePolicy"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# FairsharePolicy

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_FairsharePolicy
> **target_lang:** meta — documentation tier. ALL sections preserved.



# FairsharePolicy
<a name="API_FairsharePolicy"></a>

The fair-share scheduling policy details.

## Contents
<a name="API_FairsharePolicy_Contents"></a>

 ** computeReservation **   <a name="Batch-Type-FairsharePolicy-computeReservation"></a>
A value used to reserve some of the available maximum vCPU for share identifiers that aren't already used.  
The reserved ratio is `(computeReservation/100)^ActiveFairShares ` where ` ActiveFairShares ` is the number of active share identifiers.  
For example, a `computeReservation` value of 50 indicates that AWS Batch reserves 50% of the maximum available vCPU if there's only one share identifier. It reserves 25% if there are two share identifiers. It reserves 12.5% if there are three share identifiers. A `computeReservation` value of 25 indicates that AWS Batch should reserve 25% of the maximum available vCPU if there's only one share identifier, 6.25% if there are two fair share identifiers, and 1.56% if there are three share identifiers.  
The minimum value is 0 and the maximum value is 99.  
Type: Integer  
Required: No

 ** shareDecaySeconds **   <a name="Batch-Type-FairsharePolicy-shareDecaySeconds"></a>
The amount of time (in seconds) to use to calculate a fair-share percentage for each share identifier in use. A value of zero (0) indicates the default minimum time window (600 seconds). The maximum supported value is 604800 (1 week).  
The decay allows for more recently run jobs to have more weight than jobs that ran earlier. Consider adjusting this number if you have jobs that (on average) run longer than ten minutes, or a large difference in job count or job run times between share identifiers, and the allocation of resources doesn't meet your needs.  
Type: Integer  
Required: No

 ** shareDistribution **   <a name="Batch-Type-FairsharePolicy-shareDistribution"></a>
An array of `SharedIdentifier` objects that contain the weights for the share identifiers for the fair-share policy. Share identifiers that aren't included have a default weight of `1.0`.  
Type: Array of [ShareAttributes](API_ShareAttributes.md) objects  
Required: No

## See Also
<a name="API_FairsharePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/FairsharePolicy) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/FairsharePolicy) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/FairsharePolicy) 