from fastapi import FastAPI
import os


app = FastAPI()


@app.get("/computeC/{first}/{second}/{sigma}")
def computeC(first: str, second: str, sigma: str):
    cmd = f'./computeC {first} {second} {sigma}'
    print(os.popen(cmd).read())
    value = int(os.popen(cmd).read())

    return value
