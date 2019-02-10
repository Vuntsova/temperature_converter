class NoTemperatureException(Exception):
    pass


class TempConverter(object):
    
    # initilizing the class attributes
    def __init__(self, celsius=None, fahrenheit=None):
        # condition that raises exception for mendatory attribute
        if not celsius and not fahrenheit:
            raise NoTemperatureException("*************Provide temperature**********")
        # setting the attributes for the isinstances
        self.celsius = celsius
        self.farenheit = fahrenheit
        
    # METHODS:
    # to celsius method that will convert the temperature from celsius to farenheit IF the temperature is not provided in celsius:
    def to_celsius(self):
        if self.celsius is not None:
            return self.celsius
        # (temp_fahrenheit - 32) * 5/9 --->celsius to farenheit formula. Round to one decimal place
        return round(float((self.farenheit - 32) * 5/9) , 1)
    # to farenheit method that will convert the temperature from farenheit to celsius IF the temperature is not provided in farenheit:
    def to_fahrenheit(self):
        if self.farenheit is not None:
            return self.farenheit
        # (temp_celsius * 9/5) + 32 --->farenheit to celsius formula. Round to one decimal place
        return round(float((self.celsius * 9/5) + 32 ), 1)
