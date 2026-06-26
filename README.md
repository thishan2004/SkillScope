# SkillScope: Data Science Job Market Analytics & Career Recommendation System

## Live Demo

https://skillscope-fhuwyzjefjjsd5ghvf63xf.streamlit.app

## Tableau Dashboard

Explore an interactive Tableau dashboard that visualizes current trends in the Data Science job market.

🔗 Tableau Public:
https://public.tableau.com/app/profile/thishanujan.kugathasan/viz/SkillScope_Dashboard/DataScienceJobMarketDashboard?publish=yes

## Overview

SkillScope is an end-to-end Data Science project that helps aspiring data professionals understand current job market trends, identify skill gaps, evaluate employability, and discover suitable career paths.

The system analyzes over **1,300 Data Science-related job postings** extracted from a large LinkedIn job dataset and provides actionable insights through an interactive Streamlit dashboard.

---

## Problem Statement

Many students and aspiring professionals struggle to answer questions such as:

* Which skills are currently in demand?
* Which Data Science role best matches my skills?
* What skills should I learn to improve my employability?

SkillScope addresses these challenges by combining job market analytics with personalized career guidance.

---

## Dataset

**Source:** LinkedIn Data Science Jobs Dataset (2023–2024)

https://www.kaggle.com/datasets/muqaddasejaz/linkedin-data-science-jobs-dataset

### Original Dataset

* 123,849 Job Postings

### Filtered Dataset

* 1,307 Data Science-related Job Postings

### Target Roles

* Data Scientist
* Data Analyst
* Data Engineer
* Machine Learning Engineer
* Business Intelligence Analyst
* AI Engineer

---

## Key Features

### 1. Data Science Job Market Analytics

* Analyze Data Science job postings
* Identify popular job roles
* Explore experience-level requirements
* Examine work-type distribution
* Discover industry hiring trends

### 2. Skill Demand Analysis

Identify the most demanded skills in the Data Science job market.

#### Top Skills Identified

* SQL
* Python
* Machine Learning
* AWS
* Statistics
* Azure
* ETL
* Spark
* Tableau
* Excel

### 3. Employability Score Calculator

Users can select their existing skills and compare them against current market demand.

#### Outputs

* Employability Score
* Matched Skills
* Missing Skills
* Skill Gap Analysis

### 4. Career Recommendation Engine

Recommends suitable Data Science career paths based on a user's current skill set.

#### Supported Career Paths

* Data Analyst
* Data Scientist
* Data Engineer
* Machine Learning Engineer
* BI Analyst

---

## Key Insights from the Analysis

| Metric                      | Value          |
| --------------------------- | -------------- |
| Total Jobs Analyzed         | 1,307          |
| Most In-Demand Skill        | SQL            |
| Second Most In-Demand Skill | Python         |
| Top Cloud Skill             | AWS            |
| Top Visualization Skills    | Tableau, Excel |
| Top Data Engineering Skills | Spark, ETL     |

---

## Scoring Logic

### Employability Score Formula

Employability Score = (Matched Skills / Top Market Skills) × 100

### Example

User Skills:

* Python
* SQL
* Machine Learning

Matched Skills:

* Python
* SQL
* Machine Learning

Result:

* Employability Score = 30/100

---

## Technologies Used

### Programming

* Python

### Data Analysis

* Pandas
* NumPy

### Data Visualization

* Matplotlib
* Plotly

### Web Application

* Streamlit

### Development Tools

* Jupyter Notebook
* Visual Studio Code

### Version Control

* Git
* GitHub

---

## Project Workflow

Data Collection
→ Data Cleaning
→ Data Science Job Filtering
→ Skill Demand Analysis
→ Employability Score Calculation
→ Career Recommendation
→ Streamlit Dashboard

---

## Dashboard Screenshots

### Market Insights – Overview

![Market Insights](images/Market%20Insights%20page.png)

### Market Insights – Skills Analysis

![Market Insights 2](images/Market%20Insights%20page%202.png)

### Employability Score

![Employability Score](images/Employability%20Score%20page.png)

### Career Recommendation

![Career Recommendation](https://github.com/thishan2004/SkillScope/blob/main/images/%20career_recommendation.png)

---

## Project Structure

```text
SkillScope/
│
├── app/
│   └── app.py
│
├── data/
│   └── processed/
│
├── images/
│
├── notebooks/
│
├── requirements.txt
│
└── README.md
```

---

## How to Run

### Clone Repository

```bash
git clone https://github.com/thishan2004/SkillScope.git
cd SkillScope
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app/app.py
```

---

## Limitations

* Uses a global LinkedIn dataset rather than Sri Lankan job data.
* Career recommendations are rule-based.
* Skill extraction is dictionary-based.
* Does not currently include salary prediction.

---

## Future Enhancements

* Sri Lankan Data Science Job Market Analysis
* Salary Trend Analysis
* Learning Roadmap Generator
* Resume Skill Matching
* NLP-Based Skill Extraction
* Machine Learning-Based Career Recommendation
* Real-Time Job Market Updates

---

## Author

### Kugathasan Thishanujan

BSc (Hons) Information Technology
Specialization in Data Science
Sri Lanka Institute of Information Technology (SLIIT)

📧 Email: [thishan2004@gmail.com](mailto:thishan2004@gmail.com)

🔗 LinkedIn: https://www.linkedin.com/in/thishanujan-kugathasan-7282b9311/

💼 Open to Data Science Internship Opportunities
