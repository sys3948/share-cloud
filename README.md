# share-cloud
<h2>Django로 구현하는 share cloud</h2>

<h3>File Server : <a href="https://github.com/sys3948/share-cloud-FS">https://github.com/sys3948/share-cloud-FS</a></h3>

<h3>진행 기록</h3><br>

<h4>2022 - 03 - 17 : </h4>
  - Folder들을 html로 Rendering할 때 group by절로 정리 후 Rendering하려고 할 경우에 문제 발생.<br />
  - 문제 내용. group by절을 사용하기 위한 values()의 반환 값은 QuerySet Object에서 dict type으로 값이 반환되기 때문에 ForeignKey에 해당되는 객체 값을 가져오지 못하는 문제가 발생.<br />
  - 해결방법 ORM으로는 해결하기 어렵다고 판다. 그렇기에 따로 해당 Data들을 불러올 수 있게 실행 쿼리를 정의한 함수를 구현해서 불러오는 것으로 생각.
  - 다음 진행할 것(3월 18일 이후)<br />
  <ul>
    <li>쿼리를 정의한 함수 구현하기.</li>
    <li>File Upload 구현하기.</li>
  </ul><br /><br />

<h4>2022 - 03 - 16 : </h4>
  - File Server에서 폴더를 엉뚱하게 생성하는 문제 해결함.<br />
  - Folder들을 html로 Rendering할 때 group by절로 정리 후 Rendering하려고 할 경우에 문제 발생.<br />
  - 문제 내용. group by절을 사용하기 위한 values()의 반환 값은 QuerySet Object에서 dict type으로 값이 반환되기 때문에 ForeignKey에 해당되는 객체 값을 가져오지 못하는 문제가 발생.<br />
  - 다음 진행할 것(3월 17일)<br />
  <ul>
    <li>발생된 문제 해결하기.</li>
    <li>File Upload 구현하기.</li>
  </ul><br /><br />

<h4>2022 - 03 - 14 : </h4>
  - 폴더 저장구조가 문제 해결.<br />
  - 데이터베이스에 저장된 폴더에 해당되는 path를 File Server에서 엉뚱하게 생성하는 문제가 발생함.<br />

<h4>2022 - 03 - 12 : </h4>
  - 폴더 저장구조가 문제 생김.<br />
    - 문제 1. 최상위 폴더로 생성할 경우 folder_path가 최신으로 생성한 상위 폴더의 하위 폴더로 지정이 됨<br />

<h4>2022 - 03 - 07 : </h4>
  - 폴더 생성 기능을 Home(root path)에서부터 선택할 수 있게 했는데 어느 폴더가 어느 폴더의 상위인지 하위인지 구분되지 않는 문제점이 발생. 그렇기에 존재하고 있는 폴더에서 새로운 폴더를 생성할 수 있도록 구현하기 위해 Models 수정. 더 수정할 거 같다.<br />
  - 다음 진행할 것(3월 8일 이후)<br />
  <ul>
    <li>수정한 부분 테스트 후, 다시 수정하거나 Nav에 rendering 하기.</li>
    <li>파일 업로드 기능 구현.</li>
  </ul><br /><br />

<h4>2022 - 03 - 06 : </h4>
  - FS에서 폴더 생성 구현.<br />
  - Side Nav에 생성한 폴더 rendering 하기.<br />
  - 다음 진행할 것(3월 7일)<br />
  <ul>
    <li>폴더 생성 기능을 Home(root path)에서 부터 선택할 수 있게 했는데 어느 폴더가 어느 폴더의 상위인지 하위인지 구분되지 않는 문제점이 발생. 그렇기에 존재하고 있는 폴더에서 새로운 폴더를 생성할 수 있도록 구현하기.</li>
    <li>파일 업로드 기능 구현.</li>
  </ul><br /><br />

<h4>2022 - 03 - 05 : </h4>
  - folder 생성 DB 저장 작업 중(DB에 저장한 정보 FS에 전송하기.)<br />
  - <br />
  - 다음 진행할 것(3월 6일)<br />
  <ul>
    <li>FS에서 받은 정보로 folder 생성하기.</li>
  </ul><br /><br />

