# 디스코드 보이스 채팅방 이벤트 기록 봇
## 개요

디스코드 보이스 채팅방의 다양한 이벤트 (연결, 연결해제, 이동)을 텍스트 채팅방에 기록하기위해 제작되었습니다.

파이썬 3.5 이상에서 개발되었으며, discord.py 는 당연히 필수입니다.

> discord.py (보이스 지원) 설치 명령어 : python3 -m pip install -U discord.py[voice]

## config

bot.py를 텍스트 편집기로 여시면 설정하실 수 있습니다.

> CHANNEL_NAME = "voice-notice" **이벤트를 기록할 텍스트 채팅방**

> BOT_TOKEN = "" **디스코드 봇 토큰**
