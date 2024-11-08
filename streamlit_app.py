import streamlit as st
import pandas as pd

# 타이틀 설정
st.title("Streamlit 내가 만드는 서비스")

# 서브타이틀
st.subheader("잘 해보자")

# 표 데이터 생성
data = {
    '이름': ['곽두팔', '김두식', '이헌식'],
    '나이': [25, 30, 22],
    '직업': ['건달아님', '평범한 인간', '셰프']
}
df = pd.DataFrame(data)

# 표 출력
st.write("걍 해:")
st.dataframe(df)

# HTML 메시지 출력
st.markdown("""
    <div style="background-color: lightblue; padding: 10px;">
        <h3>HTML 스타일링 메시지</h3>
        <p>Streamlit에서는 Markdown을 사용하여 HTML 태그를 삽입하고 스타일을 지정할 수 있습니다.</p>
    </div>
""", unsafe_allow_html=True)

# 추가적인 텍스트
st.write("Streamlit을 활용한 빠른 웹 애플리케이션 개발!")
