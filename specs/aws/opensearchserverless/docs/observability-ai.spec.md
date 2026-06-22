---
id: "@specs/aws/opensearchserverless/docs/observability-ai"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AI observability"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# AI observability

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/observability-ai
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AI observability
<a name="observability-ai"></a>

AI observability in OpenSearch provides end-to-end tooling for monitoring, debugging, and optimizing AI agent and large language model (LLM) workflows. Built on GenAI semantic conventions and natively integrated with OpenTelemetry (OTel), it gives you full visibility into how your AI applications behave in production.

AI observability includes the following capabilities:
+ **Agent tracing** – Capture hierarchical execution traces across agent orchestration steps, LLM calls, tool invocations, and retrieval operations.
+ **GenAI semantic conventions** – Use standardized OTel attributes such as `gen_ai.system`, `gen_ai.request.model`, and `gen_ai.usage.input_tokens` to describe AI-specific telemetry.
+ **Auto-instrumentation** – Automatically capture traces from popular AI frameworks and providers, including OpenAI, Anthropic, Amazon Bedrock, LangChain, and more than 20 additional libraries.
+ **PPL querying** – Query and aggregate trace data using Piped Processing Language (PPL) directly from OpenSearch UI.

## Getting started
<a name="observability-ai-getting-started"></a>

This section walks you through instrumenting an AI agent, sending traces to Amazon OpenSearch Service, and viewing them in OpenSearch UI.

### To install the SDK
<a name="observability-ai-install-sdk"></a>

Install the OpenTelemetry GenAI instrumentation package:

```
pip install opentelemetry-instrumentation-openai-v2 opentelemetry-sdk opentelemetry-exporter-otlp
```

### To instrument your agent code
<a name="observability-ai-instrument"></a>

The following example shows how to register the OTel SDK, annotate your agent functions with the `@observe` decorator, and enrich spans with GenAI attributes.

```
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter

# Register the tracer provider
provider = TracerProvider()
processor = BatchSpanProcessor(
    OTLPSpanExporter(endpoint="<your-osis-endpoint>")  # Use your OpenSearch Ingestion endpoint with SigV4
)
provider.add_span_processor(processor)
trace.set_tracer_provider(provider)

tracer = trace.get_tracer(__name__)

# Decorate your agent function
@observe
def run_agent(prompt: str):
    with tracer.start_as_current_span("invoke_agent") as span:
        span.set_attribute("gen_ai.operation.name", "invoke_agent")
        span.set_attribute("gen_ai.system", "openai")
        span.set_attribute("gen_ai.request.model", "gpt-4")

        # Enrich with token usage after the LLM call
        response = call_llm(prompt)
        span.set_attribute("gen_ai.usage.input_tokens", response.input_tokens)
        span.set_attribute("gen_ai.usage.output_tokens", response.output_tokens)
        return response
```

**Note**  
When you send traces to Amazon OpenSearch Service, use your OpenSearch Ingestion pipeline endpoint with SigV4 authentication instead of a localhost endpoint. For more information about configuring OpenSearch Ingestion pipelines, see [Overview of Amazon OpenSearch Ingestion](ingestion.md).

### To view traces in OpenSearch UI
<a name="observability-ai-view-traces"></a>

After your instrumented application sends trace data, you can explore it in OpenSearch UI. In your observability workspace, expand **Discover** in the left navigation and choose **Agent Traces**.

## Agent Tracing UI
<a name="observability-ai-agent-tracing"></a>

The Agent Traces page in OpenSearch UI provides a purpose-built interface for exploring, debugging, and monitoring LLM agent execution traces. It gives developers and platform operators full observability into agentic AI applications, including hierarchical trace views, detail flyouts, flow visualizations, and aggregate metrics.

### Architecture
<a name="observability-ai-architecture"></a>

The following diagram shows the data flow from instrumented applications to the Agent Traces UI:

```
LLM Application (with OTel SDK + GenAI instrumentation)
    |
    |  OTLP (gRPC/HTTP)
    v
OTel Collector (batch, transform)
    |
    +---- OTLP ----> OpenSearch Ingestion --> OpenSearch (otel-v1-apm-span-*)
    |
    +---- Prometheus Remote Write --> Prometheus (metrics)
                                          |
                                          v
                              OpenSearch UI
                              +-- Agent Traces Plugin
```

### Prerequisites
<a name="observability-ai-prereqs"></a>

Before you use Agent Traces, make sure you have the following:
+ An OpenSearch cluster with trace data indexed in `otel-v1-apm-span-*` indices.
+ OpenTelemetry instrumentation with GenAI semantic conventions enabled in your LLM application.
+ OpenSearch Ingestion configured with the `otel_trace_raw` processor to ingest spans into OpenSearch.
+ PPL query support enabled in OpenSearch UI.

### Required span attributes
<a name="observability-ai-span-attributes"></a>

Agent Traces requires specific span attributes to render trace data correctly. The following tables describe the core fields and GenAI-specific attributes.

