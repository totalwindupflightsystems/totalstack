---
id: acm-plan
title: ACM Implementation Plan
target_lang: py
depends_on: ["specs/aws/acm/acm.spec.meta.md"]
---

# ACM Implementation Plan

## Store: ACMStore

Single dict-backed store for certificate records. Key: CertificateArn.

## Exceptions
- InvalidArnException — malformed ARN
- InvalidDomainValidationOptionsException — bad domain opts
- InvalidParameterException — bad params
- InvalidStateException — wrong state for operation
- InvalidTagException — bad tag format
- LimitExceededException — too many certificates
- RequestInProgressException — duplicate request
- ResourceInUseException — cert in use
- ResourceNotFoundException — cert not found
- TooManyTagsException — tag limit exceeded
- ValidationException — validation error

## CertificateRecord Fields
- CertificateArn, DomainName, SubjectAlternativeNames, Status (PENDING_VALIDATION/ISSUED/INACTIVE/REVOKED/EXPIRED/FAILED/IMPORTED), Type (IMPORTED/AMAZON_ISSUED/PRIVATE), KeyAlgorithm, SignatureAlgorithm, CreatedAt, IssuedAt, NotBefore, NotAfter, RevokedAt, RevocationReason, InUseBy, DomainValidationOptions, ExtendedKeyUsages, RenewalSummary, Options, Tags

## Handler Counts
- 16 total operations
- Core: RequestCertificate, ImportCertificate, DescribeCertificate, GetCertificate, ListCertificates, DeleteCertificate, ExportCertificate
- Lifecycle: RenewCertificate, RevokeCertificate, UpdateCertificateOptions
- Tags: AddTagsToCertificate, ListTagsForCertificate, RemoveTagsFromCertificate
- Account: GetAccountConfiguration, PutAccountConfiguration
- Validation: ResendValidationEmail
