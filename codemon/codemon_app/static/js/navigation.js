// static/js/navigation.js
class MobileNavigation {
    constructor() {
        this.toggle = document.querySelector('.nav-toggle');
        this.menu = document.querySelector('.nav-menu');
        this.overlay = this.createOverlay();
        
        this.init();
    }
    
    createOverlay() {
        const overlay = document.createElement('div');
        overlay.className = 'nav-overlay';
        overlay.setAttribute('data-visible', 'false');
        document.body.appendChild(overlay);
        return overlay;
    }
    
    init() {
        // Toggle menu
        this.toggle.addEventListener('click', () => this.toggleMenu());
        
        // Close menu when clicking overlay
        this.overlay.addEventListener('click', () => this.closeMenu());
        
        // Close menu when pressing Escape key
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && this.isMenuOpen()) {
                this.closeMenu();
            }
        });
        
        // Close menu when clicking on nav links (mobile)
        this.menu.querySelectorAll('.nav-link').forEach(link => {
            link.addEventListener('click', () => {
                if (window.innerWidth < 768) {
                    this.closeMenu();
                }
            });
        });
        
        // Handle window resize
        window.addEventListener('resize', () => {
            if (window.innerWidth >= 768 && this.isMenuOpen()) {
                this.closeMenu();
            }
        });
    }
    
    toggleMenu() {
        if (this.isMenuOpen()) {
            this.closeMenu();
        } else {
            this.openMenu();
        }
    }
    
    openMenu() {
        this.menu.setAttribute('data-visible', 'true');
        this.overlay.setAttribute('data-visible', 'true');
        this.toggle.setAttribute('aria-expanded', 'true');
        
        // Trap focus inside menu
        this.trapFocus();
        
        // Prevent body scroll
        document.body.style.overflow = 'hidden';
    }
    
    closeMenu() {
        this.menu.setAttribute('data-visible', 'false');
        this.overlay.setAttribute('data-visible', 'false');
        this.toggle.setAttribute('aria-expanded', 'false');
        
        // Restore body scroll
        document.body.style.overflow = '';
        
        // Return focus to toggle button
        this.toggle.focus();
    }
    
    isMenuOpen() {
        return this.menu.getAttribute('data-visible') === 'true';
    }
    
    trapFocus() {
        const focusableElements = this.menu.querySelectorAll(
            'a, button, input, select, textarea, [tabindex]:not([tabindex="-1"])'
        );
        
        if (focusableElements.length > 0) {
            focusableElements[0].focus();
        }
    }
}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    new MobileNavigation();
});