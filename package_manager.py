import json
import os
import requests
import zipfile
import tempfile

CONFIG_FILE = 'config.json'

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    return {"installed_packages": {}}

def save_config(config):
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f, indent=4)

def install_package(repo_url):
    config = load_config()
    repo_name = repo_url.split('/')[-1]
    
    if repo_name in config["installed_packages"]:
        print(f"{repo_name} is already installed.")
        return
    
    with tempfile.TemporaryDirectory() as tmpdirname:
        zip_path = os.path.join(tmpdirname, f"{repo_name}.zip")
        with requests.get(f"{repo_url}/archive/refs/heads/main.zip", stream=True) as r:
            r.raise_for_status()
            with open(zip_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
        
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(tmpdirname)
        
        extracted_dir = os.path.join(tmpdirname, f"{repo_name}-main")
        os.system(f'pip install {extracted_dir}')
        
        config["installed_packages"][repo_name] = repo_url
        save_config(config)
        print(f"Installed {repo_name} from {repo_url}")

def uninstall_package(package_name):
    config = load_config()
    if package_name not in config["installed_packages"]:
        print(f"{package_name} is not installed.")
        return
    
    os.system(f'pip uninstall -y {package_name}')
    del config["installed_packages"][package_name]
    save_config(config)
    print(f"Uninstalled {package_name}")

def list_packages():
    config = load_config()
    for package, url in config["installed_packages"].items():
        print(f"{package}: {url}")

def main():
    import argparse

    parser = argparse.ArgumentParser(description="Simple GitHub package manager.")
    parser.add_argument('pal', choices=['install', 'uninstall', 'list'])
    parser.add_argument('package', nargs='?', help='Package to install/uninstall')

    args = parser.parse_args()

    if args.pal == 'install' and args.package:
        install_package(args.package)
    elif args.pal == 'uninstall' and args.package:
        uninstall_package(args.package)
    elif args.pal == 'list':
        list_packages()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
