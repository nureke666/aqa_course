from pydantic import BaseModel, model_validator

order_data = {
    "item_name": "Пицца Маргарита",
    "delivery_type": "courier",
    "address": "ул. Пушкина, дом Колотушкина",
}


class OrderInfo(BaseModel):
    item_name: str
    delivery_type: str
    address: str | None = None

    @model_validator(mode="after")
    def check_delivery_type(self):
        if self.delivery_type == "courier" and self.address is None:
            raise ValueError("For courier delivery type you should write address!")
        return self


order = OrderInfo.model_validate(order_data)
print("SUCCESS")
