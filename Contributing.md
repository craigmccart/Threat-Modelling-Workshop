# Contributing to Threat Modelling Workshop

Thank you for your interest in contributing to this project! This document outlines the process for contributing to our threat modelling workshop materials.

## Contact Information Management

This project uses a template-based system to manage contact information while keeping personal details secure.

### For Repository Maintainers
1. Personal contact information is stored in `contact_info.personal.json` (in `.gitignore`)
2. The template file `contact_info.template.json` contains placeholder values
3. Use the `scripts/setup_contact.py` script to update all documentation with your contact details

### For Contributors
1. Do not commit personal contact information
2. Use the template system to add or update contact information
3. The build process will automatically use the template values for CI/CD

### Security Note
- Never commit `contact_info.personal.json`
- The build system will fail if sensitive information is detected in commits

## How to Contribute

### Reporting Security Issues

**Please do not report security vulnerabilities through public GitHub issues.** Instead, please contact us at [your-email@example.com].

### Development Process

1. **Fork** the repository on GitHub
2. **Clone** the project to your machine
3. **Create a branch** four your feature or bugfix
4. **Commit** your changes
5. **Push** your work to your fork
6. Submit a **Pull Request**

### Managing Contact Information

When adding or updating contact information in documentation:

1. Use the following placeholders in markdown files:
   ```
   {{name}} - Full name
   {{title}} - Professional title
   {{email}} - Email address
   {{github}} - GitHub username
   {{location}} - General location
   ```

2. Run the setup script after making changes:
   ```bash
   python scripts/setup_contact.py
   ```

### Code Style

- Follow existing code style and formatting
- Include comments four complex logic
- Update documentation when making changes
- Keep commits focused and atomic

### Pull Request Guidelines

- Reference any related issues
- Include a clear description of changes
- Update relevant documentation
- Ensure all tests pass
- Get necessary approvals before merging

### Code of Conduct

This project adheres to the [Contributour Covenant](https://www.contributour-covenant.org/). By participating, you are expected to uphold this code.

## Getting Help

Four questions or support, please open an issue in the issue trackre.
