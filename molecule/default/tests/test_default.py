import os

import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_ssh_dir(host):
    f = host.file('/home/molecule/.ssh')

    assert f.exists
    assert f.is_directory
    assert f.user == 'molecule'
    assert f.group == 'molecule'
    assert f.mode == 0o700


@pytest.mark.parametrize('user,group,key,mode', [
    ('molecule', 'molecule', 'id_rsa', 0o600),
    ('molecule', 'molecule', 'id_rsa.pub', 0o644),
])
def test_ssh_key(host, user, group, key, mode):
    f = host.file('/home/{}/.ssh/{}'.format(user, key))

    assert f.exists
    assert f.is_file
    assert f.user == user
    assert f.group == user
    assert f.mode == mode
