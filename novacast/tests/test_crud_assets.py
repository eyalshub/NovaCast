import pytest
from app.db.crud.assets import create_asset, get_asset, update_asset, delete_asset
from app.db.models.asset import Asset

@pytest.fixture
def asset_data():
    return {
        "name": "Test Asset",
        "description": "This is a test asset.",
        "url": "http://example.com/test-asset"
    }

def test_create_asset(asset_data):
    asset = create_asset(asset_data)
    assert asset.name == asset_data["name"]
    assert asset.description == asset_data["description"]
    assert asset.url == asset_data["url"]

def test_get_asset(asset_data):
    asset = create_asset(asset_data)
    fetched_asset = get_asset(asset.id)
    assert fetched_asset is not None
    assert fetched_asset.id == asset.id

def test_update_asset(asset_data):
    asset = create_asset(asset_data)
    updated_data = {"name": "Updated Asset"}
    updated_asset = update_asset(asset.id, updated_data)
    assert updated_asset.name == updated_data["name"]
    assert updated_asset.description == asset.description  # Ensure other fields remain unchanged

def test_delete_asset(asset_data):
    asset = create_asset(asset_data)
    delete_asset(asset.id)
    fetched_asset = get_asset(asset.id)
    assert fetched_asset is None  # Asset should be deleted and not found