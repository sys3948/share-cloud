# share-cloud
<h2>Django로 구현하는 share cloud</h2>

<h4>2022 - 01 -04 : </h4>
  - VM 생성 후 Ubuntu 20.04.2.0 설치 MySQL Community server 설치<br />
  - MySQL Root 권한 계정 생성<br />
  - Django Project에 MySQL연동<br />


<h4>2022 - 01 -05 : </h4>
  - Django Model 구현<br />
    - Django에서 지원하는 User Model을 이용하려고 했으나 Password Hash 부분에 대한 정보 부족으로 Account Model을 새로 구현하기로 했다.<br />
    - 구현한 Model은 Account(사용자), StoreFile(저장파일), ShareStoreFile(공유 파일)다.<br />