from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.session import SessionLocal
from ali_backend.models.test_model import TestModel  # Adjust import to your model location

router = APIRouter()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/db-test")
def db_test(db: Session = Depends(get_db)):
    # Create test entry
    test_entry = TestModel(name="test entry")
    db.add(test_entry)
    db.commit()
    db.refresh(test_entry)

    # Query the entry back
    result = db.query(TestModel).filter_by(id=test_entry.id).first()
    if result:
        return {"message": "DB connection is working!", "id": result.id, "name": result.name}
    else:
        return {"message": "Something went wrong."}
