function setId() {
    let pupilId= document.getElementById("valid-pupil-id").innerHTML
    localStorage.setItem("id", pupilId);
}

function validateForm() {
    let pupilId = document.forms["form"]["pupil_id"].value;
    console.log(document.forms["form"]["pupil_id"].value)
    let storedId = localStorage.getItem("id");
        if (pupilId !=  storedId) {
        alert("Incorrect ID");
        return false;
        } else {
        return true;
  }
}