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

  document.querySelector('.bitlink--detail--MAIN').dataset.stealth =
    document.querySelector('.bitlink--MAIN').dataset.stealth;

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

  // document
  //   .querySelector('.bitlink--copy-tooltip')
  //   .querySelector('input').value =
  //   document.querySelector('.bitlink--MAIN').dataset.abbrefy;

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

  document.querySelector('.bitlink--detail--MAIN').dataset.stealth =
    link.querySelector('.bitlink--MAIN').dataset.stealth;

  document
    .querySelector('.item-detail--url')
    .setAttribute('href', link.querySelector('.bitlink--MAIN').dataset.origin);

  document.querySelector('.button--COPY').dataset.clipboard =
    link.querySelector('.bitlink--MAIN').dataset.abbrefy;

  document.querySelector('.bitlink--detail--MAIN').textContent =
    link.querySelector('.bitlink--MAIN').dataset.abbrefy;

  // document
  //   .querySelector('.bitlink--copy-tooltip')
  //   .querySelector('input').value =
  //   link.querySelector('.bitlink--MAIN').dataset.abbrefy;

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

// helper function for copying link to clipboard
document.querySelector('.button--COPY').addEventListener('click', linkCopy);
function linkCopy() {
  var data = document.querySelector('.button--COPY').dataset.clipboard;
  console.log(data);
  const link = document.createElement('input');
  link.value = data;
  document.body.append(link);
  link.select();
  link.setSelectionRange(0, 99999);
  document.execCommand('copy');
  halfmoon.initStickyAlert({
    content: 'Link copied',
    alertType: 'alert-success',
    fillType: 'filled-lm',
  });
  link.remove();
}

//helper functions for link sharing
function twitterShare(el) {
  var parent =
    el.parentElement.parentElement.parentElement.parentElement.parentElement
      .parentElement;
  el.href = `https://twitter.com/intent/tweet?text=${
    parent.querySelector('.item-detail--title').textContent
  }&url=${parent.querySelector('.bitlink--detail--MAIN').textContent}`;
}
function linkedInShare(el) {
  var parent =
    el.parentElement.parentElement.parentElement.parentElement.parentElement
      .parentElement;
  el.href = `https://www.linkedin.com/shareArticle?mini=true&url=${
    parent.querySelector('.bitlink--detail--MAIN').textContent
  }&summary=${parent.querySelector('.item-detail--title').textContent}`;
}
function facebookShare(el) {
  var parent =
    el.parentElement.parentElement.parentElement.parentElement.parentElement
      .parentElement;
  el.href = `http://www.facebook.com/sharer/sharer.php?u=${
    parent.querySelector('.bitlink--detail--MAIN').textContent
  }`;
}
//helper functions for link sharing end

// helper function for modifying and deleting links
let edit = document.querySelector('.button__edit');
let save = document.querySelector('#save');
let del = document.querySelector('#delete');
let modal = document.querySelector('#modal-1');
// prefilling values when the edit button gets clicked
edit.onclick = function () {
  var parent = this.parentElement.parentElement.parentElement.parentElement;
  title = document.querySelector('#abbrefy__title');
  stealth = document.querySelector('#abbrefy__stealth');
  slug = document.querySelector('#abbrefy__slug');
  stealth.checked =
    parent.querySelector('.bitlink--detail--MAIN').dataset.stealth == 'True';
  title.value = parent.querySelector('.item-detail--title').textContent.trim();
  slug.value = parent
    .querySelector('.bitlink--detail--MAIN')
    .textContent.trim()
    .split('/')[3];
  slug.dataset.slug = slug.value;
};
//saving the changes when the save button gets clicked
save.onclick = function (e) {
  title = document.querySelector('#abbrefy__title').value;
  stealth = document.querySelector('#abbrefy__stealth').checked;
  newSlug = document.querySelector('#abbrefy__slug').value;
  slug = document.querySelector('#abbrefy__slug').dataset.slug;

  error = 'Only text, hyphen, and underscore';
  updateLink(title, stealth, newSlug, slug);
};

// ansynchronous function for updating the URL
async function updateLink(title, stealth, newSlug, slug) {
  updateURL = '/api/hidden/url/update/';
  request = await fetch(updateURL, {
    method: 'UPDATE',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      title: title,
      stealth: stealth,
      new_slug: newSlug,
      slug: slug,
    }),
  });

  response = await request.json();
  // handling response based on error gotten
  if (response.status == false) {
    if (response.error == 'USAGE_ERROR') {
      document.querySelector('#slug__error').textContent = get_error(
        response.error
      );
    } else {
      history.back();
      document.querySelector('#slug__error').textContent = '';
      halfmoon.initStickyAlert({
        content: get_error(response.error),
        alertType: 'alert-danger',
        fillType: 'filled-lm',
      });
    }
  } else {
    window.history.back();
    document.querySelector('#slug__error').textContent = '';
    halfmoon.initStickyAlert({
      content: 'Abbrefy link updated successfully',
      alertType: 'alert-success',
      fillType: 'filled-lm',
    });
  }
}

// helper function for passing error
function get_error(identifier) {
  messages = {
    DATA_ERROR: 'URL data is required',
    URL_ERROR: 'That URL is invalid',
    DUPLICATE_ERROR: "That's already an Abbrefy link",
    USAGE_ERROR: 'That slug is already in use',
    EXISTENCE_ERROR: "We couldn't find that link",
    AUTHORIZATION_ERROR: "You aren't authorized for that action",
    UNKNOWN_ERROR: 'Something completely went wrong',
  };
  return messages[identifier];
}

//deleting the link when the delete button gets clicked
del.onclick = function () {
  slug = document.querySelector('#abbrefy__slug').dataset.slug;
};
// helper function for modifying and deleting links end
