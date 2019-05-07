//XHR은 브라우저에서만 실행시킬 수 있다. console 에 복붙 한뒤에 실행시키면 된다.
const DOMAIN = "https://jsonplaceholder.typicode.com/";
const RESOURCE = "posts";
const QUERY_STRING = "";
const URL = DOMAIN + RESOURCE + QUERY_STRING;

// req 대리인 XHR 객체 생성
const XHR = new XMLHttpRequest();

// XHR 요청 발사 준비 (method, url)
// 요청을 만들고, 정보를 담고, 보내고, 기다리고, 처리한다.
XHR.open("POST", URL);

XHR.setRequestHeader(
    "Content-Type",
    "application/json;charset=UTF-8"
);

// POST 요청을 보낼 때 괄호 안에 BODY (JSON : string )를 넣는다
XHR.send(
    JSON.stringify({ "title":"NewPost", "body":"This is New Post", "userId":1  })
    // '{ "title":"NewPost", "body":"This is New Post", "userId":1   }'
);

XHR.addEventListener("load", e => {
   // console.log(rawData);
   const parseData = JSON.parse(e.target.response);
   console.log(parseData);
});