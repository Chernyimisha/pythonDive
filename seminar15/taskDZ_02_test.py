import pytest
import os
import shutil
from seminar15.taskDZ_02 import dir_parser, cl_parser
from collections import namedtuple


@pytest.fixture
def create_result(request):
    """
    Фикстура выполнит создание папки test_folder с 5 и 25 вложенными папками и файлами соответственно.
    Данные о количестве объектов будем использовать в переменной data_fixture, data_fixture_folder и
    data_fixture_file.
    """
    os.mkdir('test_folder')
    for i in range(5):
        dir_name = f'test_folder/test_folder{i}'
        os.mkdir(dir_name)
        for j in range(5):
            file_name = f'{dir_name}/test_file{j}.txt'
            with open(file_name, 'w'):
                pass

    def delete_test_folder():
        shutil.rmtree('test_folder')
    request.addfinalizer(delete_test_folder)
    return dir_parser('test_folder')


def test_count_objects_in_result(create_result):
    """Проверим сколько будет всего объектов в результате парсинга"""
    data_fixture = 30
    assert len(create_result) == data_fixture, 'Error'


def test_count_folder_in_result(create_result):
    """Проверим сколько будет папок в результате парсинга"""
    data_fixture_folder = 5
    count_folder = 0
    for obj in create_result:
        if str(type(obj)).find('Folder') != -1:
            count_folder += 1
    assert count_folder == data_fixture_folder, 'Error'


def test_count_file_in_result(create_result):
    """Проверим сколько будет файлов в результате парсинга"""
    data_fixture_file = 25
    count_file = 0
    for obj in create_result:
        if str(type(obj)).find('File') != -1:
            count_file += 1
    assert count_file == data_fixture_file, 'Error'


def test_attribute(create_result):
    """Проверим наличие аттрибутов в результате парсинга"""
    for obj in create_result:
        if str(type(obj)).find('File') != -1:
            assert obj.name is not None, 'Error'
            assert obj.extension is not None, 'Error'
            assert obj.parent_dir is not None, 'Error'
        else:
            assert obj.name is not None, 'Error'
            assert obj.flag is not None, 'Error'
            assert obj.parent_dir is not None, 'Error'

