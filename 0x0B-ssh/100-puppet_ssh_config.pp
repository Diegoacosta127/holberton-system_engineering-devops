# SSH client configuration
file { '/etc/ssh/ssh_config':
    ensure  => 'present',
    mode    => '0744',
    owner   => 'root',
    group   => 'root',
    content => 'Host * \n PasswordAuthentication yes\nIdentityFile ~/.ssh/school'
}