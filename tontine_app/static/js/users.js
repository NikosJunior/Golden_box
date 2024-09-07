function openModal(modalId) {
    var modal = document.getElementById(modalId);
    modal.classList.remove('hidden');
}

function closeModal(modalId) {
    var modal = document.getElementById(modalId);
    modal.classList.add('hidden');
}

const deleteButtons = document.querySelectorAll('.delete-button')
const user = document.getElementById('user')
const id_input = document.getElementById('id_input')

deleteButtons.forEach(button => {
    button.addEventListener('click', (event)=> {
        const Name = event.target.getAttribute('data-name');
        const id = event.target.getAttribute('data-id');
        user.textContent = Name
        id_input.value=id
    })
})