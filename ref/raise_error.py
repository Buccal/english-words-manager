from fastapi import HTTPException, status

def raise_error(code, detail):
	if(code == 400):
		raise HTTPException(
            status_code=400,
            detail=detail,
        )
	elif(code == 401):
		raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=detail,
            headers={"WWW-Authenticate": "Bearer"}, # 规范要求
        )

