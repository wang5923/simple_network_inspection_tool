import re

from netmiko import BaseConnection

from API.decorator import DataHandle

data = DataHandle()

__all__ = ['backup_config', 'test1', 'test2', 'test3']


@data.backup_config
def backup_config(conn: BaseConnection):
    output = conn.send_command(command_string='display cu')
    file_names = re.search(r'sysname\s(.*)', output).group(1)
    file_name = f'{file_names}.txt'
    data = output
    return data, file_name


def test1():
    print("H3C模块1")


def test2():
    print("H3C模块2")


def test3():
    print("H3C模块3")
