# Selenium reCAPTCHA Solver with DeathByCaptcha

This project is an automation example using Selenium and Python that utilizes the DeathByCaptcha API service to solve Google reCAPTCHA v2 challenges.

## 📋 Description

The script automates reCAPTCHA solving using:
- **Selenium WebDriver**: To automate the browser (Firefox or Chrome)
- **DeathByCaptcha API**: Captcha solving service
- **Python-dotenv**: To securely manage credentials via environment variables

## 🚀 Features

- Automatic credential loading from `.env` file
- Support for Firefox and Chrome (configurable)
- DeathByCaptcha account balance verification
- Automatic reCAPTCHA v2 solving
- Captcha solution validation

## 📦 Requirements

- Python 3.6+
- Firefox or Chrome installed
- GeckoDriver (for Firefox) or ChromeDriver (for Chrome)
- Active account at [DeathByCaptcha](https://www.deathbycaptcha.com/)

## 🔧 Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd dbc_api_selenium_python3
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Linux/Mac
   # or
   venv\Scripts\activate  # On Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure credentials:**
   ```bash
   cp .env.example .env
   ```
   
   Edit the `.env` file and add your DeathByCaptcha credentials:
   ```
   DBC_USERNAME=your_deathbycaptcha_username
   DBC_PASSWORD=your_deathbycaptcha_password
   ```

5. **Download the WebDriver:**
   - **GeckoDriver (Firefox)**: [Download here](https://github.com/mozilla/geckodriver/releases)
   - **ChromeDriver (Chrome)**: [Download here](https://chromedriver.chromium.org/)
   
   Make sure the driver is in your PATH or in the project directory.

## 💻 Usage

1. **Make sure the `.env` file is configured correctly**

2. **Run the script:**
   ```bash
   python python_selenium_example.py
   ```

3. **The script will:**
   - Open the browser
   - Navigate to the reCAPTCHA demo page
   - Extract the site key
   - Send the captcha to DeathByCaptcha to solve it
   - Insert the solution into the form
   - Verify if the solution was successful

## 🔄 Switching Browsers

By default, the script uses Firefox. To use Chrome, edit the `python_selenium_example.py` file:

```python
# Comment this line:
# with webdriver.Firefox() as driver:

# Uncomment this line:
with webdriver.Chrome() as driver:
```

## 📁 Project Structure

```
.
├── python_selenium_example.py  # Main script
├── requirements.txt            # Project dependencies
├── .env.example               # Environment variables template
├── .env                       # Your credentials (not uploaded to git)
├── .gitignore                 # Files to ignore in git
├── .github/workflows/ci.yml   # GitHub Actions CI configuration
└── README.md                  # This file
```

## ⚙️ CI/CD with GitHub Actions

This project includes `.github/workflows/ci.yml` for automated testing with GitHub Actions.

### Workflow Features

- **Multi-version Testing**: Runs on Python 3.14 and 3.15
- **Headless Firefox**: Uses Firefox + GeckoDriver in headless mode
- **Validation Steps**: Syntax and imports checks before script execution
- **Optional Full Run**: Executes the Selenium script only when secrets are available
- **Debug Artifacts**: Uploads screenshots and logs after each run

### Headless Mode

The script runs in headless mode automatically on GitHub Actions (`GITHUB_ACTIONS=true`).

For local testing in headless mode:

```bash
HEADLESS=1 python python_selenium_example.py
```

### Required GitHub Secrets

To execute the full captcha flow, configure these repository secrets:

1. Go to **Settings > Secrets and variables > Actions**
2. Add:
   - `DBC_USERNAME`
   - `DBC_PASSWORD`

If secrets are not set, the workflow still runs validation checks and skips the live captcha execution.

## ⚠️ Important Notes

- **Never upload the `.env` file to the repository** - it contains your credentials
- Using captcha solving services may violate the terms of service of some websites
- This script is for educational and testing purposes only
- Make sure you have sufficient credits in your DeathByCaptcha account

## 🔒 Security

- Credentials are loaded from environment variables using `.env`
- The `.env` file is included in `.gitignore` to prevent exposure
- Use `.env.example` as a template without real credentials

## 📝 Dependencies

- `deathbycaptcha-official`: Official DeathByCaptcha Python client
- `selenium`: Browser automation framework
- `python-dotenv`: Loads environment variables from .env files

## 🆘 Support

For issues with:
- **DeathByCaptcha API**: [Official Documentation](https://deathbycaptcha.com/api)
- **Selenium**: [Selenium Documentation](https://selenium-python.readthedocs.io/)

## 📄 License

This project is an educational example. Use it at your own risk.

## 🤝 Contributions

Contributions are welcome. Please:
1. Fork the project
2. Create a branch for your feature (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
