from pydantic import BaseModel, Field

order_data = {
    "Order-Number": "A-12345",
    "customerEmail": "test@test.com",
    "@status": "paid",
    "from": "Web",
}


class Order(BaseModel):
    order_number: str = Field(alias="Order-Number")
    customer_email: str = Field(alias="customerEmail")
    status: str = Field(alias="@status")
    source: str = Field(alias="from")


order = Order.model_validate(order_data)

print(order.order_number)
print(order.source)

back_to_json = order.model_dump(by_alias=True)
print(back_to_json)
