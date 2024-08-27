const elements = document.querySelectorAll('[id^="title"][class*="ytd-transcript-section-header-renderer"][aria-hidden="true"][tabindex="-1"]');
const texts = Array.from(elements).map(element => element.textContent.trim());

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



function getChatpter(chapterNumber){
  if (chapterNumber >= 1) {
    return extractTextBetweenStringsFromElement(texts[chapterNumber-1],texts[chapterNumber])
  }
  return "";
}
  
function copySub(chapterNumber) {

  navigator.clipboard.writeText(getChatpter(chapterNumber))
  
}
