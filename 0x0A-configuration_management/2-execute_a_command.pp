#killa a process named killmenow

exec {'kill_killmenow':
    command => 'pkill -f killmenow',
    path    => ['/usr/bin', '/usr/sbin']
}
