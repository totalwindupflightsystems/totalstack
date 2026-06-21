---
id: "@specs/aws/lightsail/docs/amazon-lightsail-bundles"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Bundles"
status: active
depends_on:
  - "@specs/aws/lightsail/meta"
---

# Bundles

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lightsail/docs/amazon-lightsail-bundles
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Lightsail instance bundles
<a name="amazon-lightsail-bundles"></a>

Lightsail offers a variety of instance bundles (also known as instance plans) to meet different workload requirements. Each bundle provides compute power (vCPUs), memory (RAM), storage, and a data transfer allowance. Bundles are billed on an on-demand hourly rate, so you pay only for what you use. For every bundle you use, we charge you the fixed hourly price, up to the maximum monthly plan cost.

 General purpose plans provide a balanced mix of compute, memory, and networking resources suitable for the majority of applications, such as web and application servers, virtual desktops, microservices, databases, and batch processing. Memory optimized plans provide a higher memory-to-CPU ratio that benefits workloads such as in-memory caching, real-time big data analytics, or high-performance databases. Compute optimized plans provide a higher CPU-to-memory ratio that benefits compute-intensive workloads such as batch processing, video encoding, and dedicated game servers. 

Each bundle will include public IP addressing. It will provide either a public IPv4 address, a public IPv4 address with an IPv6 address (known as dual-stack), or just an IPv6 address (known as IPv6 only). The bundle price varies depending on whether it includes a public IPv4 address.

