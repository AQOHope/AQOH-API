from fastapi import Header, HTTPException


async def get_token_header(x_token: str = Header(default=None)):
    if x_token != "AQOH-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def get_query_token(token: str):
    if token != "AQOH":
        raise HTTPException(status_code=400, detail="No AQOH token provided")