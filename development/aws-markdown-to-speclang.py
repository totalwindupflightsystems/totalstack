#!/usr/bin/env python3
"""
AWS Markdown → SpecLang: download API Reference markdown files from AWS docs,
add SpecLang YAML frontmatter, and save to per-service spec directories.

Usage:
    .venv/bin/python3 development/aws-markdown-to-speclang.py s3
    .venv/bin/python3 development/aws-markdown-to-speclang.py dynamodb
    .venv/bin/python3 development/aws-markdown-to-speclang.py --discover lambda

What it does:
1. Probes known URL patterns to find the correct docs base URL
2. Downloads toc-contents.json to get the full operation/page list
3. Downloads each .md file
4. Wraps with SpecLang YAML frontmatter (id, target_lang, owned-by, depends_on)
5. Saves to specs/aws/{service}/docs/{page}.spec.md
"""
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request

# ── URL discovery ──────────────────────────────────────────────────────

# Known URL patterns for AWS docs (tried in order)
# The {svc_long} is the service name in the URL (e.g., AmazonS3, AWSSimpleQueueService)
URL_PATTERNS = [
    # S3 pattern: /AmazonS3/latest/API/
    lambda svc_long, _: f"https://docs.aws.amazon.com/{svc_long}/latest/API/",
    # Standard pattern: /{service}/latest/APIReference/
    lambda svc_long, svc: f"https://docs.aws.amazon.com/{svc_long}/latest/APIReference/",
    # Lambda pattern: /lambda/latest/dg/
    lambda svc_long, svc: f"https://docs.aws.amazon.com/{svc}/latest/dg/",
    # Fallback: /{service}/latest/userguide/
    lambda svc_long, svc: f"https://docs.aws.amazon.com/{svc}/latest/userguide/",
]

# Manual overrides for known services
SERVICE_URL_OVERRIDES = {
    's3': 'https://docs.aws.amazon.com/AmazonS3/latest/API/',
    'dynamodb': 'https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/',
    'lambda': 'https://docs.aws.amazon.com/lambda/latest/dg/',
    'sqs': 'https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/',
    'sns': 'https://docs.aws.amazon.com/sns/latest/APIReference/',
    'kms': 'https://docs.aws.amazon.com/kms/latest/APIReference/',
    'iam': 'https://docs.aws.amazon.com/IAM/latest/APIReference/',
    'ec2': 'https://docs.aws.amazon.com/AWSEC2/latest/APIReference/',
    'ecs': 'https://docs.aws.amazon.com/AmazonECS/latest/APIReference/',
    'rds': 'https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/',
    'elbv2': 'https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/',
    'cloudformation': 'https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/',
    'cloudwatch': 'https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/',
    'route53': 'https://docs.aws.amazon.com/Route53/latest/APIReference/',
    'shield': 'https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/',
    'application-autoscaling': 'https://docs.aws.amazon.com/autoscaling/application/APIReference/',
    'cloudfront': 'https://docs.aws.amazon.com/cloudfront/latest/APIReference/',
    'cloudtrail': 'https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/',
    'cognito-identity': 'https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/',
    'ecr': 'https://docs.aws.amazon.com/AmazonECR/latest/APIReference/',
    'wafv2': 'https://docs.aws.amazon.com/waf/latest/APIReference/',
    'docdb': 'https://docs.aws.amazon.com/documentdb/latest/APIReference/',
    'sesv2': 'https://docs.aws.amazon.com/ses/latest/APIReference-V2/',
    's3tables': 'https://docs.aws.amazon.com/AmazonS3/latest/API/',
    'mq': 'https://docs.aws.amazon.com/amazon-mq/latest/api-reference/',
    'backup': 'https://docs.aws.amazon.com/aws-backup/latest/devguide/',
    'kafka': 'https://docs.aws.amazon.com/msk/latest/developerguide/',
    'opensearchserverless': 'https://docs.aws.amazon.com/opensearch-service/latest/developerguide/',
    'bedrock-agent': 'https://docs.aws.amazon.com/bedrock/latest/APIReference/',
    'bedrock-runtime': 'https://docs.aws.amazon.com/bedrock/latest/APIReference/',
    'timestream-influxdb': 'https://docs.aws.amazon.com/timestream/latest/developerguide/',
    'dynamodbstreams': 'https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/',
    'appmesh': 'https://docs.aws.amazon.com/app-mesh/latest/APIReference/',
}

