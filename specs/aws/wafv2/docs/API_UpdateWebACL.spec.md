---
id: "@specs/aws/wafv2/docs/API_UpdateWebACL"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateWebACL"
status: active
depends_on:
  - "@specs/aws/wafv2/meta"
---

# UpdateWebACL

> **source:** AWS Documentation
> **spec:id:** @specs/aws/wafv2/docs/API_UpdateWebACL
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateWebACL
<a name="API_UpdateWebACL"></a>

Updates the specified [WebACL](API_WebACL.md). While updating a web ACL, AWS WAF provides continuous coverage to the resources that you have associated with the web ACL. 

**Note**  
This operation completely replaces the mutable specifications that you already have for the web ACL with the ones that you provide to this call.   
To modify a web ACL, do the following:   
Retrieve it by calling [GetWebACL](API_GetWebACL.md) 
Update its settings as needed
Provide the complete web ACL specification to this call

 A web ACL defines a collection of rules to use to inspect and control web requests. Each rule has a statement that defines what to look for in web requests and an action that AWS WAF applies to requests that match the statement. In the web ACL, you assign a default action to take (allow, block) for any request that does not match any of the rules. The rules in a web ACL can be a combination of the types [Rule](API_Rule.md), [RuleGroup](API_RuleGroup.md), and managed rule group. You can associate a web ACL with one or more AWS resources to protect. The resource types include Amazon CloudFront distribution, Amazon API Gateway REST API, Application Load Balancer, AWS AppSync GraphQL API, Amazon Cognito user pool, AWS App Runner service, AWS Amplify application, and AWS Verified Access instance. 

 **Temporary inconsistencies during updates** 

When you create or change a web ACL or other AWS WAF resources, the changes take a small amount of time to propagate to all areas where the resources are stored. The propagation time can be from a few seconds to a number of minutes. 

The following are examples of the temporary inconsistencies that you might notice during change propagation: 
+ After you create a web ACL, if you try to associate it with a resource, you might get an exception indicating that the web ACL is unavailable. 
+ After you add a rule group to a web ACL, the new rule group rules might be in effect in one area where the web ACL is used and not in another.
+ After you change a rule action setting, you might see the old action in some places and the new action in others. 
+ After you add an IP address to an IP set that is in use in a blocking rule, the new address might be blocked in one area while still allowed in another.

## Request Syntax
<a name="API_UpdateWebACL_RequestSyntax"></a>

```
{
   "ApplicationConfig": { 
      "Attributes": [ 
         { 
            "Name": "{{string}}",
            "Values": [ "{{string}}" ]
         }
      ]
   },
   "AssociationConfig": { 
      "RequestBody": { 
         "{{string}}" : { 
            "DefaultSizeInspectionLimit": "{{string}}"
         }
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
   "CustomResponseBodies": { 
      "{{string}}" : { 
         "Content": "{{string}}",
         "ContentType": "{{string}}"
      }
   },
   "DataProtectionConfig": { 
      "DataProtections": [ 
         { 
            "Action": "{{string}}",
            "ExcludeRateBasedDetails": {{boolean}},
            "ExcludeRuleMatchDetails": {{boolean}},
            "Field": { 
               "FieldKeys": [ "{{string}}" ],
               "FieldType": "{{string}}"
            }
         }
      ]
   },
   "DefaultAction": { 
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
      }
   },
   "Description": "{{string}}",
   "Id": "{{string}}",
   "LockToken": "{{string}}",
   "MonetizationConfig": { 
      "CryptoConfig": { 
         "PaymentNetworks": [ 
            { 
               "Chain": "{{string}}",
               "Prices": [ 
                  { 
                     "Amount": "{{string}}",
                     "Currency": "{{string}}"
                  }
               ],
               "WalletAddress": "{{string}}"
            }
         ]
      },
      "CurrencyMode": "{{string}}"
   },
   "Name": "{{string}}",
   "OnSourceDDoSProtectionConfig": { 
      "ALBLowReputationMode": "{{string}}"
   },
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
   "Scope": "{{string}}",
   "TokenDomains": [ "{{string}}" ],
   "VisibilityConfig": { 
      "CloudWatchMetricsEnabled": {{boolean}},
      "MetricName": "{{string}}",
      "SampledRequestsEnabled": {{boolean}}
   }
}
```

