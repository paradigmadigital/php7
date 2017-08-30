import os
import testinfra.utils.ansible_runner
import pytest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize("name", ['php7.0-cli',
                                  'php7.0-common', 'php7.0-fpm', 'php7.0-intl',
                                  'php7.0-mysql', 'php7.0-mbstring',
                                  'php7.0-xml', 'php7.0-ldap', 'php7.0-gd',
                                  'php7.0-bcmath'])
def test_packages(host, name):
    package = host.package(name)
    assert package.is_installed
