{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_covid=pd.read_csv('COVID19.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['ID', 'age', 'sex', 'city', 'province', 'country',\n",
       "       'wuhan(0)_not_wuhan(1)', 'latitude', 'longitude', 'geo_resolution',\n",
       "       'date_onset_symptoms', 'date_admission_hospital', 'date_confirmation',\n",
       "       'symptoms', 'lives_in_Wuhan', 'travel_history_dates',\n",
       "       'travel_history_location', 'reported_market_exposure',\n",
       "       'additional_information', 'chronic_disease_binary', 'chronic_disease',\n",
       "       'source', 'sequence_available', 'outcome', 'date_death_or_discharge',\n",
       "       'notes_for_discussion', 'location', 'admin3', 'admin2', 'admin1',\n",
       "       'country_new', 'admin_id', 'data_moderator_initials'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_covid.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_covid2 = df_covid[['age','sex','symptoms','country','date_onset_symptoms','travel_history_location','chronic_disease_binary','chronic_disease','outcome']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>age</th>\n",
       "      <th>sex</th>\n",
       "      <th>symptoms</th>\n",
       "      <th>country</th>\n",
       "      <th>date_onset_symptoms</th>\n",
       "      <th>travel_history_location</th>\n",
       "      <th>chronic_disease_binary</th>\n",
       "      <th>chronic_disease</th>\n",
       "      <th>outcome</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>30</td>\n",
       "      <td>male</td>\n",
       "      <td>NaN</td>\n",
       "      <td>China</td>\n",
       "      <td>18.01.2020</td>\n",
       "      <td>Wuhan</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>47</td>\n",
       "      <td>male</td>\n",
       "      <td>NaN</td>\n",
       "      <td>China</td>\n",
       "      <td>10.01.2020</td>\n",
       "      <td>Luzhou Hunan, via Wuhan</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>49</td>\n",
       "      <td>male</td>\n",
       "      <td>NaN</td>\n",
       "      <td>China</td>\n",
       "      <td>15.01.2020</td>\n",
       "      <td>Yinzhou Hunan, via Wuhan</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>47</td>\n",
       "      <td>female</td>\n",
       "      <td>NaN</td>\n",
       "      <td>China</td>\n",
       "      <td>17.01.2020</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>50</td>\n",
       "      <td>female</td>\n",
       "      <td>NaN</td>\n",
       "      <td>China</td>\n",
       "      <td>10.01.2020</td>\n",
       "      <td>Wuhan</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  age     sex symptoms country date_onset_symptoms   travel_history_location  \\\n",
       "0  30    male      NaN   China          18.01.2020                     Wuhan   \n",
       "1  47    male      NaN   China          10.01.2020   Luzhou Hunan, via Wuhan   \n",
       "2  49    male      NaN   China          15.01.2020  Yinzhou Hunan, via Wuhan   \n",
       "3  47  female      NaN   China          17.01.2020                       NaN   \n",
       "4  50  female      NaN   China          10.01.2020                     Wuhan   \n",
       "\n",
       "   chronic_disease_binary chronic_disease outcome  \n",
       "0                     NaN             NaN     NaN  \n",
       "1                     NaN             NaN     NaN  \n",
       "2                     NaN             NaN     NaN  \n",
       "3                     NaN             NaN     NaN  \n",
       "4                     NaN             NaN     NaN  "
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_covid2.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "age                        True\n",
       "sex                        True\n",
       "symptoms                   True\n",
       "country                    True\n",
       "date_onset_symptoms        True\n",
       "travel_history_location    True\n",
       "chronic_disease_binary     True\n",
       "chronic_disease            True\n",
       "outcome                    True\n",
       "dtype: bool"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    " df_covid2.isnull().any()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "age                        11825\n",
       "sex                        11910\n",
       "symptoms                   12681\n",
       "country                       26\n",
       "date_onset_symptoms        12428\n",
       "travel_history_location    12416\n",
       "chronic_disease_binary     13156\n",
       "chronic_disease            13161\n",
       "outcome                    12990\n",
       "dtype: int64"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_covid2.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(13174, 33)"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_covid.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "del df_covid2['chronic_disease']\n",
    "del df_covid2['chronic_disease_binary']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "# del df_covid2['travel_history_dates']\n",
    "del df_covid2['date_onset_symptoms']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "df_covid2=df_covid2.reset_index(drop=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>age</th>\n",
       "      <th>sex</th>\n",
       "      <th>symptoms</th>\n",
       "      <th>country</th>\n",
       "      <th>travel_history_location</th>\n",
       "      <th>outcome</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>30</td>\n",
       "      <td>male</td>\n",
       "      <td>NaN</td>\n",
       "      <td>China</td>\n",
       "      <td>Wuhan</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>47</td>\n",
       "      <td>male</td>\n",
       "      <td>NaN</td>\n",
       "      <td>China</td>\n",
       "      <td>Luzhou Hunan, via Wuhan</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>49</td>\n",
       "      <td>male</td>\n",
       "      <td>NaN</td>\n",
       "      <td>China</td>\n",
       "      <td>Yinzhou Hunan, via Wuhan</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>47</td>\n",
       "      <td>female</td>\n",
       "      <td>NaN</td>\n",
       "      <td>China</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>50</td>\n",
       "      <td>female</td>\n",
       "      <td>NaN</td>\n",
       "      <td>China</td>\n",
       "      <td>Wuhan</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  age     sex symptoms country   travel_history_location outcome\n",
       "0  30    male      NaN   China                     Wuhan     NaN\n",
       "1  47    male      NaN   China   Luzhou Hunan, via Wuhan     NaN\n",
       "2  49    male      NaN   China  Yinzhou Hunan, via Wuhan     NaN\n",
       "3  47  female      NaN   China                       NaN     NaN\n",
       "4  50  female      NaN   China                     Wuhan     NaN"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_covid2.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_covid2.outcome=1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>age</th>\n",
       "      <th>sex</th>\n",
       "      <th>symptoms</th>\n",
       "      <th>country</th>\n",
       "      <th>travel_history_location</th>\n",
       "      <th>outcome</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>30</td>\n",
       "      <td>male</td>\n",
       "      <td>NaN</td>\n",
       "      <td>China</td>\n",
       "      <td>Wuhan</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>47</td>\n",
       "      <td>male</td>\n",
       "      <td>NaN</td>\n",
       "      <td>China</td>\n",
       "      <td>Luzhou Hunan, via Wuhan</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>49</td>\n",
       "      <td>male</td>\n",
       "      <td>NaN</td>\n",
       "      <td>China</td>\n",
       "      <td>Yinzhou Hunan, via Wuhan</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>47</td>\n",
       "      <td>female</td>\n",
       "      <td>NaN</td>\n",
       "      <td>China</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>50</td>\n",
       "      <td>female</td>\n",
       "      <td>NaN</td>\n",
       "      <td>China</td>\n",
       "      <td>Wuhan</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  age     sex symptoms country   travel_history_location  outcome\n",
       "0  30    male      NaN   China                     Wuhan        1\n",
       "1  47    male      NaN   China   Luzhou Hunan, via Wuhan        1\n",
       "2  49    male      NaN   China  Yinzhou Hunan, via Wuhan        1\n",
       "3  47  female      NaN   China                       NaN        1\n",
       "4  50  female      NaN   China                     Wuhan        1"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_covid2.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_covid2 = df_covid2.dropna(how ='any') df_covid2.isnull().sum()\n",
    "df_covid2=df_covid2.reset_index(drop=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(260, 6)"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_covid2.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['China', 'France', 'Japan', 'Malaysia', 'Nepal', 'Singapore',\n",
       "       'South Korea', 'Thailand', 'United States', 'Cambodia', 'Vietnam',\n",
       "       'Philippines', 'Italy', 'Lebanon', 'Spain', 'Lithuania'],\n",
       "      dtype=object)"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_covid2.country.unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "arr_0=['China','France','South Korea', 'United States', 'Italy', 'Spain']\n",
    "arr_1=['Japan', 'Malaysia', 'Nepal', 'Singapore', 'Thailand', 'Cambodia', 'Vietnam','Philippines', 'Lebanon', 'Lithuania']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['Wuhan', 'Ezhou City, Hubei', 'Thailand', 'Changsha', 'Hubei',\n",
       "       'Hangzhou', 'Rushan City', 'Xiaogan', 'Macheng', 'Xiangtan',\n",
       "       'Wuhan via Shanghai', 'Singapore',\n",
       "       'from Wuhan , traveled to Johor from Singapore', 'Hong Kong',\n",
       "       'Xianyang City',\n",
       "       'Went to Thailand; had dinner with firedns prior to trip',\n",
       "       'Beijing, Zhuzhou, Hunan, and Chengdu, Sichuan',\n",
       "       'Wuhan via Hong Kong', 'Wuhan via Qingdao',\n",
       "       'Osaka to Tokyo; on tour bus for chinese tourists', 'Yokohama',\n",
       "       'Guangzhou', 'Taizhou, Jiangsu', \"Wuhan via Xi'an\",\n",
       "       'Yichang City, Hubei', 'Ziyang County, Ankang', 'Malaysia', 'no',\n",
       "       'Xiangyang, Hubei', 'Baodi district department store in Tianjin',\n",
       "       'Wuhan City, Hubei Province', 'Zhengzhou Henan', 'Beijing',\n",
       "       'Vietnam', 'Wuhan - Hefei - Lujiang', 'Luzhou', 'Wuhan to Xuanwei',\n",
       "       'Xiaogan City, Huber province', 'Hawaii, USA',\n",
       "       'Shiyan City, Hubei; Qingyuan County, Guangdong',\n",
       "       'Shapingba District, Chongqing City', 'Yinchuan',\n",
       "       'Jiangxi, Guangzhou', 'Dongguan City, Guangdong Province',\n",
       "       'Guizhou, China', 'Aichi Prefecture', 'Wuhan, China',\n",
       "       'Macau, mainland China', 'Qom, Iran', 'Sapporo', 'Indonesia',\n",
       "       'Wuhan; Nanning', 'Yichang City, Hubei Province', 'Chengdu',\n",
       "       'Italy', 'Japan', 'Verona, Italy', '#192', '#193',\n",
       "       '#194 return to home after disembarking the cruise ship Diamond Princess',\n",
       "       '#195/Hokkaido 55', '#196/Hokkaido 56', '#197/Hokkaido 57',\n",
       "       '#198/Hokkaido 58', '#199/Hokkaido 59', '#200/Hokkaido 60',\n",
       "       '#201/Hokkaido 61', '#202/Hokkaido 62', '#203/Hokkaido 63',\n",
       "       '#205/Hokkaido 65', '#206/Hokkaido 66', '#207', '#208'],\n",
       "      dtype=object)"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_covid2.travel_history_location.unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "# df_covid2.to_csv('4152020modified')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [],
   "source": [
    "# df_modified1=pd.read_csv('modified.csv', encoding = \"ISO-8859-1\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_modified1=df_covid2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_modified1=df_modified1.reset_index(drop=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>age</th>\n",
       "      <th>sex</th>\n",
       "      <th>symptoms</th>\n",
       "      <th>country</th>\n",
       "      <th>travel_history_location</th>\n",
       "      <th>outcome</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>42</td>\n",
       "      <td>female</td>\n",
       "      <td>fever</td>\n",
       "      <td>China</td>\n",
       "      <td>Wuhan</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>59</td>\n",
       "      <td>female</td>\n",
       "      <td>fever</td>\n",
       "      <td>China</td>\n",
       "      <td>Wuhan</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>38</td>\n",
       "      <td>female</td>\n",
       "      <td>cough</td>\n",
       "      <td>China</td>\n",
       "      <td>Wuhan</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>45</td>\n",
       "      <td>male</td>\n",
       "      <td>fever</td>\n",
       "      <td>China</td>\n",
       "      <td>Wuhan</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>33</td>\n",
       "      <td>female</td>\n",
       "      <td>fever</td>\n",
       "      <td>China</td>\n",
       "      <td>Wuhan</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  age     sex symptoms country travel_history_location  outcome\n",
       "0  42  female    fever   China                   Wuhan        1\n",
       "1  59  female    fever   China                   Wuhan        1\n",
       "2  38  female    cough   China                   Wuhan        1\n",
       "3  45    male    fever   China                   Wuhan        1\n",
       "4  33  female    fever   China                   Wuhan        1"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_modified1.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\dell\\Anaconda3\\lib\\site-packages\\ipykernel_launcher.py:4: SettingWithCopyWarning: \n",
      "A value is trying to be set on a copy of a slice from a DataFrame\n",
      "\n",
      "See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy\n",
      "  after removing the cwd from sys.path.\n",
      "C:\\Users\\dell\\Anaconda3\\lib\\site-packages\\ipykernel_launcher.py:8: SettingWithCopyWarning: \n",
      "A value is trying to be set on a copy of a slice from a DataFrame\n",
      "\n",
      "See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy\n",
      "  \n"
     ]
    }
   ],
   "source": [
    "for i in range(len(df_modified1)):\n",
    "    for j in range(len(arr_0)):\n",
    "        if df_modified1['country'][i]==arr_0[j]:\n",
    "            df_modified1['country'][i]=1\n",
    "            break\n",
    "    for j in range(len(arr_1)):\n",
    "        if df_modified1['country'][i]==arr_1[j]:\n",
    "            df_modified1['country'][i]=0\n",
    "            break\n",
    "    \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>age</th>\n",
       "      <th>sex</th>\n",
       "      <th>symptoms</th>\n",
       "      <th>country</th>\n",
       "      <th>travel_history_location</th>\n",
       "      <th>outcome</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>42</td>\n",
       "      <td>female</td>\n",
       "      <td>fever</td>\n",
       "      <td>1</td>\n",
       "      <td>Wuhan</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>59</td>\n",
       "      <td>female</td>\n",
       "      <td>fever</td>\n",
       "      <td>1</td>\n",
       "      <td>Wuhan</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>38</td>\n",
       "      <td>female</td>\n",
       "      <td>cough</td>\n",
       "      <td>1</td>\n",
       "      <td>Wuhan</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>45</td>\n",
       "      <td>male</td>\n",
       "      <td>fever</td>\n",
       "      <td>1</td>\n",
       "      <td>Wuhan</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>33</td>\n",
       "      <td>female</td>\n",
       "      <td>fever</td>\n",
       "      <td>1</td>\n",
       "      <td>Wuhan</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  age     sex symptoms country travel_history_location  outcome\n",
       "0  42  female    fever       1                   Wuhan        1\n",
       "1  59  female    fever       1                   Wuhan        1\n",
       "2  38  female    cough       1                   Wuhan        1\n",
       "3  45    male    fever       1                   Wuhan        1\n",
       "4  33  female    fever       1                   Wuhan        1"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_modified1.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_modified1.symptoms=1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\dell\\Anaconda3\\lib\\site-packages\\ipykernel_launcher.py:5: SettingWithCopyWarning: \n",
      "A value is trying to be set on a copy of a slice from a DataFrame\n",
      "\n",
      "See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy\n",
      "  \"\"\"\n",
      "C:\\Users\\dell\\Anaconda3\\lib\\site-packages\\ipykernel_launcher.py:3: SettingWithCopyWarning: \n",
      "A value is trying to be set on a copy of a slice from a DataFrame\n",
      "\n",
      "See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy\n",
      "  This is separate from the ipykernel package so we can avoid doing imports until\n"
     ]
    }
   ],
   "source": [
    "for i in range(len(df_modified1)):\n",
    "    if df_modified1['travel_history_location'][i]=='no':\n",
    "        df_modified1['travel_history_location'][i]=0\n",
    "    else:\n",
    "        df_modified1['travel_history_location'][i]=1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\dell\\Anaconda3\\lib\\site-packages\\ipykernel_launcher.py:5: SettingWithCopyWarning: \n",
      "A value is trying to be set on a copy of a slice from a DataFrame\n",
      "\n",
      "See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy\n",
      "  \"\"\"\n",
      "C:\\Users\\dell\\Anaconda3\\lib\\site-packages\\ipykernel_launcher.py:3: SettingWithCopyWarning: \n",
      "A value is trying to be set on a copy of a slice from a DataFrame\n",
      "\n",
      "See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy\n",
      "  This is separate from the ipykernel package so we can avoid doing imports until\n"
     ]
    }
   ],
   "source": [
    "for i in range(len(df_modified1)):\n",
    "    if df_modified1['sex'][i]=='male':\n",
    "        df_modified1['sex'][i]=0\n",
    "    else:\n",
    "        df_modified1['sex'][i]=1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [],
   "source": [
    "# del df_modified1['city']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 'dis' in df_modified1['outcome'][0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>age</th>\n",
       "      <th>sex</th>\n",
       "      <th>symptoms</th>\n",
       "      <th>country</th>\n",
       "      <th>travel_history_location</th>\n",
       "      <th>outcome</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>42</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>59</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>38</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>45</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>33</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  age sex  symptoms country travel_history_location  outcome\n",
       "0  42   1         1       1                       1        1\n",
       "1  59   1         1       1                       1        1\n",
       "2  38   1         1       1                       1        1\n",
       "3  45   0         1       1                       1        1\n",
       "4  33   1         1       1                       1        1"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_modified1.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# df_covid2.travel_history_location.unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "# df_modified1.to_csv('4152020modified2correction')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_modified1=pd.read_csv('covid19latest.csv', encoding = \"ISO-8859-1\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>age</th>\n",
       "      <th>sex</th>\n",
       "      <th>symptoms</th>\n",
       "      <th>country</th>\n",
       "      <th>travel_history_location</th>\n",
       "      <th>outcome</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>42.0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>59.0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>38.0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>45.0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>33.0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    age  sex  symptoms  country  travel_history_location  outcome\n",
       "0  42.0    1         1        1                        1        1\n",
       "1  59.0    1         1        1                        1        1\n",
       "2  38.0    1         1        1                        1        1\n",
       "3  45.0    0         1        1                        1        1\n",
       "4  33.0    1         1        1                        1        1"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_modified1.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(2, 0.8735294117647059, 1.0)"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import statistics \n",
    "len(df_modified1.travel_history_location.unique()), statistics.mean(df_modified1.travel_history_location),statistics.median(df_modified1.travel_history_location)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([1, 0], dtype=int64)"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_modified1.sex.unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_train=df_modified1[['age','sex','country','travel_history_location','symptoms']]\n",
    "df_test=df_modified1[['outcome']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\dell\\Anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py:578: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  y = column_or_1d(y, warn=True)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.9411764705882353\n"
     ]
    }
   ],
   "source": [
    "from sklearn.model_selection import train_test_split\n",
    "for i in range(1):\n",
    "    x, x_test, y, y_test = train_test_split(df_train,df_test,test_size=0.2,train_size=0.8)\n",
    "    y=y.astype('int')\n",
    "    clf = LogisticRegression().fit(x, y)\n",
    "    y_test=y_test.astype('int')\n",
    "    clf.fit(x,y)\n",
    "    print(clf.score(x_test, y_test))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "# df_train"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\dell\\Anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py:578: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  y = column_or_1d(y, warn=True)\n"
     ]
    }
   ],
   "source": [
    "from sklearn.linear_model import LogisticRegression\n",
    "x, x_test, y, y_test = train_test_split(df_train,df_test,test_size=0.2,train_size=0.8)\n",
    "# y=y.astype('int')\n",
    "y=y.astype('int')\n",
    "clf = LogisticRegression(random_state=0).fit(x, y)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\dell\\Anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py:578: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  y = column_or_1d(y, warn=True)\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True,\n",
       "          intercept_scaling=1, max_iter=100, multi_class='ovr', n_jobs=1,\n",
       "          penalty='l2', random_state=0, solver='liblinear', tol=0.0001,\n",
       "          verbose=0, warm_start=False)"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y_test=y_test.astype('int')\n",
    "clf.fit(x,y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.9117647058823529"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "clf.score(x_test, y_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "# x_test"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1,\n",
       "       1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1,\n",
       "       1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1,\n",
       "       1, 1])"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y_pred=clf.predict(x_test)\n",
    "y_pred"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[16  6]\n",
      " [ 0 46]]\n"
     ]
    }
   ],
   "source": [
    "y_pred=clf.predict(x_test)\n",
    "from sklearn.metrics import confusion_matrix\n",
    "cm = confusion_matrix(y_test, y_pred)\n",
    "print(cm)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.9264705882352942"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "63/68"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[-0.0134039 ,  0.46081516,  0.56151164,  2.30330724,  2.79536314]])"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# df_train=df_modified1[['age','sex','country','travel_history_location','symptoms']]\n",
    "clf.coef_"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([-2.88362995])"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "clf.intercept_"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 360x360 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "from sklearn.metrics import confusion_matrix\n",
    "cm = confusion_matrix(y_test, y_pred)\n",
    "f, ax = plt.subplots(figsize=(5,5))\n",
    "sns.heatmap(cm,fmt=\".0f\", annot=True,linewidths=0.2, linecolor=\"purple\", ax=ax)\n",
    "plt.xlabel(\"Predicted\")\n",
    "plt.ylabel(\"Grand Truth\")\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# decision tree"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DecisionTreeRegressor(criterion='mse', max_depth=None, max_features=None,\n",
       "           max_leaf_nodes=None, min_impurity_decrease=0.0,\n",
       "           min_impurity_split=None, min_samples_leaf=1,\n",
       "           min_samples_split=2, min_weight_fraction_leaf=0.0,\n",
       "           presort=False, random_state=3, splitter='best')"
      ]
     },
     "execution_count": 55,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.tree import DecisionTreeRegressor  \n",
    "regressor = DecisionTreeRegressor(random_state = 3)  \n",
    "regressor.fit(x, y) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.metrics import accuracy_score\n",
    "# accuracy_score(regressor.predict(x_test),y_test)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Gaussian"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.naive_bayes import GaussianNB"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.9264705882352942\n",
      "0.9264705882352942\n",
      "0.9117647058823529\n",
      "0.9264705882352942\n",
      "0.9117647058823529\n",
      "0.9558823529411765\n",
      "0.9411764705882353\n",
      "0.9264705882352942\n",
      "0.9558823529411765\n",
      "0.9264705882352942\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\dell\\Anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py:578: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  y = column_or_1d(y, warn=True)\n"
     ]
    }
   ],
   "source": [
    "for i in range(1):\n",
    "    x, x_test, y, y_test = train_test_split(df_train,df_test,test_size=0.2,train_size=0.8)\n",
    "    gnb.fit(x,y)\n",
    "    GaussianNB(priors=None)\n",
    "    print(gnb.score(x_test,y_test))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [],
   "source": [
    "  x, x_test, y, y_test = train_test_split(df_train,df_test,test_size=0.2,train_size=0.8)\n",
    "gnb = GaussianNB()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\dell\\Anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py:578: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  y = column_or_1d(y, warn=True)\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "GaussianNB(priors=None)"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "gnb.fit(x,y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "GaussianNB(priors=None)"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "GaussianNB(priors=None)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.8970588235294118"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "gnb.score(x_test,y_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[15  7]\n",
      " [ 0 46]]\n"
     ]
    }
   ],
   "source": [
    "y_pred=clf.predict(x_test)\n",
    "from sklearn.metrics import confusion_matrix\n",
    "cm = confusion_matrix(y_test, y_pred)\n",
    "print(cm)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 360x360 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "from sklearn.metrics import confusion_matrix\n",
    "cm = confusion_matrix(y_test, y_pred)\n",
    "f, ax = plt.subplots(figsize=(5,5))\n",
    "sns.heatmap(cm,fmt=\".0f\", annot=True,linewidths=0.2, linecolor=\"purple\", ax=ax)\n",
    "plt.xlabel(\"Predicted\")\n",
    "plt.ylabel(\"Grand Truth\")\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# KNN"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np \n",
    "import pandas as pd \n",
    "from sklearn.model_selection import train_test_split \n",
    "from sklearn.neighbors import KNeighborsClassifier \n",
    "import matplotlib.pyplot as plt  \n",
    "import seaborn as sns "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.9222222222222223\n",
      "[[  2  14]\n",
      " [  0 164]]\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\dell\\Anaconda3\\lib\\site-packages\\ipykernel_launcher.py:3: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  This is separate from the ipykernel package so we can avoid doing imports until\n"
     ]
    }
   ],
   "source": [
    "x, x_test, y, y_test = train_test_split(df_train,df_test,test_size=0.2,train_size=0.8)\n",
    "clf = KNeighborsClassifier(n_neighbors = 3) \n",
    "clf.fit(x, y) \n",
    "training_score = clf.score(x, y) \n",
    "test_score = clf.score(x_test, y_test) \n",
    "print(test_score)\n",
    "y_pred=clf.predict(x_test)\n",
    "from sklearn.metrics import confusion_matrix\n",
    "cm = confusion_matrix(y_test, y_pred)\n",
    "print(cm)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\dell\\Anaconda3\\lib\\site-packages\\ipykernel_launcher.py:8: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  \n"
     ]
    }
   ],
   "source": [
    "K = [] \n",
    "training = [] \n",
    "test = [] \n",
    "scores = {} \n",
    "\n",
    "for k in range(2, 3): \n",
    "    clf = KNeighborsClassifier(n_neighbors = 5) \n",
    "    clf.fit(x, y) \n",
    "\n",
    "    training_score = clf.score(x, y) \n",
    "    test_score = clf.score(x_test, y_test) \n",
    "    K.append(k) \n",
    "\n",
    "    training.append(training_score) \n",
    "    test.append(test_score) \n",
    "    scores[k] = [training_score, test_score] \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2 : [0.9135285913528591, 0.9111111111111111]\n"
     ]
    }
   ],
   "source": [
    "for keys, values in scores.items(): \n",
    "    print(keys, ':', values) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\dell\\Anaconda3\\lib\\site-packages\\sklearn\\ensemble\\weight_boosting.py:29: DeprecationWarning: numpy.core.umath_tests is an internal NumPy module and should not be imported. It will be removed in a future NumPy release.\n",
      "  from numpy.core.umath_tests import inner1d\n",
      "C:\\Users\\dell\\Anaconda3\\lib\\site-packages\\ipykernel_launcher.py:11: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples,), for example using ravel().\n",
      "  # This is added back by InteractiveShellApp.init_path()\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.8823529411764706\n"
     ]
    }
   ],
   "source": [
    "from sklearn.ensemble import RandomForestClassifier\n",
    "from sklearn.metrics import accuracy_score\n",
    "# Create the model with 100 trees\n",
    "model = RandomForestClassifier(n_estimators=100, \n",
    "                               bootstrap = True,\n",
    "                               max_features = 'sqrt')\n",
    "# Fit on training data\n",
    "\n",
    "for i in range(1):\n",
    "    x, x_test, y, y_test = train_test_split(df_train,df_test,test_size=0.2,train_size=0.8)\n",
    "    model.fit(x, y)\n",
    "    print(accuracy_score(model.predict(x_test),y_test))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 11   9]\n",
      " [  1 159]]\n"
     ]
    }
   ],
   "source": [
    "y_pred=clf.predict(x_test)\n",
    "from sklearn.metrics import confusion_matrix\n",
    "cm = confusion_matrix(y_test, y_pred)\n",
    "print(cm)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "metadata": {},
   "outputs": [],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "# from sklearn import preprocessing\n",
    "# mm_scaler = preprocessing.MinMaxScaler()\n",
    "# X_train_minmax = mm_scaler.fit_transform(df_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x44f47fa908>"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 720x360 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize = (10,5))\n",
    "sns.heatmap(df_modified1.corr(), annot=True, linewidths=.1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\dell\\Anaconda3\\lib\\site-packages\\h5py\\__init__.py:36: FutureWarning: Conversion of the second argument of issubdtype from `float` to `np.floating` is deprecated. In future, it will be treated as `np.float64 == np.dtype(float).type`.\n",
      "  from ._conv import register_converters as _register_converters\n",
      "Using TensorFlow backend.\n"
     ]
    }
   ],
   "source": [
    "from keras import Sequential\n",
    "from keras.layers import Dense"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "WARNING:tensorflow:From C:\\Users\\dell\\Anaconda3\\lib\\site-packages\\tensorflow\\python\\framework\\op_def_library.py:263: colocate_with (from tensorflow.python.framework.ops) is deprecated and will be removed in a future version.\n",
      "Instructions for updating:\n",
      "Colocations handled automatically by placer.\n"
     ]
    }
   ],
   "source": [
    "classifier = Sequential()\n",
    "#First Hidden Layer\n",
    "classifier.add(Dense(5, activation='relu', kernel_initializer='random_normal', input_dim=5))\n",
    "#Second  Hidden Layer\n",
    "\n",
    "classifier.add(Dense(3, activation='relu', kernel_initializer='random_normal'))\n",
    "#Output Layer\n",
    "classifier.add(Dense(1, activation='sigmoid', kernel_initializer='random_normal'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "metadata": {},
   "outputs": [],
   "source": [
    "classifier.compile(optimizer ='adam',loss='binary_crossentropy', metrics =['accuracy'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "WARNING:tensorflow:From C:\\Users\\dell\\Anaconda3\\lib\\site-packages\\tensorflow\\python\\ops\\math_ops.py:3066: to_int32 (from tensorflow.python.ops.math_ops) is deprecated and will be removed in a future version.\n",
      "Instructions for updating:\n",
      "Use tf.cast instead.\n",
      "Epoch 1/300\n",
      "272/272 [==============================] - 2s 7ms/step - loss: 0.6896 - acc: 0.7132\n",
      "Epoch 2/300\n",
      "272/272 [==============================] - 0s 195us/step - loss: 0.6758 - acc: 0.7610\n",
      "Epoch 3/300\n",
      "272/272 [==============================] - 0s 188us/step - loss: 0.6449 - acc: 0.7610\n",
      "Epoch 4/300\n",
      "272/272 [==============================] - 0s 195us/step - loss: 0.5964 - acc: 0.7610\n",
      "Epoch 5/300\n",
      "272/272 [==============================] - 0s 239us/step - loss: 0.5669 - acc: 0.7610\n",
      "Epoch 6/300\n",
      "272/272 [==============================] - 0s 217us/step - loss: 0.5631 - acc: 0.7610\n",
      "Epoch 7/300\n",
      "272/272 [==============================] - 0s 213us/step - loss: 0.5599 - acc: 0.7610\n",
      "Epoch 8/300\n",
      "272/272 [==============================] - 0s 210us/step - loss: 0.5584 - acc: 0.7610\n",
      "Epoch 9/300\n",
      "272/272 [==============================] - 0s 202us/step - loss: 0.5578 - acc: 0.7610\n",
      "Epoch 10/300\n",
      "272/272 [==============================] - 0s 246us/step - loss: 0.5573 - acc: 0.7610\n",
      "Epoch 11/300\n",
      "272/272 [==============================] - 0s 199us/step - loss: 0.5545 - acc: 0.7610\n",
      "Epoch 12/300\n",
      "272/272 [==============================] - 0s 195us/step - loss: 0.5565 - acc: 0.7610\n",
      "Epoch 13/300\n",
      "272/272 [==============================] - 0s 217us/step - loss: 0.5522 - acc: 0.7610\n",
      "Epoch 14/300\n",
      "272/272 [==============================] - 0s 235us/step - loss: 0.5517 - acc: 0.7610\n",
      "Epoch 15/300\n",
      "272/272 [==============================] - 0s 199us/step - loss: 0.5511 - acc: 0.7610\n",
      "Epoch 16/300\n",
      "272/272 [==============================] - 0s 191us/step - loss: 0.5499 - acc: 0.7610\n",
      "Epoch 17/300\n",
      "272/272 [==============================] - 0s 191us/step - loss: 0.5481 - acc: 0.7610\n",
      "Epoch 18/300\n",
      "272/272 [==============================] - 0s 232us/step - loss: 0.5462 - acc: 0.7610\n",
      "Epoch 19/300\n",
      "272/272 [==============================] - 0s 228us/step - loss: 0.5450 - acc: 0.7610\n",
      "Epoch 20/300\n",
      "272/272 [==============================] - 0s 217us/step - loss: 0.5435 - acc: 0.7610\n",
      "Epoch 21/300\n",
      "272/272 [==============================] - 0s 195us/step - loss: 0.5422 - acc: 0.7610\n",
      "Epoch 22/300\n",
      "272/272 [==============================] - 0s 221us/step - loss: 0.5406 - acc: 0.7610\n",
      "Epoch 23/300\n",
      "272/272 [==============================] - 0s 235us/step - loss: 0.5385 - acc: 0.7610\n",
      "Epoch 24/300\n",
      "272/272 [==============================] - 0s 202us/step - loss: 0.5369 - acc: 0.7610\n",
      "Epoch 25/300\n",
      "272/272 [==============================] - 0s 184us/step - loss: 0.5354 - acc: 0.7610\n",
      "Epoch 26/300\n",
      "272/272 [==============================] - 0s 188us/step - loss: 0.5341 - acc: 0.7610\n",
      "Epoch 27/300\n",
      "272/272 [==============================] - 0s 228us/step - loss: 0.5320 - acc: 0.7610\n",
      "Epoch 28/300\n",
      "272/272 [==============================] - 0s 184us/step - loss: 0.5285 - acc: 0.7610\n",
      "Epoch 29/300\n",
      "272/272 [==============================] - 0s 173us/step - loss: 0.5269 - acc: 0.7610\n",
      "Epoch 30/300\n",
      "272/272 [==============================] - 0s 177us/step - loss: 0.5228 - acc: 0.7610\n",
      "Epoch 31/300\n",
      "272/272 [==============================] - 0s 206us/step - loss: 0.5201 - acc: 0.7610\n",
      "Epoch 32/300\n",
      "272/272 [==============================] - 0s 184us/step - loss: 0.5169 - acc: 0.7610\n",
      "Epoch 33/300\n",
      "272/272 [==============================] - 0s 173us/step - loss: 0.5123 - acc: 0.7610\n",
      "Epoch 34/300\n",
      "272/272 [==============================] - 0s 173us/step - loss: 0.5084 - acc: 0.7610\n",
      "Epoch 35/300\n",
      "272/272 [==============================] - 0s 195us/step - loss: 0.5041 - acc: 0.7610\n",
      "Epoch 36/300\n",
      "272/272 [==============================] - 0s 184us/step - loss: 0.4984 - acc: 0.7610\n",
      "Epoch 37/300\n",
      "272/272 [==============================] - 0s 173us/step - loss: 0.4922 - acc: 0.7610\n",
      "Epoch 38/300\n",
      "272/272 [==============================] - 0s 177us/step - loss: 0.4868 - acc: 0.7610\n",
      "Epoch 39/300\n",
      "272/272 [==============================] - 0s 195us/step - loss: 0.4791 - acc: 0.7610\n",
      "Epoch 40/300\n",
      "272/272 [==============================] - 0s 195us/step - loss: 0.4713 - acc: 0.7610\n",
      "Epoch 41/300\n",
      "272/272 [==============================] - 0s 173us/step - loss: 0.4661 - acc: 0.7610\n",
      "Epoch 42/300\n",
      "272/272 [==============================] - 0s 173us/step - loss: 0.4583 - acc: 0.7610\n",
      "Epoch 43/300\n",
      "272/272 [==============================] - 0s 169us/step - loss: 0.4508 - acc: 0.7610\n",
      "Epoch 44/300\n",
      "272/272 [==============================] - 0s 221us/step - loss: 0.4450 - acc: 0.7610\n",
      "Epoch 45/300\n",
      "272/272 [==============================] - 0s 177us/step - loss: 0.4393 - acc: 0.7610\n",
      "Epoch 46/300\n",
      "272/272 [==============================] - 0s 180us/step - loss: 0.4327 - acc: 0.7610\n",
      "Epoch 47/300\n",
      "272/272 [==============================] - 0s 180us/step - loss: 0.4281 - acc: 0.7610\n",
      "Epoch 48/300\n",
      "272/272 [==============================] - 0s 217us/step - loss: 0.4227 - acc: 0.7610\n",
      "Epoch 49/300\n",
      "272/272 [==============================] - 0s 177us/step - loss: 0.4218 - acc: 0.7610\n",
      "Epoch 50/300\n",
      "272/272 [==============================] - 0s 184us/step - loss: 0.4155 - acc: 0.7610\n",
      "Epoch 51/300\n",
      "272/272 [==============================] - 0s 177us/step - loss: 0.4117 - acc: 0.7610\n",
      "Epoch 52/300\n",
      "272/272 [==============================] - 0s 213us/step - loss: 0.4100 - acc: 0.7610\n",
      "Epoch 53/300\n",
      "272/272 [==============================] - 0s 180us/step - loss: 0.4055 - acc: 0.7610\n",
      "Epoch 54/300\n",
      "272/272 [==============================] - 0s 173us/step - loss: 0.4055 - acc: 0.7610\n",
      "Epoch 55/300\n",
      "272/272 [==============================] - 0s 177us/step - loss: 0.4002 - acc: 0.7610\n",
      "Epoch 56/300\n",
      "272/272 [==============================] - 0s 213us/step - loss: 0.4003 - acc: 0.7610\n",
      "Epoch 57/300\n",
      "272/272 [==============================] - 0s 177us/step - loss: 0.3967 - acc: 0.7647\n",
      "Epoch 58/300\n",
      "272/272 [==============================] - 0s 177us/step - loss: 0.3934 - acc: 0.8346\n",
      "Epoch 59/300\n",
      "272/272 [==============================] - 0s 177us/step - loss: 0.3939 - acc: 0.8272\n",
      "Epoch 60/300\n",
      "272/272 [==============================] - 0s 206us/step - loss: 0.3915 - acc: 0.8603\n",
      "Epoch 61/300\n",
      "272/272 [==============================] - 0s 195us/step - loss: 0.3900 - acc: 0.8419\n",
      "Epoch 62/300\n",
      "272/272 [==============================] - 0s 177us/step - loss: 0.3871 - acc: 0.8566\n",
      "Epoch 63/300\n",
      "272/272 [==============================] - 0s 173us/step - loss: 0.3860 - acc: 0.8456\n",
      "Epoch 64/300\n",
      "272/272 [==============================] - 0s 173us/step - loss: 0.3837 - acc: 0.8603\n",
      "Epoch 65/300\n",
      "272/272 [==============================] - 0s 184us/step - loss: 0.3850 - acc: 0.8456\n",
      "Epoch 66/300\n",
      "272/272 [==============================] - 0s 210us/step - loss: 0.3865 - acc: 0.8750\n",
      "Epoch 67/300\n",
      "272/272 [==============================] - 0s 180us/step - loss: 0.3883 - acc: 0.8309\n",
      "Epoch 68/300\n",
      "272/272 [==============================] - 0s 188us/step - loss: 0.3799 - acc: 0.8529\n",
      "Epoch 69/300\n",
      "272/272 [==============================] - 0s 180us/step - loss: 0.3765 - acc: 0.8713\n",
      "Epoch 70/300\n",
      "272/272 [==============================] - 0s 188us/step - loss: 0.3753 - acc: 0.8676\n",
      "Epoch 71/300\n",
      "272/272 [==============================] - 0s 188us/step - loss: 0.3746 - acc: 0.8640\n",
      "Epoch 72/300\n",
      "272/272 [==============================] - 0s 184us/step - loss: 0.3719 - acc: 0.8603\n",
      "Epoch 73/300\n",
      "272/272 [==============================] - 0s 184us/step - loss: 0.3715 - acc: 0.8676\n",
      "Epoch 74/300\n",
      "272/272 [==============================] - 0s 180us/step - loss: 0.3738 - acc: 0.8419\n",
      "Epoch 75/300\n",
      "272/272 [==============================] - 0s 188us/step - loss: 0.3696 - acc: 0.8640\n",
      "Epoch 76/300\n",
      "272/272 [==============================] - 0s 184us/step - loss: 0.3669 - acc: 0.8750\n",
      "Epoch 77/300\n",
      "272/272 [==============================] - 0s 180us/step - loss: 0.3653 - acc: 0.8640\n",
      "Epoch 78/300\n",
      "272/272 [==============================] - 0s 184us/step - loss: 0.3636 - acc: 0.8787\n",
      "Epoch 79/300\n",
      "272/272 [==============================] - 0s 177us/step - loss: 0.3659 - acc: 0.8713\n",
      "Epoch 80/300\n",
      "272/272 [==============================] - 0s 184us/step - loss: 0.3631 - acc: 0.8603\n",
      "Epoch 81/300\n",
      "272/272 [==============================] - 0s 180us/step - loss: 0.3598 - acc: 0.8750\n",
      "Epoch 82/300\n",
      "272/272 [==============================] - 0s 180us/step - loss: 0.3582 - acc: 0.8750\n",
      "Epoch 83/300\n",
      "272/272 [==============================] - 0s 180us/step - loss: 0.3572 - acc: 0.8676\n",
      "Epoch 84/300\n",
      "272/272 [==============================] - 0s 188us/step - loss: 0.3563 - acc: 0.8676\n",
      "Epoch 85/300\n",
      "272/272 [==============================] - 0s 217us/step - loss: 0.3538 - acc: 0.8824\n",
      "Epoch 86/300\n",
      "272/272 [==============================] - 0s 180us/step - loss: 0.3537 - acc: 0.8713\n",
      "Epoch 87/300\n",
      "272/272 [==============================] - 0s 177us/step - loss: 0.3531 - acc: 0.8860\n",
      "Epoch 88/300\n",
      "272/272 [==============================] - 0s 188us/step - loss: 0.3500 - acc: 0.8824\n",
      "Epoch 89/300\n",
      "272/272 [==============================] - 0s 173us/step - loss: 0.3477 - acc: 0.8824\n",
      "Epoch 90/300\n",
      "272/272 [==============================] - 0s 184us/step - loss: 0.3467 - acc: 0.8750\n",
      "Epoch 91/300\n",
      "272/272 [==============================] - 0s 188us/step - loss: 0.3548 - acc: 0.8934\n",
      "Epoch 92/300\n",
      "272/272 [==============================] - 0s 173us/step - loss: 0.3443 - acc: 0.8750\n",
      "Epoch 93/300\n",
      "272/272 [==============================] - 0s 180us/step - loss: 0.3452 - acc: 0.8824\n",
      "Epoch 94/300\n",
      "272/272 [==============================] - 0s 188us/step - loss: 0.3427 - acc: 0.8787\n",
      "Epoch 95/300\n",
      "272/272 [==============================] - 0s 173us/step - loss: 0.3403 - acc: 0.8860\n",
      "Epoch 96/300\n",
      "272/272 [==============================] - 0s 180us/step - loss: 0.3439 - acc: 0.8934\n",
      "Epoch 97/300\n",
      "272/272 [==============================] - 0s 191us/step - loss: 0.3379 - acc: 0.8860\n",
      "Epoch 98/300\n",
      "272/272 [==============================] - 0s 177us/step - loss: 0.3365 - acc: 0.8897\n",
      "Epoch 99/300\n",
      "272/272 [==============================] - 0s 180us/step - loss: 0.3358 - acc: 0.8897\n",
      "Epoch 100/300\n",
      "272/272 [==============================] - 0s 184us/step - loss: 0.3361 - acc: 0.8860\n",
      "Epoch 101/300\n",
      "272/272 [==============================] - 0s 180us/step - loss: 0.3323 - acc: 0.8860\n",
      "Epoch 102/300\n",
      "272/272 [==============================] - 0s 180us/step - loss: 0.3317 - acc: 0.8897\n",
      "Epoch 103/300\n",
      "272/272 [==============================] - 0s 188us/step - loss: 0.3301 - acc: 0.8897\n",
      "Epoch 104/300\n",
      "272/272 [==============================] - 0s 184us/step - loss: 0.3297 - acc: 0.8824\n",
      "Epoch 105/300\n",
      "272/272 [==============================] - 0s 180us/step - loss: 0.3286 - acc: 0.8934\n",
      "Epoch 106/300\n",
      "272/272 [==============================] - 0s 188us/step - loss: 0.3258 - acc: 0.8897\n",
      "Epoch 107/300\n",
      "272/272 [==============================] - 0s 184us/step - loss: 0.3277 - acc: 0.9007\n",
      "Epoch 108/300\n",
      "272/272 [==============================] - 0s 180us/step - loss: 0.3244 - acc: 0.8860\n",
      "Epoch 109/300\n",
      "272/272 [==============================] - 0s 184us/step - loss: 0.3266 - acc: 0.8971\n",
      "Epoch 110/300\n",
      "272/272 [==============================] - 0s 177us/step - loss: 0.3234 - acc: 0.8860\n",
      "Epoch 111/300\n",
      "272/272 [==============================] - 0s 177us/step - loss: 0.3204 - acc: 0.8971\n",
      "Epoch 112/300\n",
      "272/272 [==============================] - 0s 180us/step - loss: 0.3242 - acc: 0.8860\n",
      "Epoch 113/300\n",
      "272/272 [==============================] - 0s 188us/step - loss: 0.3188 - acc: 0.8934\n",
      "Epoch 114/300\n",
      "272/272 [==============================] - 0s 180us/step - loss: 0.3185 - acc: 0.8971\n",
      "Epoch 115/300\n",
      "272/272 [==============================] - 0s 184us/step - loss: 0.3162 - acc: 0.9044\n",
      "Epoch 116/300\n",
      "272/272 [==============================] - 0s 191us/step - loss: 0.3153 - acc: 0.9007\n",
      "Epoch 117/300\n",
      "272/272 [==============================] - 0s 184us/step - loss: 0.3130 - acc: 0.8971\n",
      "Epoch 118/300\n",
      "272/272 [==============================] - 0s 188us/step - loss: 0.3145 - acc: 0.9044\n",
      "Epoch 119/300\n",
      "272/272 [==============================] - 0s 188us/step - loss: 0.3120 - acc: 0.8971\n",
      "Epoch 120/300\n",
      "272/272 [==============================] - 0s 180us/step - loss: 0.3102 - acc: 0.9044\n",
      "Epoch 121/300\n",
      "272/272 [==============================] - 0s 180us/step - loss: 0.3101 - acc: 0.9007\n",
      "Epoch 122/300\n",
      "272/272 [==============================] - 0s 191us/step - loss: 0.3116 - acc: 0.8934\n",
      "Epoch 123/300\n",
      "272/272 [==============================] - 0s 180us/step - loss: 0.3078 - acc: 0.9007\n",
      "Epoch 124/300\n",
      "272/272 [==============================] - 0s 180us/step - loss: 0.3092 - acc: 0.9044\n",
      "Epoch 125/300\n",
      "272/272 [==============================] - 0s 191us/step - loss: 0.3055 - acc: 0.9118\n",
      "Epoch 126/300\n",
      "272/272 [==============================] - 0s 188us/step - loss: 0.3049 - acc: 0.9154\n",
      "Epoch 127/300\n",
      "272/272 [==============================] - 0s 184us/step - loss: 0.3049 - acc: 0.9118\n",
      "Epoch 128/300\n",
      "272/272 [==============================] - 0s 187us/step - loss: 0.3014 - acc: 0.9081\n",
      "Epoch 129/300\n",
      "272/272 [==============================] - 0s 184us/step - loss: 0.3022 - acc: 0.9191\n",
      "Epoch 130/300\n",
      "272/272 [==============================] - 0s 184us/step - loss: 0.3002 - acc: 0.9044\n",
      "Epoch 131/300\n",
      "272/272 [==============================] - 0s 184us/step - loss: 0.2988 - acc: 0.9265\n",
      "Epoch 132/300\n",
      "272/272 [==============================] - 0s 188us/step - loss: 0.2994 - acc: 0.9118\n",
      "Epoch 133/300\n",
      "272/272 [==============================] - 0s 184us/step - loss: 0.2983 - acc: 0.9265\n",
      "Epoch 134/300\n",
      "272/272 [==============================] - 0s 184us/step - loss: 0.2953 - acc: 0.9154\n",
      "Epoch 135/300\n",
      "272/272 [==============================] - 0s 180us/step - loss: 0.2963 - acc: 0.9228\n",
      "Epoch 136/300\n",
      "272/272 [==============================] - 0s 180us/step - loss: 0.2936 - acc: 0.9301\n",
      "Epoch 137/300\n",
      "272/272 [==============================] - 0s 195us/step - loss: 0.2950 - acc: 0.9191\n",
      "Epoch 138/300\n",
      "272/272 [==============================] - 0s 188us/step - loss: 0.2925 - acc: 0.9228\n",
      "Epoch 139/300\n",
      "272/272 [==============================] - 0s 184us/step - loss: 0.2917 - acc: 0.9375\n",
      "Epoch 140/300\n",
      "272/272 [==============================] - 0s 184us/step - loss: 0.2895 - acc: 0.9265\n",
      "Epoch 141/300\n",
      "272/272 [==============================] - 0s 191us/step - loss: 0.2904 - acc: 0.9338\n",
      "Epoch 142/300\n",
      "272/272 [==============================] - 0s 177us/step - loss: 0.2904 - acc: 0.9301\n",
      "Epoch 143/300\n",
      "272/272 [==============================] - 0s 202us/step - loss: 0.2915 - acc: 0.9338\n",
      "Epoch 144/300\n",
      "272/272 [==============================] - 0s 184us/step - loss: 0.2856 - acc: 0.9375\n",
      "Epoch 145/300\n",
      "272/272 [==============================] - 0s 180us/step - loss: 0.2870 - acc: 0.9338\n",
      "Epoch 146/300\n",
      "272/272 [==============================] - 0s 180us/step - loss: 0.2850 - acc: 0.9338\n",
      "Epoch 147/300\n",
      "272/272 [==============================] - 0s 184us/step - loss: 0.2887 - acc: 0.9338\n",
      "Epoch 148/300\n",
      "272/272 [==============================] - 0s 180us/step - loss: 0.2896 - acc: 0.9338\n",
      "Epoch 149/300\n",
      "272/272 [==============================] - 0s 180us/step - loss: 0.2834 - acc: 0.9338\n",
      "Epoch 150/300\n",
      "272/272 [==============================] - 0s 177us/step - loss: 0.2819 - acc: 0.9375\n",
      "Epoch 151/300\n",
      "272/272 [==============================] - 0s 184us/step - loss: 0.2807 - acc: 0.9375\n",
      "Epoch 152/300\n",
      "272/272 [==============================] - 0s 188us/step - loss: 0.2815 - acc: 0.9338\n",
      "Epoch 153/300\n",
      "272/272 [==============================] - 0s 177us/step - loss: 0.2809 - acc: 0.9265\n",
      "Epoch 154/300\n",
      "272/272 [==============================] - 0s 184us/step - loss: 0.2798 - acc: 0.9375\n",
      "Epoch 155/300\n",
      "272/272 [==============================] - 0s 180us/step - loss: 0.2782 - acc: 0.9375\n",
      "Epoch 156/300\n",
      "272/272 [==============================] - 0s 177us/step - loss: 0.2783 - acc: 0.9338\n",
      "Epoch 157/300\n",
      "272/272 [==============================] - 0s 180us/step - loss: 0.2781 - acc: 0.9375\n",
      "Epoch 158/300\n",
      "272/272 [==============================] - 0s 184us/step - loss: 0.2756 - acc: 0.9375\n",
      "Epoch 159/300\n",
      "272/272 [==============================] - 0s 177us/step - loss: 0.2748 - acc: 0.9375\n",
      "Epoch 160/300\n",
      "272/272 [==============================] - 0s 180us/step - loss: 0.2744 - acc: 0.9375\n",
      "Epoch 161/300\n",
      "272/272 [==============================] - 0s 184us/step - loss: 0.2755 - acc: 0.9338\n",
      "Epoch 162/300\n",
      "272/272 [==============================] - 0s 184us/step - loss: 0.2717 - acc: 0.9375\n",
      "Epoch 163/300\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "272/272 [==============================] - 0s 188us/step - loss: 0.2714 - acc: 0.9375\n",
      "Epoch 164/300\n",
      "272/272 [==============================] - 0s 177us/step - loss: 0.2721 - acc: 0.9338\n",
      "Epoch 165/300\n",
      "272/272 [==============================] - 0s 184us/step - loss: 0.2750 - acc: 0.9301\n",
      "Epoch 166/300\n",
      "272/272 [==============================] - 0s 184us/step - loss: 0.2710 - acc: 0.9338\n",
      "Epoch 167/300\n",
      "272/272 [==============================] - 0s 184us/step - loss: 0.2689 - acc: 0.9338\n",
      "Epoch 168/300\n",
      "272/272 [==============================] - 0s 180us/step - loss: 0.2684 - acc: 0.9338\n",
      "Epoch 169/300\n",
      "272/272 [==============================] - 0s 180us/step - loss: 0.2676 - acc: 0.9338\n",
      "Epoch 170/300\n",
      "272/272 [==============================] - 0s 202us/step - loss: 0.2678 - acc: 0.9338\n",
      "Epoch 171/300\n",
      "272/272 [==============================] - 0s 180us/step - loss: 0.2659 - acc: 0.9338\n",
      "Epoch 172/300\n",
      "272/272 [==============================] - 0s 184us/step - loss: 0.2663 - acc: 0.9338\n",
      "Epoch 173/300\n",
      "272/272 [==============================] - 0s 177us/step - loss: 0.2637 - acc: 0.9338\n",
      "Epoch 174/300\n",
      "272/272 [==============================] - 0s 173us/step - loss: 0.2659 - acc: 0.9338\n",
      "Epoch 175/300\n",
      "272/272 [==============================] - 0s 180us/step - loss: 0.2614 - acc: 0.9338\n",
      "Epoch 176/300\n",
      "272/272 [==============================] - 0s 184us/step - loss: 0.2637 - acc: 0.9338\n",
      "Epoch 177/300\n",
      "272/272 [==============================] - 0s 180us/step - loss: 0.2641 - acc: 0.9338\n",
      "Epoch 178/300\n",
      "272/272 [==============================] - 0s 177us/step - loss: 0.2673 - acc: 0.9375\n",
      "Epoch 179/300\n",
      "272/272 [==============================] - 0s 184us/step - loss: 0.2620 - acc: 0.9338\n",
      "Epoch 180/300\n",
      "272/272 [==============================] - 0s 180us/step - loss: 0.2612 - acc: 0.9301\n",
      "Epoch 181/300\n",
      "272/272 [==============================] - 0s 180us/step - loss: 0.2600 - acc: 0.9338\n",
      "Epoch 182/300\n",
      "272/272 [==============================] - 0s 188us/step - loss: 0.2596 - acc: 0.9375\n",
      "Epoch 183/300\n",
      "272/272 [==============================] - 0s 177us/step - loss: 0.2599 - acc: 0.9338\n",
      "Epoch 184/300\n",
      "272/272 [==============================] - 0s 188us/step - loss: 0.2672 - acc: 0.9338\n",
      "Epoch 185/300\n",
      "272/272 [==============================] - 0s 177us/step - loss: 0.2573 - acc: 0.9338\n",
      "Epoch 186/300\n",
      "272/272 [==============================] - 0s 180us/step - loss: 0.2598 - acc: 0.9338\n",
      "Epoch 187/300\n",
      "272/272 [==============================] - ETA: 0s - loss: 0.1165 - acc: 1.000 - 0s 180us/step - loss: 0.2566 - acc: 0.9338\n",
      "Epoch 188/300\n",
      "272/272 [==============================] - 0s 180us/step - loss: 0.2567 - acc: 0.9338\n",
      "Epoch 189/300\n",
      "272/272 [==============================] - 0s 280us/step - loss: 0.2604 - acc: 0.9301\n",
      "Epoch 190/300\n",
      "272/272 [==============================] - 0s 184us/step - loss: 0.2633 - acc: 0.9375\n",
      "Epoch 191/300\n",
      "272/272 [==============================] - 0s 180us/step - loss: 0.2548 - acc: 0.9375\n",
      "Epoch 192/300\n",
      "272/272 [==============================] - 0s 184us/step - loss: 0.2557 - acc: 0.9375\n",
      "Epoch 193/300\n",
      "272/272 [==============================] - 0s 180us/step - loss: 0.2546 - acc: 0.9375\n",
      "Epoch 194/300\n",
      "272/272 [==============================] - 0s 210us/step - loss: 0.2537 - acc: 0.9375\n",
      "Epoch 195/300\n",
      "272/272 [==============================] - 0s 202us/step - loss: 0.2528 - acc: 0.9375\n",
      "Epoch 196/300\n",
      "272/272 [==============================] - 0s 184us/step - loss: 0.2531 - acc: 0.9375\n",
      "Epoch 197/300\n",
      "272/272 [==============================] - 0s 180us/step - loss: 0.2542 - acc: 0.9375\n",
      "Epoch 198/300\n",
      "272/272 [==============================] - 0s 180us/step - loss: 0.2533 - acc: 0.9375\n",
      "Epoch 199/300\n",
      "272/272 [==============================] - 0s 177us/step - loss: 0.2538 - acc: 0.9375\n",
      "Epoch 200/300\n",
      "272/272 [==============================] - 0s 184us/step - loss: 0.2519 - acc: 0.9375\n",
      "Epoch 201/300\n",
      "272/272 [==============================] - 0s 177us/step - loss: 0.2519 - acc: 0.9375\n",
      "Epoch 202/300\n",
      "272/272 [==============================] - 0s 184us/step - loss: 0.2516 - acc: 0.9375\n",
      "Epoch 203/300\n",
      "272/272 [==============================] - 0s 177us/step - loss: 0.2507 - acc: 0.9375\n",
      "Epoch 204/300\n",
      "272/272 [==============================] - 0s 184us/step - loss: 0.2522 - acc: 0.9375\n",
      "Epoch 205/300\n",
      "272/272 [==============================] - 0s 180us/step - loss: 0.2498 - acc: 0.9375\n",
      "Epoch 206/300\n",
      "272/272 [==============================] - 0s 184us/step - loss: 0.2515 - acc: 0.9375\n",
      "Epoch 207/300\n",
      "272/272 [==============================] - 0s 191us/step - loss: 0.2526 - acc: 0.9375\n",
      "Epoch 208/300\n",
      "272/272 [==============================] - 0s 177us/step - loss: 0.2625 - acc: 0.9375\n",
      "Epoch 209/300\n",
      "272/272 [==============================] - 0s 180us/step - loss: 0.2492 - acc: 0.9375\n",
      "Epoch 210/300\n",
      "272/272 [==============================] - 0s 177us/step - loss: 0.2481 - acc: 0.9375\n",
      "Epoch 211/300\n",
      "272/272 [==============================] - 0s 184us/step - loss: 0.2486 - acc: 0.9375\n",
      "Epoch 212/300\n",
      "272/272 [==============================] - 0s 184us/step - loss: 0.2463 - acc: 0.9375\n",
      "Epoch 213/300\n",
      "272/272 [==============================] - 0s 188us/step - loss: 0.2496 - acc: 0.9375\n",
      "Epoch 214/300\n",
      "272/272 [==============================] - 0s 184us/step - loss: 0.2458 - acc: 0.9375\n",
      "Epoch 215/300\n",
      "272/272 [==============================] - 0s 180us/step - loss: 0.2505 - acc: 0.9375\n",
      "Epoch 216/300\n",
      "272/272 [==============================] - 0s 184us/step - loss: 0.2464 - acc: 0.9375\n",
      "Epoch 217/300\n",
      "272/272 [==============================] - 0s 184us/step - loss: 0.2470 - acc: 0.9375\n",
      "Epoch 218/300\n",
      "272/272 [==============================] - 0s 180us/step - loss: 0.2464 - acc: 0.9375\n",
      "Epoch 219/300\n",
      "272/272 [==============================] - 0s 184us/step - loss: 0.2445 - acc: 0.9375\n",
      "Epoch 220/300\n",
      "272/272 [==============================] - 0s 191us/step - loss: 0.2451 - acc: 0.9375\n",
      "Epoch 221/300\n",
      "272/272 [==============================] - 0s 188us/step - loss: 0.2448 - acc: 0.9375\n",
      "Epoch 222/300\n",
      "272/272 [==============================] - 0s 232us/step - loss: 0.2444 - acc: 0.9375\n",
      "Epoch 223/300\n",
      "272/272 [==============================] - 0s 202us/step - loss: 0.2447 - acc: 0.9375\n",
      "Epoch 224/300\n",
      "272/272 [==============================] - 0s 191us/step - loss: 0.2457 - acc: 0.9375\n",
      "Epoch 225/300\n",
      "272/272 [==============================] - 0s 184us/step - loss: 0.2431 - acc: 0.9375\n",
      "Epoch 226/300\n",
      "272/272 [==============================] - 0s 166us/step - loss: 0.2470 - acc: 0.9375\n",
      "Epoch 227/300\n",
      "272/272 [==============================] - 0s 162us/step - loss: 0.2419 - acc: 0.9375\n",
      "Epoch 228/300\n",
      "272/272 [==============================] - 0s 162us/step - loss: 0.2437 - acc: 0.9375\n",
      "Epoch 229/300\n",
      "272/272 [==============================] - 0s 162us/step - loss: 0.2414 - acc: 0.9375\n",
      "Epoch 230/300\n",
      "272/272 [==============================] - 0s 162us/step - loss: 0.2435 - acc: 0.9375\n",
      "Epoch 231/300\n",
      "272/272 [==============================] - 0s 166us/step - loss: 0.2435 - acc: 0.9375\n",
      "Epoch 232/300\n",
      "272/272 [==============================] - 0s 169us/step - loss: 0.2443 - acc: 0.9375\n",
      "Epoch 233/300\n",
      "272/272 [==============================] - 0s 169us/step - loss: 0.2418 - acc: 0.9375\n",
      "Epoch 234/300\n",
      "272/272 [==============================] - 0s 173us/step - loss: 0.2449 - acc: 0.9375\n",
      "Epoch 235/300\n",
      "272/272 [==============================] - 0s 180us/step - loss: 0.2411 - acc: 0.9375\n",
      "Epoch 236/300\n",
      "272/272 [==============================] - 0s 143us/step - loss: 0.2415 - acc: 0.9375\n",
      "Epoch 237/300\n",
      "272/272 [==============================] - 0s 143us/step - loss: 0.2396 - acc: 0.9375\n",
      "Epoch 238/300\n",
      "272/272 [==============================] - 0s 162us/step - loss: 0.2400 - acc: 0.9375\n",
      "Epoch 239/300\n",
      "272/272 [==============================] - 0s 158us/step - loss: 0.2406 - acc: 0.9375\n",
      "Epoch 240/300\n",
      "272/272 [==============================] - 0s 162us/step - loss: 0.2421 - acc: 0.9375\n",
      "Epoch 241/300\n",
      "272/272 [==============================] - 0s 166us/step - loss: 0.2397 - acc: 0.9375\n",
      "Epoch 242/300\n",
      "272/272 [==============================] - 0s 177us/step - loss: 0.2391 - acc: 0.9375\n",
      "Epoch 243/300\n",
      "272/272 [==============================] - ETA: 0s - loss: 0.3328 - acc: 0.900 - 0s 166us/step - loss: 0.2397 - acc: 0.9375\n",
      "Epoch 244/300\n",
      "272/272 [==============================] - 0s 169us/step - loss: 0.2400 - acc: 0.9375\n",
      "Epoch 245/300\n",
      "272/272 [==============================] - 0s 162us/step - loss: 0.2383 - acc: 0.9375\n",
      "Epoch 246/300\n",
      "272/272 [==============================] - 0s 162us/step - loss: 0.2418 - acc: 0.9375\n",
      "Epoch 247/300\n",
      "272/272 [==============================] - 0s 199us/step - loss: 0.2434 - acc: 0.9375\n",
      "Epoch 248/300\n",
      "272/272 [==============================] - 0s 213us/step - loss: 0.2409 - acc: 0.9375\n",
      "Epoch 249/300\n",
      "272/272 [==============================] - 0s 206us/step - loss: 0.2399 - acc: 0.9375\n",
      "Epoch 250/300\n",
      "272/272 [==============================] - 0s 217us/step - loss: 0.2373 - acc: 0.9375\n",
      "Epoch 251/300\n",
      "272/272 [==============================] - 0s 195us/step - loss: 0.2416 - acc: 0.9375\n",
      "Epoch 252/300\n",
      "272/272 [==============================] - 0s 213us/step - loss: 0.2410 - acc: 0.9375\n",
      "Epoch 253/300\n",
      "272/272 [==============================] - 0s 188us/step - loss: 0.2418 - acc: 0.9375\n",
      "Epoch 254/300\n",
      "272/272 [==============================] - 0s 188us/step - loss: 0.2376 - acc: 0.9375\n",
      "Epoch 255/300\n",
      "272/272 [==============================] - 0s 188us/step - loss: 0.2367 - acc: 0.9375\n",
      "Epoch 256/300\n",
      "272/272 [==============================] - 0s 180us/step - loss: 0.2382 - acc: 0.9375\n",
      "Epoch 257/300\n",
      "272/272 [==============================] - 0s 188us/step - loss: 0.2357 - acc: 0.9375\n",
      "Epoch 258/300\n",
      "272/272 [==============================] - 0s 180us/step - loss: 0.2433 - acc: 0.9375\n",
      "Epoch 259/300\n",
      "272/272 [==============================] - 0s 199us/step - loss: 0.2453 - acc: 0.9375\n",
      "Epoch 260/300\n",
      "272/272 [==============================] - 0s 184us/step - loss: 0.2368 - acc: 0.9375\n",
      "Epoch 261/300\n",
      "272/272 [==============================] - 0s 188us/step - loss: 0.2374 - acc: 0.9375\n",
      "Epoch 262/300\n",
      "272/272 [==============================] - 0s 180us/step - loss: 0.2372 - acc: 0.9375\n",
      "Epoch 263/300\n",
      "272/272 [==============================] - 0s 180us/step - loss: 0.2360 - acc: 0.9375\n",
      "Epoch 264/300\n",
      "272/272 [==============================] - 0s 188us/step - loss: 0.2347 - acc: 0.9375\n",
      "Epoch 265/300\n",
      "272/272 [==============================] - 0s 180us/step - loss: 0.2360 - acc: 0.9375\n",
      "Epoch 266/300\n",
      "272/272 [==============================] - 0s 188us/step - loss: 0.2360 - acc: 0.9375\n",
      "Epoch 267/300\n",
      "272/272 [==============================] - 0s 180us/step - loss: 0.2381 - acc: 0.9375\n",
      "Epoch 268/300\n",
      "272/272 [==============================] - 0s 184us/step - loss: 0.2376 - acc: 0.9375\n",
      "Epoch 269/300\n",
      "272/272 [==============================] - 0s 188us/step - loss: 0.2349 - acc: 0.9375\n",
      "Epoch 270/300\n",
      "272/272 [==============================] - 0s 184us/step - loss: 0.2351 - acc: 0.9375\n",
      "Epoch 271/300\n",
      "272/272 [==============================] - 0s 188us/step - loss: 0.2365 - acc: 0.9375\n",
      "Epoch 272/300\n",
      "272/272 [==============================] - 0s 184us/step - loss: 0.2394 - acc: 0.9375\n",
      "Epoch 273/300\n",
      "272/272 [==============================] - 0s 184us/step - loss: 0.2618 - acc: 0.9375\n",
      "Epoch 274/300\n",
      "272/272 [==============================] - 0s 180us/step - loss: 0.2308 - acc: 0.9375\n",
      "Epoch 275/300\n",
      "272/272 [==============================] - 0s 188us/step - loss: 0.2354 - acc: 0.9375\n",
      "Epoch 276/300\n",
      "272/272 [==============================] - 0s 184us/step - loss: 0.2323 - acc: 0.9375\n",
      "Epoch 277/300\n",
      "272/272 [==============================] - 0s 180us/step - loss: 0.2338 - acc: 0.9375\n",
      "Epoch 278/300\n",
      "272/272 [==============================] - 0s 184us/step - loss: 0.2341 - acc: 0.9375\n",
      "Epoch 279/300\n",
      "272/272 [==============================] - 0s 184us/step - loss: 0.2338 - acc: 0.9375\n",
      "Epoch 280/300\n",
      "272/272 [==============================] - 0s 180us/step - loss: 0.2347 - acc: 0.9375\n",
      "Epoch 281/300\n",
      "272/272 [==============================] - 0s 188us/step - loss: 0.2319 - acc: 0.9375\n",
      "Epoch 282/300\n",
      "272/272 [==============================] - 0s 180us/step - loss: 0.2345 - acc: 0.9375\n",
      "Epoch 283/300\n",
      "272/272 [==============================] - 0s 188us/step - loss: 0.2356 - acc: 0.9375\n",
      "Epoch 284/300\n",
      "272/272 [==============================] - 0s 188us/step - loss: 0.2319 - acc: 0.9375\n",
      "Epoch 285/300\n",
      "272/272 [==============================] - 0s 180us/step - loss: 0.2330 - acc: 0.9375\n",
      "Epoch 286/300\n",
      "272/272 [==============================] - 0s 180us/step - loss: 0.2339 - acc: 0.9375\n",
      "Epoch 287/300\n",
      "272/272 [==============================] - 0s 199us/step - loss: 0.2339 - acc: 0.9375\n",
      "Epoch 288/300\n",
      "272/272 [==============================] - 0s 210us/step - loss: 0.2349 - acc: 0.9375\n",
      "Epoch 289/300\n",
      "272/272 [==============================] - 0s 235us/step - loss: 0.2354 - acc: 0.9375\n",
      "Epoch 290/300\n",
      "272/272 [==============================] - 0s 228us/step - loss: 0.2361 - acc: 0.9375\n",
      "Epoch 291/300\n",
      "272/272 [==============================] - 0s 202us/step - loss: 0.2312 - acc: 0.9375\n",
      "Epoch 292/300\n",
      "272/272 [==============================] - 0s 232us/step - loss: 0.2320 - acc: 0.9375\n",
      "Epoch 293/300\n",
      "272/272 [==============================] - 0s 232us/step - loss: 0.2310 - acc: 0.9375\n",
      "Epoch 294/300\n",
      "272/272 [==============================] - 0s 239us/step - loss: 0.2304 - acc: 0.9375\n",
      "Epoch 295/300\n",
      "272/272 [==============================] - 0s 228us/step - loss: 0.2315 - acc: 0.9375\n",
      "Epoch 296/300\n",
      "272/272 [==============================] - 0s 213us/step - loss: 0.2305 - acc: 0.9375\n",
      "Epoch 297/300\n",
      "272/272 [==============================] - 0s 195us/step - loss: 0.2298 - acc: 0.9375\n",
      "Epoch 298/300\n",
      "272/272 [==============================] - 0s 228us/step - loss: 0.2340 - acc: 0.9375\n",
      "Epoch 299/300\n",
      "272/272 [==============================] - 0s 239us/step - loss: 0.2364 - acc: 0.9375\n",
      "Epoch 300/300\n",
      "272/272 [==============================] - 0s 235us/step - loss: 0.2318 - acc: 0.9375\n",
      "272/272 [==============================] - 0s 699us/step\n",
      "[0.23026652108220494, 0.9375]\n"
     ]
    }
   ],
   "source": [
    "for i in range(1):\n",
    "    x, x_test, y, y_test = train_test_split(df_train,df_test,test_size=0.2,train_size=0.8)\n",
    "    classifier.compile(optimizer ='adam',loss='binary_crossentropy', metrics =['accuracy'])\n",
    "    classifier.fit(x,y, batch_size=10, epochs=300)\n",
    "    eval_model=classifier.evaluate(x, y)\n",
    "    print(eval_model)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "272/272 [==============================] - 0s 48us/step\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "[0.23026652108220494, 0.9375]"
      ]
     },
     "execution_count": 65,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "eval_model=classifier.evaluate(x, y)\n",
    "eval_model\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "9.308823529200001"
      ]
     },
     "execution_count": 66,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "0.9264705882+0.9264705882+0.9117647059+0.9264705882+0.9117647059+0.9558823529+0.9411764706+0.9264705882+0.9558823529+0.9264705882"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[10  5]\n",
      " [ 1 52]]\n"
     ]
    }
   ],
   "source": [
    "y_pred=classifier.predict(x_test)\n",
    "y_pred =(y_pred>0.5)\n",
    "from sklearn.metrics import confusion_matrix\n",
    "cm = confusion_matrix(y_test, y_pred)\n",
    "print(cm)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# part-2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_modified2=pd.read_csv('modified3.csv', encoding = \"ISO-8859-1\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>age</th>\n",
       "      <th>sex</th>\n",
       "      <th>country</th>\n",
       "      <th>travel_history_location</th>\n",
       "      <th>outcome</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>50.0</td>\n",
       "      <td>female</td>\n",
       "      <td>China</td>\n",
       "      <td>Wuhan</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>42.0</td>\n",
       "      <td>female</td>\n",
       "      <td>China</td>\n",
       "      <td>Wuhan</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>59.0</td>\n",
       "      <td>female</td>\n",
       "      <td>China</td>\n",
       "      <td>Wuhan</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>30.0</td>\n",
       "      <td>male</td>\n",
       "      <td>China</td>\n",
       "      <td>Wuhan</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>39.0</td>\n",
       "      <td>male</td>\n",
       "      <td>China</td>\n",
       "      <td>Wuhan</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    age     sex country travel_history_location  outcome\n",
       "0  50.0  female   China                   Wuhan        1\n",
       "1  42.0  female   China                   Wuhan        1\n",
       "2  59.0  female   China                   Wuhan        1\n",
       "3  30.0    male   China                   Wuhan        1\n",
       "4  39.0    male   China                   Wuhan        1"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_modified2.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 172,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['China', 'France', 'Japan', 'Malaysia', 'Nepal', 'Singapore',\n",
       "       'South Korea', 'Thailand', 'United States', 'Vietnam', 'Australia',\n",
       "       'Canada', 'Cambodia', 'Sri Lanka', 'Philippines', 'Sweden',\n",
       "       'Italy', 'Lebanon', 'United Arab Emirates', 'North Macedonia',\n",
       "       'Spain', 'Pakistan', 'Greece', 'Afghanistan', 'Germany', 'Brazil',\n",
       "       'Romania', 'Georgia', 'Croatia', 'Switzerland', 'Estonia',\n",
       "       'Lithuania', 'India'], dtype=object)"
      ]
     },
     "execution_count": 172,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_modified2['country'].unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 173,
   "metadata": {},
   "outputs": [],
   "source": [
    "arr0=['China', 'France', 'Japan', 'Malaysia','Singapore','South Korea', 'Thailand', 'United States', 'Australia','Canada','Philippines', 'Sweden','Italy','Spain', 'Pakistan', 'Germany', 'Brazil','Romania']\n",
    "arr1=['Vietnam','Sri Lanka','Lebanon','Greece', 'Afghanistan','India']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 174,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\dell\\Anaconda3\\lib\\site-packages\\ipykernel_launcher.py:4: SettingWithCopyWarning: \n",
      "A value is trying to be set on a copy of a slice from a DataFrame\n",
      "\n",
      "See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy\n",
      "  after removing the cwd from sys.path.\n",
      "C:\\Users\\dell\\Anaconda3\\lib\\site-packages\\ipykernel_launcher.py:8: SettingWithCopyWarning: \n",
      "A value is trying to be set on a copy of a slice from a DataFrame\n",
      "\n",
      "See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy\n",
      "  \n"
     ]
    }
   ],
   "source": [
    "for i in range(len(df_modified2)):\n",
    "    for j in range(len(arr0)):\n",
    "        if str(df_modified2['country'][i]) == str(arr0[j]):\n",
    "            df_modified2['country'][i]=1     \n",
    "    for j in range(len(arr1)):\n",
    "#         print(df_modified2['country'][i],str(arr_1[j]),str(df_modified2['country'][i]) == str(arr_1[j]))\n",
    "        if str(df_modified2['country'][i]) == str(arr1[j]):\n",
    "            df_modified2['country'][i]=0\n",
    "                "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 175,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\dell\\Anaconda3\\lib\\site-packages\\ipykernel_launcher.py:5: SettingWithCopyWarning: \n",
      "A value is trying to be set on a copy of a slice from a DataFrame\n",
      "\n",
      "See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy\n",
      "  \"\"\"\n",
      "C:\\Users\\dell\\Anaconda3\\lib\\site-packages\\ipykernel_launcher.py:3: SettingWithCopyWarning: \n",
      "A value is trying to be set on a copy of a slice from a DataFrame\n",
      "\n",
      "See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy\n",
      "  This is separate from the ipykernel package so we can avoid doing imports until\n",
      "C:\\Users\\dell\\Anaconda3\\lib\\site-packages\\ipykernel_launcher.py:10: SettingWithCopyWarning: \n",
      "A value is trying to be set on a copy of a slice from a DataFrame\n",
      "\n",
      "See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy\n",
      "  # Remove the CWD from sys.path while we load stuff.\n",
      "C:\\Users\\dell\\Anaconda3\\lib\\site-packages\\ipykernel_launcher.py:8: SettingWithCopyWarning: \n",
      "A value is trying to be set on a copy of a slice from a DataFrame\n",
      "\n",
      "See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy\n",
      "  \n"
     ]
    }
   ],
   "source": [
    "for i in range(len(df_modified2)):\n",
    "    if df_modified2['travel_history_location'][i]=='no':\n",
    "        df_modified2['travel_history_location'][i]=0\n",
    "    else:\n",
    "        df_modified2['travel_history_location'][i]=1\n",
    "for i in range(len(df_modified2)):\n",
    "    if df_modified2['sex'][i]=='male':\n",
    "        df_modified2['sex'][i]=0\n",
    "    else:\n",
    "        df_modified2['sex'][i]=1        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 178,
   "metadata": {},
   "outputs": [],
   "source": [
    "# for i in range(len(df_modified1)):\n",
    "#     if 'dis' in df_modified1['outcome'][i] or 'sta' in df_modified1['outcome'][i]:\n",
    "#         df_modified1['outcome'][i]=0\n",
    "#     else:\n",
    "#         df_modified1['outcome'][i]=1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 177,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\dell\\Anaconda3\\lib\\site-packages\\ipykernel_launcher.py:2: SettingWithCopyWarning: \n",
      "A value is trying to be set on a copy of a slice from a DataFrame\n",
      "\n",
      "See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy\n",
      "  \n"
     ]
    }
   ],
   "source": [
    "for i in range(len(df_modified1)):\n",
    "    df_modified1['outcome'][i]=1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 179,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_modified2.to_csv('coronafinal')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_modified2=pd.read_csv('Corona.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 143,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_train=df_modified2[['age','sex','travel_history_location','country']]\n",
    "df_test=df_modified2[['outcome']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 144,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split\n",
    "\n",
    "x, x_test, y, y_test = train_test_split(df_train,df_test,test_size=0.2,train_size=0.8,random_state=3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 145,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\dell\\Anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py:578: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  y = column_or_1d(y, warn=True)\n"
     ]
    }
   ],
   "source": [
    "from sklearn.linear_model import LogisticRegression\n",
    "y=y.astype('int')\n",
    "clf = LogisticRegression(random_state=2).fit(x, y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 146,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.9935483870967742"
      ]
     },
     "execution_count": 146,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "clf.score(x_test, y_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 147,
   "metadata": {},
   "outputs": [],
   "source": [
    "# from sklearn import preprocessing\n",
    "# mm_scaler = preprocessing.MinMaxScaler()\n",
    "# X_train_minmax = mm_scaler.fit_transform(df_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 148,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split\n",
    "\n",
    "x, x_test, y, y_test = train_test_split(df_train,df_test,test_size=0.2,train_size=0.8,random_state=3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 149,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\dell\\Anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py:578: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  y = column_or_1d(y, warn=True)\n"
     ]
    }
   ],
   "source": [
    "from sklearn.linear_model import LogisticRegression\n",
    "y=y.astype('int')\n",
    "clf = LogisticRegression(random_state=2).fit(x, y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 150,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.9935483870967742"
      ]
     },
     "execution_count": 150,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "clf.score(x_test, y_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 151,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 39   0]\n",
      " [  1 115]]\n"
     ]
    }
   ],
   "source": [
    "y_pred=clf.predict(x_test)\n",
    "from sklearn.metrics import confusion_matrix\n",
    "cm = confusion_matrix(y_test, y_pred)\n",
    "print(cm)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 155,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>age</th>\n",
       "      <th>sex</th>\n",
       "      <th>travel_history_location</th>\n",
       "      <th>country</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>50.0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>42.0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>59.0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>30.0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>39.0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>38.0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>45.0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>33.0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>37.0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>39.0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>32.0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>45.0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>45.0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>18.0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>56.0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15</th>\n",
       "      <td>42.0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>16</th>\n",
       "      <td>33.0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>17</th>\n",
       "      <td>44.0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18</th>\n",
       "      <td>65.0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19</th>\n",
       "      <td>21.0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>20</th>\n",
       "      <td>41.0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>21</th>\n",
       "      <td>44.0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>22</th>\n",
       "      <td>30.0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>23</th>\n",
       "      <td>43.0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>24</th>\n",
       "      <td>31.0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25</th>\n",
       "      <td>43.0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>26</th>\n",
       "      <td>24.0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>27</th>\n",
       "      <td>66.0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>28</th>\n",
       "      <td>65.0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>29</th>\n",
       "      <td>36.0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>741</th>\n",
       "      <td>26.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>742</th>\n",
       "      <td>28.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>743</th>\n",
       "      <td>34.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>744</th>\n",
       "      <td>55.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>745</th>\n",
       "      <td>35.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>746</th>\n",
       "      <td>55.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>747</th>\n",
       "      <td>30.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>748</th>\n",
       "      <td>45.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>749</th>\n",
       "      <td>45.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>750</th>\n",
       "      <td>38.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>751</th>\n",
       "      <td>39.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>752</th>\n",
       "      <td>45.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>753</th>\n",
       "      <td>25.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>754</th>\n",
       "      <td>65.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>755</th>\n",
       "      <td>85.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>756</th>\n",
       "      <td>5.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>757</th>\n",
       "      <td>85.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>758</th>\n",
       "      <td>65.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>759</th>\n",
       "      <td>65.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>760</th>\n",
       "      <td>65.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>761</th>\n",
       "      <td>65.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>762</th>\n",
       "      <td>45.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>763</th>\n",
       "      <td>75.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>764</th>\n",
       "      <td>65.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>765</th>\n",
       "      <td>65.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>766</th>\n",
       "      <td>65.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>767</th>\n",
       "      <td>55.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>768</th>\n",
       "      <td>65.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>769</th>\n",
       "      <td>45.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>770</th>\n",
       "      <td>5.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>771 rows × 4 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "      age  sex  travel_history_location  country\n",
       "0    50.0    1                        1        1\n",
       "1    42.0    1                        1        1\n",
       "2    59.0    1                        1        1\n",
       "3    30.0    0                        1        1\n",
       "4    39.0    0                        1        1\n",
       "5    38.0    1                        1        1\n",
       "6    45.0    0                        1        1\n",
       "7    33.0    1                        1        1\n",
       "8    37.0    0                        1        1\n",
       "9    39.0    0                        1        1\n",
       "10   32.0    1                        1        1\n",
       "11   45.0    0                        1        1\n",
       "12   45.0    0                        1        1\n",
       "13   18.0    1                        1        1\n",
       "14   56.0    1                        1        1\n",
       "15   42.0    0                        1        1\n",
       "16   33.0    1                        1        1\n",
       "17   44.0    0                        1        1\n",
       "18   65.0    0                        1        1\n",
       "19   21.0    0                        1        1\n",
       "20   41.0    0                        1        1\n",
       "21   44.0    1                        1        1\n",
       "22   30.0    1                        1        1\n",
       "23   43.0    1                        1        1\n",
       "24   31.0    0                        1        1\n",
       "25   43.0    0                        1        1\n",
       "26   24.0    0                        1        1\n",
       "27   66.0    0                        1        1\n",
       "28   65.0    1                        1        1\n",
       "29   36.0    0                        1        1\n",
       "..    ...  ...                      ...      ...\n",
       "741  26.0    0                        0        0\n",
       "742  28.0    0                        0        0\n",
       "743  34.0    0                        0        0\n",
       "744  55.0    0                        0        0\n",
       "745  35.0    0                        0        0\n",
       "746  55.0    0                        0        0\n",
       "747  30.0    1                        0        0\n",
       "748  45.0    0                        0        0\n",
       "749  45.0    0                        0        0\n",
       "750  38.0    1                        0        0\n",
       "751  39.0    1                        0        0\n",
       "752  45.0    1                        0        0\n",
       "753  25.0    0                        0        0\n",
       "754  65.0    0                        0        0\n",
       "755  85.0    1                        0        0\n",
       "756   5.0    0                        0        0\n",
       "757  85.0    0                        0        0\n",
       "758  65.0    1                        0        0\n",
       "759  65.0    0                        0        0\n",
       "760  65.0    0                        0        0\n",
       "761  65.0    1                        0        0\n",
       "762  45.0    0                        0        0\n",
       "763  75.0    0                        0        0\n",
       "764  65.0    1                        0        0\n",
       "765  65.0    1                        0        0\n",
       "766  65.0    0                        0        0\n",
       "767  55.0    0                        0        0\n",
       "768  65.0    0                        0        0\n",
       "769  45.0    1                        0        0\n",
       "770   5.0    1                        0        0\n",
       "\n",
       "[771 rows x 4 columns]"
      ]
     },
     "execution_count": 155,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# df_train=df_modified2[['age','sex','travel_history_location','country']]\n",
    "# clf.predict([25,1,1,1])\n",
    "df_train"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[-0.0203393 ,  0.10659857,  4.13074219,  4.18009311]])"
      ]
     },
     "execution_count": 63,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "clf.coef_"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([-2.27455974])"
      ]
     },
     "execution_count": 64,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "clf.intercept_"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 193,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "-2.67"
      ]
     },
     "execution_count": 193,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "(25*(-0.02))+0.10-2.27"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 195,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "15.43996919280288"
      ]
     },
     "execution_count": 195,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import math\n",
    "1/1+math.exp(2.67)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Heart Disease"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Features:\n",
    "\n",
    "- Age | Objective Feature | age | int (days)\n",
    "- | Objective Feature | height | int (cm) |\n",
    "- Weight | Objective Feature | weight | float (kg) |\n",
    "- Gender | Objective Feature | gender | categorical code |\n",
    "- Systolic blood pressure | Examination Feature | ap_hi | int |\n",
    "- Diastolic blood pressure | Examination Feature | ap_lo | int |\n",
    "- Cholesterol | Examination Feature | cholesterol | 1: normal, 2: above normal, 3: well above normal |\n",
    "- Glucose | Examination Feature | gluc | 1: normal, 2: above normal, 3: well above normal |\n",
    "- Smoking | Subjective Feature | smoke | binary |\n",
    "- Alcohol intake | Subjective Feature | alco | binary |\n",
    "- Physical activity | Subjective Feature | active | binary |\n",
    "- Presence or absence of cardiovascular disease | Target Variable | cardio | binary |"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "df_cardio=pd.read_csv('cardio_train.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>id</th>\n",
       "      <th>age</th>\n",
       "      <th>gender</th>\n",
       "      <th>height</th>\n",
       "      <th>weight</th>\n",
       "      <th>ap_hi</th>\n",
       "      <th>ap_lo</th>\n",
       "      <th>cholesterol</th>\n",
       "      <th>gluc</th>\n",
       "      <th>smoke</th>\n",
       "      <th>alco</th>\n",
       "      <th>active</th>\n",
       "      <th>cardio</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>18393</td>\n",
       "      <td>2</td>\n",
       "      <td>168</td>\n",
       "      <td>62.0</td>\n",
       "      <td>110</td>\n",
       "      <td>80</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>20228</td>\n",
       "      <td>1</td>\n",
       "      <td>156</td>\n",
       "      <td>85.0</td>\n",
       "      <td>140</td>\n",
       "      <td>90</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2</td>\n",
       "      <td>18857</td>\n",
       "      <td>1</td>\n",
       "      <td>165</td>\n",
       "      <td>64.0</td>\n",
       "      <td>130</td>\n",
       "      <td>70</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3</td>\n",
       "      <td>17623</td>\n",
       "      <td>2</td>\n",
       "      <td>169</td>\n",
       "      <td>82.0</td>\n",
       "      <td>150</td>\n",
       "      <td>100</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>4</td>\n",
       "      <td>17474</td>\n",
       "      <td>1</td>\n",
       "      <td>156</td>\n",
       "      <td>56.0</td>\n",
       "      <td>100</td>\n",
       "      <td>60</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   id    age  gender  height  weight  ap_hi  ap_lo  cholesterol  gluc  smoke  \\\n",
       "0   0  18393       2     168    62.0    110     80            1     1      0   \n",
       "1   1  20228       1     156    85.0    140     90            3     1      0   \n",
       "2   2  18857       1     165    64.0    130     70            3     1      0   \n",
       "3   3  17623       2     169    82.0    150    100            1     1      0   \n",
       "4   4  17474       1     156    56.0    100     60            1     1      0   \n",
       "\n",
       "   alco  active  cardio  \n",
       "0     0       1       0  \n",
       "1     0       1       1  \n",
       "2     0       0       1  \n",
       "3     0       1       1  \n",
       "4     0       0       0  "
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_cardio.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(70000, 13)"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_cardio.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_cardio['age']=df_cardio['age']/365"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>id</th>\n",
       "      <th>age</th>\n",
       "      <th>gender</th>\n",
       "      <th>height</th>\n",
       "      <th>weight</th>\n",
       "      <th>ap_hi</th>\n",
       "      <th>ap_lo</th>\n",
       "      <th>cholesterol</th>\n",
       "      <th>gluc</th>\n",
       "      <th>smoke</th>\n",
       "      <th>alco</th>\n",
       "      <th>active</th>\n",
       "      <th>cardio</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>50.391781</td>\n",
       "      <td>2</td>\n",
       "      <td>168</td>\n",
       "      <td>62.0</td>\n",
       "      <td>110</td>\n",
       "      <td>80</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>55.419178</td>\n",
       "      <td>1</td>\n",
       "      <td>156</td>\n",
       "      <td>85.0</td>\n",
       "      <td>140</td>\n",
       "      <td>90</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2</td>\n",
       "      <td>51.663014</td>\n",
       "      <td>1</td>\n",
       "      <td>165</td>\n",
       "      <td>64.0</td>\n",
       "      <td>130</td>\n",
       "      <td>70</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3</td>\n",
       "      <td>48.282192</td>\n",
       "      <td>2</td>\n",
       "      <td>169</td>\n",
       "      <td>82.0</td>\n",
       "      <td>150</td>\n",
       "      <td>100</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>4</td>\n",
       "      <td>47.873973</td>\n",
       "      <td>1</td>\n",
       "      <td>156</td>\n",
       "      <td>56.0</td>\n",
       "      <td>100</td>\n",
       "      <td>60</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   id        age  gender  height  weight  ap_hi  ap_lo  cholesterol  gluc  \\\n",
       "0   0  50.391781       2     168    62.0    110     80            1     1   \n",
       "1   1  55.419178       1     156    85.0    140     90            3     1   \n",
       "2   2  51.663014       1     165    64.0    130     70            3     1   \n",
       "3   3  48.282192       2     169    82.0    150    100            1     1   \n",
       "4   4  47.873973       1     156    56.0    100     60            1     1   \n",
       "\n",
       "   smoke  alco  active  cardio  \n",
       "0      0     0       1       0  \n",
       "1      0     0       1       1  \n",
       "2      0     0       0       1  \n",
       "3      0     0       1       1  \n",
       "4      0     0       0       0  "
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_cardio.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 70000 entries, 0 to 69999\n",
      "Data columns (total 13 columns):\n",
      "id             70000 non-null int64\n",
      "age            70000 non-null float64\n",
      "gender         70000 non-null int64\n",
      "height         70000 non-null int64\n",
      "weight         70000 non-null float64\n",
      "ap_hi          70000 non-null int64\n",
      "ap_lo          70000 non-null int64\n",
      "cholesterol    70000 non-null int64\n",
      "gluc           70000 non-null int64\n",
      "smoke          70000 non-null int64\n",
      "alco           70000 non-null int64\n",
      "active         70000 non-null int64\n",
      "cardio         70000 non-null int64\n",
      "dtypes: float64(2), int64(11)\n",
      "memory usage: 6.9 MB\n"
     ]
    }
   ],
   "source": [
    "df_cardio.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "id             0\n",
       "age            0\n",
       "gender         0\n",
       "height         0\n",
       "weight         0\n",
       "ap_hi          0\n",
       "ap_lo          0\n",
       "cholesterol    0\n",
       "gluc           0\n",
       "smoke          0\n",
       "alco           0\n",
       "active         0\n",
       "cardio         0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_cardio.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_train=df_cardio[['age','gender','height','weight','cholesterol','gluc','smoke','alco','ap_hi','ap_lo','active']]\n",
    "df_test=df_cardio[['cardio']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split\n",
    "\n",
    "x, x_test, y, y_test = train_test_split(df_train,df_test,test_size=0.2,train_size=0.8,random_state=4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\dell\\Anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py:578: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  y = column_or_1d(y, warn=True)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.7173571428571428\n",
      "0.7185\n",
      "0.7166428571428571\n",
      "0.7265714285714285\n",
      "0.7194285714285714\n",
      "0.7158571428571429\n",
      "0.7192142857142857\n",
      "0.7177142857142857\n",
      "0.7175714285714285\n",
      "0.7274285714285714\n"
     ]
    }
   ],
   "source": [
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.linear_model import LogisticRegression\n",
    "for i in range(10):\n",
    "    x, x_test, y, y_test = train_test_split(df_train,df_test,test_size=0.2,train_size=0.8)\n",
    "    y=y.astype('int')\n",
    "    clf = LogisticRegression().fit(x, y)\n",
    "    y_test=y_test.astype('int')\n",
    "    clf.fit(x,y)\n",
    "    print(clf.score(x_test, y_test))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.615\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\dell\\Anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py:578: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  y = column_or_1d(y, warn=True)\n"
     ]
    }
   ],
   "source": [
    "x, x_test, y, y_test = train_test_split(df_train,df_test,test_size=0.2,train_size=0.8)\n",
    "gnb.fit(x,y)\n",
    "GaussianNB(priors=None)\n",
    "print(gnb.score(x_test,y_test))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\dell\\Anaconda3\\lib\\site-packages\\ipykernel_launcher.py:8: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  \n",
      "C:\\Users\\dell\\Anaconda3\\lib\\site-packages\\ipykernel_launcher.py:8: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  \n",
      "C:\\Users\\dell\\Anaconda3\\lib\\site-packages\\ipykernel_launcher.py:8: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  \n",
      "C:\\Users\\dell\\Anaconda3\\lib\\site-packages\\ipykernel_launcher.py:8: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  \n",
      "C:\\Users\\dell\\Anaconda3\\lib\\site-packages\\ipykernel_launcher.py:8: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  \n"
     ]
    }
   ],
   "source": [
    "K = [] \n",
    "training = [] \n",
    "test = [] \n",
    "scores = {} \n",
    "\n",
    "for k in range(2, 7): \n",
    "    clf = KNeighborsClassifier(n_neighbors = k) \n",
    "    clf.fit(x, y) \n",
    "\n",
    "    training_score = clf.score(x, y) \n",
    "    test_score = clf.score(x_test, y_test) \n",
    "    K.append(k) \n",
    "\n",
    "    training.append(training_score) \n",
    "    test.append(test_score) \n",
    "    scores[k] = [training_score, test_score] "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{2: [0.813625, 0.6363571428571428],\n",
       " 3: [0.8154285714285714, 0.67],\n",
       " 4: [0.7782142857142857, 0.6764285714285714],\n",
       " 5: [0.7812142857142857, 0.688],\n",
       " 6: [0.7626785714285714, 0.6885]}"
      ]
     },
     "execution_count": 74,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "scores"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\dell\\Anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py:578: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  y = column_or_1d(y, warn=True)\n"
     ]
    }
   ],
   "source": [
    "from sklearn.linear_model import LogisticRegression\n",
    "y=y.astype('int')\n",
    "clf = LogisticRegression(random_state=2).fit(x, y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.7253571428571428"
      ]
     },
     "execution_count": 97,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "clf.score(x_test, y_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 5.21817879e-02,  2.52502569e-02, -8.62105610e-03,\n",
       "         1.48616203e-02,  5.11432118e-01, -1.12319184e-01,\n",
       "        -1.22601218e-01, -2.16692905e-01,  4.30816359e-02,\n",
       "         1.92828843e-04]])"
      ]
     },
     "execution_count": 98,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# df_train=df_cardio[['age','gender','height',\n",
    "#                     'weight','cholesterol','gluc',\n",
    "#                     'smoke','alco','ap_hi',\n",
    "#                     'ap_lo']]\n",
    "# df_test=df_cardio[['cardio']]\n",
    "clf.coef_"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 283,
   "metadata": {},
   "outputs": [],
   "source": [
    "# from sklearn import preprocessing\n",
    "# mm_scaler = preprocessing.MinMaxScaler()\n",
    "# X_train_minmax = mm_scaler.fit_transform(df_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split\n",
    "\n",
    "x, x_test, y, y_test = train_test_split(df_train,df_test,test_size=0.2,train_size=0.8,random_state=4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\dell\\Anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py:578: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  y = column_or_1d(y, warn=True)\n"
     ]
    }
   ],
   "source": [
    "from sklearn.linear_model import LogisticRegression\n",
    "y=y.astype('int')\n",
    "clf = LogisticRegression(random_state=2).fit(x, y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.7099285714285715"
      ]
     },
     "execution_count": 75,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "clf.score(x_test, y_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "metadata": {},
   "outputs": [],
   "source": [
    "# df_train=df_cardio[['age','gender','height','weight','cholesterol','gluc','smoke','alco','ap_hi','ap_lo']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 5.21817879e-02,  2.52502569e-02, -8.62105610e-03,\n",
       "         1.48616203e-02,  5.11432118e-01, -1.12319184e-01,\n",
       "        -1.22601218e-01, -2.16692905e-01,  4.30816359e-02,\n",
       "         1.92828843e-04]])"
      ]
     },
     "execution_count": 99,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "clf.coef_"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([-8.49171082])"
      ]
     },
     "execution_count": 100,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "clf.intercept_"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[5356 1611]\n",
      " [2234 4799]]\n"
     ]
    }
   ],
   "source": [
    "y_pred=clf.predict(x_test)\n",
    "from sklearn.metrics import confusion_matrix\n",
    "cm = confusion_matrix(y_test, y_pred)\n",
    "print(cm)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 280,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\dell\\Anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py:578: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  y = column_or_1d(y, warn=True)\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,\n",
       "  decision_function_shape='ovr', degree=3, gamma='auto', kernel='poly',\n",
       "  max_iter=-1, probability=False, random_state=None, shrinking=True,\n",
       "  tol=0.001, verbose=False)"
      ]
     },
     "execution_count": 280,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn import svm\n",
    "clf = svm.SVC(kernel='poly', degree=3)\n",
    "clf.fit(x, y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 281,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.6273571428571428"
      ]
     },
     "execution_count": 281,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "clf.score(x_test,y_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 164,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>cardio</th>\n",
       "      <th>features</th>\n",
       "      <th>value</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>age</td>\n",
       "      <td>-0.436058</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>age</td>\n",
       "      <td>0.307684</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1</td>\n",
       "      <td>age</td>\n",
       "      <td>-0.247995</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1</td>\n",
       "      <td>age</td>\n",
       "      <td>-0.748147</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0</td>\n",
       "      <td>age</td>\n",
       "      <td>-0.808538</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>0</td>\n",
       "      <td>age</td>\n",
       "      <td>0.991036</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>0</td>\n",
       "      <td>age</td>\n",
       "      <td>1.071692</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>1</td>\n",
       "      <td>age</td>\n",
       "      <td>1.262593</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>0</td>\n",
       "      <td>age</td>\n",
       "      <td>-0.729908</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>0</td>\n",
       "      <td>age</td>\n",
       "      <td>0.147992</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>0</td>\n",
       "      <td>age</td>\n",
       "      <td>1.240706</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>0</td>\n",
       "      <td>age</td>\n",
       "      <td>-0.265018</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>0</td>\n",
       "      <td>age</td>\n",
       "      <td>-1.895982</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>0</td>\n",
       "      <td>age</td>\n",
       "      <td>0.137860</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>0</td>\n",
       "      <td>age</td>\n",
       "      <td>-2.000958</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15</th>\n",
       "      <td>1</td>\n",
       "      <td>age</td>\n",
       "      <td>-1.089012</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>16</th>\n",
       "      <td>0</td>\n",
       "      <td>age</td>\n",
       "      <td>0.740554</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>17</th>\n",
       "      <td>0</td>\n",
       "      <td>age</td>\n",
       "      <td>-1.103197</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18</th>\n",
       "      <td>0</td>\n",
       "      <td>age</td>\n",
       "      <td>-0.805295</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19</th>\n",
       "      <td>0</td>\n",
       "      <td>age</td>\n",
       "      <td>0.926591</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>20</th>\n",
       "      <td>0</td>\n",
       "      <td>age</td>\n",
       "      <td>0.125295</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>21</th>\n",
       "      <td>0</td>\n",
       "      <td>age</td>\n",
       "      <td>0.787976</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>22</th>\n",
       "      <td>1</td>\n",
       "      <td>age</td>\n",
       "      <td>1.449846</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>23</th>\n",
       "      <td>0</td>\n",
       "      <td>age</td>\n",
       "      <td>1.583598</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>24</th>\n",
       "      <td>1</td>\n",
       "      <td>age</td>\n",
       "      <td>-1.159535</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25</th>\n",
       "      <td>0</td>\n",
       "      <td>age</td>\n",
       "      <td>-2.032977</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>26</th>\n",
       "      <td>0</td>\n",
       "      <td>age</td>\n",
       "      <td>0.036532</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>27</th>\n",
       "      <td>0</td>\n",
       "      <td>age</td>\n",
       "      <td>-0.560894</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>28</th>\n",
       "      <td>0</td>\n",
       "      <td>age</td>\n",
       "      <td>-1.983935</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>29</th>\n",
       "      <td>0</td>\n",
       "      <td>age</td>\n",
       "      <td>0.643686</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>559970</th>\n",
       "      <td>1</td>\n",
       "      <td>alco</td>\n",
       "      <td>4.194876</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>559971</th>\n",
       "      <td>0</td>\n",
       "      <td>alco</td>\n",
       "      <td>-0.238383</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>559972</th>\n",
       "      <td>1</td>\n",
       "      <td>alco</td>\n",
       "      <td>-0.238383</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>559973</th>\n",
       "      <td>0</td>\n",
       "      <td>alco</td>\n",
       "      <td>-0.238383</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>559974</th>\n",
       "      <td>0</td>\n",
       "      <td>alco</td>\n",
       "      <td>-0.238383</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>559975</th>\n",
       "      <td>1</td>\n",
       "      <td>alco</td>\n",
       "      <td>-0.238383</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>559976</th>\n",
       "      <td>0</td>\n",
       "      <td>alco</td>\n",
       "      <td>-0.238383</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>559977</th>\n",
       "      <td>0</td>\n",
       "      <td>alco</td>\n",
       "      <td>-0.238383</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>559978</th>\n",
       "      <td>1</td>\n",
       "      <td>alco</td>\n",
       "      <td>-0.238383</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>559979</th>\n",
       "      <td>1</td>\n",
       "      <td>alco</td>\n",
       "      <td>-0.238383</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>559980</th>\n",
       "      <td>0</td>\n",
       "      <td>alco</td>\n",
       "      <td>4.194876</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>559981</th>\n",
       "      <td>1</td>\n",
       "      <td>alco</td>\n",
       "      <td>-0.238383</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>559982</th>\n",
       "      <td>1</td>\n",
       "      <td>alco</td>\n",
       "      <td>-0.238383</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>559983</th>\n",
       "      <td>0</td>\n",
       "      <td>alco</td>\n",
       "      <td>-0.238383</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>559984</th>\n",
       "      <td>1</td>\n",
       "      <td>alco</td>\n",
       "      <td>-0.238383</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>559985</th>\n",
       "      <td>1</td>\n",
       "      <td>alco</td>\n",
       "      <td>4.194876</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>559986</th>\n",
       "      <td>0</td>\n",
       "      <td>alco</td>\n",
       "      <td>-0.238383</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>559987</th>\n",
       "      <td>0</td>\n",
       "      <td>alco</td>\n",
       "      <td>-0.238383</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>559988</th>\n",
       "      <td>0</td>\n",
       "      <td>alco</td>\n",
       "      <td>-0.238383</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>559989</th>\n",
       "      <td>1</td>\n",
       "      <td>alco</td>\n",
       "      <td>-0.238383</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>559990</th>\n",
       "      <td>1</td>\n",
       "      <td>alco</td>\n",
       "      <td>-0.238383</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>559991</th>\n",
       "      <td>0</td>\n",
       "      <td>alco</td>\n",
       "      <td>-0.238383</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>559992</th>\n",
       "      <td>1</td>\n",
       "      <td>alco</td>\n",
       "      <td>-0.238383</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>559993</th>\n",
       "      <td>1</td>\n",
       "      <td>alco</td>\n",
       "      <td>-0.238383</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>559994</th>\n",
       "      <td>1</td>\n",
       "      <td>alco</td>\n",
       "      <td>-0.238383</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>559995</th>\n",
       "      <td>0</td>\n",
       "      <td>alco</td>\n",
       "      <td>-0.238383</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>559996</th>\n",
       "      <td>1</td>\n",
       "      <td>alco</td>\n",
       "      <td>-0.238383</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>559997</th>\n",
       "      <td>1</td>\n",
       "      <td>alco</td>\n",
       "      <td>4.194876</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>559998</th>\n",
       "      <td>1</td>\n",
       "      <td>alco</td>\n",
       "      <td>-0.238383</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>559999</th>\n",
       "      <td>0</td>\n",
       "      <td>alco</td>\n",
       "      <td>-0.238383</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>560000 rows × 3 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "        cardio features     value\n",
       "0            0      age -0.436058\n",
       "1            1      age  0.307684\n",
       "2            1      age -0.247995\n",
       "3            1      age -0.748147\n",
       "4            0      age -0.808538\n",
       "5            0      age  0.991036\n",
       "6            0      age  1.071692\n",
       "7            1      age  1.262593\n",
       "8            0      age -0.729908\n",
       "9            0      age  0.147992\n",
       "10           0      age  1.240706\n",
       "11           0      age -0.265018\n",
       "12           0      age -1.895982\n",
       "13           0      age  0.137860\n",
       "14           0      age -2.000958\n",
       "15           1      age -1.089012\n",
       "16           0      age  0.740554\n",
       "17           0      age -1.103197\n",
       "18           0      age -0.805295\n",
       "19           0      age  0.926591\n",
       "20           0      age  0.125295\n",
       "21           0      age  0.787976\n",
       "22           1      age  1.449846\n",
       "23           0      age  1.583598\n",
       "24           1      age -1.159535\n",
       "25           0      age -2.032977\n",
       "26           0      age  0.036532\n",
       "27           0      age -0.560894\n",
       "28           0      age -1.983935\n",
       "29           0      age  0.643686\n",
       "...        ...      ...       ...\n",
       "559970       1     alco  4.194876\n",
       "559971       0     alco -0.238383\n",
       "559972       1     alco -0.238383\n",
       "559973       0     alco -0.238383\n",
       "559974       0     alco -0.238383\n",
       "559975       1     alco -0.238383\n",
       "559976       0     alco -0.238383\n",
       "559977       0     alco -0.238383\n",
       "559978       1     alco -0.238383\n",
       "559979       1     alco -0.238383\n",
       "559980       0     alco  4.194876\n",
       "559981       1     alco -0.238383\n",
       "559982       1     alco -0.238383\n",
       "559983       0     alco -0.238383\n",
       "559984       1     alco -0.238383\n",
       "559985       1     alco  4.194876\n",
       "559986       0     alco -0.238383\n",
       "559987       0     alco -0.238383\n",
       "559988       0     alco -0.238383\n",
       "559989       1     alco -0.238383\n",
       "559990       1     alco -0.238383\n",
       "559991       0     alco -0.238383\n",
       "559992       1     alco -0.238383\n",
       "559993       1     alco -0.238383\n",
       "559994       1     alco -0.238383\n",
       "559995       0     alco -0.238383\n",
       "559996       1     alco -0.238383\n",
       "559997       1     alco  4.194876\n",
       "559998       1     alco -0.238383\n",
       "559999       0     alco -0.238383\n",
       "\n",
       "[560000 rows x 3 columns]"
      ]
     },
     "execution_count": 164,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s_list =['age','gender','height','weight','cholesterol','gluc','smoke','alco']\n",
    "def standartization(df_cardio):\n",
    "    x_std = df_cardio.copy(deep=True)\n",
    "    for column in s_list:\n",
    "        x_std[column] = (x_std[column]-x_std[column].mean())/x_std[column].std()\n",
    "    return x_std \n",
    "x_std=standartization(df_cardio)\n",
    "x_std.head()\n",
    "x_melted = pd.melt(frame=x_std, id_vars=\"cardio\", value_vars=df_train, var_name=\"features\", value_name=\"value\", col_level=None)\n",
    "x_melted  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 165,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(array([0, 1, 2, 3, 4, 5, 6, 7]), <a list of 8 Text xticklabel objects>)"
      ]
     },
     "execution_count": 165,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 720x720 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(10,10))\n",
    "sns.boxplot(x=\"features\", y=\"value\", hue=\"cardio\", data=x_melted)\n",
    "plt.xticks(rotation=90)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {},
   "outputs": [],
   "source": [
    "y_true = y_test\n",
    "y_pred = clf.predict(x_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.metrics import confusion_matrix\n",
    "cm = confusion_matrix(y_true, y_pred)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 360x360 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "from sklearn.metrics import confusion_matrix\n",
    "cm = confusion_matrix(y_true, y_pred)\n",
    "f, ax = plt.subplots(figsize=(5,5))\n",
    "sns.heatmap(cm,fmt=\".0f\", annot=True,linewidths=0.2, linecolor=\"purple\", ax=ax)\n",
    "plt.xlabel(\"Predicted\")\n",
    "plt.ylabel(\"Grand Truth\")\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 167,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0xf696fdea20>"
      ]
     },
     "execution_count": 167,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 1152x360 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "out_filter = ((df_cardio[\"ap_hi\"]>200) | (df_cardio[\"ap_lo\"]>150) )\n",
    "df_cardio = df_cardio[~out_filter]\n",
    "plt.figure(figsize = (16,5))\n",
    "sns.heatmap(df_cardio.corr(), annot=True, linewidths=.1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\dell\\Anaconda3\\lib\\site-packages\\h5py\\__init__.py:36: FutureWarning: Conversion of the second argument of issubdtype from `float` to `np.floating` is deprecated. In future, it will be treated as `np.float64 == np.dtype(float).type`.\n",
      "  from ._conv import register_converters as _register_converters\n",
      "Using TensorFlow backend.\n"
     ]
    }
   ],
   "source": [
    "from keras import Sequential\n",
    "from keras.layers import Dense"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "metadata": {},
   "outputs": [],
   "source": [
    "classifier = Sequential()\n",
    "#First Hidden Layer\n",
    "classifier.add(Dense(5, activation='relu', kernel_initializer='random_normal', input_dim=11))\n",
    "#Second  Hidden Layer\n",
    "classifier.add(Dense(4, activation='relu', kernel_initializer='random_normal'))\n",
    "#Output Layer\n",
    "classifier.add(Dense(1, activation='sigmoid', kernel_initializer='random_normal'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "metadata": {},
   "outputs": [],
   "source": [
    "classifier.compile(optimizer ='adam',loss='binary_crossentropy', metrics =['accuracy'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "WARNING:tensorflow:From C:\\Users\\dell\\Anaconda3\\lib\\site-packages\\tensorflow\\python\\ops\\math_ops.py:3066: to_int32 (from tensorflow.python.ops.math_ops) is deprecated and will be removed in a future version.\n",
      "Instructions for updating:\n",
      "Use tf.cast instead.\n",
      "Epoch 1/100\n",
      "56000/56000 [==============================] - 11s 201us/step - loss: 0.6510 - acc: 0.6165\n",
      "Epoch 2/100\n",
      "56000/56000 [==============================] - 9s 166us/step - loss: 0.6312 - acc: 0.6434\n",
      "Epoch 3/100\n",
      "56000/56000 [==============================] - 9s 161us/step - loss: 0.6278 - acc: 0.6475\n",
      "Epoch 4/100\n",
      "56000/56000 [==============================] - 9s 166us/step - loss: 0.6262 - acc: 0.6494\n",
      "Epoch 5/100\n",
      "56000/56000 [==============================] - 9s 165us/step - loss: 0.6255 - acc: 0.6486\n",
      "Epoch 6/100\n",
      "56000/56000 [==============================] - 12s 206us/step - loss: 0.6246 - acc: 0.6511\n",
      "Epoch 7/100\n",
      "56000/56000 [==============================] - 11s 200us/step - loss: 0.6241 - acc: 0.6512\n",
      "Epoch 8/100\n",
      "56000/56000 [==============================] - 13s 228us/step - loss: 0.6232 - acc: 0.65160s - loss: 0.623\n",
      "Epoch 9/100\n",
      "56000/56000 [==============================] - 13s 228us/step - loss: 0.6227 - acc: 0.6503\n",
      "Epoch 10/100\n",
      "56000/56000 [==============================] - 13s 233us/step - loss: 0.6223 - acc: 0.6515\n",
      "Epoch 11/100\n",
      "56000/56000 [==============================] - 14s 254us/step - loss: 0.6216 - acc: 0.6533\n",
      "Epoch 12/100\n",
      "56000/56000 [==============================] - 15s 275us/step - loss: 0.6207 - acc: 0.6544\n",
      "Epoch 13/100\n",
      "56000/56000 [==============================] - 13s 237us/step - loss: 0.6197 - acc: 0.65602\n",
      "Epoch 14/100\n",
      "56000/56000 [==============================] - 13s 231us/step - loss: 0.6190 - acc: 0.6565\n",
      "Epoch 15/100\n",
      "56000/56000 [==============================] - 14s 249us/step - loss: 0.6182 - acc: 0.6583\n",
      "Epoch 16/100\n",
      "56000/56000 [==============================] - 15s 262us/step - loss: 0.6163 - acc: 0.65962s - lo - ETA: 1s - loss: 0.6167 - acc:\n",
      "Epoch 17/100\n",
      "56000/56000 [==============================] - 12s 216us/step - loss: 0.6144 - acc: 0.6619\n",
      "Epoch 18/100\n",
      "56000/56000 [==============================] - 12s 216us/step - loss: 0.6123 - acc: 0.6650\n",
      "Epoch 19/100\n",
      "56000/56000 [==============================] - 15s 264us/step - loss: 0.6096 - acc: 0.6676\n",
      "Epoch 20/100\n",
      "56000/56000 [==============================] - 12s 212us/step - loss: 0.6064 - acc: 0.6704\n",
      "Epoch 21/100\n",
      "56000/56000 [==============================] - 12s 211us/step - loss: 0.6027 - acc: 0.6767\n",
      "Epoch 22/100\n",
      "56000/56000 [==============================] - 16s 289us/step - loss: 0.5982 - acc: 0.6824\n",
      "Epoch 23/100\n",
      "56000/56000 [==============================] - 14s 248us/step - loss: 0.5924 - acc: 0.6886\n",
      "Epoch 24/100\n",
      "56000/56000 [==============================] - 15s 263us/step - loss: 0.5881 - acc: 0.6947\n",
      "Epoch 25/100\n",
      "56000/56000 [==============================] - 12s 209us/step - loss: 0.5848 - acc: 0.6984\n",
      "Epoch 26/100\n",
      "56000/56000 [==============================] - 12s 209us/step - loss: 0.5816 - acc: 0.7008\n",
      "Epoch 27/100\n",
      "56000/56000 [==============================] - 12s 206us/step - loss: 0.5805 - acc: 0.7041\n",
      "Epoch 28/100\n",
      "56000/56000 [==============================] - 13s 231us/step - loss: 0.5783 - acc: 0.7062\n",
      "Epoch 29/100\n",
      "56000/56000 [==============================] - 17s 305us/step - loss: 0.5788 - acc: 0.7056\n",
      "Epoch 30/100\n",
      "56000/56000 [==============================] - 13s 227us/step - loss: 0.5783 - acc: 0.7050\n",
      "Epoch 31/100\n",
      "56000/56000 [==============================] - 13s 235us/step - loss: 0.5770 - acc: 0.7075\n",
      "Epoch 32/100\n",
      "56000/56000 [==============================] - 15s 263us/step - loss: 0.5770 - acc: 0.7074\n",
      "Epoch 33/100\n",
      "56000/56000 [==============================] - 14s 256us/step - loss: 0.5761 - acc: 0.7085\n",
      "Epoch 34/100\n",
      "56000/56000 [==============================] - 16s 279us/step - loss: 0.5766 - acc: 0.7071\n",
      "Epoch 35/100\n",
      "56000/56000 [==============================] - 15s 266us/step - loss: 0.5760 - acc: 0.7077\n",
      "Epoch 36/100\n",
      "56000/56000 [==============================] - 16s 293us/step - loss: 0.5755 - acc: 0.7090A: 0s - loss: 0.5756 - ac\n",
      "Epoch 37/100\n",
      "56000/56000 [==============================] - 17s 295us/step - loss: 0.5755 - acc: 0.7090\n",
      "Epoch 38/100\n",
      "56000/56000 [==============================] - 15s 261us/step - loss: 0.5759 - acc: 0.7093\n",
      "Epoch 39/100\n",
      "56000/56000 [==============================] - 12s 214us/step - loss: 0.5747 - acc: 0.7097\n",
      "Epoch 40/100\n",
      "56000/56000 [==============================] - 12s 213us/step - loss: 0.5744 - acc: 0.7108\n",
      "Epoch 41/100\n",
      "56000/56000 [==============================] - 11s 205us/step - loss: 0.5750 - acc: 0.7072\n",
      "Epoch 42/100\n",
      "56000/56000 [==============================] - 11s 203us/step - loss: 0.5745 - acc: 0.7111\n",
      "Epoch 43/100\n",
      "56000/56000 [==============================] - 12s 214us/step - loss: 0.5739 - acc: 0.7120\n",
      "Epoch 44/100\n",
      "56000/56000 [==============================] - 16s 293us/step - loss: 0.5731 - acc: 0.7118\n",
      "Epoch 45/100\n",
      "56000/56000 [==============================] - 13s 230us/step - loss: 0.5724 - acc: 0.7121\n",
      "Epoch 46/100\n",
      "56000/56000 [==============================] - 13s 231us/step - loss: 0.5712 - acc: 0.7124\n",
      "Epoch 47/100\n",
      "56000/56000 [==============================] - 15s 273us/step - loss: 0.5708 - acc: 0.71310s - loss: \n",
      "Epoch 48/100\n",
      "56000/56000 [==============================] - 14s 255us/step - loss: 0.5706 - acc: 0.7107\n",
      "Epoch 49/100\n",
      "56000/56000 [==============================] - 14s 258us/step - loss: 0.5691 - acc: 0.7140\n",
      "Epoch 50/100\n",
      "56000/56000 [==============================] - 15s 273us/step - loss: 0.5683 - acc: 0.7127\n",
      "Epoch 51/100\n",
      "56000/56000 [==============================] - 15s 267us/step - loss: 0.5680 - acc: 0.7164\n",
      "Epoch 52/100\n",
      "56000/56000 [==============================] - 15s 270us/step - loss: 0.5671 - acc: 0.71423s - loss: 0. - ETA: 2s - loss: 0.5656 - acc: 0\n",
      "Epoch 53/100\n",
      "56000/56000 [==============================] - 16s 280us/step - loss: 0.5658 - acc: 0.7170\n",
      "Epoch 54/100\n",
      "56000/56000 [==============================] - 15s 263us/step - loss: 0.5658 - acc: 0.7158\n",
      "Epoch 55/100\n",
      "56000/56000 [==============================] - 14s 244us/step - loss: 0.5655 - acc: 0.7159\n",
      "Epoch 56/100\n",
      "56000/56000 [==============================] - 14s 251us/step - loss: 0.5650 - acc: 0.7158TA: 1s - loss\n",
      "Epoch 57/100\n",
      "56000/56000 [==============================] - 13s 233us/step - loss: 0.5641 - acc: 0.7172\n",
      "Epoch 58/100\n",
      "56000/56000 [==============================] - 13s 232us/step - loss: 0.5645 - acc: 0.7170\n",
      "Epoch 59/100\n",
      "56000/56000 [==============================] - 13s 236us/step - loss: 0.5643 - acc: 0.7178\n",
      "Epoch 60/100\n",
      "56000/56000 [==============================] - 14s 249us/step - loss: 0.5632 - acc: 0.7190\n",
      "Epoch 61/100\n",
      "56000/56000 [==============================] - 13s 234us/step - loss: 0.5634 - acc: 0.7191\n",
      "Epoch 62/100\n",
      "56000/56000 [==============================] - 13s 234us/step - loss: 0.5640 - acc: 0.7191\n",
      "Epoch 63/100\n",
      "56000/56000 [==============================] - 14s 251us/step - loss: 0.5647 - acc: 0.7183\n",
      "Epoch 64/100\n",
      "56000/56000 [==============================] - 14s 250us/step - loss: 0.5635 - acc: 0.7185\n",
      "Epoch 65/100\n",
      "56000/56000 [==============================] - 14s 248us/step - loss: 0.5643 - acc: 0.7184\n",
      "Epoch 66/100\n",
      "56000/56000 [==============================] - 14s 246us/step - loss: 0.5640 - acc: 0.7188\n",
      "Epoch 67/100\n",
      "56000/56000 [==============================] - 14s 248us/step - loss: 0.5635 - acc: 0.7191TA: 0s - loss: 0.5637\n",
      "Epoch 68/100\n",
      "56000/56000 [==============================] - 13s 233us/step - loss: 0.5636 - acc: 0.7180\n",
      "Epoch 69/100\n",
      "56000/56000 [==============================] - 13s 233us/step - loss: 0.5622 - acc: 0.7189\n",
      "Epoch 70/100\n",
      "56000/56000 [==============================] - 14s 256us/step - loss: 0.5624 - acc: 0.7191\n",
      "Epoch 71/100\n",
      "56000/56000 [==============================] - 13s 237us/step - loss: 0.5626 - acc: 0.7192\n",
      "Epoch 72/100\n",
      "56000/56000 [==============================] - 13s 232us/step - loss: 0.5625 - acc: 0.7186\n",
      "Epoch 73/100\n",
      "56000/56000 [==============================] - 13s 224us/step - loss: 0.5622 - acc: 0.7192\n",
      "Epoch 74/100\n",
      "56000/56000 [==============================] - 15s 267us/step - loss: 0.5624 - acc: 0.7190\n",
      "Epoch 75/100\n",
      "56000/56000 [==============================] - 13s 228us/step - loss: 0.5626 - acc: 0.7189ETA: 1s - loss: \n",
      "Epoch 76/100\n",
      "56000/56000 [==============================] - 13s 231us/step - loss: 0.5614 - acc: 0.7202\n",
      "Epoch 77/100\n",
      "56000/56000 [==============================] - 13s 238us/step - loss: 0.5613 - acc: 0.7195\n",
      "Epoch 78/100\n",
      "56000/56000 [==============================] - 14s 248us/step - loss: 0.5614 - acc: 0.7194\n",
      "Epoch 79/100\n",
      "56000/56000 [==============================] - 13s 236us/step - loss: 0.5604 - acc: 0.71981s - loss: 0.5607  - ETA: 1s - loss: 0.5605 - - ETA: 1s \n",
      "Epoch 80/100\n",
      "56000/56000 [==============================] - 13s 226us/step - loss: 0.5602 - acc: 0.7214\n",
      "Epoch 81/100\n",
      "56000/56000 [==============================] - 13s 233us/step - loss: 0.5597 - acc: 0.7211\n",
      "Epoch 82/100\n",
      "56000/56000 [==============================] - 13s 228us/step - loss: 0.5603 - acc: 0.7192\n",
      "Epoch 83/100\n",
      "56000/56000 [==============================] - 14s 259us/step - loss: 0.5607 - acc: 0.72030s - loss: 0.5606 - a\n",
      "Epoch 84/100\n",
      "56000/56000 [==============================] - 12s 218us/step - loss: 0.5596 - acc: 0.7207\n",
      "Epoch 85/100\n",
      "56000/56000 [==============================] - 13s 229us/step - loss: 0.5597 - acc: 0.7204\n",
      "Epoch 86/100\n",
      "56000/56000 [==============================] - 13s 229us/step - loss: 0.5602 - acc: 0.7213\n",
      "Epoch 87/100\n",
      "56000/56000 [==============================] - ETA: 0s - loss: 0.5602 - acc: 0.720 - 14s 253us/step - loss: 0.5602 - acc: 0.7207\n",
      "Epoch 88/100\n",
      "56000/56000 [==============================] - 14s 244us/step - loss: 0.5609 - acc: 0.7209\n",
      "Epoch 89/100\n",
      "56000/56000 [==============================] - 13s 229us/step - loss: 0.5597 - acc: 0.7203\n",
      "Epoch 90/100\n",
      "56000/56000 [==============================] - 13s 225us/step - loss: 0.5602 - acc: 0.7200\n",
      "Epoch 91/100\n",
      "56000/56000 [==============================] - 13s 229us/step - loss: 0.5605 - acc: 0.7193\n",
      "Epoch 92/100\n",
      "56000/56000 [==============================] - 14s 255us/step - loss: 0.5599 - acc: 0.72010s - loss:\n",
      "Epoch 93/100\n",
      "56000/56000 [==============================] - 13s 239us/step - loss: 0.5595 - acc: 0.7221\n",
      "Epoch 94/100\n",
      "56000/56000 [==============================] - 13s 229us/step - loss: 0.5597 - acc: 0.7204\n",
      "Epoch 95/100\n",
      "56000/56000 [==============================] - 13s 232us/step - loss: 0.5589 - acc: 0.7217\n",
      "Epoch 96/100\n",
      "56000/56000 [==============================] - 16s 281us/step - loss: 0.5606 - acc: 0.7192\n",
      "Epoch 97/100\n",
      "56000/56000 [==============================] - 12s 221us/step - loss: 0.5588 - acc: 0.7213\n",
      "Epoch 98/100\n",
      "56000/56000 [==============================] - 15s 262us/step - loss: 0.5590 - acc: 0.7212\n",
      "Epoch 99/100\n",
      "56000/56000 [==============================] - 13s 241us/step - loss: 0.5597 - acc: 0.7202\n",
      "Epoch 100/100\n",
      "56000/56000 [==============================] - 14s 250us/step - loss: 0.5591 - acc: 0.7222\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "<keras.callbacks.History at 0xf69b4520b8>"
      ]
     },
     "execution_count": 94,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "classifier.fit(x,y, batch_size=10, epochs=100)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "56000/56000 [==============================] - 1s 25us/step\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "[0.5656480377401625, 0.7119642857142857]"
      ]
     },
     "execution_count": 96,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "eval_model=classifier.evaluate(x, y)\n",
    "eval_model"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "metadata": {},
   "outputs": [],
   "source": [
    "# eval_model=classifier.evaluate(x, y)\n",
    "# eval_model\n",
    "y_pred=classifier.predict(x_test)\n",
    "y_pred =(y_pred>0.5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[5755 1227]\n",
      " [2788 4230]]\n"
     ]
    }
   ],
   "source": [
    "# eval_model=classifier.evaluate(x, y)\n",
    "# eval_model\n",
    "# y_pred=classifier.predict(x_test)\n",
    "# y_pred =(y_pred>0.5)\n",
    "from sklearn.metrics import confusion_matrix\n",
    "cm = confusion_matrix(y_test, y_pred)\n",
    "print(cm)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[<tf.Variable 'dense_4/kernel:0' shape=(11, 5) dtype=float32_ref>,\n",
       " <tf.Variable 'dense_4/bias:0' shape=(5,) dtype=float32_ref>,\n",
       " <tf.Variable 'dense_5/kernel:0' shape=(5, 4) dtype=float32_ref>,\n",
       " <tf.Variable 'dense_5/bias:0' shape=(4,) dtype=float32_ref>,\n",
       " <tf.Variable 'dense_6/kernel:0' shape=(4, 1) dtype=float32_ref>,\n",
       " <tf.Variable 'dense_6/bias:0' shape=(1,) dtype=float32_ref>]"
      ]
     },
     "execution_count": 101,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "classifier.c"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Diabetes/"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_diabetes=pd.read_csv('diabetes.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Pregnancies</th>\n",
       "      <th>Glucose</th>\n",
       "      <th>BloodPressure</th>\n",
       "      <th>SkinThickness</th>\n",
       "      <th>Insulin</th>\n",
       "      <th>BMI</th>\n",
       "      <th>DiabetesPedigreeFunction</th>\n",
       "      <th>Age</th>\n",
       "      <th>Outcome</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>6</td>\n",
       "      <td>148</td>\n",
       "      <td>72</td>\n",
       "      <td>35</td>\n",
       "      <td>0</td>\n",
       "      <td>33.6</td>\n",
       "      <td>0.63</td>\n",
       "      <td>50</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>85</td>\n",
       "      <td>66</td>\n",
       "      <td>29</td>\n",
       "      <td>0</td>\n",
       "      <td>26.6</td>\n",
       "      <td>0.35</td>\n",
       "      <td>31</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>8</td>\n",
       "      <td>183</td>\n",
       "      <td>64</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>23.3</td>\n",
       "      <td>0.67</td>\n",
       "      <td>32</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1</td>\n",
       "      <td>89</td>\n",
       "      <td>66</td>\n",
       "      <td>23</td>\n",
       "      <td>94</td>\n",
       "      <td>28.1</td>\n",
       "      <td>0.17</td>\n",
       "      <td>21</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0</td>\n",
       "      <td>137</td>\n",
       "      <td>40</td>\n",
       "      <td>35</td>\n",
       "      <td>168</td>\n",
       "      <td>43.1</td>\n",
       "      <td>2.29</td>\n",
       "      <td>33</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Pregnancies  Glucose  BloodPressure  SkinThickness  Insulin   BMI  \\\n",
       "0            6      148             72             35        0  33.6   \n",
       "1            1       85             66             29        0  26.6   \n",
       "2            8      183             64              0        0  23.3   \n",
       "3            1       89             66             23       94  28.1   \n",
       "4            0      137             40             35      168  43.1   \n",
       "\n",
       "   DiabetesPedigreeFunction  Age  Outcome  \n",
       "0                      0.63   50        1  \n",
       "1                      0.35   31        0  \n",
       "2                      0.67   32        1  \n",
       "3                      0.17   21        0  \n",
       "4                      2.29   33        1  "
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_diabetes.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(768, 9)"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_diabetes.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x315633e588>"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 1152x360 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "plt.figure(figsize = (16,5))\n",
    "sns.heatmap(df_diabetes.corr(), annot=True, linewidths=.1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_diabetes.columns\n",
    "out_filter = ((df_diabetes[\"BloodPressure\"]>150) | (df_diabetes[\"BloodPressure\"]<50) )\n",
    "df_diabetes = df_diabetes[~out_filter]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_diabetes.reset_index(drop=True, inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.4750209205020917"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_diabetes['DiabetesPedigreeFunction'].mean()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2.42"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_diabetes['DiabetesPedigreeFunction'].max()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.08"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_diabetes['DiabetesPedigreeFunction'].min()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.5517269076305219"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "count=0\n",
    "sumhere=0\n",
    "for i in range(len(df_diabetes)):\n",
    "    if df_diabetes['Outcome'][i]==1:\n",
    "        sumhere=sumhere+df_diabetes['DiabetesPedigreeFunction'][i]\n",
    "        count=count+1\n",
    "sumhere/count"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.43420940170940164"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "count=0\n",
    "sumhere=0\n",
    "for i in range(len(df_diabetes)):\n",
    "    if df_diabetes['Outcome'][i]==0:\n",
    "        sumhere=sumhere+df_diabetes['DiabetesPedigreeFunction'][i]\n",
    "        count=count+1\n",
    "sumhere/count"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "249"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "count=0\n",
    "for i in range(len(df_diabetes)):\n",
    "    if df_diabetes['Outcome'][i]==1:\n",
    "        count=count+1\n",
    "count"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "468"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "count=0\n",
    "for i in range(len(df_diabetes)):\n",
    "    if df_diabetes['Outcome'][i]==0:\n",
    "        count=count+1\n",
    "count"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "129"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "count=0\n",
    "for i in range(len(df_diabetes)):\n",
    "    if df_diabetes['DiabetesPedigreeFunction'][i]>0.43 and df_diabetes['Outcome'][i]==1:\n",
    "        count=count+1\n",
    "count"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.5180722891566265"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "129/249"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "175"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "count=0\n",
    "for i in range(len(df_diabetes)):\n",
    "    if df_diabetes['DiabetesPedigreeFunction'][i]>0.43 and df_diabetes['Outcome'][i]==0:\n",
    "        count=count+1\n",
    "count"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.37393162393162394"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "175/468"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "118"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "count=0\n",
    "for i in range(len(df_diabetes)):\n",
    "    if df_diabetes['DiabetesPedigreeFunction'][i]<0.43 and df_diabetes['Outcome'][i]==1:\n",
    "        count=count+1\n",
    "count"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.4738955823293173"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "118/249"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "285"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "count=0\n",
    "for i in range(len(df_diabetes)):\n",
    "    if df_diabetes['DiabetesPedigreeFunction'][i]<0.43 and df_diabetes['Outcome'][i]==0:\n",
    "        count=count+1\n",
    "count"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.6089743589743589"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "285/468"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_train=df_diabetes[['Pregnancies', 'BloodPressure', 'BMI','Age']]\n",
    "df_test=df_diabetes[['Outcome']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.7361111111111112\n",
      "0.6666666666666666\n",
      "0.7013888888888888\n",
      "0.6875\n",
      "0.7222222222222222\n",
      "0.6666666666666666\n",
      "0.6666666666666666\n",
      "0.6944444444444444\n",
      "0.6319444444444444\n",
      "0.7013888888888888\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\dell\\Anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py:578: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  y = column_or_1d(y, warn=True)\n",
      "C:\\Users\\dell\\Anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py:578: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  y = column_or_1d(y, warn=True)\n",
      "C:\\Users\\dell\\Anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py:578: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  y = column_or_1d(y, warn=True)\n",
      "C:\\Users\\dell\\Anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py:578: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  y = column_or_1d(y, warn=True)\n",
      "C:\\Users\\dell\\Anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py:578: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  y = column_or_1d(y, warn=True)\n",
      "C:\\Users\\dell\\Anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py:578: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  y = column_or_1d(y, warn=True)\n",
      "C:\\Users\\dell\\Anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py:578: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  y = column_or_1d(y, warn=True)\n",
      "C:\\Users\\dell\\Anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py:578: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  y = column_or_1d(y, warn=True)\n",
      "C:\\Users\\dell\\Anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py:578: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  y = column_or_1d(y, warn=True)\n",
      "C:\\Users\\dell\\Anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py:578: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  y = column_or_1d(y, warn=True)\n",
      "C:\\Users\\dell\\Anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py:578: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  y = column_or_1d(y, warn=True)\n",
      "C:\\Users\\dell\\Anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py:578: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  y = column_or_1d(y, warn=True)\n",
      "C:\\Users\\dell\\Anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py:578: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  y = column_or_1d(y, warn=True)\n",
      "C:\\Users\\dell\\Anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py:578: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  y = column_or_1d(y, warn=True)\n",
      "C:\\Users\\dell\\Anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py:578: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  y = column_or_1d(y, warn=True)\n",
      "C:\\Users\\dell\\Anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py:578: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  y = column_or_1d(y, warn=True)\n",
      "C:\\Users\\dell\\Anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py:578: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  y = column_or_1d(y, warn=True)\n",
      "C:\\Users\\dell\\Anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py:578: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  y = column_or_1d(y, warn=True)\n",
      "C:\\Users\\dell\\Anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py:578: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  y = column_or_1d(y, warn=True)\n",
      "C:\\Users\\dell\\Anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py:578: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  y = column_or_1d(y, warn=True)\n"
     ]
    }
   ],
   "source": [
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.linear_model import LogisticRegression\n",
    "for i in range(10):\n",
    "    x, x_test, y, y_test = train_test_split(df_train,df_test,test_size=0.2,train_size=0.8)\n",
    "    y=y.astype('int')\n",
    "    clf = LogisticRegression().fit(x, y)\n",
    "    y_test=y_test.astype('int')\n",
    "    clf.fit(x,y)\n",
    "    print(clf.score(x_test, y_test))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 136,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split\n",
    "\n",
    "x, x_test, y, y_test = train_test_split(df_train,df_test,test_size=0.2,train_size=0.8,random_state=0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 137,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\dell\\Anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py:578: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  y = column_or_1d(y, warn=True)\n"
     ]
    }
   ],
   "source": [
    "from sklearn.linear_model import LogisticRegression\n",
    "y=y.astype('int')\n",
    "clf = LogisticRegression(random_state=2).fit(x, y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 138,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.7013888888888888"
      ]
     },
     "execution_count": 138,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "clf.score(x_test, y_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 139,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 0.09772417, -0.00962269,  0.08197178,  0.02415225]])"
      ]
     },
     "execution_count": 139,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_train=df_diabetes[['Pregnancies', 'BloodPressure', 'BMI','Age']]\n",
    "df_test=df_diabetes[['Outcome']]\n",
    "clf.coef_"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 140,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([-3.78229043])"
      ]
     },
     "execution_count": 140,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "clf.intercept_"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 141,
   "metadata": {},
   "outputs": [],
   "source": [
    "y_true = y_test\n",
    "y_pred = clf.predict(x_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 142,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAATsAAAE9CAYAAAB0hcXaAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4xLjEsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy8QZhcZAAAXR0lEQVR4nO3de/xc853H8ddbIiVxCRIRly2lKG1FJVZpi7DZUhX0alsqPBqtdqu11RJbaWhttngovWh/cWtQl9pqWnelipbULwSJuIVmE0ri1q2IkN989o+Z6DR+md9knJlzTr7vp8d5ZObMmTOfh/B5fL7Xo4jAzGx1t0beAZiZdYKTnZklwcnOzJLgZGdmSXCyM7MkONmZWRL65x3AykzSJM+JMcvBxJioVr73+nNPtPT/7JpD3tHS762qwiY7gAmLDss7BGvBaUMv5tQ1u/IOw1o0kYl5h9AWhU52ZlYilZ68I2jIyc7MshGVvCNoyMnOzLJRcbIzswSEKzszS4IrOzNLgis7M0uCR2PNLAmu7MwsCe6zM7MUeDTWzNLgys7MkuDKzsyS4NFYM0uCKzszS4L77MwsCW2q7CRtB1xRd+odwMnAYODzwKLa+QkRcd3K7uNkZ2aFFhGPACMAJPUDngKuBsYBZ0XEGc3cx8nOzLLRmWbsPsDciJgnrdpu7n7gjpllIqKnpWMVfRq4rO79lyU9IOkCSRs0+qKTnZllIyotHZLGS+quO8b3dntJA4ADgV/UTp0LbE21ifsX4MxG4bkZa2bZaLEZGxFdQDNPaNoPuDcinq1979nlH0iaAlzT6MtOdmaWjfbPszuUuiaspOER8Zfa24OBWY2+7GRnZtlo4woKSQOBfwGOrjv9PUkjgAD+vMJnb+JkZ2bZaGNlFxGvAButcG6VHiztZGdm2fAKCjNLgtfGmlkSXNmZWRKc7MwsBS2shugoJzszy4YrOzNLggcozCwJruzMLAkFr+y864mZJcGVnZllw81YM0tCwZuxTnZmlg1XdmaWBCc7M0uCm7FmlgRXdmaWBFd2ZpYEV3ZmlgRXdmaWBFd2ZpYEJzszS0JE3hE05GRnZtlwZWdmSXCyM7MkeDTWzJJQ8MrOm3eaWRJc2ZlZNjwaa2ZJKHgz1snOzLLhZGdmSfBorJmlICruszOzFLgZa2ZJcDPWzJLgZqyZJcHNWDNLQsGTnZeLdcDUy69m7GeO5qDPfoHjJ05m6dLXWPD0Mxz6+a+y/6eO4j++9V+8/vrreYdpvZjSdSZPL7ifmffd8sa5k791HPOe7Kb7npvovucm9vvw6BwjLJCI1o4OcbJrs2cXPcelV03jigvO4VeX/IRKpcL1v/09Z517AYd96iCuu+J81lt3Hf7nmhvzDtV6MXXqlXzkgM+86fzZ50xh5KgxjBw1hutvuDWHyAqoUmnt6JC2JTtJ20v6pqRzJJ1de/2udv1ekS3r6WHp0tdYtqyHJa8uZeiQDZk+437G7PVBAMbuvy+33n5XzlFab+64czovvPhS3mGUQyVaOzqkLclO0jeBywEBfwLuqb2+TNIJ7fjNoho2dAhHHPox9j3kcPYe+2+sO2ggO2y3DeuuM4j+/fu9cc3CRc/nHKmtimO+OI57Z9zMlK4zGTx4/bzDKYaotHZ0SLsqu6OAURExOSIuqR2TgV1rnyXjr//3N353x93c+IsLuXXapSx5dSl33N39pusk5RCdteInP53Kttvvzi4jx/DMMws5/Xsn5x1SMaRY2QEVYNNezg+vfdYrSeMldUvq7ubNCaGM7u6eyWabDmPDDQazZv/+7LPn7sx88CH+9vJili3rAar9ekOHbJhzpNashQufo1KpEBGcd/6ljBo1Iu+QCiEqlZaOTmlXsvsqcIuk6yV11Y4bgFuAY1f2pYjoioiRETFyJCPbFFpnDR82lAdmPcySV18lIpjePZOtt/wndn3fe7nptjsAmHbdbxn9wffnHKk1a5NNNn7j9UFj92P27EdyjMaa1ZZ5dhFxg6RtqTZbN6PaX7cAuCcietrxm0X13h2351/2/gCfHPfv9OvXj+233ZpPjN2PD+2+K8dPnMwPuqbyrm235pADxuQdqvXikot/xJ4fej9DhmzIn5/oZtIpZ7Dnnruz0047EBHMm7eALx7zzbzDLIaCr6BQFHR30UmaFBMWHZZ3GNaC04ZezKlrduUdhrVo2WtPtdSBvPg7n20pmQz6z0s60mHtFRRmlo2CV3ZOdmaWjYIvF3OyM7NsuLIzsyR4PzszS4IrOzNLQScnCLfCyc7MsuHKzsySUPBk5/3szCwbbdz1RNJgSVdJeljSHEnvl7ShpJslPVb7c4NG93CyM7NstHfXk7OBGyJie2AnYA5wAnBLRLyT6rr7htvHOdmZWSaiEi0dfZG0HvAh4HyAiHgtIl4CxgI/q132M+CgRvdxsjOzbLSvsnsHsAi4UNJ9ks6TNAgYFhF/Aaj9uXGjmzjZmVk2WnwGRf0+lrVj/Ap37g+8Dzg3InYGFtNHk7U3Ho01s2y0OBobEV1Ao21yFgALImJ67f1VVJPds5KGR8RfJA0HFjb6HVd2ZpaNNjVjI+IZYL6k7Wqn9gEeAn4NfK527nPAtEb3cWVnZmXw78ClkgYATwDjqBZrV0o6Cvhf4BONbuBkZ2aZaOdGwBExE3p9VsM+zd7Dyc7MslHwFRROdmaWDSc7M0tBMxOE8+RkZ2bZcLIzsyQUezs7Jzszy4absWaWBic7M0uCm7FmlgI3Y80sDa7szCwFruzMLA2u7MwsBU0+Oyc3TnZmlg0nOzNLQdErO+9UbGZJcGVnZtkoeGXnZGdmmSh6M7bPZCdpG+A4YMv66yNiTPvCMrOyKX2yo/rYsvOBS4Ce9oZjZmW1OiS7SkT8oO2RmFm5hfKOoKGVJjtJ69VeTqs9oftqYOnyzyPi/9ocm5mVSJkru9lAAMvT9bfqPgvgn9oVlJmVT1RKWtlFxBYAktaMiNfrP5O0ZrsDM7NyKXpl18yk4ulNnjOzhEWopaNTGvXZbQwMB9aW9B7+3pxdDxjYgdjMrESKXtk16rP7CHAksDnw47rzf+Mf++/MzErdZ3chcKGkT0bElR2MycxKKIq9d2dT8+zeKWnCiicj4rQ2xGNmJVXayq7OsrrXa1Ft3s5uTzhmVlalT3YR8d/17yX9N/CrtkVkZqW0OjRjV/Q2YOusAzGzcit9ZSfpPqorJgD6UZ2O4v46MyuVZiq7j9e9XgY8ExFLV3axmaWpkxOEW9Ew2UnqB/wyInbqUDxmVlJlnlRMRPRIekjSZhHxVKeCMrPyqZS5sqsZAsyRdBewePnJiDikbVGZWemUuhlbM7ntUZhZ6ZV2NFbSTRExJiJu6WRAZlZOZZ5nN7RjUZhZ6ZW2sgPWl7TSfrmI+GUb4jGzkirzAMX6wAH8fR+7egE42ZnZG8o8QDEvIo7sWCRmVmpl7rMrdpo2s0IpczP2sI5FYWalV9pmbETM6mQgZlZuZW7G5u60oRfnHYK16Fuvj887BOuwMjdjc9e9xT15h2AtGDl/FFM3mpZ3GNaiiUxs6XulbcZKepC/72P3JhHx3rZEZGalVObK7oDan1+q/bm8TfkZ4JW2RWRm1gaNBijmAUjaIyL2qPvoBEl/AE5pd3BmVh4FH59gjSauGSTpA8vfSNodGNS+kMysjCqhlo5OaWaA4ijgAknr196/BHhlhZn9g9IOUCwXETOAnSStBygi/tr+sMysbAq+K3tTTxd7G/AxYEugv1TN3hHhPjsze0O0cYVp7Xk43cBTEXGApIuAPYHlxdcRETGz0T2aacZOq91wBuCniplZryrtHaE4FpgDrFd37viIuKrZGzST7DaPiA+vamRmlpZKmyo7SZsDHwG+CxzX6n2aGY39o6T3tPoDZpaGQC0dksZL6q47Vlxr+H3gG7y5W/C7kh6QdFatu62hZiq7DwBHSHqSajNWQHgFhZnVa3WAIiK6gK7ePpN0ALAwImZI2qvuoxOBZ4ABte9+kz7m/jaT7PZrJmAzS1ubBij2AA6UtD+wFrCepEsi4rO1z5dKuhD4el836rMZGxHzaqspllCdJL38MDN7Q6XFo5GIODEiNo+ILYFPA7dGxGclDQdQdXrIQUCfW9I1M/XkQOBMYFNgIfB2qqMiO/b1XTNLR4fn2V0qaSjVbrWZwBf6+kIzzdhTgd2A30bEzpL2Bg59S2Ga2WqnnfPsACLiNuC22uvRq/r9ZkZjX4+I54E1JK0REb8DRqzqD5nZ6q2i1o5Oaaaye0nSOsDtVEvHhcCy9oZlZmXTrnl2WWmmshtLdf+6rwE3AHOBj7YzKDMrn2jx6JSGlV1tPdq0iNiXav/jzzoSlZlZxhomu4jokfSKpPW924mZNVL6XU+AV4EHJd0MLF5+MiK+0raozKx0Kip2n10zye7a2mFmtlJFX2nQzOad7qczsz4VvRm70tFYSWMlfanu/XRJT9SOj3cmPDMrizLPs/sG1bVoy70NGEX1YTsXAk1vmmdmq7+iz7NrlOwGRMT8uvd31lZSPC/JTxczs39Q5j67DerfRMSX694ObU84ZlZWnWyStqLRCorpkj6/4klJRwN/al9IZlZG7djiKUuNKruvAb+S9G/AvbVzu1Dtuzuo3YGZWbmUthkbEQuB3SWN5u97110bEbd2JDIzK5WiN2ObmWd3K+AEZ2YNFX2eXTMrKMzM+uRkZ2ZJiLI3Y83MmuHKzsyS4GRnZkko+tSTZrZlNzMrPVd2ZpaJ0s+zMzNrhvvszCwJTnZmloSiD1A42ZlZJtxnZ2ZJcDPWzJLgZqyZJaFS8HTnZGdmmXAz1sySUOy6zsnOzDLiys7MkuCpJ2aWBA9QmFkSip3qnOzMLCPuszOzJBS9GevNO80sCa7szCwTxa7rnOzMLCPuszOzJBS9z87JzswyUexU52RnZhlxM9bMkhAFr+2c7MwsE67szCwJHqBI3JDhQ/jaWcexwdANiKhww89v5DcX/JqtdtiKY077EgPeNoCenh7OPelcHrv/0bzDtRUM33QYZ/z4FIZsPIRKpcIVU3/JRV2Xsd+B+/KVbxzNNttuxSFjDuPBmXPyDjV3xU51TnZt19PTwwXfOZ+5s+ay9qC1Oeva7zPzjvsYN2Ecl3//MmbcNoNd9h7JuAnjmPCpE/MO11awrKeH004+i9kPPMygdQYy7ZZLufO2u3l0zlyOOeLrfOfMk/IOsTBc2SXuxYUv8uLCFwFYsngJ8x+fz0abbEQErL3uQAAGrTuQF559Ps8wbSUWPfsci559DoDFL7/C448+ybDhG/OH30/PObLicZ/dCiSNi4gLO/27RbDx5huz9Y7v4JH7HmHKpC5OufgUjjzpSNZYYw2OP/jreYdnfdhsi+Hs+J7tuH/GrLxDKaSij8bmsRHApBx+M3drDVyLE386gSmTprDk5SXsf9j+nHfKeRy52zjOO2UKXzn92LxDtAYGDlqbH190BqeedCYvv7w473AKqdLi0SltSXaSHljJ8SAwrMH3xkvqltTdTXc7QstFv/79OPGnE7jt6tu464a7ABj9sX344/V/BODOa+5k2522zTNEa6B///786MIzmHbVddx07a15h1NY0eI/ndKuym4YcDjw0V6OlXZORURXRIyMiJEjGdmm0DrvK6cfy/zH5zPtvF+9ce6FZ1/g3bu9B4D37rETT//56bzCsz5MPvtk5j76JBece2neoRRauyo7SWtJ+pOk+yXNljSpdn4rSdMlPSbpCkkDGt2nXX121wDrRMTMXgK/rU2/WUg7jNqB0R8bzZNznuTs688BYOr3pvLDE37A5789nn79+vHa0tf44Qk/yDlS680u/zyCgz91AA/Pfozf/O4yAM787g8ZMGAAJ0/+BhtutAHn/fwcHpr1KOM++aWco81XJdpWpS0FRkfEy5LWBO6UdD1wHHBWRFwu6SfAUcC5K7uJon0BviWTNCm6t7gn7zCsBSPnj2LqRtPyDsNaNPe5e1t6Tthhbz+kpWRy8bxfNv17kgYCdwJfBK4FNomIZZLeD3w7Iv51Zd/1TsVmlolo8WiGpH6SZgILgZuBucBLEbGsdskCYLNG93CyM7NMVIiWjvqBydoxfsV7R0RPRIwANgd2Bd7VSwgNc6cnFZtZJlodWY2ILqCryWtfqvX77wYMltS/Vt1tDjQc5XNlZ2aZaONo7FBJg2uv1wb2BeYAvwM+Xrvsc0DDjmJXdmaWiTaujR0O/ExSP6oF2pURcY2kh4DLJX0HuA84v9FNnOzMLBPtmiAcEQ8AO/dy/gmq/XdNcbIzs0x4IwAzS0JR5+wu52RnZpnwfnZmlgQ3Y80sCUXfz87Jzswy4WasmSXBAxRmlgT32ZlZEtxnZ2ZJKHqfnTcCMLMkuLIzs0x4gMLMklD0ZqyTnZllwgMUZpaENj5dLBNOdmaWiWKnOic7M8uI++zMLAlOdmaWBE89MbMkuLIzsyR46omZJcHNWDNLgpuxZpYEV3ZmlgRXdmaWBA9QmFkSir421pt3mlkSXNmZWSbcjDWzJBS9GetkZ2aZcGVnZklwZWdmSXBlZ2ZJcGVnZklwZWdmSYio5B1CQ052ZpYJr401syR41xMzS4IrOzNLgis7M0uCp56YWRI89cTMkuBmrJklwQMUZpaEold23qnYzJLgys7MMuHRWDNLQtGbsU52ZpYJD1CYWRJc2ZlZEtxnZ2ZJ8AoKM0uCKzszS0LR++w8qdjMMhEt/tMXSRdIWihpVt25b0t6StLM2rF/X/dxsjOzTERES0cTLgI+3Mv5syJiRO24rq+buBlrZploVzM2Im6XtOVbvU+hk93I+aPyDsFadPjzY/MOwToshx67L0s6HOgG/iMiXmx0sYreqbi6kjQ+IrryjsNa47+/7EgaD4yvO9W14r/bWmV3TUS8u/Z+GPAc1Rx7KjA8Io5s+DtOdvmQ1B0RI/OOw1rjv7/OWjHZNftZPQ9QmFnpSBpe9/ZgYNbKrl2u0H12ZmaSLgP2AoZIWgBMBPaSNIJqM/bPwNF93cfJLj/u7yk3//11SEQc2svp81f1Pu6zM7MkuM/OzJLgZJcDSR+W9IikxyWdkHc81rzeli5ZOTjZdZikfsCPgP2AHYBDJe2Qb1S2Ci6i96VLVnBOdp23K/B4RDwREa8BlwNeblASEXE78ELecdiqc7LrvM2A+XXvF9TOmVkbOdl1nno55yFxszZzsuu8BcAWde83B57OKRazZDjZdd49wDslbSVpAPBp4Nc5x2S22nOy67CIWAZ8GbgRmANcGRGz843KmlVbunQXsJ2kBZKOyjsma45XUJhZElzZmVkSnOzMLAlOdmaWBCc7M0uCk52ZJcHJLmGSemoPGJ4l6ReSBr6Fe+0l6Zra6wMb7eYiabCkY1r4jW9L+nqrMVranOzStqT2gOF3A68BX6j/UFWr/N9IRPw6IiY3uGQwsMrJzuytcLKz5e4AtpG0paQ5kn4M3AtsIWmMpLsk3VurANeBN/ble1jSncAhy28k6QhJP6y9Hibpakn3147dgcnA1rWq8vTadcdLukfSA5Im1d3rpNref78FtuvYvw1b7TjZGZL6U91f78Haqe2AqRGxM7AY+E9g34h4H9UHEh8naS1gCvBR4IPAJiu5/TnA7yNiJ+B9wGzgBGBurao8XtIY4J1Ut78aAewi6UOSdqG6nG5nqsnUT023lvmBO2lbW9LM2us7qD7EZFNgXkTcXTu/G9VNRv8gCWAA1eVS2wNPRsRjAJIu4R8fdLzcaOBwgIjoAf4qaYMVrhlTO+6rvV+HavJbF7g6Il6p/YbXEFvLnOzStiQiRtSfqCW0xfWngJtXfMJT3WPssiDgvyLipyv8xlcz/A1LnJux1pe7gT0kbQMgaaCkbYGHga0kbV27rrfH3QHcAnyx9t1+ktYD/ka1alvuRuDIur7AzSRtDNwOHCxpbUnrUm0ym7XEyc4aiohFwBHAZZIeoJr8to+IV6k2W6+tDVDMW8ktjgX2lvQgMAPYMSKep9osniXp9Ii4Cfg5cFftuquAdSPiXuAKYCbwP1Sb2mYt8a4nZpYEV3ZmlgQnOzNLgpOdmSXByc7MkuBkZ2ZJcLIzsyQ42ZlZEpzszCwJ/w/lmvx4TaeofgAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<Figure size 360x360 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "from sklearn.metrics import confusion_matrix\n",
    "cm = confusion_matrix(y_true, y_pred)\n",
    "f, ax = plt.subplots(figsize=(5,5))\n",
    "sns.heatmap(cm,fmt=\".0f\", annot=True,linewidths=0.2, linecolor=\"purple\", ax=ax)\n",
    "plt.xlabel(\"Predicted\")\n",
    "plt.ylabel(\"Grand Truth\")\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# covid"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_covid=pd.read_csv('patients_datacovid.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(24613, 21)"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_covid.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['patient_number', 'p_id', 'state_patient_number', 'date_announced',\n",
       "       'age_bracket', 'gender', 'detected_city', 'detected_district',\n",
       "       'detected_state', 'state_code', 'nationality', 'type_of_transmission',\n",
       "       'contracted_from_which_patient_suspected', 'status_change_date',\n",
       "       'current_status', 'estimated_onset_date', 'source1', 'source2',\n",
       "       'source3', 'notes', 'backup_notes'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 70,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_covid.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_covid2 = df_covid[['age_bracket','gender', 'nationality', 'type_of_transmission']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "age_bracket             22488\n",
       "gender                  19526\n",
       "nationality             21917\n",
       "type_of_transmission    21632\n",
       "dtype: int64"
      ]
     },
     "execution_count": 72,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_covid2.isnull().sum()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_covid2 = df_covid2.dropna(how ='any') \n",
    "df_covid2=df_covid2.reset_index(drop=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(813, 4)"
      ]
     },
     "execution_count": 74,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_covid2.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>age_bracket</th>\n",
       "      <th>gender</th>\n",
       "      <th>nationality</th>\n",
       "      <th>type_of_transmission</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>20</td>\n",
       "      <td>F</td>\n",
       "      <td>India</td>\n",
       "      <td>Imported</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>45</td>\n",
       "      <td>M</td>\n",
       "      <td>India</td>\n",
       "      <td>Imported</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>24</td>\n",
       "      <td>M</td>\n",
       "      <td>India</td>\n",
       "      <td>Imported</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>69</td>\n",
       "      <td>M</td>\n",
       "      <td>Italy</td>\n",
       "      <td>Imported</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>70</td>\n",
       "      <td>F</td>\n",
       "      <td>Italy</td>\n",
       "      <td>Imported</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  age_bracket gender nationality type_of_transmission\n",
       "0          20      F       India             Imported\n",
       "1          45      M       India             Imported\n",
       "2          24      M       India             Imported\n",
       "3          69      M       Italy             Imported\n",
       "4          70      F       Italy             Imported"
      ]
     },
     "execution_count": 75,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_covid2.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['India', 'Italy', 'Indonesia', 'Thailand',\n",
       "       'United States of America', 'United Kingdom', 'Tibet', 'Malaysia',\n",
       "       'Myanmar'], dtype=object)"
      ]
     },
     "execution_count": 76,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_covid2.nationality.unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "metadata": {},
   "outputs": [],
   "source": [
    "for i in range(len(df_covid2)):\n",
    "    if df_covid2['nationality'][i]=='India':\n",
    "        df_covid2['nationality'][i]=0\n",
    "    else:\n",
    "        df_covid2['nationality'][i]=1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "metadata": {},
   "outputs": [],
   "source": [
    "for i in range(len(df_covid2)):\n",
    "    if df_covid2['gender'][i]=='M':\n",
    "        df_covid2['gender'][i]=0\n",
    "    else:\n",
    "        df_covid2['gender'][i]=1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "metadata": {},
   "outputs": [],
   "source": [
    "for i in range(len(df_covid2)):\n",
    "    if df_covid2['type_of_transmission'][i]=='Imported':\n",
    "        df_covid2['type_of_transmission'][i]=1\n",
    "    else:\n",
    "        df_covid2['type_of_transmission'][i]=0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>age_bracket</th>\n",
       "      <th>gender</th>\n",
       "      <th>nationality</th>\n",
       "      <th>type_of_transmission</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>20</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>45</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>24</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>69</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>70</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  age_bracket gender nationality type_of_transmission\n",
       "0          20      1           0                    1\n",
       "1          45      0           0                    1\n",
       "2          24      0           0                    1\n",
       "3          69      0           1                    1\n",
       "4          70      1           1                    1"
      ]
     },
     "execution_count": 80,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_covid2.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_covid2.to_csv('covidsecond')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(340, 6)"
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_modified1.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_covid=pd.read_csv('coviddata2.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>age_bracket</th>\n",
       "      <th>gender</th>\n",
       "      <th>nationality</th>\n",
       "      <th>type_of_transmission</th>\n",
       "      <th>outcome</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>20</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>45</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>24</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>69</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>70</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   age_bracket  gender  nationality  type_of_transmission  outcome\n",
       "0           20       1            1                     1        1\n",
       "1           45       0            1                     1        1\n",
       "2           24       0            1                     1        1\n",
       "3           69       0            1                     1        1\n",
       "4           70       1            1                     1        1"
      ]
     },
     "execution_count": 54,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_modified1=df_covid\n",
    "df_covid.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(2, 0.4069119286510591, 0)"
      ]
     },
     "execution_count": 55,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import statistics \n",
    "len(df_covid.type_of_transmission.unique()), statistics.mean(df_covid.type_of_transmission),statistics.median(df_covid.type_of_transmission)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x736af4fa90>"
      ]
     },
     "execution_count": 56,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 720x360 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize = (10,5))\n",
    "sns.heatmap(df_modified1.corr(), annot=True, linewidths=.1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_train=df_modified1[['age_bracket','gender','nationality','type_of_transmission']]\n",
    "df_test=df_modified1[['outcome']]\n",
    "x, x_test, y, y_test = train_test_split(df_train,df_test,test_size=0.2,train_size=0.8)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.9\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\dell\\Anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py:578: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  y = column_or_1d(y, warn=True)\n",
      "C:\\Users\\dell\\Anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py:578: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  y = column_or_1d(y, warn=True)\n"
     ]
    }
   ],
   "source": [
    "from sklearn.model_selection import train_test_split\n",
    "for i in range(1):\n",
    "    x, x_test, y, y_test = train_test_split(df_train,df_test,test_size=0.2,train_size=0.8)\n",
    "    y=y.astype('int')\n",
    "    clf = LogisticRegression().fit(x, y)\n",
    "    y_test=y_test.astype('int')\n",
    "    clf.fit(x,y)\n",
    "    print(clf.score(x_test, y_test))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 10  15]\n",
      " [  3 152]]\n"
     ]
    }
   ],
   "source": [
    "y_pred=clf.predict(x_test)\n",
    "from sklearn.metrics import confusion_matrix\n",
    "cm = confusion_matrix(y_test, y_pred)\n",
    "print(cm)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.9666666666666667\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\dell\\Anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py:578: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  y = column_or_1d(y, warn=True)\n"
     ]
    }
   ],
   "source": [
    "gnb.fit(x,y)\n",
    "GaussianNB(priors=None)\n",
    "print(gnb.score(x_test,y_test))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 11   8]\n",
      " [  6 155]]\n"
     ]
    }
   ],
   "source": [
    "y_pred=clf.predict(x_test)\n",
    "from sklearn.metrics import confusion_matrix\n",
    "cm = confusion_matrix(y_test, y_pred)\n",
    "print(cm)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\dell\\Anaconda3\\lib\\site-packages\\ipykernel_launcher.py:3: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples,), for example using ravel().\n",
      "  This is separate from the ipykernel package so we can avoid doing imports until\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.9388888888888889\n"
     ]
    }
   ],
   "source": [
    "for i in range(1):\n",
    "    x, x_test, y, y_test = train_test_split(df_train,df_test,test_size=0.2,train_size=0.8)\n",
    "    model.fit(x, y)\n",
    "    print(accuracy_score(model.predict(x_test),y_test))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 10   6]\n",
      " [  1 163]]\n"
     ]
    }
   ],
   "source": [
    "y_pred=clf.predict(x_test)\n",
    "from sklearn.metrics import confusion_matrix\n",
    "cm = confusion_matrix(y_test, y_pred)\n",
    "print(cm)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'Sequential' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-52-d4b49a32916a>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m()\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mclassifier\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mSequential\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m \u001b[1;31m#First Hidden Layer\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[0mclassifier\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0madd\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mDense\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m5\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mactivation\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;34m'relu'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mkernel_initializer\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;34m'random_normal'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0minput_dim\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;36m4\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[1;31m#Second  Hidden Layer\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'Sequential' is not defined"
     ]
    }
   ],
   "source": [
    "classifier = Sequential()\n",
    "#First Hidden Layer\n",
    "classifier.add(Dense(5, activation='relu', kernel_initializer='random_normal', input_dim=4))\n",
    "#Second  Hidden Layer\n",
    "\n",
    "classifier.add(Dense(3, activation='relu', kernel_initializer='random_normal'))\n",
    "#Output Layer\n",
    "classifier.add(Dense(1, activation='sigmoid', kernel_initializer='random_normal'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Epoch 1/300\n",
      "717/717 [==============================] - 1s 945us/step - loss: 0.6492 - acc: 0.9010\n",
      "Epoch 2/300\n",
      "717/717 [==============================] - 0s 197us/step - loss: 0.4623 - acc: 0.9010\n",
      "Epoch 3/300\n",
      "717/717 [==============================] - 0s 186us/step - loss: 0.3589 - acc: 0.9010\n",
      "Epoch 4/300\n",
      "717/717 [==============================] - 0s 187us/step - loss: 0.3578 - acc: 0.9010\n",
      "Epoch 5/300\n",
      "717/717 [==============================] - 0s 194us/step - loss: 0.3556 - acc: 0.9010\n",
      "Epoch 6/300\n",
      "717/717 [==============================] - 0s 184us/step - loss: 0.3547 - acc: 0.9010\n",
      "Epoch 7/300\n",
      "717/717 [==============================] - 0s 188us/step - loss: 0.3530 - acc: 0.9010\n",
      "Epoch 8/300\n",
      "717/717 [==============================] - 0s 193us/step - loss: 0.3535 - acc: 0.9010\n",
      "Epoch 9/300\n",
      "717/717 [==============================] - 0s 173us/step - loss: 0.3495 - acc: 0.9010\n",
      "Epoch 10/300\n",
      "717/717 [==============================] - 0s 188us/step - loss: 0.3488 - acc: 0.9010\n",
      "Epoch 11/300\n",
      "717/717 [==============================] - 0s 195us/step - loss: 0.3465 - acc: 0.9010\n",
      "Epoch 12/300\n",
      "717/717 [==============================] - 0s 181us/step - loss: 0.3449 - acc: 0.9010\n",
      "Epoch 13/300\n",
      "717/717 [==============================] - 0s 184us/step - loss: 0.3429 - acc: 0.9010\n",
      "Epoch 14/300\n",
      "717/717 [==============================] - 0s 184us/step - loss: 0.3416 - acc: 0.9010\n",
      "Epoch 15/300\n",
      "717/717 [==============================] - 0s 186us/step - loss: 0.3402 - acc: 0.9010\n",
      "Epoch 16/300\n",
      "717/717 [==============================] - 0s 186us/step - loss: 0.3389 - acc: 0.9010\n",
      "Epoch 17/300\n",
      "717/717 [==============================] - 0s 187us/step - loss: 0.3366 - acc: 0.9010\n",
      "Epoch 18/300\n",
      "717/717 [==============================] - 0s 186us/step - loss: 0.3349 - acc: 0.9010\n",
      "Epoch 19/300\n",
      "717/717 [==============================] - 0s 193us/step - loss: 0.3334 - acc: 0.9010\n",
      "Epoch 20/300\n",
      "717/717 [==============================] - 0s 188us/step - loss: 0.3314 - acc: 0.9010\n",
      "Epoch 21/300\n",
      "717/717 [==============================] - 0s 186us/step - loss: 0.3298 - acc: 0.9010\n",
      "Epoch 22/300\n",
      "717/717 [==============================] - 0s 177us/step - loss: 0.3268 - acc: 0.9010\n",
      "Epoch 23/300\n",
      "717/717 [==============================] - 0s 187us/step - loss: 0.3249 - acc: 0.9010\n",
      "Epoch 24/300\n",
      "717/717 [==============================] - 0s 190us/step - loss: 0.3224 - acc: 0.9010\n",
      "Epoch 25/300\n",
      "717/717 [==============================] - 0s 184us/step - loss: 0.3199 - acc: 0.9010\n",
      "Epoch 26/300\n",
      "717/717 [==============================] - 0s 179us/step - loss: 0.3174 - acc: 0.9010\n",
      "Epoch 27/300\n",
      "717/717 [==============================] - 0s 188us/step - loss: 0.3164 - acc: 0.9010\n",
      "Epoch 28/300\n",
      "717/717 [==============================] - 0s 187us/step - loss: 0.3120 - acc: 0.9010\n",
      "Epoch 29/300\n",
      "717/717 [==============================] - 0s 186us/step - loss: 0.3097 - acc: 0.9010\n",
      "Epoch 30/300\n",
      "717/717 [==============================] - 0s 184us/step - loss: 0.3065 - acc: 0.9010\n",
      "Epoch 31/300\n",
      "717/717 [==============================] - 0s 181us/step - loss: 0.3030 - acc: 0.9010\n",
      "Epoch 32/300\n",
      "717/717 [==============================] - 0s 194us/step - loss: 0.2989 - acc: 0.9010\n",
      "Epoch 33/300\n",
      "717/717 [==============================] - 0s 187us/step - loss: 0.2954 - acc: 0.9010\n",
      "Epoch 34/300\n",
      "717/717 [==============================] - 0s 184us/step - loss: 0.2905 - acc: 0.9010\n",
      "Epoch 35/300\n",
      "717/717 [==============================] - 0s 190us/step - loss: 0.2884 - acc: 0.9010\n",
      "Epoch 36/300\n",
      "717/717 [==============================] - 0s 186us/step - loss: 0.2849 - acc: 0.9010\n",
      "Epoch 37/300\n",
      "717/717 [==============================] - 0s 184us/step - loss: 0.2803 - acc: 0.9010\n",
      "Epoch 38/300\n",
      "717/717 [==============================] - 0s 183us/step - loss: 0.2770 - acc: 0.9010\n",
      "Epoch 39/300\n",
      "717/717 [==============================] - 0s 181us/step - loss: 0.2737 - acc: 0.9010\n",
      "Epoch 40/300\n",
      "717/717 [==============================] - 0s 184us/step - loss: 0.2722 - acc: 0.9010\n",
      "Epoch 41/300\n",
      "717/717 [==============================] - 0s 184us/step - loss: 0.2700 - acc: 0.9010\n",
      "Epoch 42/300\n",
      "717/717 [==============================] - 0s 197us/step - loss: 0.2694 - acc: 0.9010\n",
      "Epoch 43/300\n",
      "717/717 [==============================] - 0s 209us/step - loss: 0.2669 - acc: 0.9010\n",
      "Epoch 44/300\n",
      "717/717 [==============================] - 0s 195us/step - loss: 0.2664 - acc: 0.9010\n",
      "Epoch 45/300\n",
      "717/717 [==============================] - 0s 190us/step - loss: 0.2645 - acc: 0.9010\n",
      "Epoch 46/300\n",
      "717/717 [==============================] - 0s 183us/step - loss: 0.2628 - acc: 0.9010\n",
      "Epoch 47/300\n",
      "717/717 [==============================] - 0s 174us/step - loss: 0.2615 - acc: 0.9010\n",
      "Epoch 48/300\n",
      "717/717 [==============================] - 0s 198us/step - loss: 0.2609 - acc: 0.9010\n",
      "Epoch 49/300\n",
      "717/717 [==============================] - 0s 218us/step - loss: 0.2600 - acc: 0.9010\n",
      "Epoch 50/300\n",
      "717/717 [==============================] - 0s 206us/step - loss: 0.2577 - acc: 0.9010\n",
      "Epoch 51/300\n",
      "717/717 [==============================] - 0s 184us/step - loss: 0.2586 - acc: 0.9010\n",
      "Epoch 52/300\n",
      "717/717 [==============================] - 0s 184us/step - loss: 0.2571 - acc: 0.9010\n",
      "Epoch 53/300\n",
      "717/717 [==============================] - 0s 179us/step - loss: 0.2559 - acc: 0.9010\n",
      "Epoch 54/300\n",
      "717/717 [==============================] - 0s 179us/step - loss: 0.2558 - acc: 0.9010\n",
      "Epoch 55/300\n",
      "717/717 [==============================] - 0s 185us/step - loss: 0.2545 - acc: 0.9010\n",
      "Epoch 56/300\n",
      "717/717 [==============================] - 0s 190us/step - loss: 0.2541 - acc: 0.9010\n",
      "Epoch 57/300\n",
      "717/717 [==============================] - 0s 179us/step - loss: 0.2523 - acc: 0.9010\n",
      "Epoch 58/300\n",
      "717/717 [==============================] - 0s 190us/step - loss: 0.2524 - acc: 0.9010\n",
      "Epoch 59/300\n",
      "717/717 [==============================] - 0s 173us/step - loss: 0.2505 - acc: 0.9010\n",
      "Epoch 60/300\n",
      "717/717 [==============================] - 0s 179us/step - loss: 0.2488 - acc: 0.9010\n",
      "Epoch 61/300\n",
      "717/717 [==============================] - 0s 179us/step - loss: 0.2500 - acc: 0.9010\n",
      "Epoch 62/300\n",
      "717/717 [==============================] - 0s 184us/step - loss: 0.2496 - acc: 0.9010\n",
      "Epoch 63/300\n",
      "717/717 [==============================] - 0s 184us/step - loss: 0.2479 - acc: 0.9010\n",
      "Epoch 64/300\n",
      "717/717 [==============================] - 0s 179us/step - loss: 0.2466 - acc: 0.9010\n",
      "Epoch 65/300\n",
      "717/717 [==============================] - 0s 179us/step - loss: 0.2482 - acc: 0.9010\n",
      "Epoch 66/300\n",
      "717/717 [==============================] - 0s 201us/step - loss: 0.2455 - acc: 0.9010\n",
      "Epoch 67/300\n",
      "717/717 [==============================] - 0s 206us/step - loss: 0.2451 - acc: 0.9010\n",
      "Epoch 68/300\n",
      "717/717 [==============================] - 0s 223us/step - loss: 0.2460 - acc: 0.9010\n",
      "Epoch 69/300\n",
      "717/717 [==============================] - 0s 206us/step - loss: 0.2430 - acc: 0.9010\n",
      "Epoch 70/300\n",
      "717/717 [==============================] - 0s 206us/step - loss: 0.2439 - acc: 0.9010\n",
      "Epoch 71/300\n",
      "717/717 [==============================] - 0s 201us/step - loss: 0.2428 - acc: 0.9010\n",
      "Epoch 72/300\n",
      "717/717 [==============================] - 0s 212us/step - loss: 0.2433 - acc: 0.9010\n",
      "Epoch 73/300\n",
      "717/717 [==============================] - 0s 206us/step - loss: 0.2425 - acc: 0.9010\n",
      "Epoch 74/300\n",
      "717/717 [==============================] - 0s 218us/step - loss: 0.2395 - acc: 0.9010\n",
      "Epoch 75/300\n",
      "717/717 [==============================] - 0s 206us/step - loss: 0.2416 - acc: 0.9010\n",
      "Epoch 76/300\n",
      "717/717 [==============================] - 0s 206us/step - loss: 0.2392 - acc: 0.9010\n",
      "Epoch 77/300\n",
      "717/717 [==============================] - 0s 206us/step - loss: 0.2389 - acc: 0.9010\n",
      "Epoch 78/300\n",
      "717/717 [==============================] - 0s 206us/step - loss: 0.2422 - acc: 0.9010\n",
      "Epoch 79/300\n",
      "717/717 [==============================] - 0s 206us/step - loss: 0.2411 - acc: 0.9135\n",
      "Epoch 80/300\n",
      "717/717 [==============================] - 0s 218us/step - loss: 0.2363 - acc: 0.9344\n",
      "Epoch 81/300\n",
      "717/717 [==============================] - 0s 206us/step - loss: 0.2372 - acc: 0.9344\n",
      "Epoch 82/300\n",
      "717/717 [==============================] - 0s 195us/step - loss: 0.2382 - acc: 0.9344\n",
      "Epoch 83/300\n",
      "717/717 [==============================] - 0s 190us/step - loss: 0.2376 - acc: 0.9344\n",
      "Epoch 84/300\n",
      "717/717 [==============================] - 0s 190us/step - loss: 0.2362 - acc: 0.9344\n",
      "Epoch 85/300\n",
      "717/717 [==============================] - 0s 179us/step - loss: 0.2361 - acc: 0.9344\n",
      "Epoch 86/300\n",
      "717/717 [==============================] - 0s 187us/step - loss: 0.2349 - acc: 0.9344\n",
      "Epoch 87/300\n",
      "717/717 [==============================] - 0s 188us/step - loss: 0.2368 - acc: 0.9344\n",
      "Epoch 88/300\n",
      "717/717 [==============================] - 0s 186us/step - loss: 0.2357 - acc: 0.9344\n",
      "Epoch 89/300\n",
      "717/717 [==============================] - 0s 186us/step - loss: 0.2357 - acc: 0.9344\n",
      "Epoch 90/300\n",
      "717/717 [==============================] - 0s 176us/step - loss: 0.2360 - acc: 0.9344\n",
      "Epoch 91/300\n",
      "717/717 [==============================] - 0s 188us/step - loss: 0.2352 - acc: 0.9344\n",
      "Epoch 92/300\n",
      "717/717 [==============================] - 0s 184us/step - loss: 0.2362 - acc: 0.9344\n",
      "Epoch 93/300\n",
      "717/717 [==============================] - 0s 184us/step - loss: 0.2343 - acc: 0.9344\n",
      "Epoch 94/300\n",
      "717/717 [==============================] - 0s 184us/step - loss: 0.2344 - acc: 0.9344\n",
      "Epoch 95/300\n",
      "717/717 [==============================] - 0s 187us/step - loss: 0.2339 - acc: 0.9344 0s - loss: 0.1868 - acc: 0.948 - ETA: 0s - loss: 0.2206 - acc: 0.939\n",
      "Epoch 96/300\n",
      "717/717 [==============================] - 0s 186us/step - loss: 0.2341 - acc: 0.9344\n",
      "Epoch 97/300\n",
      "717/717 [==============================] - 0s 184us/step - loss: 0.2343 - acc: 0.9344\n",
      "Epoch 98/300\n",
      "717/717 [==============================] - 0s 193us/step - loss: 0.2353 - acc: 0.9344\n",
      "Epoch 99/300\n",
      "717/717 [==============================] - 0s 184us/step - loss: 0.2335 - acc: 0.9344\n",
      "Epoch 100/300\n",
      "717/717 [==============================] - 0s 173us/step - loss: 0.2330 - acc: 0.9344\n",
      "Epoch 101/300\n",
      "717/717 [==============================] - 0s 184us/step - loss: 0.2348 - acc: 0.9344\n",
      "Epoch 102/300\n",
      "717/717 [==============================] - 0s 181us/step - loss: 0.2325 - acc: 0.9344\n",
      "Epoch 103/300\n",
      "717/717 [==============================] - 0s 186us/step - loss: 0.2325 - acc: 0.9344\n",
      "Epoch 104/300\n",
      "717/717 [==============================] - 0s 176us/step - loss: 0.2312 - acc: 0.9344\n",
      "Epoch 105/300\n",
      "717/717 [==============================] - 0s 180us/step - loss: 0.2338 - acc: 0.9344\n",
      "Epoch 106/300\n",
      "717/717 [==============================] - 0s 181us/step - loss: 0.2340 - acc: 0.9344\n",
      "Epoch 107/300\n",
      "717/717 [==============================] - 0s 177us/step - loss: 0.2348 - acc: 0.9344\n",
      "Epoch 108/300\n",
      "717/717 [==============================] - 0s 194us/step - loss: 0.2316 - acc: 0.9344\n",
      "Epoch 109/300\n",
      "717/717 [==============================] - 0s 190us/step - loss: 0.2335 - acc: 0.9344\n",
      "Epoch 110/300\n",
      "717/717 [==============================] - 0s 188us/step - loss: 0.2340 - acc: 0.9344\n",
      "Epoch 111/300\n",
      "717/717 [==============================] - 0s 181us/step - loss: 0.2297 - acc: 0.9344\n",
      "Epoch 112/300\n",
      "717/717 [==============================] - 0s 185us/step - loss: 0.2356 - acc: 0.9344\n",
      "Epoch 113/300\n",
      "717/717 [==============================] - 0s 174us/step - loss: 0.2335 - acc: 0.9344\n",
      "Epoch 114/300\n",
      "717/717 [==============================] - 0s 186us/step - loss: 0.2351 - acc: 0.9344\n",
      "Epoch 115/300\n",
      "717/717 [==============================] - 0s 187us/step - loss: 0.2323 - acc: 0.9344\n",
      "Epoch 116/300\n",
      "717/717 [==============================] - 0s 181us/step - loss: 0.2347 - acc: 0.9344\n",
      "Epoch 117/300\n",
      "717/717 [==============================] - 0s 193us/step - loss: 0.2326 - acc: 0.9344 0s - loss: 0.2473 - acc: 0.928\n",
      "Epoch 118/300\n",
      "717/717 [==============================] - 0s 184us/step - loss: 0.2316 - acc: 0.9344\n",
      "Epoch 119/300\n",
      "717/717 [==============================] - 0s 187us/step - loss: 0.2319 - acc: 0.9344\n",
      "Epoch 120/300\n",
      "717/717 [==============================] - 0s 187us/step - loss: 0.2316 - acc: 0.9344\n",
      "Epoch 121/300\n",
      "717/717 [==============================] - 0s 188us/step - loss: 0.2313 - acc: 0.9344\n",
      "Epoch 122/300\n",
      "717/717 [==============================] - 0s 188us/step - loss: 0.2303 - acc: 0.9344\n",
      "Epoch 123/300\n",
      "717/717 [==============================] - 0s 186us/step - loss: 0.2305 - acc: 0.9344\n",
      "Epoch 124/300\n",
      "717/717 [==============================] - 0s 186us/step - loss: 0.2297 - acc: 0.9344\n",
      "Epoch 125/300\n",
      "717/717 [==============================] - 0s 183us/step - loss: 0.2323 - acc: 0.9344\n",
      "Epoch 126/300\n",
      "717/717 [==============================] - 0s 186us/step - loss: 0.2301 - acc: 0.9344\n",
      "Epoch 127/300\n",
      "717/717 [==============================] - 0s 173us/step - loss: 0.2314 - acc: 0.9344\n",
      "Epoch 128/300\n",
      "717/717 [==============================] - 0s 188us/step - loss: 0.2288 - acc: 0.9344\n",
      "Epoch 129/300\n",
      "717/717 [==============================] - 0s 187us/step - loss: 0.2315 - acc: 0.9344\n",
      "Epoch 130/300\n",
      "717/717 [==============================] - 0s 193us/step - loss: 0.2304 - acc: 0.9344\n",
      "Epoch 131/300\n",
      "717/717 [==============================] - 0s 186us/step - loss: 0.2322 - acc: 0.9344\n",
      "Epoch 132/300\n",
      "717/717 [==============================] - 0s 179us/step - loss: 0.2313 - acc: 0.9344\n",
      "Epoch 133/300\n",
      "717/717 [==============================] - 0s 179us/step - loss: 0.2346 - acc: 0.9344\n",
      "Epoch 134/300\n",
      "717/717 [==============================] - 0s 187us/step - loss: 0.2318 - acc: 0.9344\n",
      "Epoch 135/300\n",
      "717/717 [==============================] - 0s 183us/step - loss: 0.2305 - acc: 0.9344\n",
      "Epoch 136/300\n",
      "717/717 [==============================] - 0s 183us/step - loss: 0.2310 - acc: 0.9344\n",
      "Epoch 137/300\n",
      "717/717 [==============================] - 0s 174us/step - loss: 0.2312 - acc: 0.9344\n",
      "Epoch 138/300\n",
      "717/717 [==============================] - 0s 184us/step - loss: 0.2292 - acc: 0.9344\n",
      "Epoch 139/300\n",
      "717/717 [==============================] - 0s 183us/step - loss: 0.2292 - acc: 0.9344\n",
      "Epoch 140/300\n",
      "717/717 [==============================] - 0s 183us/step - loss: 0.2296 - acc: 0.9344\n",
      "Epoch 141/300\n",
      "717/717 [==============================] - 0s 187us/step - loss: 0.2298 - acc: 0.9344\n",
      "Epoch 142/300\n",
      "717/717 [==============================] - 0s 180us/step - loss: 0.2293 - acc: 0.9344\n",
      "Epoch 143/300\n",
      "717/717 [==============================] - 0s 181us/step - loss: 0.2311 - acc: 0.9344\n",
      "Epoch 144/300\n",
      "717/717 [==============================] - 0s 186us/step - loss: 0.2290 - acc: 0.9344\n",
      "Epoch 145/300\n",
      "717/717 [==============================] - 0s 181us/step - loss: 0.2301 - acc: 0.9344\n",
      "Epoch 146/300\n",
      "717/717 [==============================] - 0s 180us/step - loss: 0.2314 - acc: 0.9344\n",
      "Epoch 147/300\n",
      "717/717 [==============================] - 0s 181us/step - loss: 0.2338 - acc: 0.9344\n",
      "Epoch 148/300\n",
      "717/717 [==============================] - 0s 194us/step - loss: 0.2287 - acc: 0.9344\n",
      "Epoch 149/300\n",
      "717/717 [==============================] - 0s 188us/step - loss: 0.2285 - acc: 0.9344\n",
      "Epoch 150/300\n",
      "717/717 [==============================] - 0s 181us/step - loss: 0.2314 - acc: 0.9344\n",
      "Epoch 151/300\n",
      "717/717 [==============================] - 0s 188us/step - loss: 0.2307 - acc: 0.9344\n",
      "Epoch 152/300\n",
      "717/717 [==============================] - 0s 188us/step - loss: 0.2306 - acc: 0.9344\n",
      "Epoch 153/300\n",
      "717/717 [==============================] - 0s 181us/step - loss: 0.2294 - acc: 0.9344\n",
      "Epoch 154/300\n",
      "717/717 [==============================] - 0s 188us/step - loss: 0.2326 - acc: 0.9344\n",
      "Epoch 155/300\n",
      "717/717 [==============================] - 0s 183us/step - loss: 0.2291 - acc: 0.9344\n",
      "Epoch 156/300\n",
      "717/717 [==============================] - 0s 181us/step - loss: 0.2300 - acc: 0.9344\n",
      "Epoch 157/300\n",
      "717/717 [==============================] - 0s 186us/step - loss: 0.2313 - acc: 0.9344\n",
      "Epoch 158/300\n",
      "717/717 [==============================] - 0s 180us/step - loss: 0.2331 - acc: 0.9344\n",
      "Epoch 159/300\n",
      "717/717 [==============================] - 0s 181us/step - loss: 0.2339 - acc: 0.9344 0s - loss: 0.2454 - acc: 0.929\n",
      "Epoch 160/300\n",
      "717/717 [==============================] - 0s 190us/step - loss: 0.2293 - acc: 0.9344\n",
      "Epoch 161/300\n",
      "717/717 [==============================] - 0s 181us/step - loss: 0.2311 - acc: 0.9344\n",
      "Epoch 162/300\n",
      "717/717 [==============================] - 0s 176us/step - loss: 0.2312 - acc: 0.9344\n",
      "Epoch 163/300\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "717/717 [==============================] - 0s 181us/step - loss: 0.2294 - acc: 0.9344\n",
      "Epoch 164/300\n",
      "717/717 [==============================] - 0s 187us/step - loss: 0.2313 - acc: 0.9344\n",
      "Epoch 165/300\n",
      "717/717 [==============================] - 0s 177us/step - loss: 0.2299 - acc: 0.9344\n",
      "Epoch 166/300\n",
      "717/717 [==============================] - 0s 177us/step - loss: 0.2278 - acc: 0.9344\n",
      "Epoch 167/300\n",
      "717/717 [==============================] - 0s 183us/step - loss: 0.2287 - acc: 0.9344\n",
      "Epoch 168/300\n",
      "717/717 [==============================] - 0s 183us/step - loss: 0.2297 - acc: 0.9344\n",
      "Epoch 169/300\n",
      "717/717 [==============================] - 0s 183us/step - loss: 0.2312 - acc: 0.9344\n",
      "Epoch 170/300\n",
      "717/717 [==============================] - 0s 190us/step - loss: 0.2302 - acc: 0.9344\n",
      "Epoch 171/300\n",
      "717/717 [==============================] - 0s 184us/step - loss: 0.2319 - acc: 0.9344\n",
      "Epoch 172/300\n",
      "717/717 [==============================] - 0s 177us/step - loss: 0.2279 - acc: 0.9344\n",
      "Epoch 173/300\n",
      "717/717 [==============================] - 0s 174us/step - loss: 0.2276 - acc: 0.9344\n",
      "Epoch 174/300\n",
      "717/717 [==============================] - 0s 179us/step - loss: 0.2306 - acc: 0.9344\n",
      "Epoch 175/300\n",
      "717/717 [==============================] - 0s 177us/step - loss: 0.2290 - acc: 0.9344\n",
      "Epoch 176/300\n",
      "717/717 [==============================] - 0s 190us/step - loss: 0.2308 - acc: 0.9344\n",
      "Epoch 177/300\n",
      "717/717 [==============================] - 0s 184us/step - loss: 0.2322 - acc: 0.9344\n",
      "Epoch 178/300\n",
      "717/717 [==============================] - 0s 193us/step - loss: 0.2284 - acc: 0.9344\n",
      "Epoch 179/300\n",
      "717/717 [==============================] - 0s 183us/step - loss: 0.2288 - acc: 0.9344\n",
      "Epoch 180/300\n",
      "717/717 [==============================] - 0s 177us/step - loss: 0.2284 - acc: 0.9344\n",
      "Epoch 181/300\n",
      "717/717 [==============================] - 0s 184us/step - loss: 0.2283 - acc: 0.9344\n",
      "Epoch 182/300\n",
      "717/717 [==============================] - 0s 183us/step - loss: 0.2298 - acc: 0.9344 0s - loss: 0.2222 - acc: 0.94\n",
      "Epoch 183/300\n",
      "717/717 [==============================] - 0s 174us/step - loss: 0.2280 - acc: 0.9344\n",
      "Epoch 184/300\n",
      "717/717 [==============================] - 0s 201us/step - loss: 0.2290 - acc: 0.9344\n",
      "Epoch 185/300\n",
      "717/717 [==============================] - 0s 207us/step - loss: 0.2292 - acc: 0.9344\n",
      "Epoch 186/300\n",
      "717/717 [==============================] - 0s 211us/step - loss: 0.2280 - acc: 0.9344\n",
      "Epoch 187/300\n",
      "717/717 [==============================] - 0s 202us/step - loss: 0.2286 - acc: 0.9344\n",
      "Epoch 188/300\n",
      "717/717 [==============================] - 0s 200us/step - loss: 0.2289 - acc: 0.9344\n",
      "Epoch 189/300\n",
      "717/717 [==============================] - 0s 202us/step - loss: 0.2299 - acc: 0.9344\n",
      "Epoch 190/300\n",
      "717/717 [==============================] - 0s 198us/step - loss: 0.2296 - acc: 0.9344\n",
      "Epoch 191/300\n",
      "717/717 [==============================] - 0s 214us/step - loss: 0.2283 - acc: 0.9344\n",
      "Epoch 192/300\n",
      "717/717 [==============================] - 0s 227us/step - loss: 0.2301 - acc: 0.9344\n",
      "Epoch 193/300\n",
      "717/717 [==============================] - 0s 208us/step - loss: 0.2270 - acc: 0.9344\n",
      "Epoch 194/300\n",
      "717/717 [==============================] - 0s 214us/step - loss: 0.2284 - acc: 0.9344\n",
      "Epoch 195/300\n",
      "717/717 [==============================] - 0s 202us/step - loss: 0.2296 - acc: 0.9344\n",
      "Epoch 196/300\n",
      "717/717 [==============================] - 0s 194us/step - loss: 0.2282 - acc: 0.9344\n",
      "Epoch 197/300\n",
      "717/717 [==============================] - 0s 204us/step - loss: 0.2287 - acc: 0.9344\n",
      "Epoch 198/300\n",
      "717/717 [==============================] - 0s 197us/step - loss: 0.2304 - acc: 0.9344\n",
      "Epoch 199/300\n",
      "717/717 [==============================] - 0s 188us/step - loss: 0.2294 - acc: 0.9344\n",
      "Epoch 200/300\n",
      "717/717 [==============================] - 0s 190us/step - loss: 0.2297 - acc: 0.9344 0s - loss: 0.2149 - acc: 0.940\n",
      "Epoch 201/300\n",
      "717/717 [==============================] - 0s 194us/step - loss: 0.2324 - acc: 0.9344\n",
      "Epoch 202/300\n",
      "717/717 [==============================] - 0s 202us/step - loss: 0.2296 - acc: 0.9344\n",
      "Epoch 203/300\n",
      "717/717 [==============================] - 0s 190us/step - loss: 0.2291 - acc: 0.9344\n",
      "Epoch 204/300\n",
      "717/717 [==============================] - 0s 188us/step - loss: 0.2276 - acc: 0.9344\n",
      "Epoch 205/300\n",
      "717/717 [==============================] - 0s 195us/step - loss: 0.2283 - acc: 0.9344\n",
      "Epoch 206/300\n",
      "717/717 [==============================] - 0s 190us/step - loss: 0.2293 - acc: 0.9344\n",
      "Epoch 207/300\n",
      "717/717 [==============================] - 0s 186us/step - loss: 0.2267 - acc: 0.9344\n",
      "Epoch 208/300\n",
      "717/717 [==============================] - 0s 197us/step - loss: 0.2296 - acc: 0.9344\n",
      "Epoch 209/300\n",
      "717/717 [==============================] - 0s 190us/step - loss: 0.2287 - acc: 0.9344\n",
      "Epoch 210/300\n",
      "717/717 [==============================] - 0s 190us/step - loss: 0.2326 - acc: 0.9344\n",
      "Epoch 211/300\n",
      "717/717 [==============================] - 0s 188us/step - loss: 0.2319 - acc: 0.9344\n",
      "Epoch 212/300\n",
      "717/717 [==============================] - 0s 194us/step - loss: 0.2283 - acc: 0.9344\n",
      "Epoch 213/300\n",
      "717/717 [==============================] - 0s 191us/step - loss: 0.2320 - acc: 0.9344\n",
      "Epoch 214/300\n",
      "717/717 [==============================] - 0s 190us/step - loss: 0.2277 - acc: 0.9344\n",
      "Epoch 215/300\n",
      "717/717 [==============================] - 0s 186us/step - loss: 0.2312 - acc: 0.9344\n",
      "Epoch 216/300\n",
      "717/717 [==============================] - 0s 188us/step - loss: 0.2299 - acc: 0.9344\n",
      "Epoch 217/300\n",
      "717/717 [==============================] - 0s 193us/step - loss: 0.2276 - acc: 0.9344\n",
      "Epoch 218/300\n",
      "717/717 [==============================] - 0s 183us/step - loss: 0.2295 - acc: 0.9344\n",
      "Epoch 219/300\n",
      "717/717 [==============================] - 0s 174us/step - loss: 0.2277 - acc: 0.9344\n",
      "Epoch 220/300\n",
      "717/717 [==============================] - 0s 177us/step - loss: 0.2280 - acc: 0.9344\n",
      "Epoch 221/300\n",
      "717/717 [==============================] - 0s 194us/step - loss: 0.2285 - acc: 0.9344\n",
      "Epoch 222/300\n",
      "717/717 [==============================] - 0s 204us/step - loss: 0.2287 - acc: 0.9344\n",
      "Epoch 223/300\n",
      "717/717 [==============================] - 0s 183us/step - loss: 0.2328 - acc: 0.9344\n",
      "Epoch 224/300\n",
      "717/717 [==============================] - 0s 179us/step - loss: 0.2287 - acc: 0.9344\n",
      "Epoch 225/300\n",
      "717/717 [==============================] - 0s 172us/step - loss: 0.2306 - acc: 0.9344\n",
      "Epoch 226/300\n",
      "717/717 [==============================] - 0s 184us/step - loss: 0.2287 - acc: 0.9344\n",
      "Epoch 227/300\n",
      "717/717 [==============================] - 0s 191us/step - loss: 0.2295 - acc: 0.9344\n",
      "Epoch 228/300\n",
      "717/717 [==============================] - 0s 183us/step - loss: 0.2291 - acc: 0.9344\n",
      "Epoch 229/300\n",
      "717/717 [==============================] - 0s 179us/step - loss: 0.2282 - acc: 0.9344\n",
      "Epoch 230/300\n",
      "717/717 [==============================] - 0s 191us/step - loss: 0.2276 - acc: 0.9344\n",
      "Epoch 231/300\n",
      "717/717 [==============================] - 0s 188us/step - loss: 0.2269 - acc: 0.9344\n",
      "Epoch 232/300\n",
      "717/717 [==============================] - 0s 205us/step - loss: 0.2279 - acc: 0.9344\n",
      "Epoch 233/300\n",
      "717/717 [==============================] - 0s 190us/step - loss: 0.2273 - acc: 0.9344\n",
      "Epoch 234/300\n",
      "717/717 [==============================] - 0s 184us/step - loss: 0.2292 - acc: 0.9344\n",
      "Epoch 235/300\n",
      "717/717 [==============================] - 0s 190us/step - loss: 0.2275 - acc: 0.9344\n",
      "Epoch 236/300\n",
      "717/717 [==============================] - 0s 180us/step - loss: 0.2284 - acc: 0.9344\n",
      "Epoch 237/300\n",
      "717/717 [==============================] - 0s 184us/step - loss: 0.2282 - acc: 0.9344\n",
      "Epoch 238/300\n",
      "717/717 [==============================] - 0s 180us/step - loss: 0.2345 - acc: 0.9344\n",
      "Epoch 239/300\n",
      "717/717 [==============================] - 0s 186us/step - loss: 0.2287 - acc: 0.9344\n",
      "Epoch 240/300\n",
      "717/717 [==============================] - 0s 193us/step - loss: 0.2286 - acc: 0.9344\n",
      "Epoch 241/300\n",
      "717/717 [==============================] - 0s 191us/step - loss: 0.2280 - acc: 0.9344\n",
      "Epoch 242/300\n",
      "717/717 [==============================] - 0s 184us/step - loss: 0.2337 - acc: 0.9344\n",
      "Epoch 243/300\n",
      "717/717 [==============================] - 0s 188us/step - loss: 0.2295 - acc: 0.9344\n",
      "Epoch 244/300\n",
      "717/717 [==============================] - 0s 181us/step - loss: 0.2313 - acc: 0.9344\n",
      "Epoch 245/300\n",
      "717/717 [==============================] - 0s 184us/step - loss: 0.2267 - acc: 0.9344\n",
      "Epoch 246/300\n",
      "717/717 [==============================] - 0s 195us/step - loss: 0.2322 - acc: 0.9344\n",
      "Epoch 247/300\n",
      "717/717 [==============================] - 0s 190us/step - loss: 0.2310 - acc: 0.9344 0s - loss: 0.2376 - acc: 0.931\n",
      "Epoch 248/300\n",
      "717/717 [==============================] - 0s 202us/step - loss: 0.2317 - acc: 0.9344\n",
      "Epoch 249/300\n",
      "717/717 [==============================] - 0s 190us/step - loss: 0.2284 - acc: 0.9344\n",
      "Epoch 250/300\n",
      "717/717 [==============================] - 0s 191us/step - loss: 0.2289 - acc: 0.9344\n",
      "Epoch 251/300\n",
      "717/717 [==============================] - 0s 183us/step - loss: 0.2315 - acc: 0.9344\n",
      "Epoch 252/300\n",
      "717/717 [==============================] - 0s 186us/step - loss: 0.2274 - acc: 0.9344\n",
      "Epoch 253/300\n",
      "717/717 [==============================] - 0s 190us/step - loss: 0.2295 - acc: 0.9344 0s - loss: 0.2180 - acc: 0.936\n",
      "Epoch 254/300\n",
      "717/717 [==============================] - 0s 201us/step - loss: 0.2274 - acc: 0.9344\n",
      "Epoch 255/300\n",
      "717/717 [==============================] - 0s 194us/step - loss: 0.2272 - acc: 0.9344\n",
      "Epoch 256/300\n",
      "717/717 [==============================] - 0s 190us/step - loss: 0.2279 - acc: 0.9344\n",
      "Epoch 257/300\n",
      "717/717 [==============================] - 0s 180us/step - loss: 0.2284 - acc: 0.9344\n",
      "Epoch 258/300\n",
      "717/717 [==============================] - 0s 188us/step - loss: 0.2277 - acc: 0.9344\n",
      "Epoch 259/300\n",
      "717/717 [==============================] - 0s 419us/step - loss: 0.2279 - acc: 0.9344\n",
      "Epoch 260/300\n",
      "717/717 [==============================] - 0s 493us/step - loss: 0.2302 - acc: 0.9344\n",
      "Epoch 261/300\n",
      "717/717 [==============================] - 0s 483us/step - loss: 0.2273 - acc: 0.9344 0s - loss: 0.2227 - acc: 0.936\n",
      "Epoch 262/300\n",
      "717/717 [==============================] - 0s 497us/step - loss: 0.2273 - acc: 0.9344\n",
      "Epoch 263/300\n",
      "717/717 [==============================] - 0s 477us/step - loss: 0.2267 - acc: 0.9344\n",
      "Epoch 264/300\n",
      "717/717 [==============================] - ETA: 0s - loss: 0.2322 - acc: 0.931 - 0s 475us/step - loss: 0.2259 - acc: 0.9344\n",
      "Epoch 265/300\n",
      "717/717 [==============================] - 0s 515us/step - loss: 0.2288 - acc: 0.9344\n",
      "Epoch 266/300\n",
      "717/717 [==============================] - 0s 272us/step - loss: 0.2283 - acc: 0.9344\n",
      "Epoch 267/300\n",
      "717/717 [==============================] - 0s 186us/step - loss: 0.2281 - acc: 0.9344\n",
      "Epoch 268/300\n",
      "717/717 [==============================] - 0s 204us/step - loss: 0.2283 - acc: 0.9344\n",
      "Epoch 269/300\n",
      "717/717 [==============================] - 0s 190us/step - loss: 0.2271 - acc: 0.9344\n",
      "Epoch 270/300\n",
      "717/717 [==============================] - 0s 191us/step - loss: 0.2273 - acc: 0.9344\n",
      "Epoch 271/300\n",
      "717/717 [==============================] - 0s 197us/step - loss: 0.2289 - acc: 0.9344\n",
      "Epoch 272/300\n",
      "717/717 [==============================] - 0s 202us/step - loss: 0.2274 - acc: 0.9344\n",
      "Epoch 273/300\n",
      "717/717 [==============================] - 0s 194us/step - loss: 0.2281 - acc: 0.9344\n",
      "Epoch 274/300\n",
      "717/717 [==============================] - 0s 200us/step - loss: 0.2277 - acc: 0.9344\n",
      "Epoch 275/300\n",
      "717/717 [==============================] - 0s 195us/step - loss: 0.2280 - acc: 0.9344\n",
      "Epoch 276/300\n",
      "717/717 [==============================] - 0s 195us/step - loss: 0.2279 - acc: 0.9344\n",
      "Epoch 277/300\n",
      "717/717 [==============================] - 0s 194us/step - loss: 0.2269 - acc: 0.9344\n",
      "Epoch 278/300\n",
      "717/717 [==============================] - 0s 200us/step - loss: 0.2287 - acc: 0.9344\n",
      "Epoch 279/300\n",
      "717/717 [==============================] - 0s 198us/step - loss: 0.2277 - acc: 0.9344\n",
      "Epoch 280/300\n",
      "717/717 [==============================] - 0s 193us/step - loss: 0.2349 - acc: 0.9344\n",
      "Epoch 281/300\n",
      "717/717 [==============================] - 0s 198us/step - loss: 0.2302 - acc: 0.9344\n",
      "Epoch 282/300\n",
      "717/717 [==============================] - 0s 202us/step - loss: 0.2282 - acc: 0.9344\n",
      "Epoch 283/300\n",
      "717/717 [==============================] - 0s 197us/step - loss: 0.2284 - acc: 0.9344\n",
      "Epoch 284/300\n",
      "717/717 [==============================] - 0s 194us/step - loss: 0.2268 - acc: 0.9344\n",
      "Epoch 285/300\n",
      "717/717 [==============================] - 0s 193us/step - loss: 0.2320 - acc: 0.9344\n",
      "Epoch 286/300\n",
      "717/717 [==============================] - 0s 198us/step - loss: 0.2295 - acc: 0.9344\n",
      "Epoch 287/300\n",
      "717/717 [==============================] - 0s 197us/step - loss: 0.2295 - acc: 0.9344\n",
      "Epoch 288/300\n",
      "717/717 [==============================] - 0s 232us/step - loss: 0.2312 - acc: 0.9344\n",
      "Epoch 289/300\n",
      "717/717 [==============================] - 0s 214us/step - loss: 0.2284 - acc: 0.9344\n",
      "Epoch 290/300\n",
      "717/717 [==============================] - 0s 215us/step - loss: 0.2298 - acc: 0.9344\n",
      "Epoch 291/300\n",
      "717/717 [==============================] - 0s 215us/step - loss: 0.2277 - acc: 0.9344\n",
      "Epoch 292/300\n",
      "717/717 [==============================] - 0s 215us/step - loss: 0.2278 - acc: 0.9344\n",
      "Epoch 293/300\n",
      "717/717 [==============================] - 0s 324us/step - loss: 0.2304 - acc: 0.9344\n",
      "Epoch 294/300\n",
      "717/717 [==============================] - 0s 550us/step - loss: 0.2274 - acc: 0.9344\n",
      "Epoch 295/300\n",
      "717/717 [==============================] - 0s 550us/step - loss: 0.2321 - acc: 0.9344\n",
      "Epoch 296/300\n",
      "717/717 [==============================] - 0s 561us/step - loss: 0.2312 - acc: 0.9344\n",
      "Epoch 297/300\n",
      "717/717 [==============================] - 0s 555us/step - loss: 0.2270 - acc: 0.9344\n",
      "Epoch 298/300\n",
      "717/717 [==============================] - 0s 561us/step - loss: 0.2299 - acc: 0.9344\n",
      "Epoch 299/300\n",
      "717/717 [==============================] - 0s 574us/step - loss: 0.2291 - acc: 0.9344\n",
      "Epoch 300/300\n",
      "717/717 [==============================] - 0s 533us/step - loss: 0.2315 - acc: 0.9344\n",
      "717/717 [==============================] - 0s 260us/step\n",
      "[0.2259737330916204, 0.93444909352804]\n"
     ]
    }
   ],
   "source": [
    "for i in range(1):\n",
    "    x, x_test, y, y_test = train_test_split(df_train,df_test,test_size=0.2,train_size=0.8)\n",
    "    classifier.compile(optimizer ='adam',loss='binary_crossentropy', metrics =['accuracy'])\n",
    "    classifier.fit(x,y, batch_size=10, epochs=300)\n",
    "    eval_model=classifier.evaluate(x, y)\n",
    "    print(eval_model)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[  5   8]\n",
      " [  2 165]]\n"
     ]
    }
   ],
   "source": [
    "y_pred=clf.predict(x_test)\n",
    "from sklearn.metrics import confusion_matrix\n",
    "cm = confusion_matrix(y_test, y_pred)\n",
    "print(cm)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
