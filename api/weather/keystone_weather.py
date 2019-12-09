from weather.weather import Weather


class KeystoneWeather(Weather):
    def __init__(self):
        super().__init__("https://www.keystoneresort.com/api/PageApi/GetWeatherDataForHeader")

# Resort Snow Report Sections Functions
    def setSnowReportSections(self):
        self.snowReportSections = self.status['SnowReportSections']

    def getSnowReportSections(self):
        return self.snowReportSections

    def storeSnowReportSections(self):
        # store snowReportSections in dynamoDB
        print(self.snowReportSections)

    def runSnowReport(self):
        super().setStatus()
        self.setSnowReportSections()
        return self.getSnowReportSections()
