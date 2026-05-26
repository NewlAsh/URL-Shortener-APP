#main_url.py
from fastapi.middleware.cors import CORSMiddleware  # ← new import

from fastapi import FastAPI
from typing import Annotated
from fastapi import HTTPException, Depends, status
from sqlalchemy import select
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from datetime import UTC, datetime
from main_database import get_db, Base, engine
from main_model import ShortURL
from main_utils import generate_code
from main_schemas import Url_Response, Url

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


Base.metadata.create_all(bind=engine)

@app.post(f"/short", name="Enter_the_new_url", response_model=Url_Response)
def post_url(request: Url, db: Annotated[Session, Depends(get_db)]):
    result = db.execute(select(ShortURL).where(ShortURL.url == request.url))
    
    url_database = result.scalars().first()
    if url_database:
        return {
    "url": url_database.url,
    "code_used": url_database.code,
    "expiry": url_database.expires_at
    }
    

    while True:
        code = generate_code()
        
        result = db.execute(select(ShortURL).where(ShortURL.code == code))
        required_code = result.scalars().first()
        if not required_code:
            break

    new_url = ShortURL(
        url = request.url,
        code = code,
        expires_at = request.expires_at
    )
    db.add(new_url)
    db.commit()
    db.refresh(new_url)

    return {
    "url": new_url.url,
    "code_used": new_url.code
    }


@app.get("/redirect", name="page_to_enter_the_code")
def redirect(s_code: str, db: Annotated[Session, Depends(get_db)]):
    result = db.execute(select(ShortURL).where(ShortURL.code == s_code))
    code_required = result.scalars().first()

    if not code_required:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid short code entered...Enter another code please!!")
    
    print(code_required.expires_at)
    
    if code_required.expires_at and code_required.expires_at < datetime.now():
        db.delete(code_required)
        db.commit()

        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Code expired! Kindly generate a new code please...")
    
    url_required = code_required.url
    code_required.click_cnt += 1
    db.commit()
    return RedirectResponse(url=url_required)
    
