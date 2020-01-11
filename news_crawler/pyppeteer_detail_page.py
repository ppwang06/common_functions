"""
@File: pyppeteer_detail_page.md.py
@CreateTime: 2020/1/10 下午7:34
@Desc: pyppeteer的使用
https://www.cnblogs.com/baoyu7yi/p/7058537.html
https://miyakogi.github.io/pyppeteer/reference.html
"""
import asyncio
import logging
import datetime
from pyppeteer import launch


logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")


async def main(start_url: str):
    windows_width = 1366
    windows_height = 768
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 " \
                 "(KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
    logging.info(f"打开浏览器{datetime.datetime.now().isoformat()}")
    args = ["--disable-infobars"]
    browser = await launch(
        headless=False, dumpio=True, handleSIGTERM=False, handleSIGINT=False,
        args=args, logLevel=logging.ERROR, ignoreHTTPSErrors=True
    )
    page = await browser.newPage()
    await page.setViewport(viewport={"width": windows_width, "height": windows_height})
    await page.setUserAgent(user_agent)
    await page.setJavaScriptEnabled(enabled=True)

    await page.goto(start_url)
    await asyncio.sleep(5)
    content = await page.content()

    await page.screenshot({'path': './example.png'})
    await browser.close()
    return content


if __name__ == '__main__':
    url = "https://www.infoq.cn/article/1wm0Y1vdZo8CK5BL1Wuk"
    content = asyncio.get_event_loop().run_until_complete(
        main(start_url=url)
    )
    print(content)




