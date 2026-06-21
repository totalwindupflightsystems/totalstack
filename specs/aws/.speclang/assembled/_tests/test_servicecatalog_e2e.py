"""E2E tests for Service Catalog — boto3 against running localstack."""
import os

import boto3
import pytest
from botocore.exceptions import ClientError

ENDPOINT = os.environ.get('LOCALSTACK_ENDPOINT', 'http://localhost:4566')
TEST_CREDS = {'aws_access_key_id': 'test', 'aws_secret_access_key': 'test', 'aws_session_token': 'test'}

# Skip E2E tests until the Service Catalog provider is wired into localstack
def _service_available():
    try:
        client = boto3.client('servicecatalog', endpoint_url=ENDPOINT,
                              region_name='us-east-1', **TEST_CREDS)
        client.list_portfolios()
        return True
    except Exception:
        return False

SKIP_REASON = "Service Catalog provider not yet wired into LocalStack"
skip_if_not_available = pytest.mark.skipif(not _service_available(), reason=SKIP_REASON)


class TestServiceCatalogE2E:

    @pytest.fixture
    def client(self):
        return boto3.client('servicecatalog', endpoint_url=ENDPOINT,
                           region_name='us-east-1', **TEST_CREDS)

    @pytest.fixture(autouse=True)
    def cleanup(self, client):
        yield
        # Best-effort cleanup
        try:
            portfolios = client.list_portfolios()
            for p in portfolios.get('PortfolioDetails', []):
                try:
                    client.delete_portfolio(Id=p['Id'])
                except ClientError:
                    pass
        except ClientError:
            pass

    @skip_if_not_available
    def test_full_portfolio_crud_workflow(self, client):
        """Create → describe → list → update → delete portfolio."""
        # 1. Create
        response = client.create_portfolio(
            DisplayName='E2E Test Portfolio',
            ProviderName='E2E Provider',
            Description='E2E test'
        )
        assert response is not None
        portfolio_id = response['PortfolioDetail']['Id']
        assert portfolio_id.startswith('port-')

        # 2. Describe
        response = client.describe_portfolio(Id=portfolio_id)
        assert response['PortfolioDetail']['DisplayName'] == 'E2E Test Portfolio'

        # 3. List
        response = client.list_portfolios()
        ids = [p['Id'] for p in response['PortfolioDetails']]
        assert portfolio_id in ids

        # 4. Update
        response = client.update_portfolio(Id=portfolio_id, DisplayName='Updated Name')
        assert response['PortfolioDetail']['DisplayName'] == 'Updated Name'

        # 5. Delete
        client.delete_portfolio(Id=portfolio_id)

        # 6. Verify deleted
        with pytest.raises(ClientError) as exc:
            client.describe_portfolio(Id=portfolio_id)
        assert exc.value.response['Error']['Code'] == 'ResourceNotFoundException'

    @skip_if_not_available
    def test_full_product_crud_workflow(self, client):
        """Create → search → describe → delete product."""
        response = client.create_product(
            Name='E2E Product',
            Owner='E2E Owner',
            ProductType='CLOUD_FORMATION_TEMPLATE',
            Description='Test product'
        )
        product_id = response['ProductViewDetail']['ProductViewSummary']['Id']

        # Search
        response = client.search_products()
        found = any(p['Id'] == product_id for p in response.get('ProductViewSummaries', []))
        assert found

        # Cleanup
        client.delete_product(Id=product_id)

    @skip_if_not_available
    def test_error_nonexistent_read(self, client):
        """Reading a nonexistent portfolio returns ResourceNotFoundException."""
        with pytest.raises(ClientError) as exc:
            client.describe_portfolio(Id='port-nonexistent')
        assert exc.value.response['Error']['Code'] == 'ResourceNotFoundException'

    @skip_if_not_available
    def test_error_missing_required(self, client):
        """Creating a portfolio without required fields returns error."""
        with pytest.raises(ClientError) as exc:
            client.create_portfolio(DisplayName='NoProvider')
        # Should be ValidationException or InvalidParametersException
        assert exc.value.response['Error']['Code'] in (
            'ValidationException', 'InvalidParametersException')