## Request Parameters
<a name="API_UpdateWebACL_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ApplicationConfig](#API_UpdateWebACL_RequestSyntax) **   <a name="WAF-UpdateWebACL-request-ApplicationConfig"></a>
Configures the ability for the AWS WAF console to store and retrieve application attributes. Application attributes help AWS WAF give recommendations for protection packs.  
When using `UpdateWebACL`, `ApplicationConfig` follows these rules:  
+ If you omit `ApplicationConfig` from the request, all existing entries in the web ACL are retained.
+ If you include `ApplicationConfig`, entries must match the existing values exactly. Any attempt to modify existing entries will result in an error.
Type: [ApplicationConfig](API_ApplicationConfig.md) object  
Required: No

 ** [AssociationConfig](#API_UpdateWebACL_RequestSyntax) **   <a name="WAF-UpdateWebACL-request-AssociationConfig"></a>
Specifies custom configurations for the associations between the web ACL and protected resources.   
Use this to customize the maximum size of the request body that your protected resources forward to AWS WAF for inspection. You can customize this setting for CloudFront, API Gateway, Amazon Cognito, App Runner, or Verified Access resources. The default setting is 16 KB (16,384 bytes).   
You are charged additional fees when your protected resources forward body sizes that are larger than the default. For more information, see [AWS WAF Pricing](http://aws.amazon.com/waf/pricing/).
For Application Load Balancer and AWS AppSync, the limit is fixed at 8 KB (8,192 bytes).  
Type: [AssociationConfig](API_AssociationConfig.md) object  
Required: No

 ** [CaptchaConfig](#API_UpdateWebACL_RequestSyntax) **   <a name="WAF-UpdateWebACL-request-CaptchaConfig"></a>
Specifies how AWS WAF should handle `CAPTCHA` evaluations for rules that don't have their own `CaptchaConfig` settings. If you don't specify this, AWS WAF uses its default settings for `CaptchaConfig`.   
Type: [CaptchaConfig](API_CaptchaConfig.md) object  
Required: No

 ** [ChallengeConfig](#API_UpdateWebACL_RequestSyntax) **   <a name="WAF-UpdateWebACL-request-ChallengeConfig"></a>
Specifies how AWS WAF should handle challenge evaluations for rules that don't have their own `ChallengeConfig` settings. If you don't specify this, AWS WAF uses its default settings for `ChallengeConfig`.   
Type: [ChallengeConfig](API_ChallengeConfig.md) object  
Required: No

 ** [CustomResponseBodies](#API_UpdateWebACL_RequestSyntax) **   <a name="WAF-UpdateWebACL-request-CustomResponseBodies"></a>
A map of custom response keys and content bodies. When you create a rule with a block action, you can send a custom response to the web request. You define these for the web ACL, and then use them in the rules and default actions that you define in the web ACL.   
For information about customizing web requests and responses, see [Customizing web requests and responses in AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-custom-request-response.html) in the * AWS WAF Developer Guide*.   
For information about the limits on count and size for custom request and response settings, see [AWS WAF quotas](https://docs.aws.amazon.com/waf/latest/developerguide/limits.html) in the * AWS WAF Developer Guide*.   
Type: String to [CustomResponseBody](API_CustomResponseBody.md) object map  
Map Entries: Maximum number of items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `^[\w\-]+$`   
Required: No

 ** [DataProtectionConfig](#API_UpdateWebACL_RequestSyntax) **   <a name="WAF-UpdateWebACL-request-DataProtectionConfig"></a>
Specifies data protection to apply to the web request data for the web ACL. This is a web ACL level data protection option.   
The data protection that you configure for the web ACL alters the data that's available for any other data collection activity, including your AWS WAF logging destinations, web ACL request sampling, and Amazon Security Lake data collection and management. Your other option for data protection is in the logging configuration, which only affects logging.   
Type: [DataProtectionConfig](API_DataProtectionConfig.md) object  
Required: No

 ** [DefaultAction](#API_UpdateWebACL_RequestSyntax) **   <a name="WAF-UpdateWebACL-request-DefaultAction"></a>
The action to perform if none of the `Rules` contained in the `WebACL` match.   
Type: [DefaultAction](API_DefaultAction.md) object  
Required: Yes

 ** [Description](#API_UpdateWebACL_RequestSyntax) **   <a name="WAF-UpdateWebACL-request-Description"></a>
A description of the web ACL that helps with identification.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^[\w+=:#@/\-,\.][\w+=:#@/\-,\.\s]+[\w+=:#@/\-,\.]$`   
Required: No

 ** [Id](#API_UpdateWebACL_RequestSyntax) **   <a name="WAF-UpdateWebACL-request-Id"></a>
The unique identifier for the web ACL. This ID is returned in the responses to create and list commands. You provide it to operations like update and delete.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 36.  
Pattern: `^[0-9a-f]{8}-(?:[0-9a-f]{4}-){3}[0-9a-f]{12}$`   
Required: Yes

 ** [LockToken](#API_UpdateWebACL_RequestSyntax) **   <a name="WAF-UpdateWebACL-request-LockToken"></a>
A token used for optimistic locking. AWS WAF returns a token to your `get` and `list` requests, to mark the state of the entity at the time of the request. To make changes to the entity associated with the token, you provide the token to operations like `update` and `delete`. AWS WAF uses the token to ensure that no changes have been made to the entity since you last retrieved it. If a change has been made, the update fails with a `WAFOptimisticLockException`. If this happens, perform another `get`, and use the new token returned by that operation.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 36.  
Pattern: `^[0-9a-f]{8}-(?:[0-9a-f]{4}-){3}[0-9a-f]{12}$`   
Required: Yes

 ** [MonetizationConfig](#API_UpdateWebACL_RequestSyntax) **   <a name="WAF-UpdateWebACL-request-MonetizationConfig"></a>
The monetization configuration for the web ACL. Provide this when any rule in the web ACL uses the `Monetize` action.  
Type: [MonetizationConfig](API_MonetizationConfig.md) object  
Required: No

 ** [Name](#API_UpdateWebACL_RequestSyntax) **   <a name="WAF-UpdateWebACL-request-Name"></a>
The name of the web ACL. You cannot change the name of a web ACL after you create it.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^[\w\-]+$`   
Required: Yes

 ** [OnSourceDDoSProtectionConfig](#API_UpdateWebACL_RequestSyntax) **   <a name="WAF-UpdateWebACL-request-OnSourceDDoSProtectionConfig"></a>
Specifies the type of DDoS protection to apply to web request data for a web ACL. For most scenarios, it is recommended to use the default protection level, `ACTIVE_UNDER_DDOS`. If a web ACL is associated with multiple Application Load Balancers, the changes you make to DDoS protection in that web ACL will apply to all associated Application Load Balancers.  
Type: [OnSourceDDoSProtectionConfig](API_OnSourceDDoSProtectionConfig.md) object  
Required: No

 ** [Rules](#API_UpdateWebACL_RequestSyntax) **   <a name="WAF-UpdateWebACL-request-Rules"></a>
The [Rule](API_Rule.md) statements used to identify the web requests that you want to manage. Each rule includes one top-level statement that AWS WAF uses to identify matching web requests, and parameters that govern how AWS WAF handles them.   
Type: Array of [Rule](API_Rule.md) objects  
Required: No

 ** [Scope](#API_UpdateWebACL_RequestSyntax) **   <a name="WAF-UpdateWebACL-request-Scope"></a>
Specifies whether this is for a global resource type, such as a Amazon CloudFront distribution. For an AWS Amplify application, use `CLOUDFRONT`.  
To work with CloudFront, you must also specify the Region US East (N. Virginia) as follows:   
+ CLI - Specify the Region when you use the CloudFront scope: `--scope=CLOUDFRONT --region=us-east-1`. 
+ API and SDKs - For all calls, use the Region endpoint us-east-1. 
Type: String  
Valid Values: `CLOUDFRONT | REGIONAL`   
Required: Yes

 ** [TokenDomains](#API_UpdateWebACL_RequestSyntax) **   <a name="WAF-UpdateWebACL-request-TokenDomains"></a>
Specifies the domains that AWS WAF should accept in a web request token. This enables the use of tokens across multiple protected websites. When AWS WAF provides a token, it uses the domain of the AWS resource that the web ACL is protecting. If you don't specify a list of token domains, AWS WAF accepts tokens only for the domain of the protected resource. With a token domain list, AWS WAF accepts the resource's host domain plus all domains in the token domain list, including their prefixed subdomains.  
Example JSON: `"TokenDomains": { "mywebsite.com", "myotherwebsite.com" }`   
Public suffixes aren't allowed. For example, you can't use `gov.au` or `co.uk` as token domains.  
Type: Array of strings  
Length Constraints: Minimum length of 1. Maximum length of 253.  
Pattern: `^[\w\.\-/]+$`   
Required: No

 ** [VisibilityConfig](#API_UpdateWebACL_RequestSyntax) **   <a name="WAF-UpdateWebACL-request-VisibilityConfig"></a>
Defines and enables Amazon CloudWatch metrics and web request sample collection.   
Type: [VisibilityConfig](API_VisibilityConfig.md) object  
Required: Yes

## Response Syntax
<a name="API_UpdateWebACL_ResponseSyntax"></a>

```
{
   "NextLockToken": "string"
}
```

## Response Elements
<a name="API_UpdateWebACL_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextLockToken](#API_UpdateWebACL_ResponseSyntax) **   <a name="WAF-UpdateWebACL-response-NextLockToken"></a>
A token used for optimistic locking. AWS WAF returns this token to your `update` requests. You use `NextLockToken` in the same manner as you use `LockToken`.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 36.  
Pattern: `^[0-9a-f]{8}-(?:[0-9a-f]{4}-){3}[0-9a-f]{12}$` 

## Errors
<a name="API_UpdateWebACL_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** WAFConfigurationWarningException **   
The operation failed because you are inspecting the web request body, headers, or cookies without specifying how to handle oversize components. Rules that inspect the body must either provide an `OversizeHandling` configuration or they must be preceded by a `SizeConstraintStatement` that blocks the body content from being too large. Rules that inspect the headers or cookies must provide an `OversizeHandling` configuration.   
Provide the handling configuration and retry your operation.  
Alternately, you can suppress this warning by adding the following tag to the resource that you provide to this operation: `Tag` (key:`WAF:OversizeFieldsHandlingConstraintOptOut`, value:`true`).  
HTTP Status Code: 400

 ** WAFDuplicateItemException **   
 AWS WAF couldn’t perform the operation because the resource that you tried to save is a duplicate of an existing one.  
HTTP Status Code: 400

 ** WAFExpiredManagedRuleGroupVersionException **   
The operation failed because the specified version for the managed rule group has expired. You can retrieve the available versions for the managed rule group by calling [ListAvailableManagedRuleGroupVersions](API_ListAvailableManagedRuleGroupVersions.md).  
HTTP Status Code: 400

 ** WAFFeatureNotIncludedInPricingPlanException **   
The operation failed because the specified AWS WAF feature isn't supported by the CloudFront pricing plan associated with the web ACL.    
 ** DisallowedFeatures **   
The names of the disallowed AWS WAF features.
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

 ** WAFOptimisticLockException **   
 AWS WAF couldn’t save your changes because you tried to update or delete a resource that has changed since you last retrieved it. Get the resource again, make any changes you need to make to the new copy, and retry your operation.   
HTTP Status Code: 400

 ** WAFSubscriptionNotFoundException **   
You tried to use a managed rule group that's available by subscription, but you aren't subscribed to it yet.   
HTTP Status Code: 400

 ** WAFUnavailableEntityException **   
 AWS WAF couldn’t retrieve a resource that you specified for this operation. If you've just created a resource that you're using in this operation, you might just need to wait a few minutes. It can take from a few seconds to a number of minutes for changes to propagate. Verify the resource specifications in your request parameters and then retry the operation.  
HTTP Status Code: 400

## See Also
<a name="API_UpdateWebACL_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wafv2-2019-07-29/UpdateWebACL) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wafv2-2019-07-29/UpdateWebACL) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/UpdateWebACL) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wafv2-2019-07-29/UpdateWebACL) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/UpdateWebACL) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wafv2-2019-07-29/UpdateWebACL) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wafv2-2019-07-29/UpdateWebACL) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wafv2-2019-07-29/UpdateWebACL) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/wafv2-2019-07-29/UpdateWebACL) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/UpdateWebACL) 