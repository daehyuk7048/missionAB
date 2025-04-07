---
영상입니다.
https://youtu.be/T79BvZd81Uo?si=fxpGCJ9Lhbaq_SQX
---
![image](https://github.com/user-attachments/assets/dd6dd92b-f924-4d8d-b930-7614081aa978)
led는 18,19,20 을 이용하였습니다.
led를 초기화 시키기 위해 for 구문을 이용하여 led 모두를 초기화 시켰습니다.

![image](https://github.com/user-attachments/assets/2e870d08-bcc5-4c1c-92d1-b335385718c8)
무한루프를 위해 while을 사용했습니다.
bin이란 변수에는 i의 값을 2진수로 표현하여 세자리수를 넣게 하였습니다.
ex) i가 6이라면 bin에는 110

bit이라는 변수는 bin이라는 변수를 통해 만들어지게 되는데 가령 i가 6이라면 bin=110이고 bit=[0 1 1] 저장 됩니다.
따라서 led는 차례대로 bit의 값을 받게 되므로 led 18번 =0 / led 19번은 =1 / led 20번 =1 되므로 이진수 표현으로 점등되게 됩니다. 

---
회로입니다.
![KakaoTalk_20250407_213954532](https://github.com/user-attachments/assets/d513efb9-6602-4c39-b20f-6514dfc6badd)

