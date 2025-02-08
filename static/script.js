document.addEventListener("DOMContentLoaded", function () {
    let searchInput = document.getElementById("search");
    let cardsContainer = document.querySelector(".cards");
    let cards = Array.from(document.querySelectorAll(".card"));

    searchInput.addEventListener("input", function () {
        let searchText = searchInput.value.toLowerCase();

        let filteredCards = cards
            .map(card => ({
                card,
                title: card.dataset.title.toLowerCase()
            }))
            .filter(({ title }) => title.includes(searchText))
            .sort((a, b) => {
                let indexA = a.title.indexOf(searchText);
                let indexB = b.title.indexOf(searchText);
                return indexA - indexB;
            })
            .map(({ card }) => card);

        // Очищаем контейнер и добавляем отсортированные карточки
        cardsContainer.innerHTML = "";
        filteredCards.forEach(card => cardsContainer.appendChild(card));

        // Если поле поиска пустое, показываем все карточки обратно
        if (searchText === "") {
            cards.forEach(card => cardsContainer.appendChild(card));
        }
    });
});
