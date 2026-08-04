// Mobile header menu
(function () {
  const btn = document.getElementById("mobile-menu-btn");
  const links = document.querySelector(".nav-links");

  btn?.addEventListener("click", () => {
    links?.classList.toggle("open");
  });

  links?.querySelectorAll("a").forEach((a) => {
    a.addEventListener("click", () => links.classList.remove("open"));
  });
})();

// Docs sidebar drawer (mobile)
(function () {
  const toggle = document.getElementById("docs-sidebar-toggle");
  const sidebar = document.getElementById("docs-sidebar");
  const backdrop = document.getElementById("docs-sidebar-backdrop");

  function closeSidebar() {
    sidebar?.classList.remove("open");
    backdrop?.classList.remove("open");
    toggle?.setAttribute("aria-expanded", "false");
  }

  function openSidebar() {
    sidebar?.classList.add("open");
    backdrop?.classList.add("open");
    toggle?.setAttribute("aria-expanded", "true");
  }

  toggle?.addEventListener("click", () => {
    if (sidebar?.classList.contains("open")) closeSidebar();
    else openSidebar();
  });

  backdrop?.addEventListener("click", closeSidebar);

  sidebar?.querySelectorAll("a").forEach((a) => {
    a.addEventListener("click", closeSidebar);
  });
})();

// Scoped nested tabs (install / sync-async / etc.)
(function () {
  function activateInGroup(group, panelId) {
    if (!group || !panelId) return false;
    const panel = group.querySelector(`:scope > .tab-panel#${CSS.escape(panelId)}`);
    const btn = group.querySelector(`:scope > .tab-bar > .tab-btn[data-tab="${CSS.escape(panelId)}"]`);
    if (!panel || !btn) return false;

    group.querySelectorAll(":scope > .tab-bar > .tab-btn").forEach((b) => {
      b.classList.remove("active");
      b.setAttribute("aria-selected", "false");
    });
    group.querySelectorAll(":scope > .tab-panel").forEach((p) => {
      p.classList.remove("active");
    });

    btn.classList.add("active");
    btn.setAttribute("aria-selected", "true");
    panel.classList.add("active");
    return true;
  }

  document.querySelectorAll("[data-tabs]").forEach((group) => {
    group.querySelectorAll(":scope > .tab-bar > .tab-btn").forEach((btn) => {
      btn.addEventListener("click", () => {
        activateInGroup(group, btn.dataset.tab);
      });
    });
  });
})();

// Copy code blocks
(function () {
  document.querySelectorAll(".copy-btn").forEach((btn) => {
    btn.addEventListener("click", async () => {
      const block = btn.closest(".code-block");
      const text = block?.querySelector(".code-block-body code")?.textContent ?? "";
      if (!text) return;

      try {
        await navigator.clipboard.writeText(text);
      } catch {
        const range = document.createRange();
        const code = block.querySelector(".code-block-body code");
        if (!code) return;
        range.selectNodeContents(code);
        const sel = window.getSelection();
        sel?.removeAllRanges();
        sel?.addRange(range);
        document.execCommand("copy");
        sel?.removeAllRanges();
      }

      const prev = btn.textContent;
      btn.textContent = "Copied";
      btn.classList.add("copied");
      window.setTimeout(() => {
        btn.textContent = prev;
        btn.classList.remove("copied");
      }, 1600);
    });
  });
})();

// Legacy hash redirects on landing (/#docs-django → /docs/django/)
(function () {
  const HASH_REDIRECTS = {
    "docs-core": "/docs/core/",
    "docs-django": "/docs/django/",
    "docs-fastapi": "/docs/fastapi/",
    "docs-aiohttp": "/docs/aiohttp/",
    "docs-flask": "/docs/flask/",
    docs: "/docs/",
    packages: "/#packages",
  };

  if (!document.body.classList.contains("landing-page")) return;

  const id = location.hash.replace(/^#/, "");
  if (!id || !(id in HASH_REDIRECTS)) return;

  const target = HASH_REDIRECTS[id];
  if (target.startsWith("/#")) return;
  location.replace(target);
})();

// Pagefind search (docs pages)
(function () {
  const mount = document.getElementById("docs-search");
  if (!mount) return;
  if (typeof PagefindUI === "undefined") return;

  try {
    new PagefindUI({
      element: "#docs-search",
      showImages: false,
      showSubResults: true,
      resetStyles: false,
    });
  } catch (err) {
    console.warn("Pagefind UI failed to initialize", err);
  }
})();

// Syntax highlighting
if (window.Prism) {
  Prism.highlightAll();
}
