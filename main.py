import numpy as np
import pandas as pd
from dotenv import load_dotenv
import support
from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

load_dotenv()
temp = pd.read_csv("PBLFinalDatawithClusters.csv")

app = FastAPI()
origins = [
    'https://fastapi-production-3bee.up.railway.app'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

@app.route('/show')
def show():
    return "working"

@app.get("/test")
async def fortest_string(test_string: str):
    temp = test_string.upper()
    return temp

@app.post("/get_recomm")
async def process_string(weight_string: str):
    print('something')
    weight_vec = []
    s = ""
    for i in range(len(weight_string)):
        if weight_string[i] == ' ':
            weight_vec.append(float(s))
            s = ""
        else:
            s += weight_string[i]
    print(weight_vec)
    garbage, clun = support.model.kneighbors (np.array(weight_vec).reshape(1,-1)) 
    del garbage
    clunum = clun[0][0]
    d,index = support.nf[clunum].kneighbors (np.array(weight_vec).reshape(1,-1))

    print(clunum)
    print(index)
    
    token = support.get_token()
    uri_ls = []
    token = support.get_token()
    for i in range(5):
        uri_ls.append(temp['uri'][index[0][i]])
    track_names = []
    weights = []
    for i in uri_ls:
        track_names.append(support.get_track_name(token, i))
        temp1 = support.get_track_info(token, i)
        s = ""
        lst = ["danceability","energy","key","loudness","mode","speechiness","acousticness","instrumentalness","liveness","valence","tempo","time_signature"]
        for i in lst:
            s += "+" + str(temp1[i])
        s  = s[1:] + "+0+0"
        weights.append(s)
    
    json_val = {}
    count = 0
    for i in track_names:
        temp_json = {"name":i[0],
                    "artist":i[1],
                    "poster_link":i[2],
                    "redirect_link":i[3],
                    "preview_link": i[4],
                    "weight_str":weights[count]
                    }
        json_val[count] = temp_json
        count += 1        
    print('result is: ',track_names)
    print(type(json_val))
    return json_val
