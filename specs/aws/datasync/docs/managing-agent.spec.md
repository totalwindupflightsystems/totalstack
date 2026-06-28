---
id: "@specs/aws/datasync/docs/managing-agent"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Managing your agent"
status: active
depends_on:
  - "@specs/aws/datasync/meta"
---

# Managing your agent

> **source:** AWS Documentation
> **spec:id:** @specs/aws/datasync/docs/managing-agent
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Managing your AWS DataSync agent
<a name="managing-agent"></a>

Once you [activate an AWS DataSync agent](activate-agent.md), AWS manages the virtual machine (VM) appliance for you.

## Agent software updates
<a name="managing-agent-updates"></a>

AWS automatically updates your agent's software, including the underlying operating system and related DataSync software packages. 

DataSync updates your agent only when it's idle. For example, your agent won't be updated until your transfer is complete.

The agent might go offline briefly following updates. This can happen, for instance, shortly after [agent activation](activate-agent.md) when AWS updates the agent.

**Important**  
DataSync automatically and regularly patches agents to maintain their security and stability. DataSync Basic mode agents use Amazon Linux 2 as their base operating system. DataSync Enhanced mode agents use Amazon Linux 2023 as their base operating system. You can view the current status of detected Common Vulnerabilities and Exposures (CVE) issues on the [Amazon Linux Security Center](https://explore.alas.aws.amazon.com/). CVE patches are automatically applied within 30 days of their release date, as indicated on the Amazon Linux Security Center. Patching occurs as long as your agent is online and not actively running a task execution.
DataSync doesn't support updating an Amazon EC2 agent manually with cloud-init directives. If you update an agent this way, you may encounter interoperability problems with DataSync where you can’t activate or use the agent.

## Agent statuses
<a name="understand-agent-statuses"></a>

The following table describes the status of DataSync agents.


| Agent status | Meaning | 
| --- | --- | 
| Online | The agent is configured properly and ready to use. This is the normal running status for an agent. | 
| Offline | The agent has been out of contact with the DataSync service for five minutes or longer. This can happen for a few reasons. For more information, see [What do I do if my agent is offline?](troubleshooting-datasync-agents.md#troubleshoot-agent-offline) | 

## Troubleshooting your agent
<a name="managing-agent-troubleshooting"></a>

While AWS manages the DataSync agent for you, there are situations when you might need to again work directly with it. For example, if your agent goes offline or loses its connection to your on-premises storage system, you can try to resolve these issues in the [agent’s local console](local-console-vm.md).

For more information, see [troubleshooting DataSync agents](troubleshooting-datasync-agents.md).