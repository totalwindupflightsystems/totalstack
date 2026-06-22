---
id: acm
title: AWS Certificate Manager (ACM)
target_lang: py
model: openrouter/owl-alpha
tags: [aws, acm, tls, certificates, public, private]
---

# ACM — AWS Certificate Manager

Provision, manage, and deploy public and private SSL/TLS certificates for use with AWS services.

## Architecture

- **16 operations** — request, import, export, describe, list, delete, renew certificates
- **Tag management** — add, list, remove tags
- **Account configuration** — get/put expiry events + opt-in settings
- **Validation** — email and DNS validation methods supported
- **Export** — private certificates can be exported with encrypted private key

## Subsystems

1. **Certificate Lifecycle** — RequestCertificate, ImportCertificate, RenewCertificate, RevokeCertificate, DeleteCertificate
2. **Certificate Query** — DescribeCertificate, GetCertificate, ListCertificates, ExportCertificate
3. **Tag Management** — AddTagsToCertificate, ListTagsForCertificate, RemoveTagsFromCertificate  
4. **Account Config** — GetAccountConfiguration, PutAccountConfiguration
5. **Validation** — ResendValidationEmail, UpdateCertificateOptions
