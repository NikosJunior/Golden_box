function openModal(modalId) {
    var modal = document.getElementById(modalId);
    modal.classList.remove('hidden');
}

function closeModal(modalId) {
    var modal = document.getElementById(modalId);
    modal.classList.add('hidden');
}

const validation_button = document.querySelectorAll('.valider')
const input_validation = document.getElementById('input-validation')
const input_cancel = document.getElementById('input-cancel')
const amountElement = document.querySelector('.amount')
const nameElement = document.querySelector('.name')
const amountElementC = document.querySelector('.amount-c')
const nameElementC = document.querySelector('.name-c')
const cancel_button = document.querySelectorAll('.canceled')

validation_button.forEach(button => {
    button.addEventListener('click', (event) => {
        const name = event.target.getAttribute('data-name');
        const pk = event.target.getAttribute('data-pk');
        const amount = event.target.getAttribute('data-amount');
        // console.log(name, pk, amount)
        amountElement.textContent = amount;
        input_validation.value = pk;
        nameElement.textContent = name;
    })
})

cancel_button.forEach(button => {
    button.addEventListener('click', (event) => {
        const name = event.target.getAttribute('data-name');
        const pk = event.target.getAttribute('data-pk');
        const amount = event.target.getAttribute('data-amount');
        // console.log(name, pk, amount)
        amountElementC.textContent = amount;
        input_cancel.value = pk;
        nameElementC.textContent = name;
    })
})