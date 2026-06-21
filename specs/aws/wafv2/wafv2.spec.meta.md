---
id: "@specs/aws/wafv2/meta"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
status: active
---
# WAFv2 — AWS WAF (Web Application Firewall v2)

WAFv2 is AWS's web application firewall service that protects web applications
from common web exploits. It provides:

- **WebACL**: Web Access Control Lists — rule collections applied to resources
- **IPSet**: IP address collections for allow/block rules
- **RegexPatternSet**: Regex patterns for matching request components
- **RuleGroup**: Reusable rule collections for WebACLs
- **LoggingConfiguration**: Log destination configuration
- **PermissionPolicy**: Resource-based permission policies

## Architecture

Each resource is scoped to `REGIONAL` (ALB, API Gateway, AppSync) or `CLOUDFRONT`.
Lock tokens provide optimistic concurrency for updates/deletes.
