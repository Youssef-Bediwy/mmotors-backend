# main.py - Application FastAPI M-Motors Backend
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title='M-Motors API', version='1.0.0')

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*'],
)

@app.get('/')
def root():
    return {'message': 'HELLO WORLD', 'service': 'M-Motors Backend API'}

@app.get('/health')
def health():
    return {'status': 'ok'}
