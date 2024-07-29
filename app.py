import streamlit as st



def main(number_class, time_class, time_break):
    for i in range(number_class):
        


st.title(":bell: 학교 종이 땡땡땡 :bell:")
st.divider()

st.subheader(":school: :orange[몇 교시까지 있나요]")

number_class=int(st.selectbox(
    "number of class",
    [1,2,3,4,5,6,7,8,9],
    label_visibility="collapsed"
    )
)

time_class=int(
    st.selectbox(
        "class time",
        [10,20,30,40,50],
        label_visibility="collapsed"
    )    
)

time_break=int(
    st.selectbox(
        "break time",
        [5,10,15,20],
        label_visibility="collapsed"
    )
)

