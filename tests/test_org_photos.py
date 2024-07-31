import pytest
from unittest.mock import patch, MagicMock
import os

# Import your script's functions
from org_photos import make_place_directories, extract_place, organize_photos

test_file_1 = "2018-01-03_Scotland_21_51_57.jpg"
test_file_2 = "2017-07-30_Cancun_07_50_45.jpg"
test_file_3 = "2016-09-04_Berlin_08_25_50.jpg"
# Test for extract_place
def test_extract_place():
    assert extract_place(test_file_1) == "Scotland"
    assert extract_place(test_file_2) == "Cancun"
    assert extract_place(test_file_3) == "Berlin"

# Test for make_place_directories
@patch('os.mkdir')
def test_make_place_directories(mock_mkdir):
    places = ["Scotland", "Cancun", "Berlin"]
    make_place_directories(places)
    # Ensure os.mkdir is called with the correct arguments
    for place in places:
        mock_mkdir.assert_any_call(place)

# Test for organize_photos
@patch('os.chdir')
@patch('os.listdir')
@patch('os.rename')
@patch('os.mkdir')
def test_organize_photos(mock_mkdir, mock_rename, mock_listdir, mock_chdir):
    # Setup mock return values
    mock_listdir.return_value = [test_file_1, test_file_2 ,test_file_3]
    
    # Mock for os.chdir, os.mkdir, os.rename
    organize_photos("test_directory")
    
    # Verify that os.chdir is called with the correct directory
    mock_chdir.assert_called_once_with("test_directory")
    
    # Verify that make_place_directories was called with the correct places
    mock_mkdir.assert_any_call("Scotland")
    mock_mkdir.assert_any_call("Cancun")
    
    # Verify that os.rename was called with the correct arguments
    mock_rename.assert_any_call(test_file_1, os.path.join("Scotland", test_file_1))
    mock_rename.assert_any_call(test_file_2, os.path.join("Cancun", test_file_2))

if __name__ == "__main__":
    pytest.main()
