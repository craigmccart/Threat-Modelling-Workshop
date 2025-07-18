#!/usr/bin/env python3
"""
Contact Information Setup Script

This script generates contact information files from a template.
Create a personal copy of contact_info.template.json as contact_info.personal.json
and fill in your details. The personal file is in .gitignore and won't be committed.
"""
import json
import os
from pathlib import Path

def load_template():
    """Load the contact information template."""
    with open('contact_info.template.json', 'r') as f:
        return json.load(f)

def load_personal_info():
    """Load personal contact information if available, otherwise use template."""
    if os.path.exists('contact_info.personal.json'):
        with open('contact_info.personal.json', 'r') as f:
            return json.load(f)
    return load_template()

def update_files(contact_info):
    """Update all files with contact information."""
    # List of files that need contact info updates
    files_to_update = [
        'README.md',
        'Project_summary.md',
        'Portfolio_summary.md',
        'Cv_summary.md'
    ]
    
    for file_path in files_to_update:
        if not os.path.exists(file_path):
            continue
            
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Update contact information
        updated = content
        updated = updated.replace('{{name}}', contact_info['name'])
        updated = updated.replace('{{title}}', contact_info['title'])
        updated = updated.replace('{{email}}', contact_info['email'])
        updated = updated.replace('{{github}}', contact_info['github'])
        updated = updated.replace('{{location}}', contact_info['location'])
        
        # Write back if changes were made
        if updated != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(updated)
            print(f"Updated contact info in {file_path}")

def main():
    # Create scripts directory if it doesn't exist
    Path('scripts').mkdir(exist_ok=True)
    
    # Load contact info
    if not os.path.exists('contact_info.personal.json'):
        print("Personal contact info not found. Creating template...")
        template = load_template()
        with open('contact_info.personal.json', 'w') as f:
            json.dump(template, f, indent=2)
        print("\nPlease edit contact_info.personal.json with your details and run this script again.")
        return
    
    contact_info = load_personal_info()
    update_files(contact_info)
    print("\nContact information updated successfully!")

if __name__ == "__main__":
    main()