<h4>2022 - 03 - 04 : </h4>
  - folder 생성 DB 저장 작업 중(DB에 문제 없이 저장 완료. 코드 중복 제거하기.)<br />

<h4>2022 - 03 - 03 : </h4>
  - 폴더 생성하기 기능 구현중에 폴더 모델 수정<br />
  - ORM queryset에서 로그인 로직을 잘 못 구현해서 수정<br />
  - folder 생성 DB 저장 작업중<br />
  - 다음 진행할 것(3월 4일)<br />
  <ul>
    <li>folder 생성 DB 저장 작업 완료(문제 발생 : 상위 폴더 정보가 없는 상태로 저장하는 방식으로 구현하여 상위 폴더 정보를 저장할 수 없다는 문제가 발생)</li>
    <li>File Server에 DB에 저장된 폴더 생성하기.</li>
  </ul><br /><br />

<h4>2022 - 02 - 25 ~ 03 - 02 : </h4>
  - 이유 없이 쉼(문제) <br /><br />


<h4>2022 - 02 - 24 : </h4>
  - 23일날은 쉼<br />
  - 폴더 생성하기 기능 구현중<br />
  - 25일날 할 것. <br />
  <ul>
    <li>폴더 생성하기 기능 구현.</li>
    <li>파일 업로드 기능 구현</li>
  </ul><br /><br />


<h4>2022 - 02 - 22 : </h4>
  - flow chart 기반으로 기능 구현하려고 했는데 Model이 이상한 부분이 있는 관계로 Model 수정.<br />
  - Model 수정하고 적용하는 과정에 예상치 못한 상황이 발생하여 기능 구현하지 못함.<br />
  - 17 ~ 21일은 해당 Project를 진행하지 못 했다. <br />
  - 23일날 할 것. <br />
  <ul>
    <li>그린 두 가지 기능에 대한 flow chart를 기반으로 기능 구현하기.</li>
  </ul><br /><br />

<h4>2022 - 02 - 16 : </h4>
  - File Upload와 Folder Create 기능 부분 구현함에 있어서 기능 로직에 대한 모호성이 생기는 상황이 발생함. 그렇기에 해당 기능 로직에 대한 명확하게 하기 위해 두 가지 기능에 대한 flow chart를 그렸다.<br />
  - 17일날 할 것. <br />
  <ul>
    <li>그린 두 가지 기능에 대한 flow chart를 기반으로 기능 구현하기.</li>
  </ul><br /><br />

<h4>2022 - 02 - 15 : </h4>
  - http 통신에 해당하여 FS에 Folder 생성시 Error 발생하면 회원 가입 못하도록 에러 처리 기능 구현.<br />
  - File Upload하기 위한 Modal 디자인 및 구현.<br />
  - 16일날 할 것. <br />
  <ul>
    <li>본격적으로 File Upload와 Folder Create 기능 부분 구현하기.</li>
  </ul><br /><br />

<h4>2022 - 02 - 14 : </h4>
  - 회원 가입 시 File Server에 해당 계정의 폴더 생성하기.<br />
  - 생성된 폴더 용량 정보를 가져올 수 있는지 확인해보기. -> 정확히는 폴더의 용량 정보는 못 얻었고 폴더에 생성된 파일의 용량 정보는 얻을 수 있다.<br />
  - 15일날 할 것. <br />
  <ul>
    <li>http 통신에 해당하여 FS에 Folder 생성시 Error 발생하면 회원 가입 못하도록 에러 처리 기능 다 구현 못 한거 구현하기.</li>
    <li>File Upload하기 위한 Modal 디자인 및 구현하기.</li>
  </ul><br /><br />

<h4>2022 - 02 - 13 : </h4>
  - CORS Error 해결완료! CORS policy 정책에 걸려서 통신이 되지 않았던 상황은 url을 잘 못 기입했기에 CORS policy 정책에 의해 block 된거였다.<br />
  - 두 Server간 http 통신으로 폴더 생성하는 법까지 완료<br />
  - 14일날 할 것. <br />
  <ul>
    <li>회원 가입 시 File Server에 해당 계정의 폴더 생성하기.</li>
    <li>생성된 폴더 용량 정보를 가져올 수 있는지 확인해보기.</li>
    <li>File Upload하기 위한 Modal 디자인 및 구현하기.</li>
  </ul><br /><br />

