[![Build Status](https://travis-ci.com/fiaasco/icinga2-master.svg?branch=master)](https://travis-ci.com/fiaasco/apache2)

# Ansible Role: Apache2

This role installs a configured Apache2 server.
The role supports Debian and Ubuntu.

## Requirements

Certificates are supposed to be in place.

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

* (Icinga2 documentation)[https://icinga.com/docs/]

## Author Information

Luc Stroobant
