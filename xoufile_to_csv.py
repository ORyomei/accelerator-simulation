from io import TextIOWrapper
from typing import List, Tuple
import numpy as np


class XOU2CSV:
    TITLE_RUN_PARAMETERS = "--- Run parameters ---\n"
    TITLE_NODES = "--- Nodes ---\n"
    TITLE_REGION_PROPERTIES = "--- Region properties --- \n"
    TITLE_REGION_NAMES = "--- Region names --- \n"
    TITLES = [TITLE_RUN_PARAMETERS, TITLE_NODES,
              TITLE_REGION_PROPERTIES, TITLE_REGION_NAMES]
    PHI_COLLUM = 7
    K_COLLUM = 0
    L_COLLUM = 1

    runParametersRowRange: List[int]
    nodesRowRange: List[int]
    regionPropertiesRowRange: List[int]
    regionNamesRowRange: List[int]
    xouFileName: str
    runParameters: dict
    xMin: float
    xMax: float
    kMin: int
    yMin: float
    yMax: float
    lMax: float
    dUnit: float
    nReg: int
    iCylin: int

    def __init__(self, xouFileName: str, outputCsvFileName: str):
        self.xouFileName = xouFileName
        self.runParametersRowRange = list(range(2))
        self.nodesRowRange = list(range(2))
        self.regionPropertiesRowRange = list(range(2))
        self.regionNamesRowRange = list(range(2))
        with open(xouFileName, "r") as file:
            lines = file.readlines()
            self._findTitleRanges(lines)
            self._findRunParametersData(lines)

    def _findTitleRanges(self, lines: List[str]):
        for row, line in enumerate(lines):
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

        self.regionNamesRowRange[1] = len(lines) - 1

    def _findRunParametersData(self, lines: List[str]):
        runParameterlines = lines[self.runParametersRowRange[0] +
                                  1: self.runParametersRowRange[1] + 1]
        runParameters_ = [line.replace("\n", "").split(":")
                          for line in runParameterlines]
        for parameterStrs in runParameters_:
            if "." in parameterStrs[1]:
                parameterStrs[1] = float(parameterStrs[1])
            else:
                parameterStrs[1] = int(parameterStrs[1])
        self.runParameters = dict(runParameters_)

    def writeToCsv(self):
        skip_header = self.nodesRowRange[0] + 3
        max_rows = self.nodesRowRange[1] - self.nodesRowRange[0] - 2
        data = np.genfromtxt(
            self.xouFileName,
            skip_header=skip_header,
            max_rows=max_rows)
        # for i
        print(data)

    # f = open("eou/electrode.EOU")
# field = XOU2CSV("eou/electrode.EOU", "a")
# print(field.regionNamesRowRange)
# print(field.runParameters)
