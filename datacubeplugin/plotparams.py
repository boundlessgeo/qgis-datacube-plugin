from qgis.core import QgsRaster

class PlotParameter():

    def __str__(self):
        return self.name

class BandValue(PlotParameter):

    def __init__(self, idx):
        self.idx = idx
        self.name =  "Band " + str(self.idx + 1)

    def value(self, layer, pt):
        try:
            value = layer.dataProvider().identify(pt,
                QgsRaster.IdentifyFormatValue).results().values()[self.idx]
            return value
        except IndexError:
            return None

class NDVI(PlotParameter):

    name = "NDVI"

    def value(self, layer, pt):
        pass

class EVI(PlotParameter):

    name = "EVI"

    def value(self, layer, pt):
        pass

class NDWI(PlotParameter):

    name = "NDWI"

    def value(self, layer, pt):
        pass

class NDBI(PlotParameter):

    name = "NDBI"

    def value(self, layer, pt):
        pass

class WOFS(PlotParameter):

    name = "WOFS"

    def value(self, layer, pt):
        pass

class TSM(PlotParameter):

    name = "TSM"

    def value(self, layer, pt):
        pass

class BS(PlotParameter):

    name = "BS"

    def value(self, layer, pt):
        pass

class PV(PlotParameter):

    name = "PV"

    def value(self, layer, pt):
        pass

class NPV(PlotParameter):

    name = "NPV"

    def value(self, layer, pt):
        pass


parameters = [BandValue(i) for i in range(9)]
parameters.extend([NDVI(), NDBI(), EVI(), NDWI(), WOFS(), TSM(), BS(), PV(), NPV()])