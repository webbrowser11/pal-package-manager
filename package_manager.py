import os
import subprocess
import argparse

# Function to install the repository if it has "PAL" in the name
def install_repo(repo_url):
    repo_name = repo_url.split("/")[-1]

    if "PAL" not in repo_name:
        print("Error: Repository name must contain 'PAL'.")
        return

    # Create .apps directory if it doesn't exist
    if not os.path.exists(".apps"):
        os.makedirs(".apps")

    # Define the path where the repo will be cloned
    clone_path = os.path.join(".apps", repo_name)

    # Clone the repo into the .apps directory
    subprocess.run(["git", "clone", repo_url, clone_path])

    print(f"Installed {repo_name} to .apps/{repo_name}")

# Main function to handle command-line arguments
def main():
    parser = argparse.ArgumentParser(description="PAL Package Manager")
    parser.add_argument("command", choices=["install"], help="Command to execute")
    parser.add_argument("repo_url", nargs="?", help="Repository URL to install")
    args = parser.parse_args()

    if args.command == "install":
        if args.repo_url:
            install_repo(args.repo_url)
        else:
            print("Error: 'install' command requires a repository URL.")

if __name__ == "__main__":
    main()
