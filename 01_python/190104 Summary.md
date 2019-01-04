\ 루트 = 내pc

ls : 파일, 폴더 리스트(list)

ls -a  == ls -all : .이 붙은 숨김파일까지 모두 보여달라는 명령어

cd : 특정 폴더(디렉토리)로 이동하는 명령어, 더블클릭과 같다.

mkdir 폴더명 :  폴더 만드는 명령어

touch 파일명.확장자 : 파일 만드는 명령어



$(프롬프트) : 명령을 받을 준비가 되어 있음

echo "hello" : hello가 출력된다

man echo :  echo에 대한 설명이 나온다. q누르면 설명에서 나올 수 있음

맨 마지막에 콜론이 고정되어 있으면  q로 나올 수 있음

ctrl + p 이전 명령어( 화살표 ↑와 같음)

clear : 화면을 위로 쭉 (ctrl + l)

날려버리는 건 ctrl + d (파이썬 안에서 quit()도 가능)\

sleep 5(second가 default)

echo "할말" > 파일명.확장자  :  확장자에 할말이 들어감 (덮어쓰기)

echo "할말" >> 파일명.확장자  :  확장자에 할말이 들어감 (추가하기)

cat 파일명.확장자 ==> 확장자 내용이 표시됨 (이걸로 넘겨줄수도 있음 >>)

new라인이 없다면 그냥 붙어서 나옴

touch ."파일명" :  숨김파일 생성

ls -l : 파일 생성일

옵션을 여러개 붙여서 사용해도 작동

ls -al

d가 붙어있으면 파일

ls -altr

mv 원래파일명 새파일명 : 이름바꾸기

cp 파일명 만들파일명 : 파일복사

rm 파일명 :  파일 삭제

rm -i 파일명 :  파일 삭제 확인하는 단계가 추가됨

rm -f 파일명 : 강제 삭제

rm *.확장자명 : 해당 확장자 가진 파일 다 지울 수 있음

rm a* :  a로 시작하는거 다 지울 수 있음

rm * : 다 지움 

git -f  : 이렇게 하는건 비추천

git --force

ls 파일명 : 해당 파일이 있으면 보여준다.

ls a* : a로 시작하는 파일명 다 보여준다.

ls \*a\*: 앞뒤로 a있는거 다 지워버림

curl -OL neovansoarer.github.io/files/sonnets.txt : 해당 주소 파일을 받을 수 있음

which XXX : XXX가 있는지 확인하는 것

which git, which curl



curl -I https://leesangju92.github.io : 헤더 호출 status 200은 언제나 좋은 것



ls -lh : 사람이 읽기 편하게 정보를 표기, 용량이라던지..

head 파일명 : 처음 10줄만 보여줌

tail 파일명 : 마지막 10줄만 보여줌

ping 인터넷주소 : 신호를 보내 속도를 알아낸다

ping 인터넷주소 > google.log

tail -f 파일명

wc  파일명 : 줄 수 글자 수 용량을 알려준다.

x | y : x의 표준출력을 그대로 y로 넘긴다.  >리다이렉트 >>어펜드

less 파일명 : 뷰어

/누르면 검색모드, shift + N 이면 next 단어

grep rose sonnets.txt	

grep rose sonnets.txt	| wc : rose가 등장한 횟수

grep -i(대문자소문자상관없이 검색) rose sonnets.txt

ps aux : 지금 돌고있는 status가 모두 나온다.

ps aux | grep jupyter | kill -9 첫번째숫자 : 강제 종료

/ : root directory

sudo((super user do)) touch /opt/fake_file : 뭐든지 가능

~ : home directory , 컴퓨터 마다 장소가 다르다.

cd ~ : / 아래에서 내가 자유로운 작성이 가능한 곳

mkdir -p ssafy/ss3/students : 한번에 세 개의 파일 다 만드는 것.

rmdir a

rm -r

rm -rf 폴더이름/



touch rm / mkdir rm -rf

pwd ls cd

cd = cd ~

cd .. : 한단계 위 디렉토리로 가는 것 cd ../../

cd . : 지금 자신이 있는 장소 ( git add . = git add -A)

 cd - : 뒤로가기

