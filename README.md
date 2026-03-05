# CaliPain Automation Suite 

[![Selenium Python CI](https://github.com/JohnnyBoyGit/selenium-automation-ci/actions/workflows/regression.yml/badge.svg)](https://github.com/JohnnyBoyGit/selenium-automation-ci/actions/workflows/regression.yml)

## 🚀 Project Overview

This repository contains a professional-grade **CI/CD Automation Pipeline** for the [CaliPain.com](https://calipain.com) platform. Built with **Python** and **Selenium**, the suite is fully integrated into **GitHub Actions** to ensure continuous site health and reliable regression testing.

## 🛠️ Tech Stack

- **Language:** Python 3.11
- **Framework:** Pytest
- **Automation:** Selenium WebDriver
- **CI/CD:** GitHub Actions
- **Reporting:** Pytest-HTML (Artifacts)

## 🏗️ Framework Highlights

To ensure maximum maintainability and zero code duplication, this suite implements several advanced design patterns:

- **Unified Strategy Pattern:** A centralized `CommonLogic` engine handles complex navigation flows, allowing tests to dynamically swap between `safe_click`, `force_click`, and `JS-scroll` via simple parameters.
- **Lazy-Loaded Components:** Global elements like the Header and Footer are implemented as `@property` decorators in the `BasePage`, ensuring they are only instantiated when needed (reducing memory overhead).
- **Stealth Automation:** Integrated Custom Driver logic using CDP (Chrome DevTools Protocol) to bypass anti-bot detection by nullifying the `navigator.webdriver` property.
- **Automated State Recovery:** Post-test cleanup fixtures ensure a "Clean Slate" by automatically closing external tabs and resetting the driver handle after every execution.

## 🏗️ CI/CD Pipeline Architecture

The pipeline is designed for high reliability in **headless environments**:

- **Triggers:** Automatically runs on every `push` to the main branch.
- **Manual Control:** Supports `workflow_dispatch` for on-demand health checks directly from GitHub or VS Code.
- **Artifacts:** Generates and uploads a detailed, self-contained HTML test report after every run.
- **Stability:** Features custom `safe_click` and `quick_click` synchronization logic to handle lazy-loading, scrolling, and dynamic UI components.
- **Unified Engine:** Implements a **Strategy Pattern** via `CommonLogic`, allowing tests to dynamically toggle between native clicks, JS-forced clicks, and automated scrolling through simple parameters.
- **Stealth Mode:** Employs Chrome DevTools Protocol (CDP) to nullify `navigator.webdriver`, bypassing anti-automation scripts during CI runs.

## 📊 How to View Reports

1. Navigate to the [Actions Tab](https://github.com/JohnnyBoyGit/selenium-automation-ci/actions).
2. Click on the most recent **Workflow Run** (e.g., "final: sync fixed page object").
3. Scroll down to the **Artifacts** section at the bottom of the summary.
4. Download the `selenium-test-report-run-XX` zip file.
5. Unzip and open `report.html` in any browser to see interactive results.
    - **Pro-Tip:** High-resolution screenshots are automatically embedded in the report for any failed test case to accelerate debugging.

## 🧪 Current Test Coverage

- **Carousel Navigation:** Verified with JS hydration and ActionChains.
- **Header/Footer:** 100% link verification across sub-menus and quick links.
- **Specialized Pages:** Electrodiagnostics flow and "Schedule Now" functionality.
- **Regression Tracking:** Strategic use of `xfail` to monitor known site-side bugs.
