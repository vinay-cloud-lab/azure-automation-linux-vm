import subprocess

def run_command(cmd):
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.returncode, result.stdout.strip(), result.stderr.strip()


def create_user(username):
    code, out, err = run_command(["useradd", "-m", username])

    if code == 0:
        print(f"User '{username}' created")
    else:
        print(f"Error creating '{username}': {err}")


def delete_user(username):
    code, out, err = run_command(["userdel", "-r", username])

    if code == 0:
        print(f"User '{username}' deleted")
    else:
        print(f"Error deleting '{username}': {err}")


def main():
    user1 = "user1"
    user2 = "user2"

    print("Starting user management task...")

    create_user(user1)
    create_user(user2)

    delete_user(user2)

    print("Task completed.")


if __name__ == "__main__":
    main()
  
