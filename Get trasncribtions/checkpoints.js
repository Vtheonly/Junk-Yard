const elements = document.querySelectorAll('[id^="title"][class*="ytd-transcript-section-header-renderer"][aria-hidden="true"][tabindex="-1"]');
const texts = Array.from(elements).map(element => element.textContent.trim());

export default texts;
