from dataspec import ValidationError


def parse_spec_to_readable_message(ex: ValidationError):
    invalidations = []
    for e in ex.errors:
        if e.message == 'Value is not a mapping type':
            f"Invalid type provided: {e.pred.keys()}"
        else:
            allowed = ', '.join(list(map(str, e.pred)))
            field_name = '.'.join(list(map(str, e.path)))
            invalidations.append(
                f"Provided value {e.value} for parameter {field_name} is invalid. The allowed values are: {allowed}")
    return invalidations
