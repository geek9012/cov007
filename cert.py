import streamlit as st
import fitz
import cv2 as cv
import os
import base64


    
st.header('Customize your COVID certificate')    

st.file_uploader("Upload Covid certificate...", type="pdf")
doc = fitz.open('certificate.pdf')
    
