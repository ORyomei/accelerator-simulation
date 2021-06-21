from io import TextIOWrapper
from typing import List


class XOU2CSV:
    TITLE_RUN_PARAMETERS = "--- Run parameters ---\n"
    TITLE_NODES = "--- Nodes ---\n"
    TITLE_REGION_PROPERTIES = "--- Region properties --- \n"
    TITLE_REGION_NAMES = "--- Region names --- \n"
    TITLES = [TITLE_RUN_PARAMETERS, TITLE_NODES,
              TITLE_REGION_PROPERTIES, TITLE_REGION_NAMES]

    runParametersRowRange: List[int]
    nodesRowRange: List[int]
    regionPropertiesRowRange: List[int]
    regionNamesRowRange: List[int]
    lines: List[str]

    def __init__(self, fileName: str, outputCsvFileName: str):
        self.file = open(fileName)
        self.runParametersRowRange = list(range(2))
        self.nodesRowRange = list(range(2))
        self.regionPropertiesRowRange = list(range(2))
        self.regionNamesRowRange = list(range(2))
        self.lines = self.file.readlines()
        self._findTitleRanges()

    def _findTitleRanges(self):
        for row, line in enumerate(self.lines):
            if line == XOU2CSV.TITLE_RUN_PARAMETERS:
                findingRange = self.runParametersRowRange
                self.runParametersRowRange[0] = row

            if line == XOU2CSV.TITLE_NODES:
                findingRange = self.nodesRowRange
                self.nodesRowRange[0] = row

            if line == XOU2CSV.TITLE_REGION_PROPERTIES:
                findingRange = self.regionPropertiesRowRange
                self.regionPropertiesRowRange[0] = row

            if line == XOU2CSV.TITLE_REGION_NAMES:
                findingRange = self.regionNamesRowRange
                self.regionNamesRowRange[0] = row

            if line == "" or line == "\n":
                findingRange[1] = row - 1

        self.regionNamesRowRange[1] = len(self.lines) - 1

    def parsePotential(self):
        pass


# f = open("eou/electrode.EOU")
# field = XOU2CSV(f, "a")
# print(field.regionNamesRowRange)
