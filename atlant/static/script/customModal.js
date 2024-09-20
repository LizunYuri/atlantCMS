const modal = document.getElementById('custom-modal');
const closeButton = document.querySelector('.closed');
const openModal = document.querySelectorAll('.open-modal');

const modalReview = document.getElementById('custom-modal-review');
const closeButtonReview = document.querySelector('.closed-review');

const openModalWindow = () => {
    modal.style.display = 'flex';
}

const openModalWindowReview = () => {
    modalReview.style.display = 'flex';
}

closeButtonReview.addEventListener('click', () => {
    modalReview.style.display = 'none';
});


window.addEventListener('click', (event) => {
    if (event.target === modalReview) {
        modalReview.style.display = 'none';
    }
});


closeButton.addEventListener('click', () => {
    modal.style.display = 'none';
});


window.addEventListener('click', (event) => {
    if (event.target === modal) {
        modal.style.display = 'none';
    }
});




const userPhoneInput = document.getElementById('phone');

userPhoneInput.addEventListener('input', function(e) {
    let x = this.value.replace(/\D/g, '');
    let formattedNumber = '+7 (';

    if (x.length > 1) {
        formattedNumber += x.substring(1, 4);
    }
    if (x.length >= 5) {
        formattedNumber += ') ' + x.substring(4, 7);
    }
    if (x.length >= 8) {
        formattedNumber += '-' + x.substring(7, 9);
    }
    if (x.length >= 10) {
        formattedNumber += '-' + x.substring(9, 11);
    }

    this.value = formattedNumber;
});


document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('client-form').addEventListener('submit', function(event) {
        event.preventDefault();

        const formData = new FormData(this);
        fetch(window.submitUrl, {
            method: 'POST',
            body: formData,
            headers: {
                'X-Requested-With': 'XMLHttpRequest',
                'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
            },
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                document.getElementById('success-message').style.display = 'flex';
                document.getElementById('client-form').style.display = 'none';
            } else {
                alert(data.message);
            }
        })
        .catch(error => console.error("Ошибка:", error));
    });
});

