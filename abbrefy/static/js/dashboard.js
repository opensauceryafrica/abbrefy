// getting API Key Elements
getEl();
document.addEventListener('DOMContentLoaded', () => {
  const itemDetail = document.querySelector('.item-detail--MAIN');
  itemDetail.classList.remove('open');

  // setting the Edit Profile Username on page load
  document.querySelector('#username').value =
    document.querySelector('.username').dataset.author;

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

  document.querySelector('.button--COPY').dataset.clipboard = `http://${
    document.querySelector('.bitlink--MAIN').dataset.abbrefy
  }`;

  document.querySelector('.bitlink--detail--MAIN').textContent = `${
    document.querySelector('.bitlink--MAIN').dataset.abbrefy
  }`;

  // document
  //   .querySelector('.bitlink--copy-tooltip')
  //   .querySelector('input').value =
  //   document.querySelector('.bitlink--MAIN').dataset.abbrefy;

  document
    .querySelector('.bitlink--detail--MAIN')
    .setAttribute(
      'title',
      `http://${document.querySelector('.bitlink--MAIN').dataset.abbrefy}`
    );

  document
    .querySelector('.bitlink--copyable-text')
    .setAttribute(
      'href',
      `http://${document.querySelector('.bitlink--MAIN').dataset.abbrefy}`
    );

  document.querySelector('.info-wrapper--clicks-text').textContent =
    document.querySelector('.click-count--MAIN').dataset.clicks;

  if (
    document.querySelector('.click-count--MAIN').dataset.audience.length > 2
  ) {
    locations = [
      ...document
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
});

// closing the link details view when in mobile view
const close = document.querySelector('.icon.close-icon');

close.onclick = function () {
  const itemDetail = document.querySelector('.item-detail--MAIN');
  const activeDetail = document.querySelector('.bitlink-item--ACTIVE');
  // activeDetail.style.backgroundColor = 'initial';

  itemDetail.classList.remove('open');
};

// listening for click function on any of the links
document.querySelector('.list--MAIN').onclick = function (e) {
  if (
    e.target.classList == 'bitlink-item--MAIN' ||
    e.target.classList == 'bitlink-item--ACTIVE'
  ) {
    const activeDetail = document.querySelector('.bitlink-item--ACTIVE');
    activeDetail.classList = 'bitlink-item--MAIN';
    link = e.target;
    link.classList = 'bitlink-item--ACTIVE';
    updateView(link);
  } else if (
    e.target.parentElement.classList == 'bitlink-item--MAIN' ||
    e.target.parentElement.classList == 'bitlink-item--ACTIVE'
  ) {
    const activeDetail = document.querySelector('.bitlink-item--ACTIVE');
    activeDetail.classList = 'bitlink-item--MAIN';
    link = e.target.parentElement;
    link.classList = 'bitlink-item--ACTIVE';
    updateView(link);
  } else if (
    e.target.parentElement.parentElement.classList == 'bitlink-item--MAIN' ||
    e.target.parentElement.parentElement.classList == 'bitlink-item--ACTIVE'
  ) {
    const activeDetail = document.querySelector('.bitlink-item--ACTIVE');
    activeDetail.classList = 'bitlink-item--MAIN';
    link = e.target.parentElement.parentElement;
    link.classList = 'bitlink-item--ACTIVE';
    updateView(link);
  } else if (
    e.target.parentElement.parentElement.parentElement.classList ==
      'bitlink-item--MAIN' ||
    e.target.parentElement.parentElement.parentElement.classList ==
      'bitlink-item--ACTIVE'
  ) {
    const activeDetail = document.querySelector('.bitlink-item--ACTIVE');
    activeDetail.classList = 'bitlink-item--MAIN';
    // activeDetail.style.backgroundColor = 'initial';
    link = e.target.parentElement.parentElement.parentElement;
    link.classList = 'bitlink-item--ACTIVE';
    updateView(link);
  }
};

function updateView(link) {
  // link.style.backgroundColor = '#fff';
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

  document.querySelector('.button--COPY').dataset.clipboard = `http://${
    link.querySelector('.bitlink--MAIN').dataset.abbrefy
  }`;

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
    .setAttribute(
      'href',
      `http://${link.querySelector('.bitlink--MAIN').dataset.abbrefy}`
    );

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

  const itemDetail = document.querySelector('.item-detail--MAIN');
  itemDetail.classList.add('open');

  // end of view update
}

// helper function for copying link to clipboard
document.querySelector('.button--COPY').addEventListener('click', linkCopy);
function linkCopy() {
  var data = document.querySelector('.button--COPY').dataset.clipboard;

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
  }&url=http://${parent.querySelector('.bitlink--detail--MAIN').textContent}`;
}
function linkedInShare(el) {
  var parent =
    el.parentElement.parentElement.parentElement.parentElement.parentElement
      .parentElement;
  el.href = `https://www.linkedin.com/shareArticle?mini=true&url=http://${
    parent.querySelector('.bitlink--detail--MAIN').textContent
  }&summary=${parent.querySelector('.item-detail--title').textContent}`;
}
function facebookShare(el) {
  var parent =
    el.parentElement.parentElement.parentElement.parentElement.parentElement
      .parentElement;
  el.href = `http://www.facebook.com/sharer/sharer.php?u=http://${
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
    parent
      .querySelector('.bitlink--detail--MAIN')
      .dataset.stealth.toUpperCase() == 'TRUE';
  initTitle = parent.querySelector('.item-detail--title').textContent.trim();
  title.value = initTitle;
  slug.value = parent
    .querySelector('.bitlink--detail--MAIN')
    .textContent.trim()
    .split('/')[1];
  slug.dataset.slug = slug.value;
};
//saving the changes when the save button gets clicked
function handleError(OK1, OK2) {
  titleError = 'Only letters, numbers, and spaces';
  slugError = 'Only letters, numbers, underscores and hyphens';
  if (!OK1 && !OK2) {
    document.querySelector('#title__error').textContent = titleError;
    document.querySelector('#slug__error').textContent = slugError;
  } else if (!OK1) {
    error = 'Only text, hyphen, and underscore';
    document.querySelector('#title__error').textContent = titleError;
    document.querySelector('#slug__error').textContent = '';
  } else if (!OK2) {
    error = 'Only text, hyphen, and underscore';
    document.querySelector('#slug__error').textContent = slugError;
    document.querySelector('#title__error').textContent = '';
  }
}
save.onclick = function (e) {
  newTitle = document.querySelector('#abbrefy__title').value.trim();
  stealth = document.querySelector('#abbrefy__stealth').checked;
  newSlug = document.querySelector('#abbrefy__slug').value.trim();
  slug = document.querySelector('#abbrefy__slug').dataset.slug;

  // validating the inputs
  regexp = /^[a-zA-Z0-9_]+(?:[\w-]*[a-zA-Z0-9]+)*$/gm;
  regexp2 = /^[a-zA-Z0-9_.:|()· ]+(?:[\w-|.()_: ·]a-zA-Z0-9+)*$/gm;

  try {
    OK1 = regexp2.test(newTitle);
    OK2 = regexp.test(newSlug);
  } catch (error) {
    titleError = 'Only letters, numbers, and spaces';
    slugError = 'Only letters, numbers, underscores and hyphens';
    document.querySelector('#title__error').textContent = titleError;
    document.querySelector('#slug__error').textContent = slugError;
    return;
  }

  if (!OK1 || !OK2) {
    handleError(OK1, OK2);
  } else {
    initUpdate();
  }
};

// helper function for initiating the link update
function initUpdate() {
  document.querySelector('#title__error').textContent = '';
  document.querySelector('#slug__error').textContent = '';

  if (newSlug == slug && newTitle == initTitle) {
    data = {
      stealth: stealth,
      idSlug: slug,
    };

    updateLink(data);
  } else if (newSlug != slug && newTitle != initTitle) {
    data = {
      title: newTitle,
      slug: newSlug,
      stealth: stealth,
      idSlug: slug,
    };
    updateLink(data);
  } else if (newSlug != slug) {
    data = {
      slug: newSlug,
      stealth: stealth,
      idSlug: slug,
    };

    updateLink(data);
  } else if (newTitle != initTitle) {
    data = {
      title: newTitle,
      stealth: stealth,
      idSlug: slug,
    };

    updateLink(data);
  }
}

// helper function for updating view
function modView(title, url, stealth) {
  document.querySelector('.item-detail--title').textContent = title;
  document.querySelector('.bitlink--detail--MAIN').textContent = url;
  document.querySelector(
    '.bitlink--detail--MAIN'
  ).dataset.stealth = `${stealth}`;
  document
    .querySelector('.bitlink--detail--MAIN')
    .setAttribute('title', `http://${url}`);
  document
    .querySelector('.bitlink--copyable-text')
    .setAttribute('href', `http://${url}`);

  document.querySelector('.button--COPY').dataset.clipboard = `http://${url}`;

  document
    .querySelector('.bitlink-item--ACTIVE')
    .querySelector('.bitlink-item--title').textContent = title;
  document
    .querySelector('.bitlink-item--ACTIVE')
    .querySelector('.bitlink-item--title').dataset.title = title;
  document
    .querySelector('.bitlink-item--ACTIVE')
    .querySelector('.bitlink--MAIN').textContent = url;
  document
    .querySelector('.bitlink-item--ACTIVE')
    .querySelector('.bitlink--MAIN').dataset.abbrefy = url;
  document
    .querySelector('.bitlink-item--ACTIVE')
    .querySelector('.bitlink--MAIN').dataset.stealth = `${stealth}`;
  document
    .querySelector('.bitlink-item--ACTIVE')
    .querySelector('.bitlink--MAIN')
    .setAttribute('title', url);
}

// ansynchronous function for updating the URL
async function updateLink(data) {
  updateURL = '/api/hidden/url/update/';
  request = await fetch(updateURL, {
    method: 'UPDATE',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
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
    modView(response.data.title, response.data.url, response.data.stealth);
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
    CHARACTER_LIMIT_ERROR: 'You have exceeded the character limit',
    DATA_VALIDATION_ERROR: 'Invalid characters in data sent',
    SECURE_PASSWORD_ERROR: 'Password not strong enough',
    PASSWORD_MATCH_ERROR: 'You provided the wrong password',
    KEY_LIMIT_EXCEEDED: 'You have exceeded the allowed API Key limit',
  };
  return messages[identifier];
}

//deleting the link when the delete button gets clicked
del.onclick = function () {
  slug = document.querySelector('#abbrefy__slug').dataset.slug;

  deleteLink({ idSlug: slug });
};

// helper function for deleting links
async function deleteLink(data) {
  deleteURL = '/api/hidden/url/delete/';

  request = await fetch(deleteURL, {
    method: 'DELETE',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
  });

  response = await request.json();

  // handling response based on error gotten
  if (response.status == false) {
    window.history.back();
    // document.querySelector('#slug__error').textContent = '';
    halfmoon.initStickyAlert({
      content: get_error(response.error),
      alertType: 'alert-danger',
      fillType: 'filled-lm',
    });
  } else {
    deleteView();
    window.history.back();
    // document.querySelector('#slug__error').textContent = '';
    halfmoon.initStickyAlert({
      content: 'Abbrefy link deleted successfully',
      alertType: 'alert-success',
      fillType: 'filled-lm',
    });
  }
}
// helper function for deleting link from view
function deleteView() {
  const newView = document.querySelector('.bitlink-item--MAIN');
  const oldView = document.querySelector('.bitlink-item--ACTIVE');
  const linkCount = document.querySelector('.link__count');
  linkCount.textContent = parseInt(linkCount.textContent) - 1;

  oldView.remove();
  newView.classList = 'bitlink-item--ACTIVE';
  updateView(newView);
}
// helper function for modifying and deleting links end

// helper function for creating abbrefy link
const create = document.querySelector('#create');
create.onclick = function () {
  const longURL = document.querySelector('#abbrefy__url').value;
  const isAuth = document.querySelector('.item-detail--created-link').dataset
    .auth;
  if (longURL.length < 1) {
    return (document.querySelector('#url__error').textContent =
      'Long URL is required');
  } else {
    document.querySelector('#url__error').textContent = '';
  }
  create.textContent = 'Abbrefying...';
  create.style.backgroundColor = '#e67083';

  if (isAuth != 'True') {
    window.history.back();
    return halfmoon.initStickyAlert({
      content: get_error('AUTHORIZATION_ERROR'),
      alertType: 'alert-danger',
      fillType: 'filled-lm',
    });
  }

  shorten(longURL);
};

// helper function for shortening Long URLs
async function shorten(longURL) {
  url = '/api/hidden/url/abbrefy/';
  request = await fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ url: longURL }),
  });
  response = await request.json();

  // handling server response
  if (response.status == false) {
    create.textContent = 'Abbrefy';
    create.style.backgroundColor = '#e3425a';
    window.history.back();
    halfmoon.initStickyAlert({
      content: get_error(response.error),
      alertType: 'alert-danger',
      fillType: 'filled-lm',
    });
  } else {
    addToView(response);
    window.history.back();
    halfmoon.initStickyAlert({
      content: 'Abbrefy Link Created Successfully',
      alertType: 'alert-success',
      fillType: 'filled-lm',
    });
  }
}
// helper function to update view after abbrefying Long URL
function addToView(data) {
  const linkCount = document.querySelector('.link__count');
  linkCount.textContent = parseInt(linkCount.textContent) + 1;
  document.querySelector('#abbrefy__url').value = '';
  create.textContent = 'Abbrefy';
  create.style.backgroundColor = '#e3425a';
  initLinks = document.querySelector('#abbrefy__links__con');

  const newLink = `<a class="bitlink-item--MAIN"><span class="bitlink-item--checkbox"><div class="checkbox--SMALL" id="3uyFTMA">
            <i class="fas fa-code-branch"></i></div></span><time data-date_created="${
              data.dateCreated
            }" class="bitlink-item--created-date" datetime="05-26-2021">${
    data.dateCreated2
  }</time>

        

        <div data-author="${
          document.querySelector('.username').dataset.author
        }" data-title="${data.title}" class="bitlink-item--title">
         ${data.title}
        </div>
        

        <div>
          <div class="bitlink--MAIN" data-origin="${
            data.origin
          }" data-stealth="${data.stealth}" tabindex="-1" title="abbrefy.xyz/${
    data.slug
  }" data-abbrefy="abbrefy.xyz/${data.slug}">
            abbrefy.xyz/<span>${data.slug}</span>
          </div>
          <span data-clicks="${data.clicks}" data-audience="${
    data.audience
  }" class="click-count--MAIN">${
    data.clicks
  }<span class="icon clicks-icon"></span></span></div></a>`;

  initLinks.innerHTML = newLink + initLinks.innerHTML;
}

