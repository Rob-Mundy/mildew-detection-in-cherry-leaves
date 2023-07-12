import streamlit as st
import matplotlib.pyplot as plt


def page_project_hypothesis_body():
    st.write("### Project Hypothesis and Validation")

    st.success(
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
