from binance.enums import *
from bot.logging_config import setup_logger

logger = setup_logger()


class OrderManager:
    def __init__(self, client):
        self.client = client

    def place_order(self, symbol, side, order_type, quantity, price=None):
        """
        Place MARKET or LIMIT order.
        """

        try:
            logger.info(
                f"Order Request -> Symbol={symbol}, Side={side}, Type={order_type}, Quantity={quantity}, Price={price}"
            )

            if order_type == "MARKET":

                response = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type=FUTURE_ORDER_TYPE_MARKET,
                    quantity=quantity,
                )

            elif order_type == "LIMIT":

                response = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type=FUTURE_ORDER_TYPE_LIMIT,
                    quantity=quantity,
                    price=price,
                    timeInForce=TIME_IN_FORCE_GTC,
                )

            else:
                raise ValueError("Unsupported order type.")

            logger.info(f"Order Response -> {response}")

            print("\n========== ORDER SUCCESS ==========")
            print(f"Order ID      : {response.get('orderId')}")
            print(f"Status        : {response.get('status')}")
            print(f"Symbol        : {response.get('symbol')}")
            print(f"Side          : {response.get('side')}")
            print(f"Type          : {response.get('type')}")
            print(f"Quantity      : {response.get('origQty')}")
            print(f"Executed Qty  : {response.get('executedQty')}")
            avg_price = response.get("avgPrice", "N/A")
            print(f"Price         : {response.get('price')}")
            print(f"Average Price : {avg_price}")
            
            print("===================================\n")

            return response

        except Exception as e:
            logger.error(f"Order Failed -> {e}")
            print(f"\n Error: {e}\n")
            raise