import streamlit as st
import pandas as pd
from resume_parser import parse_resume
from utils import extract_text_from_pdf
from match_score import calculate_similarity

st.title("AI-Powered Resume Screening Tool")

job_desc = st.text_area("Enter Job Description")

uploaded_files = st.file_uploader("Upload Resumes (PDF)", type=["pdf"], accept_multiple_files=True)

if st.button("Rank Candidates") and uploaded_files:
    resumes = []
    names = []
    for file in uploaded_files:
        name = file.name
        text = extract_text_from_pdf(file)
        parsed = parse_resume(text)
        resumes.append(parsed)
        names.append(name)

    scores = calculate_similarity(resumes, job_desc)
    results = pd.DataFrame({"Candidate": names, "Score": scores})
    results = results.sort_values("Score", ascending=False).reset_index(drop=True)

    st.subheader("Ranked Candidates")
    st.dataframe(results)
    st.download_button("Download Results as CSV", results.to_csv(index=False), "results.csv", "text/csv")
