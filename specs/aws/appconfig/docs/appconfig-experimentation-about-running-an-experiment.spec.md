---
id: "@specs/aws/appconfig/docs/appconfig-experimentation-about-running-an-experiment"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS About running and monitoring an experiment"
status: active
depends_on:
  - "@specs/aws/appconfig/meta"
---

# About running and monitoring an experiment

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appconfig/docs/appconfig-experimentation-about-running-an-experiment
> **target_lang:** meta — documentation tier. ALL sections preserved.



# About running and monitoring an experiment
<a name="appconfig-experimentation-about-running-an-experiment"></a>

Running an experiment in production requires careful monitoring and operational planning. Gradually increasing exposure, validating implementation, and monitoring performance can help reduce risk and improve the reliability of experiment results.

**Topics**
+ [Operational considerations](#appconfig-experimentation-about-running-an-experiment-operational-considerations)
+ [Performance considerations](#appconfig-experimentation-about-running-an-experiment-performance-considerations)
+ [Operational principles](#appconfig-experimentation-about-running-an-experiment-implementation-considerations)

## Operational considerations
<a name="appconfig-experimentation-about-running-an-experiment-operational-considerations"></a>

**Start with low or 0% exposure and increase exposure gradually**

Before exposing users to treatments:
+ Validate treatment rendering
+ Confirm feature flag evaluation
+ Verify metrics and logging
+ Test instrumentation using treatment assignment overrides

Starting with 0% exposure helps detect implementation issues before affecting users. You can then increase exposure gradually and thereby limit the impact of regressions if problems occur. By validating experiment behavior under increasing load, you can monitor experiment results and operational metrics before exposing your entire audience to changes.

**Define rollback procedures**

Before starting an experiment run, determine:
+ When the run should be stopped
+ Which metrics indicate unacceptable behavior
+ How to disable treatments

You can configure alarms in CloudWatch or third-party monitoring tools such as Datadog, New Relic, or Dynatrace to monitor key metrics like page load time, conversion rate, or error rates during an experiment. If an alarm triggers, evaluate the impact and decide whether to stop the experiment run or continue. For more information about configuring alarms, see [Monitoring deployments for automatic rollback](monitoring-deployments.md).

**Coordinate deployments**

Avoid introducing major application changes during an active experiment run. Changes to feature flag logic, backend systems, or user flows can invalidate experiment results or complicate analysis. If changes are required, stop the current run and start a new one after updates have been applied.

Also, limit overlapping experiments affecting the same users or functionality. Overlapping experiments can skew results and introduce conflicting behavior. In short, coordinate experiments carefully when audiences overlap.

## Performance considerations
<a name="appconfig-experimentation-about-running-an-experiment-performance-considerations"></a>

When you start an experiment, monitor application performance by tracking operational metrics throughout the run. Specifically, monitor:
+ Latency
+ Error rates
+ Throughput
+ Resource utilization

A treatment may affect system behavior even if experiment metrics appear positive. Gradual exposure helps identify these issues safely.

**Validate client-side performance**

For UI experiments, monitor:
+ Page load time
+ Rendering performance
+ Client-side errors
+ Device-specific behavior

Different treatments may affect frontend performance differently.

## Operational principles
<a name="appconfig-experimentation-about-running-an-experiment-implementation-considerations"></a>

As an experiment is running, keep in mind the following operational principles:

**Treat experiments as production changes**  
Even small experiments can affect application stability, performance, user experience, and data quality. Careful monitoring and gradual exposure help reduce risk while improving confidence in experiment results.

**Maintain treatment consistency**  
Users should receive the same treatment throughout the run. For more information about treatment design, see [About controls and treatments](appconfig-experimentation-about-controls-and-treatments.md).

**Validate instrumentation**  
Before increasing exposure, confirm that metrics are recorded correctly and that logs include treatment information.

**Monitor experiment-specific metrics**  
In addition to operational metrics, monitor metrics directly related to the experiment, such as:  
+ Conversion rate
+ Feature engagement
+ Click-through rate
+ Error frequency
+ User retention
Choose metrics that align with the experiment objective.