---
id: "@specs/aws/appconfig/docs/appconfig-creating-multi-variant-feature-flags-rules-operators"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Defining rules for multi-variant feature flags"
status: active
depends_on:
  - "@specs/aws/appconfig/meta"
---

# Defining rules for multi-variant feature flags

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appconfig/docs/appconfig-creating-multi-variant-feature-flags-rules-operators
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Defining rules for multi-variant feature flags
<a name="appconfig-creating-multi-variant-feature-flags-rules-operators"></a>

A variant rule is an expression comprised of one or more operands and an operator. An operand is a specific value used during the evaluation of a rule. Operand values can be either static, such as a literal number or string, or variable, such as the value found in a context or the result of another expression. An operator, such as "greater than", is a test or action applied to its operands that produces a value. A variant rule expression must produce either a "true" or "false" to be valid.

**Operands**


****  

| Type | Description | Example | 
| --- | --- | --- | 
| String | A sequence of UTF-8 characters, enclosed in double-quotes. |  <pre>"apple", "Ḽơᶉëᶆ ȋṕšᶙṁ"</pre>  | 
| Integer | A 64-bit integer value. |  <pre>-7, 42 </pre>  | 
| Float | A 64-bit IEEE-754 floating-point value. |  <pre>3.14, 1.234e-5</pre>  | 
| Timestamp | A specific moment in time as described by the [W3C note on date and time formats](https://www.w3.org/TR/NOTE-datetime). |  <pre>2012-03-04T05:06:07-08:00, 2024-01</pre>  | 
| Boolean | A true or false value. |  <pre>true, false</pre>  | 
| Context value | A parameterized value in the form of ${{key}} that is retrieved from the context during rule evaluation. |  <pre>$country, $userId</pre>  | 

**Comparison operators**


****  

| Operator | Description | Example | 
| --- | --- | --- | 
| eq | Determines whether a context value is equal to a given value. |  <pre>(eq $state "Virginia")</pre>  | 
| gt | Determines whether a context value is greater than a given value. |  <pre>(gt $age 65)</pre>  | 
| gte | Determines whether a context value is greater than or equal to a given value. |  <pre>(gte $age 65)</pre>  | 
| lt | Determines whether a context value is less than a given value. |  <pre>(lt $age 65)</pre>  | 
| lte | Determines whether a context value is less than or equal to a given value. |  <pre>(lte $age 65)</pre>  | 

**Logical operators**


****  

| Operator | Description | Example | 
| --- | --- | --- | 
| and | Determines if both operands are true. |  <pre>(and <br />    (eq $state "Virginia") <br />    (gt $age 65)<br />)</pre>  | 
| or | Determines if at least one of the operands is true. |  <pre>(or<br />    (eq $state "Virginia") <br />    (gt $age 65)<br />)</pre>  | 
| not | Reverses the value of an expression. |  <pre>(not (eq $state "Virginia"))</pre>  | 

**Custom operators**


****  

| Operator | Description | Example | 
| --- | --- | --- | 
| begins\_with | Determines whether a context value begins with a given prefix. |  <pre>(begins_with $state "A")</pre>  | 
| ends\_with | Determines whether a context value ends with a given prefix. |  <pre>(ends_with $email "amazon.com")</pre>  | 
| contains | Determines whether a context value contains a given substring. |  <pre>(contains $promoCode "WIN")</pre>  | 
| in | Determines whether a context value is contained within a list of constants. |  <pre>(in $userId ["123", "456"])</pre>  | 
| matches | Determines whether a context value matches a given regex pattern. |  <pre>(matches in::$greeting pattern::"h.*y")</pre>  | 
| exists | Determines whether any value was provided for a context key. |  <pre>(exists key::"country")</pre>  | 
| split | Evaluates to `true` for a given percentage of traffic based on a consistent hash of the provided context value(s). For a detailed explanation of how `split` works, see the next section in this topic, [Understanding the split operator](appconfig-creating-multi-variant-feature-flags-rules.md#appconfig-creating-multi-variant-feature-flags-rules-operators-split).<br />Note that `seed` is an optional property. If you don't specify `seed`, the hash is *locally* consistent, meaning traffic will be split consistently for that flag, but other flags receiving the same context value may split traffic differently. If `seed` is provided, each unique value is guaranteed to split traffic consistently across feature flags, configuration profiles, and AWS accounts. |  <pre>(split pct::10 by::$userId seed::"abc")</pre>  | 