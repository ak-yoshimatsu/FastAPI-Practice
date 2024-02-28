from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from app.config.databases import get_section
from app.models.users import Patient

router = APIRouter()


@router.get("/")
async def index(session: Session = Depends(get_section)):
    result = session.exec(select(Patient)).all()
    return {
        "resultcode": "0000",
        "data": result,
    }


@router.post("/")
async def store_patienst(
    request: Patient,
    session: Session = Depends(get_section),
):
    session.add(request)
    session.commit()
    session.refresh(request)

    return request


@router.get(
    "/{id}",
    summary="患者詳細情報取得",
    response_description="取得成功",
    description="idを指定して患者の詳細情報を取得する",
    # operation_id="getDetailPatient",
    response_model=Patient,
)
def get_detail(
    id: int,
    session: Session = Depends(get_section),
):
    detail = session.get(Patient, id)
    if not detail:
        raise HTTPException(status_code=404, detail="そんなのありませーん！")
    return detai


@router.patch(
    "/{id}",
    summary="患者詳細情報更新",
    response_description="更新成功",
    description="idを指定して患者の詳細情報を更新する",
    # operation_id="updateDetailPatient",
)
async def update_detail(
    id: int,
    request: Patient,
    session: Session = Depends(get_section),
):
    db_patient = session.get(Patient, id)
    if not db_patient:
        raise HTTPException(status_code=404, detail="そんなのありませーん！")
    update_data = request.model_dump(exclude_unset=True)
    db_patient.sqlmodel_update(update_data)
    session.add(db_patient)
    session.commit()
    session.refresh(db_patient)
    return db_patient


@router.delete(
    "/{id}",
    summary="患者詳細情報削除",
    response_description="削除成功",
    description="idを指定して患者の詳細情報を削除する",
    # operation_id="updateDetailPatient",
)
async def delete_detail(
    id: int,
    request: Patient,
    session: Session = Depends(get_section),
):
    db_patient = session.get(Patient, id)
    if not db_patient:
        raise HTTPException(status_code=404, detail="そんなのありませーん！")
    session.delete(db_patient)
    session.commit()
    return {"id": db_patient}
