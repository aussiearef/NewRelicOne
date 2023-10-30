const { By, until } = $browser;

// Define your test URL
const testURL = "https://www.syntheticmonitor.live";

// Define the credentials you want to use for testing
const username = "your_username";
const password = "your_password";

// Open the login page
$browser.get(testURL)
  .then(() => {
    // Wait for the login page elements to load
    return $browser.waitForAndFindElement(By.css('input#username'), 5000);
  })
  .then((usernameInput) => {
    // Enter the username
    usernameInput.sendKeys(username);
    // Find the password input field and enter the password
    return $browser.waitForAndFindElement(By.css('input#password'), 5000);
  })
  .then((passwordInput) => {
    passwordInput.sendKeys(password);
    // Find and click the login button
    return $browser.waitForAndFindElement(By.css('button[type="submit"]'), 5000);
  })
  .then((loginButton) => {
    return loginButton.click();
  })
  .then(() => {
    // Wait for a page element that indicates a successful login
    return $browser.waitForAndFindElement(By.css('.dashboard'), 10000);
  })
  .then(() => {
    // You can add additional checks here to ensure that the login was successful
    console.log("Login successful");
  })
  .catch((err) => {
    // Handle errors or failed login attempts
    console.error("Login failed: " + err);
  })
  .finally(() => {

  });