// helper function for updating the USER PROFILE
const update = document.querySelector('#update');

update.onclick = function () {
  let newUsername = document.querySelector('#username').value;
  let oldPassword = document.querySelector('#old__pass').value;
  let newPassword = document.querySelector('#new__pass').value;

  let validator = /^[a-zA-Z0-9_]+$/gm;
  let validated = validator.test(newUsername);

  if (newUsername.length < 3 || newUsername.length > 10) {
    return (document.querySelector('#username__error').textContent =
      'must be between 3 and 10 characters');
  } else if (!validated) {
    return (document.querySelector('#username__error').textContent =
      'can contain only text and underscore');
  } else {
    document.querySelector('#username__error').textContent = '';
  }

  let profileData = { usernameData: newUsername };

  if (oldPassword.length > 0 && newPassword.length > 0) {
    let passwordData = {
      oldPassword: oldPassword,
      newPassword: newPassword,
    };

    profileData.passwordData = passwordData;
  }
  update.textContent = 'Updating...';
  updateProfile(profileData);
};

// helper function for sending profile update request
async function updateProfile(data) {
  let profileUrl = '/auth/profile/';
  request = await fetch(profileUrl, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
  });

  response = await request.json();
  // handling server response
  if (response.status == false) {
    if (response.error == 'PASSWORD_MATCH_ERROR') {
      document.querySelector('#new__error').textContent = '';
      document.querySelector('#old__error').textContent = get_error(
        response.error
      );
      // reseting the button value
      update.textContent = 'Update';
      create.style.backgroundColor = '#e3425a';
    } else if (response.error == 'SECURE_PASSWORD_ERROR') {
      document.querySelector('#old__error').textContent = '';
      document.querySelector('#new__error').textContent = get_error(
        response.error
      );
      // reseting the button value
      update.textContent = 'Update';
      create.style.backgroundColor = '#e3425a';
    } else {
      // clearing the errors
      document.querySelector('#new__error').textContent = '';
      document.querySelector('#old__error').textContent = '';
      // reseting the button value
      update.textContent = 'Update';
      create.style.backgroundColor = '#e3425a';
      document.querySelector('#old__pass').value = '';
      document.querySelector('#new__pass').value = '';
      window.history.back();
      halfmoon.initStickyAlert({
        content: get_error(response.error),
        alertType: 'alert-danger',
        fillType: 'filled-lm',
      });
    }
  } else {
    profileViewMod(response.data.userData.username);
    document.querySelector('#username').value =
      document.querySelector('.username').dataset.author;
    window.history.back();
    halfmoon.initStickyAlert({
      content: 'Profile update successfully',
      alertType: 'alert-success',
      fillType: 'filled-lm',
    });
  }
}
// helper function for updating UI after profile update
function profileViewMod(username) {
  // setting the username in all aspect of the view
  document.querySelectorAll('.username')[0].textContent = username;
  document.querySelectorAll('.username')[1].textContent = username;
  document.querySelector('.username').dataset.author = username;
  update.textContent = 'Update';
  create.style.backgroundColor = '#e3425a';
  // clearing the input of the password fields
  document.querySelector('#old__pass').value = '';
  document.querySelector('#new__pass').value = '';
}

