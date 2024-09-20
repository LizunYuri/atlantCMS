document.addEventListener('DOMContentLoaded', () => {
    const images = document.querySelectorAll('.about-img');
    const texts = document.querySelectorAll('.about-card');
    let currentIndex = 0;

    const updateSlides = () => {
        // Обновляем изобр
        images.forEach((img, index) => {
            img.classList.remove('first', 'second', 'third');
            img.style.display = 'none';
        });

        // Первые три изображения показываем с разными классами
        images[currentIndex].classList.add('first');
        images[currentIndex].style.display = 'block';

        images[(currentIndex + 1) % images.length].classList.add('second');
        images[(currentIndex + 1) % images.length].style.display = 'block';

        images[(currentIndex + 2) % images.length].classList.add('third');
        images[(currentIndex + 2) % images.length].style.display = 'block';

        // Обновляем текстовые блоки
        texts.forEach((text, index) => {
            text.classList.remove('active');
            text.style.display = 'none';
        });

        // Показать только текст, который соответствует изображению с классом 'first'
        const currentImageDataAttr = images[currentIndex].querySelector('img').getAttribute('src').match(/\d/)[0]; 
        texts.forEach(text => {
            
            if (text.getAttribute('data-img') === currentImageDataAttr) {
                setTimeout(() => {
                text.classList.add('active');
                text.style.display = 'block';
            }, 500)
            }
        });
    };


    updateSlides();

    document.querySelector('.next-slide').addEventListener('click', () => {
        currentIndex = (currentIndex + 1) % images.length;
        updateSlides();
    });

    // Кнопка "предыдущий слайд"
    document.querySelector('.prev-slide').addEventListener('click', () => {
        currentIndex = (currentIndex - 1 + images.length) % images.length;
        updateSlides();
    });
});
