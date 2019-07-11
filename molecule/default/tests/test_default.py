import os

import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('user,group,file,mode', [
    ('molecule', 'molecule', '', 0o700),
    ('molecule', 'molecule', 'id_rsa', 0o600),
    ('molecule', 'molecule', 'id_rsa.pub', 0o644),
    ('molecule', 'molecule', 'authorized_keys', 0o600),
])
def test_file_properties(host, user, group, file, mode):
    f = host.file('/home/{}/.ssh/{}'.format(user, file))
    t = 'is_file' if file else 'is_directory'

    assert f.exists
    assert getattr(f, t)
    assert f.user == user
    assert f.group == user
    assert f.mode == mode
