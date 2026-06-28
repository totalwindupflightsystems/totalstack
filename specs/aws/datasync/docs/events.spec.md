---
id: "@specs/aws/datasync/docs/events"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Monitoring with EventBridge"
status: active
depends_on:
  - "@specs/aws/datasync/meta"
---

# Monitoring with EventBridge

> **source:** AWS Documentation
> **spec:id:** @specs/aws/datasync/docs/events
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Monitoring events by using Amazon EventBridge
<a name="events"></a>

Amazon EventBridge events describe changes in DataSync resources. You can set up rules to match these events and route them to one or more target functions or streams. Events are emitted on a best-effort basis.

## DataSync transfer events
<a name="events-transfer"></a>

The following EventBridge events are available for DataSync transfers.


| **Agent state changes** | 
| --- |
| Event | Description | 
| Online | The agent is configured properly and ready to use. This is the normal running status for an agent. | 
| Offline | The agent has been out of contact with the DataSync service for five minutes or longer. This can happen for a few reasons. For more information, see [What do I do if my agent is offline?](troubleshooting-datasync-agents.md#troubleshoot-agent-offline) | 
| **Location state changes** | 
| --- |
| Event | Description | 
| Adding | DataSync is adding a location. | 
| Available | The location is created and is available to use. | 
| **Task state changes** | 
| --- |
| Event | Description | 
| Available | The task was created and is ready to start. | 
| Running | The task is in progress and functioning properly.  | 
| Unavailable | The task isn't configured properly and can't be used. You might see this event when an agent associated with the task goes offline.  | 
| Queued | Another task is running and using the same agent. DataSync runs tasks in series (first in, first out).  | 
| **Task execution state changes** | 
| --- |
| Event | Description | 
| Queueing | Another task execution is running and using the same DataSync agent. For more information, see [Knowing when your task is queued](run-task.md#queue-task-execution). | 
| Launching | DataSync is initializing the task execution. This status usually goes quickly but can take up to a few minutes. | 
| Preparing | DataSync is determining what data to transfer.<br />This step can take just minutes or a few hours depending on the number of files, objects, or directories in both locations and on how you configure your task. Preparation also might not be applicable to your task. For more information, see [How DataSync prepares your data transfer](how-datasync-transfer-works.md#how-datasync-prepares). | 
| Transferring |  DataSync is performing the actual data transfer. | 
| Verifying | DataSync is performing a data-integrity check at the end of the transfer. | 
| Success | The task execution succeeded. | 
| Cancelling | The task execution is in the process of being cancelled. | 
| Error | The task execution failed. | 