"""Storage Gateway store — Gateway, FileShare, Volume, Tape, Tags."""
import uuid


class InvalidRequestException(Exception):
    pass


class InternalException(Exception):
    pass


class ResourceNotFoundException(InvalidRequestException):
    pass


class ResourceInUseException(InvalidRequestException):
    pass


def _convert_tags(tags):
    if not tags:
        return {}
    if isinstance(tags, dict):
        return tags
    if isinstance(tags, list):
        return {t.get("Key", t.get("key", "")): t.get("Value", t.get("value", "")) for t in tags}
    return {}


class GatewayRecord:
    def __init__(self, ActivationKey=None, GatewayName=None, GatewayTimezone=None,
                 GatewayType=None, MediumChangerType=None, TapeDriveType=None, Tags=None):
        self.GatewayARN = f"arn:aws:storagegateway:us-east-1:000000000000:gateway/gw-{uuid.uuid4().hex[:8]}"
        self.ActivationKey = ActivationKey or ""
        self.GatewayName = GatewayName or ""
        self.GatewayTimezone = GatewayTimezone or "GMT"
        self.GatewayType = GatewayType or "FILE_S3"
        self.MediumChangerType = MediumChangerType or ""
        self.TapeDriveType = TapeDriveType or ""
        self.Tags = _convert_tags(Tags)

    def to_dict(self):
        return {
            "GatewayARN": self.GatewayARN,
            "GatewayName": self.GatewayName,
            "GatewayTimezone": self.GatewayTimezone,
            "GatewayType": self.GatewayType,
        }


class FileShareRecord:
    def __init__(self, GatewayARN=None, Role=None, LocationARN=None, ClientList=None,
                 FileShareName=None, FileShareType="NFS", Tags=None, **kwargs):
        self.FileShareARN = f"arn:aws:storagegateway:us-east-1:000000000000:share/share-{uuid.uuid4().hex[:8]}"
        self.GatewayARN = GatewayARN or ""
        self.Role = Role or ""
        self.LocationARN = LocationARN or ""
        self.ClientList = ClientList or []
        self.FileShareName = FileShareName or ""
        self.FileShareType = FileShareType
        self.Tags = _convert_tags(Tags)
        self._extra = kwargs

    def to_dict(self):
        d = {
            "FileShareARN": self.FileShareARN,
            "GatewayARN": self.GatewayARN,
            "Role": self.Role,
            "LocationARN": self.LocationARN,
            "ClientList": self.ClientList,
            "FileShareName": self.FileShareName,
            "FileShareType": self.FileShareType,
        }
        d.update(self._extra)
        return d


class VolumeRecord:
    def __init__(self, GatewayARN=None, VolumeType="CACHED", VolumeSizeInBytes=None,
                 SnapshotId=None, DiskId=None, TargetName=None, Tags=None, **kwargs):
        self.VolumeARN = f"arn:aws:storagegateway:us-east-1:000000000000:volume/vol-{uuid.uuid4().hex[:8]}"
        self.GatewayARN = GatewayARN or ""
        self.VolumeType = VolumeType
        self.VolumeSizeInBytes = VolumeSizeInBytes or 0
        self.SnapshotId = SnapshotId or ""
        self.DiskId = DiskId or ""
        self.TargetName = TargetName or ""
        self.Tags = _convert_tags(Tags)
        self._extra = kwargs

    def to_dict(self):
        d = {
            "VolumeARN": self.VolumeARN,
            "GatewayARN": self.GatewayARN,
            "VolumeType": self.VolumeType,
            "VolumeSizeInBytes": self.VolumeSizeInBytes,
            "TargetName": self.TargetName,
        }
        d.update(self._extra)
        return d


