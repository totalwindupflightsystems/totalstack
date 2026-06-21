"""Integration tests for Service Catalog — real ServiceCatalogStore + generated handlers."""
import importlib.util
import os
import types

import pytest

ASSEMBLED_DIR = os.path.dirname(__file__)
SERVICE_DIR = os.path.join(ASSEMBLED_DIR, '..', 'servicecatalog')

# ── Load models.code.py dynamically ────────────────────────────
models_spec = importlib.util.spec_from_file_location(
    'models', os.path.join(SERVICE_DIR, 'models.code.py'))
models_mod = importlib.util.module_from_spec(models_spec)
models_spec.loader.exec_module(models_mod)

ServiceCatalogStore = models_mod.ServiceCatalogStore
InvalidParametersException = models_mod.InvalidParametersException
ResourceNotFoundException = models_mod.ResourceNotFoundException
ResourceInUseException = models_mod.ResourceInUseException
LimitExceededException = models_mod.LimitExceededException
DuplicateResourceException = models_mod.DuplicateResourceException
TagOptionNotMigratedException = models_mod.TagOptionNotMigratedException

# ── Module loader helpers ───────────────────────────────────────

def _load_handler(op_name):
    """Load a single-handler .code.py file — returns the first function found."""
    path = os.path.join(SERVICE_DIR, op_name + '.code.py')
    spec = importlib.util.spec_from_file_location(op_name, path)
    mod = importlib.util.module_from_spec(spec)
    # Inject exception classes (generated code references these without imports)
    mod.InvalidParametersException = InvalidParametersException
    mod.ResourceNotFoundException = ResourceNotFoundException
    # Find the handler function
    spec.loader.exec_module(mod)
    for v in mod.__dict__.values():
        if isinstance(v, types.FunctionType) and not v.__name__.startswith('_'):
            return v
    raise RuntimeError(f"No handler function found in {op_name}.code.py")


# ═══════════════════════════════════════════════════════════════════
# Portfolio Tests
# ═══════════════════════════════════════════════════════════════════

class TestPortfolio:
    @pytest.fixture
    def store(self):
        return ServiceCatalogStore()

    def test_create_portfolio_happy_path(self, store):
        handler = _load_handler('CreatePortfolio')
        response = handler(store, {
            'DisplayName': 'My Portfolio',
            'ProviderName': 'My Company',
            'Description': 'A test portfolio'
        })
        assert 'PortfolioDetail' in response
        detail = response['PortfolioDetail']
        assert detail['DisplayName'] == 'My Portfolio'
        assert detail['ProviderName'] == 'My Company'
        assert detail['Description'] == 'A test portfolio'
        assert detail['Id'].startswith('port-')

    def test_create_portfolio_missing_required(self, store):
        handler = _load_handler('CreatePortfolio')
        with pytest.raises(InvalidParametersException):
            handler(store, {})

    def test_describe_portfolio_happy_path(self, store):
        create = _load_handler('CreatePortfolio')
        desc = _load_handler('DescribePortfolio')
        created = create(store, {'DisplayName': 'P1', 'ProviderName': 'Co'})
        pid = created['PortfolioDetail']['Id']
        response = desc(store, {'Id': pid})
        assert response['PortfolioDetail']['DisplayName'] == 'P1'

    def test_describe_portfolio_nonexistent(self, store):
        handler = _load_handler('DescribePortfolio')
        with pytest.raises(ResourceNotFoundException):
            handler(store, {'Id': 'port-nonexistent'})

    def test_list_portfolios(self, store):
        create = _load_handler('CreatePortfolio')
        list_handler = _load_handler('ListPortfolios')
        create(store, {'DisplayName': 'P1', 'ProviderName': 'Co1'})
        create(store, {'DisplayName': 'P2', 'ProviderName': 'Co2'})
        response = list_handler(store, {})
        assert len(response['PortfolioDetails']) == 2

    def test_update_portfolio(self, store):
        create = _load_handler('CreatePortfolio')
        update = _load_handler('UpdatePortfolio')
        created = create(store, {'DisplayName': 'Old Name', 'ProviderName': 'Co'})
        pid = created['PortfolioDetail']['Id']
        response = update(store, {'Id': pid, 'DisplayName': 'New Name'})
        assert response['PortfolioDetail']['DisplayName'] == 'New Name'
        # ProviderName should be unchanged
        assert response['PortfolioDetail']['ProviderName'] == 'Co'

    def test_delete_portfolio(self, store):
        create = _load_handler('CreatePortfolio')
        delete = _load_handler('DeletePortfolio')
        desc = _load_handler('DescribePortfolio')
        created = create(store, {'DisplayName': 'P1', 'ProviderName': 'Co'})
        pid = created['PortfolioDetail']['Id']
        delete(store, {'Id': pid})
        with pytest.raises(ResourceNotFoundException):
            desc(store, {'Id': pid})


