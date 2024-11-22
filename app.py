# 분류 모델 웹앱 만들기
import streamlit as st

# 1. 기계학습 모델 파일 로드
import jioblib
model = joblib.load('')

# 2. 모델 설명
st.title('지능형 환율 예측 에이전트') 

# 3. 데이터시각화
col1,col2 = st.columns(2)
with col1:
  st.subheader('데이터시각화1')
  st.image
with col2:('image(1).png')
  st.subheader('데이터시각화2')
  st.image('image.png')  

# 4. 모델 활용
st.subheader('모델 활용')
st.write('환율을 예측하고 싶으시다면, 1을 눌러주세요.')
a = st.selectbox('환율예측 확인 입력(확인한다:0, 확인하지않는다:1',[0,1])

if st.button('환율 예측'):
  input_data = [[ a ]]
 p = model.predict(input_data)
 st.write('환율예측 결과는',p)
