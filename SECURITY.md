# Security Policy

## Reporting a Vulnerability

TotalStack is a development tool — it runs locally and does not handle production data. If you discover a security issue, please open a GitHub issue or contact the maintainers directly.

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| main    | :white_check_mark: |

## Security Model

TotalStack is a local AWS cloud stack emulator. It does not:

- Expose network services by default
- Store or transmit credentials
- Handle production workloads

Security concerns related to LocalStack (the upstream project) should be reported to the LocalStack team.
