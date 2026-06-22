"""
AWS Batch store — compute environments, job queues, job definitions, jobs, scheduling policies.
"""
import uuid


# ── Exceptions ─────────────────────────────────────────────────────
class ClientException(Exception):
    pass

class ServerException(Exception):
    pass


# ── Data Classes ────────────────────────────────────────────────────
class ComputeEnvironmentRecord:
    def __init__(self, compute_environment_name, compute_environment_arn="",
                 compute_resources=None, service_role="", state="ENABLED",
                 status="VALID", status_reason="", ecs_cluster_arn=""):
        self.compute_environment_name = compute_environment_name
        self.compute_environment_arn = compute_environment_arn or f"arn:aws:batch:us-east-1:000000000000:compute-environment/{compute_environment_name}"
        self.compute_resources = compute_resources or {}
        self.service_role = service_role
        self.state = state
        self.status = status
        self.status_reason = status_reason
        self.ecs_cluster_arn = ecs_cluster_arn
        self.type = "MANAGED" if compute_resources else "UNMANAGED"

    def to_dict(self):
        return {
            "computeEnvironmentName": self.compute_environment_name,
            "computeEnvironmentArn": self.compute_environment_arn,
            "ecsClusterArn": self.ecs_cluster_arn,
            "type": self.type,
            "state": self.state,
            "status": self.status,
            "statusReason": self.status_reason,
            "computeResources": self.compute_resources,
            "serviceRole": self.service_role,
        }


class JobQueueRecord:
    def __init__(self, job_queue_name, job_queue_arn="",
                 priority=1, state="ENABLED", status="VALID",
                 compute_environment_order=None, scheduling_policy_arn=""):
        self.job_queue_name = job_queue_name
        self.job_queue_arn = job_queue_arn or f"arn:aws:batch:us-east-1:000000000000:job-queue/{job_queue_name}"
        self.priority = priority
        self.state = state
        self.status = status
        self.compute_environment_order = compute_environment_order or []
        self.scheduling_policy_arn = scheduling_policy_arn

    def to_dict(self):
        return {
            "jobQueueName": self.job_queue_name,
            "jobQueueArn": self.job_queue_arn,
            "priority": self.priority,
            "state": self.state,
            "status": self.status,
            "computeEnvironmentOrder": self.compute_environment_order,
            "schedulingPolicyArn": self.scheduling_policy_arn,
        }


class JobDefinitionRecord:
    def __init__(self, job_definition_name, job_definition_arn="",
                 revision=1, type="container", status="ACTIVE",
                 container_properties=None, node_properties=None,
                 parameters=None, platform_capabilities=None,
                 propagate_tags=False, retry_strategy=None,
                 timeout=None, tags=None):
        self.job_definition_name = job_definition_name
        self.job_definition_arn = job_definition_arn or f"arn:aws:batch:us-east-1:000000000000:job-definition/{job_definition_name}:{revision}"
        self.revision = revision
        self.type = type
        self.status = status
        self.container_properties = container_properties or {}
        self.node_properties = node_properties
        self.parameters = parameters or {}
        self.platform_capabilities = platform_capabilities or ["EC2"]
        self.propagate_tags = propagate_tags
        self.retry_strategy = retry_strategy
        self.timeout = timeout
        self.tags = tags or {}

    def to_dict(self):
        result = {
            "jobDefinitionName": self.job_definition_name,
            "jobDefinitionArn": self.job_definition_arn,
            "revision": self.revision,
            "type": self.type,
            "status": self.status,
        }
        if self.container_properties:
            result["containerProperties"] = self.container_properties
        if self.parameters:
            result["parameters"] = self.parameters
        if self.retry_strategy:
            result["retryStrategy"] = self.retry_strategy
        if self.timeout:
            result["timeout"] = self.timeout
        if self.tags:
            result["tags"] = self.tags
        return result


