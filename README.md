# Binance Futures Trading Bot

A modular Python command-line trading bot that interacts with the Binance Futures Testnet API to place Market and Limit orders. The project demonstrates API integration, CLI design, input validation, logging, and exception handling.

---

## Features

- Place **Market Orders**
- Place **Limit Orders**
- Command Line Interface (CLI)
- Input Validation
- Logging using Python logging module
- Exception Handling
- Environment Variable Support (.env)
- Modular Project Structure

---

## Project Structure

```text
TradingBotAssignment/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── cli.py
│   ├── logging_config.py
│   ├── orders.py
│   └── validators.py
│
├── logs/
│
├── .gitignore
├── README.md
├── requirements.txt
└── main.py
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/ShrutiKamble02/Binance-Futures-Trading-Bot.git
```

Move into project directory

```bash
cd Binance-Futures-Trading-Bot
```

Create virtual environment

```bash
python -m venv venv
```

Activate virtual environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

```env
BINANCE_API_KEY=YOUR_API_KEY
BINANCE_API_SECRET=YOUR_API_SECRET
BASE_URL=https://testnet.binancefuture.com

---

## Usage

### Market Order

```bash
python main.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### Limit Order

```bash
python main.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 30000
```

---

## Logging

All trading activities are stored inside

```
logs/trading.log
```

Logs include:

- Connection status
- Order request
- Order response
- Errors
- Exceptions

---

## Validation

The project validates:

- Trading Symbol
- Order Side
- Order Type
- Quantity
- Price (required for LIMIT orders)

---

## Exception Handling

The application handles:

- Binance API Errors
- Network Errors
- Invalid User Inputs
- Unexpected Exceptions

---


## Technologies Used

- Python 3.x
- python-binance
- python-dotenv
- argparse
- logging
- Git & GitHub

## Notes

This project is designed for the Binance Futures Testnet. A valid Testnet API Key and Secret are required to execute authenticated API requests.

## License

This project was developed as part of an internship assessment and is intended for educational purposes.

## Author

Shruti Kamble
