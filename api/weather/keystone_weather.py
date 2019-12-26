from weather.weather import Weather
from datetime import datetime

class KeystoneWeather(Weather):
    def __init__(self):
        super().__init__("https://www.keystoneresort.com/api/PageApi/GetWeatherDataForHeader")
        self.resort_name = "Keystone"

# Resort Snow Report Sections Functions
    def set_snow_report_sections(self):
        self.snow_report_sections = self.status['SnowReportSections']

    def get_snow_report_sections(self):
        return self.snow_report_sections

    def store_snow_report_sections(self):
        # store snowReportSections in dynamoDB
        print(self.snow_report_sections)

    def run_snow_report(self):
        super().set_status()
        self.set_snow_report_sections()
        return self.transform_api_data(self.get_snow_report_sections())

    def transform_api_data(self, data):
        # error handle
        overnight = None
        twentyFourHour = None
        for item in data["SnowReportSections"]:
            if "Overnight" in item["Description"]:
                overnight = item["Depth"]
            if "24 Hour" in item["Description"]:
                twentyFourHour = item["Depth"]
        return {
            "error": None,
            "overnight": {
                "inches": overnight["Inches"],
                "centimeters": overnight["Centimeters"]
            },
            "twentyFourHour": {
                "inches": twentyFourHour["Inches"],
                "centimeters": twentyFourHour["Centimeters"]
            },
            "timestamp": datetime.utcnow().isoformat(),
            "resort": "Keystone"
        }