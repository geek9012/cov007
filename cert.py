import streamlit as st
import fitz
import cv2 as cv
import os
import base64

def get_binary_file_downloader_html(bin_file, file_label='File'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}">Download {file_label}</a>'
    return href
    
st.header('Customize your COVID certificate')    

if st.file_uploader("Upload Covid certificate...", type="pdf"):
    doc = fitz.open('certificate.pdf')
    page = doc.loadPage(0)  # number of page
    pix = page.getPixmap()
    output = "outfile.png"
    pix.writePNG(output)
    l_img = cv.imread(output)
    s_img = cv.imread("pik.png")
    s_img = cv.cvtColor(s_img, cv.COLOR_BGR2RGB)
    x_offset = 10
    y_offset = 560
    l_img[y_offset:y_offset+s_img.shape[0], x_offset:x_offset+s_img.shape[1]] = s_img

    #st.markdown(get_binary_file_downloader_html(l_img, 'Picture'), unsafe_allow_html=True)
    st.image(l_img, width=None)