const { text } = require("stream/consumers");

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
  if (navigator.clipboard) {
    navigator.clipboard
      .writeText(text)
      .then(() => {
        console.log("Text copied to clipboard");
      })
      .catch((err) => {
        console.error("Failed to copy text: ", err);
        fallbackCopyTextToClipboard(text);
      });
  } else {
    fallbackCopyTextToClipboard(text);
  }
}



function fallbackCopyTextToClipboard(text) {
  var textArea = document.createElement("textarea");
  textArea.value = text;

  // Avoid scrolling to bottom
  textArea.style.top = "0";
  textArea.style.left = "0";
  textArea.style.position = "fixed";

  document.body.appendChild(textArea);
  textArea.focus();
  textArea.select();

  try {
    var successful = document.execCommand("copy");
    var msg = successful ? "successful" : "unsuccessful";
    console.log("Fallback: Copying text command was " + msg);
  } catch (err) {
    console.error("Fallback: Oops, unable to copy", err);
  }

  document.body.removeChild(textArea);
}
