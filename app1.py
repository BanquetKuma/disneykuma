#!/usr/bin/env python
# coding: utf-8

# In[1]:


import plotly
import plotly_express as px
import pandas as pd
from pathlib import Path
import numpy as np
import os
from bottle import route, run
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def set_index_datetime(df):
    df["datetime"]=pd.to_datetime(df["datetime"],infer_datetime_format=True) 
    #datetime列をdatetime型に変換、infer_datetime_format=Trueで変換速度アップ
    df["DATETIME"]=df["datetime"]
    #datetime列をDATETIME列にコピー
    df=df.set_index(["datetime"])
    #datetime列をindexにする
    df=df.dropna(subset=["wait_time(actual)"])
    #wait_time(actual)列の要素がNaNの行は落とす
    df=df.loc["2018-07":"2018-12"]
    #indexを７月〜１２月で絞る
    df.loc[df["wait_time(actual)"] < 0,"wait_time(actual)"]=np.nan
    #ait_time(actual)列の要素が負の場合NaNに置き換える
    df.loc[df["wait_time(actual)"]>1000,"wait_time(actual)"]=np.nan
    #ait_time(actual)列の要素が１０００より大きい場合NaNに置き換える
    return df

splash_mountain=pd.read_csv("/Users/yuza/PycharmProjects/untitled4/Altair/2018/splash_mountain.csv")
splash_mountain["attractions"]="Splash Mountain"
splash_mountain=set_index_datetime(splash_mountain)
splash_mountain["Longtitude"]=-81.585040
splash_mountain["Latitude"]=28.419170

seven_dwarfs_train=pd.read_csv("https://raw.githubusercontent.com/BanquetKuma/disneykuma/master/7_dwarfs_train.csv")
seven_dwarfs_train["attractions"]="Seven Dwarfs Train"
seven_dwarfs_train=set_index_datetime(seven_dwarfs_train)
seven_dwarfs_train["Longtitude"]=-81.580442
seven_dwarfs_train["Latitude"]=28.420571

dinosaur=pd.read_csv("https://raw.githubusercontent.com/BanquetKuma/disneykuma/master/dinosaur.csv")
dinosaur["attractions"]="Dinosaur"
dinosaur=set_index_datetime(dinosaur)
dinosaur["Longtitude"]=-81.588307
dinosaur["Latitude"]=28.355354

Expedition_Everest=pd.read_csv("https://raw.githubusercontent.com/BanquetKuma/disneykuma/master/expedition_everest.csv")
Expedition_Everest["attractions"]="Expedition Everest"
Expedition_Everest=set_index_datetime(Expedition_Everest)
Expedition_Everest["Longtitude"]=-81.587138
Expedition_Everest["Latitude"]=28.358794

flight_of_passage=pd.read_csv("https://raw.githubusercontent.com/BanquetKuma/disneykuma/master/flight_of_passage.csv")
flight_of_passage["attractions"]="Avatar Flight of Passage"
flight_of_passage=set_index_datetime(flight_of_passage)
flight_of_passage["Longtitude"]=-81.592119
flight_of_passage["Latitude"]=28.355869

kilimanjaro_safaris=pd.read_csv("https://raw.githubusercontent.com/BanquetKuma/disneykuma/master/kilimanjaro_safaris.csv")
kilimanjaro_safaris["attractions"]="Kilimanjaro Safaris"
kilimanjaro_safaris=set_index_datetime(kilimanjaro_safaris)
kilimanjaro_safaris["Longtitude"]=-81.592423
kilimanjaro_safaris["Latitude"]=28.359728

Pirates_of_Caribbean=pd.read_csv("https://raw.githubusercontent.com/BanquetKuma/disneykuma/master/pirates_of_caribbean.csv")
Pirates_of_Caribbean["attractions"]="Pirates of the Caribbean"
Pirates_of_Caribbean=set_index_datetime(Pirates_of_Caribbean)
Pirates_of_Caribbean["Longtitude"]=-81.584227
Pirates_of_Caribbean["Latitude"]=28.418099


