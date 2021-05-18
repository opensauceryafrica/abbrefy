document.addEventListener('DOMContentLoaded', () => {
  document.querySelector('.bitlink-item--MAIN').classList =
    'bitlink-item--ACTIVE';

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

  document.querySelector('.button--COPY').dataset.clipboard =
    document.querySelector('.bitlink--MAIN').dataset.abbrefy;

  document.querySelector('.bitlink--detail--MAIN').textContent =
    document.querySelector('.bitlink--MAIN').dataset.abbrefy;

  document
    .querySelector('.bitlink--copy-tooltip')
    .querySelector('input').value =
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
});

// closing the link details view when in mobile view
const close = document.querySelector('.icon.close-icon');

close.onclick = function () {
  const itemDetail = document.querySelector('.item-detail--MAIN.open');
  const activeDetail = document.querySelector('.bitlink-item--ACTIVE');
  activeDetail.classList = 'bitlink-item--MAIN';
  itemDetail.classList.remove('open');
};

// listening for click function on any of the links
document.querySelector('.list--MAIN').onclick = function (e) {
  if (e.target.classList == 'bitlink-item--MAIN') {
    const activeDetail = document.querySelector('.bitlink-item--ACTIVE');
    activeDetail.classList = 'bitlink-item--MAIN';
    link = e.target;
    link.classList = 'bitlink-item--ACTIVE';
    updateView(link);
  } else if (e.target.parentElement.classList == 'bitlink-item--MAIN') {
    const activeDetail = document.querySelector('.bitlink-item--ACTIVE');
    activeDetail.classList = 'bitlink-item--MAIN';
    link = e.target.parentElement;
    link.classList = 'bitlink-item--ACTIVE';
    updateView(link);
  } else if (
    e.target.parentElement.parentElement.classList == 'bitlink-item--MAIN'
  ) {
    const activeDetail = document.querySelector('.bitlink-item--ACTIVE');
    activeDetail.classList = 'bitlink-item--MAIN';
    link = e.target.parentElement.parentElement;
    link.classList = 'bitlink-item--ACTIVE';
    updateView(link);
  } else if (
    e.target.parentElement.parentElement.parentElement.classList ==
    'bitlink-item--MAIN'
  ) {
    const activeDetail = document.querySelector('.bitlink-item--ACTIVE');
    activeDetail.classList = 'bitlink-item--MAIN';
    link = e.target.parentElement.parentElement.parentElement;
    link.classList = 'bitlink-item--ACTIVE';
    updateView(link);
  }
};

function updateView(link) {
  document.querySelector('.item-detail--created-date').textContent =
    'CREATED ' +
    link.querySelector('.bitlink-item--created-date').dataset.date_created;

  document.querySelector('.item-detail--title').textContent =
    link.querySelector('.bitlink-item--title').dataset.title;

  document.querySelector('.item-detail--url').textContent =
    link.querySelector('.bitlink--MAIN').dataset.origin;

  document
    .querySelector('.item-detail--url')
    .setAttribute('href', link.querySelector('.bitlink--MAIN').dataset.origin);

  document.querySelector('.button--COPY').dataset.clipboard =
    link.querySelector('.bitlink--MAIN').dataset.abbrefy;

  document.querySelector('.bitlink--detail--MAIN').textContent =
    link.querySelector('.bitlink--MAIN').dataset.abbrefy;

  document
    .querySelector('.bitlink--copy-tooltip')
    .querySelector('input').value =
    link.querySelector('.bitlink--MAIN').dataset.abbrefy;

  document
    .querySelector('.bitlink--detail--MAIN')
    .setAttribute(
      'title',
      link.querySelector('.bitlink--MAIN').dataset.abbrefy
    );

  document
    .querySelector('.bitlink--copyable-text')
    .setAttribute('href', link.querySelector('.bitlink--MAIN').dataset.abbrefy);

  document.querySelector('.info-wrapper--clicks-text').textContent =
    link.querySelector('.click-count--MAIN').dataset.clicks;

  if (link.querySelector('.click-count--MAIN').dataset.audience.length > 2) {
    locations = [
      ...link
        .querySelector('.click-count--MAIN')
        .dataset.audience.split('[')[1]
        .split(']')[0]
        .split(', '),
    ];

    document.querySelector('.audience--locations---MAIN').innerHTML = '';

    locations.forEach((location) => {
      document.querySelector('.audience--locations---MAIN').innerHTML += `<h6>${
        location.split("'")[1].split("'")[0]
      }</h6>`;
    });
  } else {
    document.querySelector('.audience--locations---MAIN').innerHTML = '';
  }

  // end of view update
}
