from dataclasses import dataclass


@dataclass(frozen=True)
class ClimateClassification:
    regime: str
    confidence: float


def classify_temperature_regime(temperature: float, humidity: float) -> ClimateClassification:
    if temperature >= 25 and humidity >= 60:
        return ClimateClassification("Warm and humid", 0.9)
    if temperature <= 10:
        return ClimateClassification("Cold", 0.9)
    return ClimateClassification("Moderate", 0.75)
