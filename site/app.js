const roster = document.querySelector("[data-pet-roster]");

function petCard(pet) {
  const article = document.createElement("article");
  article.className = "pet-card";
  const preview = document.createElement("div");
  preview.className = "pet-preview";
  const image = document.createElement("img");
  image.src = pet.preview;
  image.alt = `${pet.name} animated preview`;
  image.loading = "lazy";
  preview.appendChild(image);

  const meta = document.createElement("div");
  meta.className = "pet-meta";
  const copy = document.createElement("div");
  const eyebrow = document.createElement("p");
  eyebrow.className = "eyebrow";
  eyebrow.textContent = `${pet.species} · ${pet.featured ? "Launch pet" : "Collection pet"}`;
  const name = document.createElement("h3");
  name.textContent = pet.name;
  const description = document.createElement("p");
  description.textContent = pet.description;
  const actions = document.createElement("p");
  actions.className = "pet-actions";
  actions.textContent = pet.actions.join(" · ");
  copy.append(eyebrow, name, description, actions);

  const link = document.createElement("a");
  link.className = "round-link";
  link.href = pet.repositoryUrl;
  link.setAttribute("aria-label", `Open ${pet.name} files`);
  link.textContent = "↗";
  meta.append(copy, link);
  article.append(preview, meta);
  return article;
}

fetch("data/pets.json")
  .then((response) => {
    if (!response.ok) throw new Error("catalog unavailable");
    return response.json();
  })
  .then(({ pets }) => {
    roster.replaceChildren();
    pets
      .sort((a, b) => Number(b.featured) - Number(a.featured) || a.name.localeCompare(b.name))
      .forEach((pet) => roster.appendChild(petCard(pet)));
  })
  .catch(() => {
    const message = document.createElement("p");
    message.className = "roster-error";
    message.textContent = "The pet roster is loading from the latest release. Visit GitHub to browse the collection.";
    roster.replaceChildren(message);
  });
