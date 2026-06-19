import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(
    page_title="SkillScope",
    page_icon="📊",
    layout="wide"
)

@st.cache_data
def load_data():
    ds_jobs = pd.read_csv("data/processed/ds_jobs.csv")
    skill_df = pd.read_csv("data/processed/skill_demand.csv")
    return ds_jobs, skill_df

ds_jobs, skill_df = load_data()

st.title("SkillScope")
st.subheader("Data Science Job Market Analytics & Career Recommendation System")

tabs = st.tabs([
    "📊 Market Insights",
    "🎯 Employability Score",
    "🚀 Career Recommender"
])

with tabs[0]:
    st.header("Market Insights")

    st.metric("Total Data Science Jobs Analyzed", len(ds_jobs))

    fig = px.bar(
        skill_df.head(10),
        x="Skill",
        y="Count",
        title="Top Skills in Data Science Jobs"
    )
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Top Data Science Roles")
    top_roles = ds_jobs["title"].value_counts().head(10).reset_index()
    top_roles.columns = ["Role", "Count"]
    st.dataframe(top_roles)

with tabs[1]:
    st.header("Employability Score")

    top_market_skills = skill_df.head(10)["Skill"].tolist()

    user_skills = st.multiselect(
        "Select your current skills",
        options=skill_df["Skill"].tolist()
    )

    if st.button("Calculate Score"):
        matched = [skill for skill in top_market_skills if skill in user_skills]
        missing = [skill for skill in top_market_skills if skill not in user_skills]

        score = (len(matched) / len(top_market_skills)) * 100

        st.metric("Employability Score", f"{score:.2f}/100")

        st.success("Skills you already have: " + ", ".join(matched))
        st.warning("Skills to improve: " + ", ".join(missing))

with tabs[2]:
    st.header("Career Recommender")

    career_paths = {
        "Data Analyst": ["SQL", "Excel", "Power BI", "Tableau", "Statistics"],
        "Data Scientist": ["Python", "SQL", "Machine Learning", "Statistics", "Pandas"],
        "Data Engineer": ["SQL", "Python", "AWS", "Spark", "ETL"],
        "Machine Learning Engineer": ["Python", "Machine Learning", "Deep Learning", "TensorFlow", "PyTorch"],
        "BI Analyst": ["SQL", "Power BI", "Tableau", "Excel", "Statistics"]
    }

    selected_skills = st.multiselect(
        "Select your skills for career recommendation",
        options=skill_df["Skill"].tolist(),
        key="career_skills"
    )

    if st.button("Recommend Career"):
        results = []

        for role, required in career_paths.items():
            matched = [skill for skill in required if skill in selected_skills]
            missing = [skill for skill in required if skill not in selected_skills]
            score = (len(matched) / len(required)) * 100

            results.append({
                "Role": role,
                "Match Score": round(score, 2),
                "Matched Skills": ", ".join(matched),
                "Missing Skills": ", ".join(missing)
            })

        result_df = pd.DataFrame(results).sort_values(
            by="Match Score",
            ascending=False
        )

        best_role = result_df.iloc[0]

        st.success(f"Recommended Career: {best_role['Role']}")
        st.metric("Match Score", f"{best_role['Match Score']}/100")
        st.dataframe(result_df)