from datetime import date

from workalendar.tests import GenericCalendarTest
from workalendar.europe import (
    Scotland,
    ScotlandAngus,
    ScotlandAyr,
    ScotlandCarnoustie,
    ScotlandClydebank,
    ScotlandDumfriesGalloway,
    ScotlandDundee,
    ScotlandEastDunbartonshire,
    ScotlandEdinburgh,
    ScotlandElgin,
    ScotlandFalkirk,
    ScotlandFife,
    ScotlandGlasgow,
    ScotlandInverclyde,
    ScotlandInverness,
    ScotlandKilmarnock,
    ScotlandLochaber,
    ScotlandMonifieth,
    ScotlandPaisley,
    ScotlandPerth,
    ScotlandScottishBorders,
    ScotlandStirling,
    ScotlandSouth,
    ScotlandSouthLanarkshire,
    ScotlandNorthLanarkshire,
    ScotlandWestDunbartonshire,
)


# Test mixins
class GoodFridayMixin(object):

    def test_good_friday_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 4, 18), holidays)  # Good friday


class EasterMondayMixin(object):

    def test_easter_monday_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 4, 21), holidays)  # Easter monday


class SpringHolidayFirstMondayAprilMixin(object):

    def test_spring_holiday_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 4, 7), holidays)  # Spring holiday


class SpringHolidaySecondMondayAprilMixin(object):

    def test_spring_holiday_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 4, 14), holidays)  # Spring holiday


class SpringHolidayTuesdayMondayMayMixin(object):
    "Test the 'Tuesday after 1st Monday in May' rule"
    def test_spring_holiday_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 5, 5), holidays)

    def test_spring_holiday_2012(self):
        # Special case: since May 1st is a Tuesday, it's not the 1st Tuesday
        holidays = self.cal.holidays_set(2012)
        self.assertIn(date(2012, 5, 8), holidays)


class VictoriaDayLastMondayBefore24MayMixin(object):
    "Test the 'Last Monday strictly before 24 May' rule"
    def test_victoria_day_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 5, 19), holidays)

    def test_victoria_day_2010(self):
        # Special case: May 24th is a Monday, but it's *strictly* this day
        holidays = self.cal.holidays_set(2010)
        self.assertIn(date(2010, 5, 17), holidays)


class SpringHolidayLastMondayMayMixin(object):
    def test_spring_holiday_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 5, 26), holidays)

    def test_spring_holiday_2011(self):
        holidays = self.cal.holidays_set(2011)
        self.assertIn(date(2011, 5, 30), holidays)


class VictoriaDayLastMondayMayMixin(object):
    def test_victoria_day_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 5, 26), holidays)

    def test_victoria_day_2011(self):
        holidays = self.cal.holidays_set(2011)
        self.assertIn(date(2011, 5, 30), holidays)


# -----------------------------------------------------------------------------
class ScotlandTest(GenericCalendarTest):
    cal_class = Scotland

    def test_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 1, 1), holidays)  # New year's day
        self.assertIn(date(2014, 1, 2), holidays)  # New year holiday
        self.assertIn(date(2014, 5, 5), holidays)  # May day
        self.assertIn(date(2014, 8, 4), holidays)  # Summer Holiday
        self.assertIn(date(2014, 11, 30), holidays)  # St. Andrew
        self.assertIn(date(2014, 12, 25), holidays)  # XMas
        self.assertIn(date(2014, 12, 26), holidays)  # Boxing day


class ScotlandInvernessTest(SpringHolidayFirstMondayAprilMixin, ScotlandTest):
    cal_class = ScotlandInverness

    def test_regional_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 2, 3), holidays)  # winter holiday
        self.assertIn(date(2014, 3, 3), holidays)  # 1st monday in march


class ScotlandLochaberTest(ScotlandTest):
    cal_class = ScotlandLochaber

    def test_regional_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 3, 31), holidays)  # last monday in march


class ScotlandAngusTest(SpringHolidaySecondMondayAprilMixin, ScotlandTest):
    cal_class = ScotlandAngus