**Topics**
+ [Linux/Unix bundles (with public IPv4 addressing)](#linux-unix-bundles)
+ [Linux/Unix bundles (IPv6-only)](#linux-unix-ipv6-bundles)
+ [Windows bundles (with public IPv4 addressing)](#windows-bundles)
+ [Windows bundles (IPv6-only)](#windows-ipv6-bundles)

## Linux/Unix bundles (with public IPv4 addressing)
<a name="linux-unix-bundles"></a>

The following table lists the specifications for Linux/Unix instance bundles that include an IPv4 address.


|  Bundle name  |  Price (USD/month)  |  vCPUs  |  Memory  |  Storage  |  Data transfer \*  | 
| --- | --- | --- | --- | --- | --- | 
| Nano-0.5GB Linux with public IPv4 | $5.00 | 2 | 0.5 GB | 20 GB | 1 TB | 
| Micro-1GB Linux with public IPv4 | $7.00 | 2 | 1 GB | 40 GB | 2 TB | 
| Small-2GB Linux with public IPv4 | $12.00 | 2 | 2 GB | 60 GB | 3 TB | 
| Medium-4GB Linux with public IPv4 | $24.00 | 2 | 4 GB | 80 GB | 4 TB | 
| Large-8GB Linux with public IPv4 | $44.00 | 2 | 8 GB | 160 GB | 5 TB | 
| Xlarge-16GB Linux with public IPv4 | $84.00 | 4 | 16 GB | 320 GB | 6 TB | 
| 2Xlarge-32GB Linux with public IPv4 | $164.00 | 8 | 32 GB | 640 GB | 7 TB | 
| 4Xlarge-64GB Linux with public IPv4 | $384.00 | 16 | 64 GB | 1,280 GB | 8 TB | 
| 8Xlarge-128GB Linux with public IPv4 | $884.00 | 32 | 128 GB | 1,280 GB | 9 TB | 
| 12Xlarge-192GB Linux with public IPv4 | $1,324.00 | 48 | 192 GB | 1,280 GB | 10 TB | 
| 16Xlarge-256GB Linux with public IPv4 | $1,764.00 | 64 | 256 GB | 1,280 GB | 10 TB | 
| Memory-optimized Large-16GB Linux with public IPv4 | $74.00 | 2 | 16 GB | 160 GB | 5 TB | 
| Memory-optimized Xlarge-32GB Linux with public IPv4 | $144.00 | 4 | 32 GB | 320 GB | 6 TB | 
| Memory-optimized 2Xlarge-64GB Linux with public IPv4 | $294.00 | 8 | 64 GB | 640 GB | 7 TB | 
| Memory-optimized 4Xlarge-128GB Linux with public IPv4 | $584.00 | 16 | 128 GB | 1,280 GB | 8 TB | 
| Memory-optimized 8Xlarge-256GB Linux with public IPv4 | $1174.00 | 32 | 256 GB | 1,280 GB | 9 TB | 
| Memory-optimized 12Xlarge-384GB Linux with public IPv4 | $1,764.00 | 48 | 384 GB | 1,280 GB | 10 TB | 
| Memory-optimized 16Xlarge-512GB Linux with public IPv4 | $2,344.00 | 64 | 512 GB | 1,280 GB | 10 TB | 
| Compute-optimized Large-4GB Linux with public IPv4 | $42.00 | 2 | 4 GB | 160 GB | 5 TB | 
| Compute-optimized Xlarge-8GB Linux with public IPv4 | $84.00 | 4 | 8 GB | 320 GB | 6 TB | 
| Compute-optimized 2Xlarge-16GB Linux with public IPv4 | $168.00 | 8 | 16 GB | 640 GB | 7 TB | 
| Compute-optimized 4Xlarge-32GB Linux with public IPv4 | $336.00 | 16 | 32 GB | 1,280 GB | 8 TB | 
| Compute-optimized 9Xlarge-72GB Linux with public IPv4 | $844.00 | 36 | 72 GB | 1,280 GB | 9 TB | 
| Compute-optimized 12Xlarge-96GB Linux with public IPv4 | $1,126.00 | 48 | 96 GB | 1,280 GB | 10 TB | 
| Compute-optimized 18Xlarge-144GB Linux with public IPv4 | $1,688.00 | 72 | 144 GB | 1,280 GB | 10 TB | 

\* The data transfer allowance can vary by Region. For more information, see [How does my data transfer allowance for instances vary by AWS Region?](amazon-lightsail-faq-data-transfer-allowance.md#data-transfer-allowance-how-do-data-transfer-allowances-vary-by-region).

## Linux/Unix bundles (IPv6-only)
<a name="linux-unix-ipv6-bundles"></a>

The following table lists the specifications for Linux/Unix instance bundles with only an IPv6 address.


|  Bundle name  |  Price (USD/month)  |  vCPUs  |  Memory  |  Storage  |  Data transfer \*  | 
| --- | --- | --- | --- | --- | --- | 
| Nano-0.5GB Linux IPv6-only | $3.50 | 2 | 0.5 GB | 20 GB | 1 TB | 
| Micro-1GB Linux IPv6-only | $5.00 | 2 | 1 GB | 40 GB | 2 TB | 
| Small-2GB Linux IPv6-only | $10.00 | 2 | 2 GB | 60 GB | 3 TB | 
| Medium-4GB Linux IPv6-only | $20.00 | 2 | 4 GB | 80 GB | 4 TB | 
| Large-8GB Linux IPv6-only | $40.00 | 2 | 8 GB | 160 GB | 5 TB | 
| Xlarge-16GB Linux IPv6-only | $80.00 | 4 | 16 GB | 320 GB | 6 TB | 
| 2Xlarge-32GB Linux IPv6-only | $160.00 | 8 | 32 GB | 640 GB | 7 TB | 
| 4Xlarge-64GB Linux IPv6-only | $380.00 | 16 | 64 GB | 1,280 GB | 8 TB | 
| 8Xlarge-128GB Linux IPv6-only | $880.00 | 32 | 128 GB | 1,280 GB | 9 TB | 
| 12Xlarge-192GB Linux IPv6-only | $1,320.00 | 48 | 192 GB | 1,280 GB | 10 TB | 
| 16Xlarge-256GB Linux IPv6-only | $1,760.00 | 64 | 256 GB | 1,280 GB | 10 TB | 
| Memory-optimized Large-16GB Linux IPv6-only | $70.00 | 2 | 16 GB | 160 GB | 5 TB | 
| Memory-optimized Xlarge-32GB Linux IPv6-only | $140.00 | 4 | 32 GB | 320 GB | 6 TB | 
| Memory-optimized 2Xlarge-64GB Linux IPv6-only | $290.00 | 8 | 64 GB | 640 GB | 7 TB | 
| Memory-optimized 4Xlarge-128GB Linux IPv6-only | $580.00 | 16 | 128 GB | 1,280 GB | 8 TB | 
| Memory-optimized 8Xlarge-256GB Linux IPv6-only | $1170.00 | 32 | 256 GB | 1,280 GB | 9 TB | 
| Memory-optimized 12Xlarge-384GB Linux IPv6-only | $1,760.00 | 48 | 384 GB | 1,280 GB | 10 TB | 
| Memory-optimized 16Xlarge-512GB Linux IPv6-only | $2,340.00 | 64 | 512 GB | 1,280 GB | 10 TB | 
| Compute-optimized Large-4GB Linux IPv6-only | $38.00 | 2 | 4 GB | 160 GB | 5 TB | 
| Compute-optimized Xlarge-8GB Linux IPv6-only | $80.00 | 4 | 8 GB | 320 GB | 6 TB | 
| Compute-optimized 2Xlarge-16GB Linux IPv6-only | $164.00 | 8 | 16 GB | 640 GB | 7 TB | 
| Compute-optimized 4Xlarge-32GB Linux IPv6-only | $332.00 | 16 | 32 GB | 1,280 GB | 8 TB | 
| Compute-optimized 9Xlarge-72GB Linux IPv6-only | $840.00 | 36 | 72 GB | 1,280 GB | 9 TB | 
| Compute-optimized 12Xlarge-96GB Linux IPv6-only | $1,122.00 | 48 | 96 GB | 1,280 GB | 10 TB | 
| Compute-optimized 18Xlarge-144GB Linux IPv6-only | $1,684.00 | 72 | 144 GB | 1,280 GB | 10 TB | 

\* The data transfer allowance can vary by Region. For more information, see [How does my data transfer allowance for instances vary by AWS Region?](amazon-lightsail-faq-data-transfer-allowance.md#data-transfer-allowance-how-do-data-transfer-allowances-vary-by-region).

## Windows bundles (with public IPv4 addressing)
<a name="windows-bundles"></a>

The following table lists the specifications for Windows instance bundles that include an IPv4 address.


|  Bundle name  |  Price (USD/month)  |  vCPUs  |  Memory  |  Storage  |  Data transfer \*  | 
| --- | --- | --- | --- | --- | --- | 
| Nano-0.5GB Windows with public IPv4 | $9.50 | 2 | 0.5 GB | 30 GB | 1 TB | 
| Micro-1GB Windows with public IPv4 | $14.00 | 2 | 1 GB | 40 GB | 2 TB | 
| Small-2GB Windows with public IPv4 | $22.00 | 2 | 2 GB | 60 GB | 3 TB | 
| Medium-4GB Windows with public IPv4 | $44.00 | 2 | 4 GB | 80 GB | 4 TB | 
| Large-8GB Windows with public IPv4 | $74.00 | 2 | 8 GB | 160 GB | 5 TB | 
| Xlarge-16GB Windows with public IPv4 | $124.00 | 4 | 16 GB | 320 GB | 6 TB | 
| 2Xlarge-32GB Windows with public IPv4 | $244.00 | 8 | 32 GB | 640 GB | 7 TB | 
| 4Xlarge-64GB Windows with public IPv4 | $574.00 | 16 | 64 GB | 1,280 GB | 8 TB | 
| 8Xlarge-128GB Windows with public IPv4 | $1,254.00 | 32 | 128 GB | 1,280 GB | 9 TB | 
| 12Xlarge-192GB Windows with public IPv4 | $1,884.00 | 48 | 192 GB | 1,280 GB | 10 TB | 
| 16Xlarge-256GB Windows with public IPv4 | $2,504.00 | 64 | 256 GB | 1,280 GB | 10 TB | 
| Memory-optimized Large-16GB Windows with public IPv4 | $134.00 | 2 | 16 GB | 160 GB | 5 TB | 
| Memory-optimized Xlarge-32GB Windows with public IPv4 | $264.00 | 4 | 32 GB | 320 GB | 6 TB | 
| Memory-optimized 2Xlarge-64GB Windows with public IPv4 | $524.00 | 8 | 64 GB | 640 GB | 7 TB | 
| Memory-optimized 4Xlarge-128GB Windows with public IPv4 | $1044.00 | 16 | 128 GB | 1,280 GB | 8 TB | 
| Memory-optimized 8Xlarge-256GB Windows with public IPv4 | $2,104.00 | 32 | 256 GB | 1,280 GB | 9 TB | 
| Memory-optimized 12Xlarge-384GB Windows with public IPv4 | $3,164.00 | 48 | 384 GB | 1,280 GB | 10 TB | 
| Memory-optimized 16Xlarge-512GB Windows with public IPv4 | $4,204.00 | 64 | 512 GB | 1,280 GB | 10 TB | 
| Compute-optimized Large-4GB Windows with public IPv4 | $100.00 | 2 | 4 GB | 160 GB | 5 TB | 
| Compute-optimized Xlarge-8GB Windows with public IPv4 | $200.00 | 4 | 8 GB | 320 GB | 6 TB | 
| Compute-optimized 2Xlarge-16GB Windows with public IPv4 | $400.00 | 8 | 16 GB | 640 GB | 7 TB | 
| Compute-optimized 4Xlarge-32GB Windows with public IPv4 | $800.00 | 16 | 32 GB | 1,280 GB | 8 TB | 
| Compute-optimized 9Xlarge-72GB Windows with public IPv4 | $1,888.00 | 36 | 72 GB | 1,280 GB | 9 TB | 
| Compute-optimized 12Xlarge-96GB Windows with public IPv4 | $2,518.00 | 48 | 96 GB | 1,280 GB | 10 TB | 
| Compute-optimized 18Xlarge-144GB Windows with public IPv4 | $3,776.00 | 72 | 144 GB | 1,280 GB | 10 TB | 

\* The data transfer allowance can vary by Region. For more information, see [How does my data transfer allowance for instances vary by AWS Region?](amazon-lightsail-faq-data-transfer-allowance.md#data-transfer-allowance-how-do-data-transfer-allowances-vary-by-region).

## Windows bundles (IPv6-only)
<a name="windows-ipv6-bundles"></a>

The following table lists the specifications for Windows instance bundles with only an IPv6 address.


|  Bundle name  |  Price (USD/month)  |  vCPUs  |  Memory  |  Storage  |  Data transfer \*  | 
| --- | --- | --- | --- | --- | --- | 
| Nano-0.5GB Windows IPv6-only | $8.00 | 2 | 0.5 GB | 30 GB | 1 TB | 
| Micro-1GB Windows IPv6-only | $12.00 | 2 | 1 GB | 40 GB | 2 TB | 
| Small-2GB Windows IPv6-only | $20.00 | 2 | 2 GB | 60 GB | 3 TB | 
| Medium-4GB Windows IPv6-only | $40.00 | 2 | 4 GB | 80 GB | 4 TB | 
| Large-8GB Windows IPv6-only | $70.00 | 2 | 8 GB | 160 GB | 5 TB | 
| Xlarge-16GB Windows IPv6-only | $120.00 | 4 | 16 GB | 320 GB | 6 TB | 
| 2Xlarge-32GB Windows IPv6-only | $240.00 | 8 | 32 GB | 640 GB | 7 TB | 
| 4Xlarge-64GB Windows IPv6-only | $570.00 | 16 | 64 GB | 1,280 GB | 8 TB | 
| 8Xlarge-128GB Windows IPv6-only | $1,250.00 | 32 | 128 GB | 1,280 GB | 9 TB | 
| 12Xlarge-192GB Windows IPv6-only | $1,880.00 | 48 | 192 GB | 1,280 GB | 10 TB | 
| 16Xlarge-256GB Windows IPv6-only | $2,500.00 | 64 | 256 GB | 1,280 GB | 10 TB | 
| Memory-optimized Large-16GB Windows IPv6-only | $130.00 | 2 | 16 GB | 160 GB | 5 TB | 
| Memory-optimized Xlarge-32GB Windows IPv6-only | $260.00 | 4 | 32 GB | 320 GB | 6 TB | 
| Memory-optimized 2Xlarge-64GB Windows IPv6-only | $520.00 | 8 | 64 GB | 640 GB | 7 TB | 
| Memory-optimized 4Xlarge-128GB Windows IPv6-only | $1,040.00 | 16 | 128 GB | 1,280 GB | 8 TB | 
| Memory-optimized 8Xlarge-256GB Windows IPv6-only | $2,100.00 | 32 | 256 GB | 1,280 GB | 9 TB | 
| Memory-optimized 12Xlarge-384GB Windows IPv6-only | $3,160.00 | 48 | 384 GB | 1,280 GB | 10 TB | 
| Memory-optimized 16Xlarge-512GB Windows IPv6-only | $4,200.00 | 64 | 512 GB | 1,280 GB | 10 TB | 
| Compute-optimized Large-4GB Windows IPv6-only | $96.00 | 2 | 4 GB | 160 GB | 5 TB | 
| Compute-optimized Xlarge-8GB Windows IPv6-only | $196.00 | 4 | 8 GB | 320 GB | 6 TB | 
| Compute-optimized 2Xlarge-16GB Windows IPv6-only | $396.00 | 8 | 16 GB | 640 GB | 7 TB | 
| Compute-optimized 4Xlarge-32GB Windows IPv6-only | $796.00 | 16 | 32 GB | 1,280 GB | 8 TB | 
| Compute-optimized 9Xlarge-72GB Windows IPv6-only | $1,884.00 | 36 | 72 GB | 1,280 GB | 9 TB | 
| Compute-optimized 12Xlarge-96GB Windows IPv6-only | $2,514.00 | 48 | 96 GB | 1,280 GB | 10 TB | 
| Compute-optimized 18Xlarge-144GB Windows IPv6-only | $3,772.00 | 72 | 144 GB | 1,280 GB | 10 TB | 

\* The data transfer allowance can vary by Region. For more information, see [How does my data transfer allowance for instances vary by AWS Region?](amazon-lightsail-faq-data-transfer-allowance.md#data-transfer-allowance-how-do-data-transfer-allowances-vary-by-region).