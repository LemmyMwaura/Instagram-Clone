document.addEventListener('click', (e) => {
    const isDropDownButton = e.target.matches('[data-dropdown-button]')
    if(!isDropDownButton && e.target.closest('[data-dropdown]') != null) return;

    let currentDropdown
    if (isDropDownButton){
        currentDropdown = e.target.closest('[data-dropdown]')
        currentDropdown.classList.toggle('active')
    }

    document.querySelectorAll('[data-dropdown].active').forEach( dropdown => {
        if(dropdown === currentDropdown) return;
        dropdown.classList.remove('active')
    })
})

const modalBtns = document.querySelectorAll('.modal-btn')
modalBtns.forEach((btn) => {
  btn.addEventListener('click', () => {
    closeFlashMessage(btn)
  })
})


function closeFlashMessage(btn){
  let modal = btn.closest('.modal')
  modal.classList.add('inactive')
}
