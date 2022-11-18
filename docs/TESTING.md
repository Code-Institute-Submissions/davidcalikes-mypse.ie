# Testing

## Tests during development

### User Story Tests

I tested each of my user stories by adding an acceptance criteria to each card of each of the four sprint boards I created as part of the Agile planning process. 

No story could move to the 'done' column of each Kanban board unless all tasks had been completed and the criteria had been met.

<img src="../docs/testing_images/testing_us1.png"><br>
_User Story Screenshot_ 

<img src="../docs/testing_images/testing_us2.png"><br>
_Bug Screenshot_ 

All of the user story acceptance criteria can be inspected via the four Sprint boards I have linked to in the [AGILE](../docs/AGILE.md) documentation.

<br>

## Manual Testing

Each page, feature and link of the application has been rigorously tested.
I have used dropdown menus for each page to make the documentation more human readable.

Each link was tested for each user type and was marked 'pass' when the following expected behaviour was produced via clickable link.

Home Page Testing

* Login Redirect -- The user is directed to the correct page depending on the users authentication status upon login or when the login links in the homepage cards are clicked.

* Can Access About Page -- The user can access the about page from the home page.

* Can Access Login Page -- The user can access the login page via the nav bar.

* Can Access Logout Page -- The user can access the logout page via the nav bar.

* Card Links -- The user is redirected to the login page if not authenticated or redirected to correct landing page for user type if authenticated if login card link is clicked. The user can access the about page from the about card link.

* Can open footer links -- Footer links open in a new tab.

Below are the testing tables for the home page.

| Logged in as  | Login Redirect             | Can Access About Page | Can Access Login | Can Access Logout | Can Access Register  | Card Links                   | Can open Footer Links (new tab) |
|---------------|----------------------------|-----------------------|------------------|-------------------|----------------------|------------------------------|---------------------------------|
| Not Logged In | N/A                        | pass                  | yes/pass         | no/pass           | yes/pass             | login-login-about/pass       | yes/pass                        |
| Admin         | home                       | pass                  | no/pass          | yes/pass          | no/pass              | home-home-about/pass         | yes/pass                        |
| School        | Enrolled Pupil List/pass   | pass                  | no/pass          | yes/pass          | no/pass              | redirect-redirect-about/pass | yes/pass                        |
| Pupil         | Pupil Check/pass           | pass                  | no/pass          | yes/pass          | no/pass              | redirect-redirect-about/pass | yes/pass                        |
| Parent        | Passport List/pass         | pass                  | no/pass          | yes/pass          | no/pass              | redirect-redirect-about/pass | yes/pass                        |
| Teacher       | Teacher Passport List/pass | pass                  | no/pass          | yes/pass          | no/pass              | redirect-redirect-about/pass | yes/pass                        |

Home page validator testing.


## Bugs

### Bugs found during development

After I imported django allauth I recieved the following error.

<img src="../docs/testing_images/testing_error_1_allauth.png"><br>
_ProgrammingError Screenshot_

I searched for and found a solution to this issue on Stack Overflow.

<img src="../docs/testing_images/testing_error_1_allauth_fix_1.png"><br>
_ProgrammingError Stack Overflow Screenshot_ 

<img src="../docs/testing_images/testing_error_1_allauth_fix2.png"><br>
_ProgrammingError Bugfix Screenshot_ 

Migrating sites fixed the error.

<br>

The next bug I found during development took the form of a 'NoReverseMatch' error. 

<img src="../docs/testing_images/testing_error_4_typo_screen.png"><br>
_NoReverseMatch Bug Screenshot_ 

This was simply a typo in the Login Redirect setting.

<img src="../docs/testing_images/testing_error_4_typo_fix.png"><br>
_NoReverseMatch Bug Screenshot_ 

I fixed the typo to correct the error.

<br>

By far the most difficult error I had during development was when attempting to develop the update record view. This is the message that was returned.

<img src="../docs/testing_images/testing_error_pk_error.png"><br>
_AttributeError Screenshot_

This was caused by the incorrect syntax being used in the URL configuration.

I resolved this issue by contacting the Code Institute's tutor support and was given assistance by Ger.

<img src="../docs/testing_images/testing_error_pk_error_fix.png"><br>
_Transcript from Code Institute tutor support_

I was somewhat heartend to hear that this problem was an unusual issue and it took an experienced developer a bit of time to reach a resolution.
Because of the nature and scope of this project, I was less concerned about trying to solve every issue by myself. If anything feel I probably spent too long working on this error before asking for help. It is a trait I will concentrate on as I continue my journey as a junior developer. 

