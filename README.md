# docker_compose

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![GitHub release](https://img.shields.io/github/release/codeyourinfra/docker_compose.svg)](https://github.com/codeyourinfra/docker_compose/releases/latest) [![Build status](https://travis-ci.org/codeyourinfra/docker_compose.svg?branch=master)](https://travis-ci.org/codeyourinfra/docker_compose) [![Ansible Role](https://img.shields.io/ansible/role/29245.svg)](https://galaxy.ansible.com/codeyourinfra/docker_compose) [![Ansible Role downloads](https://img.shields.io/ansible/role/d/29245.svg)](https://galaxy.ansible.com/codeyourinfra/docker_compose)

Ansible role to install [docker-compose](https://docs.docker.com/compose).

## Example Playbook

```yml
---
- hosts: servers
  roles:
    - codeyourinfra.docker_compose
```

## Dependencies

The role is dependent of [Codeyourinfra Docker Ansible role](https://galaxy.ansible.com/codeyourinfra/docker), once we need Docker to run docker-compose. Docker is so installed before the docker-compose installation.

Please don't turn off facts, because the `codeyourinfra.docker` role requires the *ansible_distribution_release* variable, obtained through the [gathering facts phase](https://docs.ansible.com/ansible/latest/user_guide/playbooks_variables.html#information-discovered-from-systems-facts).

## Build process

The build process is performed in [Travis CI](https://travis-ci.org/codeyourinfra/docker_compose). During the build, the role is tested by using [Ubuntu Docker images with Python 3](https://hub.docker.com/r/codeyourinfra/python3).

The build is also triggered if any change is made in the `codeyourinfra.docker` role. After all, nobody wants some issue introduced by a change made in the upstream code :)

## Author Information

[@gustavomcarmo](https://github.com/gustavomcarmo) is a contributor of [Codeyourinfra](https://github.com/codeyourinfra). Get on board too! :)
