"""SESv2 store — Simple Email Service v2 for sending and managing email.

Entities:
- ContactList: A list of contacts (subscribers)
- Contact: An individual contact within a contact list
- EmailIdentity: A verified email address or domain
- EmailTemplate: A reusable email template
- ConfigurationSet: A set of rules for sending email
"""

import uuid
import time


# =============================================================================
# Exception Classes
# =============================================================================

class InvalidParameterException(Exception):
    pass


class ResourceNotFoundException(Exception):
    pass


class AlreadyExistsException(Exception):
    pass


class NotFoundException(ResourceNotFoundException):
    pass


class ConflictException(Exception):
    pass


class LimitExceededException(Exception):
    pass


class TooManyRequestsException(Exception):
    pass


class InternalServerException(Exception):
    pass


class BadRequestException(Exception):
    pass


# =============================================================================
# Record Classes
# =============================================================================

class ContactListRecord:
    def __init__(self, ContactListName, **kwargs):
        self.ContactListName = ContactListName
        self.Description = kwargs.get('Description', '')
        self.Topics = kwargs.get('Topics', [])
        self.CreatedTimestamp = kwargs.get('CreatedTimestamp', time.time())
        self.LastUpdatedTimestamp = kwargs.get('LastUpdatedTimestamp', time.time())

    def to_dict(self):
        return self.__dict__


class ContactRecord:
    def __init__(self, ContactListName, EmailAddress, **kwargs):
        self.ContactListName = ContactListName
        self.EmailAddress = EmailAddress
        self.TopicPreferences = kwargs.get('TopicPreferences', [])
        self.UnsubscribeAll = kwargs.get('UnsubscribeAll', False)
        self.AttributesData = kwargs.get('AttributesData', '')
        self.CreatedTimestamp = kwargs.get('CreatedTimestamp', time.time())
        self.LastUpdatedTimestamp = kwargs.get('LastUpdatedTimestamp', time.time())

    def to_dict(self):
        return self.__dict__


class EmailIdentityRecord:
    def __init__(self, EmailIdentity, **kwargs):
        self.EmailIdentity = EmailIdentity
        self.IdentityType = kwargs.get('IdentityType', 'EMAIL_ADDRESS')
        self.VerifiedForSendingStatus = kwargs.get('VerifiedForSendingStatus', False)
        self.DkimAttributes = kwargs.get('DkimAttributes', {})
        self.MailFromAttributes = kwargs.get('MailFromAttributes', {})
        self.Policies = kwargs.get('Policies', {})
        self.ConfigurationSetName = kwargs.get('ConfigurationSetName', None)
        self.Tags = kwargs.get('Tags', [])

    def to_dict(self):
        return self.__dict__


class EmailTemplateRecord:
    def __init__(self, TemplateName, **kwargs):
        self.TemplateName = TemplateName
        self.SubjectPart = kwargs.get('SubjectPart', '')
        self.TextPart = kwargs.get('TextPart', '')
        self.HtmlPart = kwargs.get('HtmlPart', '')
        self.CreatedTimestamp = kwargs.get('CreatedTimestamp', time.time())

    def to_dict(self):
        return self.__dict__


class ConfigurationSetRecord:
    def __init__(self, ConfigurationSetName, **kwargs):
        self.ConfigurationSetName = ConfigurationSetName
        self.SendingOptions = kwargs.get('SendingOptions', {})
        self.TrackingOptions = kwargs.get('TrackingOptions', {})
        self.DeliveryOptions = kwargs.get('DeliveryOptions', {})
        self.ReputationOptions = kwargs.get('ReputationOptions', {})
        self.VdmOptions = kwargs.get('VdmOptions', {})

    def to_dict(self):
        return self.__dict__


# =============================================================================
# SESv2 Store
# =============================================================================

