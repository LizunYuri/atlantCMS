const cycleObjectsCard = document.querySelectorAll('.cycle-objects-card')
const cycleObjectsSubtitle = document.querySelectorAll('.cycle-objects-subtitle')
const cycleObjectsTitle = document.querySelectorAll('.cycle-objects-title')
const cycleObjectsImg = document.querySelectorAll('.cycle-objects-img')
const backgroundSlides = document.querySelectorAll('.first-screen-slide')
const itemAnimation = document.querySelectorAll('.item-animation-objects')
const itemAnimationExpress = document.querySelectorAll('.item-animation-objects-express')
const elementReverse = document.querySelectorAll('.trainer-content-card')

const cycleEffectCard = (content, timing, effect, delay, percent) => {
    content.forEach((e, index) => {
        const position = e.getBoundingClientRect();
        const positionCenter = position.top + (position.height * percent);

        if (positionCenter < window.innerHeight) {
            setTimeout(() => {
                e.classList.add(effect);
            }, timing + index * delay);
        }
    });
};

const cycleEffectFade = (content, timeout, effect, percent) => {
    content.forEach((e) => {
        const position = e.getBoundingClientRect(); // Исправлено на e
        const positionElement = position.top + position.height * percent;

        if (positionElement < window.innerHeight) {
            setTimeout(() => {
                e.classList.add(effect);
            }, timeout);
        }
    });
};

const slideShowBackground = () =>{
    let currentSlide = 0;
    const intervalSlideShow = 6000;

    const slideShow = (index) => {
        backgroundSlides.forEach((slide, i) => {
            slide.classList.remove('active-slide')
            if(i === index){
                slide.classList.add('active-slide')
            }
        })
    }

    const nextSlide = () => {
        currentSlide = (currentSlide + 1) % backgroundSlides.length
        slideShow(currentSlide)
    }

    slideShow(currentSlide)
    setInterval(nextSlide, intervalSlideShow)

}


const reverseBlock =() => {
    
    if (window.innerWidth < 468) {
        elementReverse.forEach((e) => {
            
                e.style.flexDirection = 'column';
            
        })
    } else {
        elementReverse.forEach((e, index) => {
            if ((index + 1) % 2 === 0) {
                e.style.flexDirection = 'row-reverse';
            }
        })
    }

}


const handleScrollEffect = () => {
    cycleEffectCard(
        cycleObjectsCard,
        700,
        'fade-element',
        300,
        0.1
        );
        cycleEffectCard(
            itemAnimation,
            700,
            'fade-element',
            300,
            0.1
        );
        cycleEffectCard(
            itemAnimationExpress,
            400,
            'fade-element',
            200,
            0.1
        );

    cycleEffectFade(
        cycleObjectsSubtitle,
        500,
        'fade-element',
        0.1
    )
    cycleEffectFade(
        cycleObjectsTitle,
        600,
        'fade-element',
        0.1
    )
    cycleEffectFade(
        cycleObjectsImg,
        700,
        'fade-element',
        0.2
    )
    cycleEffectFade(
        cycleObjectsImg,
        700,
        'fade-element',
        0.2
    )
}

window.addEventListener('DOMContentLoaded', () => {
    handleScrollEffect();
    slideShowBackground();
    reverseBlock ();
    window.addEventListener('scroll', handleScrollEffect);
});


