# Update package info
# custom HTTP  header must be X-Served-By

exec { 'apt-update':
  command => '/usr/bin/apt-get -y update',
  path    => ['/usr/bin', '/bin'],
}

# Install the Nginx package
package { 'nginx':
  ensure => installed,
}

# Create a HTML file
file { '/var/www/html/index.html':
  content => 'Hello World!',
}

# Configure Nginx to add the custom HTTP header
file_line { 'add custom header':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  line   => "\tadd_header X-Served-By ${hostname};",
  after  => 'server_name _;',
}

# Ensuring Nginx is running
service { 'nginx':
  ensure => running,
}
