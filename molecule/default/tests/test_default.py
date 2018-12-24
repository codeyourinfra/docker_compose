import os
import re
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_docker_is_installed(host):
    docker = host.package("docker-ce")
    assert docker.is_installed


def test_docker_compose_is_installed(host):
    cmd = host.run("docker-compose -v")
    assert cmd.rc == 0
    pattern = re.compile("^docker-compose version [\\d.]+")
    assert pattern.match(cmd.stdout)