class JobRecord:
    def __init__(self, job_id=None, job_name="", job_queue="",
                 job_definition="", status="SUBMITTED",
                 status_reason="", created_at=None, started_at=None,
                 stopped_at=None, container=None, parameters=None,
                 array_properties=None, depends_on=None,
                 retry_strategy=None, timeout=None, tags=None):
        self.job_id = job_id or str(uuid.uuid4())
        self.job_name = job_name
        self.job_queue = job_queue
        self.job_definition = job_definition
        self.status = status
        self.status_reason = status_reason
        self.created_at = created_at
        self.started_at = started_at
        self.stopped_at = stopped_at
        self.container = container or {}
        self.parameters = parameters or {}
        self.array_properties = array_properties
        self.depends_on = depends_on or []
        self.retry_strategy = retry_strategy
        self.timeout = timeout
        self.tags = tags or {}

    def to_dict(self):
        return {
            "jobId": self.job_id,
            "jobName": self.job_name,
            "jobQueue": self.job_queue,
            "jobDefinition": self.job_definition,
            "status": self.status,
            "statusReason": self.status_reason,
            "createdAt": self.created_at,
            "startedAt": self.started_at,
            "stoppedAt": self.stopped_at,
            "container": self.container,
            "parameters": self.parameters,
            "dependsOn": self.depends_on,
            "tags": self.tags,
        }


class SchedulingPolicyRecord:
    def __init__(self, name, arn="", fairshare_policy=None):
        self.name = name
        self.arn = arn or f"arn:aws:batch:us-east-1:000000000000:scheduling-policy/{name}"
        self.fairshare_policy = fairshare_policy or {}

    def to_dict(self):
        return {
            "name": self.name,
            "arn": self.arn,
            "fairsharePolicy": self.fairshare_policy,
        }


