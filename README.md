
# CaliPain Automation Suite
<!-- 1. THE STATUS BADGE (Paste the code you copied from GitHub Actions here) -->
[![Selenium Python CI](https://github.com/JohnnyBoyGit/selenium-automation-ci/actions/workflows/regression.yml/badge.svg)](https://github.com/JohnnyBoyGit/selenium-automation-ci/actions/workflows/regression.yml)

## 🚀 Project Overview
This repository contains a professional-grade **CI/CD Automation Pipeline** for the [CaliPain.com](https://calipain.com) platform. Built with **Python** and **Selenium**, the suite is fully integrated into **GitHub Actions** to ensure continuous site health.

## 🛠️ Tech Stack
* **Language:** Python 3.11
* **Framework:** Pytest
* **Automation:** Selenium WebDriver
* **CI/CD:** GitHub Actions
* **Reporting:** Pytest-HTML (Artifacts)

## 🏗️ CI/CD Pipeline Architecture
The pipeline is designed for high reliability in **headless environments**:
* **Triggers:** Automatically runs on every `push` and `pull_request`.
* **Manual Control:** Supports `workflow_dispatch` for on-demand health checks.
* **Artifacts:** Generates and uploads a detailed HTML test report after every run.
* **Stability:** Features custom `safe_click` and `quick_click` synchronization logic to handle lazy-loading and dynamic UI components.

## 📊 How to View Reports
1. Navigate to the [Actions Tab](https://github.com[JohnnyBoyGit]/[selenium-automation-ci]/actions).
2. Click on the most recent **Workflow Run**.
3. Scroll down to **Artifacts** and download `selenium-test-report`.
4. Unzip and open `report.html` in any browser.

## 🧪 Current Test Coverage
* **Carousel Navigation:** Verified with JS hydration and ActionChains.
* **Header/Footer:** 100% link verification across sub-menus and quick links.
* **Specialized Pages:** Electrodiagnostics flow verification.
