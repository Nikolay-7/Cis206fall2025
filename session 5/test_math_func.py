import pytest
import math_func
from math_func import convert_weight_to_kg, convert_height_to_meters, calculate_bmi

def test_convert_weight():
    assert convert_weight_to_kg(220) == 99.79024
    #checks weight is correctly converted to kg

def test_convert_weight_invalid():
    with pytest.raises(ValueError):
        convert_weight_to_kg(2000)
        #tests that valuerror for weight above range is raised

def test_convert_height():
    assert convert_height_to_meters(5, 10) == 1.778
    #tests that height is correctly translated to meters

def test_convert_height_invalid():
    with pytest.raises(ValueError):
        convert_height_to_meters(5, 15)
        #tests that makes sure error is raised when input of inches is out of range

def test_calculate_bmi():
    assert calculate_bmi(70, 1.75) == 22.857142857142858
    #tests that BMI is being appropriately calculated
