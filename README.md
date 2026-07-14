# Binance Futures Trading Bot

A Python-based command-line trading bot that places Market and Limit orders on the Binance Futures Testnet using the official Binance API.

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

```
TradingBotAssignment/
│
├── bot/
│   ├── client.py
│   ├── order.py
│   ├── validator.py
│   ├── logging_config.py
│   └── __init__.py
│
├── logs/
│   └── trading.log
│
├── .env
├── main.py
├── requirements.txt
├── README.md
└── test_connection.py
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/ShrutiKamble02/TradingBotAssignment.git
```

Move into project directory

```bash
cd TradingBotAssignment
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

BINANCE_API_KEY=AsJyKw9bo5qKAwa7BUL509cTngROmHd6z4tedYjum13Y6ZuMLddGiwSu3S1inlSi
BINANCE_API_SECRET=ta50yAeIKU26A3YyPtFWfc6foZ5GrtIOaIb6vINobwi1qBv2CJaBZB8i3dGoBJR7
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

---

## Notes

This project is configured for Binance Futures Testnet/Demo Trading. Valid API credentials with appropriate permissions are required to place live test orders.

---

## Author

Shruti Kamble