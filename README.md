# share-cloud
<h2>Django로 구현하는 share cloud</h2>

<h4>2022 - 01 -04 : </h4>
  - VM 생성 후 Ubuntu 20.04.2.0 설치 MySQL Community server 설치<br />
  - MySQL Root 권한 계정 생성<br />
  - Django Project에 MySQL연동<br /><br /><br />


<h4>2022 - 01 -05 : </h4>
  - Django Model 구현<br />
    - Django에서 지원하는 User Model을 이용하려고 했으나 Password Hash 부분에 대한 정보 부족으로 Account Model을 새로 구현하기로 했다.<br />
    - 구현한 Model은 Account(사용자), StoreFile(저장파일), ShareStoreFile(공유 파일)다.<br /><br /><br />


  <h4>2022 - 01 -08 : </h4>
  - 로그인 &회원가입 templates 구현<br /><br /><br />


<h4>2022 - 01 -09 : </h4>
  - 회원가입 할 때 fetch API를 통한 데이터 전송 구현 중 에러 발생 <br />
  - 에러 내용 : Django Forbidden(CSRF token missing) <br />
  - Forbidden 에러 https://docs.djangoproject.com/en/3.2/ref/csrf/#ajax 문서 정보를 참고하여 해결함.<br />
  - 메일 인증 기능을 itsdangerous 모듈을 이용하여 구현 중 don't matched 에러 발생<br />
  - itsdangerous 모듈이 아닌 get_current_sit, urlsafe_base64_decode, urlsafe_base64_encode, force_bytes, force_str, PasswordResetTokenGenerator 모듈을 이용하여 이메일 인증 기능을 구현함.<br /><br /><br />