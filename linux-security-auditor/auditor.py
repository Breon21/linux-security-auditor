#!/usr/bin/env python3

import os
import platform
import shutil
import subprocess
from datetime import datetime


def run_command(command):
    """Run a command safely and return its output."""

    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=10,
            check=False
        )

        if result.returncode == 0:
            return result.stdout.strip()

        return result.stderr.strip() or "Command returned an error."

    except FileNotFoundError:
        return "Command not available."

    except subprocess.TimeoutExpired:
        return "Command timed out."


def check_system():
    """Collect basic Linux system information."""

    print("\n[+] SYSTEM INFORMATION")

    print(f"Operating System: {platform.system()}")
    print(f"OS Version: {platform.release()}")
    print(f"Architecture: {platform.machine()}")
    print(f"Python Version: {platform.python_version()}")


def check_current_user():
    """Display the current user and identity information."""

    print("\n[+] CURRENT USER")

    username = os.getenv("USER", "Unknown")
    print(f"Username: {username}")

    if shutil.which("id"):
        print(run_command(["id"]))

    else:
        print("The id command is unavailable.")


def check_sensitive_permissions():
    """Check permissions on selected sensitive system files."""

    print("\n[+] SENSITIVE FILE PERMISSIONS")

    files_to_check = [
        "/etc/passwd",
        "/etc/shadow",
        "/etc/ssh/sshd_config"
    ]

    for filepath in files_to_check:

        if not os.path.exists(filepath):
            print(f"[INFO] {filepath}: File not present.")
            continue

        try:
            permissions = os.stat(filepath).st_mode & 0o777
            mode = format(permissions, "04o")

            print(f"{filepath}: {mode}")

            if filepath == "/etc/passwd":
                if permissions & 0o022:
                    print(
                        "[HIGH] /etc/passwd is writable "
                        "by group or others."
                    )

            elif filepath == "/etc/shadow":
                if permissions & 0o007:
                    print(
                        "[HIGH] /etc/shadow has permissions "
                        "allowing access by others."
                    )

            elif filepath == "/etc/ssh/sshd_config":
                if permissions & 0o022:
                    print(
                        "[HIGH] SSH configuration is writable "
                        "by group or others."
                    )

        except PermissionError:
            print(f"[INFO] Permission denied: {filepath}")


def check_network_tools():
    """Check for common network inspection utilities."""

    print("\n[+] NETWORK TOOLS")

    tools = ["ip", "ss", "ufw", "firewall-cmd"]

    for tool in tools:
        if shutil.which(tool):
            print(f"[AVAILABLE] {tool}")
        else:
            print(f"[NOT FOUND] {tool}")

    if shutil.which("ss"):
        print("\nListening TCP/UDP sockets:")

        print(
            run_command(
                ["ss", "-lntu"]
            )
        )


def main():
    """Run the security audit."""

    print("=" * 45)
    print(" LINUX SECURITY AUDITOR")
    print("=" * 45)

    print(f"Audit started: {datetime.now().isoformat()}")

    check_system()
    check_current_user()
    check_sensitive_permissions()
    check_network_tools()

    print("\n[+] AUDIT COMPLETE")
    print("Review the findings before making system changes.")


if __name__ == "__main__":
    main()
