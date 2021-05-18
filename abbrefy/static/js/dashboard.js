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

document.querySelector('.list--MAIN').onclick = function (e) {
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

// console.log(
//   document.querySelector('.bitlink-item--created-date').dataset.date_created
// );
// console.log(document.querySelector('.bitlink-item--title').dataset.author);
// console.log(document.querySelector('.bitlink-item--title').dataset.title);
// console.log(document.querySelector('.bitlink--MAIN').dataset.origin);
// console.log(document.querySelector('.bitlink--MAIN').dataset.abbrefy);
// console.log(document.querySelector('.click-count--MAIN').dataset.clicks);
// console.log(document.querySelector('.click-count--MAIN').dataset.audience);

document.querySelector('.item-detail--created-date').textContent =
  'CREATED ' +
  document.querySelector('.bitlink-item--created-date').dataset.date_created;

document.querySelector('.item-detail--title').textContent =
  document.querySelector('.bitlink-item--title').dataset.title;

document.querySelector('.item-detail--url').textContent =
  document.querySelector('.bitlink--MAIN').dataset.origin;

document
  .querySelector('.item-detail--url')
  .setAttribute(
    'href',
    document.querySelector('.bitlink--MAIN').dataset.origin
  );

document.querySelector('.bitlink--detail--MAIN').textContent =
  document.querySelector('.bitlink--MAIN').dataset.abbrefy;

document.querySelector('.bitlink--copy-tooltip').querySelector('input').value =
  document.querySelector('.bitlink--MAIN').dataset.abbrefy;

document
  .querySelector('.bitlink--detail--MAIN')
  .setAttribute(
    'title',
    document.querySelector('.bitlink--MAIN').dataset.abbrefy
  );

document
  .querySelector('.bitlink--copyable-text')
  .setAttribute(
    'href',
    document.querySelector('.bitlink--MAIN').dataset.abbrefy
  );

document.querySelector('.info-wrapper--clicks-text').textContent =
  document.querySelector('.click-count--MAIN').dataset.clicks;

locations = [
  ...document
    .querySelector('.click-count--MAIN')
    .dataset.audience.split('[')[1]
    .split(']')[0]
    .split(', '),
];

locations.forEach((location) => {
  document.querySelector('.audience--locations---MAIN').innerHTML += `<h6>${
    location.split("'")[1].split("'")[0]
  }</h6>`;
});
