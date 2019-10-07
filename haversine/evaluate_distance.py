import math


class Formula:

    def __init__(self, lat1=None, long1=None):

        if not lat1:
            self.lat1 = 52.339428
        else:
            self.lat1 = lat1

        if not long1:
            self.long1 = -7.257664
        else:
            self.long1 = long1

    def _calculate(self, lat2: float, lon2: float):

        earth_radius = 6372.8  # Earth radius in kilometers

        dLat = math.radians(lat2 - self.lat1)
        dLon = math.radians(lon2 - self.long1)
        lat1 = math.radians(self.lat1)
        lat2 = math.radians(lat2)

        a = math.sin(dLat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dLon / 2) ** 2
        c = 2 * math.asin(math.sqrt(a))

        return earth_radius * c
