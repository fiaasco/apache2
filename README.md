[![Build Status](https://travis-ci.org/fiaasco/apache2.svg?branch=master)](https://travis-ci.org/fiaasco/apache2)

# Ansible Role: Apache2

This role installs a configured Apache2 server.
The role supports Debian and Ubuntu.

## Requirements

Certificates are supposed to be in place (possible example in the molecule test preparation).

## Role Variables

Role variables are documented inline in the following files:
- Variables in defaults/main.yml
- Constants in vars/main.yml


## Dependencies

None

## Examples

    - hosts: servers
      roles:
         - role: apaches2

## Tags

No tags available.

## License

MIT

## Further Reading


## Author Information

Luc Stroobant