# ═══════════════════════════════════════════════════════════════════
# Product Tests
# ═══════════════════════════════════════════════════════════════════

class TestProduct:
    @pytest.fixture
    def store(self):
        return ServiceCatalogStore()

    def test_create_product_happy_path(self, store):
        handler = _load_handler('CreateProduct')
        response = handler(store, {
            'Name': 'My Product',
            'Owner': 'Owner Org',
            'ProductType': 'CLOUD_FORMATION_TEMPLATE',
            'Description': 'A test product'
        })
        assert 'ProductViewDetail' in response
        pvs = response['ProductViewDetail']['ProductViewSummary']
        assert pvs['Name'] == 'My Product'
        assert pvs['Owner'] == 'Owner Org'
        assert pvs['ProductType'] == 'CLOUD_FORMATION_TEMPLATE'

    def test_create_product_missing_required(self, store):
        handler = _load_handler('CreateProduct')
        with pytest.raises(InvalidParametersException):
            handler(store, {'Name': 'NoOwner'})

    def test_describe_product_happy_path(self, store):
        create = _load_handler('CreateProduct')
        desc = _load_handler('DescribeProduct')
        created = create(store, {'Name': 'P1', 'Owner': 'O1', 'ProductType': 'CFT'})
        pid = created['ProductViewDetail']['ProductViewSummary']['Id']
        response = desc(store, {'Id': pid})
        assert response['ProductViewDetail']['ProductViewSummary']['Name'] == 'P1'

    def test_describe_product_nonexistent(self, store):
        handler = _load_handler('DescribeProduct')
        with pytest.raises(ResourceNotFoundException):
            handler(store, {'Id': 'prod-nonexistent'})

    def test_search_products(self, store):
        create = _load_handler('CreateProduct')
        search = _load_handler('SearchProducts')
        create(store, {'Name': 'A', 'Owner': 'O1', 'ProductType': 'CFT'})
        create(store, {'Name': 'B', 'Owner': 'O2', 'ProductType': 'CFT'})
        response = search(store, {})
        assert len(response['ProductViewSummaries']) == 2

    def test_delete_product(self, store):
        create = _load_handler('CreateProduct')
        delete = _load_handler('DeleteProduct')
        desc = _load_handler('DescribeProduct')
        created = create(store, {'Name': 'X', 'Owner': 'O', 'ProductType': 'CFT'})
        pid = created['ProductViewDetail']['ProductViewSummary']['Id']
        delete(store, {'Id': pid})
        with pytest.raises(ResourceNotFoundException):
            desc(store, {'Id': pid})


# ═══════════════════════════════════════════════════════════════════
# Provisioning Artifact Tests
# ═══════════════════════════════════════════════════════════════════

