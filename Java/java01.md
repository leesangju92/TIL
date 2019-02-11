자바는 실수와 정수 구분
실수 double a;
정수 int a; 
문자열 string a;
문자 '생'
문자열 "생활코딩" 그냥 큰따옴표만 쓰자.

\"
\n

한줄 주석 : //하고싶은말

여러줄 주석 : `/*`  + `*/` (JavaDoc 주석, method가 무엇인지 알려주는 역할)

파이썬은 """

```java
package org.opentutorials.javatutorials.number;

public class StringDemo {
	public static void main(String[] args) {
		//String first;
		//first = "coding";
		String first = "coding";
		String a, b;
		a = "coding";
		b = "everbody";
		System.out.println(a+b);	
	}
}
```

문자열 끝에 세미콜론`;`붙이기. 따라서 `;`만 잘 붙인다면 한 줄에 여러 문장 작성가능

파이썬은 붙이지 않는다.



알트 f12

```java
package org.opentutorials.javatutorials.number;

public class IntDatatypeDemo {

	public static void main(String[] args) {
		byte a;
		a = 127; //128은 byte의 범위를 넘어서기 때문에 오류가 표시된다.
        byte district = 1;
		int population = 50000000; //byte popualtion = 50000000;은 에러가 뜬다.
		//변수가 어떤 데이터 타입을 가지고 있는지가 중요
	}

}
```











정수형은 보통  int를 사용한다.

`byte(-128~127), short(	-32,768 ~ 32,767), int(	-2,147,483,648~2,147,483,647), long`

실수형은 보통 double을 사용한다.

`float ±(1.40129846432481707e-45 ~ 3.40282346638528860e+38) , double ±(4.94065645841246544e-324d ~ 1.79769313486231570e+308d)`

문자형은 char 밖에 없음

`char:모든 유니코드 문자, "A"는 2byte "AB"는 4byte`