class SESV2Store:
    def __init__(self):
        self._contact_lists: dict[str, ContactListRecord] = {}
        self._contacts: dict[str, dict[str, ContactRecord]] = {}  # list_name → {email → record}
        self._email_identities: dict[str, EmailIdentityRecord] = {}
        self._email_templates: dict[str, EmailTemplateRecord] = {}
        self._configuration_sets: dict[str, ConfigurationSetRecord] = {}

    # ---- Accessors ----

    def contact_lists(self, name=None):
        if name is not None:
            return self._contact_lists.get(name)
        return list(self._contact_lists.values())

    def contacts(self, list_name=None, email=None):
        if list_name and email:
            return self._contacts.get(list_name, {}).get(email)
        if list_name:
            return list(self._contacts.get(list_name, {}).values())
        return []

    def email_identities(self, email=None):
        if email is not None:
            return self._email_identities.get(email)
        return list(self._email_identities.values())

    def email_templates(self, name=None):
        if name is not None:
            return self._email_templates.get(name)
        return list(self._email_templates.values())

    def configuration_sets(self, name=None):
        if name is not None:
            return self._configuration_sets.get(name)
        return list(self._configuration_sets.values())

    # ===== ContactList CRUD =====

    def create_contact_list(self, ContactListName, **kwargs):
        if ContactListName in self._contact_lists:
            raise AlreadyExistsException(f"Contact list {ContactListName} already exists")
        record = ContactListRecord(ContactListName, **kwargs)
        self._contact_lists[ContactListName] = record
        return record.to_dict()

    def get_contact_list(self, ContactListName):
        record = self._contact_lists.get(ContactListName)
        if not record:
            raise NotFoundException(f"Contact list {ContactListName} not found")
        return record.to_dict()

    def list_contact_lists(self, **kwargs):
        return {'ContactLists': [r.to_dict() for r in self._contact_lists.values()]}

    def delete_contact_list(self, ContactListName):
        if ContactListName not in self._contact_lists:
            raise NotFoundException(f"Contact list {ContactListName} not found")
        del self._contact_lists[ContactListName]
        if ContactListName in self._contacts:
            del self._contacts[ContactListName]
        return {}

    # ===== Contact CRUD =====

    def create_contact(self, ContactListName, EmailAddress, **kwargs):
        if ContactListName not in self._contact_lists:
            raise NotFoundException(f"Contact list {ContactListName} not found")
        if ContactListName not in self._contacts:
            self._contacts[ContactListName] = {}
        if EmailAddress in self._contacts[ContactListName]:
            raise AlreadyExistsException(f"Contact {EmailAddress} already exists")
        record = ContactRecord(ContactListName, EmailAddress, **kwargs)
        self._contacts[ContactListName][EmailAddress] = record
        return record.to_dict()

    def get_contact(self, ContactListName, EmailAddress):
        if ContactListName not in self._contact_lists:
            raise NotFoundException(f"Contact list {ContactListName} not found")
        contact = self._contacts.get(ContactListName, {}).get(EmailAddress)
        if not contact:
            raise NotFoundException(f"Contact {EmailAddress} not found")
        return contact.to_dict()

    def list_contacts(self, ContactListName, **kwargs):
        if ContactListName not in self._contact_lists:
            raise NotFoundException(f"Contact list {ContactListName} not found")
        return {'Contacts': [r.to_dict() for r in self._contacts.get(ContactListName, {}).values()]}

    def update_contact(self, ContactListName, EmailAddress, **kwargs):
        if ContactListName not in self._contact_lists:
            raise NotFoundException(f"Contact list {ContactListName} not found")
        contact = self._contacts.get(ContactListName, {}).get(EmailAddress)
        if not contact:
            raise NotFoundException(f"Contact {EmailAddress} not found")
        for key, value in kwargs.items():
            if hasattr(contact, key):
                setattr(contact, key, value)
        return contact.to_dict()

    def delete_contact(self, ContactListName, EmailAddress):
        if ContactListName not in self._contact_lists:
            raise NotFoundException(f"Contact list {ContactListName} not found")
        if ContactListName not in self._contacts or EmailAddress not in self._contacts[ContactListName]:
            raise NotFoundException(f"Contact {EmailAddress} not found")
        del self._contacts[ContactListName][EmailAddress]
        return {}

    # ===== EmailIdentity CRUD =====

    def create_email_identity(self, EmailIdentity, **kwargs):
        if EmailIdentity in self._email_identities:
            raise AlreadyExistsException(f"Email identity {EmailIdentity} already exists")
        record = EmailIdentityRecord(EmailIdentity, **kwargs)
        self._email_identities[EmailIdentity] = record
        return record.to_dict()

    def get_email_identity(self, EmailIdentity):
        record = self._email_identities.get(EmailIdentity)
        if not record:
            raise NotFoundException(f"Email identity {EmailIdentity} not found")
        return record.to_dict()

    def list_email_identities(self, **kwargs):
        return {'EmailIdentities': [r.to_dict() for r in self._email_identities.values()]}

    def delete_email_identity(self, EmailIdentity):
        if EmailIdentity not in self._email_identities:
            raise NotFoundException(f"Email identity {EmailIdentity} not found")
        del self._email_identities[EmailIdentity]
        return {}

    # ===== EmailTemplate CRUD =====

    def create_email_template(self, TemplateName, TemplateContent, **kwargs):
        if TemplateName in self._email_templates:
            raise AlreadyExistsException(f"Email template {TemplateName} already exists")
        record = EmailTemplateRecord(
            TemplateName,
            SubjectPart=TemplateContent.get('Subject', ''),
            TextPart=TemplateContent.get('Text', ''),
            HtmlPart=TemplateContent.get('Html', ''),
            **kwargs,
        )
        self._email_templates[TemplateName] = record
        return record.to_dict()

    def get_email_template(self, TemplateName):
        record = self._email_templates.get(TemplateName)
        if not record:
            raise NotFoundException(f"Email template {TemplateName} not found")
        return record.to_dict()

    def list_email_templates(self, **kwargs):
        return {'TemplatesMetadata': [
            {'TemplateName': r.TemplateName, 'CreatedTimestamp': r.CreatedTimestamp}
            for r in self._email_templates.values()
        ]}

    def update_email_template(self, TemplateName, TemplateContent, **kwargs):
        record = self._email_templates.get(TemplateName)
        if not record:
            raise NotFoundException(f"Email template {TemplateName} not found")
        if 'Subject' in TemplateContent:
            record.SubjectPart = TemplateContent['Subject']
        if 'Text' in TemplateContent:
            record.TextPart = TemplateContent['Text']
        if 'Html' in TemplateContent:
            record.HtmlPart = TemplateContent['Html']
        return record.to_dict()

    def delete_email_template(self, TemplateName):
        if TemplateName not in self._email_templates:
            raise NotFoundException(f"Email template {TemplateName} not found")
        del self._email_templates[TemplateName]
        return {}

    # ===== ConfigurationSet CRUD =====

    def create_configuration_set(self, ConfigurationSetName, **kwargs):
        if ConfigurationSetName in self._configuration_sets:
            raise AlreadyExistsException(f"Configuration set {ConfigurationSetName} already exists")
        record = ConfigurationSetRecord(ConfigurationSetName, **kwargs)
        self._configuration_sets[ConfigurationSetName] = record
        return record.to_dict()

    def get_configuration_set(self, ConfigurationSetName):
        record = self._configuration_sets.get(ConfigurationSetName)
        if not record:
            raise NotFoundException(f"Configuration set {ConfigurationSetName} not found")
        return record.to_dict()

    def list_configuration_sets(self, **kwargs):
        return {'ConfigurationSets': [
            {'Name': r.ConfigurationSetName} for r in self._configuration_sets.values()
        ]}

    def delete_configuration_set(self, ConfigurationSetName):
        if ConfigurationSetName not in self._configuration_sets:
            raise NotFoundException(f"Configuration set {ConfigurationSetName} not found")
        del self._configuration_sets[ConfigurationSetName]
        return {}

    # ===== SendEmail =====

    def send_email(self, **kwargs):
        """Simulate sending an email. Returns a message ID."""
        return {
            'MessageId': f'message-{str(uuid.uuid4())[:8]}',
        }
