# TESTING

## Validation and Linting 

### HTML

[W3C - HTML](https://validator.w3.org/)

The website was run through the validator by URL instead of file to avoid issues with Djangos variables and extends used in its templates.

A strange warning appeared on some pages where it says there is no lang attribute on some pages. I have also included a picture of the source code from the browser to show it is there but other than that the only warning is a script type reference which is part of MDBs cdn. 

Please find all HTML validation screenshots [here.](/documentation/HTML-VALIDATION.md)

### CSS

[Jigsaw - CSS](https://jigsaw.w3.org/css-validator/)

The website only has two CSS files. One of which Jigsaw could not find by URI for whatever reason, so I had to use direct input to validate the other. Most flags are due to vendor extensions and the fact CSS variables are not statically checked.

I have included them here in this TESTING file as there is only two.

#### style.css
![style.css](/documentation/jigsaw-style.css.png)

#### bookings-style.css
![bookings-style.css](/documentation/jigsaw-bookings-style.css.png)

### JavaScript

[JSHint - JS](https://jshint.com/)

The website features two small JS files app.js controls the message alerts while bookings-app.js controls what dates can be picked while booking.

I have included them here is this TESTING file as there is only two.

#### app.js
![app.js](/documentation/jshint-app.js.png)

#### bookings-app.js
![app.js](/documentation/jshint-bookings-app.js.png)

### Python 

[CI Linter](https://pep8ci.herokuapp.com/)

All files were passed through Code Institutes liniting app which were all returned as PEP8 compliant. 

You can find Screenshots of all validation [Here.](/documentation/PEP8-VALIDATION.md)

## Manual Testing 

### Homepage & Nav

Feature Tested | Expected Result | Pass/Fail
---------------|-----------------|-----------
Homepage background img responsiveness | Img and filter look and size correct at all widths | &check;
Hero responsiveness | Hero blurb resizes accordingly | &check;
Restaurant cards | cards resize and change flex direction at breakpoint | &check;
Footer responsiveness | Footer is sized correctly at all widths down to 350px | &check;
Navbar options | Navbar options changed depending on users logged in/out status | &check;
Navbar responsiveness | At mobile sizes hamburger menu is present | &check;

### Accounts 

Feature Tested | Expected Result | Pass/Fail
---------------|-----------------|-----------
Registration | A new account can be made with the site | &check;
Login | An already registered account can be logged into | &check;
Logout | A user can log out of the account they are signed into | &check;

### Booking

Feature Tested | Expected Result | Pass/Fail
---------------|-----------------|-----------
Login required | logged in status required to make booking | &check;
Form input | All relevant form inputs correspond to DB model | &check;
Date Picker | Days previous to current cannot be selected | &check;
Slug creation | Any booking made auto generates a slug to be used for its own booking page | &check;

### Reservations 

Feature Tested | Expected Result | Pass/Fail
---------------|-----------------|-----------
Login required | logged in status required to view reservations page | &check;
All bookings viewable | You can see the full list of users bookings | &check;
Book now btn | you can book from reservations screen | &check;
View single booking | Click into each booking for more detail | &check;
Update booking | Bookings can be changed and updated | &check;
Delete booking | Bookings can be deleted | &check;
Update redirect | User brought back to individual booking page after updating | &check;
Delete redirect | User brought back to your bookings page after deleting a booking | &check;
Messages | after deleting or updating user given a message to confirm | &check;