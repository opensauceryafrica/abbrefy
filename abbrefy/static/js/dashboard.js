document.addEventListener('DOMContentLoaded', () => {
  document.querySelector('.bitlink-item--MAIN').classList =
    'bitlink-item--ACTIVE';
});

const close = document.querySelector('.icon.close-icon');

close.onclick = function () {
  const itemDetail = document.querySelector('.item-detail--MAIN.open');
  const activeDetail = document.querySelector('.bitlink-item--ACTIVE');
  activeDetail.classList = 'bitlink-item--MAIN';
  itemDetail.classList.remove('open');
};

document.onclick = function (e) {
  console.log(e.target);
  console.log(e.target.parentElement);
  console.log(e.target.parentElement.parentElement);
  console.log(e.target.parentElement.parentElement.parentElement);
  console.log('');
  if (
    e.target.classList == 'bitlink-item--MAIN' ||
    e.target.parentElement.classList == 'bitlink-item--MAIN' ||
    e.target.parentElement.parentElement.classList == 'bitlink-item--MAIN' ||
    e.target.parentElement.parentElement.parentElement.classList ==
      'bitlink-item--MAIN'
  ) {
    alert('yay!');
  }
};
