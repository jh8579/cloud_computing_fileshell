#Cloud Computing Project 
==============
# Project Title : FileShell
----------------
### Django와 AWS EC2, S3를 사용하여 DropBox와 같은 기능을 하는 웹 서비스 개발
Using Django and AWS EC2 and S3 develop a web service that works like a DropBox
----------------
# 프로젝트 주요 기능
> 자신의 계정에 파일을 업로드/다운로드하는 웹 서비스를 구현하는 것이다.

## 기능 / 구성
1. **홈 화면**
	- 세션에 로그인되어 있는 사용자가 없을 경우 로그인 화면으로 리다이렉트.
	- 로그인 되어 있는 경우 홈 화면 출력.
	- 홈 화면에서는 사용자가 갖고 있는 즐겨찾기 파일 목록, 최근 열람 파일 목록이 출력된다.
2. **파일 관리 화면**
	- 세션에 로그인되어 있는 사용자가 없을 경우 로그인 화면으로 리다이렉트.
	- 로그인 되어 있는 경우 파일 화면 출력.
 	- 사용자는 드래그 앤 드롭이나 클릭을 통해 파일을 업로드 할 수 있다.
  	- 사용자는 별 모양 아이콘 클릭을 통해 원하는 파일을 즐겨찾기로 설정/해제를 할 수 있다.
  	- 사용자는 휴지통 아이콘 클릭을 통해 폴더/파일을 삭제할 수 있다.
  	- 폴더 삭제의 경우 해당 폴더와 하위의 모든 폴더/파일까지 모두 삭제한다.
3. **파일 검색 화면**
  	- 사용자는 파일 이름이나 확장자를 통해 폴더/파일을 검색할 수 있다.
  	- 검색한 결과 목록에서 별 모양 아이콘 클릭을 통해 즐겨찾기 설정/해제를 할 수 있다.
  	- 검색한 결과 목록에서 휴지통 아이콘 클릭을 통해 폴더/파일을 삭제할 수 있다.
  	- 폴더 삭제의 경우 해당 폴더와 하위의 모든 폴더/파일까지 모두 삭제한다.
3. **폴더 트리구조**
	- 폴더는 자신의 부모 폴더와 자식 폴더를 가지는 트리 구조로 구성되어 있다.
	- 폴더와 파일은 서로를 Folder, Datas라는 변수를 가진다.
	- 트리 구조를 통해 파일 삭제가 이루어지므로 하위 폴더의 완벽한 삭제가 이루어진다.
----------------
패키지 설치(Install packages)

pip install -r requirements.txt
----------------
