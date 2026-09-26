import os
from pathlib import Path

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


LIVE_URL = os.environ.get(
    "LIVE_URL",
    "https://poc-12-lost-deal-recovery-phase2.onrender.com/"
)

TIMEOUT = 30
SCREENSHOT_DIR = Path("test-results")
SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)

results = []


def record(name, passed, details=""):
    status = "PASS" if passed else "FAIL"
    results.append((name, status, details))
    print(f"[{status}] {name}")
    if details:
        print(f"       {details}")


def wait_for_page(driver):
    WebDriverWait(driver, TIMEOUT).until(
        lambda d: d.execute_script("return document.readyState") == "complete"
    )


def test_live_url(driver):
    driver.get(LIVE_URL)
    wait_for_page(driver)

    WebDriverWait(driver, TIMEOUT).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//*[contains(normalize-space(), 'LOST DEAL REASON & RECOVERY INTELLIGENCE')]")
        )
    )

    record("Live URL opens", True, LIVE_URL)


def test_main_dashboard(driver):
    heading = WebDriverWait(driver, TIMEOUT).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//*[contains(normalize-space(), 'LOST DEAL REASON & RECOVERY INTELLIGENCE')]")
        )
    )

    record(
        "Main dashboard loads",
        "LOST DEAL REASON & RECOVERY INTELLIGENCE" in heading.text,
        "Dashboard heading is visible",
    )


def test_core_visualization(driver):
    canvases = WebDriverWait(driver, TIMEOUT).until(
        lambda d: d.find_elements(By.TAG_NAME, "canvas")
    )

    record(
        "Core visualization renders",
        len(canvases) > 0,
        f"{len(canvases)} chart canvas element(s) detected",
    )


def test_data_loading(driver):
    source_text = WebDriverWait(driver, TIMEOUT).until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "//*[contains(normalize-space(), 'Synthetic CRM loss and follow-up dataset')]",
            )
        )
    )

    filters = driver.find_elements(By.TAG_NAME, "select")

    record(
        "Data loading",
        bool(source_text.is_displayed()) and len(filters) >= 6,
        f"{len(filters)} filter controls detected",
    )


def test_filter_interaction(driver):
    selects = WebDriverWait(driver, TIMEOUT).until(
        lambda d: d.find_elements(By.TAG_NAME, "select")
    )

    location_filter = Select(selects[0])

    location_filter.select_by_visible_text("Kochi")

    WebDriverWait(driver, TIMEOUT).until(
        lambda d: Select(
            d.find_elements(By.TAG_NAME, "select")[0]
        ).first_selected_option.text == "Kochi"
    )

    record(
        "Filter interaction",
        True,
        "Location filter changed to Kochi",
    )

    location_filter.select_by_visible_text("ALL")


def test_backend_communication(driver):
    result = driver.execute_async_script(
        """
        const done = arguments[0];

        fetch('/api/deals')
          .then(async response => {
              const data = await response.json();

              done({
                  ok: response.ok,
                  status: response.status,
                  count: Array.isArray(data) ? data.length : -1
              });
          })
          .catch(error => {
              done({
                  ok: false,
                  status: 0,
                  count: -1,
                  error: String(error)
              });
          });
        """
    )

    passed = (
        result.get("ok") is True
        and result.get("status") == 200
        and result.get("count", 0) > 0
    )

    record(
        "Frontend-to-backend communication",
        passed,
        f"/api/deals status={result.get('status')}, records={result.get('count')}",
    )


def test_intelligence_panel(driver):
    chart = WebDriverWait(driver, TIMEOUT).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '[data-testid="loss-reason-chart"]')
        )
    )

    canvas = chart.find_element(By.TAG_NAME, "canvas")

    # Scroll the loss-reason Pareto chart into the visible browser area.
    driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center', inline: 'center'});",
        chart,
    )
    driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center', inline: 'center'});",
        canvas,
    )

    # Use the canvas center so the pointer offset stays inside the element.
    rect = driver.execute_script(
        """
        const r = arguments[0].getBoundingClientRect();
        return {
            left: r.left,
            top: r.top,
            width: r.width,
            height: r.height
        };
        """,
        canvas,
    )

    # Selenium offsets are measured from the center of the element.
    from selenium.webdriver.common.action_chains import ActionChains

    offset_x = int(rect["width"] * (0.14 - 0.50))
    offset_y = int(rect["height"] * (0.55 - 0.50))

    ActionChains(driver).move_to_element_with_offset(
        canvas,
        offset_x,
        offset_y,
    ).click().perform()

    try:
        panel_close = WebDriverWait(driver, 8).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, '[aria-label="Close intelligence panel"]')
            )
        )
        panel_title = driver.find_element(
            By.XPATH,
            "//*[contains(normalize-space(), 'DEAL INTELLIGENCE')]",
        )

        passed = panel_close.is_displayed() and panel_title.is_displayed()

        record(
            "Intelligence Panel opens",
            passed,
            "Chart data-point interaction opened the panel",
        )

        panel_close.click()

        WebDriverWait(driver, TIMEOUT).until(
            EC.invisibility_of_element_located(
                (By.CSS_SELECTOR, '[aria-label="Close intelligence panel"]')
            )
        )

        record(
            "Intelligence Panel closes",
            True,
            "Close button successfully closed the panel",
        )

    except TimeoutException:
        record(
            "Intelligence Panel opens",
            False,
            "Panel did not appear after chart interaction",
        )

