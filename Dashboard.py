import streamlit as st

st.set_page_config(
    page_title="PROHI Dashboard",
    page_icon="👋",
)

# Sidebar configuration
st.sidebar.image("./assets/project-logo.jpg",)
st.sidebar.success("Select a tab above.")

# # Page information

st.write("# Welcome to PROHI Dashboard! 👋")

st.markdown(
"""
    ## Aims

    After completing the course the student should be able to:
    - explain basic project management methods
    - be able to account for success factors in Health Informatics projects
    - understand basic methods and tools in the field of data science and machine learning
    - explain process models for data mining projects
    - explain the difference between rule-based methods and machine learning methods
    - apply basic project management methods
    - work in an international multidisciplinary project group
    - independently lead and implement a limited project in health informatics - document the steps in the design of a prototype for a health informatics project
    - apply the steps in a process model for data mining projects
    - apply methods from the field of text mining on different types of health informatics problems
    - explain and argue for their positions regarding the implementation of a health informatics project
    - explain how to work with sensitive health information in a safe and ethical way.

"""
)

# You can also add text right into the web as long comments (""")
"""
The final project aims to apply data science concepts and skills on a 
medical case study that you and your team select from a public data source.
The project assumes that you bring the technical Python skills from 
previous courses (*DSHI*: Data Science for Health Informatics), as well as 
the analytical skills to argue how and why specific techniques could
enhance the problem domain related to the selected dataset.
"""

### UNCOMMENT THE CODE BELOW TO SEE EXAMPLE OF INPUT WIDGETS

# Dashboard.py

import pandas as pd
import numpy as np

st.set_page_config(page_title="Stroke App", layout="wide")

page = st.sidebar.radio("Go to", ["Dashboard", "About"], index=0)


if page == "Dashboard":
    st.title("Stroke Prediction Dashboard")
    st.caption("Three example widgets from the stroke dataset schema, plus a synthetic table and chart (no CSV loading).")

    gender = st.sidebar.selectbox("Gender", options=["Male", "Female", "Other"])  # "gender"
    age_range = st.sidebar.slider("Age range", min_value=0, max_value=100, value=(25, 75))  # "age"
    work_types = st.sidebar.multiselect(
        "Work type",
        options=["Private", "Self-employed", "Govt_job", "children", "Never_worked"]  # "work_type"
    )

    with st.expander("Current selections (non-functional preview)"):
        st.write({"gender": gender, "age_range": age_range, "work_type": work_types})

    n = 50
    rng = np.random.default_rng(42)
    synthetic_df = pd.DataFrame({
        "age": rng.integers(0, 100, size=n),
        "avg_glucose_level": np.clip(rng.normal(110, 35, size=n), 50, 300).round(2),
        "bmi": np.clip(rng.normal(28, 6, size=n), 10, 60).round(1),
        "smoking_status": rng.choice(["formerly smoked", "never smoked", "smokes", "Unknown"], size=n),
        "stroke": rng.integers(0, 2, size=n)
    })

    left, right = st.columns([1.2, 1])
    with left:
        st.subheader("Sample data")
        st.dataframe(synthetic_df, use_container_width=True)

    with right:
        st.subheader("Simple chart")
        chart_data = pd.DataFrame(
            {
                "Series A": rng.normal(0, 1, size=30).cumsum(),
                "Series B": rng.normal(0, 1, size=30).cumsum(),
                "Series C": rng.normal(0, 1, size=30).cumsum(),
            }
        )
        st.line_chart(chart_data, use_container_width=True)

    st.info("Note: Widgets are illustrative only; no dataset is loaded and no filtering or modeling is performed.")

else:
    st.title("Md_Imran_Mansur")

st.markdown("""
### Project summary

My project analyzes the Stroke Prediction dataset to characterize risk factors and develop a binary classifier for stroke occurrence. 
The dataset includes 5,110 patient records with 12 features spanning demographics, comorbidities, lifestyle, and clinical measures. 
Key numerical variables are age, average glucose level, and BMI; categorical variables include gender, ever_married, work_type, Residence_type, and smoking_status; and binary indicators cover hypertension, heart_disease, and stroke.
The workflow encompassed data understanding, imputing missing BMI values, encoding categorical features, and cross-validated model selection. Multiple algorithms were benchmarked on the imbalanced target using F1 as the primary metric. 
The best-performing model, a GradientBoostingClassifier with 200 estimators and learning_rate=0.05, achieved the highest cross-validated F1, balancing precision and recall.

""")


