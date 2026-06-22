---
id: "@specs/aws/appconfig/docs/appconfig-integration-containers-agent-configuring"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS (Optional) Using environment variables to configure AWS AppConfig Agent for Amazon ECS and Amazon EKS"
status: active
depends_on:
  - "@specs/aws/appconfig/meta"
---

# (Optional) Using environment variables to configure AWS AppConfig Agent for Amazon ECS and Amazon EKS

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appconfig/docs/appconfig-integration-containers-agent-configuring
> **target_lang:** meta — documentation tier. ALL sections preserved.



# (Optional) Using environment variables to configure AWS AppConfig Agent for Amazon ECS and Amazon EKS
<a name="appconfig-integration-containers-agent-configuring"></a>

You can configure AWS AppConfig Agent by changing the following environment variables for your agent container.

**Note**  
The following table includes a **Sample values** column. Depending on your monitor resolution, you might need to scroll to the bottom of the table and then scroll to the right to view the column.


****  

| Environment variable | Details | Default value | Sample value(s) | 
| --- | --- | --- | --- | 
| `ACCESS_TOKEN` | This environment variable defines a token that must be provided when requesting configuration data from the agent HTTP server. The value of the token must be set in the HTTP request authorization header with an authorization type of `Bearer`. Here is an example.<pre>GET /applications/my_app/...<br />                  Host: localhost:2772<br />                  Authorization: Bearer <token value></pre> | None | MyAccessToken | 
| `BACKUP_DIRECTORY` | This environment variable enables AWS AppConfig Agent to save a backup of each configuration it retrieves to the specified directory.  Configurations backed up to disk are not encrypted. If your configuration contains sensitive data, AWS AppConfig recommends that you practice the principle of least privilege with your filesystem permissions. For more information, see [Security in AWS AppConfig](appconfig-security.md).  | None | /path/to/backups | 
| `HTTP_PORT` | This environment variable specifies the port on which the HTTP server for the agent runs. | 2772 | 2772 | 
| `HTTP_HOST` | The HTTP\_HOST variable controls how the AWS AppConfig Agent binds to network interfaces. The binding behavior differs based on the runtime environment to ensure optimal security and accessibility. |  ECS, EKS [See the AWS documentation website for more details](http://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-integration-containers-agent-configuring.html)<br />EC2 and on-prem[See the AWS documentation website for more details](http://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-integration-containers-agent-configuring.html) | Custom Configuration Options. You can override the default behavior using these values:[See the AWS documentation website for more details](http://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-integration-containers-agent-configuring.html) | 
| `LOG_LEVEL` | This environment variable specifies the level of detail that the agent logs. Each level includes the current level and all higher levels. The value is case insensitive. From most to least detailed, the log levels are: `trace`, `debug`, `info`, `warn`, `error`, `fatal`, and `none`. The `trace` log includes detailed information, including timing information, about the agent. | info | trace<br />debug<br />info<br />warn<br />error<br />fatal<br />none | 
| `LOG_PATH` | The disk location where logs are written. If not specified, logs are written to stderr. | None | /path/to/logs/agent.log | 
| `MANIFEST` | This environment variable configures AWS AppConfig Agent to take advantage of additional per-configuration features like multi-account retrievals and save configuration to disk. For more information about these features, see [Using a manifest to enable additional retrieval features](appconfig-agent-how-to-use-additional-features.md).  | None | When using AWS AppConfig configuration as manifest: `MyApp:MyEnv:MyManifestConfig`.<br />When loading manifest from disk: `file:/path/to/manifest.json` | 
| `MAX_CONNECTIONS` | This environment variable configures the maximum number of connections that the agent uses to retrieve configurations from AWS AppConfig.  | 3 | 3 | 
| `POLL_INTERVAL` | This environment variable controls how often the agent polls AWS AppConfig for updated configuration data. You can specify a number of seconds for the interval. You can also specify a number with a time unit: s for seconds, m for minutes, and h for hours. If a unit isn't specified, the agent defaults to seconds. For example, 60, 60s, and 1m result in the same poll interval.  | 45 seconds | 45<br />45s<br />5m<br />1h | 
| `PREFETCH_LIST` | This environment variable specifies the configuration data the agent requests from AWS AppConfig as soon as it starts. Multiple configuration identifiers may be provided in a comma-separated list. | None | MyApp:MyEnv:MyConfig<br />abcd123:efgh456:ijkl789<br />MyApp:MyEnv:Config1,MyApp:MyEnv:Config2 | 
| `PRELOAD_BACKUPS` | If set to `true`, AWS AppConfig Agent loads configuration backups found in the `BACKUP_DIRECTORY` into memory and immediately checks to see if a newer version exists from the service. If set to `false`, AWS AppConfig Agent only loads the contents from a configuration backup if it cannot retrieve configuration data from the service, for example if there is a problem with your network. | true | true<br />false | 
| PROXY\_HEADERS | This environment variable specifies headers that are required by the proxy referenced in the PROXY\_URL environment variable. The value is a comma-separated list of headers.  | None | header: value<br />h1: v1, h2: v2 | 
| PROXY\_URL | This environment variable specifies the proxy URL to use for connections from the agent to AWS services, including AWS AppConfig. HTTPS and HTTP URLs are supported. | None | http://localhost:7474<br />https://my-proxy.example.com | 
| `REQUEST_TIMEOUT` | This environment variable controls the amount of time the agent waits for a response from AWS AppConfig. If the service does not respond, the request fails.<br />If the request is for the initial data retrieval, the agent returns an error to your application.<br />If the timeout occurs during a background check for updated data, the agent logs the error and tries again after a short delay.<br />You can specify the number of milliseconds for the timeout. You can also specify a number with a time unit: ms for milliseconds and s for seconds. If a unit isn't specified, the agent defaults to milliseconds. As an example, 5000, 5000ms and 5s result in the same request timeout value. | 3000ms | 3000<br />3000ms<br />5s | 
| ROLE\_ARN | This environment variable specifies the Amazon Resource Name (ARN) of an IAM role. AWS AppConfig Agent assumes this role to retrieve configuration data. | None | arn:aws:iam::123456789012:role/MyRole | 
| ROLE\_EXTERNAL\_ID | This environment variable specifies the external ID to use with the assumed role ARN. | None | MyExternalId | 
| ROLE\_SESSION\_NAME | This environment variable specifies the session name to be associated with the credentials for the assumed IAM role. | None | AWSAppConfigAgentSession | 
| SERVICE\_REGION | This environment variable specifies an alternative AWS Region that AWS AppConfig Agent uses to call the AWS AppConfig service. If left undefined, the agent attempts to determine the current Region. If it can't, the agent fails to start. | None | us-east-1<br />eu-west-1 | 
| `WAIT_ON_MANIFEST` | This environment variable configures AWS AppConfig Agent to wait until the manifest is processed before completing startup. | true | true<br />false | 