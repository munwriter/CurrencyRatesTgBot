# Currency Rates Telegram Bot
![GitHub last commit](https://img.shields.io/github/last-commit/munwriter/CurrencyRatesTgBot?style=for-the-badge)
![CodeFactor Grade](https://img.shields.io/codefactor/grade/github/munwriter/currencyratestgbot?style=for-the-badge)
![Static Badge](https://img.shields.io/badge/aiogram-v3-blue?style=for-the-badge&logo=telegram)
![Static Badge](https://img.shields.io/badge/matplotlib-blue?style=for-the-badge&logo=matplotlib)
![Static Badge](https://img.shields.io/badge/httpx-red?style=for-the-badge)

## Overview

The repository is a telegram bot for tracking the exchange rate. The user can choose their preferred currencies and track the current exchange rates for them. Information can also be obtained over a long period of time. The bot provides a graphical representation of most of the data.

## Stack

- **Aiogram 3**
- **Httpx**
- **Numpy**
- **Matplotlib**
- **Sqllite3**

## Api
[Api layer - Currencies](https://apilayer.com/marketplace/currency_data-api)

## Features

### Basic setup - configurate user settings

<p> 
  <img width="400" src="https://github.com/munwriter/CurrencyRatesTgBot/blob/main/.github/Untitled.png">
</p>
<p> 
  <img width="400" src="https://github.com/munwriter/CurrencyRatesTgBot/blob/main/.github/Untitled%201.png">
</p>
You can choose src currency and required currencies from list of available currencies.


### Common comands

<p> 
  <img width="400" src="https://github.com/munwriter/CurrencyRatesTgBot/blob/main/.github/Untitled%202.png">
</p>

### Menu
<p> 
  <img width="400" src="https://github.com/munwriter/CurrencyRatesTgBot/blob/main/.github/Untitled%203.png">
</p>

### Timeframe

<p> 
  <img width="400" src="https://github.com/munwriter/CurrencyRatesTgBot/blob/main/.github/Untitled%204.png">
</p>

<p> 
  <img width="400" src="https://github.com/munwriter/CurrencyRatesTgBot/blob/main/.github/graphic.jpg">
</p>

### Convert

<p> 
  <img width="400" src="https://github.com/munwriter/CurrencyRatesTgBot/blob/main/.github/Untitled%205.png">
</p>

### Live

<p> 
  <img width="400" src="https://github.com/munwriter/CurrencyRatesTgBot/blob/main/.github/Untitled%206.png">
</p>


## Instalation and usage

### 1 . Clone a repository

```bash
git clone https://github.com/munwriter/SneakersStoreAiogramBot.git
```

### 2. Install a requirements

```bash
pip install -r requirements.txt
```

### 3. Create  .env file

```
BOT_TOKEN=''
API_URL='https://api.apilayer.com/currency_data/'
API_KEY=''
```

### 4. Run bot

```bash
py run.py
```
