"""Weather client abstraction for feature enrichment."""

from dataclasses import dataclass


@dataclass
class WeatherSnapshot:
    temperature_c: float
    humidity: float
    wind_speed_mps: float


def get_weather_stub() -> WeatherSnapshot:
    """Return static weather data placeholder until API integration is wired."""
    return WeatherSnapshot(temperature_c=31.5, humidity=0.62, wind_speed_mps=3.1)
