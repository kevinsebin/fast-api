from fastapi import FastAPI

app = FastAPI()


@app.get('/add/{first}+{second}')
def add(first, second):
    sum = int(first) + int(second)
    return {'sum' : sum}

@app.get('/percent/{first}/{second}')
def percent(first, second):
    percent = (int(first) / int(second)) * 100
    return {'percent' : percent}


