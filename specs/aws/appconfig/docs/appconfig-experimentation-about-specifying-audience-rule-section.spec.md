---
id: "@specs/aws/appconfig/docs/appconfig-experimentation-about-specifying-audience-rule-section"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Creating audience rules"
status: active
depends_on:
  - "@specs/aws/appconfig/meta"
---

# Creating audience rules

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appconfig/docs/appconfig-experimentation-about-specifying-audience-rule-section
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Creating audience rules
<a name="appconfig-experimentation-about-specifying-audience-rule-section"></a>

The **Audience rule** section includes a **Rule builder** tab and an **Editor** tab for creating rules to target an audience for the experiment.

**Topics**
+ [Using the audience rule builder](#appconfig-experimentation-about-specifying-audience-rule-builder)
+ [Using the editor](#appconfig-experimentation-about-specifying-audience-editor)

## Using the audience rule builder
<a name="appconfig-experimentation-about-specifying-audience-rule-builder"></a>

The rule builder provides a visual interface for defining audience targeting rules without writing expressions. You can create conditions using attributes and combine them with logical operators to control which users are included in the experiment. In the rule builder, you define rules by combining conditions and groups:
+ Conditions evaluate a single attribute (for example, `$plan equals "enterprise"`).
+ Groups combine multiple conditions using logical operators such as `AND` or `OR`.

Each group evaluates to either `true` or `false`. Users who match the overall rule are included in the target audience.

Use the rule builder when you want to:
+ Quickly define or modify audience rules without writing expressions
+ Visualize how conditions are grouped and evaluated
+ Build and validate targeting logic incrementally

Here are some examples:

**A rule for targeting users in the Premium account tier.**

![An image of the Rule builder tab in AWS AppConfig experimentation with sample audience rule specified.](http://docs.aws.amazon.com/appconfig/latest/userguide/images/experimentation-rule-builder-1.png)


**A rule for targeting users in a specific geographic region using a specific email domain.**

![A second image of the Rule builder tab in AWS AppConfig experimentation with sample audience rule specified.](http://docs.aws.amazon.com/appconfig/latest/userguide/images/experimentation-rule-builder-2.png)


**A rule for targeting users in a specific on a specific plan or using a secondary plan while having opted into a beta program.**

![A third image of the Rule builder tab in AWS AppConfig experimentation with sample audience rule specified.](http://docs.aws.amazon.com/appconfig/latest/userguide/images/experimentation-rule-builder-3.png)


**Relationship to the editor**

The rule builder and the editor define the same targeting logic in different formats:
+ The rule builder provides a visual way to construct rules.
+ The editor shows the equivalent logical expression.

Changes made in one view are reflected in the other.

**Best practices**
+ Keep rules readable – Use groups to organize conditions logically and avoid deeply nested structures.
+ Validate attribute values – Ensure that attribute names and values match those provided by your application.
+ Test before exposure – Use 0% exposure and treatment assignment overrides to confirm that your rules behave as expected.

## Using the editor
<a name="appconfig-experimentation-about-specifying-audience-editor"></a>

The editor lets you define targeting rules that determine which users are included in an experiment. You specify these rules as logical expressions that evaluate user or device attributes, such as platform, region, or application version. When an experiment runs, AWS AppConfig evaluates the expression for each user. Users who match the criteria are included in the target audience and can be assigned to treatments.

**Expression format**

Expressions use a prefix (function-style) syntax:

```
(operator argument1 argument2 ...)
```

For example:

```
(and
    (eq $system "iPhone")
    (lt $osVersion 1.8)
)
```

This expression includes users who:
+ Use an iPhone, and
+ Have an operating system version earlier than 1.8

The editor supports the same targeting scenarios as the rule builder. For visual examples of audience rules, see [Using the audience rule builder](#appconfig-experimentation-about-specifying-audience-rule-builder).

**Defining attributes**

Attributes represent properties of the user or environment being evaluated. Attributes are referenced with a `$` prefix.

Common examples include:
+ `$system` – device or platform type
+ `$osVersion` – operating system version
+ `$region` – geographic region
+ `$appVersion` – application version

The available attributes depend on your application and how data is passed to AWS AppConfig.

**Writing expressions**

You can combine multiple conditions using logical operators:
+ Use `and` to require all conditions to be true
+ Use `or` to match any condition
+ Use `not` to exclude conditions

Example:

```
(and
    (eq $region "us-east-1")
    (or
        (eq $system "iPhone")
        (eq $system "Android")
    )
)
```

This expression targets users in `us-east-1` who are using either iPhone or Android devices.

**Best practices**
+ Start simple – Begin with a small set of conditions and expand as needed.
+ Validate attributes – Ensure that the attributes used in expressions are consistently populated.
+ Avoid overly complex expressions – Complex logic can make targeting harder to understand and maintain.
+ Test before exposure – Use 0% exposure and treatment assignment overrides to confirm that your rules behave as expected.

**Expression operators**

The following operators are supported in audience expressions.

Logical operators


****  

| Operator | Description | Example | 
| --- | --- | --- | 
| and | Returns true if all conditions are true | `(and (eq $region "us") (eq $system "iPhone"))` | 
| or | Returns true if any condition is true | `(or (eq $system "iPhone") (eq $system "Android"))` | 
| not | Returns true if the condition is false | `(not (eq $region "eu-west-1"))` | 

Comparison operators


****  

| Operator | Description | Example | 
| --- | --- | --- | 
| eq | Equals | `(eq $system "iPhone")` | 
| ne | Not equal | `(ne $region "us-west-2")` | 
| lt | Less than | `(lt $osVersion 1.8)` | 
| lte | Less than or equal | `(lte $osVersion 2.0)` | 
| gt | Greater than | `(gt $appVersion 5.0)` | 
| gte | Greater than or equal | `(gte $appVersion 5.0)` | 

String and set operators


****  

| Operator | Description | Example | 
| --- | --- | --- | 
| in | Matches any value in a list | `(in $region ["us-east-1" "us-west-2"])` | 
| contains | Checks if a value contains a substring | `(contains $deviceName "iPhone")` | 

**Note**  
Available operators may vary depending on how attributes are defined and evaluated in your application.