import streamlit as st
from mildew_app_pages.multi_page import MultiPage

# load page scripts
# from app_pages.page_executive_summary import page_executive_summary_body
from mildew_app_pages.page_leaf_health_visualiser import page_leaf_health_visualiser_body

app = MultiPage(app_name="Mildew Detector")  # Create an instance of the app

# Add app pages using .add_page()
# app.add_page("Executive Summary", page_summary_body)
app.add_page("Leaf Health Visualiser", page_leaf_health_visualiser_body)

app.run()  # Run the  app
