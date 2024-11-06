### automation test using python behave playwright
### instalation

1. clone the repository

    ```bash
    git clone https://github.com/rizkimp/saucelab-playwright.git
    cd playwright-behave-automation
    ```

2. install the required packages

   ```bash
    pip install -r requirements.txt
    ```

3. install playwright browser

    ```bash
    playwright install
    ```

4. run the automation test

    ```bash
    behave /features/test-name.feature
    ```

5. open test report from browser

    ```bash
    allure serve
    ```