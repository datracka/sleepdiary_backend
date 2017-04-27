import accounts.constants as constant
from validate_email import validate_email


class Validator():
    REQUIRED = 'required';

    def __init__(self):
        pass

    def check(self, request, rules, messages):

        for field, value in request.data.items():
            field_rules = rules[field]
            # for every field, once we found a missed requirement we don't check anymore
            flag_condition_found = False
            for condition in field_rules:
                if not flag_condition_found:
                    if condition == constant.IS_REQUIRED:
                        message = self.validate_empty(value)
                        if message is not None:
                            messages['fields'][field] = message
                            flag_condition_found = True

                    if condition == constant.IS_EMAIL:
                        message = self.validate_email(value)
                        if message is not None:
                            messages['fields'][field] = message
                            flag_condition_found = True

                    if condition == constant.LENGTH_MIN_6:
                        message = self.validate_length(value, 6)
                        if message is not None:
                            messages['fields'][field] = message
                            flag_condition_found = True

        return messages

    def validate_length(self, value, length):
        if len(value) < length:
            return constant.LENGTH_MIN_6
        else:
            return None

    def validate_empty(self, value):

        if not value:
            return constant.IS_REQUIRED
        else:
            return None

    def validate_email(self, value):
        is_valid = validate_email(value)
        if not is_valid:
            return constant.IS_EMAIL
        else:
            return None
