# E2E Test Pattern

## Template: DynamoDB E2E Workflow

```python
"""
E2E test for DynamoDB — full workflow via boto3 against running localstack.
Tests: create_table → describe_table → put_item → get_item → query → delete_table

Requires: localstack running on http://localhost:4566
         boto3 installed
"""

import os
import pytest
import boto3
from botocore.exceptions import ClientError

ENDPOINT = os.environ.get('LOCALSTACK_ENDPOINT', 'http://localhost:4566')
TABLE_NAME = 'e2e-test-table'


class TestDynamoDBE2E:
    """End-to-end DynamoDB workflow via boto3."""

    @pytest.fixture(autouse=True)
    def client(self):
        """boto3 DynamoDB client pointed at localstack."""
        return boto3.client(
            'dynamodb',
            endpoint_url=ENDPOINT,
            region_name='us-east-1',
            aws_access_key_id='test',
            aws_secret_access_key='test',
        )

    @pytest.fixture(autouse=True)
    def cleanup(self, client):
        """Ensure table is deleted after each test."""
        yield
        try:
            client.delete_table(TableName=TABLE_NAME)
        except ClientError:
            pass  # Already deleted or never created

    def test_full_crud_workflow(self, client):
        """Complete DynamoDB CRUD workflow."""
        # 1. CREATE TABLE
        client.create_table(
            TableName=TABLE_NAME,
            KeySchema=[{'AttributeName': 'pk', 'KeyType': 'HASH'}],
            AttributeDefinitions=[{'AttributeName': 'pk', 'AttributeType': 'S'}],
            BillingMode='PAY_PER_REQUEST',
        )

        # 2. DESCRIBE TABLE — verify status
        desc = client.describe_table(TableName=TABLE_NAME)
        table = desc['Table']
        assert table['TableName'] == TABLE_NAME
        assert table['TableStatus'] in ('CREATING', 'ACTIVE')

        # 3. PUT ITEM
        client.put_item(
            TableName=TABLE_NAME,
            Item={
                'pk': {'S': 'user-1'},
                'name': {'S': 'Alice'},
                'age': {'N': '30'},
            },
        )

        # 4. GET ITEM — verify read
        result = client.get_item(
            TableName=TABLE_NAME,
            Key={'pk': {'S': 'user-1'}},
        )
        assert 'Item' in result
        assert result['Item']['name']['S'] == 'Alice'
        assert result['Item']['age']['N'] == '30'

        # 5. UPDATE ITEM
        client.update_item(
            TableName=TABLE_NAME,
            Key={'pk': {'S': 'user-1'}},
            UpdateExpression='SET age = :new_age',
            ExpressionAttributeValues={':new_age': {'N': '31'}},
        )
        result = client.get_item(
            TableName=TABLE_NAME,
            Key={'pk': {'S': 'user-1'}},
        )
        assert result['Item']['age']['N'] == '31'

        # 6. DELETE ITEM
        client.delete_item(
            TableName=TABLE_NAME,
            Key={'pk': {'S': 'user-1'}},
        )
        result = client.get_item(
            TableName=TABLE_NAME,
            Key={'pk': {'S': 'user-1'}},
        )
        assert 'Item' not in result

        # 7. DELETE TABLE
        client.delete_table(TableName=TABLE_NAME)
        with pytest.raises(ClientError) as exc:
            client.describe_table(TableName=TABLE_NAME)
        assert exc.value.response['Error']['Code'] == 'ResourceNotFoundException'

    def test_create_table_duplicate(self, client):
        """E2E: ResourceInUseException on duplicate table."""
        client.create_table(
            TableName=TABLE_NAME,
            KeySchema=[{'AttributeName': 'pk', 'KeyType': 'HASH'}],
            AttributeDefinitions=[{'AttributeName': 'pk', 'AttributeType': 'S'}],
            BillingMode='PAY_PER_REQUEST',
        )
        with pytest.raises(ClientError) as exc:
            client.create_table(
                TableName=TABLE_NAME,
                KeySchema=[{'AttributeName': 'pk', 'KeyType': 'HASH'}],
                AttributeDefinitions=[{'AttributeName': 'pk', 'AttributeType': 'S'}],
                BillingMode='PAY_PER_REQUEST',
            )
        assert exc.value.response['Error']['Code'] == 'ResourceInUseException'

    def test_get_nonexistent_item(self, client):
        """E2E: empty result for nonexistent item (not an error in DynamoDB)."""
        client.create_table(
            TableName=TABLE_NAME,
            KeySchema=[{'AttributeName': 'pk', 'KeyType': 'HASH'}],
            AttributeDefinitions=[{'AttributeName': 'pk', 'AttributeType': 'S'}],
            BillingMode='PAY_PER_REQUEST',
        )
        result = client.get_item(
            TableName=TABLE_NAME,
            Key={'pk': {'S': 'ghost'}},
        )
        assert 'Item' not in result  # DynamoDB returns empty, not error
```

## General E2E Pattern

```python
"""
E2E test pattern for any TotalStack service.

1. boto3 client pointed at localstack endpoint
2. Full workflow: create → use → verify → cleanup
3. Error paths: invalid input, duplicates, not-found
4. Cleanup in fixture teardown

Requires:
- localstack running
- boto3 installed
- LOCALSTACK_ENDPOINT env var (default: http://localhost:4566)
"""

import os
import pytest
import boto3
from botocore.exceptions import ClientError

ENDPOINT = os.environ.get('LOCALSTACK_ENDPOINT', 'http://localhost:4566')
REGION = 'us-east-1'
TEST_CREDS = {'aws_access_key_id': 'test', 'aws_secret_access_key': 'test'}


class Test{Service}E2E:

    @pytest.fixture
    def client(self):
        return boto3.client('{service}', endpoint_url=ENDPOINT,
                           region_name=REGION, **TEST_CREDS)

    @pytest.fixture(autouse=True)
    def cleanup(self, client):
        yield
        # Clean up created resources
        ...

    def test_create_resource(self, client):
        """Create → describe → verify → delete."""
        ...

    def test_error_duplicate(self, client):
        """ResourceInUseException on duplicate."""
        ...

    def test_error_not_found(self, client):
        """ResourceNotFoundException for nonexistent resource."""
        ...
```

## Running E2E Tests

```bash
# 1. Start localstack (if not already running)
cd ~/totalstack && LOCALSTACK_AUTH_TOKEN=test python -m localstack.cli.main start &

# 2. Wait for it to be ready
curl -s http://localhost:4566/_localstack/health | jq '.services.dynamodb'

# 3. Run E2E tests
LOCALSTACK_ENDPOINT=http://localhost:4566 pytest -x --tb=short \
  specs/aws/.speclang/assembled/_tests/test_dynamodb_e2e.py -v

# 4. Stop localstack
kill %1
```
