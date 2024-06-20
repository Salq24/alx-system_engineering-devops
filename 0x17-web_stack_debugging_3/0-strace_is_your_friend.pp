# a script rhat uses strace and puppet to solve issues

exec {'fix_code':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path => '/usr/local/bin/:/bin/'
}