**Core span fields**  
Each span must include the following core fields:


| Field | Type | Description | 
| --- | --- | --- | 
| traceId | String | Unique identifier for the entire trace. | 
| spanId | String | Unique identifier for this span. | 
| parentSpanId | String | Identifier of the parent span. Empty for root spans. | 
| startTime | Timestamp | Time when the span started. | 
| endTime | Timestamp | Time when the span ended. | 
| durationInNanos | Long | Duration of the span in nanoseconds. | 
| status.code | Integer | Span status code (0 = unset, 1 = OK, 2 = error). | 

**GenAI attributes**  
The following `gen_ai.*` attributes enable AI-specific features in the Agent Traces UI:


| Attribute | Example value | Description | 
| --- | --- | --- | 
| gen\_ai.operation.name | chat | The type of GenAI operation. Determines the span category. | 
| gen\_ai.system | openai | The AI system or provider. | 
| gen\_ai.request.model | gpt-4 | The model used for the request. | 
| gen\_ai.usage.input\_tokens | 150 | Number of input tokens consumed. | 
| gen\_ai.usage.output\_tokens | 85 | Number of output tokens generated. | 
| gen\_ai.response.finish\_reasons | ["stop"] | Reasons the model stopped generating. | 

### Page layout and metrics bar
<a name="observability-ai-page-layout"></a>

The Agent Traces page displays a metrics bar at the top that summarizes key statistics across all visible traces. Metrics include total trace count, average duration, error rate, and token usage. These values update dynamically based on your time filter and query.

### Traces tab
<a name="observability-ai-traces-tab"></a>

The Traces tab lists all root agent traces that match your current query and time range. Each row represents a single agent invocation.

![Table displaying agent traces with columns for time, kind, name, status, latency, tokens, input, and output.](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/agent-traces/traces-table.png)


The following table describes the columns in the traces table:


| Column | Description | 
| --- | --- | 
| Trace ID | Unique identifier for the trace. Choose the link to open the trace details flyout. | 
| Agent name | Name of the agent that initiated the trace. | 
| Status | Overall trace status (OK or Error). | 
| Duration | Total time from the first span to the last span in the trace. | 
| Spans | Total number of spans in the trace. | 
| Input tokens | Total input tokens consumed across all LLM calls in the trace. | 
| Output tokens | Total output tokens generated across all LLM calls in the trace. | 
| Start time | Timestamp when the trace started. | 

### Span categories
<a name="observability-ai-span-categories"></a>

Spans are categorized based on the `gen_ai.operation.name` attribute. Each category is displayed with a unique color and icon in the UI.


| Operation name | Category | Description | 
| --- | --- | --- | 
| invoke\_agent, create\_agent | Agent | Agent orchestration step. | 
| chat | LLM | LLM chat completion call. | 
| text\_completion, generate\_content | Content | Text generation operation. | 
| execute\_tool | Tool | Tool invocation. | 
| embeddings | Embeddings | Embedding generation. | 
| retrieval | Retrieval | Data retrieval operation. | 

### Spans tab
<a name="observability-ai-spans-tab"></a>

The Spans tab displays individual spans across all traces. You can filter and sort spans to find specific operations.

![Spans tab showing a table with columns for Time, Kind, Name, Status, Latency, Tokens, Input, and Output.](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/agent-traces/spans-table.png)


### Trace details flyout
<a name="observability-ai-trace-details"></a>

When you choose a trace ID, a flyout panel opens with two main areas:
+ **Left panel** – Displays the trace tree, which shows the hierarchical parent-child relationships between spans. It also includes a flow DAG (directed acyclic graph) that visualizes the execution path of the agent.
+ **Right panel** – Contains two tabs. The **Detail** tab shows span attributes, resource attributes, and GenAI-specific metadata. The **Timeline** tab shows a waterfall chart of span durations and their timing relationships.

### Querying traces
<a name="observability-ai-querying"></a>

Agent Traces uses PPL (Piped Processing Language) for all data fetching. You can write queries in the query panel at the top of the page.

**To list root traces**  
The following query returns the 100 most recent root agent traces:

```
source = otel-v1-apm-span-*
| where parentSpanId = "" AND isnotnull(`attributes.gen_ai.operation.name`)
| sort - startTime
| head 100
```

**To fetch all spans for a trace**  
The following query returns the complete span tree for a specific trace:

```
source = otel-v1-apm-span-*
| where traceId = "{{trace-id}}"
| head 1000
```

**To compute aggregate metrics**  
The following query computes average duration and total token usage grouped by model:

```
source = otel-v1-apm-span-*
| where isnotnull(`attributes.gen_ai.request.model`)
| stats avg(durationInNanos) as avg_duration,
        sum(`attributes.gen_ai.usage.input_tokens`) as total_input_tokens,
        sum(`attributes.gen_ai.usage.output_tokens`) as total_output_tokens
    by `attributes.gen_ai.request.model`
```