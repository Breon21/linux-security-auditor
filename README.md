# Linux Security Auditor
<img width="834" height="482" alt="Image" src="https://github.com/user-attachments/assets/171b0715-ae67-4276-b878-116043399414" />
A beginner-friendly Linux security auditing tool written in Python.

## Overview

Linux Security Auditor performs basic, read-only security
checks and displays findings that can help with an initial
review of a Linux system.

## Features

- Operating system and kernel information
- Current user identification
- Selected sensitive file permission checks
- Network utility availability checks
- Listening TCP/UDP socket inspection
- Preliminary security warnings

## Requirements

- Linux
- Python 3
- Optional network utilities such as `ip` and `ss`

## Installation

Clone the repository:

    git clone YOUR_REPOSITORY_URL

Enter the project directory:

    cd linux-security-auditor

## Usage

Run the auditor:

    python3 auditor.py

## Safety

This project is designed for authorized systems and
read-only inspection.

It does not attempt to exploit vulnerabilities, modify
system configuration, or change firewall settings.

Findings are preliminary indicators and should be
validated before taking corrective action.

## Learning Objectives

- Python scripting
- Linux permissions
- User identification
- Basic network inspection
- Cybersecurity auditing
- Git and GitHub

## Future Improvements

- Generate JSON and text reports
- Add configurable severity levels
- Improve firewall status detection
- Add automated tests
- Add remediation guidance
