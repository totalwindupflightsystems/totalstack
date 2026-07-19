"""Identity Store — users, groups, memberships."""
import uuid


class ResourceNotFoundException(Exception):
    def __init__(self, m="Resource not found"): super().__init__(m)

class ValidationException(Exception):
    def __init__(self, m="Validation error"): super().__init__(m)

class ConflictException(Exception):
    def __init__(self, m="Conflict"): super().__init__(m)

class ThrottlingException(Exception):
    def __init__(self, m="Throttled"): super().__init__(m)

class AccessDeniedException(Exception):
    def __init__(self, m="Access denied"): super().__init__(m)


class UserRecord:
    def __init__(self, identityStoreId, userId=None, userName=None, displayName=None,
                 emails=None, name=None, **kwargs):
        self.userId = userId or str(uuid.uuid4())
        self.identityStoreId = identityStoreId
        self.userName = userName or kwargs.get("UserName", "")
        self.displayName = displayName or kwargs.get("DisplayName", "")
        self.emails = emails or kwargs.get("Emails", [])
        self.name = name or kwargs.get("Name", {})
    def to_dict(self):
        return {"UserId": self.userId, "IdentityStoreId": self.identityStoreId,
                "UserName": self.userName, "DisplayName": self.displayName}


class GroupRecord:
    def __init__(self, identityStoreId, groupId=None, displayName=None, description=None, **kwargs):
        self.groupId = groupId or str(uuid.uuid4())
        self.identityStoreId = identityStoreId
        self.displayName = displayName or kwargs.get("DisplayName", "")
        self.description = description or kwargs.get("Description", "")
    def to_dict(self):
        return {"GroupId": self.groupId, "IdentityStoreId": self.identityStoreId,
                "DisplayName": self.displayName, "Description": self.description}


class GroupMembershipRecord:
    def __init__(self, identityStoreId, groupId, memberId, membershipId=None):
        self.membershipId = membershipId or str(uuid.uuid4())
        self.identityStoreId = identityStoreId
        self.groupId = groupId
        self.memberId = memberId
    def to_dict(self):
        return {"MembershipId": self.membershipId, "IdentityStoreId": self.identityStoreId,
                "GroupId": self.groupId, "MemberId": {"MemberId": self.memberId}}


