import subprocess

# Get a list of all installed packages
result = subprocess.run(['pip', 'freeze'], capture_output=True, text=True)
installed_packages = result.stdout.splitlines()

# Uninstall each package
for package in installed_packages:
    subprocess.run(['pip', 'uninstall', '-y', package.split('==')[0]])
