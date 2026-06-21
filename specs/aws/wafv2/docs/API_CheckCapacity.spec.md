---
id: "@specs/aws/wafv2/docs/API_CheckCapacity"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CheckCapacity"
status: active
depends_on:
  - "@specs/aws/wafv2/meta"
---

# CheckCapacity

> **source:** AWS Documentation
> **spec:id:** @specs/aws/wafv2/docs/API_CheckCapacity
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CheckCapacity
<a name="API_CheckCapacity"></a>

Returns the web ACL capacity unit (WCU) requirements for a specified scope and set of rules. You can use this to check the capacity requirements for the rules you want to use in a [RuleGroup](API_RuleGroup.md) or [WebACL](API_WebACL.md). 

 AWS WAF uses WCUs to calculate and control the operating resources that are used to run your rules, rule groups, and web ACLs. AWS WAF calculates capacity differently for each rule type, to reflect the relative cost of each rule. Simple rules that cost little to run use fewer WCUs than more complex rules that use more processing power. Rule group capacity is fixed at creation, which helps users plan their web ACL WCU usage when they use a rule group. For more information, see [AWS WAF web ACL capacity units (WCU)](https://docs.aws.amazon.com/waf/latest/developerguide/aws-waf-capacity-units.html) in the * AWS WAF Developer Guide*. 

## Request Syntax
<a name="API_CheckCapacity_RequestSyntax"></a>

```
{
   "Rules": [ 
      { 
         "Action": { 
            "Allow": { 
               "CustomRequestHandling": { 
                  "InsertHeaders": [ 
                     { 
                        "Name": "{{string}}",
                        "Value": "{{string}}"
                     }
                  ]
               }
            },
            "Block": { 
               "CustomResponse": { 
                  "CustomResponseBodyKey": "{{string}}",
                  "ResponseCode": {{number}},
                  "ResponseHeaders": [ 
                     { 
                        "Name": "{{string}}",
                        "Value": "{{string}}"
                     }
                  ]
               }
            },
            "Captcha": { 
               "CustomRequestHandling": { 
                  "InsertHeaders": [ 
                     { 
                        "Name": "{{string}}",
                        "Value": "{{string}}"
                     }
                  ]
               }
            },
            "Challenge": { 
               "CustomRequestHandling": { 
                  "InsertHeaders": [ 
                     { 
                        "Name": "{{string}}",
                        "Value": "{{string}}"
                     }
                  ]
               }
            },
            "Count": { 
               "CustomRequestHandling": { 
                  "InsertHeaders": [ 
                     { 
                        "Name": "{{string}}",
                        "Value": "{{string}}"
                     }
                  ]
               }
            },
            "Monetize": { 
               "PriceMultiplier": "{{string}}"
            }
         },
         "CaptchaConfig": { 
            "ImmunityTimeProperty": { 
               "ImmunityTime": {{number}}
            }
         },
         "ChallengeConfig": { 
            "ImmunityTimeProperty": { 
               "ImmunityTime": {{number}}
            }
         },
         "Name": "{{string}}",
         "OverrideAction": { 
            "Count": { 
               "CustomRequestHandling": { 
                  "InsertHeaders": [ 
                     { 
                        "Name": "{{string}}",
                        "Value": "{{string}}"
                     }
                  ]
               }
            },
            "None": { 
            }
         },
         "Priority": {{number}},
         "RuleLabels": [ 
            { 
               "Name": "{{string}}"
            }
         ],
         "Statement": { 
            "AndStatement": { 
               "Statements": [ 
                  "Statement"
               ]
            },
            "AsnMatchStatement": { 
               "AsnList": [ {{number}} ],
               "ForwardedIPConfig": { 
                  "FallbackBehavior": "{{string}}",
                  "HeaderName": "{{string}}"
               }
            },
            "ByteMatchStatement": { 
               "FieldToMatch": { 
                  "AllQueryArguments": { 
                  },
                  "Body": { 
                     "OversizeHandling": "{{string}}"
                  },
                  "Cookies": { 
                     "MatchPattern": { 
                        "All": { 
                        },
                        "ExcludedCookies": [ "{{string}}" ],
                        "IncludedCookies": [ "{{string}}" ]
                     },
                     "MatchScope": "{{string}}",
                     "OversizeHandling": "{{string}}"
                  },
                  "HeaderOrder": { 
                     "OversizeHandling": "{{string}}"
                  },
                  "Headers": { 
                     "MatchPattern": { 
                        "All": { 
                        },
                        "ExcludedHeaders": [ "{{string}}" ],
                        "IncludedHeaders": [ "{{string}}" ]
                     },
                     "MatchScope": "{{string}}",
                     "OversizeHandling": "{{string}}"
                  },
                  "JA3Fingerprint": { 
                     "FallbackBehavior": "{{string}}"
                  },
                  "JA4Fingerprint": { 
                     "FallbackBehavior": "{{string}}"
                  },
                  "JsonBody": { 
                     "InvalidFallbackBehavior": "{{string}}",
                     "MatchPattern": { 
                        "All": { 
                        },
                        "IncludedPaths": [ "{{string}}" ]
                     },
                     "MatchScope": "{{string}}",
                     "OversizeHandling": "{{string}}"
                  },
                  "Method": { 
                  },
                  "QueryString": { 
                  },
                  "SingleHeader": { 
                     "Name": "{{string}}"
                  },
                  "SingleQueryArgument": { 
                     "Name": "{{string}}"
                  },
                  "UriFragment": { 
                     "FallbackBehavior": "{{string}}"
                  },
                  "UriPath": { 
                  }
               },
               "PositionalConstraint": "{{string}}",
               "SearchString": {{blob}},
               "TextTransformations": [ 
                  { 
                     "Priority": {{number}},
                     "Type": "{{string}}"
                  }
               ]
            },
            "GeoMatchStatement": { 
               "CountryCodes": [ "{{string}}" ],
               "ForwardedIPConfig": { 
                  "FallbackBehavior": "{{string}}",
                  "HeaderName": "{{string}}"
               }
            },
            "IPSetReferenceStatement": { 
               "ARN": "{{string}}",
               "IPSetForwardedIPConfig": { 
                  "FallbackBehavior": "{{string}}",
                  "HeaderName": "{{string}}",
                  "Position": "{{string}}"
               }
            },
            "LabelMatchStatement": { 
               "Key": "{{string}}",
               "Scope": "{{string}}"
            },
            "ManagedRuleGroupStatement": { 
               "ExcludedRules": [ 
                  { 
                     "Name": "{{string}}"
                  }
               ],
               "ManagedRuleGroupConfigs": [ 
                  { 
                     "AWSManagedRulesACFPRuleSet": { 
                        "CreationPath": "{{string}}",
                        "EnableRegexInPath": {{boolean}},
                        "RegistrationPagePath": "{{string}}",
                        "RequestInspection": { 
                           "AddressFields": [ 
                              { 
                                 "Identifier": "{{string}}"
                              }
                           ],
                           "EmailField": { 
                              "Identifier": "{{string}}"
                           },
                           "PasswordField": { 
                              "Identifier": "{{string}}"
                           },
                           "PayloadType": "{{string}}",
                           "PhoneNumberFields": [ 
                              { 
                                 "Identifier": "{{string}}"
                              }
                           ],
                           "UsernameField": { 
                              "Identifier": "{{string}}"
                           }
                        },
                        "ResponseInspection": { 
                           "BodyContains": { 
                              "FailureStrings": [ "{{string}}" ],
                              "SuccessStrings": [ "{{string}}" ]
                           },
                           "Header": { 
                              "FailureValues": [ "{{string}}" ],
                              "Name": "{{string}}",
                              "SuccessValues": [ "{{string}}" ]
                           },
                           "Json": { 
                              "FailureValues": [ "{{string}}" ],
                              "Identifier": "{{string}}",
                              "SuccessValues": [ "{{string}}" ]
                           },
                           "StatusCode": { 
                              "FailureCodes": [ {{number}} ],
                              "SuccessCodes": [ {{number}} ]
                           }
                        }
                     },
                     "AWSManagedRulesAntiDDoSRuleSet": { 
                        "ClientSideActionConfig": { 
                           "Challenge": { 
                              "ExemptUriRegularExpressions": [ 
                                 { 
                                    "RegexString": "{{string}}"
                                 }
                              ],
                              "Sensitivity": "{{string}}",
                              "UsageOfAction": "{{string}}"
                           }
                        },
                        "SensitivityToBlock": "{{string}}"
                     },
                     "AWSManagedRulesATPRuleSet": { 
                        "EnableRegexInPath": {{boolean}},
                        "LoginPath": "{{string}}",
                        "RequestInspection": { 
                           "PasswordField": { 
                              "Identifier": "{{string}}"
                           },
                           "PayloadType": "{{string}}",
                           "UsernameField": { 
                              "Identifier": "{{string}}"
                           }
                        },
                        "ResponseInspection": { 
                           "BodyContains": { 
                              "FailureStrings": [ "{{string}}" ],
                              "SuccessStrings": [ "{{string}}" ]
                           },
                           "Header": { 
                              "FailureValues": [ "{{string}}" ],
                              "Name": "{{string}}",
                              "SuccessValues": [ "{{string}}" ]
                           },
                           "Json": { 
                              "FailureValues": [ "{{string}}" ],
                              "Identifier": "{{string}}",
                              "SuccessValues": [ "{{string}}" ]
                           },
                           "StatusCode": { 
                              "FailureCodes": [ {{number}} ],
                              "SuccessCodes": [ {{number}} ]
                           }
                        }
                     },
                     "AWSManagedRulesBotControlRuleSet": { 
                        "EnableMachineLearning": {{boolean}},
                        "InspectionLevel": "{{string}}"
                     },
                     "LoginPath": "{{string}}",
                     "PasswordField": { 
                        "Identifier": "{{string}}"
                     },
                     "PayloadType": "{{string}}",
                     "UsernameField": { 
                        "Identifier": "{{string}}"
                     }
                  }
               ],
               "Name": "{{string}}",
               "RuleActionOverrides": [ 
                  { 
                     "ActionToUse": { 
                        "Allow": { 
                           "CustomRequestHandling": { 
                              "InsertHeaders": [ 
                                 { 
                                    "Name": "{{string}}",
                                    "Value": "{{string}}"
                                 }
                              ]
                           }
                        },
                        "Block": { 
                           "CustomResponse": { 
                              "CustomResponseBodyKey": "{{string}}",
                              "ResponseCode": {{number}},
                              "ResponseHeaders": [ 
                                 { 
                                    "Name": "{{string}}",
                                    "Value": "{{string}}"
                                 }
                              ]
                           }
                        },
                        "Captcha": { 
                           "CustomRequestHandling": { 
                              "InsertHeaders": [ 
                                 { 
                                    "Name": "{{string}}",
                                    "Value": "{{string}}"
                                 }
                              ]
                           }
                        },
                        "Challenge": { 
                           "CustomRequestHandling": { 
                              "InsertHeaders": [ 
                                 { 
                                    "Name": "{{string}}",
                                    "Value": "{{string}}"
                                 }
                              ]
                           }
                        },
                        "Count": { 
                           "CustomRequestHandling": { 
                              "InsertHeaders": [ 
                                 { 
                                    "Name": "{{string}}",
                                    "Value": "{{string}}"
                                 }
                              ]
                           }
                        },
                        "Monetize": { 
                           "PriceMultiplier": "{{string}}"
                        }
                     },
                     "Name": "{{string}}"
                  }
               ],
               "ScopeDownStatement": "Statement",
               "VendorName": "{{string}}",
               "Version": "{{string}}"
            },
            "NotStatement": { 
               "Statement": "Statement"
            },
            "OrStatement": { 
               "Statements": [ 
                  "Statement"
               ]
            },
            "RateBasedStatement": { 
               "AggregateKeyType": "{{string}}",
               "CustomKeys": [ 
                  { 
                     "ASN": { 
                     },
                     "Cookie": { 
                        "Name": "{{string}}",
                        "TextTransformations": [ 
                           { 
                              "Priority": {{number}},
                              "Type": "{{string}}"
                           }
                        ]
                     },
                     "ForwardedIP": { 
                     },
                     "Header": { 
                        "Name": "{{string}}",
                        "TextTransformations": [ 
                           { 
                              "Priority": {{number}},
                              "Type": "{{string}}"
                           }
                        ]
                     },
                     "HTTPMethod": { 
                     },
                     "IP": { 
                     },
                     "JA3Fingerprint": { 
                        "FallbackBehavior": "{{string}}"
                     },
                     "JA4Fingerprint": { 
                        "FallbackBehavior": "{{string}}"
                     },
                     "LabelNamespace": { 
                        "Namespace": "{{string}}"
                     },
                     "QueryArgument": { 
                        "Name": "{{string}}",
                        "TextTransformations": [ 
                           { 
                              "Priority": {{number}},
                              "Type": "{{string}}"
                           }
                        ]
                     },
                     "QueryString": { 
                        "TextTransformations": [ 
                           { 
                              "Priority": {{number}},
                              "Type": "{{string}}"
                           }
                        ]
                     },
                     "UriPath": { 
                        "TextTransformations": [ 
                           { 
                              "Priority": {{number}},
                              "Type": "{{string}}"
                           }
                        ]
                     }
                  }
               ],
               "EvaluationWindowSec": {{number}},
               "ForwardedIPConfig": { 
                  "FallbackBehavior": "{{string}}",
                  "HeaderName": "{{string}}"
               },
               "Limit": {{number}},
               "ScopeDownStatement": "Statement"
            },
            "RegexMatchStatement": { 
               "FieldToMatch": { 
                  "AllQueryArguments": { 
                  },
                  "Body": { 
                     "OversizeHandling": "{{string}}"
                  },
                  "Cookies": { 
                     "MatchPattern": { 
                        "All": { 
                        },
                        "ExcludedCookies": [ "{{string}}" ],
                        "IncludedCookies": [ "{{string}}" ]
                     },
                     "MatchScope": "{{string}}",
                     "OversizeHandling": "{{string}}"
                  },
                  "HeaderOrder": { 
                     "OversizeHandling": "{{string}}"
                  },
                  "Headers": { 
                     "MatchPattern": { 
                        "All": { 
                        },
                        "ExcludedHeaders": [ "{{string}}" ],
                        "IncludedHeaders": [ "{{string}}" ]
                     },
                     "MatchScope": "{{string}}",
                     "OversizeHandling": "{{string}}"
                  },
                  "JA3Fingerprint": { 
                     "FallbackBehavior": "{{string}}"
                  },
                  "JA4Fingerprint": { 
                     "FallbackBehavior": "{{string}}"
                  },
                  "JsonBody": { 
                     "InvalidFallbackBehavior": "{{string}}",
                     "MatchPattern": { 
                        "All": { 
                        },
                        "IncludedPaths": [ "{{string}}" ]
                     },
                     "MatchScope": "{{string}}",
                     "OversizeHandling": "{{string}}"
                  },
                  "Method": { 
                  },
                  "QueryString": { 
                  },
                  "SingleHeader": { 
                     "Name": "{{string}}"
                  },
                  "SingleQueryArgument": { 
                     "Name": "{{string}}"
                  },
                  "UriFragment": { 
                     "FallbackBehavior": "{{string}}"
                  },
                  "UriPath": { 
                  }
               },
               "RegexString": "{{string}}",
               "TextTransformations": [ 
                  { 
                     "Priority": {{number}},
                     "Type": "{{string}}"
                  }
               ]
            },
            "RegexPatternSetReferenceStatement": { 
               "ARN": "{{string}}",
               "FieldToMatch": { 
                  "AllQueryArguments": { 
                  },
                  "Body": { 
                     "OversizeHandling": "{{string}}"
                  },
                  "Cookies": { 
                     "MatchPattern": { 
                        "All": { 
                        },
                        "ExcludedCookies": [ "{{string}}" ],
                        "IncludedCookies": [ "{{string}}" ]
                     },
                     "MatchScope": "{{string}}",
                     "OversizeHandling": "{{string}}"
                  },
                  "HeaderOrder": { 
                     "OversizeHandling": "{{string}}"
                  },
                  "Headers": { 
                     "MatchPattern": { 
                        "All": { 
                        },
                        "ExcludedHeaders": [ "{{string}}" ],
                        "IncludedHeaders": [ "{{string}}" ]
                     },
                     "MatchScope": "{{string}}",
                     "OversizeHandling": "{{string}}"
                  },
                  "JA3Fingerprint": { 
                     "FallbackBehavior": "{{string}}"
                  },
                  "JA4Fingerprint": { 
                     "FallbackBehavior": "{{string}}"
                  },
                  "JsonBody": { 
                     "InvalidFallbackBehavior": "{{string}}",
                     "MatchPattern": { 
                        "All": { 
                        },
                        "IncludedPaths": [ "{{string}}" ]
                     },
                     "MatchScope": "{{string}}",
                     "OversizeHandling": "{{string}}"
                  },
                  "Method": { 
                  },
                  "QueryString": { 
                  },
                  "SingleHeader": { 
                     "Name": "{{string}}"
                  },
                  "SingleQueryArgument": { 
                     "Name": "{{string}}"
                  },
                  "UriFragment": { 
                     "FallbackBehavior": "{{string}}"
                  },
                  "UriPath": { 
                  }
               },
               "TextTransformations": [ 
                  { 
                     "Priority": {{number}},
                     "Type": "{{string}}"
                  }
               ]
            },
            "RuleGroupReferenceStatement": { 
               "ARN": "{{string}}",
               "ExcludedRules": [ 
                  { 
                     "Name": "{{string}}"
                  }
               ],
               "RuleActionOverrides": [ 
                  { 
                     "ActionToUse": { 
                        "Allow": { 
                           "CustomRequestHandling": { 
                              "InsertHeaders": [ 
                                 { 
                                    "Name": "{{string}}",
                                    "Value": "{{string}}"
                                 }
                              ]
                           }
                        },
                        "Block": { 
                           "CustomResponse": { 
                              "CustomResponseBodyKey": "{{string}}",
                              "ResponseCode": {{number}},
                              "ResponseHeaders": [ 
                                 { 
                                    "Name": "{{string}}",
                                    "Value": "{{string}}"
                                 }
                              ]
                           }
                        },
                        "Captcha": { 
                           "CustomRequestHandling": { 
                              "InsertHeaders": [ 
                                 { 
                                    "Name": "{{string}}",
                                    "Value": "{{string}}"
                                 }
                              ]
                           }
                        },
                        "Challenge": { 
                           "CustomRequestHandling": { 
                              "InsertHeaders": [ 
                                 { 
                                    "Name": "{{string}}",
                                    "Value": "{{string}}"
                                 }
                              ]
                           }
                        },
                        "Count": { 
                           "CustomRequestHandling": { 
                              "InsertHeaders": [ 
                                 { 
                                    "Name": "{{string}}",
                                    "Value": "{{string}}"
                                 }
                              ]
                           }
                        },
                        "Monetize": { 
                           "PriceMultiplier": "{{string}}"
                        }
                     },
                     "Name": "{{string}}"
                  }
               ]
            },
            "SizeConstraintStatement": { 
               "ComparisonOperator": "{{string}}",
               "FieldToMatch": { 
                  "AllQueryArguments": { 
                  },
                  "Body": { 
                     "OversizeHandling": "{{string}}"
                  },
                  "Cookies": { 
                     "MatchPattern": { 
                        "All": { 
                        },
                        "ExcludedCookies": [ "{{string}}" ],
                        "IncludedCookies": [ "{{string}}" ]
                     },
                     "MatchScope": "{{string}}",
                     "OversizeHandling": "{{string}}"
                  },
                  "HeaderOrder": { 
                     "OversizeHandling": "{{string}}"
                  },
                  "Headers": { 
                     "MatchPattern": { 
                        "All": { 
                        },
                        "ExcludedHeaders": [ "{{string}}" ],
                        "IncludedHeaders": [ "{{string}}" ]
                     },
                     "MatchScope": "{{string}}",
                     "OversizeHandling": "{{string}}"
                  },
                  "JA3Fingerprint": { 
                     "FallbackBehavior": "{{string}}"
                  },
                  "JA4Fingerprint": { 
                     "FallbackBehavior": "{{string}}"
                  },
                  "JsonBody": { 
                     "InvalidFallbackBehavior": "{{string}}",
                     "MatchPattern": { 
                        "All": { 
                        },
                        "IncludedPaths": [ "{{string}}" ]
                     },
                     "MatchScope": "{{string}}",
                     "OversizeHandling": "{{string}}"
                  },
                  "Method": { 
                  },
                  "QueryString": { 
                  },
                  "SingleHeader": { 
                     "Name": "{{string}}"
                  },
                  "SingleQueryArgument": { 
                     "Name": "{{string}}"
                  },
                  "UriFragment": { 
                     "FallbackBehavior": "{{string}}"
                  },
                  "UriPath": { 
                  }
               },
               "Size": {{number}},
               "TextTransformations": [ 
                  { 
                     "Priority": {{number}},
                     "Type": "{{string}}"
                  }
               ]
            },
            "SqliMatchStatement": { 
               "FieldToMatch": { 
                  "AllQueryArguments": { 
                  },
                  "Body": { 
                     "OversizeHandling": "{{string}}"
                  },
                  "Cookies": { 
                     "MatchPattern": { 
                        "All": { 
                        },
                        "ExcludedCookies": [ "{{string}}" ],
                        "IncludedCookies": [ "{{string}}" ]
                     },
                     "MatchScope": "{{string}}",
                     "OversizeHandling": "{{string}}"
                  },
                  "HeaderOrder": { 
                     "OversizeHandling": "{{string}}"
                  },
                  "Headers": { 
                     "MatchPattern": { 
                        "All": { 
                        },
                        "ExcludedHeaders": [ "{{string}}" ],
                        "IncludedHeaders": [ "{{string}}" ]
                     },
                     "MatchScope": "{{string}}",
                     "OversizeHandling": "{{string}}"
                  },
                  "JA3Fingerprint": { 
                     "FallbackBehavior": "{{string}}"
                  },
                  "JA4Fingerprint": { 
                     "FallbackBehavior": "{{string}}"
                  },
                  "JsonBody": { 
                     "InvalidFallbackBehavior": "{{string}}",
                     "MatchPattern": { 
                        "All": { 
                        },
                        "IncludedPaths": [ "{{string}}" ]
                     },
                     "MatchScope": "{{string}}",
                     "OversizeHandling": "{{string}}"
                  },
                  "Method": { 
                  },
                  "QueryString": { 
                  },
                  "SingleHeader": { 
                     "Name": "{{string}}"
                  },
                  "SingleQueryArgument": { 
                     "Name": "{{string}}"
                  },
                  "UriFragment": { 
                     "FallbackBehavior": "{{string}}"
                  },
                  "UriPath": { 
                  }
               },
               "SensitivityLevel": "{{string}}",
               "TextTransformations": [ 
                  { 
                     "Priority": {{number}},
                     "Type": "{{string}}"
                  }
               ]
            },
            "XssMatchStatement": { 
               "FieldToMatch": { 
                  "AllQueryArguments": { 
                  },
                  "Body": { 
                     "OversizeHandling": "{{string}}"
                  },
                  "Cookies": { 
                     "MatchPattern": { 
                        "All": { 
                        },
                        "ExcludedCookies": [ "{{string}}" ],
                        "IncludedCookies": [ "{{string}}" ]
                     },
                     "MatchScope": "{{string}}",
                     "OversizeHandling": "{{string}}"
                  },
                  "HeaderOrder": { 
                     "OversizeHandling": "{{string}}"
                  },
                  "Headers": { 
                     "MatchPattern": { 
                        "All": { 
                        },
                        "ExcludedHeaders": [ "{{string}}" ],
                        "IncludedHeaders": [ "{{string}}" ]
                     },
                     "MatchScope": "{{string}}",
                     "OversizeHandling": "{{string}}"
                  },
                  "JA3Fingerprint": { 
                     "FallbackBehavior": "{{string}}"
                  },
                  "JA4Fingerprint": { 
                     "FallbackBehavior": "{{string}}"
                  },
                  "JsonBody": { 
                     "InvalidFallbackBehavior": "{{string}}",
                     "MatchPattern": { 
                        "All": { 
                        },
                        "IncludedPaths": [ "{{string}}" ]
                     },
                     "MatchScope": "{{string}}",
                     "OversizeHandling": "{{string}}"
                  },
                  "Method": { 
                  },
                  "QueryString": { 
                  },
                  "SingleHeader": { 
                     "Name": "{{string}}"
                  },
                  "SingleQueryArgument": { 
                     "Name": "{{string}}"
                  },
                  "UriFragment": { 
                     "FallbackBehavior": "{{string}}"
                  },
                  "UriPath": { 
                  }
               },
               "TextTransformations": [ 
                  { 
                     "Priority": {{number}},
                     "Type": "{{string}}"
                  }
               ]
            }
         },
         "VisibilityConfig": { 
            "CloudWatchMetricsEnabled": {{boolean}},
            "MetricName": "{{string}}",
            "SampledRequestsEnabled": {{boolean}}
         }
      }
   ],
   "Scope": "{{string}}"
}
```

## Request Parameters
<a name="API_CheckCapacity_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Rules](#API_CheckCapacity_RequestSyntax) **   <a name="WAF-CheckCapacity-request-Rules"></a>
An array of [Rule](API_Rule.md) that you're configuring to use in a rule group or web ACL.   
Type: Array of [Rule](API_Rule.md) objects  
Required: Yes

 ** [Scope](#API_CheckCapacity_RequestSyntax) **   <a name="WAF-CheckCapacity-request-Scope"></a>
Specifies whether this is for a global resource type, such as a Amazon CloudFront distribution. For an AWS Amplify application, use `CLOUDFRONT`.  
To work with CloudFront, you must also specify the Region US East (N. Virginia) as follows:   
+ CLI - Specify the Region when you use the CloudFront scope: `--scope=CLOUDFRONT --region=us-east-1`. 
+ API and SDKs - For all calls, use the Region endpoint us-east-1. 
Type: String  
Valid Values: `CLOUDFRONT | REGIONAL`   
Required: Yes

## Response Syntax
<a name="API_CheckCapacity_ResponseSyntax"></a>

```
{
   "Capacity": number
}
```

## Response Elements
<a name="API_CheckCapacity_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Capacity](#API_CheckCapacity_ResponseSyntax) **   <a name="WAF-CheckCapacity-response-Capacity"></a>
The capacity required by the rules and scope.  
Type: Long  
Valid Range: Minimum value of 0.

## Errors
<a name="API_CheckCapacity_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** WAFExpiredManagedRuleGroupVersionException **   
The operation failed because the specified version for the managed rule group has expired. You can retrieve the available versions for the managed rule group by calling [ListAvailableManagedRuleGroupVersions](API_ListAvailableManagedRuleGroupVersions.md).  
HTTP Status Code: 400

 ** WAFInternalErrorException **   
Your request is valid, but AWS WAF couldn’t perform the operation because of a system problem. Retry your request.   
HTTP Status Code: 500

 ** WAFInvalidOperationException **   
The operation isn't valid.   
HTTP Status Code: 400

 ** WAFInvalidParameterException **   
The operation failed because AWS WAF didn't recognize a parameter in the request. For example:   
+ You specified a parameter name or value that isn't valid.
+ Your nested statement isn't valid. You might have tried to nest a statement that can’t be nested. 
+ You tried to update a `WebACL` with a `DefaultAction` that isn't among the types available at [DefaultAction](API_DefaultAction.md).
+ Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL can't be associated.  
 ** Field **   
The settings where the invalid parameter was found.   
 ** Parameter **   
The invalid parameter that resulted in the exception.   
 ** Reason **   
Additional information about the exception.
HTTP Status Code: 400

 ** WAFInvalidResourceException **   
 AWS WAF couldn’t perform the operation because the resource that you requested isn’t valid. Check the resource, and try again.  
HTTP Status Code: 400

 ** WAFLimitsExceededException **   
 AWS WAF couldn’t perform the operation because you exceeded your resource limit. For example, the maximum number of `WebACL` objects that you can create for an AWS account. For more information, see [AWS WAF quotas](https://docs.aws.amazon.com/waf/latest/developerguide/limits.html) in the * AWS WAF Developer Guide*.    
 ** SourceType **   
Source type for the exception. 
HTTP Status Code: 400

 ** WAFNonexistentItemException **   
 AWS WAF couldn’t perform the operation because your resource doesn't exist. If you've just created a resource that you're using in this operation, you might just need to wait a few minutes. It can take from a few seconds to a number of minutes for changes to propagate.   
HTTP Status Code: 400

 ** WAFSubscriptionNotFoundException **   
You tried to use a managed rule group that's available by subscription, but you aren't subscribed to it yet.   
HTTP Status Code: 400

 ** WAFUnavailableEntityException **   
 AWS WAF couldn’t retrieve a resource that you specified for this operation. If you've just created a resource that you're using in this operation, you might just need to wait a few minutes. It can take from a few seconds to a number of minutes for changes to propagate. Verify the resource specifications in your request parameters and then retry the operation.  
HTTP Status Code: 400

## See Also
<a name="API_CheckCapacity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wafv2-2019-07-29/CheckCapacity) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wafv2-2019-07-29/CheckCapacity) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/CheckCapacity) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wafv2-2019-07-29/CheckCapacity) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/CheckCapacity) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wafv2-2019-07-29/CheckCapacity) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wafv2-2019-07-29/CheckCapacity) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wafv2-2019-07-29/CheckCapacity) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/wafv2-2019-07-29/CheckCapacity) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/CheckCapacity) 