import logging
import random

logger = logging.getLogger(__name__)

FORMAT = "%(levelname)s - %(message)s"
handler = logging.FileHandler('battery_temperature.log', 'a')
formatter = logging.Formatter(FORMAT)

handler.setFormatter(formatter)
logger.addHandler(handler)

# logging.basicConfig(filename='battery_temperature.log ', filemode='a', format=FORMAT)
for _ in range(0, 60):
    temperature_in_celsius = random.randint(0, 100)
    if temperature_in_celsius < 20:
        logger.debug(str(temperature_in_celsius) + ' C')
    elif temperature_in_celsius >= 30 and temperature_in_celsius <= 35:
        logger.warning(str(temperature_in_celsius) + ' C')
    elif temperature_in_celsius > 35:
        logger.critical(str(temperature_in_celsius) + ' C')

# DEBUG = TEMPERATURE_IN_CELSIUS < 20
# WARNING = TEMPERATURE_IN_CELSIUS >= 30 AND TEMPERATURE_IN_CELSIUS <= 35
# CRITICAL = TEMPERATURE_IN_CELSIUS > 35