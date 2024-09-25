document.querySelectorAll('#dropdownMenu a').forEach(function(item) {
    item.addEventListener('click', function(event) {
        event.preventDefault();
        var statusText = this.textContent;
        var statusButton = document.getElementById('statusButton');

        // Modifier le texte du bouton
        statusButton.innerText = statusText + ' ▼';

        // Modifier la couleur selon le statut sélectionné
        if (this.dataset.status === 'a-traite') {
            statusButton.className = 'status-btn red'; // Rouge pour "À Traiter"
        } else if (this.dataset.status === 'en-cours') {
            statusButton.className = 'status-btn orange'; // Orange pour "En Cours"
        } else if (this.dataset.status === 'traite') {
            statusButton.className = 'status-btn green'; // Vert pour "Traité"
        }
    });
});
