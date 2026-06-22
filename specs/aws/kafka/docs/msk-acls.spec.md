---
id: "@specs/aws/kafka/docs/msk-acls"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Apache Kafka ACLs"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Apache Kafka ACLs

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/msk-acls
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Apache Kafka ACLs
<a name="msk-acls"></a>

Apache Kafka has a pluggable authorizer and ships with an out-of-box authorizer implementation. Amazon MSK enables this authorizer in the `server.properties` file on the brokers.

Apache Kafka ACLs have the format "Principal P is [Allowed/Denied] Operation O From Host H on any Resource R matching ResourcePattern RP". If RP doesn't match a specific resource R, then R has no associated ACLs, and therefore no one other than super users is allowed to access R. To change this Apache Kafka behavior, you set the property `allow.everyone.if.no.acl.found` to true. Amazon MSK sets it to true by default. This means that with Amazon MSK clusters, if you don't explicitly set ACLs on a resource, all principals can access this resource. If you enable ACLs on a resource, only the authorized principals can access it. If you want to restrict access to a topic and authorize a client using TLS mutual authentication, add ACLs using the Apache Kafka authorizer CLI. For more information about adding, removing, and listing ACLs, see [Kafka Authorization Command Line Interface](https://cwiki.apache.org/confluence/display/KAFKA/Kafka+Authorization+Command+Line+Interface).

Because Amazon MSK configures brokers as super users, they can access all topics. This helps the brokers to replicate messages from the primary partition whether or not the `allow.everyone.if.no.acl.found` property is defined for the cluster's configuration.

**To add or remove read and write access to a topic**

1. Add your brokers to the ACL table to allow them to read from all topics that have ACLs in place. To grant your brokers read access to a topic, run the following command on a client machine that can communicate with the MSK cluster. 

   Replace {{Distinguished-Name}} with the DNS of any of your cluster's bootstrap brokers, then replace the string before the first period in this distinguished name by an asterisk (`*`). For example, if one of your cluster's bootstrap brokers has the DNS `b-6.mytestcluster.67281x.c4.kafka.us-east-1.amazonaws.com`, replace {{Distinguished-Name}} in the following command with `*.mytestcluster.67281x.c4.kafka.us-east-1.amazonaws.com`. For information on how to get the bootstrap brokers, see [Get the bootstrap brokers for an Amazon MSK cluster](msk-get-bootstrap-brokers.md).

   ```
   {{<path-to-your-kafka-installation>}}/bin/kafka-acls.sh --bootstrap-server BootstrapServerString --add --allow-principal "User:CN={{Distinguished-Name}}" --operation Read --group=* --topic {{Topic-Name}}
   ```

1. To grant a client application read access to a topic, run the following command on your client machine. If you use mutual TLS authentication, use the same {{Distinguished-Name}} you used when you created the private key.

   ```
   {{<path-to-your-kafka-installation>}}/bin/kafka-acls.sh --bootstrap-server BootstrapServerString --add --allow-principal "User:CN={{Distinguished-Name}}" --operation Read --group=* --topic {{Topic-Name}}
   ```

   To remove read access, you can run the same command, replacing `--add` with `--remove`.

1. To grant write access to a topic, run the following command on your client machine. If you use mutual TLS authentication, use the same {{Distinguished-Name}} you used when you created the private key.

   ```
   {{<path-to-your-kafka-installation>}}/bin/kafka-acls.sh --bootstrap-server BootstrapServerString --add --allow-principal "User:CN={{Distinguished-Name}}" --operation Write --topic {{Topic-Name}}
   ```

   To remove write access, you can run the same command, replacing `--add` with `--remove`.