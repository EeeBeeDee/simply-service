# TESTING

## Validation and Linting 

### HTML

[W3C - HTML](https://validator.w3.org/)

The website was run through the validator by URL instead of file to avoid issues with Djangos variables and extends used in its templates.

A strange warning appeared on some pages where it says there is no lang attribute on some pages. I have also included a picture of the source code from the browser to show it is there but other than that the only warning is a script type reference which is part of MDBs cdn. 

Please find all HTML validation screenshots [here.](/documentation/HTML-VALIDATION.md)

---


### CSS

[Jigsaw - CSS](https://jigsaw.w3.org/css-validator/)

The website only one CSS files. Most flags are due to vendor extensions and the fact CSS variables are not statically checked.

I have included it here in this TESTING file as there is only one.

<details> 
<summary>
style.css
</summary>

![style.css](/documentation/jigsaw-style.css.png)
</details>


--- 

### JavaScript

[JSHint - JS](https://jshint.com/)

The website features one small JS file. app.js controls the message alerts.

I have included it here is this TESTING file as there is only one.



<details> 
<summary>
app.js
</summary>

![app.js](/documentation/jshint-app.js.png)
</details>


---

### Python 

[CI Linter](https://pep8ci.herokuapp.com/)

All files were passed through Code Institutes liniting app which were all returned as PEP8 compliant. 

You can find Screenshots of all validation [Here.](/documentation/PEP8-VALIDATION.md)

---

## Bugs & Issues

### Slow homepage load

I found that on first load, the homepage loaded quite slowly. I finally found that the size of all images were over 2mb each and the resolution was very high. I resized all images using GIMP image editor and noticed a marked improvement. Not fully satisfied, after a bit of research I found that the dev tools' built in performance insight would be a good indication if the speed was good enough now.

As seen below. the Largest Contentful Paint (LCP), Time To Interactive (TTI) and First Contentful Paint (FCP) all managed more than a passing score and DOM Content Loaded (DCL) was within an acceptable time frame.

![performance insight](/documentation/performance-insight.png)

### Contrast Issues

Contrast was an issue flagged in my last submission and I wanted to find the best tool to help me with this, as my usual way of using Inspect on elements was not working on all my text and I feel this was how it potentially slipped past me in the first place. I assume it might have to do with the decent amount of backgrounds I have in this project with an Alpha value lower than 1.

Again my search brought me to another built in tool in chromes Devtools, CSS Overview. Running its diagnostic test, it flagged 3 issues. 2 of which I have fixed and pulled the text contrast ratios up to at least a AA standard. The last one as seen below as the element I have highlighted in the picture, it seems to be connected to the animated text which is white itself but appears on that blue overlay, not the white that the diagnostic clams is its background.  

![CSS Overview](/documentation/css-overview-contrast.png)

---

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