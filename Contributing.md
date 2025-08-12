# Contributing to Genesis Recursive Code Protocol (GRCP)

Thank you for your interest in contributing to GRCP! We welcome contributions from the community to help evolve this AI-native invention framework. Whether you're fixing bugs, adding new protocol variants, improving documentation, or sharing invention notebooks, your input is valuable.

By contributing, you help push the boundaries of AI-led R&D while adhering to our principles of recursion, ethical safeguards, and realism.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
  - [Reporting Bugs](#reporting-bugs)
  - [Suggesting Enhancements](#suggesting-enhancements)
  - [Your First Code Contribution](#your-first-code-contribution)
  - [Pull Requests](#pull-requests)
- [Style Guidelines](#style-guidelines)
  - [Code Style](#code-style)
  - [Commit Messages](#commit-messages)
  - [Documentation](#documentation)
- [Branching and Versioning](#branching-and-versioning)
- [Testing](#testing)
- [License](#license)
- [Questions?](#questions)

## Code of Conduct

This project adheres to the [Contributor Covenant Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct.html). By participating, you are expected to uphold this code. Please report unacceptable behavior to the project maintainer at [lazyxeon@example.com] (replace with actual email if available).

## How Can I Contribute?

### Reporting Bugs

- Ensure the bug was not already reported by searching on GitHub under [Issues](https://github.com/lazyxeon/Genesis-Recursive-Code-Protocol-/issues).
- If you're unable to find an open issue addressing the problem, [open a new one](https://github.com/lazyxeon/Genesis-Recursive-Code-Protocol-/issues/new?assignees=&labels=bug&template=bug_report.md&title=).
- Be sure to include a **title and clear description**, as much relevant information as possible, and a **code sample** or an **executable test case** demonstrating the expected behavior that is not occurring.
- For protocol-specific bugs (e.g., in v47 realism checks), include the variant version and a minimal reproduction prompt.

### Suggesting Enhancements

- Check if the enhancement is already suggested in [Issues](https://github.com/lazyxeon/Genesis-Recursive-Code-Protocol-/issues).
- Open a new issue using the [enhancement template](https://github.com/lazyxeon/Genesis-Recursive-Code-Protocol-/issues/new?assignees=&labels=enhancement&template=feature_request.md&title=).
- Describe the enhancement clearly, why it's needed, and how it aligns with GRCP's goals (e.g., improving recursion depth or adding new ethical proxies).
- For new protocol variants or inventions, reference the "worth-it" assessment from v47.

### Your First Code Contribution

Unsure where to begin? Check out issues labeled [`good first issue`](https://github.com/lazyxeon/Genesis-Recursive-Code-Protocol-/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+issue%22) or [`help wanted`](https://github.com/lazyxeon/Genesis-Recursive-Code-Protocol-/issues?q=is%3Aopen+is%3Aissue+label%3A%22help+wanted%22).

Examples:
- Update documentation in `Documents/` or `Charts.md`.
- Add a new notebook demo in `Notebooks/`.
- Fix a bug in the CLI tools in `CLI Bundle/`.

### Pull Requests

1. Fork the repo and create your branch from `main` (e.g., `feature/new-variant` or `fix/cli-bug`).
2. If you've added code, ensure it follows [style guidelines](#style-guidelines) and includes tests.
3. Update the README.md or relevant docs if your change affects usage.
4. For new variants (e.g., v48), include a changelog entry in `GRCP most recent variants/Changelog.md` and a worth-it assessment.
5. Ensure the description clearly describes the problem and solution. Include the relevant issue number if applicable.
6. Open a pull request and reference any related issues.

We aim to review PRs within a week. If it's a major change (e.g., new edition), discuss it in an issue first.

## Style Guidelines

### Code Style

- **Python**: Follow PEP 8. Use tools like Black for formatting and Flake8 for linting.
- **Markdown**: Consistent headings, lists, and code blocks. Use relative links for repo files.
- **Protocol Files**: Markdown with clear sections (e.g., Phases, Gates). Use consistent naming like `vXX.md`.
- Run `pip install -r requirements.txt` and ensure no new dependencies without justification.

### Commit Messages

- Use the present tense ("Add feature" not "Added feature").
- Limit the first line to 72 characters.
- Reference issues and pull requests liberally (e.g., "Fixes #123").
- For mutations or inventions, note the variant (e.g., "Mutate v47: Add EVM enhancements").

### Documentation

- All new features or changes must update relevant docs (e.g., README.md, Charts.md).
- For notebooks, include clear explanations, dependencies, and expected outputs.
- Use Mermaid for charts where possible.

## Branching and Versioning

- `main`: Stable branch for releases.
- Feature branches: `feature/xxx` or `variant/v48-new-edition`.
- Use semantic versioning for protocol editions (e.g., v47.1 for minor updates).
- Branches auto-reap after 30 days of inactivity (per v46+ governance).

## Testing

- Test locally with your LLM of choice (e.g., paste protocol into Grok and run a sample prompt).
- For CLI: Run `python gcp_cli.py --test` (if implemented) or manual phase checks.
- Notebooks: Ensure they run end-to-end in Jupyter.
- Include tests for new code (e.g., unit tests in scripts).
- For ethical changes, verify proxy scores remain consistent.

## License

By contributing, you agree that your contributions will be licensed under the [MIT License](LICENSE).

## Questions?

If you have questions, open an issue or reach out via discussions. We're excited to collaborate!

— The GRCP Community