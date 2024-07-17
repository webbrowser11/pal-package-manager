import os
import argparse
import urllib.request
import zipfile
from io import BytesIO

# Function to install the repository if it has "PAL" in the name
def install_repo(repo_url):
    repo_name = repo_url.split("/")[-1]

    if "PAL" not in repo_name:
        print("Error: Repository name must contain 'PAL'.")
        return

    # Create .apps directory if it doesn't exist
    if not os.path.exists(".apps"):
        os.makedirs(".apps")

    # Define the path where the repo will be extracted
    extract_path = os.path.join(".apps", repo_name)

    # Construct the URL for the ZIP file
    zip_url = f"{repo_url}/archive/refs/heads/main.zip"

    try:
        # Download the ZIP file
        with urllib.request.urlopen(zip_url) as response:
            zip_data = response.read()

        # Extract the ZIP file
        with zipfile.ZipFile(BytesIO(zip_data)) as z:
            z.extractall(extract_path)

        print(f"Installed {repo_name} to .apps/{repo_name}")
    except urllib.error.URLError as e:
        print(f"Error: Failed to download the repository. {e}")
    except zipfile.BadZipFile as e:
        print(f"Error: Failed to extract the repository. {e}")

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
