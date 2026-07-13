---
id: "@specs/aws/iam/list_ssh_public_keys"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_ListSSHPublicKeys"
---

# ListSSHPublicKeys

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/list_ssh_public_keys
> **spec:implements:** @kind:operation ListSSHPublicKeys
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_ListSSHPublicKeys.spec.md

Returns information about the SSH public keys associated with the specified IAM user. If none exists, the operation returns an empty list. The SSH public keys returned by this operation are used only for authenticating the IAM user to an CodeCommit repository. For more information about using SSH keys to authenticate to an CodeCommit repository, see Set up CodeCommit for SSH connections in the CodeCommit User Guide . Although each user is limited to a small number of keys, you can still paginate the results using the MaxItems and Marker parameters.

## Input Shape: ListSSHPublicKeysRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Marker | Any  # complex shape |  | Use this parameter only when paginating results and only after you receive a response indicating that the results are tr |
| MaxItems | Any  # complex shape |  | Use this only when paginating results to indicate the maximum number of items you want in the response. If additional it |
| UserName | Any  # complex shape |  | The name of the IAM user to list SSH public keys for. If none is specified, the UserName field is determined implicitly  |

## Output Shape: ListSSHPublicKeysResponse

- **IsTruncated** (Any  # complex shape): A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent 
- **Marker** (Any  # complex shape): When IsTruncated is true , this element is present and contains the value to use for the Marker parameter in a subsequen
- **SSHPublicKeys** (Any  # complex shape): A list of the SSH public keys assigned to IAM user.

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.

## Implementation

```speclang
def list_ssh_public_keys(store, request: dict) -> dict:
    """Returns information about the SSH public keys associated with the specified IAM user. If none exists, the operation returns an empty list. The SSH public keys returned by this operation are used only """

    items = store.list_ssh_public_keyss()
    return {"SSHPublicKeys": list(items.values())}
```
