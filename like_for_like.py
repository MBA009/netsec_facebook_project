import subprocess
import requests
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyperclip 
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import Select
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

facebook_email = os.getenv("FACEBOOK_EMAIL")
facebook_password = os.getenv("FACEBOOK_PASSWORD")
like4like_username = os.getenv("LIKE4LIKE_USERNAME")
like4like_password = os.getenv("LIKE4LIKE_PASSWORD")

def write_post_to_file(post, file_path):
    """Write the given post to a file."""
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(post)
    print(f"Post written to file: {file_path}")

def read_post_from_file(file_path):
    """Read the post from the file if it exists."""
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read().strip()
    return None

def get_latest_post():
    baking_phrases = [
        "Flaky layers are the ultimate goal for any puff pastry.",
        "A touch of vanilla extract can elevate your dessert to new heights.",
        "Yeast dough needs a warm environment to rise properly.",
        "Never underestimate the power of a good rolling pin.",
        "The perfect brownie has a fudgy center and a crackly top.",
        "Always sift your flour for lump-free batter.",
        "A kitchen scale ensures accurate measurements for better results.",
        "Beating egg whites to stiff peaks is essential for meringues.",
        "Cooling racks are a baker’s best friend for even airflow.",
        "The right amount of proofing is the secret to fluffy bread.",
        "Piping bags make cake decoration much easier.",
        "Always scrape down the sides of the bowl when mixing.",
        "A dash of cinnamon can transform a simple recipe.",
        "Double boilers are great for melting chocolate evenly.",
        "Measuring dry and wet ingredients in the right tools is critical.",
        "Parbaking crusts prevents soggy bottoms in pies.",
        "Egg wash gives pastries a glossy, golden finish.",
        "Kneading dough develops gluten for a better texture.",
        "Freshly grated nutmeg adds a warm, aromatic flavor.",
        "Refrigerating cookie dough enhances its flavor and texture.",
        "Chilling butter is key to flaky biscuits.",
        "Layering parchment paper prevents sticking in baking pans.",
        "Blind baking is crucial for custard-filled tarts.",
        "Cake testers or toothpicks help check doneness effectively.",
        "Pastry blenders simplify cutting butter into flour.",
        "Shortening can produce tender pie crusts.",
        "Bread flour is ideal for recipes requiring a chewy texture.",
        "Confectioner's sugar is perfect for frostings and glazes.",
        "Folding batter gently prevents deflation in sponge cakes.",
        "Room-temperature ingredients mix more uniformly.",
        "Salted butter can alter the flavor balance in baked goods.",
        "Acidic ingredients like lemon juice react with baking soda.",
        "Proofing baskets help shape artisanal loaves.",
        "Dutch ovens mimic steam ovens for crusty bread.",
        "Rolled oats add a hearty texture to cookies.",
        "Chiffon cakes rely on whipped egg whites for their airy texture.",
        "Bundt pans create beautifully shaped cakes.",
        "Always grease and flour pans to avoid sticking.",
        "Chocolate chips hold their shape better than chopped chocolate.",
        "Sifting cocoa powder prevents clumps in chocolate batters.",
        "Molasses gives gingerbread its signature rich flavor.",
        "Candy thermometers ensure precision in sugar work.",
        "Room-temperature eggs whip up to greater volume.",
        "Bread machines can simplify the kneading process.",
        "Decorative molds create intricate designs in cakes and chocolates.",
        "Overmixing batter can lead to tough baked goods.",
        "Laminating dough creates distinct layers in pastries.",
        "Baking stones provide even heat distribution for pizza crusts.",
        "Dark-colored pans absorb heat more quickly than light-colored ones.",
        "Adding espresso powder deepens the flavor of chocolate desserts.",
        "Cakes should cool completely before frosting.",
        "Brown sugar adds moisture and richness to baked goods.",
        "Overproofing can cause bread to collapse.",
        "Gelatin stabilizes whipped cream for longer-lasting peaks.",
        "Pastry cutters ensure uniform shapes for biscuits and cookies.",
        "Flavored extracts, like almond or mint, add unique notes to desserts.",
        "Using ice water ensures flaky pie crusts.",
        "Lining cupcake pans with paper liners makes removal easier.",
        "Baking soda requires an acidic ingredient to activate.",
        "Springform pans are ideal for cheesecakes and delicate tarts.",
        "Invert cakes onto a rack to prevent soggy bottoms.",
        "Stirring batter too vigorously can deflate air bubbles.",
        "Cake flour produces a softer crumb than all-purpose flour.",
        "Scoring bread helps control how it expands in the oven.",
        "A pinch of cream of tartar stabilizes egg whites.",
        "Honey can replace sugar for a softer, moister texture.",
        "Cooling cookie sheets prevents excess spreading.",
        "A pastry wheel makes crimping pie edges decorative and easy.",
        "Lemon zest brightens up the flavor of baked goods.",
        "Using buttermilk adds tang and tenderness to recipes.",
        "Browned butter adds a nutty complexity to cookies and cakes.",
        "Bread baskets provide a rustic presentation for serving loaves.",
        "Sour cream enhances the moistness of cakes and muffins.",
        "A proper bench scraper simplifies dough handling.",
        "Softened cream cheese is easier to incorporate into cheesecake batter.",
        "Scalding milk changes its protein structure for softer bread.",
        "Crumb toppings add texture and flavor to muffins and pies.",
        "Avoid opening the oven door too often to maintain temperature.",
        "Using parchment paper makes clean-up effortless.",
        "Vanilla bean paste has a more intense flavor than extract.",
        "Cutting biscuits straight down prevents uneven rising.",
        "Preheating the oven ensures even baking from the start.",
        "Cornstarch can lighten the texture of cakes and cookies.",
        "Rolling dough between parchment prevents sticking.",
        "Tapioca starch thickens fruit pie fillings perfectly.",
        "Dusting with powdered sugar adds a professional finish.",
        "Silicone baking mats provide a nonstick surface.",
        "Whole wheat flour adds a nutty flavor to baked goods.",
        "Oven thermometers ensure accurate temperature readings.",
        "Marzipan is ideal for creating edible decorations.",
        "Freezing cookie dough makes it easier to slice and bake.",
        "Investing in good bakeware leads to better results.",
        "Caramelized sugar creates rich flavors in flans and candies.",
        "Laminated pastry relies on cold butter for success."
    ]
    return random.choice(baking_phrases)


