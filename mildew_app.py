import streamlit as st
from mildew_app_pages.multi_page import MultiPage

# load page scripts
from mildew_app_pages.page_1_executive_summary import page_executive_summary_body
from mildew_app_pages.page_2_leaf_health_visualiser import page_leaf_health_visualiser_body
from mildew_app_pages.page_3_mildew_detector import page_mildew_detector_body
from mildew_app_pages.page_4_project_hypothesis import page_project_hypothesis_body
from mildew_app_pages.page_5_ml_performance_metrics import page_ml_performance_metrics_body


# Create app instance
app = MultiPage(app_name="Mildew Detector")

# Add app pages using .add_page()
app.add_page("Executive Summary", page_executive_summary_body)
app.add_page("Leaf Health Visualiser", page_leaf_health_visualiser_body)
app.add_page("Mildew Detector", page_mildew_detector_body)
app.add_page("Project Hypothesis and Validation", page_project_hypothesis_body)
app.add_page("ML Performance Metrics", page_ml_performance_metrics_body)


# Run app
app.run()
