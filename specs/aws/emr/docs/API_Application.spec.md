---
id: "@specs/aws/emr/docs/API_Application"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Application"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# Application

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_Application
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Application
<a name="API_Application"></a>

With Amazon EMR release version 4.0 and later, the only accepted parameter is the application name. To pass arguments to applications, you use configuration classifications specified using configuration JSON objects. For more information, see [Configuring Applications](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html).

With earlier Amazon EMR releases, the application is any Amazon or third-party software that you can add to the cluster. This structure contains a list of strings that indicates the software to use with the cluster and accepts a user argument list. Amazon EMR accepts and forwards the argument list to the corresponding installation script as bootstrap action argument.

## Contents
<a name="API_Application_Contents"></a>

 ** AdditionalInfo **   <a name="EMR-Type-Application-AdditionalInfo"></a>
This option is for advanced users only. This is meta information about third-party applications that third-party vendors use for testing purposes.  
Type: String to string map  
Required: No

 ** Args **   <a name="EMR-Type-Application-Args"></a>
Arguments for Amazon EMR to pass to the application.  
Type: Array of strings  
Required: No

 ** Name **   <a name="EMR-Type-Application-Name"></a>
The name of the application.  
Type: String  
Required: No

 ** Version **   <a name="EMR-Type-Application-Version"></a>
The version of the application.  
Type: String  
Required: No

## See Also
<a name="API_Application_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/Application) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/Application) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/Application) 