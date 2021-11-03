from fastapi import FastAPI, Request

app = FastAPI()

@app.get('/{date}/{month}/{year}')
def date(date : str, month : str, year : str):
    days = {0 : 'Sunday', 1 : 'Monday', 2 : 'Tuesday', 3 : 'Wednesday', 4 : 'Thursday', 5 : 'Friday', 6 : 'Saturday'}
    month_dict = {'1' : '11', '2' : '12', '3' : '01', '4' : '02', '5' : '03', '6' : '04', '7' : '05', '8' : '06', '9' : '07', '10' : '08', '11' : '09', '12' : '10'}

    k = int(date)
    m = month

    if int(k) > 31:
        return {'error' : 'date cannot be greater than 31'}
    elif int(m) > 12:
        return {'error' : 'month cannot be greater than 12'}
    else:
        m = str(int(m))
        m = int(month_dict[m])
        print(m)
        d, c = int(year[2:5]), int(year[0:2])
        m = int(m)
        formula = k+ ((13*m-1)//5) +d+ (d//4) +(c//4)-2*c
        ans = formula % 7
        day = days[ans]
        return {'day' : day}


