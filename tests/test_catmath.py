from catinabox import catmath


def test__cat_years_to_hooman_years__middle_age__succeeds():
    cat_age = 5
    assert catmath.cat_years_to_hooman_years(cat_age) == 25


def test__cat_years_to_hooman_years__less_than_one_year__succeeds():
    cat_age = .5
    assert catmath.cat_years_to_hooman_years(cat_age) == 2.5


def test__cat_years_to_hooman_years__0__returns_0():
    cat_age = 0
    assert catmath.cat_years_to_hooman_years(cat_age) == 0


# BONUS MATERIAL FOR STEP 2

def test__is_cat_leap_year__succeeds():
    assert catmath.is_cat_leap_year(2016) is True


def test__is_cat_leap_year__fails():
    assert catmath.is_cat_leap_year(1990) is False