<h4>2022 - 02 - 10 : </h4>
  - Flask에서 NetWork 문제 발생함. 땜빵식으로 NetWork를 사용용도에 따라 변경하기로 함.<br />
  - git 사용에 많은 오류 발생. 주말에 git에 대한 공부해야할 것.<br />
  - Django와 Flask연결 했늗데 CORS Error 발생<br />
  - 11일날 할 것. <br />
  <ul>
    <li>CORS Error 해결하기.</li>
    <li>두 Server간의 통신 테스트 하기.</li>
    <li>회원 가입 시 File Server에 해당 계정의 폴더 생성하기.</li>
  </ul><br /><br />

<h4>2022 - 01 - 27 ~ 02 - 09 : </h4>
  - File Server에 git 설치 및 Flask Test App 구현<br />
  - 설 연휴 기한으로 많이 쉼(문제) <br />

<h4>2022 - 01 - 25 : </h4>
  - account Model과 cloud Model 변경 상세 내용은 코드 참고.<br />
  - Header DropDown Menu 구현.<br />
  - 26일날 할 것. <br />
  <ul>
    <li>Contents 부분 구현하기.</li>
    <li>view 구현하기.</li>
  </ul><br /><br />

<h4>2022 - 01 - 24 : </h4>
  - Main Templates 구현 중<br />
  - Folder List & Size Progress Bar 디자인 구현.<br />
  - 25일날 할 것. <br />
  <ul>
    <li>현재 구현된 DB Model을 변경해야 될 상황이 옴, Model 변경하기.</li>
    <li>Main Templates의 Header부분 User DropDown 디자인 구현하기.</li>
    <li>시간 여유가 있다면 Contents 부분 구현하기.</li>
  </ul><br /><br />


<h4>2022 - 01 - 23 : </h4>
  - File Server 재구축(Nginx 설치, Python 설치, Flask 설치)<br />
  - 전 기록에 작성했듯이 File Server를 웹 서버로 구축하여 http 통신으로 파일을 저장할 것이다. 파일 서버의 프레임워크는 Flask를 사용할 것이다.<br />
  - Main 페이지 디자인 완료.<br />
  - 24일날 할 것. <br />
  <ul>
    <li>Main Templates 구현하기.</li>
  </ul><br /><br />


<h4>2022 - 01 - 19 : </h4>
  - Ubuntu SAMBA Server로 접근하는 방법을 찾지 못 함.<br />
  - 그래서 기존의 방식을 변경하려고 한다.<br />
  - 기존의 방식 : 웹 서버(Nginx, Django), DB 서버(MySQL), 파일 서버(SamBa) 이렇게 세 개의 서버를 구축하여 Share Cloud App을 구현하는 것으로 계획<br />
  - 변경 방식 : 웹 서버(Nginx, Django), DB 서버(MySQL), 파일 서버(Nginx) 웹서버로 구축해서 파일 업로드 다운로드를 웹 통신으로 구현하는 것으로 변경.<br />
  - 20일날 할 것. <br />
  <ul>
    <li>Django에서 다른 웹 서버 파일 전송하는 방법 찾기</li>
    <li>Main 페이지 디자인 하기.</li>
  </ul><br /><br />


<h4>2022 - 01 - 18 : </h4>
  - Ubuntu SAMBA Server 구축 완료.<br />
  - Host에서 SAMBA 접근까지 완료.<br />
  - 19일날 할 것. <br />
  <ul>
    <li>SAMBA에 Access하기 위한 모듈 정하기.</li>
    <li>SAMBA의 디렉토리 용량 제한 및 할당하는 방법 찾기.</li>
  </ul><br /><br />


