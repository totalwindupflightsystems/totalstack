---
id: "@specs/aws/wafv2/docs/Welcome"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Welcome"
status: active
depends_on:
  - "@specs/aws/wafv2/meta"
---

# Welcome

> **source:** AWS Documentation
> **spec:id:** @specs/aws/wafv2/docs/Welcome
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Welcome
<a name="Welcome"></a>

## AWS WAFV2
<a name="Welcome_AWS_WAFV2"></a>

**Note**  
This is the latest version of the ** AWS WAF ** API, released in November, 2019. The names of the entities that you use to access this API, like endpoints and namespaces, all have the versioning information added, like "V2" or "v2", to distinguish from the prior version. We recommend migrating your resources to this version, because it has a number of significant improvements.  
If you used AWS WAF prior to this release, you can't use this AWS WAFV2 API to access any AWS WAF resources that you created before. AWS WAF Classic support will end on September 30, 2025.   
For information about AWS WAF, including how to migrate your AWS WAF Classic resources to this version, see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). 

 AWS WAF is a web application firewall that lets you monitor the HTTP and HTTPS requests that are forwarded to a protected resource. Protected resource types include Amazon CloudFront distribution, Amazon API Gateway REST API, Application Load Balancer, AWS AppSync GraphQL API, Amazon Cognito user pool, AWS App Runner service, AWS Amplify application, and AWS Verified Access instance. AWS WAF also lets you control access to your content, to protect the AWS resource that AWS WAF is monitoring. Based on conditions that you specify, such as the IP addresses that requests originate from or the values of query strings, the protected resource responds to requests with either the requested content, an HTTP 403 status code (Forbidden), or with a custom response. 

This API guide is for developers who need detailed information about AWS WAF API actions, data types, and errors. For detailed information about AWS WAF features and guidance for configuring and using AWS WAF, see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/what-is-aws-waf.html).

You can make calls using the endpoints listed in [AWS WAF endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/waf.html). 
+ For regional resources, you can use any of the endpoints in the list. A regional application can be an Application Load Balancer (ALB), an Amazon API Gateway REST API, an AWS AppSync GraphQL API, an Amazon Cognito user pool, an AWS App Runner service, or an AWS Verified Access instance. 
+ For Amazon CloudFront and AWS Amplify, you must use the API endpoint listed for US East (N. Virginia): us-east-1.

Alternatively, you can use one of the AWS SDKs to access an API that's tailored to the programming language or platform that you're using. For more information, see [AWS SDKs](http://aws.amazon.com/tools/#SDKs).

## AWS WAF Classic
<a name="Welcome_AWS_WAF"></a>

**Note**  
 AWS WAF Classic support will end on September 30, 2025.   
This is ** AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.  
 **For the latest version of AWS WAF **, use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). With the latest version, AWS WAF has a single set of endpoints for regional and global use. 

This is the * AWS WAF Classic API Reference* for using AWS WAF Classic with Amazon CloudFront. The AWS WAF Classic actions and data types listed in the reference are available for protecting CloudFront distributions. You can use these actions and data types via the endpoint *waf.amazonaws.com*. This guide is for developers who need detailed information about the AWS WAF Classic API actions, data types, and errors. For detailed information about AWS WAF Classic features and an overview of how to use the AWS WAF Classic API, see the [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.

## AWS WAF Classic Regional
<a name="Welcome_AWS_WAF_Regional"></a>

**Note**  
 AWS WAF Classic support will end on September 30, 2025.   
This is ** AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.  
 **For the latest version of AWS WAF **, use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). With the latest version, AWS WAF has a single set of endpoints for regional and global use. 

This is the * AWS WAF Classic Regional API Reference* for using AWS WAF Classic with the AWS resources, Elastic Load Balancing Application Load Balancers and Amazon API Gateway APIs. The AWS WAF Classic actions and data types listed in the reference are available for protecting these resource types. You can use these actions and data types by means of the endpoints listed in [AWS WAF Classic endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/waf-classic.html). This guide is for developers who need detailed information about the AWS WAF Classic API actions, data types, and errors. For detailed information about AWS WAF Classic features and an overview of how to use the AWS WAF Classic API, see the [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.