from .. import Resort as Resort 

class Keystone(Resort):
    def __init__(self):
        super().__init__(self, "https://www.keystoneresort.com/api/PageApi/GetWeatherDataForHeader", "100+Dercum+Square+Keystone+CO") 

#Resort Snow Report Sections Functions
    def setSnowReportSections(self):
        self.snowReportSections = self.status['SnowReportSections']

    def getSnowReportSections(self):
        return self.snowReportSections

    def storeSnowReportSections(self):
        #store snowReportSections in dynamoDB
        print(self.snowReportSections)
