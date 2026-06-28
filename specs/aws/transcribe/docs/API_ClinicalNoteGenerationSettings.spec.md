---
id: "@specs/aws/transcribe/docs/API_ClinicalNoteGenerationSettings"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ClinicalNoteGenerationSettings"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# ClinicalNoteGenerationSettings

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_ClinicalNoteGenerationSettings
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ClinicalNoteGenerationSettings
<a name="API_ClinicalNoteGenerationSettings"></a>

The output configuration for clinical note generation.

## Contents
<a name="API_ClinicalNoteGenerationSettings_Contents"></a>

 ** NoteTemplate **   <a name="transcribe-Type-ClinicalNoteGenerationSettings-NoteTemplate"></a>
Specify one of the following templates to use for the clinical note summary. The default is `HISTORY_AND_PHYSICAL`.  
+ HISTORY\_AND\_PHYSICAL: Provides summaries for key sections of the clinical documentation. Examples of sections include Chief Complaint, History of Present Illness, Review of Systems, Past Medical History, Assessment, and Plan. 
+ GIRPP: Provides summaries based on the patients progress toward goals. Examples of sections include Goal, Intervention, Response, Progress, and Plan.
+ BIRP: Focuses on the patient's behavioral patterns and responses. Examples of sections include Behavior, Intervention, Response, and Plan.
+ SIRP: Emphasizes the situational context of therapy. Examples of sections include Situation, Intervention, Response, and Plan.
+ DAP: Provides a simplified format for clinical documentation. Examples of sections include Data, Assessment, and Plan.
+ BEHAVIORAL\_SOAP: Behavioral health focused documentation format. Examples of sections include Subjective, Objective, Assessment, and Plan.
+ PHYSICAL\_SOAP: Physical health focused documentation format. Examples of sections include Subjective, Objective, Assessment, and Plan.
Type: String  
Valid Values: `HISTORY_AND_PHYSICAL | GIRPP | BIRP | SIRP | DAP | BEHAVIORAL_SOAP | PHYSICAL_SOAP`   
Required: No

## See Also
<a name="API_ClinicalNoteGenerationSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-2017-10-26/ClinicalNoteGenerationSettings) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-2017-10-26/ClinicalNoteGenerationSettings) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-2017-10-26/ClinicalNoteGenerationSettings) 