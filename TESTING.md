# TESTING

## Validation and Linting 

[W3C - HTML](https://validator.w3.org/)


The website was run through the validator by URL instead of file to avoid issues with Djangos variables and extends used in its templates.

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
Update booking | bookings can be changed and updated | &check;
Delete booking | bookings can be deleted |&check;