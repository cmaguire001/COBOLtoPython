from fastapi import FastAPI
from pycobol_bridge.copybook import CopybookParser

app = FastAPI()

@app.get('/health')
def health():
    return {'status': 'ok'}
