import pandas as pd
import stacksurvey as so


def test_median_by_undergrad():
    # Arrange
    data = pd.DataFrame(
        {
            "NotTheSalaryColumn": [],
            "NotTheMajorColumn": [],
        }
    )

    # Act
    salaries = so.median_by_undergrad(data)

    # Assert
    assert salaries.name == "Median Salary"
    assert salaries.index.name == "Undergraduate Major"


def test_quantiles():
    pass


def test_ecdf():
    pass


def test_gt_50_k():
    pass
