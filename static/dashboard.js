$(document).ready(function () {
    let tooltipTriggerList = [].slice.call(document.querySelectorAll('.tip'));
    let tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl, {
            html: true,
            title: document.getElementById(tooltipTriggerEl.dataset.tooltipId).innerHTML,
            placement: 'auto',
            sanitize: false
        })
    })
});