<br>

Another problem was encountered when, the pupil record template returned this 404 error.
<img src="../docs/testing_images/testing_bug2_er.png"><br>
_404 Error Screenshot_ 

I examined the code block and it seemed to be because the pupil ID number began with zero and the database was dropping the leading zero.

<img src="../docs/testing_images/testing_bug2.png"><br>
_404 Bug Screenshot_ 

<img src="../docs/testing_images/testing_bug2b.png"><br>
_404 Pupil ID begins with zero_

I fixed this bug by re-configuring the fields REGEX validator to only accept digits 1-9 for the first digit of a pupil ID number.

<img src="../docs/testing_images/testing_bug2_fix.png"><br>
_404 Bugfix Screenshot_ 

I then used the Admin panel to remove any instances that began with zero.

<br>

I recieved this NameError when developing the MVT relationships to access passports.

<img src="../docs/testing_images/testing_bug4.png"><br>
_NameError Passport Bug Screenshot_

This error was caused by a missing module at the top of views.py

<img src="../docs/testing_images/testing_bugfix4.png"><br>
_NameError Passport Bugfix Screenshot_

I fixed this by importing the passport model at the top of views.py

<br>

I found and fixed a bug caused by a typo in the passport detail template. A miss-typed field name was the cause of the missing text.

<img src="../docs/testing_images/testing_bug1.png"><br>
_Typo Bug Screenshot_ 

<img src="../docs/testing_images/testing_bug1fix.png"><br>
_Typo Bugfix Screenshot_ 

<br>

The next 404 error was trying returned when I tried to access a pupil passport.

<img src="../docs/testing_images/testing_bug3.png"><br>
_404 Passpory Bug Screenshot_ 

This error was caused by a missing curly brace.

<img src="../docs/testing_images/testing_bugfix3.png"><br>
_404 Passport Bug Screenshot_ 

I fixed this by adding the missing symbol.

<br>


### JavaScript Testing

I used the console in google development tools to test my custom JavaScript code. I used the console log to return values and data types. I also used alert messages when developing MyPSE.ie's check id functions.

<img src="../docs/testing_images/testing_js_alert.png"><br>
_Alert raised to signify JS function is working_ 

A particularly annoying bug was found when I recieved an element not found error in the console.

<img src="../docs/testing_images/testing_js_missing_element.png"><br>
_Using console logs to squash a bug_ 

This was simply down to a rougue space as seen in the image below.

<img src="../docs/testing_images/testing_js_missing_element_fix.png"><br>
_Using console logs to squash a bug_ 

<br>


### Responsiveness Testing

I physically tested the responsiveness of the application across the following devices.

Macbook Pro 13 (OSX High Sierra): Chrome, Safari and Firefox

<img src="../docs/testing_images/testing_resp1.png"><br>
_Screenshot from Macbook Pro: Chrome_ 

<img src="../docs/testing_images/testing_resp2.png"><br>
_Screenshot from Macbook Pro: Safari_ 

A this was my development machine, I also used it to test responsiveness across a full range of devices using Google's Development tools.

<img src="../docs/testing_images/testing_resp3.png"><br>
_Screenshot from Macbook Pro: Safari_ 

iPhone XR Chrome, Safari

<img src="../docs/testing_images/testing_resp4.png"><br>
_MyPSE on iPhone XR_

Huawei P20 Pro (Android) Chrome, Firefox

<img src="../docs/testing_images/testing_resp5.png"><br>
_Screenshot from on Huawei P20 Pro: Chrome_

iPad Mini 5 Chrome, Safari, Firefox

<img src="../docs/testing_images/testing_resp6.png"><br>
_MyPSE on iPad Mini 5: Firefox_

HP Pavillion Notebook (Windows 10) Chrome, Safari

## Practical Testing

The app was tested for practical use by a School administrator by Susan Hynes, secretary of St Mary's Special School, Drumcar.

During testing, Susan found the following bug.

<img src="../docs/testing_images/testing_bug_susan.png"><br>
_Bug found by Susan Hynes during practical testing_

The pupil record form would not accept a lowercase letter as the final character of a school roll number.

<img src="../docs/testing_images/testing_bugfix_susan.png"><br>
_Bugfix School Roll Number_

This bug was fixed by altering the REGEX validator code for the School Roll no form field to allow lowercase letters.