def post_to_profile(page_url, driver, message):
    driver.get(page_url)
    # time.sleep(200)
    try:
        switch_now_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//div[contains(@role, 'none')]//span[contains(text(), 'Switch Now')]"
                )
            )
        )
        print("Switch Now button found. Clicking it...")
        driver.execute_script("arguments[0].click();", switch_now_button)
        time.sleep(random.uniform(1, 2))
    except:
        print("Switch Now button not found. Proceeding to post...")

    # Wait for the "What's on your mind?" button to be clickable
    whats_on_your_mind_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains(@class, 'x1i10hfl') and contains(@class, 'x1ejq31n') and contains(@class, 'xn6708d')]"
                "//span[contains(text(), \"What's on your mind?\")]"
            )
        )
    )

    # Scroll to the element to ensure it's in view
    driver.execute_script("arguments[0].scrollIntoView(true);", whats_on_your_mind_button)
    time.sleep(random.uniform(1, 2))

    # Click the button (using JavaScript click if normal click fails)
    try:
        whats_on_your_mind_button.click()
    except:
        driver.execute_script("arguments[0].click();", whats_on_your_mind_button)

    time.sleep(random.uniform(2, 4))

    # Wait for the message field to appear and locate it
    message_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//div[@role='textbox' and contains(@aria-label, \"What's on your mind?\") and contains(@contenteditable, 'true')]"
            )
        )
    )
    time.sleep(random.uniform(1, 2))
    
    for char in message:
        message_field.send_keys(char)
        time.sleep(random.uniform(0.1, 0.3))

    post_button = driver.find_element(By.XPATH, "//span[text()='Post']")
    post_button.click()

    time.sleep(random.uniform(3, 5))

    print("Post has been made successfully.")
    
    time.sleep(random.uniform(5, 7))  

    # Locate the Share button's parent div
    share_button = driver.find_element(By.CSS_SELECTOR, 'div[role="button"][aria-label*="Send this to friends"]')

    # Highlight the element red using JavaScript
    driver.execute_script("arguments[0].style.border='2px solid red'", share_button)

    # Pause for visualization
    time.sleep(2)

    # Simulate Enter key press
    share_button.send_keys(Keys.ENTER)
    time.sleep(random.uniform(3, 5))

    # Wait for the "Copy Link" option and press Enter
    wait = WebDriverWait(driver, 5)
    copy_link_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//span[text()="Copy link"]/ancestor::div[@role="button"]'))
    )
    driver.execute_script("arguments[0].style.border='3px solid red'", copy_link_button)
    time.sleep(random.uniform(1, 2))

    copy_link_button.send_keys(Keys.ENTER)
    print("Pressed Enter on the 'Copy Link' option.")

    time.sleep(random.uniform(5, 10))


    post_url = pyperclip.paste()
    print(f"Copied Post URL: {post_url}")

    # * Get the share link from clipboard
    share_link = pyperclip.paste()
    print(f"Copied Share Link: {share_link}")

    # Open the share link in a new tab and extract the permalink
    driver.execute_script("window.open();")  # Open a new tab
    driver.switch_to.window(driver.window_handles[-1])  # Switch to the new tab
    driver.get(share_link)  # Open the share link

    time.sleep(random.uniform(5, 7))  # Wait for the page to load
    final_url = driver.current_url  # Extract the URL from the address bar
    print(f"Final Post URL: {final_url}")

    # Close the new tab and return to the original
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

    return final_url

