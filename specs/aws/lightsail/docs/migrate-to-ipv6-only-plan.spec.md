---
id: "@specs/aws/lightsail/docs/migrate-to-ipv6-only-plan"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Change networking type"
status: active
depends_on:
  - "@specs/aws/lightsail/meta"
---

# Change networking type

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lightsail/docs/migrate-to-ipv6-only-plan
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Switch instance networking type to IPv6 or dual-stack in Lightsail
<a name="migrate-to-ipv6-only-plan"></a>

Your instance’s networking type determines which protocol it uses to communicate over the Internet. When you create an instance, you choose between **dual-stack** or **IPv6-only** networking. You can also change the networking type of an existing instance from dual-stack to IPv6-only, and the other way around. Change the networking type by using a guided, step-by-step workflow, or by completing the individual steps.

With the guided workflow, your instance will continue to run while the new networking type is configured. Use this option for your instance to remain reachable over the internet while the change takes place. But first, make sure your local network, computer, devices, and end-users can communicate using IPv6. For more information, see [Verify IPv6 reachability for Lightsail instances](amazon-lightsail-ipv6-reachability.md).

With the individual steps, you’ll snapshot your instance, then create a new instance from the snapshot. You can choose a different networking type as you're creating the new instance. Use this option to verify IPv6 compatibility before changing the configuration of your other instance. Before you begin, we recommend that you review the [IPv6-only considerations](#ipv6-only-considerations).

## IPv6-only considerations
<a name="ipv6-only-considerations"></a>

Review the following considerations:
+ Your instance plan changes whenever its networking type is changed. For more information, see [Announcing IPv6 instance bundles and pricing update on Amazon Lightsail](https://aws.amazon.com/blogs/compute/announcing-ipv6-instance-bundles-and-pricing-update-on-amazon-lightsail) on the *AWS Compute Blog*.
+ Your instance will communicate publicly over IPv6. It will not support incoming or outgoing public IPv4 traffic. It will receive a private IPv4 address for communicating with other resources in your Lightsail account. For more information, see [View and manage IP addresses for Lightsail resources](understanding-public-ip-and-private-ip-addresses-in-amazon-lightsail.md).
+ You can configure IPv6-only instances as the origin for a Lightsail content delivery network (CDN) distribution.
+ You can add IPv6-only instances to a Lightsail load balancer.
+ The allowance for your instance's data transfer plan will carry over when you change networking types. It will not reset.
+ Verify that your local devices, network, and Internet Service Provider (ISP) are IPv6-compatible. For more information, see [Verify IPv6 reachability for Lightsail instances](amazon-lightsail-ipv6-reachability.md).

## Option: Guided workflow
<a name="switch-instance-networking-wizard"></a>

**To configure your instance networking type using the wizard**

1. On the instance management page, on the information panel, choose **Change networking type**.

1. For **Select networking type**, select **Dual-stack** or **IPv6-only**. Review the information that is highlighted below the option that you chose, then choose **Next**.

1. For **Review resources**, review the changes that will be made to the resources currently associated with your instance. Resources can be a static IP address, or a Lightsail load balancer. No changes will be made if there are no resources attached to your instance. Resource changes will not take place until you complete the workflow in the next step. Choose **Next** to continue.

1. For **Confirm changes**, review the new instance networking type, pricing, and resource changes and choose **Confirm changes**. We start to configure your Lightsail resources.

1. (Optional) Update your instance configuration after the workflow is complete. For example, attach a static IP to your instance, or update DNS A records for IPv4, and AAAA records for IPv6. For next steps, see the [Next steps](#change-networking-next-steps) section of this guide.

## Option: Individual steps
<a name="switch-networking-manual"></a>

**To configure your instance networking type by completing the individual steps**

1. On the instance management page, on the **Snapshots** tab, choose **Create snapshot**. For more information, see one of the following topics:
   + [Back up Linux/Unix Lightsail instances with snapshots](lightsail-how-to-create-a-snapshot-of-your-instance.md)
   + [Create a snapshot of your Lightsail Windows Server instance](prepare-windows-based-instance-and-create-snapshot.md)

1. Give your snapshot a name, then choose **Create**.

1. From the snapshot actions menu (⋮), choose **Create a new instance**. For more information, see [Create Lightsail instances from snapshots](lightsail-how-to-create-instance-from-snapshot.md).

1. From the **Select networking type** section, choose **Dual-stack** or **IPv6-only**.

1. Review the remaining options and choose **Create instance**. Your new instance is created.

1. (Optional) Update your instance configuration after the workflow is complete. For example, attach a static IP to your instance, or update DNS A records for IPv4, and AAAA records for IPv6. For next steps, see the [Next steps](#change-networking-next-steps) section of this guide.

## Next steps
<a name="change-networking-next-steps"></a>

There are a few additional tasks that you can perform after you change the networking type of your instance:
+ **(IPv6-only)** Ensure that your application and users are able to communicate over IPv6. For more information, see [Verify IPv6 reachability for Lightsail instances](amazon-lightsail-ipv6-reachability.md).
+ **(Dual-stack)** Attach a static IP address to your instance. For more information, see [Attach a static IP to an instance](lightsail-create-static-ip.md).
+ **(Both)** Configure your instance as the origin of a Lightsail distribution. For more information, see [CDN distributions in Lightsail](amazon-lightsail-content-delivery-network-distributions.md).
+ **(Both)** Add or update the firewall settings for your instance. For more information, see [Instance firewalls in Lightsail](understanding-firewall-and-port-mappings-in-amazon-lightsail.md).
+ **(Both)** Add or update DNS A records for IPv4, and AAAA records for IPv6. For more information, see [Point your domain to an instance](amazon-lightsail-routing-to-instance.md).
+ **(Both)** Add your instance to a Lightsail load balancer. For more information, see [Load balancers in Lightsail](understanding-lightsail-load-balancers.md).