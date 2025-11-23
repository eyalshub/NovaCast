from fastapi import APIRouter, HTTPException, Depends
from app.db.crud.assets import create_asset, get_asset, update_asset, delete_asset, list_assets
from app.models.asset import AssetCreate, AssetUpdate, Asset
from app.api.deps.auth import get_current_user

router = APIRouter()

@router.post("/", response_model=Asset)
async def create_new_asset(asset: AssetCreate, current_user: str = Depends(get_current_user)):
    return await create_asset(asset)

@router.get("/{asset_id}", response_model=Asset)
async def read_asset(asset_id: str, current_user: str = Depends(get_current_user)):
    asset = await get_asset(asset_id)
    if asset is None:
        raise HTTPException(status_code=404, detail="Asset not found")
    return asset

@router.put("/{asset_id}", response_model=Asset)
async def update_existing_asset(asset_id: str, asset: AssetUpdate, current_user: str = Depends(get_current_user)):
    updated_asset = await update_asset(asset_id, asset)
    if updated_asset is None:
        raise HTTPException(status_code=404, detail="Asset not found")
    return updated_asset

@router.delete("/{asset_id}", response_model=dict)
async def delete_existing_asset(asset_id: str, current_user: str = Depends(get_current_user)):
    success = await delete_asset(asset_id)
    if not success:
        raise HTTPException(status_code=404, detail="Asset not found")
    return {"message": "Asset deleted successfully"}

@router.get("/", response_model=list[Asset])
async def list_all_assets(current_user: str = Depends(get_current_user)):
    return await list_assets()