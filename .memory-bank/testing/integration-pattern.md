# Integration Test Pattern

## Template: DynamoDB CreateTable Integration Test

```python
"""
Integration test for DynamoDB CreateTable operation.
Tests the spec-generated create_table() function against a real DynamoDBStore.
"""
import pytest
import sys
import os

# Add localstack to path so we can import stores
LOCALSTACK_CORE = os.path.join(os.path.dirname(__file__), '../../../../../../localstack-core')
sys.path.insert(0, LOCALSTACK_CORE)

from localstack.services.dynamodb.models import DynamoDBStore, DynamoDBTable
from localstack.aws.api.dynamodb import (
    ValidationException,
    ResourceInUseException,
    ResourceNotFoundException,
)

# Import the generated handler
# Path: specs/aws/.speclang/assembled/create-table.code.py
import importlib.util

def _load_generated_handler(name):
    """Load a generated handler module from the assembled directory."""
    path = os.path.join(os.path.dirname(__file__), f'../{name}.code.py')
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

create_table_mod = _load_generated_handler('create-table')
create_table = create_table_mod.create_table


class TestCreateTableIntegration:
    """Integration tests for CreateTable — using REAL DynamoDBStore."""

    @pytest.fixture
    def store(self):
        """Fresh store for each test."""
        s = DynamoDBStore()
        return s

    def test_create_simple_table(self, store):
        """Happy path: create a table with HASH key only."""
        request = {
            'TableName': 'TestTable',
            'KeySchema': [{'AttributeName': 'id', 'KeyType': 'HASH'}],
            'AttributeDefinitions': [{'AttributeName': 'id', 'AttributeType': 'S'}],
            'BillingMode': 'PAY_PER_REQUEST',
        }
        response = create_table(store, request)

        assert 'TableDescription' in response
        desc = response['TableDescription']
        assert desc['TableName'] == 'TestTable'
        assert desc['TableStatus'] in ('CREATING', 'ACTIVE')
        assert store.table_exists('TestTable')

    def test_create_table_missing_name(self, store):
        """Error path: TableName is required."""
        request = {
            'KeySchema': [{'AttributeName': 'id', 'KeyType': 'HASH'}],
            'AttributeDefinitions': [{'AttributeName': 'id', 'AttributeType': 'S'}],
        }
        with pytest.raises(ValidationException):
            create_table(store, request)

    def test_create_table_duplicate(self, store):
        """Error path: table already exists."""
        request = {
            'TableName': 'DupTable',
            'KeySchema': [{'AttributeName': 'id', 'KeyType': 'HASH'}],
            'AttributeDefinitions': [{'AttributeName': 'id', 'AttributeType': 'S'}],
            'BillingMode': 'PAY_PER_REQUEST',
        }
        create_table(store, request)  # First call succeeds
        with pytest.raises(ResourceInUseException):
            create_table(store, request)  # Second call fails

    def test_create_table_with_gsi(self, store):
        """Create table with a Global Secondary Index."""
        request = {
            'TableName': 'GSITable',
            'KeySchema': [{'AttributeName': 'pk', 'KeyType': 'HASH'}],
            'AttributeDefinitions': [
                {'AttributeName': 'pk', 'AttributeType': 'S'},
                {'AttributeName': 'sk', 'AttributeType': 'S'},
            ],
            'GlobalSecondaryIndexes': [{
                'IndexName': 'sk-index',
                'KeySchema': [{'AttributeName': 'sk', 'KeyType': 'HASH'}],
                'Projection': {'ProjectionType': 'ALL'},
            }],
            'BillingMode': 'PAY_PER_REQUEST',
        }
        response = create_table(store, request)
        desc = response['TableDescription']
        assert len(desc.get('GlobalSecondaryIndexes', [])) == 1
        assert desc['GlobalSecondaryIndexes'][0]['IndexName'] == 'sk-index'

    def test_get_item_on_created_table(self, store):
        """Chain: create table → get item (not found) → verify error."""
        get_item_mod = _load_generated_handler('get-item')
        get_item = get_item_mod.get_item

        # Create table
        request = {
            'TableName': 'ReadTable',
            'KeySchema': [{'AttributeName': 'pk', 'KeyType': 'HASH'}],
            'AttributeDefinitions': [{'AttributeName': 'pk', 'AttributeType': 'S'}],
            'BillingMode': 'PAY_PER_REQUEST',
        }
        create_table(store, request)

        # Try to read nonexistent item
        with pytest.raises(ResourceNotFoundException):
            get_item(store, {
                'TableName': 'ReadTable',
                'Key': {'pk': {'S': 'missing'}},
            })
```

## General Pattern for Any Service

```python
"""
Integration test pattern for any TotalStack service.

1. Load generated handler module from .speclang/assembled/{operation}.code.py
2. Import real LocalStack store/model classes
3. Import AWS API exception classes
4. Test: happy path, error path, edge case
5. Verify: response shape, store state changes, exception types
"""

import pytest
import os, sys, importlib.util

# Path setup — project root relative
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../../../'))
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'localstack-core'))

# Import stores and exceptions
from localstack.services.{service}.models import {Service}Store
from localstack.aws.api.{service} import ValidationException, ResourceNotFoundException


def _load_handler(op_name):
    """Load a generated code.py module."""
    path = os.path.join(os.path.dirname(__file__), f'../{op_name}.code.py')
    spec = importlib.util.spec_from_file_location(op_name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class Test{Service}Integration:

    @pytest.fixture
    def store(self):
        return {Service}Store()

    def test_create_happy_path(self, store):
        """Create resource → verify store state."""
        ...

    def test_create_missing_required(self, store):
        """Missing required field → ValidationException."""
        ...

    def test_get_nonexistent(self, store):
        """Read nonexistent → ResourceNotFoundException."""
        ...

    def test_delete_then_get(self, store):
        """Delete → get → ResourceNotFoundException."""
        ...
```

## Running Integration Tests

```bash
# First: install localstack
cd ~/totalstack && pip install -e localstack-core/

# Then run integration tests for a service
pytest -x --tb=short specs/aws/.speclang/assembled/_tests/test_dynamodb_integration.py -v

# Or all services
pytest -x --tb=short specs/aws/.speclang/assembled/_tests/ -v
```
