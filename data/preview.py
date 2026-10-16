def guess_type(value):
    """Given one value (as a string), guess what type of data it is."""
    if value == "":
        return "missing"
    try:
        int(value)
        return "whole number"
    except ValueError:
        pass
    try:
        float(value)
        return "decimal number"
    except ValueError:
        pass
    return "text"

print(guess_type("40578847"))    # a population value
print(guess_type("10.170"))      # a co2 value
print(guess_type("Afghanistan")) # a country name
print(guess_type(""))            # a missing gdp value
