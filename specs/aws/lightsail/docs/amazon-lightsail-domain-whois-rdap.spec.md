---
id: "@specs/aws/lightsail/docs/amazon-lightsail-domain-whois-rdap"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Domain details"
status: active
depends_on:
  - "@specs/aws/lightsail/meta"
---

# Domain details

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lightsail/docs/amazon-lightsail-domain-whois-rdap
> **target_lang:** meta — documentation tier. ALL sections preserved.



# View registration details for domains that are registered with Amazon Registrar
<a name="amazon-lightsail-domain-whois-rdap"></a>

You can view information about .com, .net, and .org domains that were registered using Amazon Lightsail and Amazon Route 53, for which Amazon Registrar is the registrar. This information includes details such as when the domain was originally registered and contact information for the domain owner and for the technical and administrative contacts.

Note the following:

**Email domain contacts when privacy protection is active**  
If privacy protection is active for the domain, contact information for the registrant, technical, and administrative contacts is replaced with contact information for the Amazon Registrar privacy service. For example, if the **example.com** domain is registered with Amazon Registrar and if privacy protection is active, the value of **Registrant Email** in the response to a WHOIS query would be similar to `owner1234@example.com.whoisprivacyservice.org`.  
To contact one or more domain contacts when privacy protection is active, send an email to the corresponding email addresses. We will automatically forward your email to the applicable contact. 

**Report abuse**  
To report any illegal activity or violation of the [Acceptable Use Policy](http://aws.amazon.com/route53/amazon-registrar-policies/#acceptable-use-policy) , including inappropriate content, phishing, malware, or spam, send an email to **trustandsafety@support.aws.com**.

**To view information about domains that are registered with Amazon Registrar**  

1. In a web browser, go to one of the following websites. Both websites display the same information. However, they use different protocols and display the information in different formats:
   + **WHOIS**: [https://registrar.amazon.com/whois](https://registrar.amazon.com/whois)
   + **RDAP**: [https://registrar.amazon.com/rdap](https://registrar.amazon.com/rdap)

1. Enter the name of the domain that you want to view information about, and choose **Search**. If the domain you search for was not registered using Amazon Lightsail or Route 53, then you will see a message stating that the domain is not in the registrar database.