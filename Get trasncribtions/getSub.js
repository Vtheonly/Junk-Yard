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
  
  
  
  extractTextBetweenStringsFromElement("0:57:36","1:02:40")
