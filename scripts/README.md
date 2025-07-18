# Scripts Directory

This directory contains utility scripts for managing the Threat Modelling Workshop project.

## setup_contact.py

This script helps manage contact information across documentation files while keeping personal details secure.

### Setup Instructions

1. **Create your personal contact file**:
   ```bash
   cp ../contact_info.template.json ../contact_info.personal.json
   ```

2. **Edit the personal file**:
   - Open `../contact_info.personal.json`
   - Replace the placeholder values with your actual information
   - Save the file

3. **Run the script**:
   ```bash
   python setup_contact.py
   ```

### What it does:
- Scans all markdown files for contact information placeholders
- Replaces them with your personal information
- Updates all relevant documentation files automatically

### Security Note:
- `contact_info.personal.json` is in `.gitignore` and won't be committed
- Only share the template file, never your personal file