class TestProvisioningArtifact:
    @pytest.fixture
    def store_with_product(self):
        store = ServiceCatalogStore()
        create = _load_handler('CreateProduct')
        create(store, {'Name': 'Base', 'Owner': 'O', 'ProductType': 'CFT'})
        return store

    def test_create_pa_happy_path(self, store_with_product):
        store = store_with_product
        product_id = list(store.products.keys())[0]
        handler = _load_handler('CreateProvisioningArtifact')
        response = handler(store, {
            'ProductId': product_id,
            'Parameters': {'Name': 'v1.0', 'Description': 'First version'}
        })
        assert 'ProvisioningArtifactDetail' in response
        assert response['ProvisioningArtifactDetail']['Name'] == 'v1.0'

    def test_create_pa_invalid_product(self, store_with_product):
        handler = _load_handler('CreateProvisioningArtifact')
        with pytest.raises(ResourceNotFoundException):
            handler(store_with_product, {'ProductId': 'prod-nonexistent', 'Parameters': {'Name': 'v'}})

    def test_list_pas(self, store_with_product):
        store = store_with_product
        product_id = list(store.products.keys())[0]
        create_pa = _load_handler('CreateProvisioningArtifact')
        list_pa = _load_handler('ListProvisioningArtifacts')
        create_pa(store, {'ProductId': product_id, 'Parameters': {'Name': 'v1'}})
        create_pa(store, {'ProductId': product_id, 'Parameters': {'Name': 'v2'}})
        response = list_pa(store, {'ProductId': product_id})
        assert len(response['ProvisioningArtifactDetails']) == 2


# ═══════════════════════════════════════════════════════════════════
# Constraint Tests
# ═══════════════════════════════════════════════════════════════════

class TestConstraint:
    @pytest.fixture
    def store(self):
        return ServiceCatalogStore()

    def test_create_constraint_happy_path(self, store):
        handler = _load_handler('CreateConstraint')
        response = handler(store, {
            'PortfolioId': 'port-1',
            'ProductId': 'prod-1',
            'Type': 'LAUNCH',
            'Parameters': '{"RoleArn": "arn:aws:iam::123:role/Test"}',
            'Description': 'Test constraint'
        })
        assert 'ConstraintDetail' in response
        assert response['ConstraintDetail']['Type'] == 'LAUNCH'
        assert response['ConstraintDetail']['ConstraintId'].startswith('const-')

    def test_create_constraint_missing_required(self, store):
        handler = _load_handler('CreateConstraint')
        with pytest.raises(InvalidParametersException):
            handler(store, {'PortfolioId': 'p-1', 'ProductId': 'p-2'})

    def test_describe_constraint_nonexistent(self, store):
        handler = _load_handler('DescribeConstraint')
        with pytest.raises(ResourceNotFoundException):
            handler(store, {'Id': 'const-nonexistent'})

    def test_delete_constraint(self, store):
        create = _load_handler('CreateConstraint')
        desc = _load_handler('DescribeConstraint')
        delete = _load_handler('DeleteConstraint')
        created = create(store, {
            'PortfolioId': 'p-1', 'ProductId': 'p-2',
            'Type': 'LAUNCH', 'Parameters': '{}'
        })
        cid = created['ConstraintDetail']['ConstraintId']
        delete(store, {'Id': cid})
        with pytest.raises(ResourceNotFoundException):
            desc(store, {'Id': cid})


# ═══════════════════════════════════════════════════════════════════
# Association Tests
# ═══════════════════════════════════════════════════════════════════

class TestAssociation:
    @pytest.fixture
    def store_with_both(self):
        store = ServiceCatalogStore()
        cpf = _load_handler('CreatePortfolio')
        cpr = _load_handler('CreateProduct')
        cpf(store, {'DisplayName': 'Port', 'ProviderName': 'Co'})
        cpr(store, {'Name': 'Prod', 'Owner': 'O', 'ProductType': 'CFT'})
        return store

    def test_associate_happy_path(self, store_with_both):
        store = store_with_both
        portfolio_id = list(store.portfolios.keys())[0]
        product_id = list(store.products.keys())[0]
        handler = _load_handler('AssociateProductWithPortfolio')
        handler(store, {'PortfolioId': portfolio_id, 'ProductId': product_id})
        assert product_id in store.portfolio_products[portfolio_id]

    def test_associate_nonexistent_portfolio(self, store_with_both):
        handler = _load_handler('AssociateProductWithPortfolio')
        product_id = list(store_with_both.products.keys())[0]
        with pytest.raises(ResourceNotFoundException):
            handler(store_with_both, {'PortfolioId': 'port-nonexistent', 'ProductId': product_id})

    def test_disassociate(self, store_with_both):
        store = store_with_both
        portfolio_id = list(store.portfolios.keys())[0]
        product_id = list(store.products.keys())[0]
        assoc = _load_handler('AssociateProductWithPortfolio')
        disassoc = _load_handler('DisassociateProductFromPortfolio')
        assoc(store, {'PortfolioId': portfolio_id, 'ProductId': product_id})
        disassoc(store, {'PortfolioId': portfolio_id, 'ProductId': product_id})
        assert product_id not in store.portfolio_products[portfolio_id]


