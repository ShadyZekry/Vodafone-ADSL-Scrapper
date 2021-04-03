const puppeteer = require("puppeteer");

function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

(async () => {
  const browser = await puppeteer.launch();
  // const browser = await puppeteer.launch({ headless: false });
  const page = await browser.newPage();
  await page.setViewport({ height: 1080, width: 1920 });
  await page.goto(
    "https://web.vodafone.com.eg",
    {
      waitUntil: "networkidle2",
    }
  );

  await page.click("button[id=InnerloginBtn]");

  await page.waitForFunction(
    'document.querySelectorAll(".spinner.d-none").length == 1'
  );

  await page.focus("#username");
  await page.keyboard.type("YourPhoneNumber");
  await page.focus("#password");
  await page.keyboard.type("YourPassword");

  await page.waitForFunction(
    'document.querySelector("#submitBtn").className ==="btn btn-primary card-btn js-btn-submit2"'
  );
  await page.click("#submitBtn");

  await page.waitForSelector('#maintab-DSL-link')

  page.on("response", async (response) => {
    if (response.url().includes("services/dxl/usage/usageConsumptionReport"))
      console.log(JSON.stringify(await response.json(), null, 2));
  });

  await page.click("a[id=maintab-DSL-link]");

  await sleep(3000);
  await page.screenshot({ path: "screenshot.png" });

  await browser.close();
})();