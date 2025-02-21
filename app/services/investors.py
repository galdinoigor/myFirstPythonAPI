from sqlalchemy.orm import Session

def get_ivestors_by_company(db: Session, company: str):
    query = """
    select unnest(investors) as investors
    from shared_drive.companies
    where lower(name) = lower(:company_id)
    """
    result = db.execute(query, {"company_id": company_id}).fetchall()
    if result:
        return [{"company_id": row.company_id, "investors": row.investor} for row in result]
    return []
