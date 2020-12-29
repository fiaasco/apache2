testinfra_hosts = ["debian10-apache2"]


def test_config(host):
    """ host specific checks
    """
    # Check if required config is in place
    a2 = host.file('/etc/apache2/apache2.conf')
    assert a2.contains('ServerName debian10-apache2')

    # Test requests
    http_resp = host.run('curl --head http://localhost')
    assert "Location: https://debian10-apache2" in http_resp.stdout
    # https_resp = host.run('curl --head --insecure https://debian10-apache2')
    # assert "200 OK" in https_resp.stdout
    # assert "Strict-Transport-Security: max-age=15768000" in https_resp.stdout
