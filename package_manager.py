import os
import subprocess
import argparse

# Function to install the repository if it has a "PAL" prefix
def install_repo(repo_url):
    if not repo_url.startswith("PAL"):
        print("Error: Repository URL must start with 'PAL'.")
        return

    # Replace "PAL" with the actual URL
    repo_url = repo_url.replace("PAL", "https://github.com/")

    # Create .apps directory if it doesn't exist
    if not os.path.exists(".apps"):
        os.makedirs(".apps")

    # Extract the repo name from the URL
    repo_name = repo_url.split("/")[-1]

    # Define the path where the repo will be cloned
    clone_path = os.path.join(".apps", repo_name)

    # Clone the repo into the .apps directory
    subprocess.run(["git", "clone", repo_url, clone_path])

    print(f"Installed {repo_name} to .apps/{repo_name}")

# Function to list installed applications
def list_apps():
    if not os.path.exists(".apps"):
        print("No applications installed.")
        return

    apps = os.listdir(".apps")
    if apps:
        print("Installed applications:")
        for app in apps:
            print(f"- {app}")
    else:
        print("No applications installed.")

# Main function to handle command-line arguments
def main():
    parser = argparse.ArgumentParser(description="PAL Package Manager")
    parser.add_argument("command", choices=["install", "list"], help="Command to execute")
    parser.add_argument("repo_url", nargs="?", help="Repository URL to install")
    args = parser.parse_args()

    if args.command == "install":
        if args.repo_url:
            install_repo(args.repo_url)
        else:
            print("Error: 'install' command requires a repository URL.")
    elif args.command == "list":
        list_apps()

if __name__ == "__main__":
    main()
