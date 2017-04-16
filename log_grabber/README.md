# Programming assignment week 11 #

## Design ##

### Specification list ###

 * Get log files from the router
 * Save it filtered to database.
    
### Task ###

Research how Juniper device logging commands work and what information we can
get ant actually want.

## Info ##

### Juniper log example ##

    Apr 11 10:27:25 router1 mgd[3606]: UI_DBASE_LOGIN_EVENT: User 'barbara' entering configuration mode
    Apr 11 10:32:22 router1 mgd[3606]: UI_DBASE_LOGOUT_EVENT: User 'barbara' exiting configuration mode
    Apr 11 11:36:15 router1 mgd[3606]: UI_COMMIT: User 'root' performed commit: no comment
    Apr 11 11:46:37 router1 mib2d[2905]: SNMP_TRAP_LINK_DOWN: ifIndex 82, ifAdminStatus up(1), ifOperStatus down(2), ifName at-1/0/0