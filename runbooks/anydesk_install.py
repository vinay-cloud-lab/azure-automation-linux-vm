import subprocess

def run(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print("ERROR:", result.stderr)

def install_anydesk():
    print("Updating packages...")
    run("apt update")

    print("Installing dependencies...")
    run("apt install -y wget gnupg2")

    print("Adding AnyDesk repo key...")
    run("wget -qO - https://keys.anydesk.com/repos/DEB-GPG-KEY | apt-key add -")

    print("Adding AnyDesk repository...")
    run('echo "deb http://deb.anydesk.com/ all main" > /etc/apt/sources.list.d/anydesk.list')

    print("Updating again...")
    run("apt update")

    print("Installing AnyDesk...")
    run("apt install -y anydesk")

    print("Starting AnyDesk service...")
    run("systemctl enable anydesk")
    run("systemctl start anydesk")

    print("Checking status...")
    run("systemctl status anydesk --no-pager")

if __name__ == "__main__":
    install_anydesk()