const key = document.querySelector('#createKey');
// helper function for creating API key
key.onclick = async function createKey() {
  key.textContent = 'Creating...';
  let apiKeyUrl = '/auth/account/apiKey/';
  request = await fetch(apiKeyUrl, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      action: 'createAPIKey',
    }),
  });

  response = await request.json();
  // handling server response

  if (response.status === false) {
    key.textContent = 'Create API Key';
    window.history.back();
    halfmoon.initStickyAlert({
      content: get_error(response.error),
      alertType: 'alert-danger',
      fillType: 'filled-lm',
    });
  } else {
    key.textContent = 'Create API Key';
    content = `
    <div class="form-group">
  <label for="full-name">API Key</label>
  <input
    value="${response.data.apiData.apiKey}"
    readonly
    type="text"
    class="form-control api__key"
  />
  <!-- <small id="old__error" class="invalid-feedback"></small> -->
  <div class="text-right mt-5">
    <a class="api__delete mr-5" role="button">Delete</a>
  </div>
</div>
    
    `;

    document.querySelector('#api__key__con').innerHTML += content;
    getEl();
  }
};

// function for handling API Keys
function getEl() {
  apiKeys = document.querySelectorAll('.api__key');
  apiDelete = document.querySelectorAll('.api__delete');

  // helper function for copying API Keys to clipboard
  apiKeys.forEach((key) => {
    key.onclick = function () {
      key.select();
      key.setSelectionRange(0, 99999);
      document.execCommand('copy');
      window.history.back();
      halfmoon.initStickyAlert({
        content: 'API key copied',
        alertType: 'alert-success',
        fillType: 'filled-lm',
      });
    };
  });

  // helper function for deleting API Keys
  apiDelete.forEach((key) => {
    key.onclick = async function () {
      apiKey = key.parentElement.parentElement.querySelector('input').value;
      let apiKeyDeleteUrl = '/auth/account/apiKey/delete';
      request = await fetch(apiKeyDeleteUrl, {
        method: 'DELETE',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          apiKey: apiKey,
        }),
      });

      response = await request.json();
      // handling server response

      if (response.status === false) {
        window.history.back();
        halfmoon.initStickyAlert({
          content: get_error(response.error),
          alertType: 'alert-danger',
          fillType: 'filled-lm',
        });
      } else {
        key.parentElement.parentElement.remove();
        getEl();
      }
    };
  });
}
