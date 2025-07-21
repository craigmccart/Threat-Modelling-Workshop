import os
import re

REQUIRED_SECTIONS = [
    'threat', 'mitigation', 'risk', 'assessment', 'control', 'dataflow', 'attacker', 'stride', 'summary'
]


def check_markdown_sections(filepath):
    missing = []
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read().lower()
        for section in REQUIRED_SECTIONS:
            if section not in content:
                missing.append(section)
    return missing


def lint_markdown_files(root_dir):
    for subdir, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.md'):
                path = os.path.join(subdir, file)
                missing = check_markdown_sections(path)
                if missing:
                    print(f"{path}: Missing sections: {', '.join(missing)}")
                else:
                    print(f"{path}: All required sections present.")


if __name__ == "__main__":
    lint_markdown_files('.') 