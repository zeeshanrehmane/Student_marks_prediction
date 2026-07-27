import streamlit as st
import joblib
import numpy as np

# Page Configuration
st.set_page_config(
    page_title="Student Marks Predictor",
    page_icon="🎓",
    layout="wide"
)

# Load Model
model = joblib.load("student_marks_prediction_model.pkl")

# Custom CSS
st.markdown("""
<style>

.stApp{
background: linear-gradient(135deg,#0f2027,#203a43,#2c5364);
}

.title{
font-size:55px;
font-weight:bold;
text-align:center;
color:white;
}

.sub{
text-align:center;
font-size:20px;
color:#dddddd;
margin-bottom:30px;
}

.box{
background:rgba(255,255,255,0.12);
padding:30px;
border-radius:20px;
backdrop-filter:blur(20px);
box-shadow:0px 0px 30px rgba(0,255,255,.4);
}

.result{
background:linear-gradient(90deg,#00c6ff,#0072ff);
padding:25px;
border-radius:20px;
font-size:35px;
text-align:center;
font-weight:bold;
color:white;
box-shadow:0px 0px 20px cyan;
}

.footer{
text-align:center;
color:white;
margin-top:50px;
font-size:18px;
}

</style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>🎓 Student Marks Prediction</div>", unsafe_allow_html=True)
st.markdown("<div class='sub'>Predict Student Marks using Machine Learning</div>", unsafe_allow_html=True)

st.markdown("<div class='box'>", unsafe_allow_html=True)

col1,col2=st.columns(2)

with col1:
    number_courses=st.slider(
        "📚 Number of Courses",
        1,
        10,
        5
    )

with col2:
    time_study=st.slider(
        "⏳ Study Time (Hours)",
        0.0,
        10.0,
        5.0
    )

st.markdown("")

if st.button("🚀 Predict Marks",use_container_width=True):

    prediction=model.predict([[number_courses,time_study]])[0]

    prediction=max(0,min(100,prediction))

    st.progress(int(prediction))

    st.balloons()

    st.markdown(
        f"""
        <div class='result'>
        🎯 Predicted Marks<br><br>
        {prediction:.2f} %
        </div>
        """,
        unsafe_allow_html=True
    )

    if prediction>=90:
        st.success("🌟 Excellent Performance!")
    elif prediction>=75:
        st.info("😊 Very Good!")
    elif prediction>=60:
        st.warning("🙂 Good, Keep Improving!")
    else:
        st.error("📖 Need More Practice!")

st.markdown("</div>", unsafe_allow_html=True)

st.markdown(
"""
<div class='footer'>
Made with ❤️ using Python | Streamlit | Machine Learning 
</div>
""",
unsafe_allow_html=True
)