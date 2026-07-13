---
id: "@specs/aws/lambda/docs/python-layers"
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
> **spec:id:** @specs/aws/lambda/docs/python-layers
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Working with layers for Python Lambda functions
<a name="python-layers"></a>

Use [Lambda layers](chapter-layers.md) to package code and dependencies that you want to reuse across multiple functions. Layers usually contain library dependencies, a [custom runtime](runtimes-custom.md), or configuration files. Creating a layer involves three general steps:

1. Package your layer content. This means creating a .zip file archive that contains the dependencies you want to use in your functions.

1. Create the layer in Lambda.

1. Add the layer to your functions.

**Topics**
+ [Package your layer content](#python-layers-package)
+ [Create the layer in Lambda](#publishing-layer)
+ [Add the layer to your function](#python-layer-adding)
+ [Sample app](#python-layer-sample-app)

## Package your layer content
<a name="python-layers-package"></a>

To create a layer, bundle your packages into a .zip file archive that meets the following requirements:
+ Build the layer using the same Python version that you plan to use for the Lambda function. For example, if you build your layer using Python 3.14, use the Python 3.14 runtime for your function.
+ Your .zip file must include a `python` directory at the root level.
+ The packages in your layer must be compatible with Linux. Lambda functions run on Amazon Linux.

You can create layers that contain either third-party Python libraries installed with `pip` (such as `requests` or `pandas`) or your own Python modules and packages.

### Third-party dependencies
<a name="python-layers-third-party-dependencies"></a>

**To create a layer using pip packages**

1. Choose one of the following methods to install `pip` packages into the required top-level directory (`python/`):

------
#### [ pip install ]

   For pure Python packages (like requests or boto3):

   ```
   pip install requests -t python/
   ```

   Some Python packages, such as NumPy and Pandas, include compiled C components. If you're building a layer with these packages on macOS or Windows, you might need to use this command to install a Linux-compatible wheel:

   ```
   pip install numpy --platform manylinux2014_x86_64 --only-binary=:all: -t python/
   ```

   For more information about working with Python packages that contain compiled components, see [Creating .zip deployment packages with native libraries](python-package.md#python-package-native-libraries).

------
#### [ requirements.txt ]

   Using a `requirements.txt` file helps you manage package versions and ensure consistent installations.

**Example requirements.txt**  

   ```
   requests==2.31.0
   boto3==1.37.34
   numpy==1.26.4
   ```

   If your `requirements.txt` file includes only pure Python packages (like requests or boto3):

   ```
   pip install -r requirements.txt -t python/
   ```

   Some Python packages, such as NumPy and Pandas, include compiled C components. If you're building a layer with these packages on macOS or Windows, you might need to use this command to install a Linux-compatible wheel:

   ```
   pip install -r requirements.txt --platform manylinux2014_x86_64 --only-binary=:all: -t python/
   ```

   For more information about working with Python packages that contain compiled components, see [Creating .zip deployment packages with native libraries](python-package.md#python-package-native-libraries).

------

1. Zip the contents of the `python` directory.

------
#### [ Linux/macOS ]

   ```
   zip -r layer.zip python/
   ```

------
#### [ PowerShell ]

   ```
   Compress-Archive -Path .\python -DestinationPath .\layer.zip
   ```

------

   The directory structure of your .zip file should look like this:

   ```
   {{python/}}              # Required top-level directory
   └── requests/
   └── boto3/
   └── numpy/
   └── (dependencies of the other packages)
   ```
**Note**  
If you use a Python virtual environment (venv) to install packages, your directory structure will be different (for example, `python/lib/python3.{{x}}/site-packages`). As long as your .zip file includes the `python` directory at the root level, Lambda can locate and import your packages.

### Custom Python modules
<a name="custom-python-modules"></a>

**To create a layer using your own code**

1. Create the required top-level directory for your layer:

   ```
   mkdir python
   ```

1. Create your Python modules in the `python` directory. The following example module validates orders by confirming that they contain the required information.  
**Example custom module: validator.py**  

   ```
   import json
   
   def validate_order(order_data):
       """Validates an order and returns formatted data."""
       required_fields = ['product_id', 'quantity']
       
       # Check required fields
       missing_fields = [field for field in required_fields if field not in order_data]
       if missing_fields:
           raise ValueError(f"Missing required fields: {', '.join(missing_fields)}")
       
       # Validate quantity
       quantity = order_data['quantity']
       if not isinstance(quantity, int) or quantity < 1:
           raise ValueError("Quantity must be a positive integer")
       
       # Format and return the validated data
       return {
           'product_id': str(order_data['product_id']),
           'quantity': quantity,
           'shipping_priority': order_data.get('priority', 'standard')
       }
   
   def format_response(status_code, body):
       """Formats the API response."""
       return {
           'statusCode': status_code,
           'body': json.dumps(body)
       }
   ```

1. Zip the contents of the `python` directory.

------
#### [ Linux/macOS ]

   ```
   zip -r layer.zip python/
   ```

------
#### [ PowerShell ]

   ```
   Compress-Archive -Path .\python -DestinationPath .\layer.zip
   ```

------

   The directory structure of your .zip file should look like this:

   ```
   {{python/}}     # Required top-level directory
   └── validator.py
   ```

1. In your function, import and use the modules as you would with any Python package. Example:

   ```
   from validator import validate_order, format_response
   import json
   
   def lambda_handler(event, context):
       try:
           # Parse the order data from the event body
           order_data = json.loads(event.get('body', '{}'))
           
           # Validate and format the order
           validated_order = validate_order(order_data)
           
           return format_response(200, {
               'message': 'Order validated successfully',
               'order': validated_order
           })
       except ValueError as e:
           return format_response(400, {
               'error': str(e)
           })
       except Exception as e:
           return format_response(500, {
               'error': 'Internal server error'
           })
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
     "body": "{\"message\": \"Order validated successfully\", \"order\": {\"product_id\": \"ABC123\", \"quantity\": 2, \"shipping_priority\": \"express\"}}"
   }
   ```

## Create the layer in Lambda
<a name="publishing-layer"></a>

You can publish your layer using either the AWS CLI or the Lambda console.

------
#### [ AWS CLI ]

Run the [publish-layer-version](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/publish-layer-version.html) AWS CLI command to create the Lambda layer:

```
aws lambda publish-layer-version --layer-name {{my-layer}} --zip-file fileb://layer.zip --compatible-runtimes {{python3.14}}
```

The [compatible runtimes](https://docs.aws.amazon.com/lambda/latest/api/API_PublishLayerVersion.html#lambda-PublishLayerVersion-request-CompatibleRuntimes) parameter is optional. When specified, Lambda uses this parameter to filter layers in the Lambda console.

------
#### [ Console ]

**To create a layer (console)**

1. Open the [Layers page](https://console.aws.amazon.com/lambda/home#/layers) of the Lambda console.

1. Choose **Create layer**.

1. Choose **Upload a .zip file**, and then upload the .zip archive that you created earlier.

1. (Optional) For **Compatible runtimes**, choose the Python runtime that corresponds to the Python version you used to build your layer.

1. Choose **Create**.

------

## Add the layer to your function
<a name="python-layer-adding"></a>

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
<a name="python-layer-sample-app"></a>

For more examples of how to use Lambda layers, see the [layer-python](https://github.com/awsdocs/aws-lambda-developer-guide/tree/main/sample-apps/layer-python) sample application in the AWS Lambda Developer Guide GitHub repository. This application includes two layers that contain Python libraries. After creating the layers, you can deploy and invoke the corresponding functions to confirm that the layers work as expected.