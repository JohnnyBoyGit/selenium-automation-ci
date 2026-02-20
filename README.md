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

## 🏗️ CI/CD Pipeline Architecture

The pipeline is designed for high reliability in **headless environments**:

- **Triggers:** Automatically runs on every `push` to the main branch.
- **Manual Control:** Supports `workflow_dispatch` for on-demand health checks directly from GitHub or VS Code.
- **Artifacts:** Generates and uploads a detailed, self-contained HTML test report after every run.
- **Stability:** Features custom `safe_click` and `quick_click` synchronization logic to handle lazy-loading, scrolling, and dynamic UI components.

## 📊 How to View Reports

1. Navigate to the [Actions Tab](https://github.com/JohnnyBoyGit/selenium-automation-ci/actions).
2. Click on the most recent **Workflow Run** (e.g., "final: sync fixed page object").
3. Scroll down to the **Artifacts** section at the bottom of the summary.
4. Download the `selenium-test-report-run-XX` zip file.
5. Unzip and open `report.html` in any browser to see interactive results.

## 🧪 Current Test Coverage

- **Carousel Navigation:** Verified with JS hydration and ActionChains.
- **Header/Footer:** 100% link verification across sub-menus and quick links.
- **Specialized Pages:** Electrodiagnostics flow and "Schedule Now" functionality.
- **Regression Tracking:** Strategic use of `xfail` to monitor known site-side bugs.
