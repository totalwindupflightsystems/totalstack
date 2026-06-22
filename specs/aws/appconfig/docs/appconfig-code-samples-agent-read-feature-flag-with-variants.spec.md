---
id: "@specs/aws/appconfig/docs/appconfig-code-samples-agent-read-feature-flag-with-variants"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Using AWS AppConfig Agent to retrieve a feature flag with variants"
status: active
depends_on:
  - "@specs/aws/appconfig/meta"
---

# Using AWS AppConfig Agent to retrieve a feature flag with variants

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appconfig/docs/appconfig-code-samples-agent-read-feature-flag-with-variants
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Using AWS AppConfig Agent to retrieve a feature flag with variants
<a name="appconfig-code-samples-agent-read-feature-flag-with-variants"></a>

Each of the following samples includes comments about the actions performed by the code.

------
#### [ Java ]

```
public static void retrieveConfigFromAgentWithVariants() throws Exception {
    /*
    This sample retrieves feature flag configuration data 
    containing variants from AWS AppConfig Agent.

    For more information about the agent, see [How to use AWS AppConfig Agent](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-agent-how-to-use.html)
    */

    // Make a GET request to the agent's local server to retrieve the configuration data
    URL url = new URL("http://localhost:2772/applications/MyDemoApp/environments/Beta/configurations/MyConfigProfile");
    HttpURLConnection con = (HttpURLConnection) url.openConnection();

    // Provide context in the 'Context' header
    // In the header value, use '=' to separate context key from context value
    // Note: Multiple context values may be passed either across 
    // multiple headers or as comma-separated values in a single header
    con.setRequestProperty("Context", "country=US");

    StringBuilder content;
    try (BufferedReader in = new BufferedReader(new InputStreamReader(con.getInputStream()))) {
        content = new StringBuilder();
        int ch;
        while ((ch = in.read()) != -1) {
            content.append((char) ch);
        }
    }
    con.disconnect();
    System.out.println("Configuration from agent via HTTP: " + content);
}
```

------
#### [ Python ]

```
# This sample retrieve features flag configuration data 
# containing variants from AWS AppConfig Agent.

# For more information about the agent, see [How to use AWS AppConfig Agent](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-agent-how-to-use.html)

import requests

application_name = 'MyDemoApp'
environment_name = 'Beta'
configuration_profile_name = 'MyConfigProfile'

# make a GET request to the agent's local server to retrieve the configuration data
response = requests.get(f"http://localhost:2772/applications/{{{application_name}}}/environments/{{{environment_name}}}/configurations/{{{configuration_profile_name}}}",
                        headers = {
                            "Context": "country=US" # Provide context in the 'Context' header
                                                    # In the header value, use '=' to separate context key from context value
                                                    # Note: Multiple context values may be passed either across 
                                                    # multiple headers or as comma-separated values in a single header
                        }
)
print("Configuration from agent via HTTP: ", response.json())
```

------
#### [ JavaScript ]

```
// This sample retrieves feature flag configuration data 
// containing variants from AWS AppConfig Agent.

// For more information about the agent, see [How to use AWS AppConfig Agent](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-agent-how-to-use.html)

const application_name = "MyDemoApp";
const environment_name = "Beta";
const configuration_profile_name = "MyConfigProfile";

const url = `http://localhost:2772/applications/${{{application_name}}}/environments/${{{environment_name}}}/configurations/${{{configuration_profile_name}}}`;

// make a GET request to the agent's local server to retrieve the configuration data
const response = await fetch(url, {
    method: 'GET',
    headers: {
        'Context': 'country=US' // Provide context in the 'Context' header
                                // In the header value, use '=' to separate context key from context value
                                // Note: Multiple context values may be passed either across 
                                // multiple headers or as comma-separated values in a single header
    }
});

const config = await response.json();
console.log("Configuration from agent via HTTP: ", config);
```

------