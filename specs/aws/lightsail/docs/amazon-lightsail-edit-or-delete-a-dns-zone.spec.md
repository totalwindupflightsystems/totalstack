---
id: "@specs/aws/lightsail/docs/amazon-lightsail-edit-or-delete-a-dns-zone"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Edit a DNS zone"
status: active
depends_on:
  - "@specs/aws/lightsail/meta"
---

# Edit a DNS zone

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lightsail/docs/amazon-lightsail-edit-or-delete-a-dns-zone
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Edit a Lightsail DNS zone
<a name="amazon-lightsail-edit-or-delete-a-dns-zone"></a>

Edit the DNS records in your domain's DNS zone. You can also delete your domain's DNS zone in Amazon Lightsail if you want to transfer management of your domain's DNS records to another DNS hosting provider or back to the registrar where you registered your domain. For more information, see [Delete a DNS zone in Lightsail](lightsail-delete-dns-zone.md)

**Note**  
Before you can edit records using the DNS editor in the Lightsail console, you must transfer management of your domain's DNS records to Lightsail. For more information, see [Create a DNS zone to manage your domain’s DNS records](lightsail-how-to-create-dns-entry.md).

## Edit DNS records
<a name="lightsail-edit-dns-records"></a>

You can edit the DNS records for your domain's DNS zone at any time using the Lightsail console.

**To edit the DNS zone**

1. Sign in to the Lightsail console.

1. On the Lightsail console home page, In the left navigation pane, choose **Domains & DNS**.

1. Choose the name of the DNS zone you want to edit.

1. On the DNS zone **DNS records** page, choose the **Delete** icon next to the record you want to delete.

1. When you're done, choose the **Save** icon to save your changes.
**Note**  
Allow time for the DNS record changes to propagate through the internet's DNS, which may take several hours.