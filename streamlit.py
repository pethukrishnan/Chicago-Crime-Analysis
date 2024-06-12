import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# data = pd.read_csv(r'C:\Users\kpaps\Desktop\Chicago_Crime\Crimes_-_2001_to_Present\Crimes_-_2001_to_Present.csv')
data = pd.read_csv(r'C:\Users\kpaps\Desktop\Chicago_Crime\file.csv')

st.header('Chicago Crime Analysis')

data.Date = pd.to_datetime(data.Date,)
data.index = pd.DatetimeIndex(data.Date)

Crime_Data_district = data.pivot_table('Arrest', aggfunc = np.sum, columns = ['District'], 
                                         index = data.index.date, fill_value = 0)
Crime_Data_ward = data.pivot_table('Arrest', aggfunc = np.sum, columns = ['Ward'], 
                                         index = data.index.date, fill_value = 0)
Crime_Data_ca = data.pivot_table('Arrest', aggfunc = np.sum, columns = ['Community Area'], 
                                         index = data.index.date, fill_value = 0)


A_R_D = (Crime_Data_district.sum() / data.groupby(data['District']).size())*100
A_R_W = (Crime_Data_ward.sum() / data.groupby(data['Ward']).size())*100
A_R_CA = (Crime_Data_ca.sum() / data.groupby(data['Community Area']).size())*100

arrest_per_year = data.groupby('Year')['Arrest'].value_counts().rename('Counts').to_frame()
arrest_per_year['Percentage'] = (100 * arrest_per_year / arrest_per_year.groupby(level=0).sum())
arrest_per_year.reset_index(level=[1],inplace=True)

loc_des = data['Location Description'].value_counts().reset_index().head(20)
loc_des.columns = ['Location', 'Count']

top_20_primary_type = data['Primary Type'].value_counts().head(20)
top_20_primary_type.reset_index()

domestic = data.Domestic.value_counts().reset_index()

type_arrests = data.groupby(['Primary Type'])['Arrest'].mean().sort_values(ascending=False).reset_index()
type_arrests.columns = ["Type", "Arrest Rate"]

#converting Arrest Rate column to percentage
type_arrests['Arrest Rate'] *= 100

type_arrests.head(10)



# st.subheader('Crime Type Analysis')
Crime_type = px.bar(data_frame=top_20_primary_type,x='count',color_discrete_sequence=px.colors.sequential.Cividis,title = "Top 20 Crimes")
st.plotly_chart(Crime_type)

crime_location = px.bar(loc_des,x='Count',y='Location',color_discrete_sequence=px.colors.sequential.Aggrnyl,title = "Top 20 Crimes Occured Location")
st.plotly_chart(crime_location)


st.write("-----------------------------------------------------------------------------------------------------------------------")


st.subheader('Temporal Analysis')
col1,col2= st.columns(2)
with col1:
    crime_per_year = px.line(data.groupby([data.index.year]).size(),labels={'Date':'Year'},title="Crimes Per Year")
    st.plotly_chart(crime_per_year)

with col2:
    crime_per_month = px.line(data.groupby([data.index.month]).size(),labels={'Date':'Month'},title="Crimes Per Month")
    st.plotly_chart(crime_per_month)

col3,col4 = st.columns(2)
with col3:
    crime_per_day = px.bar(data.groupby([data.index.day]).size(),labels={'Date':'Date'},color_discrete_sequence=['red'],
                           title="Crimes Per Day")
    st.plotly_chart(crime_per_day)
with col4:
    crime_per_hour = px.bar(data.groupby([data.index.hour]).size(),labels={'Date':'Hour'},color_discrete_sequence=['orange'],
                            title="Crimes Per Hour")
    st.plotly_chart(crime_per_hour)

st.write("-----------------------------------------------------------------------------------------------------------------------")

st.subheader('Crime Analysis')
col1,col2 = st.columns(2)
with col1:
    district_Cr = px.bar(data.groupby(data['District']).size(),color_discrete_sequence=['purple'],title="District wise Crimes")
    st.plotly_chart(district_Cr)
with col2:
    arrest_rate_district = px.bar(A_R_D,color_discrete_sequence=px.colors.sequential.Bluered_r,title="District wise Arrest Rate")
    arrest_rate_district.update_layout(yaxis_ticksuffix="%")
    st.plotly_chart(arrest_rate_district)

col3,col4 = st.columns(2)
with col3:
    ward_Cr = px.bar(data.groupby(data['Ward']).size(),color_discrete_sequence= px.colors.sequential.GnBu_r,title="Ward wise Crimes")
    st.plotly_chart(ward_Cr)
with col4:
    arrest_rate_ward = px.bar(A_R_W,color_discrete_sequence=px.colors.sequential.Aggrnyl,title="Ward wise Arrest Rate")
    arrest_rate_ward.update_layout(yaxis_ticksuffix="%")
    st.plotly_chart(arrest_rate_ward)

col5,col6 = st.columns(2)
with col5:
    Community_Area_Cr = px.bar(data.groupby(data['Community Area']).size(),color_discrete_sequence=px.colors.sequential.Rainbow,title="Community Area wise Crimes")
    st.plotly_chart(Community_Area_Cr)
with col6:
    arrest_rate_community_area = px.bar(A_R_CA,color_discrete_sequence= px.colors.sequential.haline_r,title="Community Area Arrest Rate")
    arrest_rate_community_area.update_layout(yaxis_ticksuffix="%")
    st.plotly_chart(arrest_rate_community_area)

st.write("-----------------------------------------------------------------------------------------------------------------------")

st.subheader('Arrest Analysis')

col1,col2 = st.columns(2)
with col1:
    Arrest_rate = px.pie(data_frame=data,names='Arrest',hole=0.5,title="Arrest Rate")
    st.plotly_chart(Arrest_rate)
with col2:
    domestic_crime = px.pie(domestic,values='count',names='Domestic',hole=0.5,title="Crime Occured  Domestic vs Non-Domestic"
                            ,color_discrete_sequence= px.colors.sequential.haline)
    st.plotly_chart(domestic_crime)

line_plot = arrest_per_year[arrest_per_year['Arrest'] == True]['Percentage']
plot = px.line(line_plot,title="Arrest Rate per Year")
plot.update_layout(yaxis_ticksuffix="%")
st.plotly_chart(plot)


Arrest_rate_crime_type = px.bar(type_arrests,x='Type',y='Arrest Rate',title="Arrest Rate By Primay type")
Arrest_rate_crime_type.update_layout(yaxis_ticksuffix="%")
st.plotly_chart(Arrest_rate_crime_type)



# px.bar(data_frame=top_20_primary_type,x='count',color_discrete_sequence=px.colors.sequential.Cividis)


