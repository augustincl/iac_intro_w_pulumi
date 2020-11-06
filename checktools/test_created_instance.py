import testinfra
import pytest

#check if the version of nginx is newer than 1.17.0
#@pytest.mark.skip
def test_nginx_version(host):
    
    #check if nginx is installed first to prevent the test blows
    assert host.package("nginx").is_installed

    ver = host.package("nginx").version.split('-')[0]
    assert ver >= "1.14.0"

#make sure the owner and mode of nginx config file is correct
#@pytest.mark.skip
def test_nginx_config(host):
    assert host.file("/etc/nginx/nginx.conf").user == "root"
    assert host.file("/etc/nginx/nginx.conf").mode == 0o644

