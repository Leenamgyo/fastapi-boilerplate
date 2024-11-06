from fastapi import FastAPI # FastAPI 라이브러리를 임포트합니다.

app = FastAPI() # FastAPI 애플리케이션을 생성합니다.

# "/" 경로로 요청이 들어오면 실행될 함수입니다.
@app.get("/")
async def read_root():
    return {"Hello": "World"} # {"Hello": "World"} 응답을 반환합니다.