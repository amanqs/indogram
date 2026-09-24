// ==========================================================================
// Indogram Documentation Interactive Logic
// ==========================================================================

document.addEventListener('DOMContentLoaded', () => {
    initCopyButtons();
    initCodeTabs();
    initApiFilter();
    initSearchModal();
});

// 1. Copy Buttons Handler
function initCopyButtons() {
    const copyInstallBtn = document.getElementById('copyInstallBtn');
    const installCmd = document.getElementById('installCmd');

    if (copyInstallBtn && installCmd) {
        copyInstallBtn.addEventListener('click', () => {
            navigator.clipboard.writeText(installCmd.innerText.trim()).then(() => {
                const originalText = copyInstallBtn.innerHTML;
                copyInstallBtn.innerHTML = '<span>✅</span><span>Tersalin!</span>';
                copyInstallBtn.classList.add('copied');

                setTimeout(() => {
                    copyInstallBtn.innerHTML = originalText;
                    copyInstallBtn.classList.remove('copied');
                }, 2000);
            });
        });
    }

    // Code block copy buttons
    const copyCodeBtns = document.querySelectorAll('.copy-code-btn');
    copyCodeBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const targetId = btn.getAttribute('data-target');
            const codeEl = document.getElementById(targetId);
            if (codeEl) {
                navigator.clipboard.writeText(codeEl.innerText).then(() => {
                    const original = btn.innerText;
                    btn.innerText = 'Tersalin!';
                    btn.style.color = '#34d399';
                    setTimeout(() => {
                        btn.innerText = original;
                        btn.style.color = '';
                    }, 2000);
                });
            }
        });
    });
}

// 2. Code Tabs Switcher
function initCodeTabs() {
    const tabBtns = document.querySelectorAll('.tab-btn');
    const tabPanes = document.querySelectorAll('.tab-pane');

    tabBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const tabId = btn.getAttribute('data-tab');

            tabBtns.forEach(b => b.classList.remove('active'));
            tabPanes.forEach(p => p.classList.remove('active'));

            btn.classList.add('active');
            const activePane = document.getElementById(tabId);
            if (activePane) {
                activePane.classList.add('active');
            }
        });
    });
}

// 3. API Reference Live Search & Filter
function initApiFilter() {
    const searchInput = document.getElementById('apiSearchInput');
    const chips = document.querySelectorAll('.category-chips .chip');
    const apiCards = document.querySelectorAll('.api-card');

    let currentCategory = 'all';
    let currentQuery = '';

    function filterCards() {
        apiCards.forEach(card => {
            const category = card.getAttribute('data-category');
            const cardText = card.innerText.toLowerCase();

            const matchesCategory = (currentCategory === 'all' || category === currentCategory);
            const matchesQuery = cardText.includes(currentQuery.toLowerCase());

            if (matchesCategory && matchesQuery) {
                card.style.display = 'block';
            } else {
                card.style.display = 'none';
            }
        });
    }

    if (searchInput) {
        searchInput.addEventListener('input', (e) => {
            currentQuery = e.target.value.trim();
            filterCards();
        });
    }

    chips.forEach(chip => {
        chip.addEventListener('click', () => {
            chips.forEach(c => c.classList.remove('active'));
            chip.classList.add('active');
            currentCategory = chip.getAttribute('data-category');
            filterCards();
        });
    });
}

// 4. Modal Search (Ctrl + K)
function initSearchModal() {
    const modal = document.getElementById('searchModal');
    const trigger = document.getElementById('searchTriggerBtn');
    const closeBtn = document.getElementById('closeModalBtn');
    const modalInput = document.getElementById('modalSearchInput');
    const resultsContainer = document.getElementById('modalSearchResults');

    const apiCards = Array.from(document.querySelectorAll('.api-card')).map(card => {
        const name = card.querySelector('.api-name')?.innerText || '';
        const desc = card.querySelector('.api-desc')?.innerText || '';
        const badge = card.querySelector('.api-badge')?.innerText || '';
        return { name, desc, badge, element: card };
    });

    function openModal() {
        modal.classList.add('open');
        modalInput.value = '';
        renderResults('');
        setTimeout(() => modalInput.focus(), 50);
    }

    function closeModal() {
        modal.classList.remove('open');
    }

    function renderResults(query) {
        const q = query.toLowerCase();
        const filtered = apiCards.filter(item => 
            !q || item.name.toLowerCase().includes(q) || item.desc.toLowerCase().includes(q)
        );

        if (filtered.length === 0) {
            resultsContainer.innerHTML = '<div style="padding:20px;text-align:center;color:#64748b;">Tidak ada API yang cocok</div>';
            return;
        }

        resultsContainer.innerHTML = filtered.map(item => `
            <div class="search-result-item" onclick="selectResult('${item.name}')">
                <div class="search-result-title">${item.name} <span style="font-size:0.75rem;opacity:0.6;margin-left:6px;">(${item.badge})</span></div>
                <div class="search-result-snippet">${item.desc}</div>
            </div>
        `).join('');
    }

    window.selectResult = function(name) {
        closeModal();
        const searchInput = document.getElementById('apiSearchInput');
        if (searchInput) {
            searchInput.value = name.split('(')[0];
            searchInput.dispatchEvent(new Event('input'));
            document.getElementById('api-reference').scrollIntoView({ behavior: 'smooth' });
        }
    };

    if (trigger) trigger.addEventListener('click', openModal);
    if (closeBtn) closeBtn.addEventListener('click', closeModal);

    modal.addEventListener('click', (e) => {
        if (e.target === modal) closeModal();
    });

    modalInput.addEventListener('input', (e) => {
        renderResults(e.target.value.trim());
    });

    document.addEventListener('keydown', (e) => {
        if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') {
            e.preventDefault();
            if (modal.classList.contains('open')) closeModal();
            else openModal();
        } else if (e.key === 'Escape' && modal.classList.contains('open')) {
            closeModal();
        }
    });
}
