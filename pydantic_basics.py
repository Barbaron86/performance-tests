from pydantic import BaseModel, Field, HttpUrl, EmailStr, ValidationError
from datetime import date
import uuid


class DocumentSchema(BaseModel):
    url: HttpUrl
    document: str


class UserSchema(BaseModel):
    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")
    phone_number: str = Field(alias="phoneNumber")




class CardSchema(BaseModel):
    id: str = "card_id"
    pin: str = "1234"
    cvv: str = "123"
    type: str = "PHYSICAL"
    status: str = "ACTIVE"
    account_id: str = Field(alias="accountId", default="account_id")
    card_number: str = Field(alias="cardNumber", default="1234123412341234")
    card_holder: str = Field(alias="cardHolder", default="Alise Smith")
    expiry_date: date = Field(alias="expiryDate", default=date(year=2027, month=3, day=25))
    payment_system: str = Field(alias="paymentSystem", default="VISA")


class AccountSchema(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    type: str = "CREDIT_CARD"
    cards: list[CardSchema] = Field(default_factory=list)
    status: str = "ACTIVE"
    balance: float = 25000


account_default_model = AccountSchema(
    id="account_id",
    type="CREDIT_CARD",
    cards=[
        CardSchema(
            id="card-id",
            pin="1234",
            cvv="123",
            type="PHYSICAL",
            status="ACTIVE",
            accountId="account-id",
            cardNumber="1234123412341234",
            cardHolder="Alise Smith",
            expiryDate=date(2027, 3, 25),
            paymentSystem="VISA",
        )
    ],
    status="ACTIVE",
    balance=100.57
)
print("Account default model:", account_default_model)

account_dict = {
    "id": "account_id",
    "type": "CREDIT_CARD",
    "cards": [
        {
            "id": "card-id",
            "pin": "1234",
            "cvv": "123",
            "type": "PHYSICAL",
            "status": "ACTIVE",
            "accountId": "account-id",
            "cardNumber": "1234123412341234",
            "cardHolder": "Alise Smith",
            "expiryDate": "2027-03-25",
            "paymentSystem": "VISA",
        }
    ],
    "status": "ACTIVE",
    "balance": 770.57
}
account_dict_model = AccountSchema(**account_dict)
print("Account dict model:", account_dict_model)

account_json = """
{
    "id": "account_id",
    "type": "CREDIT_CARD",
    "cards": [
        {
            "id": "card-id",
            "pin": "1234",
            "cvv": "123",
            "type": "PHYSICAL",
            "status": "ACTIVE",
            "accountId": "account-id",
            "cardNumber": "1234123412341234",
            "cardHolder": "Alise Smith",
            "expiryDate": "2027-03-25",
            "paymentSystem": "VISA"
        }
    ],
    "status": "ACTIVE",
    "balance": 770.57
}
"""

account_json_model = AccountSchema.model_validate_json(account_json)
print("Account json model:", account_json_model)

try:
    tariff = DocumentSchema(
        url="localhost",
        document="document_data"
    )
except ValidationError as error:
    print(error)
    print(error.errors())