# Service name overrides (botocore name → AWS docs URL name)
SERVICE_NAME_OVERRIDES = {
    's3': 'AmazonS3',
    'dynamodb': 'amazondynamodb',
    'lambda': 'lambda',
    'sqs': 'AWSSimpleQueueService',
    'sns': 'sns',
    'kms': 'kms',
    'iam': 'IAM',
    'ec2': 'AWSEC2',
    'ecs': 'AmazonECS',
    'rds': 'AmazonRDS',
    'elbv2': 'elasticloadbalancing',
    'cloudformation': 'AWSCloudFormation',
    'cloudwatch': 'AmazonCloudWatch',
    'route53': 'Route53',
    'sts': 'STS',
    'cognito-idp': 'cognito-user-identity-pools',
    'cognito-identity': 'cognito-identity',
    'apigateway': 'apigateway',
    'apigatewayv2': 'apigatewayv2',
    'stepfunctions': 'step-functions',
    'secretsmanager': 'secretsmanager',
    'ssm': 'systems-manager',
    'codebuild': 'codebuild',
    'codedeploy': 'codedeploy',
    'codepipeline': 'codepipeline',
    'codecommit': 'codecommit',
    'codeartifact': 'codeartifact',
    'elasticache': 'elasticache',
    'neptune': 'neptune',
    'rekognition': 'rekognition',
    'textract': 'textract',
    'athena': 'athena',
    'translate': 'translate',
    'mediaconvert': 'mediaconvert',
    'organizations': 'organizations',
    'servicecatalog': 'servicecatalog',
    'cloudfront': 'AmazonCloudFront',
    'wafv2': 'wafv2',
    'shield': 'shield',
    'guardduty': 'guardduty',
    'securityhub': 'securityhub',
    'config': 'config',
    'cloudtrail': 'cloudtrail',
    'kinesis': 'kinesis',
    'firehose': 'firehose',
    'glue': 'glue',
    'batch': 'batch',
    'sagemaker': 'sagemaker',
    'comprehend': 'comprehend',
    'polly': 'polly',
    'lex-models': 'lex-models',
    'lexv2-models': 'lexv2-models',
    'connect': 'connect',
    'pinpoint': 'pinpoint',
    'sesv2': 'sesv2',
    'acm': 'acm',
    'acm-pca': 'acm-pca',
    'amplify': 'amplify',
    'appsync': 'appsync',
    'autoscaling': 'autoscaling',
    'backup': 'backup',
    'ce': 'cost-management',
    'datasync': 'datasync',
    'dms': 'dms',
    'ds': 'directory-service',
    'ecr': 'ecr',
    'efs': 'efs',
    'eks': 'eks',
    'elasticbeanstalk': 'elastic-beanstalk',
    'emr': 'emr',
    'events': 'eventbridge',
    'fsx': 'fsx',
    'globalaccelerator': 'global-accelerator',
    'inspector2': 'inspector2',
    'iot': 'iot',
    'kafka': 'msk',
    'kendra': 'kendra',
    'keyspaces': 'keyspaces',
    'kinesisanalytics': 'kinesisanalytics',
    'kinesisvideo': 'kinesisvideo',
    'lakeformation': 'lake-formation',
    'license-manager': 'license-manager',
    'lightsail': 'lightsail',
    'macie2': 'macie2',
    'managedblockchain': 'managedblockchain',
    'mediaconnect': 'mediaconnect',
    'medialive': 'medialive',
    'mediapackage': 'mediapackage',
    'memorydb': 'memorydb',
    'mq': 'amazon-mq',
    'mwaa': 'mwaa',
    'network-firewall': 'network-firewall',
    'networkmanager': 'networkmanager',
    'opensearch': 'opensearch-service',
    'outposts': 'outposts',
    'personalize': 'personalize',
    'quicksight': 'quicksight',
    'ram': 'ram',
    'rds-data': 'rds-data',
    'redshift': 'redshift',
    'redshift-data': 'redshift-data',
    'redshift-serverless': 'redshift-serverless',
    'resource-groups': 'resource-groups',
    'rolesanywhere': 'rolesanywhere',
    'route53domains': 'route53domains',
    'route53-recovery-cluster': 'route53-recovery-cluster',
    'route53-recovery-control-config': 'route53-recovery-control-config',
    'route53-recovery-readiness': 'route53-recovery-readiness',
    'rum': 'rum',
    's3outposts': 's3outposts',
    's3control': 's3control',
    'sagemaker-runtime': 'sagemaker-runtime',
    'savingsplans': 'savingsplans',
    'schemas': 'schemas',
    'sdb': 'simpledb',
    'serverlessrepo': 'serverlessrepo',
    'service-quotas': 'servicequotas',
    'servicediscovery': 'servicediscovery',
    'signer': 'signer',
    'snowball': 'snowball',
    'sso': 'sso',
    'sso-admin': 'sso-admin',
    'sso-oidc': 'sso-oidc',
    'storagegateway': 'storagegateway',
    'synthetics': 'synthetics',
    'timestream-query': 'timestream-query',
    'timestream-write': 'timestream-write',
    'transfer': 'transfer',
    'verifiedpermissions': 'verifiedpermissions',
    'vpc-lattice': 'vpc-lattice',
    'waf': 'waf',
    'waf-regional': 'waf-regional',
    'wellarchitected': 'wellarchitected',
    'wisdom': 'wisdom',
    'workdocs': 'workdocs',
    'workmail': 'workmail',
    'workspaces': 'workspaces',
    'xray': 'xray',
}


