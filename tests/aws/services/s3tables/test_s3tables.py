import pytest
from botocore.exceptions import ClientError

from localstack.testing.pytest import markers
from localstack.utils.strings import short_uid


class TestS3Tables:
    @staticmethod
    def _transform_dynamic(snapshot):
        for key in (
            "arn",
            "tableARN",
            "tableBucketARN",
            "tableBucketId",
            "namespaceId",
            "versionToken",
            "createdAt",
            "modifiedAt",
        ):
            snapshot.add_transformer(snapshot.transform.key_value(key))

    @staticmethod
    def _match_error(snapshot, name, exc_info):
        snapshot.match(name, exc_info.value.response)
        assert exc_info.value.response["Error"]["Code"] in (
            "ConflictException",
            "NotFoundException",
        )

    @markers.aws.only_localstack
    def test_table_bucket_crud_and_listing(self, aws_client, cleanups, snapshot):
        self._transform_dynamic(snapshot)
        bucket_name = f"test-bucket-{short_uid()}"
        create = aws_client.s3tables.create_table_bucket(name=bucket_name)
        bucket_arn = create["arn"]
        cleanups.append(
            lambda: aws_client.s3tables.delete_table_bucket(tableBucketARN=bucket_arn)
        )
        snapshot.match("create-table-bucket", create)

        get_result = aws_client.s3tables.get_table_bucket(tableBucketARN=bucket_arn)
        snapshot.match("get-table-bucket", get_result)

        list_result = aws_client.s3tables.list_table_buckets(
            prefix=bucket_name[:10], maxBuckets=1
        )
        snapshot.match("list-table-buckets", list_result)

        with pytest.raises(ClientError) as duplicate:
            aws_client.s3tables.create_table_bucket(name=bucket_name)
        self._match_error(snapshot, "duplicate-table-bucket", duplicate)

        with pytest.raises(ClientError) as missing:
            aws_client.s3tables.get_table_bucket(
                tableBucketARN=f"arn:aws:s3tables:::bucket/missing-{short_uid()}"
            )
        self._match_error(snapshot, "missing-table-bucket", missing)

    @markers.aws.only_localstack
    def test_namespace_crud_and_listing(self, aws_client, cleanups, snapshot):
        self._transform_dynamic(snapshot)
        bucket = aws_client.s3tables.create_table_bucket(name=f"ns-bucket-{short_uid()}")
        bucket_arn = bucket["arn"]
        cleanups.append(
            lambda: aws_client.s3tables.delete_table_bucket(tableBucketARN=bucket_arn)
        )
        snapshot.match("namespace-bucket-create", bucket)

        namespace_name = f"namespace-{short_uid()}"
        create = aws_client.s3tables.create_namespace(
            tableBucketARN=bucket_arn, namespace=[namespace_name]
        )
        snapshot.match("create-namespace", create)

        get_result = aws_client.s3tables.get_namespace(
            tableBucketARN=bucket_arn, namespace=namespace_name
        )
        snapshot.match("get-namespace", get_result)

        list_result = aws_client.s3tables.list_namespaces(
            tableBucketARN=bucket_arn, prefix=namespace_name[:10], maxNamespaces=1
        )
        snapshot.match("list-namespaces", list_result)

        with pytest.raises(ClientError) as duplicate:
            aws_client.s3tables.create_namespace(
                tableBucketARN=bucket_arn, namespace=[namespace_name]
            )
        self._match_error(snapshot, "duplicate-namespace", duplicate)

        with pytest.raises(ClientError) as missing:
            aws_client.s3tables.get_namespace(
                tableBucketARN=bucket_arn, namespace=f"missing-{short_uid()}"
            )
        self._match_error(snapshot, "missing-namespace", missing)

        delete_result = aws_client.s3tables.delete_namespace(
            tableBucketARN=bucket_arn, namespace=namespace_name
        )
        snapshot.match("delete-namespace", delete_result)

        with pytest.raises(ClientError) as deleted:
            aws_client.s3tables.delete_namespace(
                tableBucketARN=bucket_arn, namespace=namespace_name
            )
        self._match_error(snapshot, "delete-missing-namespace", deleted)

    @markers.aws.only_localstack
    def test_table_crud_listing_and_rename(self, aws_client, cleanups, snapshot):
        self._transform_dynamic(snapshot)
        bucket = aws_client.s3tables.create_table_bucket(name=f"table-bucket-{short_uid()}")
        bucket_arn = bucket["arn"]
        cleanups.append(
            lambda: aws_client.s3tables.delete_table_bucket(tableBucketARN=bucket_arn)
        )
        snapshot.match("table-bucket-create", bucket)

        namespace = f"namespace-{short_uid()}"
        namespace_result = aws_client.s3tables.create_namespace(
            tableBucketARN=bucket_arn, namespace=[namespace]
        )
        snapshot.match("table-namespace-create", namespace_result)

        table_name = f"table-{short_uid()}"
        create = aws_client.s3tables.create_table(
            tableBucketARN=bucket_arn,
            namespace=namespace,
            name=table_name,
            format="ICEBERG",
        )
        snapshot.match("create-table", create)

        get_result = aws_client.s3tables.get_table(
            tableBucketARN=bucket_arn, namespace=namespace, name=table_name
        )
        snapshot.match("get-table", get_result)

        list_result = aws_client.s3tables.list_tables(
            tableBucketARN=bucket_arn,
            namespace=namespace,
            prefix=table_name[:10],
            maxTables=1,
        )
        snapshot.match("list-tables", list_result)

        renamed = f"renamed-{short_uid()}"
        rename_result = aws_client.s3tables.rename_table(
            tableBucketARN=bucket_arn,
            namespace=namespace,
            name=table_name,
            newName=renamed,
        )
        snapshot.match("rename-table", rename_result)

        with pytest.raises(ClientError) as missing:
            aws_client.s3tables.get_table(
                tableBucketARN=bucket_arn, namespace=namespace, name=table_name
            )
        self._match_error(snapshot, "missing-renamed-table", missing)

        with pytest.raises(ClientError) as duplicate:
            aws_client.s3tables.create_table(
                tableBucketARN=bucket_arn, namespace=namespace, name=renamed
            )
        self._match_error(snapshot, "duplicate-table", duplicate)

        delete_result = aws_client.s3tables.delete_table(
            tableBucketARN=bucket_arn, namespace=namespace, name=renamed
        )
        snapshot.match("delete-table", delete_result)

        with pytest.raises(ClientError) as deleted:
            aws_client.s3tables.delete_table(
                tableBucketARN=bucket_arn, namespace=namespace, name=renamed
            )
        self._match_error(snapshot, "delete-missing-table", deleted)

    @markers.aws.only_localstack
    def test_encryption_and_maintenance_defaults(self, aws_client, cleanups, snapshot):
        self._transform_dynamic(snapshot)
        bucket = aws_client.s3tables.create_table_bucket(name=f"config-bucket-{short_uid()}")
        bucket_arn = bucket["arn"]
        cleanups.append(
            lambda: aws_client.s3tables.delete_table_bucket(tableBucketARN=bucket_arn)
        )
        snapshot.match("config-bucket-create", bucket)

        namespace = f"namespace-{short_uid()}"
        namespace_result = aws_client.s3tables.create_namespace(
            tableBucketARN=bucket_arn, namespace=[namespace]
        )
        snapshot.match("config-namespace-create", namespace_result)
        table = f"table-{short_uid()}"
        table_result = aws_client.s3tables.create_table(
            tableBucketARN=bucket_arn, namespace=namespace, name=table
        )
        snapshot.match("config-table-create", table_result)

        bucket_encryption = aws_client.s3tables.get_table_bucket_encryption(
            tableBucketARN=bucket_arn
        )
        snapshot.match("table-bucket-encryption", bucket_encryption)
        table_encryption = aws_client.s3tables.get_table_encryption(
            tableBucketARN=bucket_arn, namespace=namespace, name=table
        )
        snapshot.match("table-encryption", table_encryption)
        bucket_maintenance = aws_client.s3tables.get_table_bucket_maintenance_configuration(
            tableBucketARN=bucket_arn
        )
        snapshot.match("table-bucket-maintenance", bucket_maintenance)
        table_maintenance = aws_client.s3tables.get_table_maintenance_configuration(
            tableBucketARN=bucket_arn, namespace=namespace, name=table
        )
        snapshot.match("table-maintenance", table_maintenance)

    @markers.aws.only_localstack
    def test_tag_round_trip(self, aws_client, cleanups, snapshot):
        self._transform_dynamic(snapshot)
        bucket = aws_client.s3tables.create_table_bucket(name=f"tag-bucket-{short_uid()}")
        bucket_arn = bucket["arn"]
        cleanups.append(
            lambda: aws_client.s3tables.delete_table_bucket(tableBucketARN=bucket_arn)
        )
        snapshot.match("tag-bucket-create", bucket)

        tag_result = aws_client.s3tables.tag_resource(
            resourceArn=bucket_arn,
            tags=[{"key": "environment", "value": "test"}],
        )
        snapshot.match("tag-resource", tag_result)
        dict_tag_result = aws_client.s3tables.tag_resource(
            resourceArn=bucket_arn, tags={"owner": "totalstack"}
        )
        snapshot.match("tag-resource-dict", dict_tag_result)

        listed = aws_client.s3tables.list_tags_for_resource(resourceArn=bucket_arn)
        snapshot.match("list-tags", listed)
        untagged = aws_client.s3tables.untag_resource(
            resourceArn=bucket_arn, tagKeys=["environment"]
        )
        snapshot.match("untag-resource", untagged)
        listed_after = aws_client.s3tables.list_tags_for_resource(resourceArn=bucket_arn)
        snapshot.match("list-tags-after-untag", listed_after)

    @markers.aws.only_localstack
    def test_delete_table_bucket(self, aws_client, cleanups, snapshot):
        self._transform_dynamic(snapshot)
        bucket = aws_client.s3tables.create_table_bucket(name=f"delete-bucket-{short_uid()}")
        bucket_arn = bucket["arn"]
        cleanups.append(
            lambda: aws_client.s3tables.delete_table_bucket(tableBucketARN=bucket_arn)
        )
        snapshot.match("delete-bucket-create", bucket)
        delete_result = aws_client.s3tables.delete_table_bucket(tableBucketARN=bucket_arn)
        snapshot.match("delete-table-bucket", delete_result)
        with pytest.raises(ClientError) as missing:
            aws_client.s3tables.delete_table_bucket(tableBucketARN=bucket_arn)
        self._match_error(snapshot, "delete-missing-table-bucket", missing)