<h4>2022 - 01 - 16 : </h4>
  - 회원 가입 후 인증 메일 전송할 시 인증 토큰 링크 생성에 관한 원리 대략적으로 분석 완료.<br />
  - File Server로는 Ubuntu SAMBA Server로 사용하기로 결정.<br />
  - File Server를 Django Projects에서 Access하기 위해 Django_smb module 사용할지 아니면 pysmb를 사용할지 결정해야한다.<br />
  - 17일날 할 것. <br />
  <ul>
    <li>Ubuntu SAMBA Server 구축</li>
    <li>SAMBA에 Access하기 위한 모듈 정하기.</li>
    <li>SAMBA의 디렉토리 용량 제한 및 할당하는 방법 찾기.</li>
  </ul><br /><br />


<h4>2022 - 01 - 13 : </h4>
  - 회원 가입 후 인증 메일 전송할 시 인증 토큰 링크 생성에 관한 원리 분석.<br />
  - 원래 메인 페이지 구현을 해야되었지만 토근 링크 생성에 관한 원리에 대한 이해가 부족하여 메인 페이지 구현을 말고 토큰 링크 생성 원리에 대해 분석함.<br />
  - 14일날 할 것. <br />
  <ul>
    <li>메인 페이지 구현에 관한 조사.</li>
    <ol>
      <li>File Server</li>
      <li>Local host가 아닌 외부 File Server에 File Upload & DownLoad 하는 방법.</li>
    </ol>
  </ul><br /><br />


<h4>2022 - 01 - 12 : </h4>
  - 11일날 구현한거(인증 절차, 인증 메일 재 전송, 인증 확인 메일 변경) 테스트 후 문제 해결<br />
  - 아이디 & 비밀번호 찾기 페이지 구현<br />
  - 13일날 할 것. <br />
  <ul>
    <li>메인 페이지 구현</li>
  </ul><br /><br />


<h4>2022 - 01 - 11 : </h4>
  - 회원 가입 후 인증 절차에 대한 상세 페이지 구현<br />
  - 인증 메일 다시 전송 기능 구현<br />
  - 인증 확인 메일 변경 페이지 구현<br />
  - 12일날 할 것. <br />
  <ul>
    <li>11일날 구현한거 테스트 하기</li>
    <li>아이디 & 비밀번호 찾기 페이지 구현</li>
  </ul><br /><br />


<h4>2022 - 01 - 10 : </h4>
  - 로그인 시 인증 절차 간단하게 디자인<br />
  - 11일날 할 것. <br />
  <ul>
    <li>회원 가입 후 인증 절차에 대한 상새 설명 페이지 구현</li>
    <li>인증 메일 다시 전송 기능 구현</li>
    <li>인증 메일 변경 페이지 구현</li>
    <li>아이디 & 비밀번호 찾기 페이지 구현</li>
  </ul><br /><br />


<h4>2022 - 01 - 09 : </h4>
  - 회원가입 할 때 fetch API를 통한 데이터 전송 구현 중 에러 발생 <br />
  - 에러 내용 : Django Forbidden(CSRF token missing) <br />
  - Forbidden 에러 https://docs.djangoproject.com/en/3.2/ref/csrf/#ajax 문서 정보를 참고하여 해결함.<br />
  - 메일 인증 기능을 itsdangerous 모듈을 이용하여 구현 중 don't matched 에러 발생<br />
  - itsdangerous 모듈이 아닌 get_current_sit, urlsafe_base64_decode, urlsafe_base64_encode, force_bytes, force_str, PasswordResetTokenGenerator 모듈을 이용하여 이메일 인증 기능을 구현함.<br /><br /><br />


  <h4>2022 - 01 - 08 : </h4>
  - 로그인 &회원가입 templates 구현<br /><br /><br />


<h4>2022 - 01 - 05 : </h4>
  - Django Model 구현<br />
    - Django에서 지원하는 User Model을 이용하려고 했으나 Password Hash 부분에 대한 정보 부족으로 Account Model을 새로 구현하기로 했다.<br />
    - 구현한 Model은 Account(사용자), StoreFile(저장파일), ShareStoreFile(공유 파일)다.<br /><br /><br />


<h4>2022 - 01 - 04 : </h4>
  - VM 생성 후 Ubuntu 20.04.2.0 설치 MySQL Community server 설치<br />
  - MySQL Root 권한 계정 생성<br />
  - Django Project에 MySQL연동<br /><br /><br />


