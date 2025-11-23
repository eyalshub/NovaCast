from sqlalchemy.orm import Session
from app.db.models.asset import Asset
from app.utils.errors import NotFoundError

def create_asset(db: Session, asset: Asset) -> Asset:
    db.add(asset)
    db.commit()
    db.refresh(asset)
    return asset

def get_asset(db: Session, asset_id: int) -> Asset:
    asset = db.query(Asset).filter(Asset.id == asset_id).first()
    if asset is None:
        raise NotFoundError(f"Asset with id {asset_id} not found")
    return asset

def get_assets(db: Session, skip: int = 0, limit: int = 100) -> list[Asset]:
    return db.query(Asset).offset(skip).limit(limit).all()

def update_asset(db: Session, asset_id: int, updated_asset: Asset) -> Asset:
    asset = get_asset(db, asset_id)
    for key, value in updated_asset.dict().items():
        setattr(asset, key, value)
    db.commit()
    db.refresh(asset)
    return asset

def delete_asset(db: Session, asset_id: int) -> None:
    asset = get_asset(db, asset_id)
    db.delete(asset)
    db.commit()