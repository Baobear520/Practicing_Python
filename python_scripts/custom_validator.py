import json as js

class User:
    def __init__(self, first_name: str = None, last_name: str = None, age: int = None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


class BaseValidator:
    cls = None
    data = None

    def to_dict(self,json):
        return js.loads(json)

    def get_model_inst(self):
        return self.cls()

    def validate_fields(self, json):

        obj = self.get_model_inst()

        errors = {}
        json_data = self.to_dict(json)
        for k, v in self.data.items():
            required_field_name = v[0]
            data_type = v[1]
            if required_field_name in json_data:
                # The field exists
                # Continue validation
                json_field_value = json_data[required_field_name]
                if isinstance(json_field_value, data_type):
                    setattr(obj, k, json_field_value)
                else:
                    errors.update(
                        {
                        required_field_name: f"Unexpected data type (must be {data_type})"
                    }
                )
            else:
                errors.update(
                    {required_field_name: "A required_field"}
                )
        if errors:
            return None, errors
        return obj, None


class UserValidator(BaseValidator):
    cls = User
    data = {
        "first_name": ("firstName", str),
        "last_name": ("lastName", str),
        "age": ("age", int)
    }

json = '{"firstName": "Иван", "age": 25}'
print(UserValidator().validate_fields(json))