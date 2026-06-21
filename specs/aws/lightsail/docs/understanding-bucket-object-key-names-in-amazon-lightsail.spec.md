---
id: "@specs/aws/lightsail/docs/understanding-bucket-object-key-names-in-amazon-lightsail"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Object key names"
status: active
depends_on:
  - "@specs/aws/lightsail/meta"
---

# Object key names

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lightsail/docs/understanding-bucket-object-key-names-in-amazon-lightsail
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Key names for Lightsail object storage buckets
<a name="understanding-bucket-object-key-names-in-amazon-lightsail"></a>

Files that you upload to your bucket are stored as objects in the Amazon Lightsail object storage service. An object key (or key name) uniquely identifies an object stored in a bucket. This guide explains the concept of key names and key name prefixes that make up the folder structure of buckets viewed through the Lightsail console. For more information about buckets, see [Object storage](buckets-in-amazon-lightsail.md).

## Key names
<a name="bucket-object-key-names"></a>

The Lightsail object storage service data model uses a flat structure instead of a hierarchical structure like you would see in a file system. There is no hierarchy of folders and subfolders. However, you can infer logical hierarchy using key name prefixes and delimiters. The Lightsail console uses the key name prefixes to display your objects in a folder structure.

Suppose that your bucket has four objects with the following object keys:
+ `Development/Projects.xls`
+ `Finance/statement1.pdf`
+ `Private/taxdocument.pdf`
+ `to-dos.doc`

The Lightsail console uses the key name prefixes (`Development/`, `Finance/`, and `Private/`) and the delimiter (`/`) to present a folder structure. The `to-dos.doc` key name does not have a prefix, so its object appears directly at the root level of your bucket. If you browse to the `Development/` folder in the Lightsail console, you see the `Projects.xls` object. In the `Finance/` folder, you see the `statement1.pdf` object, and in the `Private/` folder, you see the `taxdocument.pdf` object.

The Lightsail console allows for folder creation by creating a zero-byte object with the key name prefix and delimiter value as the key name. These folder objects don't appear in the console. However, they behave like any other objects. You can view and manipulate them using the Amazon S3 API, AWS Command Line Interface (AWS CLI), or AWS SDKs.

## Object key naming guidelines
<a name="object-key-naming-guidelines"></a>

You can use any UTF-8 character in an object key name. However, using certain characters in key names can cause problems with some applications and protocols. The following guidelines help you maximize compliance with DNS, web-safe characters, XML parsers, and other APIs.

### Safe characters
<a name="w2aac59c37b7b5"></a>

The following character sets are generally safe for use in key names.
+ Alphanumeric characters
  + 0-9
  + a-z
  + A-Z
+ Special characters
  + Forward slash (`/`)
  + Exclamation point (`!`)
  + Hyphen (`-`)
  + Underscore (`_`)
  + Period (`.`)
  + Asterisk (`*`)
  + Single quote (`'`)
  + Open parenthesis (`(`)
  + Close parenthesis (`)`)

The following are examples of valid object key names:
+ `4my-organization`
+ `my.great_photos-2014/jan/myvacation.jpg`
+ `videos/2014/birthday/video1.wmv`

**Important**  
If an object key name ends with a single period (.), or two periods (..), you can’t download the object using the Lightsail console. To download an object with a key name ending with one or two periods, you must use the Amazon S3 API, AWS CLI, and AWS SDKs. For more information, see [Download bucket objects](amazon-lightsail-downloading-bucket-objects.md).

### Characters that might require special handling
<a name="asdf"></a>

The following characters in a key name might require additional code handling and likely need to be URL encoded or referenced as HEX. Some of these are non-printable characters that your browser might not handle, which also requires special handling:
+ Ampersand ("`&`")
+ Dollar ("`$`")
+ ASCII character ranges 00–1F hex (0–31 decimal) and 7F (127 decimal)
+ 'At' symbol ("`@`")
+ Equals ("`=`")
+ Semicolon ("`;`")
+ Colon ("`:`")
+ Plus ("`+`")
+ Space – Significant sequences of spaces might be lost in some uses (especially multiple spaces)
+ Comma ("`,`")
+ Question mark ("`?`")

### Characters to avoid
<a name="key-name-characters-to-avoid"></a>

Avoid the following characters in a key name because of significant special handling for consistency across all applications.
+ Backslash ("`\`")
+ Left curly brace ("`{`")
+ Non-printable ASCII characters (128–255 decimal characters)
+ Caret ("`^`")
+ Right curly brace ("`}`")
+ Percent character ("`%`")
+ Grave accent / back tick ("```")
+ Right square bracket ("`]`")
+ Quotation marks
+ 'Greater than' symbol ("`>`")
+ Left square bracket ("`[`")
+ Tilde ("`~`")
+ 'Less than' symbol ("`<`")
+ 'Pound' character ("`#`")
+ Vertical bar / pipe ("`|`")

## XML related object key constraints
<a name="xml-object-key-constraints"></a>

As specified by the [XML standard on end-of-line handling](https://www.w3.org/TR/REC-xml/#sec-line-ends), all XML text is normalized so that single carriage returns (ASCII code 13) and carriage returns immediately followed by a line feed (ASCII code 10) are replaced by a single line feed character. To ensure the correct parsing of object keys in XML requests, carriage returns and [other special characters must be replaced with their equivalent XML entity code](https://www.w3.org/TR/xml/#syntax) when they are inserted within XML tags. The following is a list of such special characters and their equivalent entity codes:
+ `'` as `&apos;`
+ `”` as `&quot;`
+ `&` as `&amp;`
+ `<` as `&lt;`
+ `<` as `&gt;`
+ `\r` as `&#13;` or `&#x0D;`
+ `\n` as `&#10;` or `&#x0A;`

The following example illustrates the use of an XML entity code as a substitution for a carriage return. This `DeleteObjects` request deletes an object with the key parameter `/some/prefix/objectwith\rcarriagereturn` (where the \\r is the carriage return).

```
<Delete xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
      <Object>
        <Key>/some/prefix/objectwith&#13;carriagereturn</Key>
      </Object>
    </Delete>
```