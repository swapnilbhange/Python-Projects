📸 Screenshot App

A simple Python-based application that captures screenshots using `pyautogui`.

------------------------------------------------------------

🚀 Setup Instructions

1. Create the Project File
- Create your `screenshot.py` file in your desired project folder.

2. Open Command Prompt and Navigate to the Project Directory
```bash
cd C:\Users\<YourUsername>\Path\To\Your\Project
```

3. Create a Virtual Environment
```bash
python -m venv projectsenv
```
> This will create an isolated Python environment in a folder named `projectsenv`.

4. Activate the Virtual Environment

- Windows:
```bash
projectsenv\Scripts\activate
```

- If you're using VS Code, it may prompt you to select the interpreter. Choose the one from `projectsenv`.

5. Install Required Libraries
```bash
pip install pyautogui
```
> `pyautogui` will also require `pillow` and `pyscreeze`, which will be automatically installed as dependencies.

6. Run the App
```bash
python screenshot.py
```

------------------------------------------------------------

📂 Example Use Case

The script allows you to take automated screenshots through GUI interaction, useful for testing, documentation, or automation workflows.