import os
import xml.etree.ElementTree as ET


class TemperatureConverter:
    def convert_celsius_to_fahrenheit(self, celsius):
        fahrenheit = float(9 / 5) * float(celsius) + float(32)
        return fahrenheit


class ForecastXmlParser:
    def __init__(self):
        self._converter = TemperatureConverter()

    def parse(self, file):
        tree = ET.parse(file)
        root = tree.getroot()

        for item in root.findall('item'):
            day = item.find('day').text
            celsius = item.find('temperature_in_celsius').text
            fahrenfeit = self._converter.convert_celsius_to_fahrenheit(celsius)
            print(f'{day}: {celsius} Celsius, {fahrenfeit:.2f} Fahrenheit')


forecast_file = os.getcwd() + "//forecast.xml"

forecast = ForecastXmlParser()
forecast.parse(forecast_file)



# Objectives

#     improving the student's skills in parsing XML documents;
#     using known methods of the Element object;

# Scenario

# Have you seen the weather forecast for the coming week? It’ll be an extremely sunny and warm week. Familiarize yourself with the data in the forecast.xml file and then complete the following tasks:

#     Create a class named TemperatureConverter and its convert_celsius_to_fahrenheit method. The convert_celsius_to_fahrenheit method should convert the temperature from Celsius to Fahrenheit. Use the following formula:

#     F = 9/5 * C + 32.

#     Create a class named ForecastXmlParser and its parse method responsible for reading data from forecast.xml. Use the TemperatureConverter class to convert the temperature from Celsius to Fahrenheit (rounded to one decimal place). The parse method should print the following results:

#     Monday: 28 Celsius, 82.4 Fahrenheit
#     Tuesday: 27 Celsius, 80.6 Fahrenheit
#     Wednesday: 28 Celsius, 82.4 Fahrenheit
#     Thursday: 29 Celsius, 84.2 Fahrenheit
#     Friday: 29 Celsius, 84.2 Fahrenheit
#     Saturday: 32 Celsius, 89.6 Fahrenheit
#     Sunday: 33 Celsius, 91.4 Fahrenheit

# NOTE: The forecast.xml file is available in your working directory at Edube Interactive. If you want to download the file and work with it locally, you can do it here: forecast.xml

#     Sandbox

# Code

#     Console

