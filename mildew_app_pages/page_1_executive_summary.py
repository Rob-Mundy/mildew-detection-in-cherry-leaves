import streamlit as st
import matplotlib.pyplot as plt


def page_executive_summary_body():
    """
    Executive Summary
    """
    st.write("### Project Executive Summary")

    st.info(
        f"**General Information**\n"
        f"* According to [The Royal Horticultural Society](https://www.rhs.org.uk/disease/powdery-mildews)"
        f", powdery mildews are a group of related fungi which attack a wide range"
        f" of plants, causing a white, dusty coating on leaves, stems and flowers.\n"
        f"* The fungus sends feeding structures into the surface cells, greatly"
        f" reducing the vigour of the plant.\n "
        f"* If left unchecked, the fungus often spreads to a plant's fruits, "
        f"compromising the quality. \n"
        f"* Manual observations and visual verifications are currently required"
        f", taking an average of 30 mins per tree.\n\n"
        f"**Project Dataset**\n"
        f"* The [available dataset](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves) "
        f"contains 4208 images provided by the client from their manual "
        f"observations, with equal quantities of both healthy and "
        f"mildew-infected leaves.\n")

    st.write(
        f"* For additional information, please read the corresponding "
        f"[Project README file](https://github.com/Rob-Mundy/mildew-detection-in-cherry-leaves/blob/main/README.md).")

    st.success(
        f"**The project has 2 business requirements:**\n"
        f"* 1 - The client is interested in conducting a study to visually "
        f"differentiate a healthy cherry leaf from one with powdery mildew.\n"
        f"* 2 - The client is interested in predicting if a cherry leaf is "
        f"healthy or contains powdery mildew. "
    )
