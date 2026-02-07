import configparser

# --- STEP 0: Create the "mess.ini" file for testing ---
mess_content = """
[sentry]
env = prod
key = key
secret = secret

[mariadb]
env = dev
host = localhost
name = hello
user = user
password = password

[github]
env = prod
user = user
password = password

[redis]
env = dev
host = localhost
port = 6379
db = 0
"""
with open('mess.ini', 'w') as f:
    f.write(mess_content)

# --- STEP 1: Parse the messy configuration file ---
config = configparser.ConfigParser()
config.read('mess.ini')

# Create two new ConfigParser objects for our separated files
prod_config = configparser.ConfigParser()
dev_config = configparser.ConfigParser()

# --- STEP 2: Iterate and Distribute Sections ---
for section in config.sections():
    # Get the environment value
    env_type = config.get(section, 'env')
    
    # Create a dictionary of all options in this section
    options = dict(config.items(section))
    
    # Remove the 'env' key as requested
    options.pop('env', None)
    
    # Assign to the appropriate config object
    if env_type == 'prod':
        prod_config[section] = options
    elif env_type == 'dev':
        dev_config[section] = options

# --- STEP 3: Write the new configuration files ---
with open('prod_config.ini', 'w') as prod_file:
    prod_config.write(prod_file)

with open('dev_config.ini', 'w') as dev_file:
    dev_config.write(dev_file)

print("Separation complete: prod_config.ini and dev_config.ini have been created.")