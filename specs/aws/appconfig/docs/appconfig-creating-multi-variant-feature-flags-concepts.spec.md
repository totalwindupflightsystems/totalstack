---
id: "@specs/aws/appconfig/docs/appconfig-creating-multi-variant-feature-flags-concepts"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Understanding multi-variant feature flag concepts and common use cases"
status: active
depends_on:
  - "@specs/aws/appconfig/meta"
---

# Understanding multi-variant feature flag concepts and common use cases

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appconfig/docs/appconfig-creating-multi-variant-feature-flags-concepts
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Understanding multi-variant feature flag concepts and common use cases
<a name="appconfig-creating-multi-variant-feature-flags-concepts"></a>

To help you better understand feature flag variants, this section explains flag variant concepts and common use cases.

**Concepts**
+ **Feature flag**: An AWS AppConfig configuration type used to control the behavior of a feature in an application. A flag has a status (enabled or disabled) and an optional set of attributes containing arbitrary string, numeric, boolean, or array values.
+ **Feature flag variant**: A specific combination of status and attribute values belonging to a feature flag. A feature flag may have multiple variants.
+ **Variant rule**: A user-defined expression used to select a feature flag variant. Each variant has its own rule that AWS AppConfig evaluates to determine whether to return it or not.
+ **Default variant**: A special variant that is returned when no other variant is selected. All multi-variant feature flags have a default variant.

  Note, the default variant must be last in your ordering of variants, and it can't have rules associated with it. If it's not defined last, AWS AppConfig returns a `BadRequestException` when you try to create the multi-variant flag.
+ **Context**: User-defined keys and values passed to AWS AppConfig at configuration retrieval time. Context values are used during rule evaluation to select the feature flag variant to return.

**Note**  
AWS AppConfig agent evaluates variant rules and determines which rule applies to the request based on the provided context. For more information about retrieving multi-varient feature flags, see [Retrieving basic and multi-variant feature flags](appconfig-integration-retrieving-feature-flags.md).

**Common use cases**

This section describes two common use cases for feature flag variants.

*User segmentation*

User segmentation is the process of dividing users based on certain attributes. As an example, you could use flag variants to expose a feature to some users but not others based on their user ID, geographic location, device type, or purchase frequency.

Using the example of purchase frequency, suppose your commerce application supports a feature to increase customer loyalty. You can use flag variants to configure different incentive types to be shown to a user based on when they last purchased something. A new user might be offered a small discount to encourage them to become a customer, whereas a repeat customer might be given a larger discount if they purchase something from a new category.

*Traffic splitting*

Traffic splitting is the process of selecting a random, but consistent, flag variant based on a context value you define. For example, you may want to perform an experiment where a small percentage of your users (identified by their user ID) sees a particular variant. Or, you may want to execute a gradual feature rollout where a feature is first exposed to 5% of your users, then 15%, then 40%, then 100%, while maintaining a consistent user experience throughout the rollout.

Using the experimentation example, you could use flag variants to test a new button style for the primary action on your application homepage to see if it drives more clicks. For your experiment, you could create a flag variant with a traffic splitting rule that selects 5% of users to see the new style, while the default variant indicates the users that should continue to see the existing style. If the experiment is successful, you can increase the percentage value, or even turn that variant into the default.