class IdentityStoreStore:
    def __init__(self):
        self._users: dict[str, UserRecord] = {}
        self._groups: dict[str, GroupRecord] = {}
        self._memberships: dict[str, GroupMembershipRecord] = {}
        self._user_name_index: dict[str, UserRecord] = {}
        self._group_name_index: dict[str, GroupRecord] = {}

    def users(self, uid=None):
        if uid: return self._users.get(uid)
        return list(self._users.values())
    def groups(self, gid=None):
        if gid: return self._groups.get(gid)
        return list(self._groups.values())
    def memberships(self, mid=None):
        if mid: return self._memberships.get(mid)
        return list(self._memberships.values())

    def create_user(self, identityStoreId, userName=None, displayName=None, emails=None, name=None, **kwargs):
        rec = UserRecord(identityStoreId, userName=userName, displayName=displayName, emails=emails, name=name,
                         UserName=kwargs.get("UserName"), DisplayName=kwargs.get("DisplayName"),
                         Emails=kwargs.get("Emails"), Name=kwargs.get("Name"))
        self._users[rec.userId] = rec
        if rec.userName:
            self._user_name_index[rec.userName] = rec
        return rec.to_dict()

    def describe_user(self, identityStoreId, userId, **kwargs):
        rec = self._users.get(userId)
        if not rec: raise ResourceNotFoundException(f"User {userId}")
        return rec.to_dict()

    def update_user(self, identityStoreId, userId, operations, **kwargs):
        rec = self._users.get(userId)
        if not rec: raise ResourceNotFoundException(f"User {userId}")
        return rec.to_dict()

    def delete_user(self, identityStoreId, userId, **kwargs):
        if userId not in self._users: raise ResourceNotFoundException(f"User {userId}")
        del self._users[userId]
        return {}

    def list_users(self, identityStoreId, maxResults=None, nextToken=None, **kwargs):
        return {"Users": [u.to_dict() for u in self._users.values() if u.identityStoreId == identityStoreId]}

    def get_user_id(self, identityStoreId, alternateIdentifier, **kwargs):
        uname = alternateIdentifier.get("UniqueAttribute", {}).get("AttributeValue", "")
        rec = self._user_name_index.get(uname)
        if not rec: raise ResourceNotFoundException("User not found")
        return {"UserId": rec.userId, "IdentityStoreId": rec.identityStoreId}

    def create_group(self, identityStoreId, displayName=None, description=None, **kwargs):
        rec = GroupRecord(identityStoreId, displayName=displayName, description=description,
                          DisplayName=kwargs.get("DisplayName"), Description=kwargs.get("Description"))
        self._groups[rec.groupId] = rec
        if rec.displayName:
            self._group_name_index[rec.displayName] = rec
        return rec.to_dict()

    def describe_group(self, identityStoreId, groupId, **kwargs):
        rec = self._groups.get(groupId)
        if not rec: raise ResourceNotFoundException(f"Group {groupId}")
        return rec.to_dict()

    def update_group(self, identityStoreId, groupId, operations, **kwargs):
        rec = self._groups.get(groupId)
        if not rec: raise ResourceNotFoundException(f"Group {groupId}")
        return rec.to_dict()

    def delete_group(self, identityStoreId, groupId, **kwargs):
        if groupId not in self._groups: raise ResourceNotFoundException(f"Group {groupId}")
        del self._groups[groupId]
        return {}

    def list_groups(self, identityStoreId, maxResults=None, nextToken=None, **kwargs):
        return {"Groups": [g.to_dict() for g in self._groups.values() if g.identityStoreId == identityStoreId]}

    def get_group_id(self, identityStoreId, alternateIdentifier, **kwargs):
        gname = alternateIdentifier.get("UniqueAttribute", {}).get("AttributeValue", "")
        rec = self._group_name_index.get(gname)
        if not rec: raise ResourceNotFoundException("Group not found")
        return {"GroupId": rec.groupId, "IdentityStoreId": rec.identityStoreId}

    def create_group_membership(self, identityStoreId, groupId, memberId, **kwargs):
        rec = GroupMembershipRecord(identityStoreId, groupId, memberId)
        self._memberships[rec.membershipId] = rec
        return rec.to_dict()

    def describe_group_membership(self, identityStoreId, membershipId, **kwargs):
        rec = self._memberships.get(membershipId)
        if not rec: raise ResourceNotFoundException(f"Membership {membershipId}")
        return rec.to_dict()

    def delete_group_membership(self, identityStoreId, membershipId, **kwargs):
        if membershipId not in self._memberships: raise ResourceNotFoundException(f"Membership {membershipId}")
        del self._memberships[membershipId]
        return {}

    def list_group_memberships(self, identityStoreId, groupId, maxResults=None, nextToken=None, **kwargs):
        result = [m.to_dict() for m in self._memberships.values()
                  if m.identityStoreId == identityStoreId and m.groupId == groupId]
        return {"GroupMemberships": result}

    def list_group_memberships_for_member(self, identityStoreId, memberId, maxResults=None, nextToken=None, **kwargs):
        result = [m.to_dict() for m in self._memberships.values()
                  if m.identityStoreId == identityStoreId and m.memberId == memberId]
        return {"GroupMemberships": result}

    def get_group_membership_id(self, identityStoreId, groupId, memberId, **kwargs):
        for m in self._memberships.values():
            if m.identityStoreId == identityStoreId and m.groupId == groupId and m.memberId == memberId:
                return {"MembershipId": m.membershipId, "IdentityStoreId": identityStoreId}
        raise ResourceNotFoundException("Membership not found")

    def is_member_in_groups(self, identityStoreId, memberId, groupIds, **kwargs):
        member_groups = set()
        for m in self._memberships.values():
            if m.identityStoreId == identityStoreId and m.memberId == memberId and m.groupId in groupIds:
                member_groups.add(m.groupId)
        results = [{"GroupId": gid, "MembershipExists": gid in member_groups} for gid in groupIds]
        return {"Results": results}
