from sqlalchemy.orm import Session

def get_avg_funding_by_person(db: Session, person_id: int):
    query = """
    SELECT p.person_id,
    AVG(coalesce(c.known_total_funding,0)) AS avg_funding
    FROM SHARED_DRIVE.PEOPLE p
    left join (
	    select unnest(company_linkedin_names) as company_linkedin_name,
	    known_total_funding
	    from shared_drive.companies
	    group by 1, 2
    ) c
    on p.company_li_name = c.company_linkedin_name
    where p.person_id = :person_id
    group by 1
    """
    result = db.execute(query, {"person_id": person_id, "avg_funding": row.avg_funding}).fetchone()
    if result and result.avg_funding is not None:
        return float(result.avg_funding)
    return None
