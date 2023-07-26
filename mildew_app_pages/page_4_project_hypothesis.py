import streamlit as st
import matplotlib.pyplot as plt


def page_project_hypothesis_body():
    st.write("### Project Hypothesis and Validation")

    st.info(
        f"* We suspect that leaves affected by mildew display identifiable "
        f"traits, typically in the form of white, powdery patches of fungus "
        f"that spread on either the upper or lower surfaces of the leaf. These"
        f" distinct indicators will be adequate for training a machine "
        f"learning model as they effectively distinguish between infected "
        f"leaves and those that are fungus-free.\n"
        f"* Conducting an average image analysis can assist in further "
        f"investigating the matter.\n"
        f"* We propose that employing binary classification would be the most "
        f"suitable approach for discerning the distinction between infected "
        f"and healthy leaves.\n\n"
    )

    st.success(
        f"* Business Requirement 1: The client is interested in conducting a "
        f"study to visually differentiate a healthy cherry leaf from one with "
        f"powdery mildew.\n"
        f'  - "Mean" and "standard deviation" images will be displayed for '
        f"healthy leaves and those presenting powdery mildew.\n"
        f"  - The difference between an average healthy leaf and the average "
        f" mildew-infected leaf will be displayed.\n"
        f"  - An image montgage will follow for the selected label: healthy / "
        f" powdery_mildew.\n\n"
        f"* Business Requirement 2: The client is interested in predicting if a"
        f" cherry leaf is healthy or contains powdery mildew.\n"
        f"  - We want to predict whether a random sample leaf image is "
        f" presenting powdery mildew or is healthy.\n"
        f"  - We want to build a ML model with binary classification and "
        f" report on the results.\n\n"
    )
