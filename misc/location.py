from enum import IntEnum


class Location(IntEnum):
    LIVING_ROOM = 1
    OFFICE = 2
    KITCHEN = 3
    BASEMENT = 4
    MASTER_BED = 5
    KIDS_BED_1 = 6
    KIDS_BED_2 = 7
    UNKNOWN = 8

    def to_string(self):
        if self == Location.LIVING_ROOM:
            return 'living_room'
        elif self == Location.OFFICE:
            return 'office'
        elif self == Location.KITCHEN:
            return 'kitchen'
        elif self == Location.BASEMENT:
            return 'basement'
        elif self == Location.MASTER_BED:
            return 'master_bed'
        elif self == Location.KIDS_BED_1:
            return 'kids_bed_1'
        elif self == Location.KIDS_BED_2:
            return 'kids_bed_2'
        else:
            return 'unknown'

    @staticmethod
    def get_from_string(loc: str):
        loc = loc.lower()
        if loc == 'living_room':
            return Location.LIVING_ROOM
        elif loc == 'office':
            return Location.OFFICE
        elif loc == 'kitchen':
            return Location.KITCHEN
        elif loc == 'basement':
            return Location.BASEMENT
        elif loc == 'master_bed':
            return Location.MASTER_BED
        elif loc == 'kids_bed_1':
            return Location.KIDS_BED_1
        elif loc == 'kids_bed_2':
            return Location.KIDS_BED_2
        else:
            return Location.UNKNOWN
