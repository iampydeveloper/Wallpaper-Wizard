# Wallpaper-Wizard
"Wallpaper Wizard" is a project designed to automate the process of changing your desktop wallpaper. Utilizing the power of Python, it integrates with the Selenium library to interact with web pages, specifically to generate and download random images from a specified website.

Required Libraries:
1. tkinter - for the GUI.
2. selenium - for web automation.
3. requests - for downloading the image.
4. pywin32 - for interacting with Windows API to set the wallpaper.

Additional Requirements:
1. Download the appropriate version of chromedriver that matches your installed version of Google Chrome.
2. Specify the path to the chromedriver executable in your script(line 23)

To check the version of Google Chrome you have installed, follow these steps:
1. Open Google Chrome.
2. Click on the three vertical dots (menu) in the upper-right corner of the browser window.
3. Hover over "Help" in the dropdown menu.
4. Click on "About Google Chrome" from the submenu.
5. A new tab will open, displaying the version of Google Chrome you are currently using.
6. Download ChromeDriver. Visit https://googlechromelabs.github.io/chrome-for-testing/. Find and download the version matching your Chrome browser. Save and extract the file. Note the path to the chromedriver executable.
