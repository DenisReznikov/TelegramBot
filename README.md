![GitHub Actions status](https://github.com/DenisReznikov/TelegramPolikekBot/workflows/bot%20unit%20test/badge.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![BCH compliance](https://bettercodehub.com/edge/badge/DenisReznikov/TelegramPolikekBot?branch=master)](https://bettercodehub.com/)
[![codebeat badge](https://codebeat.co/badges/b7e5226b-4d10-4900-bbb4-98d7168128e9)](https://codebeat.co/projects/github-com-denisreznikov-telegrampolikekbot-master)

# Telegram Пolitex bot

## Description 
Bot shows bars, restaurants and cafes near you.\
Still bot helps to know the weather in any city or by your geolocation.\
Also helps to find the right thing on avito.

[@bot](https://t.me/Itmo_politex_Ai_bot) You can test bot hear

### Requirements
* [Python](https://www.python.org) >= 3.5(64bit)
* [beautifulsoup4](https://github.com/wention/BeautifulSoup4) and [lxml](https://github.com/lxml/lxml) library for pulling data out of HTML (avito)  
* [Python Telegram Bot](https://github.com/python-telegram-bot/python-telegram-bot) - library provides a pure Python interface for the Telegram Bot API
* [requests](https://github.com/psf/requests) - library allows you to send HTTP requests
 ### Installing  
    > git clone https://github.com/DenisReznikov/TelegramPolikekBot.git
    > pip install -r requirements.txt
    > python main.py
    
### Application architecture
I tried to stick to the to the MVC pattern (Model-View-Controller) without view ¯\\_(ツ)_/¯.
```
telegrambot/
├── scr/ 
|   ├── models/                    // model (work with weather and Yandex.Map API and parsing Avito)
|   ├── handler/                   // connect model and telegram API
```
### CI/CD
Plus bot has unit test, for simulate
[CI](https://github.com/DenisReznikov/TelegramBot/actions)
and we deploy our bot to heroku
[CD](https://github.com/DenisReznikov/TelegramBot/deployments)
## Example of work bot
