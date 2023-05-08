const alerts = document.getElementById('alerts')
const restaurantLink = document.getElementById('restaurant-link')
const navbar = document.querySelector('.navbar-collapse')

setTimeout(() => {
    alerts.classList.add('hide')
}, 4000);

restaurantLink.addEventListener('click', () => {
    navbar.classList.remove('show')  
})