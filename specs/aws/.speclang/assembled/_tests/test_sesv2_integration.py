"""Integration test for SESv2 — real SESV2Store."""
import pytest
import os
import importlib.util
import types

ASSEMBLED_DIR = os.path.dirname(__file__)
SERVICE_DIR = os.path.join(ASSEMBLED_DIR, '..', 'sesv2')

# Load models module dynamically
models_spec = importlib.util.spec_from_file_location(
    'models', os.path.join(SERVICE_DIR, 'models.code.py'))
models_mod = importlib.util.module_from_spec(models_spec)
models_spec.loader.exec_module(models_mod)

SESV2Store = models_mod.SESV2Store
ContactListRecord = models_mod.ContactListRecord
ContactRecord = models_mod.ContactRecord
EmailIdentityRecord = models_mod.EmailIdentityRecord
EmailTemplateRecord = models_mod.EmailTemplateRecord
ConfigurationSetRecord = models_mod.ConfigurationSetRecord
AlreadyExistsException = models_mod.AlreadyExistsException
NotFoundException = models_mod.NotFoundException
InvalidParameterException = models_mod.InvalidParameterException
ResourceNotFoundException = models_mod.ResourceNotFoundException
BadRequestException = models_mod.BadRequestException
InternalServerException = models_mod.InternalServerException


def _load_handler(op_name):
    """Load a single-handler .code.py file."""
    path = os.path.join(SERVICE_DIR, op_name + '.code.py')
    spec = importlib.util.spec_from_file_location(op_name, path)
    mod = importlib.util.module_from_spec(spec)
    # Inject exceptions
    mod.AlreadyExistsException = AlreadyExistsException
    mod.NotFoundException = NotFoundException
    mod.InvalidParameterException = InvalidParameterException
    mod.ResourceNotFoundException = ResourceNotFoundException
    mod.BadRequestException = BadRequestException
    mod.InternalServerException = InternalServerException
    # Inject records
    mod.ContactListRecord = ContactListRecord
    mod.ContactRecord = ContactRecord
    mod.EmailIdentityRecord = EmailIdentityRecord
    mod.EmailTemplateRecord = EmailTemplateRecord
    mod.ConfigurationSetRecord = ConfigurationSetRecord
    # Inject stdlib
    import time as _time
    import uuid as _uuid
    mod.time = _time
    mod.uuid = _uuid
    mod.dataclass = lambda f: f
    spec.loader.exec_module(mod)
    skip_names = {'dataclass', 'time', 'uuid', '<lambda>'}
    for v in mod.__dict__.values():
        if (isinstance(v, types.FunctionType)
                and not v.__name__.startswith('_')
                and v.__name__ not in skip_names):
            return v
    raise RuntimeError(f"No handler found in {op_name}")


class TestContactListIntegration:

    @pytest.fixture
    def store(self):
        return SESV2Store()

    def test_create_contact_list_happy(self, store):
        handler = _load_handler('CreateContactList')
        response = handler(store, {'ContactListName': 'my-list', 'Description': 'Test'})
        assert response['ContactListName'] == 'my-list'

    def test_create_contact_list_duplicate(self, store):
        handler = _load_handler('CreateContactList')
        handler(store, {'ContactListName': 'my-list'})
        with pytest.raises(AlreadyExistsException):
            handler(store, {'ContactListName': 'my-list'})

    def test_get_contact_list_happy(self, store):
        _load_handler('CreateContactList')(store, {'ContactListName': 'my-list'})
        handler = _load_handler('GetContactList')
        response = handler(store, {'ContactListName': 'my-list'})
        assert response['ContactListName'] == 'my-list'

    def test_get_contact_list_nonexistent(self, store):
        handler = _load_handler('GetContactList')
        with pytest.raises(NotFoundException):
            handler(store, {'ContactListName': 'nonex'})

    def test_list_contact_lists(self, store):
        h = _load_handler('CreateContactList')
        h(store, {'ContactListName': 'l1'})
        h(store, {'ContactListName': 'l2'})
        handler = _load_handler('ListContactLists')
        response = handler(store, {})
        assert len(response['ContactLists']) == 2

    def test_delete_contact_list_happy(self, store):
        _load_handler('CreateContactList')(store, {'ContactListName': 'my-list'})
        handler = _load_handler('DeleteContactList')
        response = handler(store, {'ContactListName': 'my-list'})
        assert response == {}
        assert store.contact_lists('my-list') is None

    def test_delete_contact_list_nonexistent(self, store):
        handler = _load_handler('DeleteContactList')
        with pytest.raises(NotFoundException):
            handler(store, {'ContactListName': 'nonex'})


