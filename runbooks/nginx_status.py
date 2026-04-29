import subprocess

def check_nginx_status():
    try:
        # Run systemctl command
        result = subprocess.run(
            ["systemctl", "is-active", "nginx"],
            capture_output=True,
            text=True
        )

        status = result.stdout.strip()

        if status == "active":
            print("NGINX is running ✅")
        elif status == "inactive":
            print("NGINX is not running ❌")
        elif status == "failed":
            print("NGINX has failed ⚠️")
        else:
            print(f"Unknown status: {status}")

    except Exception as e:
        print(f"Error checking NGINX status: {e}")

if __name__ == "__main__":
    check_nginx_status()
