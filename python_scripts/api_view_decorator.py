

def api_view(authenticated=False):
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            if authenticated:
                try:
                    func(*args, **kwargs)
                except Exception as e:
                    print(f'{type(e).__name__} occurred.')
            else:
                print('Access denied')
        return wrapper
    return my_decorator


@api_view(authenticated=True)
def age_validating_api(name, age) -> None:
    print(f'Current user: \n name:{name}\n age:{age}')
    if 18 < age <= 50:
        print(f'{name} is an adult')
    elif age > 50:
        print(f'{name} is a senior citizen')
    else:
        print(f'{name} is an underage.')



user = {
    'names': 'John',
    'id': 1,
    'age': 99
}
def validate_params(data):
    name = data.get('name')
    age = data.get('age')
    if name is not None and age is not None:
        return name, age
    else:
        raise KeyError("One or both Required keys are missing in the data source.")


age_validating_api(*validate_params(user))




