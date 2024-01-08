import pickle #untuk me load data pickle
import streamlit as st

#membaca model
kelulusan_model = pickle.load(open('prediksi_model_project.sav', 'rb'))

#judul web
st.title('Prediksi Kelulusan Interview Kerja')

#mendeklarasikan inputan
years_of_experience = st.text_input('Input years of experience')

functional_competency_score = st.text_input('Input functional competency score')

top1_skills_score = st.text_input('Input top 1 skills score')

top2_skills_score = st.text_input('Input top 2 skills score')

top3_skills_score = st.text_input('Input top 3 skills score')

behavior_competency_score = st.text_input('Input behavior competency score')

top1_behavior_skill_score = st.text_input('Input top 1 behavior skill score')

top2_behavior_skill_score = st.text_input('Input top 2 behavior skill score')

top3_behavior_skill_score = st.text_input('Input top 3 behavior skill score')

#code untuk prediksi
kelulusan_prediksi = ''

#membuat tombol untuk prediksi
if st.button('Test Prediksi Kelulusan') :
    kelulusan_predicion = kelulusan_model.predict([[years_of_experience, functional_competency_score, top1_skills_score, top2_skills_score, top3_skills_score, behavior_competency_score, top1_behavior_skill_score, top2_behavior_skill_score, top3_behavior_skill_score]])

    if(kelulusan_predicion[0] == 1):
        kelulusan_prediksi = 'Anda lulus interview'
    else :
        kelulusan_prediksi = 'Anda tidak lulus interview'
    st.success(kelulusan_prediksi)
    





