from lib.rm import rm

def test_rm_for_file_that_exists(mocker):
    mocked_os_remove = mocker.patch('os.remove')
    mocked_os_path = mocker.patch('os.path')

    mocked_os_path.isfile.return_value = True

    rm('some_file.txt')
    
    mocked_os_remove.assert_called_with('some_file.txt')

def test_rm_for_file_that_does_not_exist(mocker):
    mocked_os_remove = mocker.patch('os.remove')
    mocked_os_path = mocker.patch('os.path')

    mocked_os_path.isfile.return_value = False

    rm('some_mythical_file.txt')
    
    assert not mocked_os_remove.called
