1. 웹캠의 통신
웹캠은 ONVIF 통신이라고 하는 통신 방법을 사용합니다. 웹 캠 뿐만 아니라 다른 IOT 기기들에서도 ONVIF 통신을 하기도 합니다. 이러한 ONVIF 통신은 어떤 식으로 이루어 지는지 알아 보겠습니다.

ONVIF는 Open Network Video Interface Forum의 약자로 말 그대로 Network 를 이용하여 Video를 주고 받는 즉 , 감시 장비 같은 곳에서 사용하는 프로토콜 입니다. 해당 프로토콜은 "국제" 표준 프로토콜이고 , 감시 장비 들 중에는 자사 표준 프로토콜을 이용해서 감시를 하는 경우도 있습니다.



2. 그럼 ONVIF는 뭔데?
ONVIF 영상을 볼 때는 RTP/RTSP 프로토콜을 쓰고 기타 기능들을 수행할 시 WSDL , SOAP 프로토콜을 씁니다.

ONVIF 자체에서 RTP/RTSP  프로토콜을 구현 하는게 아니라 카메라 같은 장비에서 사용할 수 있는 RTP / RTSP 주소를 알려주는 역할을 합니다. IOTFragile 프로젝트를 진행하면서 퍼징의 타겟으로 잡은 것은 ONVIF 에서 사용하는 SOAP 통신 입니다.



3. ONVIF ? SOAP 그걸로 어떻게 퍼징을 진행 하는데?
ONVIF 프로토콜 공식 문서 (https://www.onvif.org/wp-content/uploads/2016/12/ONVIF_WG-APG-Application_Programmers_Guide-1.pdf) 를 이용해서 INPUT을 받는 위치를 찾아서 그 위치에 랜덤한 값을 넣어 줍니다.
이때 뮤테이션 전략으로 4가지를 사용했는데



1. <태그>와 </태그> 사이의 내용을 변경하는 전략

2. <태그>의 위치를 랜덤하게 변경하는 전략

3. <태그> 파괴

4. 랜덤한 위치에 랜덤한 문자열 삽입 



예시를 들자면



#1. ONVIF ContinousMove (카메라의 움직임)

<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
 xmlns:tptz="http://www.onvif.org/ver20/ptz/wsdl"
 xmlns:tt="http://www.onvif.org/ver10/schema">
 <soap:Body>
 <tptz:ContinuousMove>
 <tptz:ProfileToken>Profile1</tptz:ProfileToken>
 <tptz:Velocity>
 <tt:PanTilt x="1" y="1"/>
 <tt:Zoom x="1"/>
 </tptz:Velocity>
 </tptz:ContinuousMove>
 </soap:Body>
</soap:Envelope>


#1-1 . 변경 후

<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
 xmlns:tptz="http://www.onvif.org/ver20/ptz/wsdl"
 xmlns:tt="http://www.onvif.org/ver10/schema">
 <soap:Body>
 <tptz:ContinuousMove>
 <tptz:ProfileToken>Profile1</tptz:ProfileToken>
 <tptz:Velocity>
 <tt:PanTilt x="31415926535" y="1"/> #x 좌표의 숫자를 랜덤하게 변경
 <tt:Zoom x="1"/>
 </tptz:Velocity>
 </tptz:ContinuousMove>
 </soap:Body>
</soap:Envelope>


이런식으로 값을 변경한후 Crash가 난다면(많은 코드를 커버한다면) , 그 곳이 취약점이 터질수 있는 곳으로 기록합니다.



4. 기록? 기록을 한다고?
밑에 있는 Github 주소를 가면 python tool이 있는데 그 Tool을 실행 해보면 , IP를 입력 받고 (해당 IP는 대상 기기 즉 , IP 카메라입니다) 그 IP에 랜덤한 ONVIF 프로토콜을 날려서 코드 커버리지( 코드를 얼마나 커버 했는가 ) 를 DB 파일로 저장을 합니다. 해당 DB파일을 보면 어느 프로토콜에서 Crash가 나는지 , 얼마나 많은 커버리지를 기록했는지 나옵니다.

이를 통해 취약점을 찾는데 도움을 줄 수 있습니다.



5.  퍼징 vs 코드 오디팅
퍼징에 대해 말이 많이 나오는 것이 퍼징은 곧 "운" 이지 않나? 입니다. 말 그대로 , 퍼저를 이용해서 취약점을 찾을때 1시간이 걸릴수도 , 24시간 더 나아가서는 못 찾을수 있습니다. 근데 퍼저는 "도구" 입니다. 코드 오디팅만 이용해서 취약점을 찾는 경우 VS 코드 오디팅 + 퍼저 를 하는 경우 , 코드 오디팅 + 퍼저가 더 효율이 높게 나옵니다. 퍼저만 이용하지 말고 , 코드 오디팅 실력도 길러서 취약점을 찾는 능력을 키우는 것이 더 좋은 결과를 볼 수 있습니다
