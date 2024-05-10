[![Releases](https://img.shields.io/pypi/v/st-paywall)](https://pypi.org/project/st-paywall/)

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://subscription.streamlit.app)

Author: [@valantoni](https://instagram.com/tonidevpy)


## Installation

```sh
pip install google-auth-st
```


<p>&nbsp;</p>

# 🔐 google-auth-st

<strong>A python package for adding google auth to your streamlit apps! </strong>

## Documentation

Once you configure the authentication on `st.secrets`, you can use the the library methods to conditionally render the content of the page:

```python
from google_auth_st import add_auth

add_auth()

#after authentication, the email is stored in session state
st.write(st.session_state.email)

```

This package expects that you have a `.streamlit/secrets.toml` file which you will have to create. Inside it, you will need to add Google API information that runs the authentication parts of the package. If you already have all of your information for authentication providers, here is how the package expects your secrets file to look.

```toml
redirect_uris = "http://localhost:8501/"
testing_mode = true
client_id = ''
client_secret = ''
redirect_url_test = 'http://localhost:8501/'
redirect_url = "https://your_app_url..."
```


### Feedback:

If you have feedback about this package, please reach out to me on [instagram](https://instagram.com/tonidevpy).