# 전주시 빅데이터 공모전

&nbsp;

## 1. 목적 및 동기

 - 공공데이터, 뉴스 크롤링 등 데이터를 수집 
 - 수집된 데이터를 통해서 전주시의 가장큰 문제를 추천
 - 데이터 분석, 시각화를 통해서 문제의 심각성 및 개선방안 찾기
 
&nbsp;

## 2. 데이터
 - 공공데이터포털의 자동차 사고 데이터
 - 공공데이터포털의 어린이 보호 구역 데이터
 - 공공데이터포털의 자전거 사고 데이터
 - 공공데이터 전주시 인구수 데이터
 
https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=TOTAL&keyword=%EC%A0%84%EC%A3%BC%EC%8B%9C&detailKeyword=&publicDataPk=&recmSe=&detailText=&relatedKeyword=&commaNotInData=&commaAndData=&commaOrData=&must_not=&tabId=&dataSetCoreTf=&coreDataNm=&sort=&relRadio=&orgFullName=&orgFilter=&org=&orgSearch=&currentPage=1&perPage=10&brm=&instt=&svcType=&kwrdArray=&extsn=&coreDataNmArray=&pblonsipScopeCode=
 : 공공데이터의 



&nbsp;
## 3. 전체적인 과정
![전체 흐름](http://drive.google.com/uc?export=view&id=1HmCycdd-LR3Mf-t79eaOUN7v-wi_H_4j)



&nbsp;
## 4. 폴더별 세부사항 설명
&nbsp;

   ### 4-1. 뉴스 크롤링 및 API 호출
 
 
        file name :  공공데이터 API.ipynb
        
        설명 : 공공데이터 중에서 csv 파일로 제공되지 않는 데이터를 얻기위해서 API를 이용해서 데이터를 얻는 코드
        사용된 패키지 : requests, xmltodict, json, pandas, numpy


        file name : 빅카인즈 뉴스 크롤링.ipynb

        설명 : 전주시에 관한 현황을 알기위해서 '전주시'단어를 중심으로 뉴스 기사 데이터 수집 코드
        사용된 패키지 : bs4 , selenium , pandas, numpy
        
        
        
&nbsp;
   ### 4-2. 대시보드
        
        설명 : 분석한 내용 및 folium 시각화를 flask를 사용해서 대시보드화 한것
        사용된 패키지 : flask, bokeh, folium
        
        실행방법 : 해당 폴더 위치로 이동후 해당경로 cmd 에서 python flask_app.py 실행
        
&nbsp;
   ### 4-2. 시각화_그래프
        
        설명 : 전주시 공공데이터를 분석한 bokeh 그래프 및 folium 지리 시각화 자료
        사용된 패키지 : bokeh, folium

 

 
 
&nbsp;
## 5. 분석결과
  - 전주시에서 자전거 사건이 많이 발생
  - 실제 초,중,고 위치와 자전거 도로까지 위치가 너무 멀리 분포되어있음
  - 주변 관광지에서도 큰 도로만 존재 사고횟수는 많음
  
  :heavy_exclamation_mark: 결과적으로 자전거도로를 초,중,고 및 관광지와 가깝고 사고가 자주 발생되는 곳으로 추가적으로 설치하는 것이 좋다고 생각함
  
  
  :smile: 최종적으로 위의 내용에 부합한 장소를 추가적으로 자전거도로로 추천
