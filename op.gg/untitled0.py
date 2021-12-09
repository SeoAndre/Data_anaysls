# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 17:09:33 2021

@author: Hamartia
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#plt.plot([1,2,3,4,5])
#plt.xlabel('count')
#plt.ylabel('numbers')
#plt.show()

#alphabet=['a','b','c']
#values=[1,50,100]

#plt.figure(figsize=(12,4))

#plt.subplot(1,3,1)
#plt.bar(alphabet, values)
#plt.subplot(1,3,2)
#plt.scatter(alphabet, values)
#plt.subplot(1,3,3)
#plt.plot(alphabet, values)
#plt.suptitle('Categorical Plotting')

data=pd.read_csv("C:/Users/yjss1/Desktop/e스포츠 데이터 분석가 양성과정/BIPA_data.csv",index_col=0)
#data1_10=data[data['championId'].isin(range(0,10))]
#group1_10=data1_10.groupby('championId',as_index=False).mean()
#fig, ax=plt.subplots(figsize=(7,4))
#ax.barh(group1_10['championId'],
#        group1_10['totalDamageDealtToChampions'])

#import requests
#champ_ver = requests.get('https://ddragon.leagueoflegends.com/realms/na.json').json()['n']['champion']
#championJsonURL = 'http://ddragon.leagueoflegends.com/cdn/'+champ_ver+'/data/en_US/champion.json'
#request = requests.get(championJsonURL)
#champion_data=request.json()
#champion_data.keys()
#champion_dict = {}
#for c_name in champion_data['data'].keys() :
#    champion_dict[int(champion_data['data'][c_name]['key'])]=c_name
#champion_dict.keys()
#champion = pd.DataFrame.from_dict(champion_dict, orient = 'index', columns = ['champion'])
#
#group1_10=pd.merge(group1_10,champion,
#                   left_on='championId',
#                   right_index=True)

#fig, ax=plt.subplots(figsize=(7,4))
#ax.barh(group1_10['champion'],
#        group1_10['totalDamageDealtToChampions'])

#group1_10['totalDamageDealtToChampions'].plot(kind='barh')

#group1_10.index=group1_10.champion
#group1_10['totalDamageDealtToChampions'].plot(kind='barh')
#sns.set_palette('bright')
#fig, ax=plt.subplots(figsize=(7,4))
#ax.barh(group1_10[champion],
#        group1_10['totalDamageDealtToChampions'])

#fig, ax = plt.subplots(figsize=(7,4))
#sns.barplot(data=group1_10, 
#            x='totalDamageDealtToChampions',
#            y='champion')
#ax.set_xlabel('Avg_damage')
#ax.set_ylabel('Champion Name')
#ax.set_title('Avg Champion Damage')
#font_label={'color':'blue','weight':'bold'}
#font_title={
#    'family':'serif',
#    'size':20,
#    'color':'brown',
#    'weight':'bold',
#    'verticalalignment':'baseline',
#    'horizontalalignment':'center'}
#fig,ax=plt.subplots(figsize=(7,4))
#sns.barplot(data=group1_10,
#            x='totalDamageDealtToChampions',
 #           y='champion')
#ax.set_xlim(10000,20000)
#damage_mean=group1_10['totalDamageDealtToChampions'].mean()
#ax.axvline(damage_mean,ls='-',lw=5,color='brown')
#arrowprops={'arrowstyle':'->'}
#ax.annotate("average",(damage_mean, 2.5),
#            xytext=(17000,2.5), color='green',
#            fontfamily='serif', fontstyle='italic',
#            fontsize=15, arrowprops=arrowprops)
#ax.set_xlabel('Avg_damage',fontdict=font_label,
#              labelpad=20)
#ax.set_ylabel('Champion Name',
#              color='blue',labelpad=100)
#ax.set_title('Avg Champion Damage', 
#             fontdict=font_title,pad=12)

#group_data=data[data['gameLength']>1200].groupby(
#    ['position','championId'],as_index=False).mean()
#sns.violinplot(y=data['totalDamageDealtToChampions'],
#               x=data['position'])
#sns.boxplot(y=data['totalDamageDealtToChampions'],
#               x=data['position'])
#sns.displot(data[data['totalDamageDealtToChampions']<60000]
#            ['totalDamageDealtToChampions'])
#sns.displot(group_data, x='totalDamageDealtToChampions',
#            hue='level')
#sns.displot(group_data[group_data['position'].isin(['A','S'])],
#            x='totalDamageDealtToChampions', hue='position',
#            multiple='dodge',height=4,aspect=2)
#champ_stats=pd.read_csv("C:/Users/yjss1/Desktop/e스포츠 데이터 분석가 양성과정/champ_stats.csv")
#sns.scatterplot(data=champ_stats,x='hp',y='hp_18')
#for name in champ_stats['championName']:
#    plt.text(x=champ_stats[champ_stats['championName']==name]['hp']+0.3,
#             y=champ_stats[champ_stats['championName']==name]['hp_18']+0.3,
#             s=name)
#df=data.copy()
#df=df.replace({'WIN':1,'LOSE':2})
#df['len']=1
#df.drop(df[df['result']=='UNKNOWN'].index,
#        inplace=True)
#ward_rate=df[['wardPlaced','result','len']]
#ward_rate=ward_rate[ward_rate['wardPlaced']<40]
#ward_rate=ward_rate.sort_values(by='wardPlaced')

#ward_win=ward_rate.groupby(['wardPlaced'],as_index=False)['len'].sum()
#ward_rate['result']=pd.to_numeric(ward_rate['result'])
#ward_game=ward_rate.groupby(['wardPlaced'],as_index=False)['result'].sum()

#ward_win=pd.merge(ward_win,ward_game,on=['wardPlaced'])
#ward_win['win_rate']=ward_win['result']/ward_win['len']

#fig, ax=plt.subplots(figsize=(12,8))
#sns.barplot(data=ward_win, x='wardPlaced',
#            y='win_rate').set_ylim(0.3,0.6)
#ax.axhline(0.5,ls="--",lw=5,color='pink')
#ax.set_xlabel('wardPlaced')
#ax.set_ylabel('win_rate')
##데이터시각화##
#data=data[data['result']!='UNKNOWN']
#not_sup=data[data['position']!='S']
#sup=data[data['position']=='S']
#plt.figure(figsize=(20,10))
#for x,y,z in zip([212,222,221],[data,not_sup,sup],['ALL Position','Except Sup','Sup']):
#    wardPlaced =y['wardPlaced'].value_counts()
#    ward_win=[]
#    for i in wardPlaced[wardPlaced>50].index:
#        print('1')
#        win = y.value_counts(['wardPlaced','result'])[i]['WIN']
#        lose = y.value_counts(['wardPlaced','result'])[i]['LOSE']
#        win_rate = win/(win+lose)
#        ward_win.append({'wardPlaced': i , 'win_rate' : win_rate})
#    ward_win = pd.DataFrame(ward_win)    
#plt.subplot(x)
#sns.barplot(data = ward_win[ward_win['wardPlaced'] < 40], x = 'wardPlaced' , y = 'win_rate').set_ylim(0.3,0.6)
#plt.axhline(0.5, ls = '--', lw = 3, color = 'pink')
#plt.title(z, weight = 'bold')
