---
id: "@specs/aws/appconfig/docs/appconfig-code-samples-agent-read-feature-flag"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Using AWS AppConfig Agent to read a specific feature flag"
status: active
depends_on:
  - "@specs/aws/appconfig/meta"
---

# Using AWS AppConfig Agent to read a specific feature flag

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appconfig/docs/appconfig-code-samples-agent-read-feature-flag
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Using AWS AppConfig Agent to read a specific feature flag
<a name="appconfig-code-samples-agent-read-feature-flag"></a>

Each of the following samples includes comments about the actions performed by the code.

------
#### [ Java ]

```
public void retrieveSingleFlagFromAgent() throws Exception {
        /*
          You can retrieve a single flag's data from the agent by providing the "flag" query string parameter.
          Note: the configuration's type must be AWS.AppConfig.FeatureFlags
        */

        URL url = new URL("http://localhost:2772/applications/MyDemoApp/environments/Beta/configurations/MyFlagsProfile?flag=myFlagKey");
        HttpURLConnection con = (HttpURLConnection) url.openConnection();
        con.setRequestMethod("GET");
        StringBuilder content;
        try (BufferedReader in = new BufferedReader(new InputStreamReader(con.getInputStream()))) {
            content = new StringBuilder();
            int ch;
            while ((ch = in.read()) != -1) {
                content.append((char) ch);
            }
        }
        con.disconnect();
        System.out.println("MyFlagName from agent: " + content);
    }
```

------
#### [ Python ]

```
import requests

application_name = 'MyDemoApp'
environment_name = 'MyEnvironment'
config_profile_name = 'MyConfigProfile'
flag_key = 'MyFlag'

# retrieve a single flag's data by providing the "flag" query string parameter
# note: the configuration's type must be AWS.AppConfig.FeatureFlags
response = requests.get(f"http://localhost:2772/applications/{application_name}/environments/{environment_name}/configurations/{config_profile_name}?flag={flag_key}") 
config = response.content
```

------
#### [ JavaScript ]

```
const application_name = "MyDemoApp";
const environment_name = "MyEnvironment";
const config_profile_name = "MyConfigProfile";
const flag_name = "MyFlag";

// retrieve a single flag's data by providing the "flag" query string parameter
// note: the configuration's type must be AWS.AppConfig.FeatureFlags
const url = `http://localhost:2772/applications/${application_name}/environments/${environment_name}/configurations/${config_profile_name}?flag=${flag_name}`;
const response = await fetch(url);
const flag = await response.json(); // { "enabled": true/false }
```

------