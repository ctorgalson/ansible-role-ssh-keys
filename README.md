# Ansible Role SSH Keys

![](https://github.com/ctorgalson/ansible-role-oh-my-zsh/workflows/Molecule%20Test/badge.svg)

This role allows management of SSH and authorized keys independently of users.

## Requirements

No special requirements.

## Role Variables

| Variable name              | Default value                       | Description |
|----------------------------|-------------------------------------|-------------|
| `ssh_user`                 | `undefined`                         | Name of ssh key owner. |
| `ssh_user_home`            | `/home/{{ ssh_user }}`              | Derived path to owner's home directory. |
| `ssh_ssh_dir`              | `{{ ssh_user_home }}/.ssh`          | Derived path to owner's .ssh directory. |
| `ssh_ssh_dir_owner`        | `{{ ssh_user }}`                    | Owner of .ssh directory. |
| `ssh_ssh_dir_group`        | `{{ ssh_user }}`                    | Group of .ssh directory. |
| `ssh_ssh_dir_mode`         | `0700`                              | Default permissions for .ssh directory. |
| `ssh_ssh_keys`             | `[]`                                | List of ssh keys. |
| `ssh_authorized_keys_file` | `{{ ssh_ssh_dir }}/authorized_keys` | Derived path to owner's authorized_keys file. |
| `ssh_authorized_keys_mode` | `0600`                              | Default permissions for authorized_keys file. |
| `ssh_authorized_keys`      | `[]`                                | List of paths to public keys to be added to authorized_keys file. |

### `ssh_ssh_keys` Structure

The `ssh_ssh_keys` var is a list of the properties of the keys. The
`src` property is mandatory, but the `mode` property can be omitted:

    ssh_ssh_keys:
      - src: path/to/private_key
        mode: 0600
      - src: path/to/public_key.pub
        mode: 0644

### `ssh_authorized_keys` Structure

The `ssh_authorized_keys` var is a simple list of paths:

    ssh_authorized_keys:
      - path/to/public_key_1.pub
      - path/to/public_key_2.pub

### Linux vs macOS

- On linux systems, only one variable besides `ssh_ssh_keys` and/or
  `ssh_authorized_keys`_must_ be set: `ssh_user`.
- On macOS hosts, two variables besides `ssh_ssh_keys` and/or
  `ssh_authorized_keys` _must_ be set: `ssh_user` and `ssh_user_home`.

## Dependencies

None.

## Example Playbook

    - hosts: servers
      vars:
        ssh_user: "username"
        ssh_ssh_keys:
          - src: "files/keys/id_rsa"
          - src: "files/keys/id_rsa.pub"
        ssh_authorized_keys:
          - "files/authorized_keys/keyname.pub"
      role:
         - ansible-role-ssh-keys

## License

GPLv3

## Author Information

Christopher Torgalson
