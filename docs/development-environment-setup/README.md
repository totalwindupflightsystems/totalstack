# Development Environment Setup

Before you get started with contributing to TotalStack, make sure you've familiarized yourself with TotalStack from the perspective of a user. Run the stack locally with `make start`, exercise a few AWS services against it with the AWS CLI or SDKs, and inspect the project structure described in [CONTRIBUTING.md](/docs/CONTRIBUTING.md). Once TotalStack runs in your Docker environment and you've played around with it, you can move forward to set up your developer environment.

## Development requirements

You will need the following tools for the local development of TotalStack.

* [Python](https://www.python.org/downloads/) and `pip`
    * We recommend to use a Python version management tool like [`pyenv`](https://github.com/pyenv/pyenv/).
    This way you will always use the correct Python version as defined in `.python-version`.
* [Node.js & npm](https://nodejs.org/en/download/)
* [Docker](https://docs.docker.com/desktop/)

We recommend you to individually install the above tools using your favorite package manager.
For example, on macOS, you can use [Homebrew](https://brew.sh/) to install the above tools.

### Setting up the Development Environment

To make contributions to TotalStack, you need to be able to run TotalStack in host mode from your IDE, and be able to attach a debugger to the running TotalStack instance.

The basic steps include:

1. Fork the TotalStack repository on GitHub [https://github.com/totalwindupflightsystems/totalstack/](https://github.com/totalwindupflightsystems/totalstack/)
2. Clone your fork `git clone git@github.com:<GITHUB_USERNAME>/totalstack.git`
3. Ensure you have `python`, `pip`, `node`, and `npm` installed.
> [!NOTE]
> You might also need `java` for some emulated services.
4. Install the Python dependencies using `make install`.
> [!NOTE]
> This will install the required pip dependencies in a local Python 3 `venv` directory called `.venv` (your global Python packages will remain untouched).
> Depending on your system, some `pip` modules may require additional native libs installed.

> [!NOTE]
> Consider running `make install-dev-types` to enable type hinting for efficient [integration tests](../testing/integration-tests/README.md) development.
5. Start TotalStack in host mode using `make start`

### Building the Docker image for Development

We generally recommend using this command to build the TotalStack Docker image locally (works on Linux/macOS):

```bash
IMAGE_NAME="totalwindupflightsystems/totalstack" ./bin/docker-helper.sh build
```

### Additional Dependencies for running TotalStack in Host Mode

In host mode, additional dependencies (e.g., Java) are required for developing certain AWS-emulated services (e.g., DynamoDB).
The required dependencies vary depending on the service, configuration, operating system, and system architecture (i.e., x86 vs ARM).
Refer to the [Dockerfile](https://github.com/totalwindupflightsystems/totalstack/blob/main/Dockerfile) for more details.

#### Root Permissions

TotalStack runs its own DNS server which listens for requests on port 53. This requires root permission. When TotalStack starts in host mode it runs the DNS server as sudo, so a prompt is triggered asking for the sudo password. This is annoying during local development, so to disable this functionality, use `DNS_ADDRESS=0`.

> [!NOTE]
> We don't recommend disabling the DNS server in general (e.g. in Docker) because the DNS server enables seamless connectivity to TotalStack from different environments via the domain name `localhost.localstack.cloud`.

#### Python Dependencies

* [JPype1](https://pypi.org/project/JPype1/) might require `g++` to fix a compile error on ARM Linux `gcc: fatal error: cannot execute 'cc1plus'`
  * Used in StepFunctions for JSONata

#### Test Dependencies

* Node.js is required for running TotalStack tests because the test fixture for CDK-based tests needs Node.js

#### DynamoDB

* [OpenJDK](https://openjdk.org/install/)

#### Kinesis

* [NodeJS & npm](https://nodejs.org/en/download/)

#### Lambda

* macOS users need to configure `LAMBDA_DEV_PORT_EXPOSE=1` such that the host can reach Lambda containers via IPv4 in bridge mode

### Tips

* If `virtualenv` chooses system python installations before your pyenv installations, manually initialize `virtualenv` before running `make install`: `virtualenv -p ~/.pyenv/shims/python .venv` .
* Set env variable `LS_LOG='trace'` to print every `http` request sent to TotalStack and their responses. It is useful for debugging certain issues.
* Catch linter or format errors early by installing Git pre-commit hooks via `pre-commit install`. [pre-commit](https://pre-commit.com/) installation: `pip install pre-commit` or `brew install pre-commit`.