def random_delay(min_time=1, max_time=3):
    """Add a random delay to simulate human behavior."""
    time.sleep(random.uniform(min_time, max_time))

def type_with_delay(element, text):
    """Simulate typing with a delay for each character."""
    for char in text:
        element.send_keys(char)
        time.sleep(random.uniform(0.1, 0.3))  # Random delay between keystrokes

def close_popup(driver):
    """Close the pop-up if it appears."""
    try:
        # Wait until the pop-up close button is visible and clickable
        close_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, "popunder-close"))
        )
        close_button.click()  # Click the close button
        print("Pop-up closed successfully.")
    except Exception as e:
        print("Pop-up not found or could not be closed:", e)

def main():

    tor_path = r"C:\Users\hp\Desktop\Tor Browser\Browser\TorBrowser\Tor\tor.exe"

    tor_process = subprocess.Popen(tor_path, creationflags=subprocess.CREATE_NEW_CONSOLE)

    chrome_options = Options()
    chrome_options.add_argument('--proxy-server=socks5://127.0.0.1:9050')  # Tor's default SOCKS5 proxy
    chrome_options.add_argument('--disable-notifications')

    driver = webdriver.Chrome(executable_path=r'C:\Users\hp\chromedriver.exe', options=chrome_options)
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[0])
    driver.get("https://www.facebook.com/")
    
    time.sleep(random.uniform(2, 5))  # Random sleep time between actions

    try:
        decline_button = driver.find_element(By.XPATH, "//span[contains(text(), 'Decline optional cookies')]")
        decline_button.click()
        print("Declined optional cookies")
        time.sleep(random.uniform(1, 2))  # Random delay after clicking the button
    except Exception as e:
        print("Could not find the 'Decline optional cookies' button:", e)

    email_field = driver.find_element(By.ID, "email")
    for char in facebook_email:
        email_field.send_keys(char)
        time.sleep(random.uniform(0.1, 0.3))  # Random typing speed (0.1 to 0.3 seconds per key)

    time.sleep(random.uniform(1, 2))

    password_field = driver.find_element(By.ID, "pass")
    for char in facebook_password:
        password_field.send_keys(char)
        time.sleep(random.uniform(0.1, 0.3))  # Random typing speed (0.1 to 0.3 seconds per key)


    time.sleep(random.uniform(1, 2))

    login_button = driver.find_element(By.NAME, "login")
    login_button.click()

    time.sleep(random.uniform(10, 20))  # Random wait time after login action

    # Switch to the new tab
    driver.switch_to.window(driver.window_handles[-1])
    # Directly navigate to the login page
    driver.get("https://www.like4like.org/login/")
    random_delay(2, 4)
    close_popup(driver)
    # Wait for the username and password fields to be present
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
    )
    password_field = driver.find_element(By.ID, "password")

    # Enter your login details with typing delay
    type_with_delay(username_field, like4like_username) 
    random_delay(1, 2)
    type_with_delay(password_field, like4like_password) 

    # Scroll to the submit button to simulate natural behavior
    submit_button = driver.find_element(By.XPATH, "//span[@onclick='LoginFunctions();']")
    driver.execute_script("arguments[0].scrollIntoView();", submit_button)
    random_delay(1, 3)

    # Click the submit button using JavaScript
    driver.execute_script("arguments[0].click();", submit_button)

    random_delay(2, 5)

    close_popup(driver)

    random_delay(1, 3)

    # Locate the "+ Add New" button and redirect to its URL
    add_new_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[contains(text(), '+ Add New')]"))
    )
    add_new_url = add_new_button.get_attribute("href")  # Get the URL from the href attribute
    print(f"Redirecting to: {add_new_url}")
    driver.get(add_new_url)  # Navigate directly to the URL
    print("Redirected to the 'Add New' page.")

    # Wait a few seconds to observe the action (if needed)
    random_delay(3, 6)

    # Locate the dropdown for feature selection
    feature_dropdown = Select(driver.find_element(By.ID, "select-feature"))

    # Check the currently selected option
    selected_option = feature_dropdown.first_selected_option.get_attribute("value")
    print(f"Currently selected feature: {selected_option}")

    # Set the dropdown to "Facebook Likes" if not already selected
    if selected_option != "facebook":
        feature_dropdown.select_by_value("facebook")  # Set to Facebook Likes
        print("Changed feature to Facebook Likes.")
    else:
        print("Feature is already set to Facebook Likes.")

    random_delay(2, 4)

    while True:
        driver.switch_to.window(driver.window_handles[0])
        # ----------------GET POST FROM RONALDO PAGE AND POST THAT-------------------
        file_path = 'out.txt'
        saved_post = read_post_from_file(file_path)
        print(f"Saved post from file:\n{saved_post}")
        
        post_text = None
        while True:
            post_text = get_latest_post()
            driver.refresh()
            if post_text.strip() == saved_post:
                print("The latest post is the same as the saved one. Waiting for an update...")
                time.sleep(random.uniform(5, 10))  # Wait a bit before checking again
            else:
                print("A new post has been detected!")
                write_post_to_file(post_text, file_path)  # Save the new post to the file
                break

        if post_text:
            print(f"Latest post from Ronaldo: {post_text}")
            
            time.sleep(random.uniform(2, 4))  # Random delay

            page_url = "https://www.facebook.com/profile.php?id=61569961403584"
            post_link = post_to_profile(page_url, driver, post_text)
            if post_link:
                print(f"Check out your post at: {post_link}")
        else:
            print("Failed to get the latest post.")
        
        # !----------------------------------------------------------------
        # *----------------------------------------------------------------
        # !--------------------NOW TO THE COLLUSION SITE-------------------
        # *----------------------------------------------------------------
        # !----------------------------------------------------------------

        try:
            driver.switch_to.window(driver.window_handles[-1])
            while True:
                while True:
                    # Check if the Facebook URL field is already visible
                    try:
                        add_fb_link_button = WebDriverWait(driver, 10).until(
                            EC.element_to_be_clickable((By.XPATH, "//span[contains(normalize-space(text()), '+ Add New Facebook Link')]"))
                        )
                        add_fb_link_button.click()
                        random_delay(2, 4)
                        print("Facebook URL box not opened; clicking '+ Add New Facebook Link' button.")
                    except Exception:
                        print("Facebook URL box opened automatically.")

                    random_delay(2, 4)
                    # Fill in the Facebook URL field
                    try:
                        fb_url_field = WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.ID, "add-facebook"))
                        )
                        break
                    except:
                        print("Add facebook link url not found!")
                facebook_link = post_link
                type_with_delay(fb_url_field, facebook_link)  # Replace with your Facebook URL
                random_delay(1, 3)

                # Select "Credits Per Like" as 2
                credits_dropdown = Select(
                    WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.ID, "add-facebook-credits"))
                    )
                )
                credits_dropdown.select_by_value("2")  # Select the option with value "2"
                print("Set Credits Per Like to 2.")
                random_delay(1, 2)

                # Submit the form
                submit_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Submit')]"))
                )
                submit_button.click()
                print("Clicked the Submit button.")
                random_delay(10, 20)
                try:
                    no_limit_button = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located(
                        (By.XPATH, "//a[normalize-space(text())='No\xa0Limit']")
                    )
                    )
                    break
                except:
                    print('getting an error in searching for new Link (no limit), trying again')
                    driver.refresh()

            # Scroll the element into view
            driver.execute_script("arguments[0].scrollIntoView(true);", no_limit_button)

            # Wait a little bit to ensure it's fully visible
            WebDriverWait(driver, 1).until(EC.element_to_be_clickable(no_limit_button))

            # Now click on it
            driver.execute_script("arguments[0].click();", no_limit_button)
            print("Clicked on the 'No Limit' button.")

            random_delay(2, 4)

            # Wait for the checkbox with a partial id match and click it
            total_limit_checkbox = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//input[starts-with(@id, 'total-limit-chb-')]")
                )
            )
            total_limit_checkbox.click()  # Check the checkbox
            print("Checked 'Set Total Credits' checkbox.")
            random_delay(1, 2)

            # Locate the total credits input field with a partial id match and enable it if needed
            total_credits_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//input[starts-with(@id, 'ID_LIMIT_STAVKE_total_')]")
                )
            )

            # Enable the field by removing the disabled attribute if it's present
            driver.execute_script("arguments[0].removeAttribute('disabled')", total_credits_input)

            # Ensure the field is visible and interactable (sometimes fields are hidden behind others)
            driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].style.display = 'block';", total_credits_input)

            # Clear and input the value
            total_credits_input.clear()
            total_credits_input.send_keys("14")  # Enter custom limit
            print("Set Total Credits to 14.")
            random_delay(1, 2)

            # Correct the XPath by combining the conditions properly
            save_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//a[starts-with(@onclick, 'updatelink') and @title='Save Changes']")
            )
            )

            # Click the save button once located
            save_button.click()
            print("Clicked 'Save Changes' button.")
            random_delay(2, 4)

            # while True: 
            #     try:
            #         status_element = WebDriverWait(driver, 10).until(
            #             EC.presence_of_element_located((By.XPATH, "//td/span[contains(@id, 'status')]"))
            #         )

            #         status_text = status_element.text.strip()
            #         print(f"Status found: {status_text}")

            #         if status_text.lower() in ["exhausted", "limited"]:
            #             print(f"Status is '{status_text}'. Processing...")

            #             # Check if there's a "credit limit" link for transitioning to Exhausted
            #             try:
            #                 credit_limit_link = status_element.find_element(By.XPATH, "./following-sibling::a[contains(@id, 'credit_limit')]")
            #                 driver.execute_script("arguments[0].click();", credit_limit_link)
            #                 print("Clicked 'Credit Limit' link to transition to 'Exhausted'.")
            #                 random_delay(2, 4)
            #             except:
            #                 print("No 'Credit Limit' link found; continuing to archive if already 'Exhausted'.")

            #             # Locate the parent <td> and proceed with archiving
            #             parent_td = status_element.find_element(By.XPATH, "./parent::td")
            #             archive_button = parent_td.find_element(By.XPATH, ".//following-sibling::td/a[contains(@onclick, 'archivelink')]")

            #             driver.execute_script("arguments[0].click();", archive_button)
            #             print("Clicked 'Archive' button.")

            #             # Refresh and locate the delete button
            #             driver.refresh()
            #             delete_button = WebDriverWait(driver, 10).until(
            #                 EC.element_to_be_clickable(
            #                     (
            #                         By.XPATH,
            #                         "//a[contains(@onclick, 'deletelink') and contains(@title, 'Click here to delete')]",
            #                     )
            #                 )
            #             )
            #             driver.execute_script("arguments[0].click();", delete_button)
            #             print("Clicked 'Delete' button.")
            #             break 

            #         else:
            #             print(f"Status is '{status_text}' and not ready for processing. Retrying...")
            #             driver.refresh()
            #             random_delay(5, 10)

            #     except Exception as e:
            #         print(f"Error occurred: {e}")
            #         random_delay(5, 10)
            #         driver.refresh()

            #     driver.refresh()

        
        finally:
            # Close the browser
            print("Outside the try")
            time.sleep(random.uniform(3600, 4000))  # Random delay before quitting

    # Step 10: Clean up: Close the browser after use
    time.sleep(random.uniform(2, 4))  # Random delay before quitting
    driver.quit()

    # Step 11: Terminate the Tor process after you're done
    tor_process.terminate()


if __name__ == '__main__':
    main()