def http_get(url: str, retries: int = 3) -> tuple[int, str]:
    """HTTP GET with retry. Returns (status_code, body)."""
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'TotalStack/1.0'})
            with urllib.request.urlopen(req, timeout=30) as resp:
                return resp.status, resp.read().decode('utf-8', errors='replace')
        except urllib.error.HTTPError as e:
            if attempt == retries - 1:
                return e.code, ''
            time.sleep(1)
        except Exception as e:
            if attempt == retries - 1:
                return 0, str(e)
            time.sleep(1)
    return 0, ''


def discover_docs_url(service: str) -> str | None:
    """Discover the AWS docs base URL for a service."""
    # Check overrides first
    if service in SERVICE_URL_OVERRIDES:
        return SERVICE_URL_OVERRIDES[service]

    svc_long = SERVICE_NAME_OVERRIDES.get(service, service)

    # Probe known patterns
    for pattern_fn in URL_PATTERNS:
        base_url = pattern_fn(svc_long, service)
        test_url = base_url + 'toc-contents.json'
        code, _ = http_get(test_url)
        if code == 200:
            return base_url

    return None


def download_toc(base_url: str) -> list[dict]:
    """Download toc-contents.json and extract page list."""
    toc_url = base_url.rstrip('/') + '/toc-contents.json'
    code, body = http_get(toc_url)
    if code != 200:
        print(f"  WARNING: toc-contents.json returned {code}")
        return []

    try:
        toc = json.loads(body)
    except json.JSONDecodeError:
        print("  WARNING: toc-contents.json is not valid JSON")
        return []

    pages = []

    def extract_pages(node, depth=0):
        """Recursively extract leaf pages from nested contents."""
        if isinstance(node, list):
            for item in node:
                extract_pages(item, depth)
        elif isinstance(node, dict):
            href = node.get('href', '')
            title = node.get('title', '')
            children = node.get('contents', [])
            if href and not children:
                # Leaf page — has href but no sub-contents
                md_href = href.replace('.html', '.md')
                pages.append({
                    'href': md_href,
                    'title': title,
                    'file_name': md_href.split('/')[-1].replace('.md', ''),
                })
            if children:
                extract_pages(children, depth + 1)

    extract_pages(toc)
    return pages


def add_speclang_frontmatter(markdown_content: str, service: str, page_name: str, title: str) -> str:
    """Wrap AWS markdown with SpecLang YAML frontmatter."""
    # Clean the content — remove AWS-specific nav markup
    content = markdown_content
    # Remove the first H1 (it's redundant with title)
    content = re.sub(r'^# .+\n+', '', content, count=1)

    frontmatter = f'''---
id: "@specs/aws/{service}/docs/{page_name}"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS {title}"
status: active
depends_on:
  - "@specs/aws/{service}/meta"
---

# {title}

> **source:** AWS Documentation
> **spec:id:** @specs/aws/{service}/docs/{page_name}
> **target_lang:** meta — documentation tier. ALL sections preserved.

'''
    return frontmatter + content


def download_service(service: str, output_dir: str, max_pages: int = 200) -> int:
    """Download all AWS markdown docs for a service, wrap with SpecLang headers."""
    print(f"\n{'='*60}")
    print(f"Service: {service}")

    # Discover docs URL
    base_url = discover_docs_url(service)
    if not base_url:
        print(f"  ❌ Could not discover docs URL for {service}")
        print("     Add to SERVICE_URL_OVERRIDES or SERVICE_NAME_OVERRIDES")
        return 0

    print(f"  Base URL: {base_url}")

    # Download TOC
    pages = download_toc(base_url)
    if not pages:
        print("  ⚠ No pages found in toc-contents.json")
        print("     Trying direct discovery from toc-contents.json structure...")
        # Try direct listing — some services have different TOC structures
        return 0

    print(f"  Found {len(pages)} pages in TOC")
    os.makedirs(output_dir, exist_ok=True)

    downloaded = 0
    errors = 0

    for i, page in enumerate(pages[:max_pages]):
        page_url = base_url.rstrip('/') + '/' + page['href']
        code, body = http_get(page_url)

        if code == 200 and body.strip():
            wrapped = add_speclang_frontmatter(body, service, page['file_name'], page['title'])
            out_path = os.path.join(output_dir, f"{page['file_name']}.spec.md")
            with open(out_path, 'w') as f:
                f.write(wrapped)
            downloaded += 1
            if (i + 1) % 20 == 0:
                print(f"    ... {i+1}/{len(pages[:max_pages])} ({downloaded} downloaded, {errors} errors)")
        else:
            errors += 1
            if errors <= 3:
                print(f"    ⚠ {page_url} → {code}")

    print(f"  ✅ Downloaded {downloaded} pages to {output_dir}/ ({errors} errors)")
    return downloaded


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    svc = sys.argv[1]
    out = sys.argv[2] if len(sys.argv) > 2 else f'specs/aws/{svc}/docs'

    count = download_service(svc, out)
    print(f"\nDone: {count} docs → {out}/")
