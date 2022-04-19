# SSH client configuration
file { '/etc/ssh/ssh_config':
  ensure  => 'present',
  owner   => 'root',
  group   => 'root',
  mode    => '0744',
  content => 'Host * \n PasswordAuthentication yes\n IdentityFile ~/.ssh/school'
}
