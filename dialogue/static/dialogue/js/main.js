const header = document.querySelector("[data-header]");
const navToggle = document.querySelector("[data-nav-toggle]");
const navMenu = document.querySelector("[data-nav-menu]");
const hero = document.querySelector("[data-event-date]");

function updateHeader() {
    if (!header) {
        return;
    }
    header.classList.toggle("is-scrolled", window.scrollY > 8);
}

function pad(value) {
    return String(value).padStart(2, "0");
}

function updateCountdown() {
    if (!hero) {
        return;
    }

    const eventTime = new Date(hero.dataset.eventDate).getTime();
    const remaining = eventTime - Date.now();
    const safeRemaining = Math.max(remaining, 0);

    const days = Math.floor(safeRemaining / (1000 * 60 * 60 * 24));
    const hours = Math.floor((safeRemaining / (1000 * 60 * 60)) % 24);
    const minutes = Math.floor((safeRemaining / (1000 * 60)) % 60);

    const daysEl = document.querySelector("[data-days]");
    const hoursEl = document.querySelector("[data-hours]");
    const minutesEl = document.querySelector("[data-minutes]");

    if (daysEl) {
        daysEl.textContent = String(days);
    }
    if (hoursEl) {
        hoursEl.textContent = pad(hours);
    }
    if (minutesEl) {
        minutesEl.textContent = pad(minutes);
    }
}

if (navToggle && navMenu) {
    navToggle.addEventListener("click", () => {
        const isOpen = navMenu.classList.toggle("is-open");
        navToggle.setAttribute("aria-expanded", String(isOpen));
    });

    navMenu.addEventListener("click", (event) => {
        if (event.target instanceof HTMLAnchorElement) {
            navMenu.classList.remove("is-open");
            navToggle.setAttribute("aria-expanded", "false");
        }
    });
}

window.addEventListener("scroll", updateHeader, { passive: true });
updateHeader();
updateCountdown();
window.setInterval(updateCountdown, 60000);
