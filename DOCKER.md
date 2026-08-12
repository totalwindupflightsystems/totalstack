> [!NOTE]
> **TotalStack fork note:** this documentation covers the **TotalStack** fork
> (totalwindupflightsystems/totalstack) of LocalStack. The fork does **not**
> publish a pre-built Docker image yet, so the Docker workflows below build
> the image from this repository's `Dockerfile`. For the Docker-free
> development workflow (in-memory `make start`, no Docker required), see the
> [README Quickstart](README.md#quickstart) and its
> [Persistence](README.md#persistence) section.

<p align="center">
  <img src="https://raw.githubusercontent.com/totalwindupflightsystems/totalstack/main/docs/localstack-readme-banner.svg" alt="TotalStack - A fully functional local cloud stack">
</p>

<p align="center">
  <a href="https://github.com/totalwindupflightsystems/totalstack/actions/workflows/aws-main.yml?query=branch%3Amain"><img alt="GitHub Actions" src="https://github.com/totalwindupflightsystems/totalstack/actions/workflows/aws-main.yml/badge.svg?branch=main"></a>
  <a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
  <a href="https://github.com/astral-sh/ruff"><img alt="Ruff" src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json"></a>
</p>

# What is LocalStack?

[LocalStack](https://localstack.cloud) is a cloud service emulator that runs in a single container on your laptop or in your CI environment. With LocalStack, you can run your AWS applications or Lambdas entirely on your local machine without connecting to a remote cloud provider! Whether you are testing complex CDK applications or Terraform configurations, or just beginning to learn about AWS services, LocalStack helps speed up and simplify your testing and development workflow.

LocalStack supports a growing number of AWS services, like AWS Lambda, S3, Dynamodb, Kinesis, SQS, SNS, and many more! You can find a comprehensive list of supported APIs on our [☑️ Feature Coverage](https://docs.localstack.cloud/user-guide/aws/feature-coverage/) page.

LocalStack also provides additional features to make your life as a cloud developer easier! Check out LocalStack's [User Guides](https://docs.localstack.cloud/user-guide/) for more information.

## Usage

Please make sure that you have a working [Docker environment](https://docs.docker.com/get-docker/) on your machine before moving on. You can check if Docker is correctly configured on your machine by executing `docker info` in your terminal. If it does not report an error (but shows information on your Docker system), you’re good to go.

### Docker CLI

You can directly start the TotalStack container using the Docker CLI. This method requires more manual steps and configuration, but it gives you more control over the container settings.

First, build the image from this repository's Dockerfile:

```console
$ docker build -t totalstack .
```

Then start the Docker container:

```console
$ docker run --rm -it -p 4566:4566 -p 4510-4559:4510-4559 totalstack
```

Create an s3 bucket with LocalStack's [`awslocal`](https://docs.localstack.cloud/user-guide/integrations/aws-cli/#localstack-aws-cli-awslocal) CLI:

```
$ awslocal s3api create-bucket --bucket sample-bucket
$ awslocal s3api list-buckets
```

**Notes**

- Re-run `docker build -t totalstack .` from the repository root to rebuild the image with the latest source changes.

- This command does not bind all ports that are potentially used by TotalStack, nor does it mount any volumes. When using Docker to manually start TotalStack, you will have to configure the container on your own (see [`docker-compose.yml`](https://github.com/totalwindupflightsystems/totalstack/blob/main/docker-compose.yml) and [Configuration](https://docs.localstack.cloud/references/configuration/)). This could be seen as the “expert mode” of starting TotalStack. If you are looking for a simpler method of starting TotalStack, please use the [LocalStack CLI](https://docs.localstack.cloud/getting-started/installation/#localstack-cli).

### Docker Compose

You can start TotalStack with [Docker Compose](https://docs.docker.com/compose/) by configuring a `docker-compose.yml file`. Currently, docker-compose version 1.9.0+ is supported.

```
version: "3.8"

services:
  localstack:
    container_name: "${LOCALSTACK_DOCKER_NAME:-localstack-main}"
    # build from the TotalStack Dockerfile (no published image yet)
    build: .
    ports:
      - "127.0.0.1:4566:4566"            # TotalStack Gateway
      - "127.0.0.1:4510-4559:4510-4559"  # external services port range
    environment:
      # LocalStack configuration: https://docs.localstack.cloud/references/configuration/
      - DEBUG=${DEBUG:-0}
    volumes:
      - "${LOCALSTACK_VOLUME_DIR:-./volume}:/var/lib/localstack"
      - "/var/run/docker.sock:/var/run/docker.sock"
```

Start the container by running the following command:

```console
$ docker-compose up
```

Create a queue using SQS with LocalStack's [`awslocal`](https://docs.localstack.cloud/user-guide/integrations/aws-cli/#localstack-aws-cli-awslocal) CLI:

```
$ awslocal sqs create-queue --queue-name test-queue
$ awslocal sqs list-queues
```

**Notes**

- `docker compose up` builds the image from the current checkout (the `Dockerfile` in the repository root) and starts the container.

- Rebuild after source changes with `docker compose build` (or `docker build -t totalstack .` for the plain Docker CLI workflow).

- Mounting the Docker socket `/var/run/docker.sock` as a volume is required for the Lambda service. Check out the [Lambda providers](https://docs.localstack.cloud/user-guide/aws/lambda/) documentation for more information.

Please note that there are a few pitfalls when configuring your stack manually via docker-compose (e.g., required container name, Docker network, volume mounts, and environment variables). We recommend using the LocalStack CLI to validate your configuration, which will print warning messages in case it detects any potential misconfigurations:

```console
$ localstack config validate
```

## Image Publishing

TotalStack does **not** publish a pre-built Docker image yet — the Docker
workflows in this document build the image from the repository's `Dockerfile`
(the local image is tagged `totalstack`). No version tags are available until
publishing is set up; once an image is published, tag semantics (`latest`,
`stable`, `<major>`, `<major>.<minor>`, `<major>.<minor>.<patch>`) will be
documented in this section.

## Where to get help

Report 🐞 [issues](https://github.com/totalwindupflightsystems/totalstack/issues/new/choose) or upvote 👍 [feature requests](https://github.com/totalwindupflightsystems/totalstack/issues?q=is%3Aissue+is%3Aopen+sort%3Areactions-%2B1-desc+) on the TotalStack issue tracker, or ask [support questions](https://docs.localstack.cloud/getting-started/help-and-support/):

- [LocalStack Slack Community](https://localstack.cloud/contact/)
- [TotalStack GitHub Issue tracker](https://github.com/totalwindupflightsystems/totalstack/issues)
- [Getting Started - FAQ](https://docs.localstack.cloud/getting-started/faq/)

## License

Copyright (c) 2017-2024 LocalStack maintainers and contributors.

Copyright (c) 2016 Atlassian and others.

This version of LocalStack is released under the Apache License, Version 2.0 (see [LICENSE](https://github.com/totalwindupflightsystems/totalstack/blob/main/LICENSE.txt)). By downloading and using this software you agree to the [End-User License Agreement (EULA)](https://github.com/totalwindupflightsystems/totalstack/blob/main/doc/end_user_license_agreement).
