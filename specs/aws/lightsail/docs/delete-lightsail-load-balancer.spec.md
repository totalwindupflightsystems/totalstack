---
id: "@specs/aws/lightsail/docs/delete-lightsail-load-balancer"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Delete load balancers"
status: active
depends_on:
  - "@specs/aws/lightsail/meta"
---

# Delete load balancers

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lightsail/docs/delete-lightsail-load-balancer
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Delete Lightsail load balancers
<a name="delete-lightsail-load-balancer"></a>

You can delete a Lightsail load balancer if you no longer need it. Deleting a load balancer also detaches any Lightsail instances attached to it but doesn't delete the Lightsail instances. If you enabled encrypted (HTTPS) traffic using an SSL/TLS certificate, deleting the load balancer will also permanently delete any SSL/TLS certificates associated with the load balancer.

**Important**  
Deleting a Lightsail load balancer and its associated certificate is final and can't be undone.

1. In the left navigation pane, choose **Networking**.

1. Choose the load balancer you want to delete.

1. Choose **Delete**.

1. Choose **Delete load balancer**.

1. Choose **Yes, delete**.