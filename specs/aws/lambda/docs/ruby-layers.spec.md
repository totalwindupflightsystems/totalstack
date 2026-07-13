---
id: "@specs/aws/lambda/docs/ruby-layers"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Layers"
status: active
depends_on:
  - "@specs/aws/lambda/meta"
---

# Layers

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lambda/docs/ruby-layers
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Working with layers for Ruby Lambda functions
<a name="ruby-layers"></a>

Use [Lambda layers](chapter-layers.md) to package code and dependencies that you want to reuse across multiple functions. Layers usually contain library dependencies, a [custom runtime](runtimes-custom.md), or configuration files. Creating a layer involves three general steps:

1. Package your layer content. This means creating a .zip file archive that contains the dependencies you want to use in your functions.

1. Create the layer in Lambda.

1. Add the layer to your functions.

**Topics**
+ [Package your layer content](#ruby-layers-package)
+ [Create the layer in Lambda](#publishing-layer)
+ [Using gems from layers in a function](#ruby-layers-bundler-limitations)
+ [Add the layer to your function](#ruby-layer-adding)
+ [Sample app](#ruby-layer-sample-app)

## Package your layer content
<a name="ruby-layers-package"></a>

To create a layer, bundle your packages into a .zip file archive that meets the following requirements:
+ Create the layer using the same Ruby version that you plan to use for the Lambda function. For example, if you create your layer for Ruby 4.0, use the Ruby 4.0 runtime for your function.
+ Your layer's .zip file must use one of these directory structures:
  + `ruby/gems/{{x.x.x}}` (where {{x.x.x}} is your Ruby version, for example `3.4.0`)
  + `ruby/lib`

  For more information, see [Layer paths for each Lambda runtime](packaging-layers.md#packaging-layers-paths).
+ The packages in your layer must be compatible with Linux. Lambda functions run on Amazon Linux.

You can create layers that contain either third-party Ruby gems or your own Ruby modules and classes. Many popular Ruby gems contain native extensions (C code) that must be compiled for the Lambda Linux environment.

### Pure Ruby gems
<a name="ruby-layers-pure-ruby-gems"></a>

Pure Ruby gems contain only Ruby code and don't require compilation. These gems are simpler to package and work across different platforms.

**To create a layer using pure Ruby gems**

1. Create a `Gemfile` to specify the pure Ruby gems you want to include in your layer:  
**Example Gemfile**  

   ```
   source 'https://rubygems.org'
   
   gem 'tzinfo'
   ```

1. Install the gems to `vendor/bundle` directory using Bundler:

   ```
   bundle config set --local path vendor/bundle
   bundle install
   ```

1. Copy the installed gems to the directory structure that Lambda requires `ruby/gems/3.4.0`):

   ```
   mkdir -p ruby/gems/3.4.0
   cp -r vendor/bundle/ruby/3.4.0*/* ruby/gems/3.4.0/
   ```

1. Zip the layer content:

------
#### [ Linux/macOS ]

   ```
   zip -r layer.zip ruby/
   ```

------
#### [ PowerShell ]

   ```
   Compress-Archive -Path .\ruby -DestinationPath .\layer.zip
   ```

------

   The directory structure of your .zip file should look like this:

   ```
   ruby/              
   └── gems/
       └── 3.4.0/
           ├── gems/
           │   ├── concurrent-ruby-1.3.5/
           │   └── {{tzinfo-2.0.6/}}
           ├── specifications/
           ├── cache/
           ├── build_info/
           └── (other bundler directories)
   ```
**Note**  
You must require each gem individually in your function code. You can't use `bundler/setup` or `Bundler.require`. For more information, see [Using gems from layers in a function](#ruby-layers-bundler-limitations).

### Gems with native extensions
<a name="ruby-layers-native-extensions"></a>

Many popular Ruby gems contain native extensions (C code) that must be compiled for the target platform. Popular gems with native extensions include [nokogiri](https://rubygems.org/gems/nokogiri/), [pg](https://rubygems.org/gems/pg/), [mysql2](https://rubygems.org/gems/mysql2/), [sqlite3](https://rubygems.org/gems/sqlite3/), and [ffi](https://rubygems.org/gems/ffi/). These gems must be built in a Linux environment that is compatible with the Lambda runtime.

**To create a layer using gems with native extensions**

1. Create a `Gemfile`.  
**Example Gemfile**  

   ```
   source 'https://rubygems.org'
   
   gem 'nokogiri'
   gem 'httparty'
   ```

1. Use Docker to build the gems in a Linux environment that is compatible with Lambda. Specify an [AWS base image](ruby-image.md#ruby-image-base) in your Dockerfile:  
**Example Dockerfile for Ruby 4.0**  

   ```
   FROM {{public.ecr.aws/lambda/ruby:3.4}}
   
   # Copy Gemfile
   COPY Gemfile ./
   
   # Install system dependencies for native extensions
   RUN dnf update -y && \
       dnf install -y gcc gcc-c++ make
   
   # Configure bundler and install gems
   RUN bundle config set --local path vendor/bundle && \
       bundle install
   
   # Create the layer structure
   RUN mkdir -p ruby/gems/3.4.0 && \
       cp -r vendor/bundle/ruby/{{3.4.0}}*/* ruby/gems/{{3.4.0}}/
   
   # Create the layer zip file
   RUN zip -r layer.zip ruby/
   ```

1. Build the image and extract the layer:

   ```
   docker build -t ruby-layer-builder .
   docker run --rm -v $(pwd):/output --entrypoint cp ruby-layer-builder layer.zip /output/
   ```

   This builds the gems in the correct Linux environment and copies the `layer.zip` file to your local directory. The directory structure of your .zip file should look like this:

   ```
   ruby/
   └── gems/
       └── 3.4.0/
           ├── gems/
           │   ├── bigdecimal-3.2.2/
           │   ├── csv-3.3.5/
           │   ├── {{httparty-0.23.1/}}
           │   ├── mini_mime-1.1.5/
           │   ├── multi_xml-0.7.2/
           │   ├── {{nokogiri-1.18.8-x86_64-linux-gnu/}}
           │   └── racc-1.8.1/
           ├── build_info/
           ├── cache/
           ├── specifications/
           └── (other bundler directories)
   ```
**Note**  
You must require each gem individually in your function code. You can't use `bundler/setup` or `Bundler.require`. For more information, see [Using gems from layers in a function](#ruby-layers-bundler-limitations).

### Custom Ruby modules
<a name="custom-ruby-modules"></a>

**To create a layer using your own code**

1. Create the required directory structure for your layer:

   ```
   mkdir -p ruby/lib
   ```

1. Create your Ruby modules in the `ruby/lib` directory. The following example module validates orders by confirming that they contain the required information.  
**Example ruby/lib/order\_validator.rb**  

   ```
   require 'json'
   
   module OrderValidator
     class ValidationError < StandardError; end
   
     def self.validate_order(order_data)
       # Validates an order and returns formatted data
       required_fields = %w[product_id quantity]
       
       # Check required fields
       missing_fields = required_fields.reject { |field| order_data.key?(field) }
       unless missing_fields.empty?
         raise ValidationError, "Missing required fields: #{missing_fields.join(', ')}"
       end
       
       # Validate quantity
       quantity = order_data['quantity']
       unless quantity.is_a?(Integer) && quantity > 0
         raise ValidationError, 'Quantity must be a positive integer'
       end
       
       # Format and return the validated data
       {
         'product_id' => order_data['product_id'].to_s,
         'quantity' => quantity,
         'shipping_priority' => order_data.fetch('priority', 'standard')
       }
     end
   
     def self.format_response(status_code, body)
       # Formats the API response
       {
         statusCode: status_code,
         body: JSON.generate(body)
       }
     end
   end
   ```

1. Zip the layer content:

------
#### [ Linux/macOS ]

   ```
   zip -r layer.zip ruby/
   ```

------
#### [ PowerShell ]

   ```
   Compress-Archive -Path .\ruby -DestinationPath .\layer.zip
   ```

------

   The directory structure of your .zip file should look like this:

   ```
   ruby/              
   └── lib/
       └── order_validator.rb
   ```

1. In your function, require and use the modules. You must require each gem individually in your function code. You can't use `bundler/setup` or `Bundler.require`. For more information, see [Using gems from layers in a function](#ruby-layers-bundler-limitations). Example:

   ```
   require 'json'
   require 'order_validator'
   
   def lambda_handler(event:, context:)
     begin
       # Parse the order data from the event body
       order_data = JSON.parse(event['body'] || '{}')
       
       # Validate and format the order
       validated_order = OrderValidator.validate_order(order_data)
       
       OrderValidator.format_response(200, {
         message: 'Order validated successfully',
         order: validated_order
       })
     rescue OrderValidator::ValidationError => e
       OrderValidator.format_response(400, {
         error: e.message
       })
     rescue => e
       OrderValidator.format_response(500, {
         error: 'Internal server error'
       })
     end
   end
   ```

   You can use the following [test event](testing-functions.md#invoke-with-event) to invoke the function:

   ```
   {
       "body": "{\"product_id\": \"ABC123\", \"quantity\": 2, \"priority\": \"express\"}"
   }
   ```

   Expected response:

   ```
   {
     "statusCode": 200,
     "body": "{\"message\":\"Order validated successfully\",\"order\":{\"product_id\":\"ABC123\",\"quantity\":2,\"shipping_priority\":\"express\"}}"
   }
   ```

## Create the layer in Lambda
<a name="publishing-layer"></a>

You can publish your layer using either the AWS CLI or the Lambda console.

------
#### [ AWS CLI ]

Run the [publish-layer-version](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/publish-layer-version.html) AWS CLI command to create the Lambda layer:

```
aws lambda publish-layer-version --layer-name {{my-layer}} --zip-file fileb://layer.zip --compatible-runtimes {{ruby4.0}}
```

The [compatible runtimes](https://docs.aws.amazon.com/lambda/latest/api/API_PublishLayerVersion.html#lambda-PublishLayerVersion-request-CompatibleRuntimes) parameter is optional. When specified, Lambda uses this parameter to filter layers in the Lambda console.

------
#### [ Console ]

**To create a layer (console)**

1. Open the [Layers page](https://console.aws.amazon.com/lambda/home#/layers) of the Lambda console.

1. Choose **Create layer**.

1. Choose **Upload a .zip file**, and then upload the .zip archive that you created earlier.

1. (Optional) For **Compatible runtimes**, choose the Ruby runtime that corresponds to the Ruby version you used to build your layer.

1. Choose **Create**.

------

## Using gems from layers in a function
<a name="ruby-layers-bundler-limitations"></a>

In your function code, you must explicitly require each gem that you want to use. Bundler commands such as `bundler/setup` and `Bundler.require` are not supported. Here's how to properly use gems from a layer in a Lambda function:

```
# Correct: Use explicit requires for each gem
require 'nokogiri'
require 'httparty'

def lambda_handler(event:, context:)
  # Use the gems directly
  doc = Nokogiri::HTML(event['html'])
  response = HTTParty.get(event['url'])
  # ... rest of your function
end

# Incorrect: These Bundler commands will not work
# require 'bundler/setup'
# Bundler.require
```

## Add the layer to your function
<a name="ruby-layer-adding"></a>

------
#### [ AWS CLI ]

To attach the layer to your function, run the [update-function-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/update-function-configuration.html) AWS CLI command. For the `--layers` parameter, use the layer ARN. The ARN must specify the version (for example, `arn:aws:lambda:us-east-1:123456789012:layer:my-layer:{{1}}`). For more information, see [Layers and layer versions](chapter-layers.md#lambda-layer-versions).

```
aws lambda update-function-configuration --function-name {{my-function}} --cli-binary-format raw-in-base64-out --layers "{{arn:aws:lambda:us-east-1:123456789012:layer:my-layer:{{1}}}}"
```

The **cli-binary-format** option is required if you're using AWS CLI version 2. To make this the default setting, run `aws configure set cli-binary-format raw-in-base64-out`. For more information, see [AWS CLI supported global command line options](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-options.html#cli-configure-options-list) in the *AWS Command Line Interface User Guide for Version 2*.

------
#### [ Console ]

**To add a layer to a function**

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions) of the Lambda console.

1. Choose the function.

1. Scroll down to the **Layers** section, and then choose **Add a layer**.

1. Under **Choose a layer**, select **Custom layers**, and then choose your layer.
**Note**  
If you didn't add a [compatible runtime](https://docs.aws.amazon.com/lambda/latest/api/API_PublishLayerVersion.html#lambda-PublishLayerVersion-request-CompatibleRuntimes) when you created the layer, your layer won't be listed here. You can specify the layer ARN instead.

1. Choose **Add**.

------

## Sample app
<a name="ruby-layer-sample-app"></a>

For more examples of how to use Lambda layers, see the [layer-ruby](https://github.com/awsdocs/aws-lambda-developer-guide/tree/main/sample-apps/layer-ruby) sample application in the AWS Lambda Developer Guide GitHub repository. This application includes a layer that contains the [tzinfo](https://rubygems.org/gems/tzinfo) library. After creating the layer, you can deploy and invoke the corresponding function to confirm that the layer works as expected.