class TestContactIntegration:

    @pytest.fixture
    def store_with_list(self):
        store = SESV2Store()
        # Create a contact list
        cp = os.path.join(SERVICE_DIR, 'CreateContactList.code.py')
        spec = importlib.util.spec_from_file_location('CreateContactList', cp)
        mod = importlib.util.module_from_spec(spec)
        mod.AlreadyExistsException = AlreadyExistsException
        import time as _time
        import uuid as _uuid
        mod.time = _time
        mod.uuid = _uuid
        mod.dataclass = lambda f: f
        mod.ContactListRecord = ContactListRecord
        spec.loader.exec_module(mod)
        skip_names = {'dataclass', 'time', 'uuid', '<lambda>'}
        for v in mod.__dict__.values():
            if (isinstance(v, types.FunctionType) and not v.__name__.startswith('_')
                    and v.__name__ not in skip_names):
                v(store, {'ContactListName': 'my-list'})
                break
        return store

    def test_create_contact_happy(self, store_with_list):
        store = store_with_list
        handler = _load_handler('CreateContact')
        response = handler(store, {
            'ContactListName': 'my-list',
            'EmailAddress': 'test@example.com',
        })
        assert response['EmailAddress'] == 'test@example.com'

    def test_create_contact_duplicate(self, store_with_list):
        store = store_with_list
        handler = _load_handler('CreateContact')
        handler(store, {'ContactListName': 'my-list', 'EmailAddress': 'test@example.com'})
        with pytest.raises(AlreadyExistsException):
            handler(store, {'ContactListName': 'my-list', 'EmailAddress': 'test@example.com'})

    def test_create_contact_nonexistent_list(self, store_with_list):
        store = store_with_list
        handler = _load_handler('CreateContact')
        with pytest.raises(NotFoundException):
            handler(store, {'ContactListName': 'no-list', 'EmailAddress': 'test@example.com'})

    def test_get_contact_happy(self, store_with_list):
        store = store_with_list
        _load_handler('CreateContact')(store, {'ContactListName': 'my-list', 'EmailAddress': 'test@example.com'})
        handler = _load_handler('GetContact')
        response = handler(store, {'ContactListName': 'my-list', 'EmailAddress': 'test@example.com'})
        assert response['EmailAddress'] == 'test@example.com'

    def test_get_contact_nonexistent(self, store_with_list):
        store = store_with_list
        handler = _load_handler('GetContact')
        with pytest.raises(NotFoundException):
            handler(store, {'ContactListName': 'my-list', 'EmailAddress': 'no@example.com'})

    def test_list_contacts(self, store_with_list):
        store = store_with_list
        h = _load_handler('CreateContact')
        h(store, {'ContactListName': 'my-list', 'EmailAddress': 'a@ex.com'})
        h(store, {'ContactListName': 'my-list', 'EmailAddress': 'b@ex.com'})
        handler = _load_handler('ListContacts')
        response = handler(store, {'ContactListName': 'my-list'})
        assert len(response['Contacts']) == 2

    def test_update_contact_happy(self, store_with_list):
        store = store_with_list
        _load_handler('CreateContact')(store, {'ContactListName': 'my-list', 'EmailAddress': 'test@example.com'})
        handler = _load_handler('UpdateContact')
        response = handler(store, {
            'ContactListName': 'my-list',
            'EmailAddress': 'test@example.com',
            'UnsubscribeAll': True,
        })
        assert response['UnsubscribeAll'] is True

    def test_delete_contact_happy(self, store_with_list):
        store = store_with_list
        _load_handler('CreateContact')(store, {'ContactListName': 'my-list', 'EmailAddress': 'test@example.com'})
        handler = _load_handler('DeleteContact')
        response = handler(store, {'ContactListName': 'my-list', 'EmailAddress': 'test@example.com'})
        assert response == {}


class TestEmailIdentityIntegration:

    @pytest.fixture
    def store(self):
        return SESV2Store()

    def test_create_email_identity_happy(self, store):
        handler = _load_handler('CreateEmailIdentity')
        response = handler(store, {'EmailIdentity': 'sender@example.com'})
        assert response['EmailIdentity'] == 'sender@example.com'

    def test_create_email_identity_duplicate(self, store):
        handler = _load_handler('CreateEmailIdentity')
        handler(store, {'EmailIdentity': 'sender@example.com'})
        with pytest.raises(AlreadyExistsException):
            handler(store, {'EmailIdentity': 'sender@example.com'})

    def test_get_email_identity_nonexistent(self, store):
        handler = _load_handler('GetEmailIdentity')
        with pytest.raises(NotFoundException):
            handler(store, {'EmailIdentity': 'no@example.com'})

    def test_list_email_identities(self, store):
        h = _load_handler('CreateEmailIdentity')
        h(store, {'EmailIdentity': 'a@ex.com'})
        h(store, {'EmailIdentity': 'b@ex.com'})
        handler = _load_handler('ListEmailIdentities')
        response = handler(store, {})
        assert len(response['EmailIdentities']) == 2

    def test_delete_email_identity_happy(self, store):
        _load_handler('CreateEmailIdentity')(store, {'EmailIdentity': 'sender@example.com'})
        handler = _load_handler('DeleteEmailIdentity')
        response = handler(store, {'EmailIdentity': 'sender@example.com'})
        assert response == {}


