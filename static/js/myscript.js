/*exported applyId, setValidatePupilId, setTeacherId,	validateTeacher, validateForm */

/**
 * To Ensure Pupil ID cannot be changed from the one initially submitted.
 * Used when initially creating a passport.
 * Gets Pupil ID from DOM and uses Local Storage to store value in client Browser.
 * Fired via onclick event from the 'add passport' link of the validate pupil id page.
 * */
 function setValidatePupilId() {
    let pupilId= document.getElementById("valid-pupil-id").innerHTML;
    localStorage.setItem("id", pupilId);
}

/** 
 * Gets Pupil ID from DOM and uses Local Storage to store value in client Browser.
 * Used when editing a passport.
 * Fired from 'Edit Passport' onclick event in Passport Detail page.
 * */
function applyId() {
    let pupilId= document.getElementById("set-edit-pupil-id").innerHTML;
    localStorage.setItem("id", pupilId);
}

/** 
 * Displays 'Loading' modal that informs the user a form is being submitted.
 * Fired from validateForm function.
 * */
function loadingModal() {
document.getElementById("loading").style.display = "block";
}

/** 
 * Gets Teacher ID from DOM and uses Local Storage to store value in client Browser.
 * Used when teacher user attempts to access passport.
 * Fired from 'Edit Passport' onclick event in Passport Detail page.
 * */
function setTeacherId() {
    let teacherId= document.getElementById("set-teacher-id").innerHTML;
    localStorage.setItem("id", teacherId);
}

/** 
 * Ensures teacher ID matches that of teacher id in passport.
 * Used when teacher user attempts to access passport.
 * Fired from 'teacher validate pupil id page' onclick event.
 * */
function validateTeacher() {
    let teacherId= document.getElementById("passport-teacher-id").innerHTML;
    let storedId = localStorage.getItem("id");
        if (teacherId !==  storedId) {
        alert("Incorrect Teacher ID! Teacher ID must match one given after login");
        window.history.back();
        return false;
        } else {
        document.getElementById("floating-button").style.display = "none";
        document.getElementById("passport-blur").style.filter = "blur(0px)";
        return true;
  }
}

/** 
 * Ensures Pupil ID matches that of Pupil id previously submitted.
 * Used when pupil/parent user changes deviates from their assigned ID
 * Fired from passport fom sumbit button via onclick event.
 * */
function validateForm() {
    let pupilId = document.forms.form.pupil_id.value;
    let storedId = localStorage.getItem("id");
        if (pupilId !==  storedId) {
        alert("Incorrect Pupil ID! Pupil ID must match one given during authoristation check");
        return false;
        } else {
        loadingModal();
        return true;
    }
}