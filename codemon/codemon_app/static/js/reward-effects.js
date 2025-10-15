// Simplified Reward Button Effects
console.log('Reward effects loaded - simplified version');

function initRewardEffects() {
    document.addEventListener('click', (e) => {
        const button = e.target.closest('.btn-reward');
        if (button) {
            handleRewardClick(button);
        }
    });
}

function handleRewardClick(button) {
    // Prevent multiple clicks during animation
    if (button.classList.contains('animating')) return;
    button.classList.add('animating');
    
    // 1. Button pulse animation
    button.style.animation = 'rewardPulse 0.6s ease';
    
    // 2. Create a few simple confetti particles
    createSimpleConfetti(button);
    
    // 3. Animate roll counter if present
    const rollCounter = button.querySelector('.roll-counter');
    if (rollCounter) {
        rollCounter.style.animation = 'counterPop 0.8s ease';
    }
    
    // Reset after animation
    setTimeout(() => {
        button.classList.remove('animating');
        button.style.animation = '';
        if (rollCounter) rollCounter.style.animation = '';
    }, 600);
}

function createSimpleConfetti(button) {
    const rect = button.getBoundingClientRect();
    const centerX = rect.left + rect.width / 2;
    const centerY = rect.top + rect.height / 2;
    
    // Create 6 simple confetti pieces
    for (let i = 0; i < 6; i++) {
        setTimeout(() => {
            createConfettiPiece(centerX, centerY, i);
        }, i * 100);
    }
}

function createConfettiPiece(x, y, index) {
    const confetti = document.createElement('div');
    const colors = ['#FFD700', '#10B981', '#3B82F6'];
    const emojis = ['✨', '⭐', '🎯'];
    
    confetti.textContent = emojis[index % 3];
    confetti.style.cssText = `
        position: fixed;
        left: ${x}px;
        top: ${y}px;
        font-size: 16px;
        pointer-events: none;
        z-index: 10000;
        opacity: 1;
        transition: all 0.8s ease-out;
    `;
    
    document.body.appendChild(confetti);
    
    // Animate with CSS transitions
    setTimeout(() => {
        const angle = (index * 60) * (Math.PI / 180); // Spread evenly
        const distance = 40 + Math.random() * 30;
        const finalX = Math.cos(angle) * distance;
        const finalY = Math.sin(angle) * distance - 50;
        
        confetti.style.transform = `translate(${finalX}px, ${finalY}px) rotate(180deg)`;
        confetti.style.opacity = '0';
    }, 10);
    
    // Remove after animation
    setTimeout(() => {
        confetti.remove();
    }, 800);
}

// Initialize when ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initRewardEffects);
} else {
    initRewardEffects();
}