# import the module
import python_weather
import asyncio

async def getweather():
    # declare the client. format defaults to metric system (celcius, km/h, etc.)
    client = python_weather.Client(format=python_weather.IMPERIAL)

    # fetch a weather forecast from a city
    weather = await client.find("Washington DC")

    # returns the current day's forecast temperature (int)
    return weather.current.temperature

    # get the weather forecast for a few days
    # return weather.forecasts[0]
        # print(str(forecast.date), forecast.sky_text, forecast.temperature)

    # close the wrapper once done
    await client.close()

def get_wather():
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(getweather())