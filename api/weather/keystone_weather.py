from weather.weather import Weather


class KeystoneWeather(Weather):
    def __init__(self):
        super().__init__("https://www.keystoneresort.com/api/PageApi/GetWeatherDataForHeader")

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
        return self.get_snow_report_sections()
