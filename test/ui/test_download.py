from playwright.sync_api import sync_playwright


def test_download(page, tmp_path):
    page.goto("https://demoqa.com/upload-download")

    file_path = tmp_path / "demoqa_test_file.txt"
    file_path.write_text("Hello, this is a test file for DemoQA upload!")

    page.set_input_files("#uploadFile", str(file_path))

    uploaded_file_name = page.locator("#uploadedFilePath")
    assert file_path.name in uploaded_file_name.inner_text()

