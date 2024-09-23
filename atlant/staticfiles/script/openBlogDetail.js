document.querySelectorAll('.open-modal-blog').forEach(button => {
    button.addEventListener('click', function(e) {
        e.preventDefault();
        const pk = this.getAttribute('data-pk');

        // Получаем данные блога через AJAX
        fetch(`blog/${pk}/`)  // Замените на ваш URL
            .then(response => response.json())
            .then(data => {
                const modalBody = document.getElementById('blog-detail');
                modalBody.innerHTML = `
                    <div class="blog-detail-img">
                        <img src="${data.img}" alt="${data.title}">
                    </div>

                    <div class="blog-detail-text">
                        <h3>${data.title}</h3>
                        <h6>${data.theme}</h6>
                        <p>${data.text}</p>
                    </div>
                    
                `;
                document.getElementById('blog-detail-modal').style.display = 'flex';
            });
    });
});

// Закрытие модального окна
document.querySelector('.blog-detail-btn').addEventListener('click', () => {
    document.getElementById('blog-detail-modal').style.display = 'none';
});

window.addEventListener('click', (event) => {
    if (event.target == document.getElementById('blog-detail-modal')) {
        document.getElementById('blog-detail-modal').style.display = 'none';
    }
});