class TestEmailTemplateIntegration:

    @pytest.fixture
    def store(self):
        return SESV2Store()

    def test_create_template_happy(self, store):
        handler = _load_handler('CreateEmailTemplate')
        response = handler(store, {
            'TemplateName': 'welcome',
            'TemplateContent': {'Subject': 'Welcome!', 'Text': 'Hello', 'Html': '<p>Hello</p>'},
        })
        assert response['TemplateName'] == 'welcome'

    def test_get_template_happy(self, store):
        _load_handler('CreateEmailTemplate')(store, {
            'TemplateName': 'welcome',
            'TemplateContent': {'Subject': 'Welcome!', 'Text': 'Hello', 'Html': '<p>Hello</p>'},
        })
        handler = _load_handler('GetEmailTemplate')
        response = handler(store, {'TemplateName': 'welcome'})
        assert response['TemplateName'] == 'welcome'

    def test_get_template_nonexistent(self, store):
        handler = _load_handler('GetEmailTemplate')
        with pytest.raises(NotFoundException):
            handler(store, {'TemplateName': 'nonex'})

    def test_update_template_happy(self, store):
        _load_handler('CreateEmailTemplate')(store, {
            'TemplateName': 'welcome',
            'TemplateContent': {'Subject': 'Welcome!', 'Text': 'Hello'},
        })
        handler = _load_handler('UpdateEmailTemplate')
        response = handler(store, {
            'TemplateName': 'welcome',
            'TemplateContent': {'Subject': 'Updated Subject'},
        })
        assert response['TemplateContent']['Subject'] == 'Updated Subject'

    def test_delete_template_happy(self, store):
        _load_handler('CreateEmailTemplate')(store, {
            'TemplateName': 'welcome',
            'TemplateContent': {'Subject': 'Welcome!', 'Text': 'Hello'},
        })
        handler = _load_handler('DeleteEmailTemplate')
        response = handler(store, {'TemplateName': 'welcome'})
        assert response == {}


class TestConfigurationSetIntegration:

    @pytest.fixture
    def store(self):
        return SESV2Store()

    def test_create_config_set_happy(self, store):
        handler = _load_handler('CreateConfigurationSet')
        response = handler(store, {'ConfigurationSetName': 'my-config'})
        assert response['ConfigurationSetName'] == 'my-config'

    def test_create_config_set_duplicate(self, store):
        handler = _load_handler('CreateConfigurationSet')
        handler(store, {'ConfigurationSetName': 'my-config'})
        with pytest.raises(AlreadyExistsException):
            handler(store, {'ConfigurationSetName': 'my-config'})

    def test_get_config_set_happy(self, store):
        _load_handler('CreateConfigurationSet')(store, {'ConfigurationSetName': 'my-config'})
        handler = _load_handler('GetConfigurationSet')
        response = handler(store, {'ConfigurationSetName': 'my-config'})
        assert response['ConfigurationSetName'] == 'my-config'

    def test_get_config_set_nonexistent(self, store):
        handler = _load_handler('GetConfigurationSet')
        with pytest.raises(NotFoundException):
            handler(store, {'ConfigurationSetName': 'nonex'})

    def test_list_config_sets(self, store):
        h = _load_handler('CreateConfigurationSet')
        h(store, {'ConfigurationSetName': 'cs1'})
        h(store, {'ConfigurationSetName': 'cs2'})
        handler = _load_handler('ListConfigurationSets')
        response = handler(store, {})
        assert len(response['ConfigurationSets']) == 2

    def test_delete_config_set_happy(self, store):
        _load_handler('CreateConfigurationSet')(store, {'ConfigurationSetName': 'my-config'})
        handler = _load_handler('DeleteConfigurationSet')
        response = handler(store, {'ConfigurationSetName': 'my-config'})
        assert response == {}


class TestSendEmailIntegration:

    @pytest.fixture
    def store(self):
        return SESV2Store()

    def test_send_email_happy(self, store):
        handler = _load_handler('SendEmail')
        response = handler(store, {
            'FromEmailAddress': 'sender@example.com',
            'Destination': {'ToAddresses': ['recipient@example.com']},
            'Content': {
                'Simple': {
                    'Subject': {'Data': 'Test'},
                    'Body': {'Text': {'Data': 'Hello'}},
                }
            },
        })
        assert 'MessageId' in response
