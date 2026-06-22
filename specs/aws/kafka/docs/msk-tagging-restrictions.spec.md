---
id: "@specs/aws/kafka/docs/msk-tagging-restrictions"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Tag restrictions"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Tag restrictions

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/msk-tagging-restrictions
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Tag restrictions
<a name="msk-tagging-restrictions"></a>

The following restrictions apply to tags in Amazon MSK.

**Basic restrictions**
+ The maximum number of tags per resource is 50.
+ Tag keys and values are case-sensitive.
+ You can't change or edit tags for a deleted resource.

**Tag key restrictions**
+ Each tag key must be unique. If you add a tag with a key that's already in use, your new tag overwrites the existing key-value pair. 
+ You can't start a tag key with `aws:` because this prefix is reserved for use by AWS. AWS creates tags that begin with this prefix on your behalf, but you can't edit or delete them.
+ Tag keys must be between 1 and 128 Unicode characters in length.
+ Tag keys must consist of the following characters: Unicode letters, digits, white space, and the following special characters: `_ . / = + - @`.

**Tag value restrictions**
+ Tag values must be between 0 and 255 Unicode characters in length.
+ Tag values can be blank. Otherwise, they must consist of the following characters: Unicode letters, digits, white space, and any of the following special characters: `_ . / = + - @`.