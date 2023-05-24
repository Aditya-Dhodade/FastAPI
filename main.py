# from flask import Flask, request
from fastapi import FastAPI, Body

# import numpy as np
# import pandas as pd
# from dotenv import load_dotenv
# import support
# load_dotenv()
# temp = pd.read_csv("PBLFinalDatawithClusters.csv")


# app = Flask(__name__)
app = FastAPI()

# @app.route('/get_recomm')
# def show():

@app.get("/")
def read_root():
    return {"Hello": "World"}

# @app.post("/get_recomm")
# async def process_string(weight_string: str):
#     print(weight_string)
#     # weight = '0.3+0.5+0+0+0+0+0+0+0+0+0+0+0+0'
#     print('something')
#     weight_vec = []
#     s = ""
#     for i in range(len(weight_string)):
#         if weight_string[i] == ' ':
#             weight_vec.append(float(s))
#             s = ""
#         else:
#             s += weight_string[i]
#     print(weight_vec)
#     garbage, clun = support.model.kneighbors (np.array(weight_vec).reshape(1,-1)) 
#     del garbage
#     clunum = clun[0][0]
#     d,index = support.nf[clunum].kneighbors (np.array(weight_vec).reshape(1,-1))

#     print(clunum)
#     print(index)
    
#     token = support.get_token()
#     uri_ls = []
#     token = support.get_token()
#     for i in range(5):
#         uri_ls.append(temp['uri'][index[0][i]])
#     track_names = []
#     for i in uri_ls:
#         track_names.append(support.get_track_name(token, i))
#     json_val = {}
#     count = 0
#     for i in track_names:
#         temp_json = {"name":i[0],
#                     "artist":i[1],
#                     "poster_link":i[2],
#                     "redirect_link":i[3],
#                     "preview_link": i[4]
#                     }
#         json_val[count] = temp_json
#         count += 1
#     json_val    
        
#     print(track_names)
#     return json_val

