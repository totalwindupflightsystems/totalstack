---
id: "@specs/aws/lambda/docs/java-customization"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Custom startup behavior"
status: active
depends_on:
  - "@specs/aws/lambda/meta"
---

# Custom startup behavior

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lambda/docs/java-customization
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Customize Java runtime startup behavior for Lambda functions
<a name="java-customization"></a>

This page describes settings specific to Java functions in AWS Lambda. You can use these settings to customize Java runtime startup behavior. This can reduce overall function latency and improve overall function performance, without having to modify any code.

**Topics**
+ [Understanding the `JAVA_TOOL_OPTIONS` environment variable](#java-tool-options)
+ [Log4j patch for Log4Shell](#log4shell-patch)
+ [Ahead-of-Time (AOT) and CDS caches](#aot-cds-caches)

## Understanding the `JAVA_TOOL_OPTIONS` environment variable
<a name="java-tool-options"></a>

In Java, Lambda supports the `JAVA_TOOL_OPTIONS` environment variable to set additional command-line variables in Lambda. You can use this environment variable in various ways, such as to customize tiered-compilation settings. The next example demonstrates how to use the `JAVA_TOOL_OPTIONS` environment variable for this use case.

### Example: Customizing tiered compilation settings
<a name="tiered-compilation"></a>

Tiered compilation is a feature of the Java virtual machine (JVM). You can use specific tiered compilation settings to make best use of the JVM's just-in-time (JIT) compilers. Typically, the C1 compiler is optimized for fast start-up time. The C2 compiler is optimized for best overall performance, but it also uses more memory and takes a longer time to achieve it. There are 5 different levels of tiered compilation. At Level 0, the JVM interprets Java byte code. At Level 4, the JVM uses the C2 compiler to analyze profiling data collected during application startup. Over time, it monitors code usage to identify the best optimizations.

Customizing the tiered compilation level can help you tune your Java function performance. For small functions that execute quickly, setting the tiered compilation to level 1 can help improve cold start performance by having the JVM use the C1 compiler. This setting quickly produces optimized native code but it doesn't generate any profiling data and never uses the C2 compiler. For larger, computationally-intensive functions, setting tiered compilation to level 4 maximizes overall performance at the expense of additional memory consumption and additional optimization work during the first invokes after each Lambda execution environment is provisioned.

For Java 11 runtimes and below, Lambda uses the default JVM tiered compilation settings. For Java 17 and Java 21, Lambda configures the JVM to stop tiered compilation at level 1 by default. From Java 25, Lambda still stops tiered compilation at level 1 by default, except when using SnapStart or Provisioned concurrency, in which case the default JVM settings are used. This improves performance for SnapStart and Provisioned concurrency without incurring a cold start penalty since tiered compilation is performed outside of the invoke path in these cases. To maximize this benefit, you can use priming - executing code paths during function initialization to trigger JIT before taking the SnapStart snapshot or when Provisioned Concurrency execution environments are pre-provisioned. For further information, see the blog post [Optimizing cold start performance of AWS Lambda using advanced priming strategies with SnapStart](https://aws.amazon.com/blogs/compute/optimizing-cold-start-performance-of-aws-lambda-using-advanced-priming-strategies-with-snapstart/).

**To customize tiered compilation settings (console)**

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions) in the Lambda console.

1. Choose a Java function that you want to customize tiered compilation for.

1. Choose the **Configuration** tab, then choose **Environment variables** in the left menu.

1. Choose **Edit**.

1. Choose **Add environment variable**.

1.  For the key, enter `JAVA_TOOL_OPTIONS`. For the value, enter `-XX:+TieredCompilation -XX:TieredStopAtLevel=1`.   
![Add JAVA_TOOL_OPTIONS environment variable using the Lambda console](http://docs.aws.amazon.com/lambda/latest/dg/images/java-tool-options-tiered-compilation.png)

1. Choose **Save**.

**Note**  
You can also use Lambda SnapStart to mitigate cold start issues. SnapStart uses cached snapshots of your execution environment to significantly improve start-up performance. For more information about SnapStart features, limitations, and supported regions, see [Improving startup performance with Lambda SnapStart](snapstart.md).

### Example: Customizing GC behavior using JAVA\_TOOL\_OPTIONS
<a name="gc-behavior"></a>

Java 11 runtimes use the [ Serial](https://docs.oracle.com/en/java/javase/18/gctuning/available-collectors.html#GUID-45794DA6-AB96-4856-A96D-FDE5F7DEE498) garbage collector (GC) for garbage collection. By default, Java 17 runtimes also use the Serial GC. However, with Java 17 you can also use the `JAVA_TOOL_OPTIONS` environment variable to change the default GC. You can choose between the Parallel GC and [ Shenandoah GC](https://wiki.openjdk.org/display/shenandoah/Main).

For example, if your workload uses more memory and multiple CPUs, consider using the Parallel GC for better performance. You can do this by appending the following to the value of your `JAVA_TOOL_OPTIONS` environment variable:

```
-XX:+UseParallelGC
```

If your workload has many short-lived objects, you may benefit from lower memory consumption by enabling the generational mode of the Shenandoah garbage collector introduced in Java 25. To do this, append the following to the value of your `JAVA_TOOL_OPTIONS` environment variable:

```
-XX:+UseShenandoahGC -XX:ShenandoahGCMode=generational
```

## Log4j patch for Log4Shell
<a name="log4shell-patch"></a>

Lambda runtimes for Java 8, 11, 17, and 21 include a patch to mitigate the Log4Shell vulnerability (CVE-2021-44228) in Log4j, a popular Java logging framework. This patch incurs a cold start performance overhead. If you are using a patched version of Log4j (version 2.17.0 or later), you can disable this patch to improve cold start performance. To disable the patch, set the `AWS_LAMBDA_DISABLE_CVE_2021_44228_PROTECTION` environment variable to `true`.

Starting from Java 25, Lambda runtimes no longer include the Log4Shell patch. You must verify you are using Log4j version 2.17.0 or later.

## Ahead-of-Time (AOT) and CDS caches
<a name="aot-cds-caches"></a>

Starting with Java 25, the Lambda runtime includes an Ahead-of-Time (AOT) cache for the Java runtime interface client (RIC), a runtime component which actively polls for events from the Lambda Runtime API. This improves cold start performance.

AOT caches are specific to a JVM build. When Lambda updates the managed runtime, it also updates the AOT cache for the RIC. However, if you deploy your own AOT caches, these may be invalidated or result in unexpected behavior following a runtime update. We therefore strongly recommend not using AOT caches when using managed runtimes. To use AOT caches, you should deploy your functions using container images.

AOT caches cannot be used with Class Data Sharing (CDS) caches. If you deploy CDS caches in your Lambda function, then Lambda disables the AOT cache.