def test_info_modal(driver):
    info_button = WebDriverWait(driver, TIMEOUT).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '[aria-label="Application information"]')
        )
    )

    info_button.click()

    modal_title = WebDriverWait(driver, TIMEOUT).until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "//*[contains(normalize-space(), 'Lost Deal Reason & Recovery Intelligence')]",
            )
        )
    )

    record(
        "Application Info modal opens",
        modal_title.is_displayed(),
        "Application information is visible",
    )

    # Close the modal using Escape.
    driver.find_element(By.TAG_NAME, "body").send_keys("\ue00c")

    WebDriverWait(driver, TIMEOUT).until(
        lambda d: len(
            d.find_elements(
                By.CSS_SELECTOR,
                '[aria-label="Application information"]',
            )
        )
        > 0
    )


def test_responsive_viewport(driver):
    driver.set_window_size(390, 844)

    WebDriverWait(driver, TIMEOUT).until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "//*[contains(normalize-space(), 'LOST DEAL REASON & RECOVERY INTELLIGENCE')]",
            )
        )
    )

    overflow_info = driver.execute_script(
        """
        const elements = [...document.querySelectorAll("body *")];
        const overflowing = elements
          .filter(el => {
              const r = el.getBoundingClientRect();
              return r.right > window.innerWidth + 2;
          })
          .slice(0, 10)
          .map(el => ({
              tag: el.tagName,
              className: String(el.className).slice(0, 120),
              text: (el.innerText || "").trim().slice(0, 80),
              right: Math.round(el.getBoundingClientRect().right),
              width: Math.round(el.getBoundingClientRect().width),
              outerHTML: el.outerHTML.slice(0, 300)
          }));
        return {
            scrollWidth: document.documentElement.scrollWidth,
            viewportWidth: window.innerWidth,
            overflowing
        };
        """
    )

    no_horizontal_overflow = (
        overflow_info["scrollWidth"] <= overflow_info["viewportWidth"] + 2
    )

    if not no_horizontal_overflow:
        print(f"       Responsive debug: {overflow_info}")

    record(
        "Responsive mobile viewport",
        no_horizontal_overflow,
        "390x844 viewport checked",
    )

    driver.set_window_size(1280, 900)


def write_report():
    report_path = Path("test-results/Test_Report.txt")

    passed = sum(1 for _, status, _ in results if status == "PASS")
    total = len(results)

    with report_path.open("w", encoding="utf-8") as report:
        report.write("POC-12 — Selenium E2E Test Report\n")
        report.write("=" * 45 + "\n\n")
        report.write(f"Live URL: {LIVE_URL}\n\n")

        for index, (name, status, details) in enumerate(results, 1):
            report.write(f"{index}. {name}: {status}\n")
            if details:
                report.write(f"   {details}\n")

        report.write("\n")
        report.write(f"Passed: {passed}/{total}\n")
        report.write(f"Failed: {total - passed}/{total}\n\n")

        if passed == total:
            report.write("FINAL RESULT: 100% PASS\n")
        else:
            report.write("FINAL RESULT: CHANGES REQUIRED\n")


def main():
    driver = webdriver.Chrome()
    driver.set_window_size(1280, 900)

    try:
        test_live_url(driver)
        test_main_dashboard(driver)
        test_core_visualization(driver)
        test_data_loading(driver)
        test_filter_interaction(driver)
        test_backend_communication(driver)
        test_intelligence_panel(driver)
        test_info_modal(driver)
        test_responsive_viewport(driver)

        driver.save_screenshot(
            str(SCREENSHOT_DIR / "selenium_e2e.png")
        )

    except Exception as error:
        record(
            "Unexpected Selenium error",
            False,
            f"{type(error).__name__}: {error}",
        )

    finally:
        write_report()
        driver.quit()

    failed = sum(1 for _, status, _ in results if status == "FAIL")

    print()
    print("Selenium test run complete.")
    print("Report: test-results/Test_Report.txt")
    print("Screenshot: test-results/selenium_e2e.png")

    if failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
