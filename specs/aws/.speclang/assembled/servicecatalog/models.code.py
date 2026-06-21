"""Service Catalog — stores, data classes, and exception classes."""
import time
from collections import defaultdict

# ── Exception Classes ──────────────────────────────────────────

class InvalidParametersException(Exception):
    """One or more parameters are not valid."""
    pass


class ResourceNotFoundException(Exception):
    """The specified resource was not found."""
    def __init__(self, resource_type="Resource", resource_id=""):
        self.resource_type = resource_type
        self.resource_id = resource_id
        super().__init__(f"{resource_type} not found: {resource_id}")


class ResourceInUseException(Exception):
    """The resource is in use and cannot be deleted."""
    pass


class LimitExceededException(Exception):
    """A service limit was exceeded."""
    pass


class DuplicateResourceException(Exception):
    """The specified resource already exists."""
    pass


class TagOptionNotMigratedException(Exception):
    """Tag option migration has not occurred."""
    pass


# ── Data Classes ────────────────────────────────────────────────

class PortfolioRecord:
    def __init__(self, Id, DisplayName, ProviderName, Description="", ARN=""):
        self.Id = Id
        self.DisplayName = DisplayName
        self.ProviderName = ProviderName
        self.Description = Description
        self.ARN = ARN
        self.CreatedTime = time.time()


class ProductRecord:
    def __init__(self, Id, Name, Owner, ProductType, Description="",
                 Distributor="", SupportDescription="", SupportEmail="", SupportUrl="", ARN=""):
        self.Id = Id
        self.Name = Name
        self.Owner = Owner
        self.ProductType = ProductType
        self.Description = Description
        self.Distributor = Distributor
        self.SupportDescription = SupportDescription
        self.SupportEmail = SupportEmail
        self.SupportUrl = SupportUrl
        self.ARN = ARN
        self.CreatedTime = time.time()


class ProvisioningArtifactRecord:
    def __init__(self, Id, ProductId, Name, Description=""):
        self.Id = Id
        self.ProductId = ProductId
        self.Name = Name
        self.Description = Description
        self.CreatedTime = time.time()


class ConstraintRecord:
    def __init__(self, ConstraintId, PortfolioId, ProductId, Type, Parameters, Description=""):
        self.ConstraintId = ConstraintId
        self.PortfolioId = PortfolioId
        self.ProductId = ProductId
        self.Type = Type
        self.Parameters = Parameters
        self.Description = Description
        self.Owner = ""
        self.Status = "ENABLED"
        self.CreatedTime = time.time()


class ProvisionedProductRecord:
    def __init__(self, Id, ProductId, ProvisionedProductName, ProvisioningArtifactId,
                 PathId="", Status="AVAILABLE"):
        self.Id = Id
        self.ProductId = ProductId
        self.ProvisionedProductName = ProvisionedProductName
        self.ProvisioningArtifactId = ProvisioningArtifactId
        self.PathId = PathId
        self.Status = Status
        self.CreatedTime = time.time()


class TagOptionRecord:
    def __init__(self, Id, Key, Value, Active=True):
        self.Id = Id
        self.Key = Key
        self.Value = Value
        self.Active = Active


# ── Store ───────────────────────────────────────────────────────

