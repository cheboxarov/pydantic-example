from pydantic import ValidationError
import json
from city import City
from user import User
from product import Product

input_json = json.dumps(
    {
        "id": 123,
        "name": "Mocow",
        "population": "123",
        "tags": [
            {
                "id": 1,
                "name": "Mocow",
            }
        ],
    }
)

try:
    city = City.model_validate_json(str(input_json))
    print(city)
except ValidationError as error:
    print(error.json())


json_user = json.dumps(
    {
        "id": 123,
        "name": "Vanya",
    }
)

try:
    user = User.model_validate_json(str(json_user))
    print(user)
except ValidationError as error:
    print(error.json())


input_data = {"id": 1, "name": "Laptop", "sku": "ABC12345"}  # Корректный SKU

try:
    product = Product(**input_data)
    print(product)
except ValidationError as e:
    print(e.json())

input_data_invalid = {"id": 2, "name": "Tablet", "sku": "abc123"}  # Некорректный SKU

try:
    product_invalid = Product(**input_data_invalid)
    print(product_invalid)
except ValidationError as e:
    print(e.json())