Rock_Coaster=pd.read_csv("https://raw.githubusercontent.com/BanquetKuma/disneykuma/master/rock_n_rollercoaster.csv")
Rock_Coaster["attractions"]="Rock 'n' Roller Coaster Starring Aerosmith"
Rock_Coaster=set_index_datetime(Rock_Coaster)
Rock_Coaster["Longtitude"]=-81.560980
Rock_Coaster["Latitude"]=28.359658

Soarin=pd.read_csv("https://raw.githubusercontent.com/BanquetKuma/disneykuma/master/soarin.csv")
Soarin["attractions"]="Soarin"
Soarin=set_index_datetime(Soarin)
Soarin["Longtitude"]=-81.552317
Soarin["Latitude"]=28.373884

Spaceship_Earth=pd.read_csv("https://raw.githubusercontent.com/BanquetKuma/disneykuma/master/spaceship_earth.csv")
Spaceship_Earth["attractions"]="Spaceship Earth"
Spaceship_Earth=set_index_datetime(Spaceship_Earth)
Spaceship_Earth["Longtitude"]=-81.549391
Spaceship_Earth["Latitude"]=28.375437

Toy_Story_Mania=pd.read_csv("https://raw.githubusercontent.com/BanquetKuma/disneykuma/master/toy_story_mania.csv")
Toy_Story_Mania["attractions"]="Toy Story Mania!"
Toy_Story_Mania=set_index_datetime(Toy_Story_Mania)
Toy_Story_Mania["Longtitude"]=-81.561473
Toy_Story_Mania["Latitude"]=28.356091

#Alien_Swirling_Saucers=pd.read_csv("")
#Alien_Swirling_Saucers["attractions"]="Alien Swirling Saucers"
#Alien_Swirling_Saucers=set_index_datetime(Alien_Swirling_Saucers)
#Alien_Swirling_Saucers["Longtitude"]=-81.562727
#Alien_Swirling_Saucers["Latitude"]=28.355555


Navi_River=pd.read_csv("https://raw.githubusercontent.com/BanquetKuma/disneykuma/master/navi_river.csv")
Navi_River["attractions"]="Na'vi River Journey"
Navi_River=set_index_datetime(Navi_River)
Navi_River["Longtitude"]=-81.591670
Navi_River["Latitude"]=28.355311

df=pd.concat([dinosaur,flight_of_passage,Expedition_Everest,kilimanjaro_safaris,Navi_River])
#DateFrameを縦につなげる

df=df.sort_values("DATETIME")
#日付時刻順にソートしておく

df=df.dropna(subset=["wait_time(actual)"])
#何故か"wait_time(actual)"列にNaNが残っているので、もう一回弾く

df["Wait Time(min)"]=df["wait_time(actual)"]
#"wait_time(actual)"列を"Wait Time(min)"列にコピーする

px.set_mapbox_access_token("pk.eyJ1IjoiYmFucXVldGt1bWEiLCJhIjoiY2p0YjZ4bGJ2MGlseTN5bzlxcnlsbW8xNCJ9.udbxOpc2gZQcUX4m1VIqBg")
#mapboxのtokenを読み込む

pp=px.scatter_mapbox(df,
                  lat="Latitude",
                  lon="Longtitude",
                  color="Wait Time(min)",
                  size="Wait Time(min)",
                  size_max=60, 
                  zoom=10,
                  animation_frame="DATETIME",
                  animation_group="attractions",
                  color_continuous_scale=px.colors.cyclical.IceFire,
                  hover_name="attractions",
                  title="Disney's Animal Kingdom Theme Park Wait Time from {} to {}".format(df["DATETIME"].min(),df["DATETIME"].max()))
#plotly_expressの描画部分

@route("/")
def kumapx():
    return pp

run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))




