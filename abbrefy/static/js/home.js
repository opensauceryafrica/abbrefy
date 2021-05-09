// getting DOM elements
const button = document.querySelector('#abbrefy');

// changing the Abbrefy button state
document.querySelector('#link-input').oninput = function () {
  if (button.classList.contains('copy')) {
    button.textContent = 'Abbrefy';
    button.classList.remove('copy');
  }
};

// handling the unauth shorten event.
button.onclick = function () {
  // setting the copy link state
  if (button.classList.contains('copy')) {
    var link = document.querySelector('#link-input');
    link.select();
    link.setSelectionRange(0, 99999);
    document.execCommand('copy');
    halfmoon.initStickyAlert({
      content: 'Link copied',
      alertType: 'alert-success',
      fillType: 'filled-lm',
    });
  } else {
    const longURL = document.querySelector('#link-input').value;
    // basic URL validation
    if (longURL.includes('https://') || longURL.includes('http://')) {
      shorten(longURL);
    } else {
      document.querySelector('#link-input').classList.add('is-invalid');
      // sending invalid URL alert
      halfmoon.initStickyAlert({
        content: 'Enter a valid URL',
        alertType: 'alert-danger',
        fillType: 'filled-lm',
      });
    }
  }
};

// helper function for passing error
function get_error(identifier) {
  messages = {
    DATA_ERROR: 'URL data is required',
    URL_ERROR: 'That URL is invalid',
    DUPLICATE_ERROR: "That's already an Abbrefy link",
  };
  return messages[identifier];
}

// sending request to abbrefy the longURL
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
    halfmoon.initStickyAlert({
      content: get_error(response.error),
      alertType: 'alert-danger',
      fillType: 'filled-lm',
    });
  } else {
    document.querySelector('#link-input').value = response.url;
    button.textContent = 'Copy';
    button.classList.add('copy');
  }
}
