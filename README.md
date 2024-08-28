# team project: "spartamarket"

## Table of Contents
- [프로젝트 설명](#프로젝트-설명)
- [팀원 및 역할분담](#팀원-및-역할분담)
- [사용 방법 및 프로젝트 구성](#사용-방법-및-프로젝트-구성)
    - [accounts](#accounts)
    - [products](#products)
    - [users](#users)
- [사용한 기술](#사용한-기술)
- [팀 노션 및 GitHub Repository](#팀-노션-및-github-repository)

## 프로젝트 설명

팀과제, 중고장터 “스파르타마켓” 만들기

초보 개발자들의 Django 및 github 연습장입니다.

## 팀원 및 역할분담

나지수(팀장): 로그인/로그아웃 구현, 해시태그 구현, 해시태그 검색 페이지 CSS 적용, PRODUCT 페이지 CSS 적용, product_detail 페이지 css 적용, 프로플 페이지 작성, 서비스 아키택처, READ ME 작성


박연재(서기): 회원가입, 게시글 생성, 게시글 찜, 팔로우, 게시글 정렬, 게시글 검색, 프로필 이미지 수정, profile페이지 css 적용, profile update 페이지 css 적용, 개인 정보 수정 페이지 css 적용, ppt 초안 작성


김동용(팀원): sa 탬플릿 최신화, 회원정보수정, 비밀번호 변경, 상품 상세페이지, 게시글 수정, accounts페이지 css 적용, product 페이지 css 적용, hashtag 기능 수정, update페이지 최적화

이예지(팀원): 와이어프레임 최신화, 게시글 삭제, product 페이지 css 적용, 각 페이지 상호작용 버튼 추가, 로그인/비로그인시 보여지는 화면 분리 

공동 작업(화면공유, 페어프로그래밍): 스켈레톤 코드 작성, 회원 기능, 유저 기능, 게시 기능, 와이어프레임, ERD, SA 작성


## 사용 방법 및 프로젝트 구성

우리 프로젝트는 accounts, products, users 3개의 앱으로 구성되어있습니다.

### products

products(게시기능): 프로젝트의 메인 기능으로 게시글을 올리고, 검색하고, 수정 및 삭제가 가능합니다.


### accounts

accounts(회원기능): 회원기능만 담당하게 함으로서 다른 부분에서 문제가 발생하더라도 회원 기능과 민감한 정보에 영향을 주지 않게하기 위해 프로필 기능과 분리하였습니다.



### users

users(프로필): 유저의 프로필을 담당하는 앱으로 프로필 accounts에서 받아온 유저 정보를 기반으로 프로필 페이지가 생성 되고, 프로필 페이지에선 내가 작성한 게시글과, 찜한 상품을 확인하거나, 팔로우 기능을 구현해서 내가 팔로우 한 사람, 혹은 나를 팔로우한 사람 수를 확인 할 수 있습니다.

## 사용한 기술
Django 4.2
Pycharm
Vscode
github

## 팀 노션 및 GitHub Repository

- 팀 깃허브 : https://github.com/qwerrrqw/spartamarket
- 팀 노션:  https://teamsparta.notion.site/963a497589134132aa7ac8081a9a6acc