class ServiceCatalogStore:
    """In-memory store for Service Catalog entities."""

    def __init__(self):
        self.portfolios = {}
        self.products = {}
        self.provisioning_artifacts = {}
        self.constraints = {}
        self.provisioned_products = {}
        self.tag_options = {}
        self.portfolio_products = defaultdict(list)
        self.product_portfolios = defaultdict(list)
        self._counters = defaultdict(int)

    def _next_id(self, prefix):
        self._counters[prefix] += 1
        return f"{prefix}-{self._counters[prefix]:06d}"

    # ── Portfolio CRUD ──
    def create_portfolio(self, display_name, provider_name, description=""):
        pid = self._next_id("port")
        arn = f"arn:aws:servicecatalog:us-east-1:000000000000:portfolio/{pid}"
        self.portfolios[pid] = PortfolioRecord(pid, display_name, provider_name, description, arn)
        return self._serialize_portfolio(self.portfolios[pid])

    def get_portfolio(self, portfolio_id):
        if portfolio_id not in self.portfolios:
            raise ResourceNotFoundException("Portfolio", portfolio_id)
        return self._serialize_portfolio(self.portfolios[portfolio_id])

    def list_portfolios(self):
        return [self._serialize_portfolio(r) for r in self.portfolios.values()]

    def update_portfolio(self, portfolio_id, display_name="", provider_name="", description=""):
        rec = self.portfolios.get(portfolio_id)
        if not rec:
            raise ResourceNotFoundException("Portfolio", portfolio_id)
        if display_name:
            rec.DisplayName = display_name
        if provider_name:
            rec.ProviderName = provider_name
        if description is not None:
            rec.Description = description
        return self._serialize_portfolio(rec)

    def delete_portfolio(self, portfolio_id):
        if portfolio_id not in self.portfolios:
            raise ResourceNotFoundException("Portfolio", portfolio_id)
        del self.portfolios[portfolio_id]

    # ── Product CRUD ──
    def create_product(self, name, owner, product_type, description="", distributor="",
                       support_description="", support_email="", support_url=""):
        pid = self._next_id("prod")
        arn = f"arn:aws:servicecatalog:us-east-1:000000000000:product/{pid}"
        self.products[pid] = ProductRecord(pid, name, owner, product_type, description,
                                           distributor, support_description, support_email, support_url, arn)
        return self._serialize_product(self.products[pid])

    def get_product(self, product_id):
        if product_id not in self.products:
            raise ResourceNotFoundException("Product", product_id)
        return self._serialize_product(self.products[product_id])

    def search_products(self):
        return [self._serialize_product(r) for r in self.products.values()]

    def update_product(self, product_id, name="", owner="", description=""):
        rec = self.products.get(product_id)
        if not rec:
            raise ResourceNotFoundException("Product", product_id)
        if name:
            rec.Name = name
        if owner:
            rec.Owner = owner
        if description is not None:
            rec.Description = description
        return self._serialize_product(rec)

    def delete_product(self, product_id):
        if product_id not in self.products:
            raise ResourceNotFoundException("Product", product_id)
        del self.products[product_id]

    # ── Provisioning Artifact ──
    def create_provisioning_artifact(self, product_id, name, description=""):
        if product_id not in self.products:
            raise ResourceNotFoundException("Product", product_id)
        paid = self._next_id("pa")
        self.provisioning_artifacts[paid] = ProvisioningArtifactRecord(paid, product_id, name, description)
        return self._serialize_pa(self.provisioning_artifacts[paid])

    def get_provisioning_artifact(self, product_id, provisioning_artifact_id):
        if product_id not in self.products:
            raise ResourceNotFoundException("Product", product_id)
        rec = self.provisioning_artifacts.get(provisioning_artifact_id)
        if not rec:
            raise ResourceNotFoundException("ProvisioningArtifact", provisioning_artifact_id)
        return self._serialize_pa(rec)

    def list_provisioning_artifacts(self, product_id):
        if product_id not in self.products:
            raise ResourceNotFoundException("Product", product_id)
        return [self._serialize_pa(r) for r in self.provisioning_artifacts.values()
                if r.ProductId == product_id]

    def delete_provisioning_artifact(self, product_id, provisioning_artifact_id):
        if product_id not in self.products:
            raise ResourceNotFoundException("Product", product_id)
        if provisioning_artifact_id not in self.provisioning_artifacts:
            raise ResourceNotFoundException("ProvisioningArtifact", provisioning_artifact_id)
        del self.provisioning_artifacts[provisioning_artifact_id]

    # ── Constraint ──
    def create_constraint(self, portfolio_id, product_id, type, parameters, description=""):
        cid = self._next_id("const")
        self.constraints[cid] = ConstraintRecord(cid, portfolio_id, product_id, type, parameters, description)
        return self._serialize_constraint(self.constraints[cid])

    def get_constraint(self, constraint_id):
        rec = self.constraints.get(constraint_id)
        if not rec:
            raise ResourceNotFoundException("Constraint", constraint_id)
        return self._serialize_constraint(rec)

    def delete_constraint(self, constraint_id):
        if constraint_id not in self.constraints:
            raise ResourceNotFoundException("Constraint", constraint_id)
        del self.constraints[constraint_id]

    # ── Portfolio-Product Association ──
    def associate_product_with_portfolio(self, portfolio_id, product_id):
        if portfolio_id not in self.portfolios:
            raise ResourceNotFoundException("Portfolio", portfolio_id)
        if product_id not in self.products:
            raise ResourceNotFoundException("Product", product_id)
        self.portfolio_products[portfolio_id].append(product_id)
        self.product_portfolios[product_id].append(portfolio_id)

    def disassociate_product_from_portfolio(self, portfolio_id, product_id):
        if portfolio_id not in self.portfolios:
            raise ResourceNotFoundException("Portfolio", portfolio_id)
        if product_id not in self.products:
            raise ResourceNotFoundException("Product", product_id)
        if product_id in self.portfolio_products[portfolio_id]:
            self.portfolio_products[portfolio_id].remove(product_id)
        if portfolio_id in self.product_portfolios[product_id]:
            self.product_portfolios[product_id].remove(portfolio_id)

    # ── Provisioned Product ──
    def provision_product(self, product_id, provisioned_product_name, provisioning_artifact_id,
                          path_id=""):
        if product_id not in self.products:
            raise ResourceNotFoundException("Product", product_id)
        ppid = self._next_id("pp")
        self.provisioned_products[ppid] = ProvisionedProductRecord(
            ppid, product_id, provisioned_product_name, provisioning_artifact_id, path_id)
        return self._serialize_pp(self.provisioned_products[ppid])

    def get_provisioned_product(self, provisioned_product_id):
        rec = self.provisioned_products.get(provisioned_product_id)
        if not rec:
            raise ResourceNotFoundException("ProvisionedProduct", provisioned_product_id)
        return self._serialize_pp(rec)

    def terminate_provisioned_product(self, provisioned_product_id):
        if provisioned_product_id not in self.provisioned_products:
            raise ResourceNotFoundException("ProvisionedProduct", provisioned_product_id)
        del self.provisioned_products[provisioned_product_id]

    def update_provisioned_product(self, provisioned_product_id, product_id="",
                                   provisioning_artifact_id="", path_id=""):
        rec = self.provisioned_products.get(provisioned_product_id)
        if not rec:
            raise ResourceNotFoundException("ProvisionedProduct", provisioned_product_id)
        if product_id:
            rec.ProductId = product_id
        if provisioning_artifact_id:
            rec.ProvisioningArtifactId = provisioning_artifact_id
        if path_id:
            rec.PathId = path_id
        return self._serialize_pp(rec)

    # ── Tag Option ──
    def create_tag_option(self, key, value):
        tid = self._next_id("tag")
        self.tag_options[tid] = TagOptionRecord(tid, key, value)
        return self._serialize_tag_option(self.tag_options[tid])

    def list_tag_options(self):
        return [self._serialize_tag_option(r) for r in self.tag_options.values()]

    # ── Serializers ──
    def _serialize_portfolio(self, rec):
        return {"Id": rec.Id, "DisplayName": rec.DisplayName,
                "ProviderName": rec.ProviderName, "Description": rec.Description,
                "ARN": rec.ARN, "CreatedTime": rec.CreatedTime}

    def _serialize_product(self, rec):
        return {"Id": rec.Id, "Name": rec.Name, "Owner": rec.Owner,
                "ProductType": rec.ProductType, "Description": rec.Description,
                "Distributor": rec.Distributor, "SupportDescription": rec.SupportDescription,
                "SupportEmail": rec.SupportEmail, "SupportUrl": rec.SupportUrl,
                "HasDefaultPath": False, "ShortDescription": (rec.Description or "")[:100]}

    def _serialize_pa(self, rec):
        return {"Id": rec.Id, "ProductId": rec.ProductId, "Name": rec.Name,
                "Description": rec.Description, "CreatedTime": rec.CreatedTime}

    def _serialize_constraint(self, rec):
        return {"ConstraintId": rec.ConstraintId, "Type": rec.Type,
                "Parameters": rec.Parameters, "Description": rec.Description,
                "PortfolioId": rec.PortfolioId, "ProductId": rec.ProductId, "Status": rec.Status}

    def _serialize_pp(self, rec):
        return {"Id": rec.Id, "Name": rec.ProvisionedProductName, "ProductId": rec.ProductId,
                "ProvisioningArtifactId": rec.ProvisioningArtifactId, "PathId": rec.PathId,
                "Type": "CFN_STACK", "Status": rec.Status, "CreatedTime": rec.CreatedTime}

    def _serialize_tag_option(self, rec):
        return {"Id": rec.Id, "Key": rec.Key, "Value": rec.Value, "Active": rec.Active}


# Alias for handler injection
PortfolioDetail = dict
ProductViewDetail = dict
ConstraintDetail = dict
ProvisioningArtifactDetail = dict
ProvisionedProductDetail = dict
TagOptionDetail = dict
