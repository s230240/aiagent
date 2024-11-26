# 분류 모델 웹앱 만들기
import streamlit as st

# 1. 기계학습 모델 파일 로드
import joblib
model = joblib.load('linear_regression_model.pkl')

# 2. 모델 설명
st.title('지능형 환율 예측 에이전트') 
st.subheader('모델 설명')
st.write('- 기계학습 알고리즘 : 선형 회귀')
st.write('- 학습 데이터 출처 : https://www.index.go.kr/enara')
st.write('- 훈련 데이터 개수: 92건')
st.write('- 테스트 데이터 개수: 92건')
st.write('- 문제: 환율 예측 기술이 잘못된 목적으로 사용되어 시장을 조작하거나 부당한 이익을 취하려는 시도가 발생할 수 있음')
st.write('- 대응방안: 기술 사용 목적과 허용범위를 법적으로 규제 필요')
         
# 3. 데이터시각화
col1,col2 = st.columns(2)
with col1:
 st.subheader('데이터시각화1')
 st.image('image (1).png')
with col2:
 st.subheader('데이터시각화2')
 st.image('image.png')  

# 4. 모델 활용
st.subheader('모델 활용')
st.write('환율을 예측하고 싶으시다면, 1을 눌러주세요.')
a = st.number_input('금리입력',value=0)
b = st.number_input('GDP입력',value=0.0)
c = st.number_input('확인한다:0, 확인하지않는다:1')

if st.button('환율 예측'):
  input_data = [[ a,b,c ]]
  p = model.predict(input_data)
st.write('환율예측 결과는',p)
