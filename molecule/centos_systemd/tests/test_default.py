import os
import testinfra.utils.ansible_runner
import pytest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize("name", ['php70u-cli', 'php70u-common', 'php70u-fpm',
                                  'php70u-intl', 'php70u-mysqlnd',
                                  'php70u-mbstring',  'php70u-xml',
                                  'php70u-ldap', 'php70u-gd', 'php70u-bcmath'])
def test_packages(host, name):
    package = host.package(name)
    assert package.is_installed
