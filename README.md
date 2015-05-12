## USAGE

To run tests
    
    pybot --variable PARAMETER:value --variable PARAMETER2:value2 testsuite.txt

##Parameters:

 - VALID_USER : Valid username that has access to OpenStack
 - VALID_PASSWORD : Password for above user
 - USERNAME : Username used to login to newly created VM (Default debian)
 - ID_RSA : Full path to keyfile for above user
 - KEYRING_PASS : Password for keyfile (Default emtpy)
 - HOST : IP address/FQDN for newly created VM
 - TENANT : Tenant name under which Instance is started (Default: Digile.Devel)
 - IMAGE__NAME : Name of the newly created Instance ( Default: image_name)


