�ڹٴ� �Ǽ��� ���� ����
�Ǽ� double a;
���� int a; 
���ڿ� string a;
���� '��'
���ڿ� "��Ȱ�ڵ�" �׳� ū����ǥ�� ����.

\"
\n

���� �ּ� : //�ϰ������

������ �ּ� : `/*`  + `*/` (JavaDoc �ּ�, method�� �������� �˷��ִ� ����)

���̽��� """

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

���ڿ� ���� �����ݷ�`;`���̱�. ���� `;`�� �� ���δٸ� �� �ٿ� ���� ���� �ۼ�����

���̽��� ������ �ʴ´�.



��Ʈ f12

```java
package org.opentutorials.javatutorials.number;

public class IntDatatypeDemo {

	public static void main(String[] args) {
		byte a;
		a = 127; //128�� byte�� ������ �Ѿ�� ������ ������ ǥ�õȴ�.
        byte district = 1;
		int population = 50000000; //byte popualtion = 50000000;�� ������ ���.
		//������ � ������ Ÿ���� ������ �ִ����� �߿�
	}

}
```











�������� ����  int�� ����Ѵ�.

`byte(-128~127), short(	-32,768 ~ 32,767), int(	-2,147,483,648~2,147,483,647), long`

�Ǽ����� ���� double�� ����Ѵ�.

`float ��(1.40129846432481707e-45 ~ 3.40282346638528860e+38) , double ��(4.94065645841246544e-324d ~ 1.79769313486231570e+308d)`

�������� char �ۿ� ����

`char:��� �����ڵ� ����, "A"�� 2byte "AB"�� 4byte`