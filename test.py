import nodriver as uc
import time

async def main():

    browser = await uc.start()
    page = await browser.get('https://www.plemiona.pl/')

    username_field = await page.find('username')
    await username_field.send_keys('Eutio')

    time.sleep(2000)

    password_field = await page.find('password')
    await password_field.send_keys('JebacGraczyPremium1')

    log_field = await page.find('btn-login')

    time.sleep(5)
    
    await log_field.click()

    time.sleep(5)

    base_url = await page.evaluate('window.location.origin')

    relative_url = "/page/play/pl225"
    full_url = base_url + relative_url
    new_page = await browser.get(full_url)

    time.sleep(2)

    cookies = await page.send(uc.cdp.network.get_cookies())
    
    # 4. Format them into a single string (like the one in game.php headers)
    cookie_string = "; ".join([f"{c.name}={c.value}" for c in reversed(cookies)])
    print(f"Your Header Cookie String: {cookie_string}")

    time.sleep(100)


async def main2():

    browser = await uc.start()
    page = await browser.get('https://www.whatismybrowser.com/detect/what-is-my-user-agent/')
    value = await page.find('detected_value')
    user_agent = value.text

    print(browser.info.get("User-Agent"))
    print(user_agent)

    time.sleep(100)

if __name__ == '__main__':
    # since asyncio.run never worked (for me)
    uc.loop().run_until_complete(main2())
