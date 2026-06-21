---
id: "@specs/aws/lightsail/docs/lightsail-delete-dns-zone"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Delete a DNS zone"
status: active
depends_on:
  - "@specs/aws/lightsail/meta"
---

# Delete a DNS zone

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lightsail/docs/lightsail-delete-dns-zone
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Delete a DNS zone in Lightsail
<a name="lightsail-delete-dns-zone"></a>

In some cases, you might want to completely remove a DNS zone that you've set up in Amazon Lightsail to manage your domain's DNS records. Perhaps you want to transfer DNS management to a different provider or back to your domain registrar. Deleting a DNS zone is a straightforward process, but it's important to plan ahead to ensure your domain's traffic continues to route correctly. Let's go over the steps to delete a DNS zone in Lightsail.

**Important**  
If you plan to continue routing traffic through your domain, prepare a different DNS hosting provider before deleting your domain's DNS zone in Lightsail. Otherwise, all traffic to your website stops when you delete the Lightsail DNS zone. 

**To delete a DNS zone**

1. On the Lightsail console home page, In the left navigation pane, choose **Domains & DNS**.

1. Choose the name of the DNS zone you want to delete.

1. Choose the vertical ellipsis menu (⋮). Then, choose the **Delete** option.

1. Choose **Delete DNS zone** to confirm the deletion.

   The DNS zone is deleted from Lightsail.