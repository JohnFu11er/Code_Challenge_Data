# Ansible_3 Weekly Code Challenge

## Easy:
1. Create an ansible playbook that makes a directory named router_configs.


## Medium:
1. Create an ansible playbook that makes a directory named router_configs.
2. Using the attached device_var.yml file, create a file in the the Router_configs folder for each router.  The files will be named using the routers name followed by ".cfg".  Ex: Router_1.cfg
3. Use the attached router_config.j2 file to create a config file for each router in the device_var.yml file and save that config file to the router_configs directory.


## Hard:
1. Create an ansible playbook that makes a directory named router_configs.
2. Using the attached device_var.yml file, create a file in the the Router_configs folder for each router.  The files will be named using the routers name followed by ".cfg".  Ex: router_1.cfg
3. Use the attached router_config.j2 file to create a config file for each router in the device_var.yml file and save that config file to the router_configs directory.
4. Uncomment the jinja template "include" calls in the router_config.j2 file so that the child jinga files are called in the running of the router_config.j2 file
5. Properly configure the child jinga templates ( eigrp.j2 , interfaces.j2 , static_routes.j2 ) for importing all the appropriate variables into the router_config.2 file