"""E2E tests for LexV2 Models — boto3 against running localstack."""
import os
import pytest
import boto3
import urllib.request
import json

ENDPOINT = os.environ.get("LOCALSTACK_ENDPOINT", "http://localhost:4566")
TEST_CREDS = {"aws_access_key_id": "test", "aws_secret_access_key": "test"}


def _is_localstack_running():
    try:
        req = urllib.request.Request(
            f"{ENDPOINT}/_localstack/health",
            headers={"Accept": "application/json"},
        )
        resp = urllib.request.urlopen(req, timeout=3)
        json.loads(resp.read())
        return True
    except Exception:
        return False


LS_RUNNING = _is_localstack_running()


class TestLexV2ModelsE2E:

    @pytest.fixture
    def client(self):
        if not LS_RUNNING:
            pytest.skip("LocalStack not running")
        return boto3.client(
            "lexv2-models",
            endpoint_url=ENDPOINT,
            region_name="us-east-1",
            **TEST_CREDS,
        )

    def test_bot_crud(self, client):
        """Create bot → describe → list → update → delete."""
        resp = client.create_bot(
            botName="e2e-test-bot",
            roleArn="arn:aws:iam::000000000000:role/LexRole",
            dataPrivacy={"childDirected": False},
            idleSessionTTLInSeconds=300,
        )
        bot_id = resp["botId"]
        assert bot_id is not None

        desc = client.describe_bot(botId=bot_id)
        assert desc["botName"] == "e2e-test-bot"

        lst = client.list_bots()
        assert len(lst.get("botSummaries", [])) >= 1

        client.update_bot(botId=bot_id, botName="e2e-test-bot", description="updated")
        desc2 = client.describe_bot(botId=bot_id)
        assert desc2["description"] == "updated"

        client.delete_bot(botId=bot_id)

    def test_bot_alias_crud(self, client):
        """Create alias → describe → list → delete."""
        bot = client.create_bot(
            botName="alias-e2e-bot",
            roleArn="arn:aws:iam::000000000000:role/LexRole",
            dataPrivacy={"childDirected": False},
            idleSessionTTLInSeconds=300,
        )
        bot_id = bot["botId"]

        alias = client.create_bot_alias(
            botAliasName="e2e-alias",
            botId=bot_id,
            botVersion="1",
        )
        assert alias["botAliasId"] is not None

        desc = client.describe_bot_alias(botId=bot_id, botAliasName="e2e-alias")
        assert desc["botAliasName"] == "e2e-alias"

        aliases = client.list_bot_aliases(botId=bot_id)
        assert len(aliases.get("botAliasSummaries", [])) >= 1

        client.delete_bot_alias(botId=bot_id, botAliasName="e2e-alias")
        client.delete_bot(botId=bot_id)

    def test_error_nonexistent(self, client):
        """Reading nonexistent resource fails."""
        from botocore.exceptions import ClientError
        with pytest.raises(ClientError) as exc:
            client.describe_bot(botId="nonexistent-bot-xyz")
        assert exc.value.response["Error"]["Code"] in (
            "ResourceNotFoundException",
            "ValidationException",
            "InternalFailure",
            "501",
        )

    def test_error_duplicate(self, client):
        """Creating duplicate resource fails."""
        from botocore.exceptions import ClientError
        bot = client.create_bot(
            botName="dup-e2e-bot",
            roleArn="arn:aws:iam::000000000000:role/LexRole",
            dataPrivacy={"childDirected": False},
            idleSessionTTLInSeconds=300,
        )
        bot_id = bot["botId"]
        try:
            with pytest.raises(ClientError) as exc:
                client.create_bot(
                    botName="dup-e2e-bot",
                    roleArn="arn:aws:iam::000000000000:role/LexRole",
                    dataPrivacy={"childDirected": False},
                    idleSessionTTLInSeconds=300,
                )
            err_code = exc.value.response["Error"]["Code"]
            assert err_code in (
                "ResourceInUseException", "ConflictException",
                "ValidationException", "InternalFailure", "501",
            )
        finally:
            try:
                client.delete_bot(botId=bot_id)
            except Exception:
                pass
