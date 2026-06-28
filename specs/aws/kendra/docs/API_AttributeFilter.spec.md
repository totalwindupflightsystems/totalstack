---
id: "@specs/aws/kendra/docs/API_AttributeFilter"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AttributeFilter"
status: active
depends_on:
  - "@specs/aws/kendra/meta"
---

# AttributeFilter

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kendra/docs/API_AttributeFilter
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AttributeFilter
<a name="API_AttributeFilter"></a>

Filters the search results based on document attributes or fields.

You can filter results using attributes for your particular documents. The attributes must exist in your index. For example, if your documents include the custom attribute "Department", you can filter documents that belong to the "HR" department. You would use the `EqualsTo` operation to filter results or documents with "Department" equals to "HR".

You can use `AndAllFilters` and `OrAllFilters` in combination with each other or with other operations such as `EqualsTo`. For example:

 `AndAllFilters` 
+  `EqualsTo`: "Department", "HR"
+  `OrAllFilters` 
  +  `ContainsAny`: "Project Name", ["new hires", "new hiring"]

This example filters results or documents that belong to the HR department `AND` belong to projects that contain "new hires" `OR` "new hiring" in the project name (must use `ContainAny` with `StringListValue`). This example is filtering with a depth of 2.

You cannot filter more than a depth of 2, otherwise you receive a `ValidationException` exception with the message "AttributeFilter cannot have a depth of more than 2." Also, if you use more than 10 attribute filters in a given list for `AndAllFilters` or `OrAllFilters`, you receive a `ValidationException` with the message "AttributeFilter cannot have a length of more than 10".

For examples of using `AttributeFilter`, see [Using document attributes to filter search results](https://docs.aws.amazon.com/kendra/latest/dg/filtering.html#search-filtering).

## Contents
<a name="API_AttributeFilter_Contents"></a>

 ** AndAllFilters **   <a name="kendra-Type-AttributeFilter-AndAllFilters"></a>
Performs a logical `AND` operation on all filters that you specify.  
Type: Array of [AttributeFilter](#API_AttributeFilter) objects  
Required: No

 ** ContainsAll **   <a name="kendra-Type-AttributeFilter-ContainsAll"></a>
Returns true when a document contains all of the specified document attributes/fields. This filter is only applicable to [StringListValue](https://docs.aws.amazon.com/kendra/latest/APIReference/API_DocumentAttributeValue.html).  
Type: [DocumentAttribute](API_DocumentAttribute.md) object  
Required: No

 ** ContainsAny **   <a name="kendra-Type-AttributeFilter-ContainsAny"></a>
Returns true when a document contains any of the specified document attributes/fields. This filter is only applicable to [StringListValue](https://docs.aws.amazon.com/kendra/latest/APIReference/API_DocumentAttributeValue.html).  
Type: [DocumentAttribute](API_DocumentAttribute.md) object  
Required: No

 ** EqualsTo **   <a name="kendra-Type-AttributeFilter-EqualsTo"></a>
Performs an equals operation on document attributes/fields and their values.  
Type: [DocumentAttribute](API_DocumentAttribute.md) object  
Required: No

 ** GreaterThan **   <a name="kendra-Type-AttributeFilter-GreaterThan"></a>
Performs a greater than operation on document attributes/fields and their values. Use with the [document attribute type](https://docs.aws.amazon.com/kendra/latest/APIReference/API_DocumentAttributeValue.html) `Date` or `Long`.  
Type: [DocumentAttribute](API_DocumentAttribute.md) object  
Required: No

 ** GreaterThanOrEquals **   <a name="kendra-Type-AttributeFilter-GreaterThanOrEquals"></a>
Performs a greater or equals than operation on document attributes/fields and their values. Use with the [document attribute type](https://docs.aws.amazon.com/kendra/latest/APIReference/API_DocumentAttributeValue.html) `Date` or `Long`.  
Type: [DocumentAttribute](API_DocumentAttribute.md) object  
Required: No

 ** LessThan **   <a name="kendra-Type-AttributeFilter-LessThan"></a>
Performs a less than operation on document attributes/fields and their values. Use with the [document attribute type](https://docs.aws.amazon.com/kendra/latest/APIReference/API_DocumentAttributeValue.html) `Date` or `Long`.  
Type: [DocumentAttribute](API_DocumentAttribute.md) object  
Required: No

 ** LessThanOrEquals **   <a name="kendra-Type-AttributeFilter-LessThanOrEquals"></a>
Performs a less than or equals operation on document attributes/fields and their values. Use with the [document attribute type](https://docs.aws.amazon.com/kendra/latest/APIReference/API_DocumentAttributeValue.html) `Date` or `Long`.  
Type: [DocumentAttribute](API_DocumentAttribute.md) object  
Required: No

 ** NotFilter **   <a name="kendra-Type-AttributeFilter-NotFilter"></a>
Performs a logical `NOT` operation on all filters that you specify.  
Type: [AttributeFilter](#API_AttributeFilter) object  
Required: No

 ** OrAllFilters **   <a name="kendra-Type-AttributeFilter-OrAllFilters"></a>
Performs a logical `OR` operation on all filters that you specify.  
Type: Array of [AttributeFilter](#API_AttributeFilter) objects  
Required: No

## See Also
<a name="API_AttributeFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kendra-2019-02-03/AttributeFilter) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kendra-2019-02-03/AttributeFilter) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kendra-2019-02-03/AttributeFilter) 