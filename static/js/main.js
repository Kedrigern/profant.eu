document.addEventListener("DOMContentLoaded", function () {
  const feedContainer = document.getElementById("mastodon-feed");
  if (!feedContainer) return; // Pokud nejsme na stránce s pravým sloupcem, skript se ukončí

  const INSTANCE = "https://mastodon.pirati.cz";
  const USERNAME = "keddie";
  const LIMIT = 5;

  fetch(`${INSTANCE}/api/v1/accounts/lookup?acct=${USERNAME}`)
    .then((response) => {
      if (!response.ok) throw new Error("Účet nenalezen");
      return response.json();
    })
    .then((account) =>
      fetch(
        `${INSTANCE}/api/v1/accounts/${account.id}/statuses?limit=${LIMIT}&exclude_replies=true&exclude_reblogs=true`,
      ),
    )
    .then((response) => response.json())
    .then((data) => {
      if (!Array.isArray(data)) throw new Error("API nevrátilo seznam");

      feedContainer.innerHTML = "";

      data
        .filter((toot) => !toot.in_reply_to_id && !toot.in_reply_to_account_id)
        .slice(0, 3)
        .forEach((toot) => {
          const isReblog = !!toot.reblog;
          const post = isReblog ? toot.reblog : toot;

          const date = new Date(toot.created_at).toLocaleDateString("cs-CZ", {
            day: "numeric",
            month: "numeric",
            year: "numeric",
          });

          let cardHtml = "";
          if (post.card && post.card.url) {
            const cardImg = post.card.image
              ? `<div class="card-img-top" style="background-image: url('${post.card.image}'); height: 120px; background-size: cover; background-position: center;"></div>`
              : "";

            cardHtml = `
                        <a href="${post.card.url}" target="_blank" rel="noopener" class="mastodon-card d-block mt-2 border rounded text-decoration-none text-body-emphasis overflow-hidden">
                            ${cardImg}
                            <div class="p-2 bg-body-tertiary">
                                <div class="small fw-bold text-truncate">${post.card.title}</div>
                                <div class="small text-muted text-truncate" style="font-size: 0.8em;">${post.card.provider_name || "Odkaz"}</div>
                            </div>
                        </a>
                    `;
          } else if (
            post.media_attachments &&
            post.media_attachments.length > 0
          ) {
            cardHtml = `
                        <div class="mt-2 d-grid gap-2">
                            ${post.media_attachments
                              .map((attachment) => {
                                const previewUrl =
                                  attachment.preview_url || attachment.url;
                                const fullUrl =
                                  attachment.url || attachment.preview_url;
                                const description =
                                  attachment.description ||
                                  "Příloha k příspěvku";

                                if (
                                  attachment.type === "image" ||
                                  attachment.type === "gifv"
                                ) {
                                  return `
                                    <a href="${fullUrl}" target="_blank" rel="noopener" class="d-block border rounded overflow-hidden text-decoration-none">
                                        <img src="${previewUrl}" alt="${description}" class="img-fluid w-100" loading="lazy">
                                    </a>
                                  `;
                                }

                                return `
                                  <a href="${fullUrl}" target="_blank" rel="noopener" class="d-inline-flex align-items-center text-decoration-none small">
                                      <i class="fa-regular fa-paperclip me-2"></i>${description}
                                  </a>
                                `;
                              })
                              .join("")}
                        </div>
                    `;
          }

          const reblogBadge = isReblog
            ? `<div class="text-success small mb-1"><i class="fa-solid fa-retweet me-1"></i> Sdíleno od <strong>${post.account.display_name || post.account.username}</strong></div>`
            : "";

          // Úprava vzhledu pro citované příspěvky (quote-inline RE:)
          let content = post.content;

          if (post.quote && post.quote.quoted_status) {
            const qs = post.quote.quoted_status;
            const authorName = qs.account.display_name || qs.account.username;

            content = content.replace(
              /<p class="quote-inline">RE:\s*<a[^>]+>.*?<\/a><\/p>/gi,
              `<div class="small mb-2 p-2 bg-body-tertiary rounded border-start border-primary border-3">
              <div class="fw-bold mb-1">
                <i class="fa-solid fa-quote-left text-muted me-1"></i>
                <a href="${qs.url}" target="_blank" rel="noopener" class="text-decoration-none text-body">${authorName}</a>
              </div>
              <div class="text-muted">${qs.content}</div>
            </div>`,
            );
          } else {
            content = content.replace(
              /<p class="quote-inline">RE:\s*(<a[^>]+>).*?<\/a><\/p>/gi,
              '<div class="small mb-2 p-2 bg-body-tertiary rounded border-start border-primary border-3"><i class="fa-solid fa-quote-left text-muted me-1"></i> $1Citovaný příspěvek</a></div>',
            );
          }

          const item = document.createElement("div");
          item.className =
            "list-group-item bg-transparent border-0 p-3 border-bottom"; // bg-transparent kvůli tmavému režimu

          item.innerHTML = `
                    ${reblogBadge}
                    <div class="mastodon-content text-body small">
                        ${content}
                    </div>
                    ${cardHtml}
                    <div class="d-flex justify-content-end mt-2">
                        <a href="${toot.url}" target="_blank" rel="noopener" class="text-muted text-decoration-none" style="font-size: 0.75em;">
                            <i class="fa-regular fa-clock me-1"></i> ${date}
                        </a>
                    </div>
                `;
          feedContainer.appendChild(item);
        });
    })
    .catch((error) => {
      console.error(error);
      feedContainer.innerHTML =
        '<div class="p-3 text-center text-muted small">Nelze načíst feed.</div>';
    });
});

// Matomo inicializace
if (window.AppConfig && window.AppConfig.matomoUrl) {
  var _paq = (window._paq = window._paq || []);
  _paq.push(["trackPageView"]);
  _paq.push(["enableLinkTracking"]);
  (function () {
    var u = window.AppConfig.matomoUrl;
    _paq.push(["setTrackerUrl", u + "matomo.php"]);
    _paq.push(["setSiteId", window.AppConfig.matomoSiteId]);
    var d = document,
      g = d.createElement("script"),
      s = d.getElementsByTagName("script")[0];
    g.async = true;
    g.src = u + "matomo.js";
    s.parentNode.insertBefore(g, s);
  })();
}