# ═══════════════════════════════════════════════════════════════════
# Provisioned Product Tests
# ═══════════════════════════════════════════════════════════════════

class TestProvisionedProduct:
    @pytest.fixture
    def store_with_product(self):
        store = ServiceCatalogStore()
        create = _load_handler('CreateProduct')
        create(store, {'Name': 'Prod', 'Owner': 'O', 'ProductType': 'CFT'})
        return store

    def test_provision_happy_path(self, store_with_product):
        store = store_with_product
        product_id = list(store.products.keys())[0]
        handler = _load_handler('ProvisionProduct')
        response = handler(store, {
            'ProductId': product_id,
            'ProvisionedProductName': 'MyStack',
            'ProvisioningArtifactId': 'pa-test'
        })
        assert 'ProvisionedProductDetail' in response
        assert response['ProvisionedProductDetail']['Name'] == 'MyStack'

    def test_provision_nonexistent_product(self, store_with_product):
        handler = _load_handler('ProvisionProduct')
        with pytest.raises(ResourceNotFoundException):
            handler(store_with_product, {
                'ProductId': 'prod-nonexistent',
                'ProvisionedProductName': 'S',
                'ProvisioningArtifactId': 'pa-x'
            })

    def test_describe_provisioned_product(self, store_with_product):
        store = store_with_product
        product_id = list(store.products.keys())[0]
        provision = _load_handler('ProvisionProduct')
        desc = _load_handler('DescribeProvisionedProduct')
        created = provision(store, {
            'ProductId': product_id,
            'ProvisionedProductName': 'Stack1',
            'ProvisioningArtifactId': 'pa-1'
        })
        ppid = created['ProvisionedProductDetail']['Id']
        response = desc(store, {'Id': ppid})
        assert response['ProvisionedProductDetail']['Name'] == 'Stack1'

    def test_terminate_provisioned_product(self, store_with_product):
        store = store_with_product
        product_id = list(store.products.keys())[0]
        provision = _load_handler('ProvisionProduct')
        desc = _load_handler('DescribeProvisionedProduct')
        terminate = _load_handler('TerminateProvisionedProduct')
        created = provision(store, {
            'ProductId': product_id,
            'ProvisionedProductName': 'StackX',
            'ProvisioningArtifactId': 'pa-x'
        })
        ppid = created['ProvisionedProductDetail']['Id']
        terminate(store, {'ProvisionedProductId': ppid})
        with pytest.raises(ResourceNotFoundException):
            desc(store, {'Id': ppid})


# ═══════════════════════════════════════════════════════════════════
# Tag Option Tests
# ═══════════════════════════════════════════════════════════════════

class TestTagOption:
    @pytest.fixture
    def store(self):
        return ServiceCatalogStore()

    def test_create_tag_option_happy_path(self, store):
        handler = _load_handler('CreateTagOption')
        response = handler(store, {'Key': 'Environment', 'Value': 'Production'})
        assert 'TagOptionDetail' in response
        assert response['TagOptionDetail']['Key'] == 'Environment'
        assert response['TagOptionDetail']['Value'] == 'Production'

    def test_create_tag_option_missing_required(self, store):
        handler = _load_handler('CreateTagOption')
        with pytest.raises(InvalidParametersException):
            handler(store, {'Key': 'OnlyKey'})

    def test_list_tag_options(self, store):
        create = _load_handler('CreateTagOption')
        list_to = _load_handler('ListTagOptions')
        create(store, {'Key': 'Env', 'Value': 'Prod'})
        create(store, {'Key': 'Team', 'Value': 'Alpha'})
        response = list_to(store, {})
        assert len(response['TagOptionDetails']) == 2
