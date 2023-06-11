import numpy as np
import pickle

import numpy as np
import scipy.spatial
import pickle
import pandas as pd
import matplotlib.pyplot as plt
import random
from sklearn.cluster import KMeans
from sklearn.neighbors import NearestNeighbors
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import KMeans
import json
from dotenv import load_dotenv
import os
import base64
from requests import post,get
from sklearn.cluster import KMeans

data = np.load("pbldat.npy", allow_pickle= True)
nf = pickle.load(open("PBLKNN.pkl",'rb'))
model = pickle.load(open("SPalt.pkl",'rb'))

nf =  np.array(nf)

def get_token():
    auth_string = '578ab8eec910483d891f8aaeaf0bbef2:fb023288a36446dc957cf688d02be5fc'
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    result = post(url,headers = headers,data = data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

def get_auth_header(token):
    return{"Authorization": "Bearer " + token}

def get_track_name(token, track_id):
    url = f"https://api.spotify.com/v1/tracks/{track_id}"
    headers = get_auth_header(token)
    result = get(url, headers = headers)
    json_result = json.loads(result.content)
    name = (json_result['name'])
    artist = (json_result['album']['artists'][0]['name'])
    url = json_result['album']['images'][0]['url']
    dir_url = json_result['external_urls']['spotify']
    pre_url = json_result['preview_url']
    ans = [name,artist,url,dir_url,pre_url]
    return ans     

def get_track_info(token, track_id):
    url = f"https://api.spotify.com/v1/audio-features/{track_id}"

    headers = get_auth_header(token)
    result1 = get(url, headers = headers)
    json_result1 = json.loads(result1.content)
    return(json_result1)
