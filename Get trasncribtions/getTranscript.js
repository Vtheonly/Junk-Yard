
// # Documentation for `copySub(chapterNumber)` Script
// ## Usage
// To copy a chapter's text, simply call the `copySub(chapterNumber)` function with the desired chapter number. The script will automatically handle the extraction and copying process.
// important the tansrcaribe succtiom must be existan clilc on show transcribre

// ## Overview
// This script is designed to extract and copy specific chapters from a YouTube transcript based on the chapter number provided. It automates the process of copying these chapters into the clipboard, making it easy to paste the content into another tool like GPT.
// this is totally unrelated to the python file ,it's just for cleaning the time span this one brings get them from the transcribe section and copies them to the clipboard  for further use (GPT summery mostly for me)
// ## Key Functions

// ### 1. **`extractTextBetweenStringsFromElement(begin, end)`**
// - **Purpose**: Extracts text between two specific strings (`begin` and `end`) within a given HTML element.
// - **Input**: `begin` (string), `end` (string).
// - **Output**: Returns the extracted text between the `begin` and `end` strings.

// ### 2. **`getChatpter(chapterNumber)`**
// - **Purpose**: Retrieves the text for a specific chapter based on the chapter number.
// - **Input**: `chapterNumber` (integer).
// - **Output**: Returns the text of the specified chapter.

// ### 3. **`copySub(chapterNumber)`**
// - **Purpose**: Copies the text of the specified chapter to the clipboard.
// - **Input**: `chapterNumber` (integer).
// - **Output**: Copies the extracted text to the clipboard.

// ### 4. **`fallbackCopyTextToClipboard(text)`**
// - **Purpose**: Provides a fallback method to copy text to the clipboard in case the standard method fails.
// - **Input**: `text` (string).
// - **Output**: Copies the provided text to the clipboard.

// ### 5. **`filterAndJoinEvenIndices(text)`**
// - **Purpose**: Filters and joins text lines, keeping only lines at even indices (useful for removing duplicate lines).
// - **Input**: `text` (string).
// - **Output**: Returns the filtered and joined text.





const elements = document.querySelectorAll(
  '[id^="title"][class*="ytd-transcript-section-header-renderer"][aria-hidden="true"][tabindex="-1"]'
);

const texts = Array.from(elements).map((element) => element.textContent.trim());

function extractTextBetweenStringsFromElement(begin, end) {
  const selector = "#segments-container";
  const element = document.querySelector(selector);

  if (!element) {
    console.error("Element not found with selector:", selector);
    return null;
  }

  const text = element.innerText;
  const startIndex = text.indexOf(begin);

  if (startIndex === -1) {
    console.warn("Start string not found:", begin);
    return null;
  }

  const endIndex = text.indexOf(end, startIndex + begin.length);

  if (endIndex === -1) {
    console.warn("End string not found:", end);
    return null;
  }

  const extractedText = text.substring(startIndex + begin.length, endIndex);
  return extractedText.trim();
}

function getChatpter(chapterNumber) {
  if (chapterNumber >= 1) {
    return extractTextBetweenStringsFromElement(
      texts[chapterNumber - 1],
      texts[chapterNumber]
    );
  }
  return "";
}

function copySub(chapterNumber) {
  let text = getChatpter(chapterNumber);
  fallbackCopyTextToClipboard(text);
}

function fallbackCopyTextToClipboard(text) {
  
  // make one elment
  var textArea = document.createElement("textarea");
  textArea.value = filterAndJoinEvenIndices(text);
  textArea.style.top = "0";
  textArea.style.left = "0";
  textArea.style.position = "fixed";
  document.body.appendChild(textArea);
  textArea.focus();
  textArea.select();

  try {
    var successful = document.execCommand("copy");
    var msg = successful ? "successful" : "unsuccessful";
    console.log("copying text command was " + msg);
  } catch (err) {
    console.error("unable to copy", err);
  }
  document.body.removeChild(textArea);
}

function filterAndJoinEvenIndices(text) {
  const lines = text.split("\n");
  const filteredLines = lines.filter((line, index) => index % 2 === 1);
  const result = filteredLines.join("");
  return result;
}
