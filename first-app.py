# streamlit_app.py

import streamlit as st
import sqlite3

st.write("Olá!")

conn = sqlite3.connect("data.db")
c = conn.cursor()


