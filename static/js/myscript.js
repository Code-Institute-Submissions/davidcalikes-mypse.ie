function applyId() {
    alert('ID Applied');
    let pupilId= document.getElementById("set-edit-pupil-id").innerHTML
    console.log(pupilId)
    localStorage.setItem("id", pupilId);
}

function notFound() {
    let pupilPassport= document.getElementById("valid-id").innerHTML
    console.log(pupilPassport)
    if (typeof pupilPassport == "undefined") {
    alert("No matching id found!");
    }
}

function setValidPupilCheckId() {
    let pupilId= document.getElementById("valid-pupil-check-id").innerHTML
    localStorage.setItem("id", pupilId);
}

function setValidatePupilId() {
    let pupilId= document.getElementById("valid-pupil-id").innerHTML
    localStorage.setItem("id", pupilId);
}

function setEditPupilId() {
    let pupilId= document.getElementById("set-edit-pupil-id").innerHTML
    localStorage.setItem("id", pupilId);
}

function setTeacherId() {
    let teacherId= document.getElementById("set-teacher-id").innerHTML
    console.log(teacherId)
    localStorage.setItem("id", teacherId);
}

function validateTeacher() {
    let teacherId= document.getElementById("passport-teacher-id").innerHTML
    console.log(teacherId)
    let storedId = localStorage.getItem("id");
    console.log(storedId)
        if (teacherId !==  storedId) {
        alert("Incorrect Teacher ID!");
        window.history.back();
        return false;
        } else {
        document.getElementById("passport-blur").style.filter = "blur(0px)";
        alert("Teacher Id Is Valid!")
        return true;
  }
}

function validateForm() {
    let pupilId = document.forms["form"]["pupil_id"].value;
    console.log(document.forms["form"]["pupil_id"].value)
    let storedId = localStorage.getItem("id");
    console.log(storedId)
        if (pupilId !==  storedId) {
        alert("Incorrect ID");
        return false;
        } else {
        return true;
    }
}