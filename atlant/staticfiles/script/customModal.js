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


    // Обработчик для первой формы
    const clientForm = document.getElementById('client-form');
    if (clientForm) {
        clientForm.addEventListener('submit', function(event) {
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
                    clientForm.style.display = 'none';
                } else {
                    alert(data.message);
                }
            })
            .catch(error => console.error("Ошибка:", error));
        });
    }

    // Обработчик для формы отзыва
    const reviewForm = document.getElementById('review-form');
    if (!reviewForm) {
        console.error('Форма отзыва не найдена на странице');
    } else {
        console.log('Форма отзыва найдена');
        reviewForm.addEventListener('submit', function (e) {
            e.preventDefault();
            console.log('Форма отзыва отправлена');  // Проверяем, срабатывает ли это событие

            let formData = new FormData(reviewForm);
            fetch(window.submitReviewUrl, {
                method: 'POST',
                body: formData,
                headers: {
                    'X-Requested-With': 'XMLHttpRequest',
                    'X-CSRFToken': reviewForm.querySelector('[name=csrfmiddlewaretoken]').value
                }
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Ошибка в ответе от сервера');
                }
                return response.json();
            })
            .then(data => {
                console.log('Ответ сервера:', data);  // Проверяем ответ сервера
                if (data.status === 'success') {
                    document.getElementById('success-message-review').style.display = 'block';
                    reviewForm.style.display = 'none';
                } else {
                    console.error('Ошибка сервера:', data.message);
                    alert(data.message);
                }
            })
            .catch(error => {
                console.error('Ошибка при отправке формы через AJAX:', error);
                alert('Ошибка при отправке данных. Пожалуйста, попробуйте еще раз.');
            });
        });
    }
});
