PHP 7
=========

Role that install php 7, php-fpm and some other packages related to php.

Requirements
------------

To test the roles you need [molecule](http://molecule.readthedocs.io/).

Role Variables
--------------

* `force_docker`: Forces the handlers to be executed when using the docker connection. Useful only when testing the role.

Dependencies
------------

None.

Example Playbook
----------------

```yaml
- hosts: servers
  roles:
  - { role: php7, force_docker: yes }
```

Tests
-----

```bash
molecule test --all
```

License
-------

GPL3

Author Information
------------------

Àlex Pérez-Pujol Gonzalez ( alexperez [ EN ] paradigmadigital.com )
