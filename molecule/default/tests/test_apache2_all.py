import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('pkg', ['apache2', 'libapache2-mod-security2'])
def test_package(host, pkg):
    """ check if packages are installed
    """
    assert host.package(pkg).is_installed


def test_service(host):
    """ Testing whether the service is running and enabled
    """
    assert host.service('apache2').is_enabled
    assert host.service('apache2').is_running


def test_config(host):
    """ basic configuration checks
    """
    ssl = host.file('/etc/apache2/mods-available/ssl.conf')
    assert ssl.contains('SSLHonorCipherOrder     Off')
    ports = host.file('/etc/apache2/ports.conf')
    assert ports.contains('# Ansible managed')
    assert host.file('/etc/apache2/sites-available/admin-vhost.conf').exists
    # assert host.file('/etc/apache2/sites-available/admin-vhost-ssl.conf').exists

    # Check if correct vhosts are active
    assert not host.file('/etc/apache2/sites-enabled/000-default.conf').exists
    assert host.file('/etc/apache2/sites-enabled/admin-vhost.conf').is_symlink
    # assert host.file('/etc/apache2/sites-enabled/admin-vhost-ssl.conf').is_symlink

    # Check if correct modules are active
    assert host.file('/etc/apache2/mods-enabled/ssl.conf').exists
    assert host.file('/etc/apache2/mods-enabled/actions.load').exists
    assert host.file('/etc/apache2/mods-enabled/deflate.load').exists
    assert host.file('/etc/apache2/mods-enabled/rewrite.load').exists
    assert host.file('/etc/apache2/mods-enabled/headers.load').exists
    assert host.file('/etc/apache2/mods-enabled/remoteip.load').exists
    assert host.file('/etc/apache2/mods-enabled/http2.load').exists
