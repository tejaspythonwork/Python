// policies/static/js/validate.js
document.getElementById("policyForm").onsubmit = function () {
    var policy = document.getElementById("policy").value;
    if (policy === "") {
        alert("Please select a policy.");
        return false;
    }
    return true;
}