# ── Store ──────────────────────────────────────────────────────────
class BatchStore:
    def __init__(self):
        self._compute_environments: dict[str, ComputeEnvironmentRecord] = {}
        self._job_queues: dict[str, JobQueueRecord] = {}
        self._job_definitions: dict[str, list[JobDefinitionRecord]] = {}  # name → [revisions]
        self._jobs: dict[str, JobRecord] = {}
        self._scheduling_policies: dict[str, SchedulingPolicyRecord] = {}
        self._tags: dict[str, dict] = {}

    # ── Compute Environments ───────────────────────────────────────
    def compute_environments(self, name=None):
        if name is not None:
            return self._compute_environments.get(name)
        return list(self._compute_environments.values())

    def create_compute_environment(self, compute_environment_name, type,
                                    service_role, compute_resources=None,
                                    state="ENABLED", tags=None):
        if compute_environment_name in self._compute_environments:
            raise ClientException(f"Compute environment '{compute_environment_name}' already exists")
        record = ComputeEnvironmentRecord(
            compute_environment_name=compute_environment_name,
            compute_resources=compute_resources,
            service_role=service_role,
            state=state,
        )
        record.type = type
        self._compute_environments[compute_environment_name] = record
        if tags:
            self._tags[record.compute_environment_arn] = dict(tags)
        return {
            "computeEnvironmentName": record.compute_environment_name,
            "computeEnvironmentArn": record.compute_environment_arn,
        }

    def describe_compute_environments(self, compute_environments=None,
                                       max_results=None, next_token=None):
        if compute_environments:
            records = [self._compute_environments[n] for n in compute_environments
                       if n in self._compute_environments]
        else:
            records = list(self._compute_environments.values())
        items = [r.to_dict() for r in records]
        return {"computeEnvironments": items}

    def update_compute_environment(self, compute_environment, state=None,
                                    compute_resources=None, service_role=None):
        record = self._compute_environments.get(compute_environment)
        if not record:
            raise ClientException(f"Compute environment '{compute_environment}' not found")
        if state is not None:
            record.state = state
        if compute_resources is not None:
            record.compute_resources = compute_resources
        if service_role is not None:
            record.service_role = service_role
        return {
            "computeEnvironmentName": record.compute_environment_name,
            "computeEnvironmentArn": record.compute_environment_arn,
        }

    def delete_compute_environment(self, compute_environment):
        if compute_environment not in self._compute_environments:
            raise ClientException(f"Compute environment '{compute_environment}' not found")
        del self._compute_environments[compute_environment]
        return {}

    # ── Job Queues ─────────────────────────────────────────────────
    def job_queues(self, name=None):
        if name is not None:
            return self._job_queues.get(name)
        return list(self._job_queues.values())

    def create_job_queue(self, job_queue_name, state="ENABLED", priority=1,
                          compute_environment_order=None,
                          scheduling_policy_arn="", tags=None):
        if job_queue_name in self._job_queues:
            raise ClientException(f"Job queue '{job_queue_name}' already exists")
        record = JobQueueRecord(
            job_queue_name=job_queue_name,
            priority=priority,
            state=state,
            compute_environment_order=compute_environment_order,
            scheduling_policy_arn=scheduling_policy_arn,
        )
        self._job_queues[job_queue_name] = record
        if tags:
            self._tags[record.job_queue_arn] = dict(tags)
        return {
            "jobQueueName": record.job_queue_name,
            "jobQueueArn": record.job_queue_arn,
        }

    def describe_job_queues(self, job_queues=None, max_results=None, next_token=None):
        if job_queues:
            records = [self._job_queues[n] for n in job_queues if n in self._job_queues]
        else:
            records = list(self._job_queues.values())
        return {"jobQueues": [r.to_dict() for r in records]}

    def update_job_queue(self, job_queue, state=None, priority=None,
                          compute_environment_order=None,
                          scheduling_policy_arn=None):
        record = self._job_queues.get(job_queue)
        if not record:
            raise ClientException(f"Job queue '{job_queue}' not found")
        if state is not None:
            record.state = state
        if priority is not None:
            record.priority = priority
        if compute_environment_order is not None:
            record.compute_environment_order = compute_environment_order
        if scheduling_policy_arn is not None:
            record.scheduling_policy_arn = scheduling_policy_arn
        return {
            "jobQueueName": record.job_queue_name,
            "jobQueueArn": record.job_queue_arn,
        }

    def delete_job_queue(self, job_queue):
        if job_queue not in self._job_queues:
            raise ClientException(f"Job queue '{job_queue}' not found")
        del self._job_queues[job_queue]
        return {}

    # ── Job Definitions ────────────────────────────────────────────
    def register_job_definition(self, job_definition_name, type, container_properties=None,
                                 node_properties=None, parameters=None,
                                 platform_capabilities=None, propagate_tags=False,
                                 retry_strategy=None, timeout=None, tags=None):
        existing = self._job_definitions.get(job_definition_name, [])
        revision = len(existing) + 1
        record = JobDefinitionRecord(
            job_definition_name=job_definition_name,
            revision=revision,
            type=type,
            container_properties=container_properties,
            node_properties=node_properties,
            parameters=parameters,
            platform_capabilities=platform_capabilities,
            propagate_tags=propagate_tags,
            retry_strategy=retry_strategy,
            timeout=timeout,
            tags=tags,
        )
        if job_definition_name not in self._job_definitions:
            self._job_definitions[job_definition_name] = []
        self._job_definitions[job_definition_name].append(record)
        return {
            "jobDefinitionName": record.job_definition_name,
            "jobDefinitionArn": record.job_definition_arn,
            "revision": record.revision,
        }

    def describe_job_definitions(self, job_definitions=None, job_definition_name=None,
                                   status=None, max_results=None, next_token=None):
        records = []
        if job_definitions:
            # Look up by ARN
            for arn in job_definitions:
                parts = arn.split(":")
                name = parts[-1].split("/")[-1] if "/" in parts[-1] else parts[-1]
                rev_str = parts[-1].split(":")[-1] if ":" in parts[-1] else "1"
                revs = self._job_definitions.get(name, [])
                for r in revs:
                    if str(r.revision) == rev_str:
                        records.append(r)
                        break
        elif job_definition_name:
            records = self._job_definitions.get(job_definition_name, [])
        else:
            for revs in self._job_definitions.values():
                records.extend(revs)
        return {"jobDefinitions": [r.to_dict() for r in records]}

    def deregister_job_definition(self, job_definition):
        # job_definition is ARN: "arn:aws:batch:...:job-definition/name:rev"
        parts = job_definition.rsplit(":", 1)
        arn_base = parts[0]
        name = arn_base.split("job-definition/")[-1] if "job-definition/" in arn_base else arn_base.split("/")[-1]
        rev = int(parts[1]) if len(parts) > 1 and parts[1].isdigit() else None
        revs = self._job_definitions.get(name, [])
        for r in revs:
            if rev and r.revision == rev:
                r.status = "INACTIVE"
                break
        return {}

    # ── Jobs ───────────────────────────────────────────────────────
    def submit_job(self, job_name, job_queue, job_definition,
                    job_id=None, parameters=None, container_overrides=None,
                    array_properties=None, depends_on=None,
                    retry_strategy=None, timeout=None, tags=None):
        record = JobRecord(
            job_id=job_id or str(uuid.uuid4()),
            job_name=job_name,
            job_queue=job_queue,
            job_definition=job_definition,
            parameters=parameters,
            array_properties=array_properties,
            depends_on=depends_on,
            retry_strategy=retry_strategy,
            timeout=timeout,
            tags=tags,
        )
        self._jobs[record.job_id] = record
        return {"jobId": record.job_id, "jobName": record.job_name}

    def describe_jobs(self, jobs):
        records = [self._jobs[j] for j in jobs if j in self._jobs]
        return {"jobs": [r.to_dict() for r in records]}

    def list_jobs(self, job_queue=None, array_job_id=None, job_status=None,
                  max_results=None, next_token=None, filters=None):
        items = []
        for job in self._jobs.values():
            if job_queue and job.job_queue != job_queue:
                continue
            if job_status and job.status != job_status:
                continue
            items.append({
                "jobId": job.job_id,
                "jobName": job.job_name,
                "status": job.status,
                "jobDefinition": job.job_definition,
                "jobQueue": job.job_queue,
                "createdAt": job.created_at,
                "statusReason": job.status_reason,
            })
        return {"jobSummaryList": items}

    def cancel_job(self, job_id, reason):
        record = self._jobs.get(job_id)
        if not record:
            raise ClientException(f"Job '{job_id}' not found")
        record.status = "FAILED"
        record.status_reason = reason or "Canceled by user"
        return {}

    def terminate_job(self, job_id, reason):
        record = self._jobs.get(job_id)
        if not record:
            raise ClientException(f"Job '{job_id}' not found")
        record.status = "FAILED"
        record.status_reason = reason or "Terminated by user"
        return {}

    # ── Scheduling Policies ────────────────────────────────────────
    def create_scheduling_policy(self, name, fairshare_policy=None, tags=None):
        if name in self._scheduling_policies:
            raise ClientException(f"Scheduling policy '{name}' already exists")
        record = SchedulingPolicyRecord(name=name, fairshare_policy=fairshare_policy)
        self._scheduling_policies[name] = record
        if tags:
            self._tags[record.arn] = dict(tags)
        return {"name": record.name, "arn": record.arn}

    def describe_scheduling_policies(self, arns):
        records = []
        for record in self._scheduling_policies.values():
            if record.arn in arns:
                records.append(record.to_dict())
        return {"schedulingPolicies": records}

    def list_scheduling_policies(self, max_results=None, next_token=None):
        items = [r.to_dict() for r in self._scheduling_policies.values()]
        return {"schedulingPolicies": items}

    def update_scheduling_policy(self, arn, fairshare_policy=None):
        for record in self._scheduling_policies.values():
            if record.arn == arn:
                if fairshare_policy is not None:
                    record.fairshare_policy = fairshare_policy
                return {}
        raise ClientException(f"Scheduling policy '{arn}' not found")

    def delete_scheduling_policy(self, arn):
        for name, record in list(self._scheduling_policies.items()):
            if record.arn == arn:
                del self._scheduling_policies[name]
                return {}
        raise ClientException(f"Scheduling policy '{arn}' not found")

    # ── Tags ───────────────────────────────────────────────────────
    def tag_resource(self, resource_arn, tags):
        if resource_arn not in self._tags:
            self._tags[resource_arn] = {}
        self._tags[resource_arn].update(tags)
        return {}

    def untag_resource(self, resource_arn, tag_keys):
        if resource_arn in self._tags:
            for key in tag_keys:
                self._tags[resource_arn].pop(key, None)
        return {}

    def list_tags_for_resource(self, resource_arn):
        tags_dict = self._tags.get(resource_arn, {})
        return {"tags": dict(tags_dict)}
