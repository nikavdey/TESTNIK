import pytest
import task_27_2b
from netmiko.cisco.cisco_ios import CiscoIosBase
from common_functions import check_attr_or_method
from base_connect_class import BaseSSH


def test_class_created():
    assert hasattr(task_27_2b, 'MyNetmiko'), "Надо создать класс MyNetmiko"


def test_class_inheritance(first_router_from_devices_yaml):
    r1 = task_27_2b.MyNetmiko(**first_router_from_devices_yaml)
    assert isinstance(r1, CiscoIosBase), "Класс MyNetmiko должен наследовать CiscoIosBase"
    check_attr_or_method(r1, attr='send_command')
    with pytest.raises(Exception) as excinfo:
        return_value = r1.send_config_set('lo')
    r1.disconnect()