class ScotlandAyrTest(
        GoodFridayMixin, EasterMondayMixin, SpringHolidayLastMondayMayMixin,
        ScotlandTest):
    cal_class = ScotlandAyr


class ScotlandCarnoustieTest(SpringHolidayFirstMondayAprilMixin, ScotlandTest):
    cal_class = ScotlandCarnoustie


class ScotlandClydebankTest(SpringHolidayTuesdayMondayMayMixin, ScotlandTest):
    cal_class = ScotlandClydebank


class ScotlandDumfriesGallowayTest(GoodFridayMixin, ScotlandTest):
    cal_class = ScotlandDumfriesGalloway


class ScotlandEastDunbartonshireTest(
        GoodFridayMixin, EasterMondayMixin, SpringHolidayLastMondayMayMixin,
        ScotlandTest):
    cal_class = ScotlandEastDunbartonshire


class ScotlandDundeeTest(
        SpringHolidayFirstMondayAprilMixin, VictoriaDayLastMondayMayMixin,
        ScotlandTest):
    cal_class = ScotlandDundee


class ScotlandFifeTest(SpringHolidayFirstMondayAprilMixin, ScotlandTest):
    cal_class = ScotlandFife


class ScotlandEdinburghTest(
        GoodFridayMixin, EasterMondayMixin,
        VictoriaDayLastMondayBefore24MayMixin,
        ScotlandTest):
    cal_class = ScotlandEdinburgh

    def test_spring_holiday_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 4, 14), holidays)  # Spring holiday, shifted

    def test_spring_holiday_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 4, 15), holidays)  # Spring holiday


class ScotlandElginTest(SpringHolidaySecondMondayAprilMixin, ScotlandTest):
    cal_class = ScotlandElgin


class ScotlandFalkirkTest(GoodFridayMixin, EasterMondayMixin, ScotlandTest):
    cal_class = ScotlandFalkirk


class ScotlandGlasgowTest(
        EasterMondayMixin, SpringHolidayLastMondayMayMixin,
        ScotlandTest):
    cal_class = ScotlandGlasgow


class ScotlandInverclydeTest(GoodFridayMixin, EasterMondayMixin, ScotlandTest):
    cal_class = ScotlandInverclyde

    def test_spring_holiday_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 4, 28), holidays)  # Spring holiday


class ScotlandKilmarnockTest(GoodFridayMixin, EasterMondayMixin, ScotlandTest):
    cal_class = ScotlandKilmarnock


class ScotlandMonifiethTest(SpringHolidayFirstMondayAprilMixin, ScotlandTest):
    cal_class = ScotlandMonifieth


class ScotlandNorthLanarkshireTest(
        EasterMondayMixin, SpringHolidayLastMondayMayMixin,
        ScotlandTest):
    cal_class = ScotlandNorthLanarkshire


class ScotlandPaisleyTest(
        GoodFridayMixin, EasterMondayMixin, VictoriaDayLastMondayMayMixin,
        ScotlandTest):
    cal_class = ScotlandPaisley


class ScotlandPerthTest(SpringHolidayFirstMondayAprilMixin, ScotlandTest):
    cal_class = ScotlandPerth

    def test_victoria_day_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 5, 26), holidays)


class ScotlandScottishBordersTest(
        SpringHolidayFirstMondayAprilMixin,
        ScotlandTest):
    cal_class = ScotlandScottishBorders


class ScotlandStirlingTest(
        GoodFridayMixin, EasterMondayMixin, SpringHolidayTuesdayMondayMayMixin,
        ScotlandTest):
    cal_class = ScotlandStirling


class ScotlandSouthTest(GoodFridayMixin, ScotlandTest):
    cal_class = ScotlandSouth


class ScotlandSouthLanarkshireTest(
        GoodFridayMixin, EasterMondayMixin, SpringHolidayLastMondayMayMixin,
        ScotlandTest):
    cal_class = ScotlandSouthLanarkshire


class ScotlandWestDunbartonshireTest(
        GoodFridayMixin, EasterMondayMixin,
        ScotlandTest):
    cal_class = ScotlandWestDunbartonshire