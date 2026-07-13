---
id: "@specs/aws/lambda/docs/nodejs-layers"
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
> **spec:id:** @specs/aws/lambda/docs/nodejs-layers
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Working with layers for Node.js Lambda functions
<a name="nodejs-layers"></a>

Use [Lambda layers](chapter-layers.md) to package code and dependencies that you want to reuse across multiple functions. Layers usually contain library dependencies, a [custom runtime](runtimes-custom.md), or configuration files. Creating a layer involves three general steps:

1. Package your layer content. This means creating a .zip file archive that contains the dependencies you want to use in your functions.

1. Create the layer in Lambda.

1. Add the layer to your functions.

**Topics**
+ [Package your layer content](#nodejs-layers-package)
+ [Create the layer in Lambda](#publishing-layer)
+ [Add the layer to your function](#nodejs-layer-adding)
+ [Sample app](#nodejs-layer-sample-app)

## Package your layer content
<a name="nodejs-layers-package"></a>

To create a layer, bundle your packages into a .zip file archive that meets the following requirements:
+ Build the layer using the same Node.js version that you plan to use for the Lambda function. For example, if you build your layer using Node.js 24, use the Node.js 24 runtime for your function.
+ Your layer's .zip file must use one of these directory structures:
  + `nodejs/node_modules`
  + `nodejs/node{{X}}/node_modules` (where {{X}} is your Node.js version, for example `node22`)

  For more information, see [Layer paths for each Lambda runtime](packaging-layers.md#packaging-layers-paths).
+ The packages in your layer must be compatible with Linux. Lambda functions run on Amazon Linux.

You can create layers that contain either third-party Node.js libraries installed with `npm` (such as `axios` or `lodash`) or your own JavaScript modules.

### Third-party dependencies
<a name="nodejs-layers-third-party-dependencies"></a>

**To create a layer using npm packages**

1. Create the required directory structure and install packages directly into it:

   ```
   mkdir -p nodejs
   npm install --prefix nodejs lodash axios
   ```

   This command installs the packages directly into the `nodejs/node_modules` directory, which is the structure that Lambda requires.
**Note**  
For packages with native dependencies or binary components (such as [sharp](https://www.npmjs.com/package/sharp) or [bcrypt](https://www.npmjs.com/package/bcrypt)), ensure that they're compatible with the Lambda Linux environment and your function's [architecture](foundation-arch.md). You might need to use the `--platform` flag:  

   ```
   npm install --prefix nodejs --platform=linux --arch=x64 sharp
   ```
For more complex native dependencies, you might need to compile them in a Linux environment that matches the Lambda runtime. You can use Docker for this purpose.

1. Zip the layer content:

------
#### [ Linux/macOS ]

   ```
   zip -r layer.zip nodejs/
   ```

------
#### [ PowerShell ]

   ```
   Compress-Archive -Path .\nodejs -DestinationPath .\layer.zip
   ```

------

   The directory structure of your .zip file should look like this:

   ```
   nodejs/
   ├── package.json
   ├── package-lock.json
   └── node_modules/
       ├── lodash/
       ├── axios/
       └── (dependencies of the other packages)
   ```
**Note**  
Make sure your .zip file includes the `nodejs` directory at the root level with `node_modules` inside it. This structure ensures that Lambda can locate and import your packages.
The `package.json` and `package-lock.json` files in the `nodejs/` directory are used by npm for dependency management but are not required by Lambda for layer functionality. Each installed package already contains its own `package.json` file that defines how Lambda imports the package.

### Custom JavaScript modules
<a name="custom-nodejs-modules"></a>

**To create a layer using your own code**

1. Create the required directory structure for your layer:

   ```
   mkdir -p nodejs/node_modules/validator
   cd nodejs/node_modules/validator
   ```

1. Create a `package.json` file for your custom module to define how it should be imported:  
**Example nodejs/node\_modules/validator/package.json**  

   ```
   {
     "name": "validator",
     "version": "1.0.0",
     "type": "module",
     "main": "index.mjs"
   }
   ```

1. Create your JavaScript module file:  
**Example nodejs/node\_modules/validator/index.mjs**  

   ```
   export function validateOrder(orderData) {
     // Validates an order and returns formatted data
     const requiredFields = ['productId', 'quantity'];
     
     // Check required fields
     const missingFields = requiredFields.filter(field => !(field in orderData));
     if (missingFields.length > 0) {
       throw new Error(`Missing required fields: ${missingFields.join(', ')}`);
     }
     
     // Validate quantity
     const quantity = orderData.quantity;
     if (!Number.isInteger(quantity) || quantity < 1) {
       throw new Error('Quantity must be a positive integer');
     }
     
     // Format and return the validated data
     return {
       productId: String(orderData.productId),
       quantity: quantity,
       shippingPriority: orderData.priority || 'standard'
     };
   }
   
   export function formatResponse(statusCode, body) {
     // Formats the API response
     return {
       statusCode: statusCode,
       body: JSON.stringify(body)
     };
   }
   ```

1. Zip the layer content:

------
#### [ Linux/macOS ]

   ```
   zip -r layer.zip nodejs/
   ```

------
#### [ PowerShell ]

   ```
   Compress-Archive -Path .\nodejs -DestinationPath .\layer.zip
   ```

------

   The directory structure of your .zip file should look like this:

   ```
   nodejs/              
   └── node_modules/
       └── validator/
           ├── package.json
           └── index.mjs
   ```

1. In your function, import and use the modules. Example:

   ```
   import { validateOrder, formatResponse } from 'validator';
   
   export const handler = async (event) => {
     try {
       // Parse the order data from the event body
       const orderData = JSON.parse(event.body || '{}');
       
       // Validate and format the order
       const validatedOrder = validateOrder(orderData);
       
       return formatResponse(200, {
         message: 'Order validated successfully',
         order: validatedOrder
       });
     } catch (error) {
       if (error instanceof Error && error.message.includes('Missing required fields')) {
         return formatResponse(400, {
           error: error.message
         });
       }
       
       return formatResponse(500, {
         error: 'Internal server error'
       });
     }
   };
   ```

   You can use the following [test event](testing-functions.md#invoke-with-event) to invoke the function:

   ```
   {
       "body": "{\"productId\": \"ABC123\", \"quantity\": 2, \"priority\": \"express\"}"
   }
   ```

   Expected response:

   ```
   {
     "statusCode": 200,
     "body": "{\"message\":\"Order validated successfully\",\"order\":{\"productId\":\"ABC123\",\"quantity\":2,\"shippingPriority\":\"express\"}}"
   }
   ```

## Create the layer in Lambda
<a name="publishing-layer"></a>

You can publish your layer using either the AWS CLI or the Lambda console.

------
#### [ AWS CLI ]

Run the [publish-layer-version](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/publish-layer-version.html) AWS CLI command to create the Lambda layer:

```
aws lambda publish-layer-version --layer-name {{my-layer}} --zip-file fileb://layer.zip --compatible-runtimes {{nodejs24.x}}
```

The [compatible runtimes](https://docs.aws.amazon.com/lambda/latest/api/API_PublishLayerVersion.html#lambda-PublishLayerVersion-request-CompatibleRuntimes) parameter is optional. When specified, Lambda uses this parameter to filter layers in the Lambda console.

------
#### [ Console ]

**To create a layer (console)**

1. Open the [Layers page](https://console.aws.amazon.com/lambda/home#/layers) of the Lambda console.

1. Choose **Create layer**.

1. Choose **Upload a .zip file**, and then upload the .zip archive that you created earlier.

1. (Optional) For **Compatible runtimes**, choose the Node.js runtime that corresponds to the Node.js version you used to build your layer.

1. Choose **Create**.

------

## Add the layer to your function
<a name="nodejs-layer-adding"></a>

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
<a name="nodejs-layer-sample-app"></a>

For more examples of how to use Lambda layers, see the [layer-nodejs](https://github.com/awsdocs/aws-lambda-developer-guide/tree/main/sample-apps/layer-nodejs) sample application in the AWS Lambda Developer Guide GitHub repository. This application includes a layer that contains the [lodash](https://www.npmjs.com/package/lodash) library. After creating the layer, you can deploy and invoke the corresponding function to confirm that the layer works as expected.