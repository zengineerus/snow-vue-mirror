import api.handlers.Library.Resort as Resort


class Keystone(Resort):
    def __init__(self, userLocation):
        super().__init__(self, "https://www.keystoneresort.com/api/PageApi/GetWeatherDataForHeader",
                         "100+Dercum+Square+Keystone+CO", userLocation)

# Resort Snow Report Sections Functions
    def setSnowReportSections(self):
        self.snowReportSections = self.status['SnowReportSections']

    def getSnowReportSections(self):
        return self.snowReportSections

    def storeSnowReportSections(self):
        # store snowReportSections in dynamoDB
        print(self.snowReportSections)

    def runSnowReport(self):
        self.setStatus().setSnowReportSections().getSnowReportSections()
