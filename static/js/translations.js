let currentLanguage = 'en';
let translations = {};

// Load translations for a specific language
async function loadTranslations(lang) {
    try {
        const response = await fetch(`/static/js/translations/${lang}.json`);
        translations = await response.json();
        currentLanguage = lang;
        translatePage();
        
        // Update the current language display
        document.querySelector('.current-lang').textContent = lang.toUpperCase();
        
        // Update checkmarks in dropdown
        document.querySelectorAll('.dropdown-item i').forEach(icon => {
            icon.classList.add('opacity-0');
        });
        document.querySelector(`[data-lang="${lang}"] i`).classList.remove('opacity-0');
        
        // Store the language preference
        localStorage.setItem('preferred_language', lang);
    } catch (error) {
        console.error('Error loading translations:', error);
    }
}

// Translate the entire page
function translatePage() {
    document.querySelectorAll('[data-translate]').forEach(element => {
        const key = element.getAttribute('data-translate');
        if (translations[key]) {
            if (element.tagName === 'INPUT' && element.getAttribute('placeholder')) {
                element.placeholder = translations[key];
            } else {
                element.textContent = translations[key];
            }
        }
    });
    
    // Handle RTL languages
    const rtlLanguages = ['ar'];
    document.documentElement.dir = rtlLanguages.includes(currentLanguage) ? 'rtl' : 'ltr';
}

// Initialize translations
document.addEventListener('DOMContentLoaded', () => {
    // Set up language switcher
    document.querySelectorAll('.dropdown-item[data-lang]').forEach(item => {
        item.addEventListener('click', (e) => {
            e.preventDefault();
            const lang = e.currentTarget.getAttribute('data-lang');
            loadTranslations(lang);
        });
    });
    
    // Load preferred language or default to English
    const preferredLanguage = localStorage.getItem('preferred_language') || 'en';
    loadTranslations(preferredLanguage);
}); 