class TapeRecord:
    def __init__(self, GatewayARN=None, TapeSizeInBytes=None, TapeBarcode=None,
                 PoolId=None, Tags=None, **kwargs):
        self.TapeARN = f"arn:aws:storagegateway:us-east-1:000000000000:tape/tape-{uuid.uuid4().hex[:8]}"
        self.GatewayARN = GatewayARN or ""
        self.TapeSizeInBytes = TapeSizeInBytes or 0
        self.TapeBarcode = TapeBarcode or ""
        self.PoolId = PoolId or "DEFAULT_POOL"
        self.Tags = _convert_tags(Tags)
        self._extra = kwargs

    def to_dict(self):
        return {
            "TapeARN": self.TapeARN,
            "GatewayARN": self.GatewayARN,
            "TapeSizeInBytes": self.TapeSizeInBytes,
            "TapeBarcode": self.TapeBarcode,
            "PoolId": self.PoolId,
        }


class StorageGatewayStore:
    def __init__(self):
        self._gateways = {}
        self._fileshares = {}
        self._volumes = {}
        self._tapes = {}

    # === Gateway ===
    def activate_gateway(self, ActivationKey, GatewayName=None, GatewayTimezone=None,
                         GatewayType=None, MediumChangerType=None, TapeDriveType=None,
                         Tags=None):
        rec = GatewayRecord(ActivationKey=ActivationKey, GatewayName=GatewayName,
                            GatewayTimezone=GatewayTimezone, GatewayType=GatewayType,
                            MediumChangerType=MediumChangerType, TapeDriveType=TapeDriveType,
                            Tags=Tags)
        self._gateways[rec.GatewayARN] = rec
        return {"GatewayARN": rec.GatewayARN}

    def describe_gateway_information(self, GatewayARN):
        rec = self._gateways.get(GatewayARN)
        if not rec:
            raise ResourceNotFoundException(f"Gateway {GatewayARN} not found")
        return rec.to_dict()

    def list_gateways(self, Marker=None, Limit=None):
        arns = list(self._gateways.keys())
        return {"Gateways": [{"GatewayARN": a} for a in arns]}

    def delete_gateway(self, GatewayARN):
        if GatewayARN not in self._gateways:
            raise ResourceNotFoundException(f"Gateway {GatewayARN} not found")
        del self._gateways[GatewayARN]
        return {"GatewayARN": GatewayARN}

    # === FileShare ===
    def create_nfs_file_share(self, GatewayARN, Role, LocationARN, ClientList=None,
                              FileShareName=None, Tags=None, **kwargs):
        rec = FileShareRecord(GatewayARN=GatewayARN, Role=Role, LocationARN=LocationARN,
                              ClientList=ClientList, FileShareName=FileShareName,
                              FileShareType="NFS", Tags=Tags, **kwargs)
        self._fileshares[rec.FileShareARN] = rec
        return {"FileShareARN": rec.FileShareARN}

    def create_smb_file_share(self, GatewayARN, Role, LocationARN, ClientList=None,
                              FileShareName=None, Tags=None, **kwargs):
        rec = FileShareRecord(GatewayARN=GatewayARN, Role=Role, LocationARN=LocationARN,
                              ClientList=ClientList, FileShareName=FileShareName,
                              FileShareType="SMB", Tags=Tags, **kwargs)
        self._fileshares[rec.FileShareARN] = rec
        return {"FileShareARN": rec.FileShareARN}

    def describe_nfs_file_shares(self, FileShareARNList):
        return {"NFSFileShareInfoList": [
            self._fileshares[a].to_dict() for a in FileShareARNList if a in self._fileshares
        ]}

    def list_file_shares(self, GatewayARN=None, Marker=None, Limit=None):
        if GatewayARN:
            arns = [a for a, r in self._fileshares.items() if r.GatewayARN == GatewayARN]
        else:
            arns = list(self._fileshares.keys())
        return {"FileShareInfoList": [{"FileShareARN": a} for a in arns]}

    def delete_file_share(self, FileShareARN):
        if FileShareARN not in self._fileshares:
            raise ResourceNotFoundException(f"FileShare {FileShareARN} not found")
        del self._fileshares[FileShareARN]
        return {"FileShareARN": FileShareARN}

    # === Volume ===
    def create_cached_iscsi_volume(self, GatewayARN, VolumeSizeInBytes, TargetName,
                                   SnapshotId=None, DiskId=None, Tags=None, **kwargs):
        if TargetName in [r.TargetName for r in self._volumes.values()]:
            raise ResourceInUseException(f"TargetName {TargetName} already exists")
        rec = VolumeRecord(GatewayARN=GatewayARN, VolumeType="CACHED",
                          VolumeSizeInBytes=VolumeSizeInBytes, TargetName=TargetName,
                          SnapshotId=SnapshotId, DiskId=DiskId, Tags=Tags, **kwargs)
        self._volumes[rec.VolumeARN] = rec
        return {"VolumeARN": rec.VolumeARN, "TargetARN": f"{rec.VolumeARN}/target"}

    def describe_cached_iscsi_volumes(self, VolumeARNs):
        return {"CachediSCSIVolumes": [
            self._volumes[a].to_dict() for a in VolumeARNs if a in self._volumes
        ]}

    def list_volumes(self, GatewayARN=None, Marker=None, Limit=None):
        if GatewayARN:
            arns = [a for a, r in self._volumes.items() if r.GatewayARN == GatewayARN]
        else:
            arns = list(self._volumes.keys())
        return {"VolumeInfos": [{"VolumeARN": a} for a in arns]}

    def delete_volume(self, VolumeARN):
        if VolumeARN not in self._volumes:
            raise ResourceNotFoundException(f"Volume {VolumeARN} not found")
        del self._volumes[VolumeARN]
        return {"VolumeARN": VolumeARN}

    # === Tape ===
    def create_tapes(self, GatewayARN, TapeSizeInBytes, ClientToken, NumTapesToCreate,
                     TapeBarcodePrefix=None, PoolId=None, Tags=None):
        tapes = []
        for i in range(NumTapesToCreate):
            rec = TapeRecord(GatewayARN=GatewayARN, TapeSizeInBytes=TapeSizeInBytes,
                           TapeBarcodePrefix=TapeBarcodePrefix, PoolId=PoolId, Tags=Tags)
            self._tapes[rec.TapeARN] = rec
            tapes.append(rec.TapeARN)
        return {"TapeARNs": tapes}

    def describe_tapes(self, TapeARNs, GatewayARN=None, Marker=None, Limit=None):
        return {"Tapes": [
            self._tapes[a].to_dict() for a in TapeARNs if a in self._tapes
        ]}

    def list_tapes(self, TapeARNs=None, Marker=None, Limit=None):
        arns = list(self._tapes.keys())
        return {"TapeInfos": [{"TapeARN": a} for a in arns]}

    def delete_tape(self, GatewayARN, TapeARN):
        if TapeARN not in self._tapes:
            raise ResourceNotFoundException(f"Tape {TapeARN} not found")
        del self._tapes[TapeARN]
        return {"TapeARN": TapeARN}

    # === Tags ===
    def add_tags_to_resource(self, ResourceARN, Tags):
        tag_dict = _convert_tags(Tags)
        for col in [self._gateways, self._fileshares, self._volumes, self._tapes]:
            if ResourceARN in col:
                existing = getattr(col[ResourceARN], "Tags", {})
                existing.update(tag_dict)
                return {"ResourceARN": ResourceARN}
        raise ResourceNotFoundException(f"Resource {ResourceARN} not found")

    def list_tags_for_resource(self, ResourceARN):
        for col_name in ["_gateways", "_fileshares", "_volumes", "_tapes"]:
            col = getattr(self, col_name)
            if ResourceARN in col:
                tags = getattr(col[ResourceARN], "Tags", {})
                tag_list = [{"Key": k, "Value": v} for k, v in tags.items()]
                return {"Tags": tag_list, "ResourceARN": ResourceARN}
        raise ResourceNotFoundException(f"Resource {ResourceARN} not found")

    def remove_tags_from_resource(self, ResourceARN, TagKeys):
        for col_name in ["_gateways", "_fileshares", "_volumes", "_tapes"]:
            col = getattr(self, col_name)
            if ResourceARN in col:
                tags = getattr(col[ResourceARN], "Tags", {})
                for k in TagKeys:
                    tags.pop(k, None)
                return {"ResourceARN": ResourceARN}
        raise ResourceNotFoundException(f"Resource {ResourceARN} not found")
