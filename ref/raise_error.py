from fastapi import HTTPException, status

def raise_error(code: int, detail: str):
    if(code == 401):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=detail,
            headers={"WWW-Authenticate": "Bearer"}, # 规范要求
        )
    else:
        raise HTTPException(
            status_code=code,
            detail=detail,
        )
